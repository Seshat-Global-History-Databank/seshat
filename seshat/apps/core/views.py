from django.apps import apps
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import F, Value, Q, Count
from django.db.models.functions import Replace
from django.http import (
    HttpResponse,
    Http404,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.http import require_GET
from django.views.generic import (
    View,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
    RedirectView,
)
from django.views.generic.edit import FormMixin

import json
import sys

from ..accounts.models import Seshat_Expert
from ..crisisdb.models import (
    Power_transition,
    Crisis_consequence,
)
from ..general.models import (
    Polity_duration,
    Polity_preceding_entity,
    Polity_research_assistant,
)
from ..constants import (
    BASIC_CONTEXT,
    ZOTERO,
    US_STATES_GEOJSON_PATH,
)
from ..utils import (
    get_models,
    get_api_results,
    get_all_data,
)

from .forms import (
    CapitalForm,
    CitationForm,
    CommentPartFormSet,
    NgaForm,
    PolityForm,
    PolityUpdateForm,
    ReferenceForm,
    ReferenceFormSet10,
    ReferenceFormSet2_UPGRADE,
    ReferenceFormSet2,
    ReferenceFormSet5,
    ReligionForm,
    SeshatCommentForm,
    SeshatCommentForm2,
    SeshatCommentPartForm,
    SeshatCommentPartForm10,
    SeshatCommentPartForm2_UPGRADE,
    SeshatCommentPartForm2,
    SeshatCommentPartForm5,
    SeshatPrivateCommentForm,
    SeshatPrivateCommentPartForm,
    SignUpForm,
    VariablehierarchyFormNew,
)
from .models import (
    Capital,
    Citation,
    Macro_region,
    Nga,
    Polity,
    Reference,
    Religion,
    ScpThroughCtn,
    Section,
    Seshat_region,
    SeshatComment,
    SeshatCommentPart,
    SeshatPrivateComment,
    SeshatPrivateCommentPart,
    Subsection,
    Variablehierarchy,
)
from .tokens import account_activation_token
from .constants import (
    CUSTOM_ORDER,
    CUSTOM_ORDER_SR,
    WORLD_MAP_INITIAL_DISPLAYED_YEAR,
    WORLD_MAP_INITIAL_POLITY,
)
from .specific_constants.zotero import (
    MANUAL_IMPORT_REFS,
    NLP_ZOTERO_LINKS_TO_FILTER,
)
from .utils import (
    common_map_view_content,
    do_zotero_manually,
    do_zotero,
    get_data_for_polity,
    get_model_data,
    get_polity_app_data,
    get_polity_shape_content,
    get_provinces,
    random_polity_shape,
    update_citations_from_inside_zotero_update,
)


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        # Get the basic context
        context = BASIC_CONTEXT

        # Get region objects
        seshat_regions = Seshat_region.objects.annotate(
            num_polities=Count("home_seshat_region")
        ).exclude(name="Somewhere")

        macro_regions = Macro_region.objects.exclude(name="World")
        polities = Polity.objects.all()

        seshat_region_count = seshat_regions.count()
        macro_region_count = macro_regions.count()
        polity_count = polities.count()

        # Update the context with counts and queryset data
        context.update(
            {
                "sr_data": [seshat_region_count, macro_region_count],
                "pols_data": [polity_count, seshat_region_count],
                "eight_pols": Polity.objects.order_by("?")[:8],
                "eight_srs": seshat_regions.order_by("-num_polities")[:8],
            }
        )

        # Loop through apps and get their models and data
        for app_name in ["general", "sc", "wf", "crisisdb"]:
            models = get_models(app_name, exclude=["Ra"])

            unique_polities = set()
            variable_count = 0
            row_count = 0

            app_key = f"{app_name}_data"

            for model in models:
                model_name = model.__name__

                queryset = model.objects.all()

                if model_name.startswith("Us_violence"):
                    context.update(
                        {
                            "us_data": [
                                queryset.count(),
                                1,
                            ],
                            "eight_uss": queryset.order_by("?")[:8],
                        }
                    )
                    continue

                if model_name.startswith("Us_"):
                    continue

                polities = queryset.values_list("polity", flat=True).distinct()

                if model_name.startswith("Power_transition"):
                    context.update(
                        {
                            "pt_data": [
                                queryset.count(),
                                1,
                                polities.count(),
                            ],
                            "eight_pts": queryset.order_by("?")[:8],
                        }
                    )
                    continue

                if model_name.startswith("Crisis_consequence"):
                    context.update(
                        {
                            "cc_data": [
                                queryset.count(),
                                1,
                                polities.count(),
                            ],
                            "eight_ccs": queryset.order_by("?")[:8],
                        }
                    )
                    continue

                if model_name.startswith("Human_sacrifice"):
                    context.update(
                        {
                            "hs_data": [
                                queryset.count(),
                                1,
                                polities.count(),
                            ],
                            "eight_hss": queryset.order_by("?")[:8],
                        }
                    )
                    continue

                unique_polities.update(
                    queryset.values_list("polity", flat=True).distinct()
                )

                variable_count += 1
                row_count += queryset.count()

            context.update(
                {
                    app_key: [
                        row_count,
                        variable_count,
                        len(unique_polities),
                    ],
                }
            )

        return context


class ReligionListView(ListView):
    """
    List all religions.
    """

    model = Religion
    template_name = "core/religion_list.html"
    context_object_name = "religions"
    ordering = ["religion_name"]
    permission_required = "core.add_seshatprivatecommentpart"


class ReferenceListView(ListView):
    """
    List all references.
    """

    model = Reference
    template_name = "core/references/reference_list.html"
    paginate_by = 20

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("references")

    def get_queryset(self):
        """
        Get the queryset of references.

        Returns:
            QuerySet: The queryset of references.
        """
        return Reference.objects.exclude(creator="MAJIDBENAM").all()


class NlpReferenceListView(ListView):
    """
    List all NLP references.
    """

    model = Reference
    template_name = "core/references/nlp_reference_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Return the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("nlp-references")

    def get_queryset(self):
        """
        Return the queryset of NLP references.

        Returns:
            QuerySet: The queryset of NLP references.
        """
        return (
            # Use the imported list of Zotero links to filter references
            Reference.objects.filter(
                zotero_link__in=NLP_ZOTERO_LINKS_TO_FILTER
            )
            # Exclude references with 'year' less than or equal to 0
            .filter(year__gt=0)
            # Replace underscores in 'creator' with spaces
            .annotate(
                creator_with_spaces=Replace("creator", Value("_"), Value(" "))
            )
            # Replace "_et_al" at the end of 'creator' with ", ..."
            .annotate(
                creator_cleaned=Replace(
                    F("creator_with_spaces"), Value(" et al"), Value(", ...")
                )
            )
            # Order by year, descending, then by title
            .order_by("-year", "title")
        )


class ReferenceCreateView(PermissionRequiredMixin, CreateView):
    """
    Create a new reference.
    """

    model = Reference
    form_class = ReferenceForm
    template_name = "core/references/reference_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("reference-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        # TODO: Can this be removed as it looks like it doesn't communicate any valuable
        # information to the template?
        context = dict(
            context,
            **{
                "mysubsection": "abc",
                "myvar": "def reference",
                "errors": "Halooooooooo",
            },
        )

        return context

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse("index"))


class ReferenceUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Update a reference.
    """

    model = Reference
    form_class = ReferenceForm
    template_name = "core/references/reference_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        # TODO: Can this be removed as it looks like it doesn't communicate any valuable
        # information to the template?
        context = dict(
            context,
            **{
                "mysubsection": "No Subsection Proeeeevided",
                "myvar": "Reference Daeeeeta",
            },
        )

        return context


class ReferenceDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Delete a reference.
    """

    model = Reference
    success_url = reverse_lazy("references")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class ReferenceDetailView(DetailView):
    """
    Display the details of a reference.
    """

    model = Reference
    template_name = "core/references/reference_detail.html"


class CitationListView(ListView):
    """
    List all citations.
    """

    model = Citation
    template_name = "core/references/citation_list.html"
    paginate_by = 20

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("citations")


