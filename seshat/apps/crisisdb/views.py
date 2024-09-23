from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

import csv

from ..accounts.models import Seshat_Expert
from ..core.models import (
    Citation,
    SeshatComment,
    SeshatCommentPart,
    Polity,
)
from ..general.mixins import PolityIdMixin
from ..constants import (
    POLITY_NGA_NAME,
)
from ..utils import (
    check_permissions,
    get_date,
    get_api_results,
)

from .forms import (
    Power_transitionForm,
    Crisis_consequenceForm,
    Human_sacrificeForm,
    External_conflictForm,
    Internal_conflictForm,
    External_conflict_sideForm,
    Agricultural_populationForm,
    Arable_landForm,
    Arable_land_per_farmerForm,
    Gross_grain_shared_per_agricultural_populationForm,
    Net_grain_shared_per_agricultural_populationForm,
    SurplusForm,
    Military_expenseForm,
    Silver_inflowForm,
    Silver_stockForm,
    Total_populationForm,
    Gdp_per_capitaForm,
    Drought_eventForm,
    Locust_eventForm,
    Socioeconomic_turmoil_eventForm,
    Crop_failure_eventForm,
    Famine_eventForm,
    Disease_outbreakForm,
    Us_locationForm,
    Us_violence_subtypeForm,
    Us_violence_data_sourceForm,
    Us_violenceForm,
)
from .models import (
    Power_transition,
    Crisis_consequence,
    Human_sacrifice,
    External_conflict,
    Internal_conflict,
    External_conflict_side,
    Agricultural_population,
    Arable_land,
    Arable_land_per_farmer,
    Gross_grain_shared_per_agricultural_population,
    Net_grain_shared_per_agricultural_population,
    Surplus,
    Military_expense,
    Silver_inflow,
    Silver_stock,
    Total_population,
    Gdp_per_capita,
    Drought_event,
    Locust_event,
    Socioeconomic_turmoil_event,
    Crop_failure_event,
    Famine_event,
    Disease_outbreak,
    Us_location,
    Us_violence_subtype,
    Us_violence_data_source,
    Us_violence,
)
from .constants import (
    ALL_VARS_IN_SECTIONS,
    ALL_VARS_WITH_HIERARCHY,
    TAGS_DIC,
    NO_SECTION_DICT,
    QING_VARS,
)
from .utils import expand_context_from_variable_hierarchy


def get_citations_dropdown_view(request):
    """
    Get all citations as JSON.

    Args:
        request: HttpRequest object

    Returns:
        JsonResponse: JSON response with all citations for dropdown
    """
    # Get dropdown data here
    data = Citation.objects.all()
    citations_list = []
    for counter, item in enumerate(data):
        if counter < 5000:
            citations_list.append(
                {
                    "id": item.id,
                    "name": item.__str__(),
                }
            )

    # Return dropdown template as JSON response
    return JsonResponse({"data": citations_list})


class Crisis_consequenceCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Crisis_consequence instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crisis_consequence
    form_class = Crisis_consequenceForm
    success_url = reverse_lazy("crisis_consequences_all")
    template_name = "crisisdb/crisis_consequence/crisis_consequence_form.html"
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        url = reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})

        return f"{url}#crisis_case_var"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("crisis_consequence-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **NO_SECTION_DICT,
            **{
                "my_exp": self.model.Code.description,
                "mytitle": "Add a NEW crisis case below:",
                "mysubtitle": "Please complete the form below to create a new Crisis Case:",
            },
        )

        return context


class Crisis_consequenceUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Crisis_consequence instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crisis_consequence
    success_url = reverse_lazy("crisis_consequences_all")
    form_class = Crisis_consequenceForm
    template_name = "crisisdb/crisis_consequence/crisis_consequence_form.html"
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        return (
            reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})
            + "#crisis_case_var"
        )

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Z",
                "mytitle": "Update the crisis case below:",
                "mysubtitle": "Please complete the form below to update the Crisis Case:",
            },
        )

        return context


class Crisis_consequenceCreateHeavyView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Crisis_consequence instance.

    Note:
        This view is for creating a new Crisis_consequence instance with a heavy form.
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crisis_consequence
    form_class = Crisis_consequenceForm
    success_url = reverse_lazy("crisis_consequences_all")
    template_name = (
        "crisisdb/crisis_consequence/crisis_consequence_form_heavy.html"
    )
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        return (
            reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})
            + "#crisis_case_var"
        )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("crisis_consequence-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **NO_SECTION_DICT,
            **{
                "my_exp": self.model.Code.description,
                "mytitle": "Add a NEW crisis case below:",
                "mysubtitle": "Please complete the form below to create a new Crisis Case:",
            },
        )

        return context


class Crisis_consequenceUpdateHeavyView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Crisis_consequence instance.

    Note:
        This view is for updating an existing Crisis_consequence instance with a heavy form.
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crisis_consequence
    success_url = reverse_lazy("crisis_consequences_all")
    form_class = Crisis_consequenceForm
    template_name = (
        "crisisdb/crisis_consequence/crisis_consequence_form_heavy.html"
    )
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        return (
            reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})
            + "#crisis_case_var"
        )

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Z",
                "mytitle": "Update the crisis case below:",
                "mysubtitle": "Please complete the form below to update the Crisis Case:",
            },
        )

        return context


