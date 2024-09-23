from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)

from ..utils import get_variable_context, _get_context

from .forms import (
    Polity_research_assistantForm,
    Polity_utm_zoneForm,
    Polity_original_nameForm,
    Polity_alternative_nameForm,
    Polity_peak_yearsForm,
    Polity_durationForm,
    Polity_degree_of_centralizationForm,
    Polity_suprapolity_relationsForm,
    Polity_capitalForm,
    Polity_languageForm,
    Polity_linguistic_familyForm,
    Polity_language_genusForm,
    Polity_religion_genusForm,
    Polity_religion_familyForm,
    Polity_religionForm,
    Polity_relationship_to_preceding_entityForm,
    Polity_preceding_entityForm,
    Polity_succeeding_entityForm,
    Polity_supracultural_entityForm,
    Polity_scale_of_supracultural_interactionForm,
    Polity_alternate_religion_genusForm,
    Polity_alternate_religion_familyForm,
    Polity_alternate_religionForm,
    Polity_expertForm,
    Polity_editorForm,
    Polity_religious_traditionForm,
)
from .mixins import PolityIdMixin
from .models import (
    Polity_research_assistant,
    Polity_utm_zone,
    Polity_original_name,
    Polity_alternative_name,
    Polity_peak_years,
    Polity_duration,
    Polity_degree_of_centralization,
    Polity_suprapolity_relations,
    Polity_capital,
    Polity_language,
    Polity_linguistic_family,
    Polity_language_genus,
    Polity_religion_genus,
    Polity_religion_family,
    Polity_religion,
    Polity_relationship_to_preceding_entity,
    Polity_preceding_entity,
    Polity_succeeding_entity,
    Polity_supracultural_entity,
    Polity_scale_of_supracultural_interaction,
    Polity_alternate_religion_genus,
    Polity_alternate_religion_family,
    Polity_alternate_religion,
    Polity_expert,
    Polity_editor,
    Polity_religious_tradition,
)
from .constants import (
    APP_NAME,
    INNER_POLITY_ALTERNATE_RELIGION_CHOICES,
    INNER_POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES,
    INNER_POLITY_ALTERNATE_RELIGION_GENUS_CHOICES,
    INNER_POLITY_LINGUISTIC_FAMILY_CHOICES,
    INNER_POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES,
    INNER_POLITY_RELIGION_CHOICES,
    INNER_POLITY_RELIGION_FAMILY_CHOICES,
    INNER_POLITY_RELIGION_GENUS_CHOICES,
    INNER_POLITY_SUPRAPOLITY_RELATIONS_CHOICES,
)


class Polity_research_assistantCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Polity_research_assistant.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_research_assistant
    form_class = Polity_research_assistantForm
    template_name = (
        "general/polity_research_assistant/polity_research_assistant_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_research_assistant-create")

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

        context = _get_context(self, False, context)

        return context


class Polity_research_assistantUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_research_assistant.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_research_assistant
    form_class = Polity_research_assistantForm
    template_name = "general/polity_research_assistant/polity_research_assistant_update.html"  # noqa: E501 pylint: disable=C0301
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

        context = _get_context(self, True, context)

        return context


class Polity_research_assistantDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_research_assistant.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_research_assistant
    success_url = reverse_lazy("polity_research_assistants")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_research_assistantListView(ListView):
    """
    Paginated view for listing all Polity_research_assistant instances.
    """

    model = Polity_research_assistant
    template_name = (
        "general/polity_research_assistant/polity_research_assistant_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_research_assistants")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "Staff",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_research_assistantListAllView(ListView):
    """
    View for listing all Polity_research_assistant instances.
    """

    model = Polity_research_assistant
    template_name = "general/polity_research_assistant/polity_research_assistant_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_research_assistants_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_research_assistant instances.

        Returns:
            QuerySet: The queryset of Polity_research_assistant instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_research_assistant.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "Staff",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_research_assistantDetailView(DetailView):
    """
    View for displaying a single Polity_research_assistant instance.
    """

    model = Polity_research_assistant
    template_name = "general/polity_research_assistant/polity_research_assistant_detail.html"  # noqa: E501 pylint: disable=C0301


class Polity_utm_zoneCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_utm_zone.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_utm_zone
    form_class = Polity_utm_zoneForm
    template_name = "general/polity_utm_zone/polity_utm_zone_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_utm_zone-create")

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

        context = _get_context(self, context)

        return context


class Polity_utm_zoneUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_utm_zone.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_utm_zone
    form_class = Polity_utm_zoneForm
    template_name = "general/polity_utm_zone/polity_utm_zone_update.html"
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_utm_zoneDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_utm_zone.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_utm_zone
    success_url = reverse_lazy("polity_utm_zones")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_utm_zoneListView(ListView):
    """
    Paginated view for listing all Polity_utm_zone instances.
    """

    model = Polity_utm_zone
    template_name = "general/polity_utm_zone/polity_utm_zone_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_utm_zones")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_utm_zoneListAllView(ListView):
    """
    View for listing all Polity_utm_zone instances.
    """

    model = Polity_utm_zone
    template_name = "general/polity_utm_zone/polity_utm_zone_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_utm_zones_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_utm_zone instances.

        Returns:
            QuerySet: The queryset of Polity_utm_zone instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_utm_zone.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_utm_zoneDetailView(DetailView):
    """
    View for displaying a single Polity_utm_zone instance.
    """

    model = Polity_utm_zone
    template_name = "general/polity_utm_zone/polity_utm_zone_detail.html"


class Polity_original_nameCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_original_name.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_original_name
    form_class = Polity_original_nameForm
    template_name = (
        "general/polity_original_name/polity_original_name_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_original_name-create")

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

        context = _get_context(self, context)

        return context