class CitationCreateView(
    PermissionRequiredMixin, SuccessMessageMixin, CreateView
):
    """
    Create a new citation.
    """

    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_form.html"
    permission_required = "core.add_capital"
    success_message = "The citation has successfully been added."

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        context = self.get_context_data(form=form)
        context.update({"my_message": "Something went wrong"})
        return self.render_to_response(context)

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("citation-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        # TODO: Can this be removed as it looks like it doesn't communicate any valuable
        # information to the template?
        context = dict(
            context,
            **{
                "mysubsection": "abc",
                "myvar": "def citation",
                "errors": "Halooooooooo",
            },
        )

        return context


class CitationUpdateView(
    PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    """
    Update a citation.
    """

    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_update.html"
    permission_required = "core.add_capital"
    success_message = "The citation has successfully been updated."

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        context = self.get_context_data(form=form)
        context.update({"my_message": "Something went wrong"})
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        # TODO: Can this be removed as it looks like it doesn't communicate any valuable
        # information to the template?
        context = dict(
            context,
            **{
                "mysubsection": "No Subsection Proeeeevided",
                "myvar": "Citation Data xyz",
            },
        )

        return context


class CitationDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Delete a citation.
    """

    model = Citation
    success_url = reverse_lazy("citations")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CitationDetailView(DetailView):
    """
    Display the details of a citation.
    """

    model = Citation
    template_name = "core/references/citation_detail.html"


class SeshatCommentListView(ListView):
    """
    List all comments.
    """

    model = SeshatComment
    template_name = "core/seshatcomments/seshatcomment_list.html"
    paginate_by = 20

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("seshatcomments")


class SeshatCommentCreateView(PermissionRequiredMixin, CreateView):
    """
    Create a new comment.
    """

    model = SeshatComment
    form_class = SeshatCommentForm
    template_name = "core/seshatcomments/seshatcomment_form.html"  # noqa: E501  TODO: This template file is marked as missing
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("seshatcomment-create")

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse("index"))


class SeshatCommentUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Update a comment.
    """

    model = SeshatComment
    form_class = SeshatCommentForm
    template_name = "core/seshatcomments/seshatcomment_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        app_labels = ["rt", "general", "sc", "wf", "crisisdb"]
        apps_models = {name: apps.all_models[name] for name in app_labels}

        my_app_models = []
        for _, models in apps_models.items():
            for mm, model in models.items():
                if hasattr(model, "comment") and all(
                    [
                        "_citations" not in mm,
                        "_curator" not in mm,
                        not mm.startswith("us_"),
                        model.objects.filter(comment=self.object.id),
                    ]
                ):
                    obj = model.objects.get(comment=self.object.id)

                    try:
                        var_name = obj.clean_name_spaced()
                    except AttributeError:
                        var_name = obj.name

                    my_app_models.append(
                        {
                            "my_polity": obj.polity,
                            "my_value": obj.show_value,
                            "my_year_from": obj.year_from,
                            "my_year_to": obj.year_to,
                            "my_tag": obj.get_tag_display(),
                            "my_var_name": var_name,
                            "my_polity_id": obj.polity.id,
                        }
                    )

        context["my_app_models"] = my_app_models

        return context


class SeshatCommentDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Delete a comment.
    """

    model = SeshatComment
    success_url = reverse_lazy("seshatcomments")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SeshatCommentDetailView(DetailView):
    """
    Display the details of a comment.
    """

    model = SeshatComment
    template_name = "core/seshatcomments/seshatcomment_detail.html"


class SeshatCommentPartListView(ListView):
    """
    List all comment parts.
    """

    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_list.html"
    paginate_by = 20

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("seshatcommentparts")


class SeshatCommentPartListView3(ListView):
    """
    List all comment parts.
    """

    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_list3.html"
    paginate_by = 20

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("seshatcommentparts3")


class SeshatCommentPartCreateView(PermissionRequiredMixin, CreateView):
    """
    Create a new comment part.
    """

    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_form.html"  # noqa: E501  TODO: This template file is marked as missing
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("seshatcommentpart-create")

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse("index"))


class SeshatCommentPartCreate2(PermissionRequiredMixin, CreateView):
    """
    Create a new comment part.
    """

    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_form_prefilled.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("seshatcommentpart-create2")

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse("index"))

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        logged_in_expert = Seshat_Expert.objects.get(user=self.request.user)

        context = dict(
            context,
            **{
                "com_id": self.kwargs["com_id"],
                "subcom_order": self.kwargs["subcom_order"],
                "comment_curator": logged_in_expert,
                "comment_curator_id": logged_in_expert.id,
                "comment_curator_name": "Selected USER",
            },
        )

        return context


class SeshatPrivateCommentPartCreate2(PermissionRequiredMixin, CreateView):
    """
    Create a new private comment part.
    """

    model = SeshatPrivateCommentPart
    form_class = SeshatPrivateCommentPartForm
    template_name = (
        "core/seshatcomments/seshatprivatecommentpart_form_prefilled.html"
    )
    permission_required = "core.add_seshatprivatecommentpart"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("seshatprivatecommentpart-create2")

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse("index"))

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "private_com_id": self.kwargs.get("private_com_id"),
                "private_comment_owner": Seshat_Expert.objects.get(
                    user=self.request.user
                ),
            },
        )

        return context


class SeshatCommentPartUpdateView(
    PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    """
    Update a comment part.
    """

    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_update.html"
    permission_required = "core.add_capital"
    success_message = "You successfully updated the subdescription."

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        comment_curator = Seshat_Expert.objects.get(user=self.request.user)

        context = dict(
            context,
            **{
                "comment_curator": comment_curator,
                "comment_curator_id": comment_curator.id,
                "comment_curator_name": "Selected USER",
            },
        )

        return context


class SeshatPrivateCommentPartUpdateView(
    PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    """
    Update a private comment part.
    """

    model = SeshatPrivateCommentPart
    form_class = SeshatPrivateCommentPartForm
    template_name = "core/seshatcomments/seshatprivatecommentpart_update2.html"
    permission_required = "core.add_seshatprivatecommentpart"
    success_message = "You successfully updated the Private comment."

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "private_com_id": self.kwargs.get("private_com_id"),
                "pk": self.kwargs.get("pk"),
                "private_comment_owner": Seshat_Expert.objects.get(
                    user=self.request.user
                ),
            },
        )

        return context


class SeshatCommentPartDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Delete a comment part.
    """

    model = SeshatCommentPart

    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"

    def get_success_url(self):
        return reverse_lazy(
            "seshatcomment-update", kwargs={"pk": self.object.comment.pk}
        )


class SeshatCommentPartDetailView(DetailView):
    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_detail.html"


class PolityCreateView(PermissionRequiredMixin, CreateView):
    """
    Create a new Polity.
    """

    model = Polity
    form_class = PolityForm
    template_name = "core/polity/polity_form.html"
    permission_required = "core.add_capital"
    success_url = reverse_lazy("polities")

    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        # Custom validation to check if a Polity with the same new_name already exists
        if Polity.objects.filter(new_name=form.cleaned_data["new_name"]):
            messages.error(
                self.request, "A Polity with this name already exists."
            )
            return self.form_invalid(form)

        # Continue with the default behavior if validation passes
        return super().form_valid(form)

    def form_invalid(self, form):
        # Redirect to the 'polities' page with an error message
        messages.error(
            self.request, "Form submission failed. Please check the form."
        )
        return self.render_to_response(self.get_context_data(form=form))


class PolityUpdateView(
    PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    """
    Update a Polity.
    """

    model = Polity
    form_class = PolityUpdateForm
    template_name = "core/polity/polity_form.html"
    permission_required = "core.add_capital"
    success_message = "You successfully updated the Polity."

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        context = dict(context, **{"pk": self.object.pk})

        return context

    def get_success_url(self):
        return reverse_lazy(
            "polity-detail-main", kwargs={"pk": self.object.pk}
        )


class PolityLightListView(SuccessMessageMixin, ListView):
    """
    List all polities.
    """

    model = Polity
    template_name = "core/polity/polity_list_light.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polities-light")

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        macro_regions = Macro_region.objects.all()
        macro_regions = sorted(
            macro_regions, key=lambda i: CUSTOM_ORDER.index(i.id)
        )

        seshat_regions = Seshat_region.objects.all()
        seshat_regions = sorted(
            seshat_regions, key=lambda i: CUSTOM_ORDER_SR.index(i.id)
        )

        polities = Polity.objects.all().order_by("start_year")

        world_region_dict = {}
        world_region_dict_top = {}
        for macro_region in macro_regions:
            if macro_region not in world_region_dict:
                world_region_dict[macro_region.name] = {}

            if macro_region not in world_region_dict_top:
                world_region_dict_top[macro_region.name] = {}

            for seshat_region in seshat_regions:
                if seshat_region.mac_region_id == macro_region.id:
                    if (
                        seshat_region.name
                        not in world_region_dict[macro_region.name]
                    ):
                        world_region_dict[macro_region.name][
                            seshat_region.name
                        ] = []

                    if (
                        seshat_region.name
                        not in world_region_dict_top[macro_region.name]
                    ):
                        world_region_dict_top[macro_region.name][
                            seshat_region.name
                        ] = [
                            seshat_region.subregions_list,
                            0,
                        ]

        freq_dic = {"pol_count": len(polities), "d": 0}

        for polity in polities:
            if polity.home_seshat_region:
                world_region_dict[polity.home_seshat_region.mac_region.name][
                    polity.home_seshat_region.name
                ].append(polity)

                world_region_dict_top[
                    polity.home_seshat_region.mac_region.name
                ][polity.home_seshat_region.name][1] += 1

            if polity.general_description:
                freq_dic["d"] += 1

        for polity in polities:
            polity.has_g_sc_wf = None

        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "ultimate_wregion_dic": world_region_dict,
                "ultimate_wregion_dic_top": world_region_dict_top,
                "all_pols": polities,
                "all_srs": seshat_regions,
                "pol_count": freq_dic["pol_count"],
                "freq_data": freq_dic,
            },
        )

        return context


