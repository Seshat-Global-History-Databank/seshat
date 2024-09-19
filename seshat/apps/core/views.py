from django.apps import apps
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.messages.views import SuccessMessageMixin
from django.core.cache import cache
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import F, Value, Q, Min, Max, Count
from django.db.models.functions import Replace
from django.http import (
    FileResponse,
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
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    TemplateView,
)
from django.views.generic.edit import FormMixin

import csv
import json
import numpy as np
import random
import sys

from ..accounts.models import Seshat_Expert
from ..crisisdb.models import (
    Power_transition,
    Crisis_consequence,
    Human_sacrifice,
)
from ..general.models import (
    Polity_capital,
    Polity_duration,
    Polity_language_genus,
    Polity_language,
    Polity_linguistic_family,
    Polity_preceding_entity,
    Polity_research_assistant,
)
from ..global_constants import (
    ABSENT_PRESENT_CHOICES,
    BASIC_CONTEXT,
    POLITY_LANGUAGE_CHOICES,
    POLITY_LANGUAGE_GENUS_CHOICES,
    POLITY_LINGUISTIC_FAMILY_CHOICES,
    ZOTERO,
    PATTERNS,
    US_STATES_GEOJSON_PATH,
    CSV_DELIMITER,
)
from ..global_utils import (
    get_date,
    get_models,
    get_api_results,
    get_csv_path,
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
    GADMCountries,
    GADMProvinces,
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
    VideoShapefile,
)
from .tokens import account_activation_token
from .constants import (
    CUSTOM_ORDER,
    CUSTOM_ORDER_SR,
    MANUAL_IMPORT_REFS,
    NLP_ZOTERO_LINKS_TO_FILTER,
)
from .utils import (
    get_data_for_polity,
    get_model_data,
    get_polity_app_data,
)


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
                "mysection": "xyz",
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
        return HttpResponseRedirect(reverse("seshat-index"))


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
                "mysection": "Fiscal Heeeelath",
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
                "mysection": "xyz",
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
                "mysection": "Fiscal Heeeelath",
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
        return HttpResponseRedirect(reverse("seshat-index"))


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

        apps = ["rt", "general", "sc", "wf", "crisisdb"]
        apps_models = {name: apps.all_models[name] for name in apps}

        abc = []
        for _, models in apps_models.items():
            for mm, model in models.items():
                if all(
                    [
                        "_citations" not in mm,
                        "_curator" not in mm,
                        not mm.startswith("us_"),
                        model.objects.filter(comment=self.object.id),
                    ]
                ):
                    o = model.objects.get(comment=self.object.id)

                    try:
                        var_name = o.clean_name_spaced()
                    except AttributeError:
                        var_name = o.name

                    abc.append(
                        {
                            "my_polity": o.polity,
                            "my_value": o.show_value,
                            "my_year_from": o.year_from,
                            "my_year_to": o.year_to,
                            "my_tag": o.get_tag_display(),
                            "my_var_name": var_name,
                            "my_polity_id": o.polity.id,
                        }
                    )

        context["my_app_models"] = abc

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


# SeshatCommentPart
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
        return HttpResponseRedirect(reverse("seshat-index"))


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
        return HttpResponseRedirect(reverse("seshat-index"))

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

        context = {
            "com_id": self.kwargs["com_id"],
            "subcom_order": self.kwargs["subcom_order"],
            "comment_curator": logged_in_expert,
            "comment_curator_id": logged_in_expert.id,
            "comment_curator_name": "Selected USER",
        }

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
        return HttpResponseRedirect(reverse("seshat-index"))

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