class Crisis_consequenceDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Crisis_consequence instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crisis_consequence
    success_url = reverse_lazy("crisis_consequences_all")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Crisis_consequenceListView(PermissionRequiredMixin, ListView):
    """
    View for listing all Crisis_consequence instances.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crisis_consequence
    template_name = "crisisdb/crisis_consequence/crisis_consequence_list.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("crisis_consequences")

    def get_queryset(self):
        """
        Get the queryset for the view.

        Returns:
            QuerySet: QuerySet for the view
        """
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year_from")

        new_context = (
            Crisis_consequence.objects.all()
            .annotate(home_nga=POLITY_NGA_NAME)
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "fields": [
                    "decline",
                    "collapse",
                    "epidemic",
                    "downward_mobility",
                    "extermination",
                    "uprising",
                    "revolution",
                    "successful_revolution",
                    "civil_war",
                    "century_plus",
                    "fragmentation",
                    "capital",
                    "conquest",
                    "assassination",
                    "depose",
                    "constitution",
                    "labor",
                    "unfree_labor",
                    "suffrage",
                    "public_goods",
                    "religion",
                ],
                "myvar": "XX",
                "var_main_desc": "YY",
                "var_main_desc_source": "",
                "var_section": "frffrr",
                "var_subsection": "frtgtz",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "crisis_consequence": {
                        "min": None,
                        "max": None,
                        "scale": 1000,
                        "var_exp_source": None,
                        "var_exp": "No Explanations.",
                        "units": "mu?",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Crisis_consequenceListAllView(PermissionRequiredMixin, ListView):
    """
    View for listing all Crisis_consequence instances.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crisis_consequence
    template_name = (
        "crisisdb/crisis_consequence/crisis_consequence_list_all.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("crisis_consequences_all")

    def get_queryset(self):
        """
        Get the queryset for the view.

        Returns:
            QuerySet: QuerySet for the view
        """
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year_from")

        new_context = (
            Crisis_consequence.objects.all()
            .annotate(home_nga=POLITY_NGA_NAME)
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,  # noqa: E501  TODO: This was "uu" in the original code
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "Religion and Normative Ideology",
                "var_subsection": "",  # TODO: This was "uu" in the original code
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Crisis_consequenceDetailView(PermissionRequiredMixin, DetailView):
    """
    View for displaying a single Crisis_consequence instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crisis_consequence
    template_name = (
        "crisisdb/crisis_consequence/crisis_consequence_detail.html"
    )
    permission_required = "core.add_capital"


class Power_transitionCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Power_transition instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Power_transition
    form_class = Power_transitionForm
    success_url = reverse_lazy("power_transitions_all")
    template_name = "crisisdb/power_transition/power_transition_form.html"
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        return (
            reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})
            + "#power_transition_var"
        )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("power_transition-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **NO_SECTION_DICT,
            **{
                "my_exp": self.model.Code.description,
                "mytitle": "Add a NEW power transition below:",
                "mysubtitle": "Please complete the form below to create a new power transition:",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Power_transitionUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Power_transition instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Power_transition
    success_url = reverse_lazy("power_transitions_all")
    form_class = Power_transitionForm
    template_name = "crisisdb/power_transition/power_transition_update.html"
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        return (
            reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})
            + "#power_transition_var"
        )

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Z",
                "mytitle": "Update the power transition below:",
                "mysubtitle": "Please complete the form below to update the power transition:",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Power_transitionCreateHeavyView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Power_transition instance.

    Note:
        This view is for creating a new Power_transition instance with a heavy form.
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Power_transition
    form_class = Power_transitionForm
    success_url = reverse_lazy("power_transitions_all")
    template_name = (
        "crisisdb/power_transition/power_transition_form_heavy.html"
    )
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        return (
            reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})
            + "#power_transition_var"
        )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("power_transition-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **NO_SECTION_DICT,
            **{
                "my_exp": self.model.Code.description,
                "mytitle": "Add a NEW power transition below:",
                "mysubtitle": "Please complete the form below to create a new power transition:",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Power_transitionUpdateHeavyView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Power_transition instance.

    Note:
        This view is for updating an existing Power_transition instance with a heavy form.
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Power_transition
    success_url = reverse_lazy("power_transitions_all")
    form_class = Power_transitionForm
    template_name = (
        "crisisdb/power_transition/power_transition_form_heavy.html"
    )
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        return (
            reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})
            + "#power_transition_var"
        )

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Z",
                "mytitle": "Update the power transition below:",
                "mysubtitle": "Please complete the form below to update the power transition:",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Power_transitionDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Power_transition instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Power_transition
    success_url = reverse_lazy("power_transitions")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Power_transitionListView(PermissionRequiredMixin, ListView):
    """
    View for listing all Power_transition instances.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Power_transition
    template_name = "crisisdb/power_transition/power_transition_list.html"
    permission_required = "core.add_capital"

    paginate_by = 500

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("power_transitions")

    def get_queryset(self):
        """
        Get the queryset for the view.

        Returns:
            QuerySet: QuerySet for the view
        """
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year_from")

        new_context = (
            Power_transition.objects.all()
            .annotate(home_nga=POLITY_NGA_NAME)
            .order_by(order2, order)
        )
        return new_context

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "fields": [
                    "contested",
                    "overturn",
                    "predecessor_assassination",
                    "intra_elite",
                    "military_revolt",
                    "popular_uprising",
                    "separatist_rebellion",
                    "external_invasion",
                    "external_interference",
                ],
                "myvar": "XX",
                "var_main_desc": "YY",
                "var_main_desc_source": "",
                "var_section": "frffrr",
                "var_subsection": "frtgtz",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "power_transition": {
                        "min": None,
                        "max": None,
                        "scale": 1000,
                        "var_exp_source": None,
                        "var_exp": "No Explanations.",
                        "units": "mu?",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Power_transitionListAllView(PermissionRequiredMixin, ListView):
    """
    View for listing all Power_transition instances.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Power_transition
    template_name = (
        "crisisdb/power_transition/power_transition_list_all_new.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("power_transitions_all")

    def get_queryset(self):
        """
        Get the queryset for the view.

        Returns:
            QuerySet: QuerySet for the view
        """
        order = self.request.GET.get("orderby", "year_to")
        order2 = self.request.GET.get("orderby2", "year_from")

        power_transitions = Power_transition.objects.all().order_by(
            order2, order
        )

        pols_dict = {
            transition.polity_id
            or 0: {
                "polity_new_name": getattr(
                    transition.polity, "new_name", "NO_NAME"
                ),
                "polity_long_name": getattr(
                    transition.polity, "long_name", "NO_LONG_NAME"
                ),
                "polity_start_year": getattr(
                    transition.polity, "start_year", -10000
                ),
                "polity_end_year": getattr(
                    transition.polity, "end_year", 2000
                ),
                "trans_list": [],
            }
            for transition in power_transitions
        }

        for transition in power_transitions:
            pols_dict[transition.polity_id or 0]["trans_list"].append(
                {
                    "year_from": transition.year_from,
                    "year_to": transition.year_to,
                    "predecessor": transition.predecessor,
                    "successor": transition.successor,
                    "name": transition.name,
                    "trans_id": transition.id,
                    "overturn": transition.overturn,
                    "predecessor_assassination": transition.predecessor_assassination,
                    "intra_elite": transition.intra_elite,
                    "military_revolt": transition.military_revolt,
                    "popular_uprising": transition.popular_uprising,
                    "separatist_rebellion": transition.separatist_rebellion,
                    "external_invasion": transition.external_invasion,
                    "external_interference": transition.external_interference,
                }
            )

        return pols_dict

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "Religion and Normative Ideology",
                "var_subsection": "",  # noqa: E501  TODO: this was set to "uu" which doesn't seem correct  pylint: disable=C0301
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Power_transitionDetailView(PermissionRequiredMixin, DetailView):
    """
    View for displaying a single Power_transition instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Power_transition
    template_name = "crisisdb/power_transition/power_transition_detail.html"
    permission_required = "core.add_capital"


class Human_sacrificeCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Human_sacrifice instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Human_sacrifice
    form_class = Human_sacrificeForm
    template_name = "crisisdb/human_sacrifice/human_sacrifice_form.html"
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        return (
            reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})
            + "#hs_var"
        )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("human_sacrifice-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Human_sacrifice", "Human Sacrifice"
        )  # noqa: E501 pylint: disable=C0301

        return context

    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form: Form to validate

        Returns:
            HttpResponse: HTTP response
        """
        parent_comment = SeshatComment.objects.get(pk=1)
        form.instance.comment = parent_comment

        return super().form_valid(form)


class Human_sacrificeUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Human_sacrifice instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Human_sacrifice
    form_class = Human_sacrificeForm
    template_name = "crisisdb/human_sacrifice/human_sacrifice_update.html"
    permission_required = "core.add_capital"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: URL to redirect to
        """
        return (
            reverse("polity-detail-main", kwargs={"pk": self.object.polity.id})
            + "#hs_var"
        )

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(context, **{"myvar": "Human Sacrifice"})

        return context


class Human_sacrificeDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Human_sacrifice instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Human_sacrifice
    success_url = reverse_lazy("human_sacrifices")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Human_sacrificeListView(PermissionRequiredMixin, ListView):
    """
    View for listing all Human_sacrifice instances.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    """

    model = Human_sacrifice
    template_name = "crisisdb/human_sacrifice/human_sacrifice_list.html"
    paginate_by = 50
    permission_required = "core.view_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("human_sacrifices")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "Religion and Normative Ideology",
                "var_subsection": "Human Sacrifice",
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": [],
            },
        )

        return context