class PolityListView(SuccessMessageMixin, ListView):
    """
    List all polities.
    """

    model = Polity
    template_name = "core/polity/polity_list.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polities")

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        macro_regions = Macro_region.objects.all()
        macro_regions = sorted(
            macro_regions, key=lambda item: CUSTOM_ORDER.index(item.id)
        )
        seshat_regions = Seshat_region.objects.all()
        seshat_regions = sorted(
            seshat_regions, key=lambda item: CUSTOM_ORDER_SR.index(item.id)
        )

        polities = Polity.objects.all().order_by("start_year")

        world_region_dict = {}
        world_region_dict_top = {}
        for macro_region in macro_regions:
            if macro_region not in world_region_dict:
                world_region_dict[macro_region.name] = {}

            if macro_region not in world_region_dict_top:
                world_region_dict_top[macro_region.name] = {}

            for seshat_region in seshat_regions:
                if seshat_region.mac_region_id == macro_region.id:
                    if (
                        seshat_region.name
                        not in world_region_dict[macro_region.name]
                    ):
                        world_region_dict[macro_region.name][
                            seshat_region.name
                        ] = []

                    if (
                        seshat_region.name
                        not in world_region_dict_top[macro_region.name]
                    ):
                        world_region_dict_top[macro_region.name][
                            seshat_region.name
                        ] = [
                            seshat_region.subregions_list,
                            0,
                        ]

        all_polities_g_sc_wf, freq_dic = get_polity_app_data(
            Polity, return_all=True
        )
        freq_dic["d"] = 0

        for polity in polities:
            if polity.home_seshat_region:
                world_region_dict[polity.home_seshat_region.mac_region.name][
                    polity.home_seshat_region.name
                ].append(polity)

                world_region_dict_top[
                    polity.home_seshat_region.mac_region.name
                ][polity.home_seshat_region.name][1] += 1

            if polity.general_description:
                freq_dic["d"] += 1

        for polity in polities:
            try:
                polity.has_g_sc_wf = all_polities_g_sc_wf[polity.id]
            except KeyError:
                polity.has_g_sc_wf = None

            all_durations = {
                "intr": [],
                "gv": [],
                "pt": [],
                "color": "xyz",
            }
            all_durations["intr"] = [polity.start_year, polity.end_year]

            # Pol_dur object
            try:
                polity_duration = Polity_duration.objects.get(
                    polity_id=polity.id
                )

                all_durations["gv"] = [
                    polity_duration.polity_year_from,
                    polity_duration.polity_year_to,
                ]
            except:  # noqa: E722  TODO: Don't use bare except
                pass

            # Pow Trans Data
            try:
                power_transitions = Power_transition.objects.filter(
                    polity_id=polity.id
                )

                minima, maxima = [], []
                for power_transition in power_transitions:
                    if power_transition.year_from is not None:
                        minima.append(power_transition.year_from)

                    if power_transition.year_to is not None:
                        maxima.append(power_transition.year_to)

                all_durations["pt"] = [min(minima), max(maxima)]
            except:  # noqa: E722  TODO: Don't use bare except
                pass

            polity.all_durations = all_durations
            if (
                all_durations["intr"]
                and all_durations["gv"]
                and all_durations["pt"]
            ):
                if (
                    all_durations["intr"]
                    == all_durations["gv"]
                    == all_durations["pt"]
                ):
                    polity.color = "ggg"
                elif all_durations["intr"] == all_durations["gv"]:
                    polity.color = "ggr"
                elif all_durations["intr"] == all_durations["pt"]:
                    polity.color = "grg"
                elif all_durations["gv"] == all_durations["pt"]:
                    polity.color = "rgg"
            elif all_durations["intr"] and all_durations["gv"]:
                if all_durations["intr"] == all_durations["gv"]:
                    polity.color = "ggm"
                else:
                    polity.color = "grm"
            elif all_durations["intr"] and all_durations["pt"]:
                if all_durations["intr"] == all_durations["pt"]:
                    polity.color = "gmg"
                elif all_durations["intr"][0] == -10000:
                    polity.color = "rmr"
                else:
                    polity.color = "gmr"
            elif all_durations["intr"] and all_durations["intr"][0] == -10000:
                polity.color = "rmm"
            elif all_durations["intr"]:
                polity.color = "gmm"

        freq_dic["pol_count"] = len(polities)

        context = dict(
            context,
            **{
                "ultimate_wregion_dic": world_region_dict,
                "ultimate_wregion_dic_top": world_region_dict_top,
                "all_pols": polities,
                "all_srs": seshat_regions,
                "pol_count": freq_dic["pol_count"],
                "freq_data": freq_dic,
            },
        )

        return context


class PolityCommentedListView(
    PermissionRequiredMixin, SuccessMessageMixin, ListView
):
    """
    List all polities with comments.
    """

    model = Polity
    template_name = "core/polity/polity_list_commented.html"
    permission_required = "core.add_seshatprivatecommentpart"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polities")

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        polities = Polity.objects.exclude(
            Q(private_comment_n__isnull=True) | Q(private_comment_n=1)
        )

        contain_dic = get_polity_app_data(
            Polity, return_freq=False, return_contain=True
        )

        for polity in polities:
            try:
                polity.has_g_sc_wf = contain_dic[polity.id]
            except KeyError:
                polity.has_g_sc_wf = None

        context = dict(
            context, **{"all_pols": polities, "pol_count": len(polities)}
        )

        return context


class PolityDetailView(SuccessMessageMixin, DetailView):
    """
    Show details of a polity.

    ..
        TODO: This is a looot of pull on the db... how can we make it quicker?
    """

    model = Polity
    template_name = "core/polity/polity_detail.html"

    def get_object(self, queryset=None):
        """
        Get the object of the view.

        Args:
            queryset: The queryset to use.

        Returns:
            Polity: The object of the view.

        Raises:
            Http404: If no polity matches the given name/ID.
            Http404: If multiple polities are found with the same name.
        """
        if "pk" in self.kwargs:
            return get_object_or_404(Polity, pk=self.kwargs["pk"])

        if "new_name" in self.kwargs:
            # Attempt to get the object by new_name, handle multiple objects returned
            try:
                return Polity.objects.get(new_name=self.kwargs["new_name"])
            except Polity.MultipleObjectsReturned:
                # Handle the case of multiple objects with the same new_name
                raise Http404("Multiple objects with the same new_name")
            except Polity.DoesNotExist:
                # Handle the case where no object with the given new_name is found
                raise Http404("No Polity matches the given new_name")

        return None

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        all_data = get_data_for_polity(
            self.object.pk,
            "crisisdb",
            ["Arable_land", "Agricultural_population", "Human_sacrifice"],
        )
        _, all_general_data = get_all_data("general", self.object.pk)
        _, all_sc_data = get_all_data("sc", self.object.pk)
        _, all_wf_data = get_all_data("wf", self.object.pk)
        _, all_rt_data = get_all_data("rt", self.object.pk)

        context = dict(
            context,
            **{
                "pk": self.object.pk,
                "all_data": all_data,
                "all_general_data": all_general_data,
                "all_sc_data": all_sc_data,
                "all_wf_data": all_wf_data,
                "all_rt_data": all_rt_data,
                "all_crisis_cases_data": get_model_data(
                    Crisis_consequence, self.object.pk, True
                ),
                "all_power_transitions_data": get_model_data(
                    Power_transition, self.object.pk
                ),
            },
        )

        try:
            research_assistants = Polity_research_assistant.objects.filter(
                polity_id=self.object.pk
            )
            research_assistant_ids = research_assistants.values_list(
                "polity_ra_id", flat=True
            )

            experts = Seshat_Expert.objects.filter(
                id__in=research_assistant_ids
            )
            all_research_assistants = [
                f"{expert.user.first_name} {expert.user.last_name}"
                for expert in experts
            ]

            context = dict(
                context,
                **{
                    "all_Ras": ", ".join(all_research_assistants),
                },
            )

        except:  # noqa: E722  TODO: Don't use bare except
            context = dict(
                context,
                **{
                    "all_Ras": "",
                },
            )

        # Get the related data
        all_durations = {
            "intr": [self.object.start_year, self.object.end_year],
            "gv": [],
            "pt": [],
            "color": "xyz",
        }

        # Pol_dur object
        try:
            polity_duration = Polity_duration.objects.get(
                polity_id=self.object.pk
            )

            all_durations["gv"] = [
                polity_duration.polity_year_from,
                polity_duration.polity_year_to,
            ]
        except Polity_duration.DoesNotExist:
            pass

        # Pow Trans Data
        try:
            power_transitions = Power_transition.objects.filter(
                polity_id=self.object.pk
            )

            minima, maxima = [], []
            for power_transition in power_transitions:
                if power_transition.year_from is not None:
                    minima += [power_transition.year_from]

                if power_transition.year_to is not None:
                    maxima += [power_transition.year_to]

            all_durations["pt"] = [min(minima), max(maxima)]
        except Power_transition.DoesNotExist:
            pass

        if all(
            [all_durations["intr"], all_durations["gv"], all_durations["pt"]]
        ):
            if (
                all_durations["intr"]
                == all_durations["gv"]
                == all_durations["pt"]
            ):
                all_durations["color"] = "ggg"
            elif all_durations["intr"] == all_durations["gv"]:
                all_durations["color"] = "ggr"
            elif all_durations["intr"] == all_durations["pt"]:
                all_durations["color"] = "grg"
            elif all_durations["gv"] == all_durations["pt"]:
                all_durations["color"] = "rgg"
        elif all([all_durations["intr"], all_durations["gv"]]):
            if all_durations["intr"] == all_durations["gv"]:
                all_durations["color"] = "ggm"
            else:
                all_durations["color"] = "grm"
        elif all([all_durations["intr"], all_durations["pt"]]):
            if all_durations["intr"] == all_durations["pt"]:
                all_durations["color"] = "gmg"
            elif all_durations["intr"][0] == -10000:
                all_durations["color"] = "rmr"
            else:
                all_durations["color"] = "gmr"
        elif all([all_durations["intr"], all_durations["intr"][0] == -10000]):
            all_durations["color"] = "rmm"
        elif all_durations["intr"]:
            all_durations["color"] = "gmm"

        context = dict(
            context,
            **{
                "all_durations": all_durations,
                "all_vars": {
                    "arable_land": "arable_land",
                    "agricultural_population": "agricultural_population",
                },
            },
        )

        nga_pol_relations = self.object.polity_sides.all()

        time_deltas = []
        for relation in nga_pol_relations:
            if (relation.year_from, relation.year_to) not in time_deltas:
                time_deltas += [(relation.year_from, relation.year_to)]

        context["nga_pol_rel"] = {}
        for time_delta in time_deltas:
            nga_list = []
            for relation in nga_pol_relations:
                if all(
                    [
                        time_delta[0] == relation.year_from,
                        time_delta[1] == relation.year_to,
                    ]
                ):
                    nga_list += [relation.nga_party]

            context["nga_pol_rel"][time_delta] = nga_list

        _filter = Q(polity_id=self.object.pk) | Q(
            other_polity_id=self.object.pk
        )
        preceding_data, succeeding_data = [], []
        for preceding_entity in Polity_preceding_entity.objects.filter(
            _filter
        ):
            if (
                preceding_entity.polity
                and preceding_entity.polity.id == self.object.pk
            ):
                preceding_data.append(preceding_entity)
            elif (
                preceding_entity.other_polity
                and preceding_entity.other_polity.id == self.object.pk
            ):  # noqa: E501 pylint: disable=C0301
                succeeding_data.append(preceding_entity)

        context = dict(
            context,
            **{
                "preceding_data": preceding_data,
                "succeeding_data": succeeding_data,
            },
        )

        return context