class Polity_original_nameUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_original_name.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_original_name
    form_class = Polity_original_nameForm
    template_name = (
        "general/polity_original_name/polity_original_name_update.html"
    )
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_original_nameDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_original_name.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_original_name
    success_url = reverse_lazy("polity_original_names")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_original_nameListView(ListView):
    """
    Paginated view for listing all Polity_original_name instances.
    """

    model = Polity_original_name
    template_name = (
        "general/polity_original_name/polity_original_name_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_original_names")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_original_nameListAllView(ListView):
    """
    View for listing all Polity_original_name instances.
    """

    model = Polity_original_name
    template_name = (
        "general/polity_original_name/polity_original_name_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_original_names_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_original_name instances.

        Returns:
            QuerySet: The queryset of Polity_original_name instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_original_name.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_original_nameDetailView(DetailView):
    """
    View for displaying a single Polity_original_name instance.
    """

    model = Polity_original_name
    template_name = (
        "general/polity_original_name/polity_original_name_detail.html"
    )


class Polity_alternative_nameCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_alternative_name.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternative_name
    form_class = Polity_alternative_nameForm
    template_name = (
        "general/polity_alternative_name/polity_alternative_name_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternative_name-create")

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

        context = _get_context(self, context)

        return context


class Polity_alternative_nameUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_alternative_name.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternative_name
    form_class = Polity_alternative_nameForm
    template_name = (
        "general/polity_alternative_name/polity_alternative_name_update.html"
    )
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_alternative_nameDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_alternative_name.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternative_name
    success_url = reverse_lazy("polity_alternative_names")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_alternative_nameListView(ListView):
    """
    Paginated view for listing all Polity_alternative_name instances.
    """

    model = Polity_alternative_name
    template_name = (
        "general/polity_alternative_name/polity_alternative_name_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternative_names")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_alternative_nameListAllView(ListView):
    """
    View for listing all Polity_alternative_name instances.
    """

    model = Polity_alternative_name
    template_name = (
        "general/polity_alternative_name/polity_alternative_name_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternative_names_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_alternative_name instances.

        Returns:
            QuerySet: The queryset of Polity_alternative_name instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_alternative_name.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_alternative_nameDetailView(DetailView):
    """
    View for displaying a single Polity_alternative_name instance.
    """

    model = Polity_alternative_name
    template_name = (
        "general/polity_alternative_name/polity_alternative_name_detail.html"
    )


class Polity_peak_yearsCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_peak_years.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_peak_years
    form_class = Polity_peak_yearsForm
    template_name = "general/polity_peak_years/polity_peak_years_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_peak_years-create")

    def get_initial(self):
        """
        Get the initial value of the polity field from the query string.

        Note:
            TODO This should already be handled by the PolityIdMixin.

        Returns:
            dict: The initial value of the polity field.
        """
        initial = super(Polity_peak_yearsCreateView, self).get_initial()
        polity_id_x = self.request.GET.get("polity_id_x")
        initial["polity"] = polity_id_x

        return initial

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_peak_yearsUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_peak_years.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_peak_years
    form_class = Polity_peak_yearsForm
    template_name = "general/polity_peak_years/polity_peak_years_update.html"
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.subsection,
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
            },
        )

        return context


class Polity_peak_yearsDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_peak_years.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_peak_years
    success_url = reverse_lazy("polity_peak_yearss")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_peak_yearsListView(ListView):
    """
    Paginated view for listing all Polity_peak_years instances.
    """

    model = Polity_peak_years
    template_name = "general/polity_peak_years/polity_peak_years_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_peak_yearss")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.subsection,
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_peak_yearsListAllView(ListView):
    """
    View for listing all Polity_peak_years instances.
    """

    model = Polity_peak_years
    template_name = "general/polity_peak_years/polity_peak_years_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_peak_yearss_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_peak_years instances.

        Returns:
            QuerySet: The queryset of Polity_peak_years instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_peak_years.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_peak_yearsDetailView(DetailView):
    """
    View for displaying a single Polity_peak_years instance.
    """

    model = Polity_peak_years
    template_name = "general/polity_peak_years/polity_peak_years_detail.html"


class Polity_durationCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_duration.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_duration
    form_class = Polity_durationForm
    template_name = "general/polity_duration/polity_duration_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_duration-create")

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

        context["mysection"] = self.model.Code.section
        context["mysubsection"] = "Temporal Bounds"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "Temporal Bounds"
        context["myvar"] = self.model.Code.variable
        context["my_exp"] = self.model.Code.description
        context["var_null_meaning"] = self.model.Code.null_meaning
        context["inner_vars"] = self.model.Code.inner_variables
        context["potential_cols"] = self.model.Code.potential_cols

        return context


class Polity_durationUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_duration.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_duration
    form_class = Polity_durationForm
    template_name = "general/polity_duration/polity_duration_update.html"
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
                "mysubsection": "Temporal Bounds",
                "var_section": "General Variables",
                "var_subsection": "Temporal Bounds",
            },
        )

        return context


class Polity_durationDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_duration.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_duration
    success_url = reverse_lazy("polity_durations")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_durationListView(ListView):
    """
    Paginated view for listing all Polity_duration instances.
    """

    model = Polity_duration
    template_name = "general/polity_duration/polity_duration_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_durations")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "Temporal Bounds",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_durationListAllView(ListView):
    """
    View for listing all Polity_duration instances.
    """

    model = Polity_duration
    template_name = "general/polity_duration/polity_duration_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_durations_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_duration instances.

        Returns:
            QuerySet: The queryset of Polity_duration instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_duration.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "Temporal Bounds",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_durationDetailView(DetailView):
    """
    View for displaying a single Polity_duration instance.
    """

    model = Polity_duration
    template_name = "general/polity_duration/polity_duration_detail.html"