class Human_sacrificeListAllView(PermissionRequiredMixin, ListView):
    """
    View for listing all Human_sacrifice instances.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    """

    model = Human_sacrifice
    template_name = "crisisdb/human_sacrifice/human_sacrifice_list_all.html"
    permission_required = "core.view_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("human_sacrifices_all")

    def get_queryset(self):
        """
        Get the queryset for the view.

        Returns:
            QuerySet: QuerySet for the view
        """
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year_from")

        new_context = (
            Human_sacrifice.objects.all()
            .annotate(home_nga=POLITY_NGA_NAME)
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "Religion and Normative Ideology",
                "var_subsection": "Human Sacrifice",
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Human_sacrificeDetailView(PermissionRequiredMixin, DetailView):
    """
    View for displaying a single Human_sacrifice instance.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    """

    model = Human_sacrifice
    template_name = "crisisdb/human_sacrifice/human_sacrifice_detail.html"
    permission_required = "core.view_capital"


@login_required
def create_a_comment_with_a_subcomment(request, hs_instance_id):
    """
    Create a new comment instance with a subcomment and save them to the database.

    Note:
        This view is only accessible to authenticated users.

    Args:
        request: HttpRequest object
        hs_instance_id: ID of the Human_sacrifice instance

    Returns:
        HttpResponse: HTTP response
    """

    """
    Upon calling this function, I want to create a subcomment and assign it to a comment
    and then assign the comment to the model_name with id=hs_instance_id.
    """
    # Create a new comment instance and save it to the database
    comment_instance = SeshatComment.objects.create(text="a new_comment_text")

    # Get the Seshat_Expert instance associated with the user
    try:
        seshat_expert_instance = Seshat_Expert.objects.get(user=request.user)
    except Seshat_Expert.DoesNotExist:
        seshat_expert_instance = None

    # Create the subcomment instance and save it to the database
    SeshatCommentPart.objects.create(
        comment_part_text="A subdescription text placeholder (to be edited)",
        comment=comment_instance,
        comment_curator=seshat_expert_instance,
        comment_order=1,
    )

    # Get the ModelName instance
    hs_instance = Human_sacrifice.objects.get(id=hs_instance_id)

    # Assign the comment to the ModelName instance
    hs_instance.comment = comment_instance

    hs_instance.save()

    return redirect("seshatcomment-update", pk=comment_instance.id)


class External_conflictCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new External_conflict instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = External_conflict
    form_class = External_conflictForm
    template_name = "crisisdb/external_conflict/external_conflict_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("external_conflict-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "External_conflict", "External Conflict"
        )  # noqa: E501 pylint: disable=C0301

        return context


class External_conflictUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing External_conflict instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = External_conflict
    form_class = External_conflictForm
    template_name = "crisisdb/external_conflict/external_conflict_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(context, **{"myvar": "External Conflict"})

        return context


class External_conflictDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing External_conflict instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = External_conflict
    success_url = reverse_lazy("external_conflicts")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class External_conflictListView(ListView):
    """
    View for listing all External_conflict instances.
    """

    model = External_conflict
    template_name = "crisisdb/external_conflict/external_conflict_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("external_conflicts")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "External Conflict",
                "var_main_desc": "Main Descriptions for the Variable external Conflict are missing!",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "",
                "var_section": "Conflict Variables",
                "var_subsection": "External Conflicts Subsection",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "conflict_name": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The unique name of this external conflict",
                        "units": None,
                        "choices": None,
                    }
                },
                "potential_cols": [],
            },
        )

        return context


class External_conflictDetailView(DetailView):
    """
    View for displaying a single External_conflict instance.
    """

    model = External_conflict
    template_name = "crisisdb/external_conflict/external_conflict_detail.html"


class Internal_conflictCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Internal_conflict instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Internal_conflict
    form_class = Internal_conflictForm
    template_name = "crisisdb/internal_conflict/internal_conflict_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("internal_conflict-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Internal_conflict", "Internal Conflict"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Internal_conflictUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Internal_conflict instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Internal_conflict
    form_class = Internal_conflictForm
    template_name = "crisisdb/internal_conflict/internal_conflict_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(context, **{"myvar": "Internal Conflict"})

        return context


class Internal_conflictDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Internal_conflict instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Internal_conflict
    success_url = reverse_lazy("internal_conflicts")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Internal_conflictListView(ListView):
    """
    View for listing all Internal_conflict instances.
    """

    model = Internal_conflict
    template_name = "crisisdb/internal_conflict/internal_conflict_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("internal_conflicts")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Internal Conflict",
                "var_main_desc": "Main Descriptions for the Variable internal Conflict are missing!",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "",
                "var_section": "Conflict Variables",
                "var_subsection": "Internal Conflicts Subsection",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "conflict": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The name of the conflict",
                        "units": None,
                        "choices": None,
                    },
                    "expenditure": {
                        "min": None,
                        "max": None,
                        "scale": 1000000,
                        "var_exp_source": None,
                        "var_exp": "The military expenses in millions silver taels.",
                        "units": "silver taels",
                        "choices": None,
                    },
                    "leader": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The leader of the conflict",
                        "units": None,
                        "choices": None,
                    },
                    "casualty": {
                        "min": None,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "The number of people who died in this conflict.",
                        "units": "People",
                        "choices": None,
                    },
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Internal_conflictDetailView(DetailView):
    """
    View for displaying a single Internal_conflict instance.
    """

    model = Internal_conflict
    template_name = "crisisdb/internal_conflict/internal_conflict_detail.html"


class External_conflict_sideCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new External_conflict_side instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = External_conflict_side
    form_class = External_conflict_sideForm
    template_name = (
        "crisisdb/external_conflict_side/external_conflict_side_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("external_conflict_side-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "External_conflict_side", "External Conflict Side"
        )  # noqa: E501 pylint: disable=C0301

        return context


class External_conflict_sideUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing External_conflict_side instance (side).

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = External_conflict_side
    form_class = External_conflict_sideForm
    template_name = (
        "crisisdb/external_conflict_side/external_conflict_side_update.html"
    )
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(context, **{"myvar": "External Conflict Side"})

        return context