class NgaCreateView(PermissionRequiredMixin, CreateView):
    """
    Create a new NGA.
    """

    model = Nga
    form_class = NgaForm
    template_name = "core/nga/nga_form.html"  # noqa: E501  TODO: This template file is marked as missing
    permission_required = "core.add_capital"
    success_url = reverse_lazy("ngas")

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse("index"))


class NgaUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update an NGA.
    """

    model = Nga
    form_class = NgaForm
    template_name = "core/nga/nga_update.html"
    permission_required = "core.add_capital"
    success_message = "You successfully updated the Nga."
    success_url = reverse_lazy("ngas")


class NgaListView(ListView):
    """
    List all NGAs.
    """

    model = Nga
    template_name = "core/nga/nga_list.html"


class NgaDetailView(DetailView):
    """
    Show details of an NGA.
    """

    model = Nga
    template_name = "core/nga/nga_detail.html"


class CapitalCreateView(
    PermissionRequiredMixin, SuccessMessageMixin, CreateView
):
    """
    Create a new Capital.
    """

    model = Capital
    form_class = CapitalForm
    template_name = "core/capital/capital_form_create.html"
    permission_required = "core.add_capital"
    success_message = "You successfully created a new Capital."
    success_url = reverse_lazy("capitals")


class CapitalUpdateView(
    PermissionRequiredMixin, SuccessMessageMixin, UpdateView
):
    """
    Update a Capital.
    """

    model = Capital
    form_class = CapitalForm
    template_name = "core/capital/capital_form.html"
    permission_required = "core.add_capital"
    success_message = "You successfully updated the Capital."
    success_url = reverse_lazy("capitals")


class CapitalListView(ListView):
    """
    List all Capitals.
    """

    model = Capital
    template_name = "core/capital/capital_list.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("capitals")


class CapitalDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Delete a Capital.
    """

    model = Capital
    success_url = reverse_lazy("capitals")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"
    success_message = "You successfully deleted one Capital."


class SeshatPrivateCommentUpdateView(
    PermissionRequiredMixin, UpdateView, FormMixin
):
    """
    View to update a SeshatPrivateComment instance.
    """

    model = SeshatPrivateComment
    form_class = SeshatPrivateCommentForm
    template_name = "core/seshatcomments/seshatprivatecomment_update.html"
    permission_required = "core.add_seshatprivatecommentpart"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.

        Args:
            request: The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The HTTP response.
        """
        form = self.form()
        if not form.is_valid():
            return self.form_invalid(form)

        # Assuming you have this method to get the object
        self.object = self.get_object()

        new_experts = form.cleaned_data["private_comment_reader"]

        # Add the new experts to the ManyToMany field
        self.object.private_comment_reader.add(*new_experts)

        return self.form_valid(form)

    def get_another_form(self, request, *args, **kwargs):
        """
        Return the data from another form in the SeshatPrivateCommentPartForm.

        Args:
            request: The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            SeshatPrivateCommentPartForm: The form instance.
        """
        # Implement this method to return the specific instance of another_form
        return SeshatPrivateCommentPartForm(request.POST, request.another_form)

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)

        app_labels = ["core", "rt", "general", "sc", "wf", "crisisdb"]
        apps_models = {app: get_models(app) for app in app_labels}

        my_app_models = []
        for app, models in apps_models.items():
            if app == "core":
                # Handle the case where the app is 'core'
                for model_name, model in models.items():
                    if model_name == "polity" and model.objects.filter(
                        private_comment_n=self.object.id
                    ):
                        obj = model.objects.get(
                            private_comment_n=self.object.id
                        )

                        my_app_models.append(
                            {
                                "my_polity": obj,
                                "my_polity_id": obj.id,
                                "commented_pols_link": True,
                                "start_year": obj.start_year,
                                "end_year": obj.end_year,
                            }
                        )
            else:
                # Handle the case where the app is not 'core'
                for model_name, model in models.items():
                    if hasattr(model, "private_comment") and all(
                        [
                            "_citations" not in model_name,
                            "_curator" not in model_name,
                            not model_name.startswith("us_"),
                            model.objects.filter(
                                private_comment=self.object.id
                            ),
                        ]
                    ):
                        obj = model.objects.get(private_comment=self.object.id)

                        try:
                            variable_name = obj.clean_name_spaced()
                        except AttributeError:
                            variable_name = obj.name

                        my_app_models.append(
                            {
                                "my_polity": obj.polity,
                                "my_value": obj.show_value,
                                "my_year_from": obj.year_from,
                                "my_year_to": obj.year_to,
                                "my_tag": obj.get_tag_display(),
                                "my_var_name": variable_name,
                                "my_polity_id": obj.polity.id,
                                "my_description": obj.description,
                            }
                        )

        context = dict(
            context,
            **{
                "my_app_models": my_app_models,
                "another_form": SeshatPrivateCommentPartForm(),
            },
        )

        return context


class ReligionCreateView(PermissionRequiredMixin, CreateView):
    """
    Create a new religion.
    """

    model = Religion
    form_class = ReligionForm
    template_name = "core/religion_create.html"
    permission_required = "core.add_seshatprivatecommentpart"
    success_url = reverse_lazy("religion_list")


class ReligionUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Update a religion.
    """

    model = Religion
    form_class = ReligionForm
    template_name = "core/religion_update.html"
    permission_required = "core.add_seshatprivatecommentpart"
    success_url = reverse_lazy("religion_list")


class NotFoundView(TemplateView):
    template_name = "core/not_found_404.html"


class MethodsView(TemplateView):
    template_name = "core/methods.html"


class WhoWeAreView(TemplateView):
    template_name = "core/whoweare.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        try:
            with open(US_STATES_GEOJSON_PATH, "r") as json_file:
                json_data = json.load(json_file)

            context["json_data"] = json_data
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        return context


class DownloadsView(TemplateView):
    template_name = "core/downloads-old.html"


class CodebookView(TemplateView):
    template_name = "core/codebook-old.html"


class CodebookNewView(TemplateView):
    template_name = "core/codebook-new.html"


class AcknowledgementsView(TemplateView):
    template_name = "core/acknowledgements.html"


class ZoteroNoRefsListView(ListView):
    pass  # TODO: create from no_zotero_refs_list_view