class PolityListViewLight(SuccessMessageMixin, ListView):
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
            )  # noqa: 501
            research_assistant_ids = research_assistants.values_list(
                "polity_ra_id", flat=True
            )  # noqa: 501

            experts = Seshat_Expert.objects.filter(
                id__in=research_assistant_ids
            )
            all_research_assistants = [
                f"{expert.user.first_name} {expert.user.last_name}"
                for expert in experts
            ]  # noqa: 501

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
                    "all_data": None,
                    "all_general_data": None,
                    "all_sc_data": None,
                    "all_wf_data": None,
                    "all_rt_data": None,
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
        except:  # noqa: E722  TODO: Don't use bare except
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
        except:  # noqa: E722  TODO: Don't use bare except
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

        try:
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
        except:  # noqa: E722  TODO: Don't use bare except
            context["nga_pol_rel"] = None

        preceding_data, succeeding_data = [], []
        for preceding_entity in Polity_preceding_entity.objects.filter(
            Q(polity_id=self.object.pk) | Q(other_polity_id=self.object.pk)
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
        return HttpResponseRedirect(reverse("seshat-index"))


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

        apps = ["core", "rt", "general", "sc", "wf", "crisisdb"]
        apps_models = {app: get_models(app) for app in apps}

        my_app_models = []
        for app, models in apps_models.items():
            if app == "core":
                # Handle the case where the app is 'core'
                for mm, mymodel in models.items():
                    if mm == "polity" and mymodel.objects.filter(
                        private_comment_n=self.object.id
                    ):
                        o = mymodel.objects.get(
                            private_comment_n=self.object.id
                        )

                        my_app_models.append(
                            {
                                "my_polity": o,
                                "my_polity_id": o.id,
                                "commented_pols_link": True,
                                "start_year": o.start_year,
                                "end_year": o.end_year,
                            }
                        )
            else:
                # Handle the case where the app is not 'core'
                for mm, mymodel in models.items():
                    if (
                        "_citations" not in mm
                        and "_curator" not in mm
                        and not mm.startswith("us_")
                        and mymodel.objects.filter(
                            private_comment=self.object.id
                        )
                    ):
                        o = mymodel.objects.get(private_comment=self.object.id)

                        try:
                            variable_name = o.clean_name_spaced()
                        except AttributeError:
                            variable_name = o.name

                        my_app_models.append(
                            {
                                "my_polity": o.polity,
                                "my_value": o.show_value,
                                "my_year_from": o.year_from,
                                "my_year_to": o.year_to,
                                "my_tag": o.get_tag_display(),
                                "my_var_name": variable_name,
                                "my_polity_id": o.polity.id,
                                "my_description": o.description,
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


@login_required
@permission_required("core.add_seshatprivatecommentpart")
def religion_create_view(request):
    """
    Create a new religion.

    Note:
        This view is only accessible to users with the 'add_seshatprivatecommentpart'
        permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.

    ..

        # TODO: Is there a reason this is not a class-based view?
    """
    if request.method == "POST":
        form = ReligionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("religion_list")
    elif request.method == "GET":
        form = ReligionForm()

    return render(request, "core/religion_create.html", {"form": form})


@login_required
@permission_required("core.add_seshatprivatecommentpart")
def religion_update_view(request, pk):
    """
    Update an existing religion.

    Note:
        This view is only accessible to users with the 'add_seshatprivatecommentpart'
        permission.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the religion.

    Returns:
        HttpResponse: The response object.

    ..

        # TODO: Is there a reason this is not a class-based view?
    """
    religion = get_object_or_404(Religion, pk=pk)

    if request.method == "POST":
        form = ReligionForm(request.POST, instance=religion)

        if form.is_valid():
            form.save()
            return redirect("religion_list")
    elif request.method == "GET":
        form = ReligionForm(instance=religion)

    return render(request, "core/religion_update.html", {"form": form})


def four_o_four(request):
    """
    Return a 404 error page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return render(request, "core/not_found_404.html")


def methods_view(request):
    """
    Return the Seshat "Methods" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return render(request, "core/seshat-methods.html", context={})


def whoweare_view(request):
    """
    Return the Seshat "Who We are" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    try:
        with open(US_STATES_GEOJSON_PATH, "r") as json_file:
            json_data = json.load(json_file)

        context = {"json_data": json_data}
    except (FileNotFoundError, json.JSONDecodeError):
        context = {}

    return render(request, "core/seshat-whoweare.html", context=context)


def downloads_page_view(request):
    """
    Return the Seshat "Downloads" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return render(request, "core/old_downloads.html", context={})


def codebook_view(request):
    """
    Return the Seshat "Codebook" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return render(request, "core/old_codebook.html", context={})


def code_book_new_1_view(request):
    return render(request, "core/code_book_1.html", context={})


def acknowledgements_view(request):
    """
    Return the Seshat "Acknowledgements" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return render(request, "core/seshat-acknowledgements.html", context={})


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


@permission_required("core.view_capital")
def referencesdownload_view(request):
    """
    Download all references as a CSV file.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="references.csv"'

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(["zotero_link", "creator"])

    for o in Reference.objects.all():
        writer.writerow([o.zotero_link, o.creator])

    return response


@permission_required("core.add_capital")
def seshat_comment_part_create_from_null_view_OLD(
    request, com_id, subcom_order
):
    """
    Create a new comment part.

    Note:
        This function is not used in the current implementation.
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
            except Seshat_Expert.DoesNotExist:
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

                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, _ = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to),
                                )
                            else:
                                citation, _ = Citation.objects.get_or_create(
                                    ref=reference, page_from=None, page_to=None
                                )

                            # Associate the Citation with the SeshatCommentPart
                            if to_be_deleted:
                                to_be_deleted_later.append(citation)
                            else:
                                to_be_added.append(citation)
                        except:  # noqa: E722  TODO: Don't use bare except
                            # TODO: Handle the exception
                            pass

                seshat_comment_part.comment_citations.clear()
                seshat_comment_part.comment_citations.add(*to_be_added)

            return redirect(
                reverse("seshatcomment-update", kwargs={"pk": com_id})
            )

    elif request.method == "GET":
        init_data = ReferenceFormSet2(prefix="refs")
        form = SeshatCommentPartForm2()

    context = {
        "form": form,
        "com_id": com_id,
        "subcom_order": subcom_order,
        "formset": init_data,
    }

    return render(
        request, "core/seshatcomments/seshatcommentpart_create2.html", context
    )


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
                            pass  # Handle the exception as per your requirement

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
                            pass  # Handle the exception as per your requirement

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


@permission_required("core.view_capital")
def capital_download_view(request):
    """
    Download all Capitals as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="capitals.csv"'

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "capital",
            "current_country",
            "longitude",
            "latitude",
            "is_verified",
            "note",
        ]
    )

    for obj in Capital.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.current_country,
                obj.longitude,
                obj.latitude,
                obj.is_verified,
                obj.note,
            ]
        )

    return response


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

    return render(request, "core/signup_traditional.html", {"form": form})


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


# Discussion Room
def discussion_room_view(request):
    """
    Render the discussion room page.
    """
    return render(request, "core/discussion_room.html")


# NLP Room 1
def nlp_datapoints_view(request):
    """
    Render the NLP data points page.
    """
    return render(request, "core/nlp_datapoints.html")


# NLP Room 2
def nlp_datapoints_2_view(request):
    """
    Render the NLP data points page.
    """
    return render(request, "core/nlp_datapoints_2.html")


def account_activation_sent_view(request):
    """
    Render the account activation sent page.
    """
    return render(request, "core/account_activation_sent.html")


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
    for o in Variablehierarchy.objects.filter(is_verified=True):
        crisis_db_name = "crisisdb_" + o.name[0].lower() + o.name[1:]
        crisis_db_name = crisis_db_name.replace("gdp", "GDP")
        crisis_db_name = crisis_db_name.replace("gDP", "GDP")

        if crisis_db_name in good_variables:
            variable_hierarchies_to_be_hidden.append(crisis_db_name)

    select_variable = [("", " -- Select a CrisisDB Variable -- ")]
    for o in good_variables:
        if o not in variable_hierarchies_to_be_hidden:
            var_name = o.name[9].lower() + o.name[10:]
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


def do_zotero(results):
    """
    Process the results from the Zotero API.

    Args:
        results: The results from the Zotero API.

    Returns:
        list: A list of dictionaries containing the processed data.
    """
    references_parent_lst = []
    for _, item in enumerate(results):
        a_key = item["data"]["key"]
        if a_key == "3BQQ8WN8":
            # Skipped because it is not in database
            continue
        if a_key == "RR6R3383":
            # Skipped because title is too big
            continue

        try:
            # We need to make sure that all the changes in Zotero will be reflected here.
            continue
        except:  # noqa: E722  TODO: Don't use bare except
            dic = {}
            try:
                if item["data"]["key"]:
                    tuple_key = item["data"]["key"]
                    dic["key"] = tuple_key
                else:
                    # Key is empty for index: {i}: {item['data']['itemType']}
                    pass
            except:  # noqa: E722  TODO: Don't use bare except
                # No key for item with index: {i}
                pass

            try:
                if item["data"]["itemType"]:
                    tuple_item = item["data"]["itemType"]
                    dic["itemType"] = tuple_item
                else:
                    # itemType is empty for index: {i}: {item['data']['itemType']}
                    pass
            except:  # noqa: E722  TODO: Don't use bare except
                # No itemType for item with index: {i}
                pass

            try:
                num_of_creators = len(item["data"]["creators"])
                if num_of_creators < 4 and num_of_creators > 0:
                    all_creators_list = []
                    for j in range(num_of_creators):
                        if a_key == "MM6AEU7H":
                            # Skipped because it has contributors and not authors
                            continue
                        try:
                            try:
                                good_name = item["data"]["creators"][j][
                                    "lastName"
                                ]
                            except:  # noqa: E722  TODO: Don't use bare except
                                good_name = item["data"]["creators"][j]["name"]
                        except:  # noqa: E722  TODO: Don't use bare except
                            good_name = ("NO_NAMES",)
                        all_creators_list.append(good_name)

                    good_name_with_space = "_".join(all_creators_list)
                    good_name_with_underscore = good_name_with_space.replace(
                        " ", "_"
                    )

                    dic["mainCreator"] = good_name_with_underscore
                elif num_of_creators > 3:
                    try:
                        try:
                            good_name = item["data"]["creators"][0]["lastName"]
                        except:  # noqa: E722  TODO: Don't use bare except
                            good_name = item["data"]["creators"][0]["name"]
                    except:  # noqa: E722  TODO: Don't use bare except
                        good_name = ("NO_NAME",)

                    good_name_with_space = good_name + "_et_al"
                    good_name_with_underscore = good_name_with_space.replace(
                        " ", "_"
                    )

                    dic["mainCreator"] = good_name_with_underscore
                else:
                    dic["mainCreator"] = "NO_CREATOR"
            except:  # noqa: E722  TODO: Don't use bare except
                # No mainCreator for item with index: {i}: {item['data']['itemType']}
                dic["mainCreator"] = "NO_CREATORS"

            try:
                if item["data"]["date"]:
                    full_date = item["data"]["date"]
                    year = PATTERNS.YEAR.search(full_date)
                    year_int = int(year[0])
                    dic["year"] = year_int
                else:
                    # Year is empty for index {i}: {item['data']['itemType']}
                    dic["year"] = 0
            except:  # noqa: E722  TODO: Don't use bare except
                # No year for index {i}: {item['data']['itemType']}
                dic["year"] = -1

            try:
                try:
                    if item["data"]["bookTitle"]:
                        if a_key == "MM6AEU7H":
                            pass
                        if item["data"]["itemType"] == "bookSection":
                            good_title = (
                                item["data"]["title"]
                                + " (IN) "
                                + item["data"]["bookTitle"]
                            )
                            pass
                        else:
                            good_title = item["data"]["title"]

                        dic["title"] = good_title
                    else:
                        good_title = item["data"]["title"]
                        dic["title"] = good_title

                        if a_key == "MM6AEU7H":
                            pass
                except:  # noqa: E722  TODO: Don't use bare except
                    dic["title"] = item["data"]["title"]
            except:  # noqa: E722  TODO: Don't use bare except
                # No title for item with index: {i}
                pass

            pot_title = dic.get("title")
            if not pot_title:
                pot_title = "NO_TITLE_PROVIDED_IN_ZOTERO"

            newref = Reference(
                title=pot_title,
                year=dic.get("year"),
                creator=dic.get("mainCreator"),
                zotero_link=dic.get("key"),
            )

            if dic.get("year") < 2040:
                newref.save()
                references_parent_lst.append(dic)

    return references_parent_lst


def do_zotero_manually(results):
    """
    Process the results from the Zotero API.

    Args:
        results: The results from the Zotero API.

    Returns:
        list: A list of dictionaries containing the processed data.
    """
    references_parent_lst = []
    for item in results:
        key = item["key"]

        if key == "3BQQ8WN8":
            # Skipped because it is not in database
            continue
        if key == "RR6R3383":
            # Skipped because title is too big
            continue

        try:
            Reference.objects.get(zotero_link=key)
            continue
        except:  # noqa: E722  TODO: Don't use bare except
            dic = {
                "key": key,
                "mainCreator": item["mainCreator"],
                "year": item["year"],
                "title": item["title"],
            }

            newref = Reference(
                title=dic.get("title"),
                year=dic.get("year"),
                creator=dic.get("mainCreator"),
                zotero_link=dic.get("key"),
            )

            if dic.get("year") < 2040:
                newref.save()
                references_parent_lst.append(dic)

    return references_parent_lst


def update_citations_from_inside_zotero_update():
    """
    This function takes all the references and build a citation for them.

    Args:
        None

    Returns:
        None
    """
    for ref in Reference.objects.all():
        obj, _ = Citation.objects.get_or_create(
            ref=ref, page_from=None, page_to=None
        )
        obj.save()


def synczoteromanually_view(request):
    """
    This function is used to manually input the references from the Zotero data
    available in the MANUAL_IMPORT_REFS constant into the database.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    context = {"newly_adds": do_zotero_manually(MANUAL_IMPORT_REFS)}

    update_citations_from_inside_zotero_update()

    return render(request, "core/references/synczotero.html", context)


def synczotero_view(request):
    """
    This function is used to sync the Zotero data with the database.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    results = ZOTERO.client.everything(ZOTERO.client.top())

    context = {"newly_adds": do_zotero(results[0:300])}

    update_citations_from_inside_zotero_update()

    return render(request, "core/references/synczotero.html", context)


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

    context = {"newly_adds": do_zotero(results)}

    update_citations_from_inside_zotero_update()

    return render(request, "core/references/synczotero.html", context)


def update_citations_view(request):
    """
    This function takes all the references and build a citation for them.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    for ref in Reference.objects.all():
        citation, _ = Citation.objects.get_or_create(
            ref=ref, page_from=None, page_to=None
        )
        citation.save()

    return render(request, "core/references/reference_list.html")


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
    ).values("id", "name")

    return JsonResponse({"options": options})