class External_conflict_sideDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing External_conflict_side instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = External_conflict_side
    success_url = reverse_lazy("external_conflict_sides")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class External_conflict_sideListView(ListView):
    """
    View for listing all External_conflict_side instances.
    """

    model = External_conflict_side
    template_name = (
        "crisisdb/external_conflict_side/external_conflict_side_list.html"
    )
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("external_conflict_sides")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "External Conflict Side",
                "var_main_desc": "Main Descriptions for the Variable external Conflict Side are missing!",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "",
                "var_section": "Conflict Variables",
                "var_subsection": "External Conflicts Subsection",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "conflict_id": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The external_conflict which is the actual conflict we are talking about",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": None,
                    },
                    "expenditure": {
                        "min": None,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "The military expenses (from this side) in silver taels.",  # noqa: E501 pylint: disable=C0301
                        "units": "silver taels",
                        "choices": None,
                    },
                    "leader": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The leader of this side of conflict",
                        "units": None,
                        "choices": None,
                    },
                    "casualty": {
                        "min": None,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "The number of people who died (from this side) in this conflict.",  # noqa: E501 pylint: disable=C0301
                        "units": "People",
                        "choices": None,
                    },
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class External_conflict_sideDetailView(DetailView):
    """
    View for displaying a single External_conflict_side instance.
    """

    model = External_conflict_side
    template_name = (
        "crisisdb/external_conflict_side/external_conflict_side_detail.html"
    )


class Agricultural_populationCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Agricultural_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Agricultural_population
    form_class = Agricultural_populationForm
    template_name = (
        "crisisdb/agricultural_population/agricultural_population_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("agricultural_population-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Agricultural_population", "Agricultural Population"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Agricultural_populationUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Agricultural_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Agricultural_population
    form_class = Agricultural_populationForm
    template_name = (
        "crisisdb/agricultural_population/agricultural_population_update.html"
    )
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(context, **{"myvar": "Agricultural Population"})

        return context


class Agricultural_populationDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Agricultural_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Agricultural_population
    success_url = reverse_lazy("agricultural_populations")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Agricultural_populationListView(ListView):
    """
    View for listing all Agricultural_population instances.
    """

    model = Agricultural_population
    template_name = (
        "crisisdb/agricultural_population/agricultural_population_list.html"
    )
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("agricultural_populations")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Agricultural Population",
                "var_main_desc": "Main Descriptions for the Variable agricultural Population are missing!",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "",
                "var_section": "Economy Variables",
                "var_subsection": "Productivity",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "agricultural_population": {
                        "min": 0,
                        "max": None,
                        "scale": 1000,
                        "var_exp_source": None,
                        "var_exp": "No Explanations.",
                        "units": "People",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Agricultural_populationDetailView(DetailView):
    """
    View for displaying a single Agricultural_population instance.
    """

    model = Agricultural_population
    template_name = (
        "crisisdb/agricultural_population/agricultural_population_detail.html"
    )


class Arable_landCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Arable_land instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Arable_land
    form_class = Arable_landForm
    template_name = "crisisdb/arable_land/arable_land_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("arable_land-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Arable_land", "Arable Land"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Arable_landUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Arable_land instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Arable_land
    form_class = Arable_landForm
    template_name = "crisisdb/arable_land/arable_land_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(context, **{"myvar": "Arable Land"})

        return context


class Arable_landDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Arable_land instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Arable_land
    success_url = reverse_lazy("arable_lands")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Arable_landListView(ListView):
    """
    View for listing all Arable_land instances.
    """

    model = Arable_land
    template_name = "crisisdb/arable_land/arable_land_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("arable_lands")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Arable Land",
                "var_main_desc": "Main Descriptions for the Variable arable Land are missing!",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "",
                "var_section": "Economy Variables",
                "var_subsection": "Productivity",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "arable_land": {
                        "min": None,
                        "max": None,
                        "scale": 1000,
                        "var_exp_source": None,
                        "var_exp": "No Explanations.",
                        "units": "mu?",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Arable_landDetailView(DetailView):
    """
    View for displaying a single Arable_land instance.
    """

    model = Arable_land
    template_name = "crisisdb/arable_land/arable_land_detail.html"


class Arable_land_per_farmerCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Arable_land_per_farmer instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Arable_land_per_farmer
    form_class = Arable_land_per_farmerForm
    template_name = (
        "crisisdb/arable_land_per_farmer/arable_land_per_farmer_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("arable_land_per_farmer-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Arable_land_per_farmer", "Arable Land Per Farmer"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Arable_land_per_farmerUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Arable_land_per_farmer instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Arable_land_per_farmer
    form_class = Arable_land_per_farmerForm
    template_name = (
        "crisisdb/arable_land_per_farmer/arable_land_per_farmer_update.html"
    )
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Arable Land Per Farmer",
            },
        )

        return context


class Arable_land_per_farmerDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Arable_land_per_farmer instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Arable_land_per_farmer
    success_url = reverse_lazy("arable_land_per_farmers")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Arable_land_per_farmerListView(ListView):
    """
    View for listing all Arable_land_per_farmer instances.
    """

    model = Arable_land_per_farmer
    template_name = (
        "crisisdb/arable_land_per_farmer/arable_land_per_farmer_list.html"
    )
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("arable_land_per_farmers")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Arable Land Per Farmer",
                "var_main_desc": "No explanations.",
                "var_main_desc_source": "",
                "var_section": "Economy Variables",
                "var_subsection": "Productivity",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "arable_land_per_farmer": {
                        "min": None,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "No Explanations.",
                        "units": "mu?",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Arable_land_per_farmerDetailView(DetailView):
    """
    View for displaying a single Arable_land_per_farmer instance.
    """

    model = Arable_land_per_farmer
    template_name = (
        "crisisdb/arable_land_per_farmer/arable_land_per_farmer_detail.html"
    )


class Gross_grain_shared_per_agricultural_populationCreateView(
    PermissionRequiredMixin, CreateView
):
    """
    View for creating a new Gross_grain_shared_per_agricultural_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Gross_grain_shared_per_agricultural_population
    form_class = Gross_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("gross_grain_shared_per_agricultural_population-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context,
            "Gross_grain_shared_per_agricultural_population",
            "Gross Grain Shared Per Agricultural Population",
        )  # noqa: E501 pylint: disable=C0301

        return context


class Gross_grain_shared_per_agricultural_populationUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Gross_grain_shared_per_agricultural_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Gross_grain_shared_per_agricultural_population
    form_class = Gross_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Gross Grain Shared Per Agricultural Population",
            },
        )

        return context


class Gross_grain_shared_per_agricultural_populationDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Gross_grain_shared_per_agricultural_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Gross_grain_shared_per_agricultural_population
    success_url = reverse_lazy(
        "gross_grain_shared_per_agricultural_populations"
    )
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Gross_grain_shared_per_agricultural_populationListView(ListView):
    """
    View for listing all Gross_grain_shared_per_agricultural_population instances.
    """

    model = Gross_grain_shared_per_agricultural_population
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("gross_grain_shared_per_agricultural_populations")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Gross Grain Shared Per Agricultural Population",
                "var_main_desc": "No explanations.",
                "var_main_desc_source": "",
                "var_section": "Economy Variables",
                "var_subsection": "Productivity",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "gross_grain_shared_per_agricultural_population": {
                        "min": None,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "No Explanations.",
                        "units": "(catties per capita)",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Gross_grain_shared_per_agricultural_populationDetailView(DetailView):
    """
    View for displaying a single Gross_grain_shared_per_agricultural_population instance.
    """

    model = Gross_grain_shared_per_agricultural_population
    template_name = "crisisdb/gross_grain_shared_per_agricultural_population/gross_grain_shared_per_agricultural_population_detail.html"  # noqa: E501 pylint: disable=C0301


class Net_grain_shared_per_agricultural_populationCreateView(
    PermissionRequiredMixin, CreateView
):
    """
    View for creating a new Net_grain_shared_per_agricultural_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Net_grain_shared_per_agricultural_population
    form_class = Net_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("net_grain_shared_per_agricultural_population-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context,
            "Net_grain_shared_per_agricultural_population",
            "Net Grain Shared Per Agricultural Population",
        )  # noqa: E501 pylint: disable=C0301

        return context


class Net_grain_shared_per_agricultural_populationUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Net_grain_shared_per_agricultural_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Net_grain_shared_per_agricultural_population
    form_class = Net_grain_shared_per_agricultural_populationForm
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Net Grain Shared Per Agricultural Population",
            },
        )

        return context


class Net_grain_shared_per_agricultural_populationDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Net_grain_shared_per_agricultural_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Net_grain_shared_per_agricultural_population
    success_url = reverse_lazy("net_grain_shared_per_agricultural_populations")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Net_grain_shared_per_agricultural_populationListView(ListView):
    """
    View for listing all Net_grain_shared_per_agricultural_population instances.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    """

    model = Net_grain_shared_per_agricultural_population
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("net_grain_shared_per_agricultural_populations")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Net Grain Shared Per Agricultural Population",
                "var_main_desc": "No explanations.",
                "var_main_desc_source": "",
                "var_section": "Economy Variables",
                "var_subsection": "Productivity",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "net_grain_shared_per_agricultural_population": {
                        "min": None,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "No Explanations.",
                        "units": "(catties per capita)",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Net_grain_shared_per_agricultural_populationDetailView(DetailView):
    """
    View for displaying a single Net_grain_shared_per_agricultural_population instance.
    """

    model = Net_grain_shared_per_agricultural_population
    template_name = "crisisdb/net_grain_shared_per_agricultural_population/net_grain_shared_per_agricultural_population_detail.html"  # noqa: E501 pylint: disable=C0301


class SurplusCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Surplus instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Surplus
    form_class = SurplusForm
    template_name = "crisisdb/surplus/surplus_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("surplus-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Surplus", "Surplus"
        )

        return context


class SurplusUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Surplus instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Surplus
    form_class = SurplusForm
    template_name = "crisisdb/surplus/surplus_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Surplus",
            },
        )

        return context


class SurplusDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Surplus instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Surplus
    success_url = reverse_lazy("surplus")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SurplusListView(ListView):
    """
    View for listing all Surplus instances.
    """

    model = Surplus
    template_name = "crisisdb/surplus/surplus_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("surplus")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Surplus",
                "var_main_desc": "No explanations.",
                "var_main_desc_source": "",
                "var_section": "Economy Variables",
                "var_subsection": "Productivity",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "surplus": {
                        "min": None,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "No Explanations.",
                        "units": "(catties per capita)",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class SurplusDetailView(DetailView):
    """
    View for displaying a single Surplus instance.
    """

    model = Surplus
    template_name = "crisisdb/surplus/surplus_detail.html"


class Military_expenseCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Military_expense instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Military_expense
    form_class = Military_expenseForm
    template_name = "crisisdb/military_expense/military_expense_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("military_expense-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Military_expense", "Military Expense"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Military_expenseUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Military_expense instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Military_expense
    form_class = Military_expenseForm
    template_name = "crisisdb/military_expense/military_expense_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Military Expense",
            },
        )

        return context


class Military_expenseDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Military_expense instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Military_expense
    success_url = reverse_lazy("military_expenses")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Military_expenseListView(ListView):
    """
    View for listing all Military_expense instances.
    """

    model = Military_expense
    template_name = "crisisdb/military_expense/military_expense_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("military_expenses")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Military Expense",
                "var_main_desc": "Main descriptions for the variable military Expense are missing!",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "https://en.wikipedia.org/wiki/Disease_outbreak",
                "var_section": "Economy Variables",
                "var_subsection": "State Finances",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "conflict": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The name of the conflict",
                        "units": None,
                        "choices": None,
                    },
                    "expenditure": {
                        "min": None,
                        "max": None,
                        "scale": 1000000,
                        "var_exp_source": None,
                        "var_exp": "The military expenses in millions silver taels.",
                        "units": "silver taels",
                        "choices": None,
                    },
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Military_expenseDetailView(DetailView):
    """
    View for displaying a single Military_expense instance.
    """

    model = Military_expense
    template_name = "crisisdb/military_expense/military_expense_detail.html"


class Silver_inflowCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Silver_inflow instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Silver_inflow
    form_class = Silver_inflowForm
    template_name = "crisisdb/silver_inflow/silver_inflow_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("silver_inflow-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Silver_inflow", "Silver Inflow"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Silver_inflowUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Silver_inflow instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Silver_inflow
    form_class = Silver_inflowForm
    template_name = "crisisdb/silver_inflow/silver_inflow_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Silver Inflow",
            },
        )

        return context


class Silver_inflowDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Silver_inflow instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Silver_inflow
    success_url = reverse_lazy("silver_inflows")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Silver_inflowListView(ListView):
    """
    View for listing all Silver_inflow instances.
    """

    model = Silver_inflow
    template_name = "crisisdb/silver_inflow/silver_inflow_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("silver_inflows")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Silver Inflow",
                "var_main_desc": "Silver inflow in millions of silver taels??",
                "var_main_desc_source": "",
                "var_section": "Economy Variables",
                "var_subsection": "State Finances",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "silver_inflow": {
                        "min": None,
                        "max": None,
                        "scale": 1000000,
                        "var_exp_source": None,
                        "var_exp": "Silver inflow in Millions of silver taels??",
                        "units": "silver taels??",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Silver_inflowDetailView(DetailView):
    """
    View for displaying a single Silver_inflow instance.
    """

    model = Silver_inflow
    template_name = "crisisdb/silver_inflow/silver_inflow_detail.html"


class Silver_stockCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Silver_stock instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Silver_stock
    form_class = Silver_stockForm
    template_name = "crisisdb/silver_stock/silver_stock_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("silver_stock-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Silver_stock", "Silver Stock"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Silver_stockUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Silver_stock instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Silver_stock
    form_class = Silver_stockForm
    template_name = "crisisdb/silver_stock/silver_stock_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Silver Stock",
            },
        )

        return context


class Silver_stockDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Silver_stock instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Silver_stock
    success_url = reverse_lazy("silver_stocks")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Silver_stockListView(ListView):
    """
    View for listing all Silver_stock instances.
    """

    model = Silver_stock
    template_name = "crisisdb/silver_stock/silver_stock_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("silver_stocks")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Silver Stock",
                "var_main_desc": "Silver stock in millions of silver taels??",
                "var_main_desc_source": "",
                "var_section": "Economy Variables",
                "var_subsection": "State Finances",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "silver_stock": {
                        "min": None,
                        "max": None,
                        "scale": 1000000,
                        "var_exp_source": None,
                        "var_exp": "Silver stock in Millions of silver taels??",
                        "units": "silver taels??",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Silver_stockDetailView(DetailView):
    """
    View for displaying a single Silver_stock instance.
    """

    model = Silver_stock
    template_name = "crisisdb/silver_stock/silver_stock_detail.html"


class Total_populationCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Total_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Total_population
    form_class = Total_populationForm
    template_name = "crisisdb/total_population/total_population_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("total_population-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Total_population", "Total Population"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Total_populationUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Total_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Total_population
    form_class = Total_populationForm
    template_name = "crisisdb/total_population/total_population_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Total Population",
            },
        )

        return context