def no_zotero_refs_list_view(request):
    """
    List all references without a Zotero link.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    selected_no_zotero_refs = Reference.objects.filter(
        zotero_link__startswith="NOZOTERO_"
    )

    # Show 10 refs per page
    paginator = Paginator(selected_no_zotero_refs, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "object_list": selected_no_zotero_refs,
        "page_obj": page_obj,
        "is_paginated": False,
    }

    return render(
        request, "core/references/reference_list_nozotero.html", context
    )


# TODO: rewrite as a class-based view (TemplateView/View)
def reference_update_modal_view(request, pk):
    """
    Update a reference using a modal or a standalone page depending on the
    request.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the reference.

    Returns:
        HttpResponse: The response object.
    """
    is_ajax = request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"

    # Either render only the modal content, or a full standalone page
    if is_ajax:
        template_name = "core/references/reference_update_modal.html"
    else:
        template_name = "core/references/reference_update.html"

    object = Reference.objects.get(pk=pk)

    if request.method == "POST":
        form = ReferenceForm(instance=object, data=request.POST)
        if form.is_valid():
            form.save()
            if not is_ajax:
                # Reload the page
                return HttpResponseRedirect(request.META["PATH_INFO"])

    elif request.method == "GET":
        form = ReferenceForm(instance=object)

    context = {
        "object": object,
        "form": form,
    }

    return render(request, template_name, context)


# TODO: rewrite as a class-based view (TemplateView/View)
@permission_required("core.add_capital")
def seshatcommentparts_create2_view(request, com_id, subcom_order):
    """
    Create a new comment part.

    Note:
        This view is only accessible to users with the 'add_capital' permission.

    Args:
        request (HttpRequest): The request object.
        com_id (int): The primary key of the comment.
        subcom_order (int): The order of the comment part.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == "POST":
        form = SeshatCommentPartForm2(request.POST)
        parent_comment = SeshatComment.objects.get(id=com_id)

        if form.is_valid():
            comment_text = form.cleaned_data["comment_text"]

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(
                    user=request.user
                )
            except:  # noqa: E722  TODO: Don't use bare except
                seshat_expert_instance = None

            seshat_comment_part = SeshatCommentPart(
                comment_part_text=comment_text,
                comment_order=subcom_order,
                comment_curator=seshat_expert_instance,
                comment=parent_comment,
            )

            seshat_comment_part.save()

            # Process the formset
            reference_formset = ReferenceFormSet2(request.POST, prefix="refs")
            if reference_formset.is_valid():
                to_be_added = []
                to_be_deleted_later = []
                for reference_form in reference_formset:
                    if reference_form.is_valid():
                        try:
                            reference = reference_form.cleaned_data["ref"]
                            page_from = reference_form.cleaned_data[
                                "page_from"
                            ]
                            page_to = reference_form.cleaned_data["page_to"]
                            to_be_deleted = reference_form.cleaned_data[
                                "DELETE"
                            ]
                            parent_pars_inserted = reference_form.cleaned_data[
                                "parent_pars"
                            ]

                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, created = (
                                    Citation.objects.get_or_create(
                                        ref=reference,
                                        page_from=int(page_from),
                                        page_to=int(page_to),
                                    )
                                )
                            else:
                                citation, created = (
                                    Citation.objects.get_or_create(
                                        ref=reference,
                                        page_from=None,
                                        page_to=None,
                                    )
                                )

                            # Associate the Citation with the SeshatCommentPart
                            if to_be_deleted:
                                to_be_deleted_later.append(
                                    (citation, parent_pars_inserted)
                                )
                            else:
                                to_be_added.append(
                                    (citation, parent_pars_inserted)
                                )
                        except:  # noqa: E722  TODO: Don't use bare except
                            pass  # TODO: Handle the exception

                seshat_comment_part.comment_citations_plus.clear()

                for item in to_be_added:
                    # Query for an existing row based on citation and SeshatCommentPart
                    scp_through_ctn, created = (
                        ScpThroughCtn.objects.get_or_create(
                            seshatcommentpart=seshat_comment_part,
                            citation=item[0],
                            defaults={
                                "parent_paragraphs": item[1]
                            },  # Set defaults including parent_paragraphs
                        )
                    )

                    # If the row already exists, update its parent_paragraphs
                    if not created:
                        scp_through_ctn.parent_paragraphs = item[1]
                        scp_through_ctn.save()

            return redirect(
                reverse("seshatcomment-update", kwargs={"pk": com_id})
            )

    elif request.method == "GET":
        formset = ReferenceFormSet2(prefix="refs")
        form = SeshatCommentPartForm2()
        parent_comment = SeshatComment.objects.get(id=com_id)

    context = {
        "form": form,
        "com_id": com_id,
        "subcom_order": subcom_order,
        "formset": formset,
        "parent_par": parent_comment,
    }

    return render(
        request, "core/seshatcomments/seshatcommentpart_create2.html", context
    )


# TODO: rewrite as a class-based view (TemplateView/View)
@permission_required("core.add_capital")
def seshatcommentparts_create2_inline_view(
    request, app_name, model_name, instance_id
):
    if request.method == "POST":
        form = SeshatCommentPartForm2(request.POST)
        parent_comment = SeshatComment.objects.create(
            text="a new_comment_text"
        )
        model_class = apps.get_model(app_label=app_name, model_name=model_name)

        model_instance = get_object_or_404(model_class, id=instance_id)
        model_instance.comment = parent_comment

        model_instance.save()
        if form.is_valid():
            comment_text = form.cleaned_data["comment_text"]

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(
                    user=request.user
                )
            except:  # noqa: E722  TODO: Don't use bare except
                seshat_expert_instance = None

            seshat_comment_part = SeshatCommentPart(
                comment_part_text=comment_text,
                comment_order=1,
                comment_curator=seshat_expert_instance,
                comment=parent_comment,
            )

            seshat_comment_part.save()

            # Process the formset
            reference_formset = ReferenceFormSet2(request.POST, prefix="refs")
            if reference_formset.is_valid():
                to_be_added = []
                to_be_deleted_later = []
                for reference_form in reference_formset:
                    if reference_form.is_valid():
                        try:
                            reference = reference_form.cleaned_data["ref"]
                            page_from = reference_form.cleaned_data[
                                "page_from"
                            ]
                            page_to = reference_form.cleaned_data["page_to"]
                            to_be_deleted = reference_form.cleaned_data[
                                "DELETE"
                            ]
                            parent_pars_inserted = reference_form.cleaned_data[
                                "parent_pars"
                            ]

                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, created = (
                                    Citation.objects.get_or_create(
                                        ref=reference,
                                        page_from=int(page_from),
                                        page_to=int(page_to),
                                    )
                                )
                            else:
                                citation, created = (
                                    Citation.objects.get_or_create(
                                        ref=reference,
                                        page_from=None,
                                        page_to=None,
                                    )
                                )

                            # Associate the Citation with the SeshatCommentPart
                            if to_be_deleted:
                                to_be_deleted_later.append(
                                    (citation, parent_pars_inserted)
                                )
                            else:
                                to_be_added.append(
                                    (citation, parent_pars_inserted)
                                )
                        except:  # noqa: E722  TODO: Don't use bare except
                            pass  # TODO: Handle the exception

                seshat_comment_part.comment_citations_plus.clear()

                for item in to_be_added:
                    # Query for an existing row based on citation and SeshatCommentPart
                    scp_through_ctn, created = (
                        ScpThroughCtn.objects.get_or_create(
                            seshatcommentpart=seshat_comment_part,
                            citation=item[0],
                            defaults={
                                "parent_paragraphs": item[1]
                            },  # Set defaults including parent_paragraphs
                        )
                    )

                    # If the row already exists, update its parent_paragraphs
                    if not created:
                        scp_through_ctn.parent_paragraphs = item[1]
                        scp_through_ctn.save()

            return redirect(
                reverse(
                    "seshatcomment-update", kwargs={"pk": parent_comment.pk}
                )
            )

    elif request.method == "GET":
        formset = ReferenceFormSet2(prefix="refs")
        form = SeshatCommentPartForm2()

    context = {
        "form": form,
        "com_id": parent_comment.pk,
        "subcom_order": subcom_order,  # TODO: this will crash
        "formset": formset,
    }

    return render(
        request, "core/seshatcomments/seshatcommentpart_create2.html", context
    )