def download_oldcsv_view(request, file_name):
    """
    Download a CSV file.

    Args:
        request: The request object.
        file_name (str): The name of the file to download.

    Returns:
        FileResponse: The file response.
    """
    # Get file path
    file_path = get_csv_path(file_name)

    # Create a response
    response = FileResponse(open(file_path, "rb"))
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    return response


class IndexView(TemplateView):
    template_name = "core/seshat-index.html"

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

            app_key = app_name + "_data"

            for model in models:
                model_name = model.__name__

                queryset = model.objects.all()

                if model_name.startswith("Us_violence"):
                    print('here')
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


def get_polity_data_single(polity_id):
    """
    Get the data for a single polity. The returned data includes the number of
    records for each app (general, sc, wf, hs, cc, pt).

    Args:
        polity_id: The ID of the polity.

    Returns:
        dict: The data for the polity.
    """
    models = {k: get_models(k) for k in ["general", "sc", "wf"]}

    data = {
        "g": 0,
        "sc": 0,
        "wf": 0,
    }

    for model in models["general"]:
        if all(
            [
                hasattr(model, "polity_id"),
                model.objects.filter(polity_id=polity_id),
            ]
        ):
            data["g"] += model.objects.filter(polity_id=polity_id).count()

    for model in models["sc"]:
        if all(
            [
                hasattr(model, "polity_id"),
                model.objects.filter(polity_id=polity_id),
            ]
        ):
            data["sc"] += model.objects.filter(polity_id=polity_id).count()

    for model in models["wf"]:
        if all(
            [
                hasattr(model, "polity_id"),
                model.objects.filter(polity_id=polity_id),
            ]
        ):
            data["wf"] += model.objects.filter(polity_id=polity_id).count()

    data["hs"] = Human_sacrifice.objects.filter(polity=polity_id).count()
    data["cc"] = Crisis_consequence.objects.filter(polity=polity_id).count()
    data["pt"] = Power_transition.objects.filter(polity=polity_id).count()

    return data