class Total_populationDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Total_population instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Total_population
    success_url = reverse_lazy("total_populations")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Total_populationListView(ListView):
    """
    View for listing all Total_population instances.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    """

    model = Total_population
    template_name = "crisisdb/total_population/total_population_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("total_populations")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Total Population",
                "var_main_desc": "Total population or simply population, of a given area is the total number of people in that area at a given time.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "",
                "var_section": "Social Complexity Variables",
                "var_subsection": "Social Scale",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "total_population": {
                        "min": 0,
                        "max": None,
                        "scale": 1000,
                        "var_exp_source": None,
                        "var_exp": "The total population of a country (or a polity).",
                        "units": "People",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Total_populationDetailView(DetailView):
    """
    View for displaying a single Total_population instance.
    """

    model = Total_population
    template_name = "crisisdb/total_population/total_population_detail.html"


class Gdp_per_capitaCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Gdp_per_capita instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Gdp_per_capita
    form_class = Gdp_per_capitaForm
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("gdp_per_capita-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Gdp_per_capita", "GDP Per Capita"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Gdp_per_capitaUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Gdp_per_capita instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Gdp_per_capita
    form_class = Gdp_per_capitaForm
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Gdp Per Capita",
            },
        )

        return context


class Gdp_per_capitaDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Gdp_per_capita instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Gdp_per_capita
    success_url = reverse_lazy("gdp_per_capitas")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Gdp_per_capitaListView(ListView):
    """
    View for listing all Gdp_per_capita instances.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    """

    model = Gdp_per_capita
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("gdp_per_capitas")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Gdp Per Capita",
                "var_main_desc": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848",  # noqa: E501 pylint: disable=C0301
                "var_section": "Economy Variables",
                "var_subsection": "Productivity",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "gdp_per_capita": {
                        "min": None,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848",  # noqa: E501 pylint: disable=C0301
                        "var_exp": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.",  # noqa: E501 pylint: disable=C0301
                        "units": "Dollars (in 2009?)",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Gdp_per_capitaDetailView(DetailView):
    """
    View for displaying a single Gdp_per_capita instance.
    """

    model = Gdp_per_capita
    template_name = "crisisdb/gdp_per_capita/gdp_per_capita_detail.html"


class Drought_eventCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Drought_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Drought_event
    form_class = Drought_eventForm
    template_name = "crisisdb/drought_event/drought_event_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("drought_event-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Drought_event", "Drought Event"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Drought_eventUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Drought_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Drought_event
    form_class = Drought_eventForm
    template_name = "crisisdb/drought_event/drought_event_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Drought Event",
            },
        )

        return context


class Drought_eventDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Drought_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Drought_event
    success_url = reverse_lazy("drought_events")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Drought_eventListView(ListView):
    """
    View for listing all Drought_event instances.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    """

    model = Drought_event
    template_name = "crisisdb/drought_event/drought_event_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("drought_events")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Drought Event",
                "var_main_desc": "Number of geographic sites indicating drought",
                "var_main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",  # noqa: E501 pylint: disable=C0301
                "var_section": "Well Being",
                "var_subsection": "Biological Well-Being",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "drought_event": {
                        "min": 0,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "number of geographic sites indicating drought",
                        "units": "Numbers",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Drought_eventDetailView(DetailView):
    """
    View for displaying a single Drought_event instance.
    """

    model = Drought_event
    template_name = "crisisdb/drought_event/drought_event_detail.html"


class Locust_eventCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Locust_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Locust_event
    form_class = Locust_eventForm
    template_name = "crisisdb/locust_event/locust_event_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("locust_event-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Locust_event", "Locust Event"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Locust_eventUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Locust_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Locust_event
    form_class = Locust_eventForm
    template_name = "crisisdb/locust_event/locust_event_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Locust Event",
            },
        )

        return context