class Polity_degree_of_centralizationCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_degree_of_centralization.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_degree_of_centralization
    form_class = Polity_degree_of_centralizationForm
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the degree_of_centralization field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["degree_of_centralization"].choices = sorted(
            form.fields["degree_of_centralization"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_degree_of_centralization-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_value,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_degree_of_centralizationUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Polity_degree_of_centralization.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_degree_of_centralization
    form_class = Polity_degree_of_centralizationForm
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the degree_of_centralization field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["degree_of_centralization"].choices = sorted(
            form.fields["degree_of_centralization"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_degree_of_centralizationDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Polity_degree_of_centralization.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_degree_of_centralization
    success_url = reverse_lazy("polity_degree_of_centralizations")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_degree_of_centralizationListView(ListView):
    """
    Paginated view for listing all Polity_degree_of_centralization instances.
    """

    model = Polity_degree_of_centralization
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_degree_of_centralizations")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_degree_of_centralizationListAllView(ListView):
    """
    View for listing all Polity_degree_of_centralization instances.
    """

    model = Polity_degree_of_centralization
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_degree_of_centralizations_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_degree_of_centralization instances.

        Returns:
            QuerySet: The queryset of Polity_degree_of_centralization instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_degree_of_centralization.objects.all().order_by(
            order, order2
        )

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_degree_of_centralizationDetailView(DetailView):
    """
    View for displaying a single Polity_degree_of_centralization instance.
    """

    model = Polity_degree_of_centralization
    template_name = "general/polity_degree_of_centralization/polity_degree_of_centralization_detail.html"  # noqa: E501 pylint: disable=C0301


class Polity_suprapolity_relationsCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_suprapolity_relations.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_suprapolity_relations
    form_class = Polity_suprapolity_relationsForm
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the supra_polity_relations field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["supra_polity_relations"].choices = sorted(
            form.fields["supra_polity_relations"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_suprapolity_relations-create")

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

        context["mysection"] = self.model.Code.section
        context["mysubsection"] = "General Variables"
        context["var_section"] = "General Variables"
        context["var_subsection"] = "Political and Cultural Relations"
        context["myvar"] = self.model.Code.variable
        context[
            "my_exp"
        ] = """ <u>Possible Codes</u>: <br> alliance / nominal allegiance / personal union / vassalage / unknown / none <br><br>
<b>alliance</b> = belongs to a long-term military-political alliance of independent polities ('long-term' refers to more or less permanent relationship between polities extending over multiple years)<br>
<b>nominal allegiance</b> = same as 'nominal' under the variable "Degree of centralization" but now reflecting the position of the focal polity within the overarching political authority.<br>
<b>personal union</b> = the focal polity is united with another, or others, as a result of a dynastic marriage.<br>
<b>vassalage</b> = corresponding to 'loose' category in the Degree of centralization."""  # noqa: E501 pylint: disable=C0301
        context["var_null_meaning"] = self.model.Code.null_meaning
        context["inner_vars"] = self.model.Code.inner_variables
        context["potential_cols"] = self.model.Code.potential_cols

        return context


class Polity_suprapolity_relationsUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Polity_suprapolity_relations.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_suprapolity_relations
    form_class = Polity_suprapolity_relationsForm
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the supra_polity_relations field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["supra_polity_relations"].choices = sorted(
            form.fields["supra_polity_relations"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

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
                "mysection": self.model.Code.section,
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
            },
        )

        return context


class Polity_suprapolity_relationsDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Polity_suprapolity_relations.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_suprapolity_relations
    success_url = reverse_lazy("polity_suprapolity_relationss")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_suprapolity_relationsListView(ListView):
    """
    Paginated view for listing all Polity_suprapolity_relations instances.
    """

    model = Polity_suprapolity_relations
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_suprapolity_relationss")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_suprapolity_relationsListAllView(ListView):
    """
    View for listing all Polity_suprapolity_relations instances.
    """

    model = Polity_suprapolity_relations
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_suprapolity_relationss_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_suprapolity_relations instances.

        Returns:
            QuerySet: The queryset of Polity_suprapolity_relations instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_suprapolity_relations.objects.all().order_by(
            order, order2
        )

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_suprapolity_relationsDetailView(DetailView):
    """
    View for displaying a single Polity_suprapolity_relations instance.
    """

    model = Polity_suprapolity_relations
    template_name = "general/polity_suprapolity_relations/polity_suprapolity_relations_detail.html"  # noqa: E501 pylint: disable=C0301


class Polity_capitalCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_capital.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_capital
    form_class = Polity_capitalForm
    template_name = "general/polity_capital/polity_capital_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_capital-create")

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

        context = _get_context(self, True, context)

        return context


class Polity_capitalUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_capital.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_capital
    form_class = Polity_capitalForm
    template_name = "general/polity_capital/polity_capital_update.html"
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
                "my_exp": "The capital of a polity is connection point between an existing \
Polity instance and an existing Capital instance. Optionally, year range associations can \
be specified. If not provided, it implies that the capital remains constant throughout the \
entire duration of the polity's existence.",
            },
        )

        return context


class Polity_capitalDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_capital.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_capital
    success_url = reverse_lazy("polity_capitals")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_capitalListView(ListView):
    """
    Paginated view for listing all Polity_capital instances.
    """

    model = Polity_capital
    template_name = "general/polity_capital/polity_capital_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_capitals")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_capitalListAllView(ListView):
    """
    View for listing all Polity_capital instances.
    """

    model = Polity_capital
    template_name = "general/polity_capital/polity_capital_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_capitals_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_capital instances.

        Returns:
            QuerySet: The queryset of Polity_capital instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_capital.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_capitalDetailView(DetailView):
    """
    View for displaying a single Polity_capital instance.
    """

    model = Polity_capital
    template_name = "general/polity_capital/polity_capital_detail.html"


class Polity_languageCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_language.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_language
    form_class = Polity_languageForm
    template_name = "general/polity_language/polity_language_form.html"
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the language field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["language"].choices = sorted(
            form.fields["language"].choices, key=lambda x: x[1].lower()
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_language-create")

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

        context = _get_context(self, context)

        return context


class Polity_languageUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_language.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_language
    form_class = Polity_languageForm
    template_name = "general/polity_language/polity_language_update.html"
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the language field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["language"].choices = sorted(
            form.fields["language"].choices, key=lambda x: x[1].lower()
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_languageDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_language.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_language
    success_url = reverse_lazy("polity_languages")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_languageListView(ListView):
    """
    Paginated view for listing all Polity_language instances.
    """

    model = Polity_language
    template_name = "general/polity_language/polity_language_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_languages")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_languageListAllView(ListView):
    """
    View for listing all Polity_language instances.
    """

    model = Polity_language
    template_name = "general/polity_language/polity_language_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_languages_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_language instances.

        Returns:
            QuerySet: The queryset of Polity_language instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_language.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_languageDetailView(DetailView):
    """
    View for displaying a single Polity_language instance.
    """

    model = Polity_language
    template_name = "general/polity_language/polity_language_detail.html"


class Polity_linguistic_familyCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_linguistic_family.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_linguistic_family
    form_class = Polity_linguistic_familyForm
    template_name = (
        "general/polity_linguistic_family/polity_linguistic_family_form.html"
    )
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the linguistic_family field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["linguistic_family"].choices = sorted(
            form.fields["linguistic_family"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_linguistic_family-create")

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

        context = _get_context(self, context)

        return context


class Polity_linguistic_familyUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_linguistic_family.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_linguistic_family
    form_class = Polity_linguistic_familyForm
    template_name = (
        "general/polity_linguistic_family/polity_linguistic_family_update.html"
    )
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the linguistic_family field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["linguistic_family"].choices = sorted(
            form.fields["linguistic_family"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_linguistic_familyDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_linguistic_family.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_linguistic_family
    success_url = reverse_lazy("polity_linguistic_familys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_linguistic_familyListView(ListView):
    """
    Paginated view for listing all Polity_linguistic_family instances.
    """

    model = Polity_linguistic_family
    template_name = (
        "general/polity_linguistic_family/polity_linguistic_family_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_linguistic_familys")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_linguistic_familyListAllView(ListView):
    """
    View for listing all Polity_linguistic_family instances.
    """

    model = Polity_linguistic_family
    template_name = "general/polity_linguistic_family/polity_linguistic_family_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_linguistic_familys_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_linguistic_family instances.

        Returns:
            QuerySet: The queryset of Polity_linguistic_family instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_linguistic_family.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_linguistic_familyDetailView(DetailView):
    """
    View for displaying a single Polity_linguistic_family instance.
    """

    model = Polity_linguistic_family
    template_name = (
        "general/polity_linguistic_family/polity_linguistic_family_detail.html"
    )


class Polity_language_genusCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_language_genus.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_language_genus
    form_class = Polity_language_genusForm
    template_name = (
        "general/polity_language_genus/polity_language_genus_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_language_genus-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_language_genusUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_language_genus.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_language_genus
    form_class = Polity_language_genusForm
    template_name = (
        "general/polity_language_genus/polity_language_genus_update.html"
    )
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_language_genusDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_language_genus.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_language_genus
    success_url = reverse_lazy("polity_language_genuss")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_language_genusListView(ListView):
    """
    Paginated view for listing all Polity_language_genus instances.
    """

    model = Polity_language_genus
    template_name = (
        "general/polity_language_genus/polity_language_genus_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_language_genuss")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_language_genusListAllView(ListView):
    """
    View for listing all Polity_language_genus instances.
    """

    model = Polity_language_genus
    template_name = (
        "general/polity_language_genus/polity_language_genus_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_language_genuss_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_language_genus instances.

        Returns:
            QuerySet: The queryset of Polity_language_genus instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_language_genus.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_language_genusDetailView(DetailView):
    """
    View for displaying a single Polity_language_genus instance.
    """

    model = Polity_language_genus
    template_name = (
        "general/polity_language_genus/polity_language_genus_detail.html"
    )


class Polity_religion_genusCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_religion_genus.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religion_genus
    form_class = Polity_religion_genusForm
    template_name = (
        "general/polity_religion_genus/polity_religion_genus_form.html"
    )
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the religion_genus field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["religion_genus"].choices = sorted(
            form.fields["religion_genus"].choices, key=lambda x: x[1].lower()
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religion_genus-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_religion_genusUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_religion_genus.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religion_genus
    form_class = Polity_religion_genusForm
    template_name = (
        "general/polity_religion_genus/polity_religion_genus_update.html"
    )
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the religion_genus field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["religion_genus"].choices = sorted(
            form.fields["religion_genus"].choices, key=lambda x: x[1].lower()
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_religion_genusDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_religion_genus.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religion_genus
    success_url = reverse_lazy("polity_religion_genuss")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_religion_genusListView(ListView):
    """
    Paginated view for listing all Polity_religion_genus instances.
    """

    model = Polity_religion_genus
    template_name = (
        "general/polity_religion_genus/polity_religion_genus_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religion_genuss")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_religion_genusListAllView(ListView):
    """
    View for listing all Polity_religion_genus instances.
    """

    model = Polity_religion_genus
    template_name = (
        "general/polity_religion_genus/polity_religion_genus_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religion_genuss_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_religion_genus instances.

        Returns:
            QuerySet: The queryset of Polity_religion_genus instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_religion_genus.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_religion_genusDetailView(DetailView):
    """
    View for displaying a single Polity_religion_genus instance.
    """

    model = Polity_religion_genus
    template_name = (
        "general/polity_religion_genus/polity_religion_genus_detail.html"
    )


class Polity_religion_familyCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_religion_family.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religion_family
    form_class = Polity_religion_familyForm
    template_name = (
        "general/polity_religion_family/polity_religion_family_form.html"
    )
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the religion_family field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["religion_family"].choices = sorted(
            form.fields["religion_family"].choices, key=lambda x: x[1].lower()
        )
        return form

    def get_initial(self):
        """
        Get the initial value of the polity field from the query string.

        Note:
            TODO This should already be handled by the PolityIdMixin.

        Returns:
            dict: The initial value of the polity field.
        """
        initial = super(
            Polity_religion_familyCreateView, self
        ).get_initial()  # TODO: fix
        polity_id_x = self.request.GET.get("polity_id_x")
        initial["polity"] = polity_id_x

        return initial

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religion_family-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_religion_familyUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_religion_family.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religion_family
    form_class = Polity_religion_familyForm
    template_name = (
        "general/polity_religion_family/polity_religion_family_update.html"
    )
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the religion_family field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["religion_family"].choices = sorted(
            form.fields["religion_family"].choices, key=lambda x: x[1].lower()
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_religion_familyDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_religion_family.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religion_family
    success_url = reverse_lazy("polity_religion_familys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_religion_familyListView(ListView):
    """
    Paginated view for listing all Polity_religion_family instances.
    """

    model = Polity_religion_family
    template_name = (
        "general/polity_religion_family/polity_religion_family_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religion_familys")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_religion_familyListAllView(ListView):
    """
    View for listing all Polity_religion_family instances.
    """

    model = Polity_religion_family
    template_name = (
        "general/polity_religion_family/polity_religion_family_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religion_familys_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_religion_family instances.

        Returns:
            QuerySet: The queryset of Polity_religion_family instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_religion_family.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_religion_familyDetailView(DetailView):
    """
    View for displaying a single Polity_religion_family instance.
    """

    model = Polity_religion_family
    template_name = (
        "general/polity_religion_family/polity_religion_family_detail.html"
    )


class Polity_religionCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_religion.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religion
    form_class = Polity_religionForm
    template_name = "general/polity_religion/polity_religion_form.html"
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the religion field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["religion"].choices = sorted(
            form.fields["religion"].choices, key=lambda x: x[1].lower()
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religion-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_religionUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_religion.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religion
    form_class = Polity_religionForm
    template_name = "general/polity_religion/polity_religion_update.html"
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the religion field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["religion"].choices = sorted(
            form.fields["religion"].choices, key=lambda x: x[1].lower()
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_religionDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_religion.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religion
    success_url = reverse_lazy("polity_religions")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_religionListView(ListView):
    """
    Paginated view for listing all Polity_religion instances.
    """

    model = Polity_religion
    template_name = "general/polity_religion/polity_religion_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religions")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_religionListAllView(ListView):
    """
    View for listing all Polity_religion instances.
    """

    model = Polity_religion
    template_name = "general/polity_religion/polity_religion_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religions_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_religion instances.

        Returns:
            QuerySet: The queryset of Polity_religion instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_religion.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_religionDetailView(DetailView):
    """
    View for displaying a single Polity_religion instance.
    """

    model = Polity_religion
    template_name = "general/polity_religion/polity_religion_detail.html"


class Polity_relationship_to_preceding_entityCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_relationship_to_preceding_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_relationship_to_preceding_entity
    form_class = Polity_relationship_to_preceding_entityForm
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the relationship_to_preceding_entity
        field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["relationship_to_preceding_entity"].choices = sorted(
            form.fields["relationship_to_preceding_entity"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_relationship_to_preceding_entity-create")

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

        context["mysection"] = self.model.Code.section
        context["mysubsection"] = (
            self.model.Code.section
        )  # TODO Note: wrong in the original code
        context["myvar"] = self.model.Code.variable
        context["my_exp"] = self.model.Code.description
        context["var_null_meaning"] = self.model.Code.null_meaning
        context["inner_vars"] = self.model.Code.inner_variables
        context["potential_cols"] = self.model.Code.potential_cols

        return context


class Polity_relationship_to_preceding_entityUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Polity_relationship_to_preceding_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_relationship_to_preceding_entity
    form_class = Polity_relationship_to_preceding_entityForm
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the relationship_to_preceding_entity
        field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["relationship_to_preceding_entity"].choices = sorted(
            form.fields["relationship_to_preceding_entity"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_relationship_to_preceding_entityDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Polity_relationship_to_preceding_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_relationship_to_preceding_entity
    success_url = reverse_lazy("polity_relationship_to_preceding_entitys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_relationship_to_preceding_entityListView(ListView):
    """
    Paginated view for listing all Polity_relationship_to_preceding_entity instances.
    """

    model = Polity_relationship_to_preceding_entity
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_relationship_to_preceding_entitys")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_relationship_to_preceding_entityListAllView(ListView):
    """
    View for listing all Polity_relationship_to_preceding_entity instances.
    """

    model = Polity_relationship_to_preceding_entity
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_relationship_to_preceding_entitys_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_relationship_to_preceding_entity instances.

        Returns:
            QuerySet: The queryset of Polity_relationship_to_preceding_entity instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_relationship_to_preceding_entity.objects.all().order_by(
            order, order2
        )

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_relationship_to_preceding_entityDetailView(DetailView):
    """
    View for displaying a single Polity_relationship_to_preceding_entity instance.
    """

    model = Polity_relationship_to_preceding_entity
    template_name = "general/polity_relationship_to_preceding_entity/polity_relationship_to_preceding_entity_detail.html"  # noqa: E501 pylint: disable=C0301


class Polity_preceding_entityCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_preceding_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_preceding_entity
    form_class = Polity_preceding_entityForm
    template_name = (
        "general/polity_preceding_entity/polity_preceding_entity_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_preceding_entity-create")

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

        # Extract query parameters
        polity_id_x = self.request.GET.get("polity_id_x")
        other_polity_id_x = self.request.GET.get("other_polity_id_x")

        # Filter the data based on query parameters
        if polity_id_x and other_polity_id_x:
            all_rels = Polity_preceding_entity.objects.filter(
                Q(polity_id=polity_id_x)
                | Q(other_polity_id=polity_id_x)
                | Q(polity_id=other_polity_id_x)
                | Q(other_polity_id=other_polity_id_x)
            )
        elif polity_id_x:
            # If other_polity is None, exclude it from the filter
            all_rels = Polity_preceding_entity.objects.filter(
                Q(polity_id=polity_id_x) | Q(other_polity_id=polity_id_x)
            )
        elif other_polity_id_x:
            # If polity is None, exclude it from the filter
            all_rels = Polity_preceding_entity.objects.filter(
                Q(polity_id=other_polity_id_x)
                | Q(other_polity_id=other_polity_id_x)
            )
        else:
            all_rels = Polity_preceding_entity.objects.none()

        # Add extra context
        context["mysection"] = self.model.Code.section
        context["mysubsection"] = "General Variables"
        context["myvar"] = self.model.Code.variable
        context["my_exp"] = self.model.Code.description
        context["var_null_meaning"] = self.model.Code.null_meaning
        context["inner_vars"] = self.model.Code.inner_variables
        context["potential_cols"] = self.model.Code.potential_cols

        context["all_rels"] = all_rels  # Add filtered data to context

        return context


class Polity_preceding_entityUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_preceding_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_preceding_entity
    form_class = Polity_preceding_entityForm
    template_name = (
        "general/polity_preceding_entity/polity_preceding_entity_update.html"
    )
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

        if self.object.polity and self.object.other_polity:
            all_rels = Polity_preceding_entity.objects.filter(
                Q(polity_id=self.object.polity.pk)
                | Q(other_polity_id=self.object.polity.pk)
                | Q(polity_id=self.object.other_polity.pk)
                | Q(other_polity_id=self.object.other_polity.pk)
            ).exclude(id=self.object.pk)
        elif self.object.polity:
            # If other_polity is None, exclude it from the filter
            all_rels = Polity_preceding_entity.objects.filter(
                Q(polity_id=self.object.polity.pk)
                | Q(other_polity_id=self.object.polity.pk)
            ).exclude(id=self.object.pk)
        elif self.object.other_polity:
            # If polity is None, exclude it from the filter
            all_rels = Polity_preceding_entity.objects.filter(
                Q(polity_id=self.object.other_polity.pk)
                | Q(other_polity_id=self.object.other_polity.pk)
            ).exclude(id=self.object.pk)
        else:
            # If both polity and other_polity are None, exclude both from the filter
            all_rels = Polity_preceding_entity.objects.none()

        context["myvar"] = self.model.Code.variable
        context["all_rels"] = all_rels

        return context


class Polity_preceding_entityDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_preceding_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_preceding_entity
    success_url = reverse_lazy("polity_preceding_entitys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_preceding_entityListView(ListView):
    """
    Paginated view for listing all Polity_preceding_entity instances.
    """

    model = Polity_preceding_entity
    template_name = (
        "general/polity_preceding_entity/polity_preceding_entity_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_preceding_entitys")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_preceding_entityListAllView(ListView):
    """
    View for listing all Polity_preceding_entity instances.
    """

    model = Polity_preceding_entity
    template_name = (
        "general/polity_preceding_entity/polity_preceding_entity_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_preceding_entitys_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_preceding_entity instances.

        Returns:
            QuerySet: The queryset of Polity_preceding_entity instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_preceding_entity.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_preceding_entityDetailView(DetailView):
    """
    View for displaying a single Polity_preceding_entity instance.
    """

    model = Polity_preceding_entity
    template_name = (
        "general/polity_preceding_entity/polity_preceding_entity_detail.html"
    )


class Polity_succeeding_entityCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_succeeding_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_succeeding_entity
    form_class = Polity_succeeding_entityForm
    template_name = (
        "general/polity_succeeding_entity/polity_succeeding_entity_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_succeeding_entity-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_succeeding_entityUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_succeeding_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_succeeding_entity
    form_class = Polity_succeeding_entityForm
    template_name = (
        "general/polity_succeeding_entity/polity_succeeding_entity_update.html"
    )
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_succeeding_entityDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_succeeding_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_succeeding_entity
    success_url = reverse_lazy("polity_succeeding_entitys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_succeeding_entityListView(ListView):
    """
    Paginated view for listing all Polity_succeeding_entity instances.
    """

    model = Polity_succeeding_entity
    template_name = (
        "general/polity_succeeding_entity/polity_succeeding_entity_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_succeeding_entitys")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_succeeding_entityListAllView(ListView):
    """
    View for listing all Polity_succeeding_entity instances.
    """

    model = Polity_succeeding_entity
    template_name = "general/polity_succeeding_entity/polity_succeeding_entity_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_succeeding_entitys_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_succeeding_entity instances.

        Returns:
            QuerySet: The queryset of Polity_succeeding_entity instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_succeeding_entity.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_succeeding_entityDetailView(DetailView):
    """
    View for displaying a single Polity_succeeding_entity instance.
    """

    model = Polity_succeeding_entity
    template_name = (
        "general/polity_succeeding_entity/polity_succeeding_entity_detail.html"
    )


class Polity_supracultural_entityCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_supracultural_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_supracultural_entity
    form_class = Polity_supracultural_entityForm
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_supracultural_entity-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_supracultural_entityUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Polity_supracultural_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_supracultural_entity
    form_class = Polity_supracultural_entityForm
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_update.html"  # noqa: E501 pylint: disable=C0301
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_supracultural_entityDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Polity_supracultural_entity.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_supracultural_entity
    success_url = reverse_lazy("polity_supracultural_entitys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_supracultural_entityListView(ListView):
    """
    Paginated view for listing all Polity_supracultural_entity instances.
    """

    model = Polity_supracultural_entity
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_supracultural_entitys")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_supracultural_entityListAllView(ListView):
    """
    View for listing all Polity_supracultural_entity instances.
    """

    model = Polity_supracultural_entity
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_supracultural_entitys_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_supracultural_entity instances.

        Returns:
            QuerySet: The queryset of Polity_supracultural_entity instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_supracultural_entity.objects.all().order_by(
            order, order2
        )

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_supracultural_entityDetailView(DetailView):
    """
    View for displaying a single Polity_supracultural_entity instance.
    """

    model = Polity_supracultural_entity
    template_name = "general/polity_supracultural_entity/polity_supracultural_entity_detail.html"  # noqa: E501 pylint: disable=C0301


class Polity_scale_of_supracultural_interactionCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_scale_of_supracultural_interaction.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_scale_of_supracultural_interaction
    form_class = Polity_scale_of_supracultural_interactionForm
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_scale_of_supracultural_interaction-create")

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

        context["mysection"] = self.model.Code.section
        context["mysubsection"] = "General Variables"
        context["myvar"] = self.model.Code.variable
        context["my_exp"] = self.model.Code.description
        context["var_null_meaning"] = self.model.Code.null_meaning
        context["inner_vars"] = self.model.Code.inner_variables
        context["potential_cols"] = self.model.Code.potential_cols

        return context


class Polity_scale_of_supracultural_interactionUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Polity_scale_of_supracultural_interaction.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_scale_of_supracultural_interaction
    form_class = Polity_scale_of_supracultural_interactionForm
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_update.html"  # noqa: E501 pylint: disable=C0301
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_scale_of_supracultural_interactionDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Polity_scale_of_supracultural_interaction.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_scale_of_supracultural_interaction
    success_url = reverse_lazy("polity_scale_of_supracultural_interactions")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_scale_of_supracultural_interactionListView(ListView):
    """
    Paginated view for listing all Polity_scale_of_supracultural_interaction instances.
    """

    model = Polity_scale_of_supracultural_interaction
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_scale_of_supracultural_interactions")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": ["Units"],
            },
        )

        return context


class Polity_scale_of_supracultural_interactionListAllView(ListView):
    """
    View for listing all Polity_scale_of_supracultural_interaction instances.
    """

    model = Polity_scale_of_supracultural_interaction
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_scale_of_supracultural_interactions_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_scale_of_supracultural_interaction instances.

        Returns:
            QuerySet: The queryset of Polity_scale_of_supracultural_interaction instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return (
            Polity_scale_of_supracultural_interaction.objects.all().order_by(
                order, order2
            )
        )

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": ["Units"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_scale_of_supracultural_interactionDetailView(DetailView):
    """
    View for displaying a single Polity_scale_of_supracultural_interaction instance.
    """

    model = Polity_scale_of_supracultural_interaction
    template_name = "general/polity_scale_of_supracultural_interaction/polity_scale_of_supracultural_interaction_detail.html"  # noqa: E501 pylint: disable=C0301


class Polity_alternate_religion_genusCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_alternate_religion_genus.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternate_religion_genus
    form_class = Polity_alternate_religion_genusForm
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the 'alternate_religion_genus' field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["alternate_religion_genus"].choices = sorted(
            form.fields["alternate_religion_genus"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternate_religion_genus-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_alternate_religion_genusUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Polity_alternate_religion_genus.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternate_religion_genus
    form_class = Polity_alternate_religion_genusForm
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the 'alternate_religion_genus' field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["alternate_religion_genus"].choices = sorted(
            form.fields["alternate_religion_genus"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_alternate_religion_genusDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Polity_alternate_religion_genus.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternate_religion_genus
    success_url = reverse_lazy("polity_alternate_religion_genuss")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_alternate_religion_genusListView(ListView):
    """
    Paginated view for listing all Polity_alternate_religion_genus instances.
    """

    model = Polity_alternate_religion_genus
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternate_religion_genuss")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_alternate_religion_genusListAllView(ListView):
    """
    View for listing all Polity_alternate_religion_genus instances.
    """

    model = Polity_alternate_religion_genus
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternate_religion_genuss_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_alternate_religion_genus instances.

        Returns:
            QuerySet: The queryset of Polity_alternate_religion_genus instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_alternate_religion_genus.objects.all().order_by(
            order, order2
        )

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_alternate_religion_genusDetailView(DetailView):
    """
    View for displaying a single Polity_alternate_religion_genus instance.
    """

    model = Polity_alternate_religion_genus
    template_name = "general/polity_alternate_religion_genus/polity_alternate_religion_genus_detail.html"  # noqa: E501 pylint: disable=C0301


class Polity_alternate_religion_familyCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_alternate_religion_family.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternate_religion_family
    form_class = Polity_alternate_religion_familyForm
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the 'alternate_religion_family' field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["alternate_religion_family"].choices = sorted(
            form.fields["alternate_religion_family"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternate_religion_family-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_alternate_religion_familyUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Polity_alternate_religion_family.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternate_religion_family
    form_class = Polity_alternate_religion_familyForm
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the 'alternate_religion_family' field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["alternate_religion_family"].choices = sorted(
            form.fields["alternate_religion_family"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_alternate_religion_familyDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Polity_alternate_religion_family.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternate_religion_family
    success_url = reverse_lazy("polity_alternate_religion_familys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_alternate_religion_familyListView(ListView):
    """
    Paginated view for listing all Polity_alternate_religion_family instances.
    """

    model = Polity_alternate_religion_family
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternate_religion_familys")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_alternate_religion_familyListAllView(ListView):
    """
    View for listing all Polity_alternate_religion_family instances.
    """

    model = Polity_alternate_religion_family
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternate_religion_familys_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_alternate_religion_family instances.

        Returns:
            QuerySet: The queryset of Polity_alternate_religion_family instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_alternate_religion_family.objects.all().order_by(
            order, order2
        )

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_alternate_religion_familyDetailView(DetailView):
    """
    View for displaying a single Polity_alternate_religion_family instance.
    """

    model = Polity_alternate_religion_family
    template_name = "general/polity_alternate_religion_family/polity_alternate_religion_family_detail.html"  # noqa: E501 pylint: disable=C0301


class Polity_alternate_religionCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_alternate_religion.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternate_religion
    form_class = Polity_alternate_religionForm
    template_name = (
        "general/polity_alternate_religion/polity_alternate_religion_form.html"
    )
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the 'alternate_religion' field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["alternate_religion"].choices = sorted(
            form.fields["alternate_religion"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternate_religion-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_alternate_religionUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_alternate_religion.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternate_religion
    form_class = Polity_alternate_religionForm
    template_name = "general/polity_alternate_religion/polity_alternate_religion_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_form(self, form_class=None):
        """
        Get the form of the view. Sort the choices of the 'alternate_religion' field.

        Args:
            form_class: The form class. Defaults to None.

        Returns:
            Form: The form of the view.
        """
        form = super().get_form(form_class)
        form.fields["alternate_religion"].choices = sorted(
            form.fields["alternate_religion"].choices,
            key=lambda x: x[1].lower(),
        )
        return form

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
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_alternate_religionDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_alternate_religion.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_alternate_religion
    success_url = reverse_lazy("polity_alternate_religions")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_alternate_religionListView(ListView):
    """
    Paginated view for listing all Polity_alternate_religion instances.
    """

    model = Polity_alternate_religion
    template_name = (
        "general/polity_alternate_religion/polity_alternate_religion_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternate_religions")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_alternate_religionListAllView(ListView):
    """
    View for listing all Polity_alternate_religion instances.
    """

    model = Polity_alternate_religion
    template_name = "general/polity_alternate_religion/polity_alternate_religion_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_alternate_religions_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_alternate_religion instances.

        Returns:
            QuerySet: The queryset of Polity_alternate_religion instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_alternate_religion.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_alternate_religionDetailView(DetailView):
    """
    View for displaying a single Polity_alternate_religion instance.
    """

    model = Polity_alternate_religion
    template_name = "general/polity_alternate_religion/polity_alternate_religion_detail.html"  # noqa: E501 pylint: disable=C0301


class Polity_expertCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Polity_expert.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_expert
    form_class = Polity_expertForm
    template_name = "general/polity_expert/polity_expert_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_expert-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_expertUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_expert.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_expert
    form_class = Polity_expertForm
    template_name = "general/polity_expert/polity_expert_update.html"
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_expertDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_expert.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_expert
    success_url = reverse_lazy("polity_experts")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_expertListView(ListView):
    """
    Paginated view for listing all Polity_expert instances.
    """

    model = Polity_expert
    template_name = "general/polity_expert/polity_expert_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_experts")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_expertListAllView(ListView):
    """
    View for listing all Polity_expert instances.
    """

    model = Polity_expert
    template_name = "general/polity_expert/polity_expert_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_experts_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_expert instances.

        Returns:
            QuerySet: The queryset of Polity_expert instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_expert.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_expertDetailView(DetailView):
    """
    View for displaying a single Polity_expert instance.
    """

    model = Polity_expert
    template_name = "general/polity_expert/polity_expert_detail.html"


class Polity_editorCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Polity_editor.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_editor
    form_class = Polity_editorForm
    template_name = "general/polity_editor/polity_editor_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_editor-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_editorUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_editor.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_editor
    form_class = Polity_editorForm
    template_name = "general/polity_editor/polity_editor_update.html"
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_editorDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_editor.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_editor
    success_url = reverse_lazy("polity_editors")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_editorListView(ListView):
    """
    Paginated view for listing all Polity_editor instances.
    """

    model = Polity_editor
    template_name = "general/polity_editor/polity_editor_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_editors")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_editorListAllView(ListView):
    """
    View for listing all Polity_editor instances.
    """

    model = Polity_editor
    template_name = "general/polity_editor/polity_editor_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_editors_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_editor instances.

        Returns:
            QuerySet: The queryset of Polity_editor instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_editor.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_editorDetailView(DetailView):
    """
    View for displaying a single Polity_editor instance.
    """

    model = Polity_editor
    template_name = "general/polity_editor/polity_editor_detail.html"


class Polity_religious_traditionCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_religious_tradition.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religious_tradition
    form_class = Polity_religious_traditionForm
    template_name = "general/polity_religious_tradition/polity_religious_tradition_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religious_tradition-create")

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
                "mysection": self.model.Code.section,
                "mysubsection": self.model.Code.section,  # noqa: E501   TODO: This should be subsection -- misdefined in the original script?  pylint: disable=C0301
                "myvar": self.model.Code.variable,
                "my_exp": self.model.Code.description,
                "var_null_meaning": self.model.Code.null_meaning,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_religious_traditionUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """
    View for updating an existing Polity_religious_tradition.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religious_tradition
    form_class = Polity_religious_traditionForm
    template_name = "general/polity_religious_tradition/polity_religious_tradition_update.html"  # noqa: E501 pylint: disable=C0301
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

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class Polity_religious_traditionDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Polity_religious_tradition.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_religious_tradition
    success_url = reverse_lazy("polity_religious_traditions")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_religious_traditionListView(ListView):
    """
    Paginated view for listing all Polity_religious_tradition instances.
    """

    model = Polity_religious_tradition
    template_name = "general/polity_religious_tradition/polity_religious_tradition_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religious_traditions")

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
            },
        )

        return context


class Polity_religious_traditionListAllView(ListView):
    """
    View for listing all Polity_religious_tradition instances.
    """

    model = Polity_religious_tradition
    template_name = "general/polity_religious_tradition/polity_religious_tradition_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_religious_traditions_all")

    def get_queryset(self):
        """
        Get the queryset of Polity_religious_tradition instances.

        Returns:
            QuerySet: The queryset of Polity_religious_tradition instances.
        """
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_religious_tradition.objects.all().order_by(order, order2)

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
                "myvar": self.model.Code.variable,
                "var_main_desc": self.model.Code.description,
                "var_main_desc_source": self.model.Code.description_source,
                "var_section": "General Variables",
                "var_subsection": "General",
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Polity_religious_traditionDetailView(DetailView):
    """
    View for displaying a single Polity_religious_tradition instance.
    """

    model = Polity_religious_tradition
    template_name = "general/polity_religious_tradition/polity_religious_tradition_detail.html"  # noqa: E501 pylint: disable=C0301


def generalvars_view(request):
    context = get_variable_context(
        app_name=APP_NAME,
        exclude=[
            "Polity_research_assistant",
            "Polity_editor",
            "Polity_expert",
        ],
    )
    return render(request, "general/generalvars.html", context=context)