@permission_required("core.view_capital")
def download_csv_all_polities_view(request):
    """
    Download a CSV file containing all polities.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"polities_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "macro_region",
            "home_seshat_region",
            "polity_new_ID",
            "polity_old_ID",
            "polity_long_name",
            "start_year",
            "end_year",
            "home_nga",
            "G",
            "SC",
            "WF",
            "RT",
            "HS",
            "CC",
            "PT",
            "polity_tag",
            "shapefile_name",
        ]
    )

    coded_value_data = get_polity_app_data(
        Polity, return_freq=False, return_contain=True
    )

    for obj in Polity.objects.all():
        if obj.home_seshat_region:
            writer.writerow(
                [
                    obj.home_seshat_region.mac_region.name,
                    obj.home_seshat_region.name,
                    obj.new_name,
                    obj.name,
                    obj.long_name,
                    obj.start_year,
                    obj.end_year,
                    obj.home_nga,
                    coded_value_data[obj.id]["g"],
                    coded_value_data[obj.id]["sc"],
                    coded_value_data[obj.id]["wf"],
                    coded_value_data[obj.id]["rt"],
                    coded_value_data[obj.id]["hs"],
                    coded_value_data[obj.id]["cc"],
                    coded_value_data[obj.id]["pt"],
                    obj.get_polity_tag_display(),
                    obj.shapefile_name,
                ]
            )
        else:
            writer.writerow(
                [
                    "None",
                    "None",
                    obj.new_name,
                    obj.name,
                    obj.long_name,
                    obj.start_year,
                    obj.end_year,
                    obj.home_nga,
                    coded_value_data[obj.id]["g"],
                    coded_value_data[obj.id]["sc"],
                    coded_value_data[obj.id]["wf"],
                    coded_value_data[obj.id]["rt"],
                    coded_value_data[obj.id]["hs"],
                    coded_value_data[obj.id]["cc"],
                    coded_value_data[obj.id]["pt"],
                    obj.get_polity_tag_display(),
                    obj.shapefile_name,
                ]
            )

    return response


def get_or_create_citation(reference, page_from, page_to):
    """
    Get or create a Citation instance. If a matching citation already exists, it
    is returned; otherwise, a new one is created.

    Args:
        reference (Reference): The reference.
        page_from (int): The starting page number.
        page_to (int): The ending page number.

    Returns:
        Citation: The Citation instance.
    """
    # Check if a matching citation already exists
    existing_citation = Citation.objects.filter(
        ref=reference, page_from=page_from, page_to=page_to
    ).first()

    # If a matching citation exists, return it; otherwise, create a new one
    return existing_citation or Citation.objects.create(
        ref=reference, page_from=page_from, page_to=page_to
    )


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
            comment_part = SeshatCommentPart.objects.create(
                comment=comment_instance,
                comment_part_text=comment_text,
                comment_order=comment_order,
                comment_curator=seshat_expert_instance,
            )

            # Process the formset
            reference_formset = ReferenceFormSet(
                request.POST, prefix="refs"
            )  # noqa: E501   TODO: this will crash  pylint: disable=C0301

            if not reference_formset.is_valid():
                print(
                    f"Formset errors: {reference_formset.errors}, {reference_formset.non_form_errors()}"  # noqa: E501 pylint: disable=C0301
                )

            if not reference_formset.has_changed():
                print(
                    f"Formset errors: {reference_formset.errors}, {reference_formset.non_form_errors()}"  # noqa: E501 pylint: disable=C0301
                )

            for reference_form in reference_formset:
                if reference_form.is_valid():
                    try:
                        reference = reference_form.cleaned_data["ref"]
                        page_from = reference_form.cleaned_data["page_from"]
                        page_to = reference_form.cleaned_data["page_to"]

                        # Get or create the Citation instance
                        citation, _ = Citation.objects.get_or_create(
                            ref=reference,
                            page_from=int(page_from),
                            page_to=int(page_to),
                        )

                        # Associate the Citation with the SeshatCommentPart
                        comment_part.comment_citations.add(citation)
                    except:  # noqa: E722  TODO: Don't use bare except
                        pass  # TODO: Handle the exception
                else:
                    # TODO: Handle error differently
                    print(f"Form errors: {reference_form.errors}")

            # Redirect to a success page
            return redirect("seshat-index")

    elif request.method == "GET":
        form = SeshatCommentPartForm2()

    return render(
        request,
        "core/seshatcomments/seshatcommentpart_create.html",
        {"form": form},
    )


# Shapefile views


def get_provinces(selected_base_map_gadm="province"):
    """
    Get all the province or country shapes for the map base layer.

    Args:
        selected_base_map_gadm (str): The selected base map GADM level.

    Returns:
        list: A list of dictionaries containing the province or country shapes.
    """

    # Use the appropriate Django ORM query based on the selected baseMapGADM value
    if selected_base_map_gadm == "country":
        rows = GADMCountries.objects.values_list("geom", "COUNTRY")
        provinces = [
            {
                "aggregated_geometry": GEOSGeometry(geom).geojson,
                "country": country,
            }
            for geom, country in rows
            if geom is not None
        ]
    elif selected_base_map_gadm == "province":
        rows = GADMProvinces.objects.values_list(
            "geom", "COUNTRY", "NAME_1", "ENGTYPE_1"
        )
        provinces = [
            {
                "aggregated_geometry": GEOSGeometry(geom).geojson,
                "country": country,
                "province": name,
                "province_type": engtype,
            }
            for geom, country, name, engtype in rows
            if geom is not None
        ]

    return provinces


def get_polity_shape_content(
    displayed_year="all",
    seshat_id="all",
    tick_number=80,
    override_earliest_year=None,
    override_latest_year=None,
):
    """
    This function returns the polity shapes and other content for the map.
    Only one of displayed_year or seshat_id should be set; not both.

    Note:
        seshat_id in VideoShapefile is new_name in Polity.

    Args:
        displayed_year (str): The year to display the polities for. "all" will return all
            polities. Any given year will return polities that were active in that year.
        seshat_id (str): The seshat_id of the polity to display. If a value is provided,
            only the shapes for that polity being returned.

    Returns:
        dict: The content for the polity shapes.
    """

    if displayed_year != "all" and seshat_id != "all":
        raise ValueError(
            "Only one of displayed_year or seshat_id should be set not both."
        )

    if displayed_year != "all":
        rows = VideoShapefile.objects.filter(
            polity_start_year__lte=displayed_year,
            polity_end_year__gte=displayed_year,
        )
    elif seshat_id != "all":
        rows = VideoShapefile.objects.filter(seshat_id=seshat_id)
    else:
        rows = VideoShapefile.objects.all()

    # Convert 'geom' to GeoJSON in the database query
    rows = rows.annotate(geom_json=AsGeoJSON("geom")).values(
        "id",
        "seshat_id",
        "name",
        "polity",
        "start_year",
        "end_year",
        "polity_start_year",
        "polity_end_year",
        "colour",
        "area",
        "geom_json",
    )

    shapes = list(rows)

    seshat_ids = [shape["seshat_id"] for shape in shapes if shape["seshat_id"]]

    polities = Polity.objects.filter(new_name__in=seshat_ids).values(
        "new_name", "id", "long_name"
    )

    polity_info = [
        (polity["new_name"], polity["id"], polity["long_name"])
        for polity in polities
    ]

    seshat_id_page_id = {
        new_name: {"id": id, "long_name": long_name or ""}
        for new_name, id, long_name in polity_info
    }

    if "migrate" not in sys.argv:
        result = VideoShapefile.objects.aggregate(
            min_year=Min("polity_start_year"), max_year=Max("polity_end_year")
        )
        earliest_year = result["min_year"]
        latest_year = result["max_year"]
        initial_displayed_year = earliest_year
    else:
        earliest_year, latest_year = 2014, 2014
        initial_displayed_year = -3400

    if override_earliest_year is not None:
        earliest_year = override_earliest_year
    if override_latest_year is not None:
        latest_year = override_latest_year

    if displayed_year == "all":
        displayed_year = initial_displayed_year

    if seshat_id != "all":  # Used in the polity pages
        earliest_year = min([shape["start_year"] for shape in shapes])
        displayed_year = earliest_year
        latest_year = max([shape["end_year"] for shape in shapes])

    # Get the years for the tick marks on the year slider
    tick_years = [
        round(year)
        for year in np.linspace(earliest_year, latest_year, num=tick_number)
    ]

    content = {
        "shapes": shapes,
        "earliest_year": earliest_year,
        "display_year": displayed_year,
        "tick_years": json.dumps(tick_years),
        "latest_year": latest_year,
        "seshat_id_page_id": seshat_id_page_id,
    }

    return content


def get_all_polity_capitals():
    """
    Get capital cities for polities that have them.

    Returns:
        dict: A dictionary containing the capital cities for polities.
    """
    # Try to get the capitals from the cache
    all_capitals_info = cache.get("all_capitals_info")

    if all_capitals_info is None:
        all_capitals_info = {}
        for polity in Polity.objects.all():
            caps = get_polity_capitals(polity.id)

            if caps:
                # Set the start and end years to be the same as the polity where missing
                modified_caps = caps
                i = 0
                for capital_info in caps:
                    if capital_info["year_from"] is None:
                        modified_caps[i]["year_from"] = polity.start_year
                    if capital_info["year_to"] is None:
                        modified_caps[i]["year_to"] = polity.end_year
                    i += 1
                all_capitals_info[polity.new_name] = modified_caps
        # Store the capitals in the cache for 1 hour
        cache.set("all_capitals_info", all_capitals_info, 3600)

    return all_capitals_info


def assign_variables_to_shapes(shapes, app_map):
    """
    Assign the absent/present variables to the shapes.

    Args:
        shapes (list): The shapes to assign the variables to.
        app_map (dict): A dictionary mapping app names to their long names.

    Returns:
        tuple: A tuple containing the shapes and the variables.
    """
    # Try to get the variables from the cache
    variables = cache.get("variables")
    if variables is None:
        variables = {}
        for app_name, app_name_long in app_map.items():
            variables[app_name_long] = {}
            for model in get_models(app_name):
                fields = list(model._meta.get_fields())

                for field in fields:
                    if (
                        hasattr(field, "choices")
                        and field.choices == ABSENT_PRESENT_CHOICES
                    ):
                        # Get the variable name and formatted name
                        if field.name == "coded_value":
                            # Use the class name lower case for rt models where coded_value
                            # is used
                            var_name = model.__name__.lower()
                            var_long = getattr(
                                model._meta,
                                "verbose_name_plural",
                                var_name,
                            )
                            if var_name == var_long:
                                variable_formatted = (
                                    var_name.capitalize().replace("_", " ")
                                )
                            else:
                                variable_formatted = var_long
                        else:  # Use the field name for other models
                            var_name = field.name
                            variable_formatted = (
                                field.name.capitalize().replace("_", " ")
                            )
                        variables[app_name_long][var_name] = {}
                        variables[app_name_long][var_name][
                            "formatted"
                        ] = variable_formatted
                        # Get the variable subsection and subsubsection if they exist
                        variable_full_name = variable_formatted
                        instance = model()
                        if hasattr(instance, "subsubsection"):
                            variable_full_name = (
                                instance.subsubsection()
                                + ": "
                                + variable_full_name
                            )
                        if hasattr(instance, "subsection"):
                            variable_full_name = (
                                instance.subsection()
                                + ": "
                                + variable_full_name
                            )
                        variables[app_name_long][var_name][
                            "full_name"
                        ] = variable_full_name

        # Store the variables in the cache for 1 hour
        cache.set("variables", variables, 3600)

    for app_name, app_name_long in app_map.items():

        app_variables_list = list(variables[app_name_long].keys())
        module_path = "seshat.apps." + app_name + ".models"
        module = __import__(
            module_path,
            fromlist=[
                variable.capitalize() for variable in app_variables_list
            ],
        )
        variable_classes = {
            variable: getattr(module, variable.capitalize())
            for variable in app_variables_list
        }

        seshat_ids = [
            shape["seshat_id"]
            for shape in shapes
            if shape["seshat_id"] != "none"
        ]
        polities = {
            polity.new_name: polity
            for polity in Polity.objects.filter(new_name__in=seshat_ids)
        }

        for variable, class_ in variable_classes.items():
            variable_formatted = variables[app_name_long][variable][
                "formatted"
            ]
            variable_objs = {
                obj.polity_id: obj
                for obj in class_.objects.filter(
                    polity_id__in=polities.values()
                )
            }

            all_variable_objs = {}
            for obj in class_.objects.filter(polity_id__in=polities.values()):
                try:
                    variable_value = getattr(obj, variable)
                except (
                    AttributeError
                ):  # For rt models where coded_value is used
                    variable_value = getattr(obj, "coded_value")
                if obj.polity_id not in all_variable_objs:
                    all_variable_objs[obj.polity_id] = {}
                all_variable_objs[obj.polity_id][variable_value] = [
                    obj.year_from,
                    obj.year_to,
                ]

            for shape in shapes:
                shape[variable_formatted] = "uncoded"  # Default value
                polity = polities.get(shape["seshat_id"])
                if polity:
                    variable_obj = variable_objs.get(polity.id)
                    try:
                        variable_obj_dict = all_variable_objs[polity.id]
                    except KeyError:
                        pass
                    if variable_obj:
                        try:
                            # Absent/present choice
                            shape[variable_formatted] = getattr(
                                variable_obj, variable
                            )
                            shape[variable_formatted + "_dict"] = (
                                variable_obj_dict
                            )
                        except AttributeError:
                            # For rt models where coded_value is used
                            shape[variable_formatted] = getattr(
                                variable_obj, "coded_value"
                            )
                            shape[variable_formatted + "_dict"] = (
                                variable_obj_dict
                            )
                else:
                    shape[variable_formatted] = "no seshat page"

    return shapes, variables


def assign_categorical_variables_to_shapes(shapes, variables):
    """
    Assign the categorical variables to the shapes.

    Note:
        Currently only language is implemented.

    Args:
        shapes (list): The shapes to assign the variables to.
        variables (dict): The variables to assign to the shapes.

    Returns:
        tuple: A tuple containing the shapes and the variables.
    """
    # Add language variables to the variables
    variables["General Variables"] = {
        "polity_linguistic_family": {
            "formatted": "linguistic_family",
            "full_name": "Linguistic Family",
        },
        "polity_language_genus": {
            "formatted": "language_genus",
            "full_name": "Language Genus",
        },
        "polity_language": {"formatted": "language", "full_name": "Language"},
    }

    # Fetch all polities and store them in a dictionary for quick access
    polities = {polity.new_name: polity for polity in Polity.objects.all()}

    # Fetch all linguistic families, language genuses, and languages and store them in
    # dictionaries for quick access
    linguistic_families = {}
    for lf in Polity_linguistic_family.objects.all():
        if lf.polity_id not in linguistic_families:
            linguistic_families[lf.polity_id] = []
        linguistic_families[lf.polity_id].append(lf)

    language_genuses = {}
    for lg in Polity_language_genus.objects.all():
        if lg.polity_id not in language_genuses:
            language_genuses[lg.polity_id] = []
        language_genuses[lg.polity_id].append(lg)

    languages = {}
    for language in Polity_language.objects.all():
        if language.polity_id not in languages:
            languages[language.polity_id] = []
        languages[language.polity_id].append(language)

    # Add language variable info to polity shapes
    for shape in shapes:
        shape["linguistic_family"] = []
        shape["linguistic_family_dict"] = {}
        shape["language_genus"] = []
        shape["language_genus_dict"] = {}
        shape["language"] = []
        shape["language_dict"] = {}
        if shape["seshat_id"] != "none":  # Skip shapes with no seshat_id
            polity = polities.get(shape["seshat_id"])
            if polity:
                # Get the linguistic family, language genus, and language for the polity
                shape["linguistic_family"].extend(
                    [
                        lf.linguistic_family
                        for lf in linguistic_families.get(polity.id, [])
                    ]
                )
                shape["language_genus"].extend(
                    [
                        lg.language_genus
                        for lg in language_genuses.get(polity.id, [])
                    ]
                )
                shape["language"].extend(
                    [lang.language for lang in languages.get(polity.id, [])]
                )

                # Get the years for the linguistic family, language genus, and language for
                # the polity
                shape["linguistic_family_dict"].update(
                    {
                        lf.linguistic_family: [lf.year_from, lf.year_to]
                        for lf in linguistic_families.get(polity.id, [])
                    }
                )
                shape["language_genus_dict"].update(
                    {
                        lg.language_genus: [lg.year_from, lg.year_to]
                        for lg in language_genuses.get(polity.id, [])
                    }
                )
                shape["language_dict"].update(
                    {
                        lang.language: [lang.year_from, lang.year_to]
                        for lang in languages.get(polity.id, [])
                    }
                )

        # If no linguistic family, language genus, or language was found, append 'Uncoded'
        polity = polities.get(shape["seshat_id"])
        if polity:
            if not shape["linguistic_family"]:
                shape["linguistic_family"].append("Uncoded")
            if not shape["language_genus"]:
                shape["language_genus"].append("Uncoded")
            if not shape["language"]:
                shape["language"].append("Uncoded")
        else:
            if not shape["linguistic_family"]:
                shape["linguistic_family"].append("No Seshat page")
            if not shape["language_genus"]:
                shape["language_genus"].append("No Seshat page")
            if not shape["language"]:
                shape["language"].append("No Seshat page")

    return shapes, variables


# Get all the variables used in the map view
app_map = {
    "sc": "Social Complexity Variables",
    "wf": "Warfare Variables (Military Technologies)",
    # TODO: Implemented but temporarily restricted. Uncomment when ready.
    # 'rt': 'Religion Tolerance',
    # TODO: Partially implmented and hardcoded in assign_categorical_variables_to_shapes.
    # 'general': 'General Variables',
}

# Get sorted lists of choices for each categorical variable
categorical_variables = {
    "linguistic_family": sorted(
        [x[0] for x in POLITY_LINGUISTIC_FAMILY_CHOICES]
    ),
    "language_genus": sorted([x[0] for x in POLITY_LANGUAGE_GENUS_CHOICES]),
    "language": sorted([x[0] for x in POLITY_LANGUAGE_CHOICES]),
}


def random_polity_shape():
    """
    This function is used to get a random polity for the world map initial view.
    It selects a polity with a seshat_id and a start year.

    Use the VideoShapefile model to get the polity shapes.
    Choose one that has a seshat_id.
    Return the seshat_id and start year.

    Returns:
        tuple: A tuple containing the start year and seshat_id.
    """
    max_id = VideoShapefile.objects.filter(seshat_id__isnull=False).aggregate(
        max_id=Max("id")
    )["max_id"]
    while True:
        pk = random.randint(1, max_id)
        shape = VideoShapefile.objects.filter(
            seshat_id__isnull=False, id=pk
        ).first()
        if shape:
            if shape.seshat_id and shape.area > 600000:  # Big empires only
                break
    return shape.start_year, shape.seshat_id


def common_map_view_content(content):
    """
    Set of functions that update content and run in each map view function.

    Args:
        content (dict): The content for the polity shapes.

    Returns:
        dict: The updated content for the polity shapes.
    """
    # Add in the present/absent variables to view for the shapes
    content["shapes"], content["variables"] = assign_variables_to_shapes(
        content["shapes"], app_map
    )

    # Add in the categorical variables to view for the shapes
    content["shapes"], content["variables"] = (
        assign_categorical_variables_to_shapes(
            content["shapes"], content["variables"]
        )
    )

    # Load the capital cities for polities that have them
    content["all_capitals_info"] = get_all_polity_capitals()

    # Add categorical variable choices to content for dropdown selection
    content["categorical_variables"] = categorical_variables

    # Set the initial polity to highlight
    content["world_map_initial_polity"] = world_map_initial_polity

    return content


# World map defalut settings
world_map_initial_displayed_year = 117
world_map_initial_polity = "it_roman_principate"


def world_map_view(request):
    global world_map_initial_displayed_year, world_map_initial_polity
    """
    This view is used to display a map with polities plotted on it. The initial
    view just loads a polity with a seshat_id picked at random and sets the
    display year to that polity start year.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """

    # Check if 'year' parameter is different from the world_map_initial_displayed_year or
    # not present then redirect
    if "year" in request.GET:
        if request.GET["year"] != str(world_map_initial_displayed_year):
            return redirect(
                "{}?year={}".format(
                    request.path, world_map_initial_displayed_year
                )
            )
    else:
        # Select a random polity for the initial view
        if "test" not in sys.argv:
            world_map_initial_displayed_year, world_map_initial_polity = (
                random_polity_shape()
            )
        return redirect(
            "{}?year={}".format(request.path, world_map_initial_displayed_year)
        )

    content = get_polity_shape_content(seshat_id=world_map_initial_polity)

    content = common_map_view_content(content)

    # For the initial view, set the displayed year to the polity's start year
    content["display_year"] = world_map_initial_displayed_year

    return render(request, "core/world_map.html", content)


def world_map_one_year_view(request):
    """
    This view is used to display a map with polities plotted on it. The view
    loads all polities present in the year in the url.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The HTTP response with serialized JSON.
    """
    year = request.GET.get("year", world_map_initial_displayed_year)
    content = get_polity_shape_content(displayed_year=year)

    content = common_map_view_content(content)

    return JsonResponse(content)


def world_map_all_view(request):
    """
    This view is used to display a map with polities plotted on it. The view
    loads all polities for the range of years.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The HTTP response with serialized JSON.
    """

    # Temporary restriction on the latest year for the whole map view
    content = get_polity_shape_content(override_latest_year=2014)

    content = common_map_view_content(content)

    return JsonResponse(content)


def provinces_and_countries_view(request):
    """
    This view is used to get the provinces and countries for the map.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The HTTP response with serialized JSON.
    """
    provinces = get_provinces()
    countries = get_provinces(selected_base_map_gadm="country")

    content = {
        "provinces": provinces,
        "countries": countries,
    }

    return JsonResponse(content)


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

    return render(
        request,
        "core/seshatcomments/seshatcommentpart_update2.html",
        {
            "form": form,
            "formset": formset,
            "comm_num": pk,
            "comm_part_display": comment_part,
            "parent_comment": parent_comment_part,
            "subcom_order": subcomment_order,
        },
    )


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
                to_be_added = []
                to_be_deleted_later = []
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
                            pass  # Handle the exception as per your requirement

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

    return render(
        request, "core/seshatcomments/your_template.html", {"form": form}
    )


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

            for _, subcomment_form in enumerate(comment_formset):
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
                    reference_formset = ReferenceFormSet(
                        request.POST, prefix="refs"
                    )  # noqa: E501   TODO: This will crash  pylint: disable=C0301

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

                                citation, _ = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to),
                                )

                                # Associate the Citation with the SeshatCommentPart
                                comment_part.comment_citations.add(citation)
                            except:  # noqa: E722  TODO: Don't use bare except
                                # TODO: Handle exception
                                pass
                        else:
                            # TODO: Handle error differently
                            print(f"Form errors: {reference_form.errors}")

            # Redirect to a success page
            return redirect("seshat-index")

    elif request.method == "GET":
        form = SeshatCommentForm2()

    return render(
        request,
        "core/seshatcomments/seshatcomment_create.html",
        {"form": form},
    )


def search_view(request):
    """
    View to search for a polity.

    Note:
        This view can handle GET requests.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    search_term = request.GET.get("search", "")

    if search_term:
        try:
            polity = Polity.objects.filter(name__icontains=search_term).first()

            if polity:
                return redirect("polity-detail-main", pk=polity.pk)
            else:
                # No polity found = redirect to home
                return redirect("seshat-index")
        except Polity.DoesNotExist:
            # Handle the case where no polity matches the search term
            pass

    # Redirect to home if no search term is provided or no match is found
    return redirect("seshat-index")