class Locust_eventDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Locust_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Locust_event
    success_url = reverse_lazy("locust_events")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Locust_eventListView(ListView):
    """
    View for listing all Locust_event instances.
    """

    model = Locust_event
    template_name = "crisisdb/locust_event/locust_event_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("locust_events")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Locust Event",
                "var_main_desc": "Number of geographic sites indicating locusts",
                "var_main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",  # noqa: E501 pylint: disable=C0301
                "var_section": "Well Being",
                "var_subsection": "Biological Well-Being",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "locust_event": {
                        "min": 0,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "number of geographic sites indicating locusts",
                        "units": "Numbers",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Locust_eventDetailView(DetailView):
    """
    View for displaying a single Locust_event instance.
    """

    model = Locust_event
    template_name = "crisisdb/locust_event/locust_event_detail.html"


class Socioeconomic_turmoil_eventCreateView(
    PermissionRequiredMixin, CreateView
):
    """
    View for creating a new Socioeconomic_turmoil_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Socioeconomic_turmoil_event
    form_class = Socioeconomic_turmoil_eventForm
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("socioeconomic_turmoil_event-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context,
            "Socioeconomic_turmoil_event",
            "Socioeconomic Turmoil Event",
        )  # noqa: E501 pylint: disable=C0301

        return context


class Socioeconomic_turmoil_eventUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Socioeconomic_turmoil_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Socioeconomic_turmoil_event
    form_class = Socioeconomic_turmoil_eventForm
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Socioeconomic Turmoil Event",
            },
        )

        return context


class Socioeconomic_turmoil_eventDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Socioeconomic_turmoil_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Socioeconomic_turmoil_event
    success_url = reverse_lazy("socioeconomic_turmoil_events")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Socioeconomic_turmoil_eventListView(ListView):
    """
    View for listing all Socioeconomic_turmoil_event instances.
    """

    model = Socioeconomic_turmoil_event
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("socioeconomic_turmoil_events")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Socioeconomic Turmoil Event",
                "var_main_desc": "Number of geographic sites indicating socioeconomic turmoil",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",  # noqa: E501 pylint: disable=C0301
                "var_section": "Well Being",
                "var_subsection": "Biological Well-Being",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "socioeconomic_turmoil_event": {
                        "min": 0,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "number of geographic sites indicating socioeconomic turmoil",  # noqa: E501 pylint: disable=C0301
                        "units": "Numbers",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Socioeconomic_turmoil_eventDetailView(DetailView):
    """
    View for displaying a single Socioeconomic_turmoil_event instance.
    """

    model = Socioeconomic_turmoil_event
    template_name = "crisisdb/socioeconomic_turmoil_event/socioeconomic_turmoil_event_detail.html"  # noqa: E501 pylint: disable=C0301


class Crop_failure_eventCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Crop_failure_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crop_failure_event
    form_class = Crop_failure_eventForm
    template_name = "crisisdb/crop_failure_event/crop_failure_event_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("crop_failure_event-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Crop_failure_event", "Crop Failure Event"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Crop_failure_eventUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Crop_failure_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crop_failure_event
    form_class = Crop_failure_eventForm
    template_name = (
        "crisisdb/crop_failure_event/crop_failure_event_update.html"
    )
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Crop Failure Event",
            },
        )
        context["myvar"] = "Crop Failure Event"

        return context


class Crop_failure_eventDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Crop_failure_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Crop_failure_event
    success_url = reverse_lazy("crop_failure_events")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Crop_failure_eventListView(ListView):
    """
    View for listing all Crop_failure_event instances.
    """

    model = Crop_failure_event
    template_name = "crisisdb/crop_failure_event/crop_failure_event_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("crop_failure_events")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Crop Failure Event",
                "var_main_desc": "Number of geographic sites indicating crop failure",
                "var_main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",  # noqa: E501 pylint: disable=C0301
                "var_section": "Well Being",
                "var_subsection": "Biological Well-Being",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "crop_failure_event": {
                        "min": 0,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "number of geographic sites indicating crop failure",
                        "units": "Numbers",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Crop_failure_eventDetailView(DetailView):
    """
    View for displaying a single Crop_failure_event instance.
    """

    model = Crop_failure_event
    template_name = (
        "crisisdb/crop_failure_event/crop_failure_event_detail.html"
    )


class Famine_eventCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Famine_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Famine_event
    form_class = Famine_eventForm
    template_name = "crisisdb/famine_event/famine_event_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("famine_event-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Famine_event", "Famine Event"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Famine_eventUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Famine_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Famine_event
    form_class = Famine_eventForm
    template_name = "crisisdb/famine_event/famine_event_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Famine Event",
            },
        )

        return context


class Famine_eventDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Famine_event instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Famine_event
    success_url = reverse_lazy("famine_events")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Famine_eventListView(ListView):
    """
    View for listing all Famine_event instances.
    """

    model = Famine_event
    template_name = "crisisdb/famine_event/famine_event_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("famine_events")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Famine Event",
                "var_main_desc": "Number of geographic sites indicating famine",
                "var_main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",  # noqa: E501 pylint: disable=C0301
                "var_section": "Well Being",
                "var_subsection": "Biological Well-Being",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "famine_event": {
                        "min": 0,
                        "max": None,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "number of geographic sites indicating famine",
                        "units": "Numbers",
                        "choices": None,
                    }
                },
                "potential_cols": ["Scale", "Units"],
            },
        )

        return context


class Famine_eventDetailView(DetailView):
    """
    View for displaying a single Famine_event instance.
    """

    model = Famine_event
    template_name = "crisisdb/famine_event/famine_event_detail.html"


class Disease_outbreakCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Disease_outbreak instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Disease_outbreak
    form_class = Disease_outbreakForm
    template_name = "crisisdb/disease_outbreak/disease_outbreak_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("disease_outbreak-create")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = expand_context_from_variable_hierarchy(
            context, "Disease_outbreak", "Disease Outbreak"
        )  # noqa: E501 pylint: disable=C0301

        return context


class Disease_outbreakUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Disease_outbreak instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Disease_outbreak
    form_class = Disease_outbreakForm
    template_name = "crisisdb/disease_outbreak/disease_outbreak_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Disease Outbreak",
            },
        )

        return context


class Disease_outbreakDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Disease_outbreak instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Disease_outbreak
    success_url = reverse_lazy("disease_outbreaks")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Disease_outbreakListView(ListView):
    """
    View for listing all Disease_outbreak instances.
    """

    model = Disease_outbreak
    template_name = "crisisdb/disease_outbreak/disease_outbreak_list.html"
    paginate_by = 50

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: Absolute URL of the view
        """
        return reverse("disease_outbreaks")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            dict: Context data for the view
        """
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Disease Outbreak",
                "var_main_desc": "A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "https://en.wikipedia.org/wiki/Disease_outbreak",
                "var_section": "Well Being",
                "var_subsection": "Biological Well-Being",
                "var_null_meaning": "The value is not available.",
                "inner_vars": {
                    "longitude": {
                        "min": -180,
                        "max": 180,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "The longitude (in degrees) of the place where the disease was spread.",  # noqa: E501 pylint: disable=C0301
                        "units": "Degrees",
                        "choices": None,
                    },
                    "latitude": {
                        "min": -180,
                        "max": 180,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "The latitude (in degrees) of the place where the disease was spread.",  # noqa: E501 pylint: disable=C0301
                        "units": "Degrees",
                        "choices": None,
                    },
                    "elevation": {
                        "min": 0,
                        "max": 5000,
                        "scale": 1,
                        "var_exp_source": None,
                        "var_exp": "Elevation from mean sea level (in meters) of the place where the disease was spread.",  # noqa: E501 pylint: disable=C0301
                        "units": "Meters",
                        "choices": None,
                    },
                    "sub_category": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The category of the disease.",
                        "units": None,
                        "choices": [
                            "Peculiar Epidemics",
                            "Pestilence",
                            "Miasm",
                            "Pox",
                            "Uncertain Pestilence",
                            "Dysentery",
                            "Malaria",
                            "Influenza",
                            "Cholera",
                            "Diptheria",
                            "Plague",
                        ],
                    },
                    "magnitude": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "How heavy the disease was.",
                        "units": None,
                        "choices": [
                            "Uncertain",
                            "Light",
                            "Heavy",
                            "No description",
                            "Heavy- Multiple Times",
                            "No Happening",
                            "Moderate",
                        ],
                    },
                    "duration": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "How long the disease lasted.",
                        "units": None,
                        "choices": [
                            "No description",
                            "Over 90 Days",
                            "Uncertain",
                            "30-60 Days",
                            "1-10 Days",
                            "60-90 Days",
                        ],
                    },
                },
                "potential_cols": ["Min", "Units", "Scale", "Max"],
            },
        )

        return context


class Disease_outbreakDetailView(DetailView):
    """
    View for displaying a single Disease_outbreak instance.
    """

    model = Disease_outbreak
    template_name = "crisisdb/disease_outbreak/disease_outbreak_detail.html"


# The temporary function for creating the my_sections_dic dic: test_for_varhier_dic inside
# utils and the qing_vars_links_creator() inside utils.py
def qing_vars_view(request):
    """
    View for listing all Qing Variables.

    Note:
        This is a temporary view for testing the Qing variables.

    Args:
        request: HttpRequest object

    Returns:
        dict: Context data for the view
    """
    context = {"my_dict": QING_VARS}

    return render(request, "crisisdb/qing-vars.html", context=context)


def playground(request):
    """
    View for the playground.

    Args:
        request: HttpRequest object

    Returns:
        dict: Context data for the view
    """
    context = {
        "allpols": [pol.name for pol in Polity.objects.all()],
        "all_var_hiers": ALL_VARS_WITH_HIERARCHY,
        "crisi": ALL_VARS_IN_SECTIONS,
    }

    return render(request, "crisisdb/playground.html", context=context)


def playgrounddownload_view(request):
    """
    Download the data from the playground.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    """
    # Read the data from the previous from
    # Make sure you collect all the data from seshat_api
    # Sort it out and spit it out
    # Small task: download what we have on seshat_api
    checked_pols = request.POST.getlist("selected_pols")

    checked_vars = request.POST.getlist("selected_vars")

    new_checked_vars = [
        "crisisdb_" + item.lower() + "_related" for item in checked_vars
    ]

    checked_separator = request.POST.get("SeparatorRadioOptions")

    if checked_separator == "comma":
        checked_sep = ","
    elif checked_separator == "bar":
        checked_sep = "|"
    else:
        # Bad selection of Separator
        pass

    all_my_data = get_api_results()

    # Create a response object with CSV content type
    final_response = HttpResponse(content_type="text/csv")
    date = get_date()
    filename = f"CrisisDB_data_{request.user}_{date}.csv"
    final_response["Content-Disposition"] = (
        f'attachment; filename="{filename}"'
    )

    writer = csv.writer(final_response, delimiter=checked_sep)

    # The top row is the same as Equinox, so no need to read data from user
    # input for that
    writer.writerow(
        [
            "polity",
            "variable_name",
            "variable_sub_name",
            "value",
            "year_from",
            "year_to",
            "certainty",
            "references",
            "notes",
        ]
    )

    for polity_with_everything in all_my_data:
        if polity_with_everything["name"] not in checked_pols:
            continue
        else:
            for variable in new_checked_vars:
                if variable not in polity_with_everything.keys():
                    continue
                else:
                    # We can get into a list of dictionaries
                    for var_instance in polity_with_everything[variable]:
                        all_inner_keys = var_instance.keys()
                        all_used_keys = []
                        for active_key in all_inner_keys:
                            if (
                                active_key
                                not in ["year_from", "year_to", "tag"]
                                and active_key not in all_used_keys
                            ):
                                an_equinox_row = []
                                an_equinox_row.append(
                                    polity_with_everything["name"]
                                )
                                an_equinox_row.append(variable[:-8])
                                an_equinox_row.append(active_key)
                                an_equinox_row.append(var_instance[active_key])
                                all_used_keys.append(active_key)
                                an_equinox_row.append(
                                    var_instance["year_from"]
                                )
                                an_equinox_row.append(var_instance["year_to"])
                                full_tag = TAGS_DIC[var_instance["tag"]]
                                an_equinox_row.append(full_tag)
                                writer.writerow(an_equinox_row)

    return final_response


def fpl_all(request):
    """
    View for the Famine, Plague, and Locust page.
    """
    return render(request, "crisisdb/fpl_all.html")


class UsLocationListView(ListView):
    """
    View for listing all Us_location instances.
    """

    model = Us_location
    template_name = "crisisdb/us_location/list.html"
    context_object_name = "us_locations"


class UsLocationCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Us_location instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Us_location
    form_class = Us_locationForm
    template_name = "crisisdb/us_location/create.html"
    permission_required = "core.add_capital"
    success_url = reverse_lazy("us_location_list")


class UsLocationUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Us_location instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Us_location
    form_class = Us_locationForm
    template_name = "crisisdb/us_location/update.html"
    permission_required = "core.add_capital"
    success_url = reverse_lazy("us_location_list")


class UsViolenceSubtypeListView(ListView):
    """
    View for listing all Us_violence_subtype instances.
    """

    model = Us_violence_subtype
    template_name = "crisisdb/subtype/list.html"
    context_object_name = "subtypes"


class UsViolenceSubtypeCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Us_violence_subtype instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Us_violence_subtype
    form_class = Us_violence_subtypeForm
    template_name = "crisisdb/subtype/create.html"
    permission_required = "core.add_capital"
    success_url = reverse_lazy("subtype_list")


class UsViolenceSubtypeUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Us_violence_subtype instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Us_violence_subtype
    form_class = Us_violence_subtypeForm
    template_name = "crisisdb/subtype/update.html"
    permission_required = "core.add_capital"
    success_url = reverse_lazy("subtype_list")


class UsViolenceDataSourceListView(ListView):
    """
    View for listing all Us_violence_data_source instances.
    """

    model = Us_violence_data_source
    template_name = "crisisdb/datasource/list.html"
    context_object_name = "datasources"


class UsViolenceDataSourceCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Us_violence_data_source instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Us_violence_data_source
    form_class = Us_violence_data_sourceForm
    template_name = "crisisdb/datasource/create.html"
    permission_required = "core.add_capital"
    success_url = reverse_lazy("datasource_list")


class UsViolenceDataSourceUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Us_violence_data_source instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Us_violence_data_source
    form_class = Us_violence_data_sourceForm
    template_name = "crisisdb/datasource/update.html"
    permission_required = "core.add_capital"
    success_url = reverse_lazy("datasource_list")


class UsViolenceListView(ListView):
    """
    View for listing all Us_violence instances.
    """

    model = Us_violence
    template_name = "crisisdb/us_violence/list.html"
    context_object_name = "us_violences"

    def get_queryset(self):
        """
        Get the queryset for the view.

        Returns:
            QuerySet: QuerySet for the view
        """
        # Get the query parameters from the request, if provided
        order_by = self.request.GET.get("order_by", self.ordering)

        # Check if the order_by parameter is valid
        if order_by not in [
            "violence_date",
            "-violence_date",
            "violence_type",
            "-violence_type",
            "fatalities",
            "-fatalities",
        ]:
            # Use the default ordering if the parameter is invalid
            order_by = "-violence_date"

        # Get the queryset with the specified ordering
        queryset = super().get_queryset().order_by(order_by)

        return queryset


class UsViolenceListViewPaginated(ListView):
    """
    View for listing all Us_violence instances with pagination (100 per page).
    """

    model = Us_violence
    template_name = "crisisdb/us_violence/list_paginated.html"
    context_object_name = "us_violences"
    paginate_by = 100


class UsViolenceCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Us_violence instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Us_violence
    form_class = Us_violenceForm
    template_name = "crisisdb/us_violence/create.html"
    permission_required = "core.add_capital"
    success_url = reverse_lazy("us_violence_paginated")


class UsViolenceUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Us_violence instance.

    Note:
        This view is only accessible to users with the 'add_capital' permission.
    """

    model = Us_violence
    form_class = Us_violenceForm
    template_name = "crisisdb/us_violence/update.html"
    permission_required = "core.add_capital"
    success_url = reverse_lazy("us_violence_paginated")


@permission_required("core.add_capital")
def generic_confirm_delete_view(request, model_class, pk, var_name):
    """
    View for confirming the deletion of an object.

    Note:
        This view is only accessible to users with the 'add_capital' permission.

    Args:
        request: HttpRequest object
        model_class: Model class of the object to be deleted
        pk: Primary key of the object to be deleted
        var_name: Name of the object to be deleted

    Returns:
        HttpResponse: HTTP response with the confirmation page

    Raises:
        Http404: If the object with the given primary key does not exist
    """
    check_permissions(request)

    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    context = {
        "var_name": var_name,
        "obj": obj,
        "delete_object": f"{var_name}-delete",
    }

    return render(request, "core/confirm_delete.html", context)


@permission_required("core.add_capital")
def generic_delete_object_view(request, model_class, pk, var_name):
    """
    View for deleting an object.

    Note:
        This view is only accessible to users with the 'add_capital' permission.

    Args:
        request: HttpRequest object
        model_class: Model class of the object to be deleted
        pk: Primary key of the object to be deleted
        var_name: Name of the object to be deleted

    Returns:
        HttpResponse: HTTP response with the confirmation page
    """
    check_permissions(request)

    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    # Delete the object
    obj.delete()

    # Redirect to the success URL
    success_url = reverse(f"{var_name}_list")

    # Display a success message
    messages.success(request, f"{var_name} has been deleted successfully.")

    return redirect(success_url)