# TODO: rewrite as a class-based view (TemplateView/View)
@permission_required("core.add_seshatprivatecommentpart")
def seshatprivatecommentparts_create2_view(request, private_com_id):
    """
    Create a new private comment part.

    Note:
        This view is only accessible to users with the 'add_seshatprivatecommentpart'
        permission.

    Args:
        request (HttpRequest): The request object.
        private_com_id (int): The primary key of the private comment.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == "POST":
        form = SeshatPrivateCommentPartForm(request.POST)
        parent_o = SeshatPrivateComment.objects.get(id=private_com_id)

        if form.is_valid():
            private_comment_part_text = form.cleaned_data[
                "private_comment_part_text"
            ]
            private_comment_reader = form.cleaned_data[
                "private_comment_reader"
            ]

            try:
                private_comment_owner = Seshat_Expert.objects.get(
                    user=request.user
                )
            except Seshat_Expert.DoesNotExist:
                private_comment_owner = None

            seshat_private_comment_part = SeshatPrivateCommentPart(
                private_comment_part_text=private_comment_part_text,
                private_comment_owner=private_comment_owner,
                private_comment=parent_o,
            )

            seshat_private_comment_part.save()

            seshat_private_comment_part.private_comment_reader.add(
                *private_comment_reader
            )

            return redirect(
                reverse(
                    "seshatprivatecomment-update",
                    kwargs={"pk": private_com_id},
                )
            )

    elif request.method == "GET":
        form = SeshatPrivateCommentPartForm()

    context = {
        "form": form,
        "private_com_id": private_com_id,
    }

    return render(
        request,
        "core/seshatcomments/seshatprivatecommentpart_create2.html",
        context,
    )


# TODO: rewrite as a class-based view (TemplateView/View)
def signup_traditional_view(request):
    """
    Handle user signup.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            message = render_to_string(
                "core/account_activation_email.html",
                {
                    "user": user,
                    "domain": "seshat-db.com",
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )

            send_mail(
                "Seshat-DB Email Verification",
                message,
                "seshatdb@gmail.com",  # Replace with your sender email
                [user.email],  # Replace with recipient email(s)
                fail_silently=False,
            )

            return redirect("account_activation_sent")

    elif request.method == "GET":
        form = SignUpForm()

    context = {"form": form}

    return render(request, "core/signup_traditional.html", context)


# TODO: rewrite as a class-based view (TemplateView/View)
def signupfollowup_view(request):
    """
    Handle user signup follow-up.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    return render(request, "core/signup-followup.html")


def activate_view(request, uidb64, token):
    """
    Activate user account.

    Args:
        request: The request object.
        uidb64: The user ID encoded in base64.
        token: The token.

    Returns:
        HttpResponse: The HTTP response.
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.backend = "django.contrib.auth.backends.ModelBackend"
        user.save()

        login(request, user)

        return redirect("signup-followup")

    return render(request, "core/account_activation_invalid.html")


# TODO: rewrite as a class-based view (TemplateView/View)
def discussion_room_view(request):
    """
    Render the discussion room page.
    """
    return render(request, "core/discussion_room.html")


# TODO: rewrite as a class-based view (TemplateView/View)
def nlp_datapoints_view(request):
    """
    Render the NLP data points page.
    """
    return render(request, "core/nlp_datapoints.html")


# TODO: rewrite as a class-based view (TemplateView/View)
def nlp_datapoints_2_view(request):
    """
    Render the NLP data points page.
    """
    return render(request, "core/nlp_datapoints_2.html")


# TODO: rewrite as a class-based view (TemplateView/View)
def account_activation_sent_view(request):
    """
    Render the account activation sent page.
    """
    return render(request, "core/account_activation_sent.html")


# TODO: rewrite as a class-based view (TemplateView/View)
def variablehierarchy_view(request):
    """
    Handle variable hierarchy setting. This is a view for the admin to set the
    variable hierarchy.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.

    ..
        TODO: This looks like it won't do anything (as variables = {})
    """
    variables = {}

    good_variables = []
    for item in variables.keys():
        good_key = item[0:9] + item[9].lower() + item[10:]
        good_key = good_key.replace("gdp", "GDP")
        good_key = good_key.replace("gDP", "GDP")
        good_variables.append(good_key)

    variable_hierarchies_to_be_hidden = []
    for obj in Variablehierarchy.objects.filter(is_verified=True):
        crisis_db_name = "crisisdb_" + obj.name[0].lower() + obj.name[1:]
        crisis_db_name = crisis_db_name.replace("gdp", "GDP")
        crisis_db_name = crisis_db_name.replace("gDP", "GDP")

        if crisis_db_name in good_variables:
            variable_hierarchies_to_be_hidden.append(crisis_db_name)

    select_variable = [("", " -- Select a CrisisDB Variable -- ")]
    for obj in good_variables:
        if obj not in variable_hierarchies_to_be_hidden:
            var_name = obj.name[9].lower() + obj.name[10:]
            var_name = var_name.replace("gdp", "GDP")
            var_name = var_name.replace("gDP", "GDP")

            select_variable.append((var_name, var_name))

    select_section = [("", " -- Select Section -- ")]
    for section_o in Section.objects.all():
        select_section.append((section_o.name, section_o.name))

    # Subsections
    select_subsection = [("", " -- Select Section First -- ")]
    for subsection in Subsection.objects.all():
        select_subsection.append((subsection.name, subsection.name))

    # Let's create an API serializer for section and subsection hierarchy
    results = get_api_results("sections")

    section_tree_data, section_options = {}, {}
    for item in results:
        subsection_tree = {}
        subsections_list = []
        for subsection in item["subsections"]:
            subsections_list += [subsection]
            objects = Variablehierarchy.objects.filter(
                section=Section.objects.get(name=item["name"]),
                subsection=Subsection.objects.get(name=subsection),
            )
            subsection_tree[subsection] = [o.name for o in objects]

        section_tree_data[item["name"]] = subsection_tree
        section_options[item["name"]] = subsections_list

    if request.method == "POST":
        form = VariablehierarchyFormNew(request.POST)
        if True:
            data = request.POST
            variable_name = data["variable_name"]

            is_verified_str = data.get("is_verified", False)
            if is_verified_str == "on":
                is_verified = True
            elif is_verified_str == "off":
                is_verified = False
            else:
                is_verified = False

            section_name = Section.objects.get(name=data["section_name"])
            subsection_name = Subsection.objects.get(
                name=data["subsection_name"]
            )

            # Check to see if subsection and section match
            if (
                data["subsection_name"]
                in section_tree_data[data["section_name"]]
            ):
                new_var_hierarchy = Variablehierarchy(
                    name=variable_name,
                    section=section_name,
                    subsection=subsection_name,
                    is_verified=is_verified,
                )
                new_var_hierarchy.save()

                message = f"You have successfully submitted {variable_name} to: {section_name} > {subsection_name}"  # noqa: E501 pylint: disable=C0301
                messages.success(request, message)

                return HttpResponseRedirect(
                    reverse("variablehierarchysetting")
                )
            else:
                messages.warning(
                    request,
                    "Form submission unssuccessful, section and subsection do not match.",
                )
    elif request.method == "GET":
        form = VariablehierarchyFormNew()

    context = {
        "sectionOptions": section_options,
        "section_tree_data": section_tree_data,
        "form": form,
        "variable_list": select_variable,
        "section_list": select_section,
        "subsection_list": select_subsection,
    }

    return render(request, "core/variablehierarchy.html", context)


# TODO: rewrite as a class-based view (TemplateView/View)
def synczoteromanually_view(request):
    """
    This function is used to manually input the references from the Zotero data
    available in the MANUAL_IMPORT_REFS constant into the database.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    newly_adds = do_zotero_manually(MANUAL_IMPORT_REFS, Reference)

    context = {"newly_adds": newly_adds}

    update_citations_from_inside_zotero_update()

    return render(request, "core/references/synczotero.html", context)


# TODO: rewrite as a class-based view (TemplateView/View)
def synczotero_view(request):
    """
    This function is used to sync the Zotero data with the database.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    results = ZOTERO.client.everything(ZOTERO.client.top())
    newly_adds = do_zotero(results[0:300], Reference)

    context = {"newly_adds": newly_adds}

    update_citations_from_inside_zotero_update()

    return render(request, "core/references/synczotero.html", context)


# TODO: rewrite as a class-based view (TemplateView/View)
def synczotero100_view(request):
    """
    This function is used to sync the Zotero data with the database.

    Note:
        This function syncs only 100 references.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    results = ZOTERO.client.top(limit=100)

    context = {"newly_adds": do_zotero(results, Reference)}

    update_citations_from_inside_zotero_update()

    return render(request, "core/references/synczotero.html", context)


# TODO: rewrite as a class-based view (TemplateView/View)
def update_citations_view(request):
    """
    This function takes all the references and build a citation for them.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    for reference in Reference.objects.all():
        citation, _ = Citation.objects.get_or_create(
            ref=reference, page_from=None, page_to=None
        )
        citation.save()

    return render(request, "core/references/reference_list.html")


# TODO: rewrite as a class-based view (TemplateView/View)
@require_GET
def polity_filter_options_view(request):
    """
    This view returns the options for the polity filter.

    Note:
        The view is decorated with the `require_GET` decorator to ensure that
        only GET requests are allowed.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The JSON response.
    """
    # Filter the options based on the search text
    options = Polity.objects.filter(
        name__icontains=request.GET.get("search_text", "")
    )

    return JsonResponse({"options": options.values("id", "name")})


# TODO: rewrite as a class-based view (TemplateView/View)
def seshatcommentparts_create3_view(request):
    """
    Create a new SeshatCommentPart instance.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    if request.method == "POST":
        form = SeshatCommentPartForm2(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data["comment_text"]
            comment_order = form.cleaned_data["comment_order"]

            comment = SeshatComment.objects.create(text="a new_comment_text")

            try:
                seshat_expert = Seshat_Expert.objects.get(user=request.user)
            except Seshat_Expert.DoesNotExist:
                seshat_expert = None

            # Create the SeshatCommentPart instance
            comment_part = SeshatCommentPart.objects.create(
                comment=comment,
                comment_part_text=comment_text,
                comment_order=comment_order,
                comment_curator=seshat_expert,
            )

            # Process the formset
            # Note: the below will crash as ReferenceFormSet is not defined (#TODO?)
            reference_formset = ReferenceFormSet(request.POST, prefix="refs")

            if any(
                [
                    not reference_formset.is_valid(),
                    not reference_formset.has_changed(),
                ]
            ):
                error_message = f"Formset errors: {reference_formset.errors}, {reference_formset.non_form_errors()}"  # noqa: E501 pylint: disable=C0301

                # TODO: Should we handle errors differently here, rather than printing?
                print(error_message)

            for reference_form in reference_formset:
                if reference_form.is_valid():
                    try:
                        reference = reference_form.cleaned_data["ref"]
                        page_from = reference_form.cleaned_data["page_from"]
                        page_to = reference_form.cleaned_data["page_to"]
                    except KeyError:
                        # TODO: Handle the exception better here?
                        pass
                    else:
                        # Get or create the Citation instance
                        citation, _ = Citation.objects.get_or_create(
                            ref=reference,
                            page_from=int(page_from),
                            page_to=int(page_to),
                        )

                        # Associate the Citation with the SeshatCommentPart
                        comment_part.comment_citations.add(citation)
                else:
                    # TODO: Handle the exception better here?
                    print(f"Form errors: {reference_form.errors}")

            # Redirect to the index page
            return redirect("index")

    elif request.method == "GET":
        form = SeshatCommentPartForm2()

    context = {"form": form}

    return render(
        request,
        "core/seshatcomments/seshatcommentpart_create.html",
        context,
    )


# TODO: rewrite as a class-based view (TemplateView/View)
def world_map_view(request):
    # global WORLD_MAP_INITIAL_DISPLAYED_YEAR, WORLD_MAP_INITIAL_POLITY
    """
    This view is used to display a map with polities plotted on it. The initial
    view just loads a polity with a seshat_id picked at random and sets the
    display year to that polity start year.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    seshat_id = WORLD_MAP_INITIAL_POLITY
    display_year = WORLD_MAP_INITIAL_DISPLAYED_YEAR

    # Check if 'year' parameter is different from the world_map_initial_displayed_year or
    # not present then redirect
    if "year" in request.GET:
        if request.GET["year"] != str(seshat_id):
            return redirect(f"{request.path}?year={seshat_id}")
    else:
        # Select a random polity for the initial view
        if "test" not in sys.argv:
            display_year, seshat_id = random_polity_shape()
        return redirect(f"{request.path}?year={seshat_id}")

    context = get_polity_shape_content(seshat_id=seshat_id)
    context = common_map_view_content(context)

    # For the initial view, set the displayed year to the polity's start year
    context["display_year"] = display_year

    return render(request, "core/world_map.html", context)


# TODO: rewrite as a class-based view (TemplateView/View)
def world_map_one_year_view(request):
    """
    This view is used to display a map with polities plotted on it. The view
    loads all polities present in the year in the url.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The HTTP response with serialized JSON.
    """
    year = request.GET.get("year", WORLD_MAP_INITIAL_DISPLAYED_YEAR)

    content = get_polity_shape_content(displayed_year=year)
    content = common_map_view_content(content)

    return JsonResponse(content)


class WorldmapView(View):
    one_year = False

    def get(self, request, *args, **kwargs):
        """
        This view is used to display a map with polities plotted on it. The view
        loads all polities for the range of years.

        Returns:
            JsonResponse: The HTTP response with serialized JSON.
        """
        if self.one_year:
            year = request.GET.get("year", WORLD_MAP_INITIAL_DISPLAYED_YEAR)
            data = get_polity_shape_content(displayed_year=year)
        else:
            # Temporary restriction on the latest year for the whole map view
            data = get_polity_shape_content(override_latest_year=2014)

        data = common_map_view_content(data)

        return JsonResponse(data)

    @classmethod
    def as_view(
        cls,
        one_year=None,
        **initkwargs,
    ):
        """
        # TODO: docstring

        Returns:
            A callable view.
        """
        initkwargs = {
            "one_year": one_year,
        }

        return super().as_view(**initkwargs)


class ProvincesCountriesView(View):
    def get(self, request, *args, **kwargs):
        """
        This view is used to get the provinces and countries for the map as JSON data.

        Returns:
            JsonResponse: The HTTP response with serialized JSON.
        """
        provinces = get_provinces()
        countries = get_provinces(selected_base_map_gadm="country")

        data = {
            "provinces": provinces,
            "countries": countries,
        }

        # Return dropdown template as JSON response
        return JsonResponse(data)


# TODO: rewrite as a class-based view (TemplateView/View)
def update_seshat_comment_part_view(request, pk):
    """
    View to update a SeshatCommentPart instance.

    Note:
        This view can handle POST and GET requests.

    Args:
        request: The request object.
        pk: The primary key of the SeshatCommentPart instance.

    Returns:
        HttpResponse: The HTTP response.
    """
    comment_part = SeshatCommentPart.objects.get(id=pk)
    parent_comment_id = comment_part.comment.id
    subcomment_order = comment_part.comment_order

    parent_comment_part = SeshatComment.objects.get(id=parent_comment_id)

    if request.method == "POST":
        form = SeshatCommentPartForm2(request.POST)
        if form.is_valid():
            try:
                comment_curator = Seshat_Expert.objects.get(user=request.user)
            except Seshat_Expert.DoesNotExist:
                comment_curator = None

            # Update the SeshatCommentPart instance
            comment_part.comment_curator = comment_curator
            comment_part.comment_part_text = form.cleaned_data["comment_text"]
            comment_part.comment_order = form.cleaned_data["comment_order"]
            comment_part.save()

            # Process the formset
            if comment_part.citations_count <= 2:
                reference_formset = ReferenceFormSet2(
                    request.POST, prefix="refs"
                )
            elif comment_part.citations_count <= 4:
                reference_formset = ReferenceFormSet5(
                    request.POST, prefix="refs"
                )
            else:
                reference_formset = ReferenceFormSet10(
                    request.POST, prefix="refs"
                )

            if reference_formset.is_valid():
                add, delete = [], []
                for reference_form in reference_formset:
                    if reference_form.is_valid():
                        try:
                            reference = reference_form.cleaned_data["ref"]
                            page_from = reference_form.cleaned_data[
                                "page_from"
                            ]
                            page_to = reference_form.cleaned_data["page_to"]

                            parent_pars_inserted = reference_form.cleaned_data[
                                "parent_pars"
                            ]

                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, created = (
                                    Citation.objects.get_or_create(
                                        ref=reference,
                                        page_from=int(page_from),
                                        page_to=int(page_to),
                                    )
                                )
                            else:
                                citation, created = (
                                    Citation.objects.get_or_create(
                                        ref=reference,
                                        page_from=None,
                                        page_to=None,
                                    )
                                )

                            # Check whether the form indicates deletion
                            to_be_deleted = reference_form.cleaned_data[
                                "DELETE"
                            ]

                            if to_be_deleted:
                                # Add to deletion list
                                delete += [(citation, parent_pars_inserted)]
                            else:
                                # Add to addition list
                                add += [(citation, parent_pars_inserted)]
                        except:  # noqa: E722  TODO: Don't use bare except
                            # TODO: Handle the exception
                            pass

                comment_part.comment_citations_plus.clear()

                for citation, parent_paragraphs in add:
                    # Query for an existing row based on citation and SeshatCommentPart
                    scp_through_ctn, created = (
                        ScpThroughCtn.objects.get_or_create(
                            seshatcommentpart=comment_part,
                            citation=citation,
                            defaults={"parent_paragraphs": parent_paragraphs},
                        )
                    )

                    # If the row already exists, update its parent_paragraphs
                    if not created:
                        scp_through_ctn.parent_paragraphs = parent_paragraphs
                        scp_through_ctn.save()

            return redirect(
                reverse(
                    "seshatcomment-update", kwargs={"pk": parent_comment_id}
                )
            )

    elif request.method == "GET":
        all_present_citations = comment_part.comment_citations_plus.all()
        all_present_citations_plus = ScpThroughCtn.objects.filter(
            seshatcommentpart_id=comment_part.id
        )

        initial_data, formset = [], {}
        if all_present_citations_plus:
            for a_cit_through in all_present_citations_plus:
                ref = Reference.objects.get(id=a_cit_through.citation.ref.id)
                initial_data.append(
                    {
                        "ref": ref,
                        "page_from": a_cit_through.citation.page_from,
                        "page_to": a_cit_through.citation.page_to,
                        "parent_pars": a_cit_through.parent_paragraphs,
                    },
                )

        if all_present_citations:
            for a_cit in all_present_citations:
                ref = Reference.objects.get(id=a_cit.ref.id)
                initial_data.append(
                    {
                        "ref": ref,
                        "page_from": a_cit.page_from,
                        "page_to": a_cit.page_to,
                        "parent_pars": "",
                    },
                )

        if len(initial_data) <= 2:
            formset = ReferenceFormSet2(prefix="refs", initial=initial_data)
            form = SeshatCommentPartForm2(
                initial={
                    "comment_text": comment_part.comment_part_text,
                    "comment_order": comment_part.comment_order,
                }
            )
        elif len(initial_data) <= 4:
            formset = ReferenceFormSet5(prefix="refs", initial=initial_data)
            form = SeshatCommentPartForm5(
                initial={
                    "comment_text": comment_part.comment_part_text,
                    "comment_order": comment_part.comment_order,
                }
            )
        else:
            formset = ReferenceFormSet10(prefix="refs", initial=initial_data)
            form = SeshatCommentPartForm10(
                initial={
                    "comment_text": comment_part.comment_part_text,
                    "comment_order": comment_part.comment_order,
                }
            )

    context = {
        "form": form,
        "formset": formset,
        "comm_num": pk,
        "comm_part_display": comment_part,
        "parent_comment": parent_comment_part,
        "subcom_order": subcomment_order,
    }

    return render(
        request,
        "core/seshatcomments/seshatcommentpart_update2.html",
        context,
    )


# TODO: rewrite as a class-based view (CreateView)
@login_required
def create_subcomment_new_view(request, app_name, model_name, instance_id):
    """
    Create a Comment and assign it to a model instance.

    Note:
        This view has the login_required decorator to ensure that only
        logged-in users can access it.

    Args:
        request: The request object.
        app_name: The name of the app containing the model.
        model_name: The name of the model.
        instance_id: The id of the model instance.

    Returns:
        HttpResponse: The HTTP response.
    """
    # Get the model class dynamically using the provided model_name
    if model_name == "general":
        model_class = apps.get_model(
            app_label=app_name, model_name="polity_" + model_name
        )
    else:
        model_class = apps.get_model(app_label=app_name, model_name=model_name)

    # Handle the case where the model class does not exist
    if model_class is None:
        return HttpResponse("Model not found", status=404)

    # Get the instance of the model using the provided instance_id
    model_instance = get_object_or_404(model_class, id=instance_id)

    # Create a new comment instance and save it to the database
    if model_instance.comment and model_instance.comment.id > 1:
        comment_instance = model_instance.comment
    else:
        comment_instance = SeshatComment.objects.create(
            text="a new_comment_text new approach"
        )

    # Get the Seshat_Expert instance associated with the user
    try:
        seshat_expert_instance = Seshat_Expert.objects.get(user=request.user)
    except Seshat_Expert.DoesNotExist:
        seshat_expert_instance = None

    # Create the subcomment instance and save it to the database
    SeshatCommentPart.objects.create(
        comment_part_text="A subdescription text placeholder (to be edited) using the new approach",  # noqa: E501 pylint: disable=C0301
        comment=comment_instance,
        comment_curator=seshat_expert_instance,
        comment_order=1,
    )

    # Assign the comment to the model instance
    model_instance.comment = comment_instance
    model_instance.save()

    # Redirect the user
    return redirect("seshatcomment-update", pk=comment_instance.id)


# TODO: rewrite as a class-based view (TemplateView/View)
@login_required
def create_subcomment_newer_view(request, app_name, model_name, instance_id):
    """
    Create the first chunk of a new comment and assign it to a model instance and a seshat
    comment. Get the data on citations and do the appropriate assignments there as well.
    """
    if model_name == "general":
        model_class = apps.get_model(
            app_label=app_name, model_name="polity_" + model_name
        )
    else:
        model_class = apps.get_model(app_label=app_name, model_name=model_name)

    if model_class is None:
        return HttpResponse("Model not found", status=404)

    get_object_or_404(model_class, id=instance_id)

    if request.method == "POST":
        form = SeshatCommentPartForm2_UPGRADE(request.POST)
        if form.is_valid():
            references_formset = form.cleaned_data["references_formset"]

            references_formset = ReferenceFormSet2_UPGRADE(
                request.POST, prefix="refs"
            )
            if references_formset.is_valid():
                to_be_added, to_be_deleted_later = [], []
                page_from, page_to = None, None
                for reference_form in references_formset:
                    if reference_form.is_valid():
                        try:
                            reference = reference_form.cleaned_data["ref"]
                            page_from = reference_form.cleaned_data[
                                "page_from"
                            ]
                            page_to = reference_form.cleaned_data["page_to"]
                            to_be_deleted = reference_form.cleaned_data[
                                "DELETE"
                            ]
                            parent_pars_inserted = reference_form.cleaned_data[
                                "parent_pars"
                            ]
                        except KeyError:
                            pass  # TODO: Handle the exception
                        else:
                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, created = (
                                    Citation.objects.get_or_create(
                                        ref=reference,
                                        page_from=int(page_from),
                                        page_to=int(page_to),
                                    )
                                )
                            else:
                                citation, created = (
                                    Citation.objects.get_or_create(
                                        ref=reference,
                                        page_from=None,
                                        page_to=None,
                                    )
                                )

                            # Associate the Citation with the SeshatCommentPart
                            if to_be_deleted:
                                to_be_deleted_later.append(
                                    (citation, parent_pars_inserted)
                                )
                            else:
                                to_be_added.append(
                                    (citation, parent_pars_inserted)
                                )

                seshat_comment_part.comment_citations_plus.clear()  # TODO: this will crash

                for item in to_be_added:
                    # Query for an existing row based on citation and SeshatCommentPart
                    scp_through_ctn, created = (
                        ScpThroughCtn.objects.get_or_create(
                            seshatcommentpart=seshat_comment_part,  # TODO: this will crash
                            citation=item[0],
                            defaults={
                                "parent_paragraphs": item[1]
                            },  # Set defaults including parent_paragraphs
                        )
                    )

                    # If the row already exists, update its parent_paragraphs
                    if not created:
                        scp_through_ctn.parent_paragraphs = item[1]
                        scp_through_ctn.save()

            return redirect(
                reverse("seshatcomment-update", kwargs={"pk": com_id})
            )  # noqa: E501   TODO this will crash  pylint: disable=C0301
    elif request.method == "GET":
        form = SeshatCommentPartForm2_UPGRADE()

    context = {"form": form}

    return render(request, "core/seshatcomments/your_template.html", context)


# TODO: rewrite as a class-based view (CreateView)
@login_required
@permission_required("core.add_seshatprivatecommentpart")
def create_private_subcomment_new_view(
    request, app_name, model_name, instance_id
):
    """
    Create a PrivateComment and assign it to a model instance.

    Note:
        This view is only accessible to users with the 'add_seshatprivatecommentpart'
        permission.

    Args:
        request: The request object.
        app_name: The name of the app containing the model.
        model_name: The name of the model.
        instance_id: The id of the model instance.

    Returns:
        HttpResponse: The HTTP response.
    """
    # Get the model class dynamically using the provided model_name
    model_class = apps.get_model(app_label=app_name, model_name=model_name)

    # Handle the case where the model class does not exist
    if model_class is None:
        return HttpResponse("Model not found", status=404)

    # Get the instance of the model using the provided instance_id
    model_instance = get_object_or_404(model_class, id=instance_id)

    # Create a new comment instance and save it to the database
    if app_name == "core":
        if (
            model_instance.private_comment_n
            and model_instance.private_comment_n.id > 1
        ):
            private_comment_instance = model_instance.private_comment_n
        else:
            private_comment_instance = SeshatPrivateComment.objects.create(
                text="a new_private_comment_text new approach for polity"
            )
    else:
        if (
            model_instance.private_comment
            and model_instance.private_comment.id > 1
        ):
            private_comment_instance = model_instance.private_comment
        else:
            private_comment_instance = SeshatPrivateComment.objects.create(
                text="a new_private_comment_text new approach"
            )

    # Assign the comment to the model instance
    if app_name == "core":
        model_instance.private_comment_n = private_comment_instance
    else:
        model_instance.private_comment = private_comment_instance

    model_instance.save()

    # Redirect to the appropriate page
    return redirect(
        "seshatprivatecomment-update", pk=private_comment_instance.id
    )


# TODO: rewrite as a class-based view (TemplateView/View)
def seshatcomments_create3_view(request):
    """
    View to create a SeshatComment instance.

    Note:
        This view can handle POST and GET requests.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    if request.method == "POST":
        form = SeshatCommentForm2(request.POST)
        if form.is_valid():
            comment_instance = SeshatComment.objects.create(
                text="a new_comment_text"
            )

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(
                    user=request.user
                )
            except Seshat_Expert.DoesNotExist:
                seshat_expert_instance = None

            # Create the SeshatCommentPart instance
            comment_part = SeshatComment.objects.create(
                text="initial text",
            )

            # Process the formset
            comment_formset = CommentPartFormSet(
                request.POST, prefix="commentpart"
            )

            for subcomment_form in comment_formset:
                if subcomment_form.is_valid():
                    comment_text = subcomment_form.cleaned_data["comment_text"]
                    comment_order = subcomment_form.cleaned_data[
                        "comment_order"
                    ]

                    # Create the SeshatCommentPart instance
                    comment_part = SeshatCommentPart.objects.create(
                        comment=comment_instance,
                        comment_part_text=comment_text,
                        comment_order=comment_order,
                        comment_curator=seshat_expert_instance,
                    )

                    # Process the formset
                    # Note: the below will crash as ReferenceFormSet is not defined (#TODO?)
                    reference_formset = ReferenceFormSet(
                        request.POST, prefix="refs"
                    )

                    for reference_form in reference_formset:
                        if reference_form.is_valid():
                            try:
                                reference = reference_form.cleaned_data["ref"]
                                page_from = reference_form.cleaned_data[
                                    "page_from"
                                ]
                                page_to = reference_form.cleaned_data[
                                    "page_to"
                                ]
                            except KeyError:
                                # TODO: Handle exception
                                pass
                            else:
                                citation, _ = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to),
                                )

                                # Associate the Citation with the SeshatCommentPart
                                comment_part.comment_citations.add(citation)
                        else:
                            # TODO: Handle error differently
                            print(f"Form errors: {reference_form.errors}")

            # Redirect to a success page
            return redirect("index")

    elif request.method == "GET":
        form = SeshatCommentForm2()

    context = {"form": form}

    return render(
        request,
        "core/seshatcomments/seshatcomment_create.html",
        context,
    )


class SearchSuggestionsView(TemplateView):
    template_name = "core/partials/_search_suggestions.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        search_term = self.request.GET.get("search", "")
        _filter = (
            Q(name__icontains=search_term)
            | Q(long_name__icontains=search_term)
            | Q(new_name__icontains=search_term)
        )

        context = dict(context, **{
            "polities": Polity.objects.filter(_filter).order_by("start_year")[:8]
        })

        return context


class SearchRedirectView(RedirectView):
    pattern_name = "polity-detail-main"

    def get_redirect_url(self, *args, **kwargs):
        search_term = self.request.GET.get("search", "")

        polity = Polity.objects.filter(
            name__icontains=search_term
        ).first()

        if not polity:
            return reverse("index")

        return reverse(
            self.pattern_name,
            kwargs={"pk": polity.pk},
        )