def search_suggestions_view(request):
    """
    View to get search suggestions for a polity.

    Note:
        This view can handle GET requests.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    search_term = request.GET.get("search", "")

    # TODO? Limit to 5 suggestions [:5]
    context = {
        "polities": Polity.objects.filter(
            Q(name__icontains=search_term)
            | Q(long_name__icontains=search_term)
            | Q(new_name__icontains=search_term)
        ).order_by("start_year")
    }

    return render(request, "core/partials/_search_suggestions.html", context)


def get_polity_capitals(pk):
    """
    Get all the capitals for a polity and coordinates.

    Args:
        pk (int): The primary key of the polity.

    Returns:
        list: A list of dictionaries containing the capital name, latitude,
            longitude, start year (or 0 or None if they aren't present in the
            database), and end year (or 0 or None if they aren't present in
            the database).
    """
    capitals_info = []
    for polity_capital in Polity_capital.objects.filter(polity_id=pk):
        capitals = Capital.objects.filter(name=polity_capital.capital)

        for capital in capitals:
            if capital.name and capital.latitude and capital.longitude:
                capital_info = {
                    "capital": capital.name,
                    "latitude": float(capital.latitude),
                    "longitude": float(capital.longitude),
                }

                if polity_capital.year_from == 0:
                    capital_info["year_from"] = 0
                elif polity_capital.year_from is not None:
                    capital_info["year_from"] = polity_capital.year_from
                else:
                    capital_info["year_from"] = None

                if polity_capital.year_to == 0:
                    capital_info["year_to"] = 0
                elif polity_capital.year_to is not None:
                    capital_info["year_to"] = polity_capital.year_to
                else:
                    capital_info["year_to"] = None

                capitals_info.append(capital_info)

    return capitals_info
