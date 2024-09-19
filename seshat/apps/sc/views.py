# TODO: move the metadata values to the Code attribute on models.

from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)

from ..core.models import Reference
from ..general.mixins import PolityIdMixin
from ..global_utils import (
    check_permissions,
    get_problematic_data_context,
    has_add_capital_permission,
    get_variable_context
)
from ..global_constants import ABSENT_PRESENT_STRING_LIST

from .forms import (
    RaForm,
    Polity_territoryForm,
    Polity_populationForm,
    Population_of_the_largest_settlementForm,
    Settlement_hierarchyForm,
    Administrative_levelForm,
    Religious_levelForm,
    Military_levelForm,
    Professional_military_officerForm,
    Professional_soldierForm,
    Professional_priesthoodForm,
    Full_time_bureaucratForm,
    Examination_systemForm,
    Merit_promotionForm,
    Specialized_government_buildingForm,
    Formal_legal_codeForm,
    JudgeForm,
    CourtForm,
    Professional_lawyerForm,
    Irrigation_systemForm,
    Drinking_water_supply_systemForm,
    MarketForm,
    Food_storage_siteForm,
    RoadForm,
    BridgeForm,
    CanalForm,
    PortForm,
    Mines_or_quarryForm,
    Mnemonic_deviceForm,
    Nonwritten_recordForm,
    Written_recordForm,
    ScriptForm,
    Non_phonetic_writingForm,
    Phonetic_alphabetic_writingForm,
    Lists_tables_and_classificationForm,
    CalendarForm,
    Sacred_textForm,
    Religious_literatureForm,
    Practical_literatureForm,
    HistoryForm,
    PhilosophyForm,
    Scientific_literatureForm,
    FictionForm,
    ArticleForm,
    TokenForm,
    Precious_metalForm,
    Foreign_coinForm,
    Indigenous_coinForm,
    Paper_currencyForm,
    CourierForm,
    Postal_stationForm,
    General_postal_serviceForm,
)
from .models import (
    Ra,
    Polity_territory,
    Polity_population,
    Population_of_the_largest_settlement,
    Settlement_hierarchy,
    Administrative_level,
    Religious_level,
    Military_level,
    Professional_military_officer,
    Professional_soldier,
    Professional_priesthood,
    Full_time_bureaucrat,
    Examination_system,
    Merit_promotion,
    Specialized_government_building,
    Formal_legal_code,
    Judge,
    Court,
    Professional_lawyer,
    Irrigation_system,
    Drinking_water_supply_system,
    Market,
    Food_storage_site,
    Road,
    Bridge,
    Canal,
    Port,
    Mines_or_quarry,
    Mnemonic_device,
    Nonwritten_record,
    Written_record,
    Script,
    Non_phonetic_writing,
    Phonetic_alphabetic_writing,
    Lists_tables_and_classification,
    Calendar,
    Sacred_text,
    Religious_literature,
    Practical_literature,
    History,
    Philosophy,
    Scientific_literature,
    Fiction,
    Article,
    Token,
    Precious_metal,
    Foreign_coin,
    Indigenous_coin,
    Paper_currency,
    Courier,
    Postal_station,
    General_postal_service,
)
from .constants import APP_NAME
from .specific_views.downloads import (
    ra_download_view,
    ra_meta_download_view,
    polity_territory_download_view,
    polity_territory_meta_download_view,
    polity_population_download_view,
    polity_population_meta_download_view,
    population_of_the_largest_settlement_download_view,
    population_of_the_largest_settlement_meta_download_view,
    settlement_hierarchy_download_view,
    settlement_hierarchy_meta_download_view,
    administrative_level_download_view,
    administrative_level_meta_download_view,
    religious_level_download_view,
    religious_level_meta_download_view,
    military_level_download_view,
    military_level_meta_download_view,
    professional_military_officer_download_view,
    professional_military_officer_meta_download_view,
    professional_soldier_download_view,
    professional_soldier_meta_download_view,
    professional_priesthood_download_view,
    full_time_bureaucrat_download_view,
    full_time_bureaucrat_meta_download_view,
    examination_system_download_view,
    examination_system_meta_download_view,
    merit_promotion_download_view,
    merit_promotion_meta_download_view,
    specialized_government_building_download_view,
    specialized_government_building_meta_download_view,
    formal_legal_code_download_view,
    formal_legal_code_meta_download_view,
    judge_download_view,
    judge_meta_download_view,
    court_download_view,
    court_meta_download_view,
    professional_lawyer_download_view,
    professional_lawyer_meta_download_view,
    irrigation_system_download_view,
    irrigation_system_meta_download_view,
    drinking_water_supply_system_download_view,
    drinking_water_supply_system_meta_download_view,
    market_download_view,
    market_meta_download_view,
    food_storage_site_download_view,
    food_storage_site_meta_download_view,
    road_download_view,
    road_meta_download_view,
    bridge_download_view,
    bridge_meta_download_view,
    canal_download_view,
    canal_meta_download_view,
    port_download_view,
    port_meta_download_view,
    mines_or_quarry_download_view,
    mines_or_quarry_meta_download_view,
    mnemonic_device_download_view,
    mnemonic_device_meta_download_view,
    nonwritten_record_download_view,
    nonwritten_record_meta_download_view,
    written_record_download_view,
    written_record_meta_download_view,
    script_download_view,
    script_meta_download_view,
    non_phonetic_writing_download_view,
    non_phonetic_writing_meta_download_view,
    phonetic_alphabetic_writing_download_view,
    phonetic_alphabetic_writing_meta_download_view,
    lists_tables_and_classification_download_view,
    lists_tables_and_classification_meta_download_view,
    calendar_download_view,
    calendar_meta_download_view,
    sacred_text_download_view,
    sacred_text_meta_download_view,
    religious_literature_download_view,
    religious_literature_meta_download_view,
    practical_literature_download_view,
    practical_literature_meta_download_view,
    history_download_view,
    history_meta_download_view,
    philosophy_download_view,
    philosophy_meta_download_view,
    scientific_literature_download_view,
    scientific_literature_meta_download_view,
    fiction_download_view,
    fiction_meta_download_view,
    article_download_view,
    article_meta_download_view,
    token_download_view,
    token_meta_download_view,
    precious_metal_download_view,
    precious_metal_meta_download_view,
    foreign_coin_download_view,
    foreign_coin_meta_download_view,
    indigenous_coin_download_view,
    indigenous_coin_meta_download_view,
    paper_currency_download_view,
    paper_currency_meta_download_view,
    courier_download_view,
    courier_meta_download_view,
    postal_station_download_view,
    postal_station_meta_download_view,
    general_postal_service_download_view,
    general_postal_service_meta_download_view,
)


class RaCreateView(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Ra object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Ra
    form_class = RaForm
    template_name = "sc/ra/ra_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("ra-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class RaUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Ra object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Ra
    form_class = RaForm
    template_name = "sc/ra/ra_update.html"
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


class RaDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Ra object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Ra
    success_url = reverse_lazy("ras")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class RaListView(ListView):
    """
    Paginated view for listing all the Ra objects.
    """

    model = Ra
    template_name = "sc/ra/ra_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("ras")

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
            },
        )

        return context


class RaListAllView(ListView):
    """
    View for listing all the Ra objects.
    """

    model = Ra
    template_name = "sc/ra/ra_list_all.html"

    def get_absolute_url(self) -> str:
        return reverse("ras_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Ra.objects.all().order_by(order, order2)

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


class RaDetailView(DetailView):
    """
    View for displaying the details of a Ra object.
    """

    model = Ra
    template_name = "sc/ra/ra_detail.html"


class Polity_territoryCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_territory object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_territory
    form_class = Polity_territoryForm
    template_name = "sc/polity_territory/polity_territory_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_territory-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Polity_territoryUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_territory object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_territory
    form_class = Polity_territoryForm
    template_name = "sc/polity_territory/polity_territory_update.html"
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


class Polity_territoryDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_territory object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_territory
    success_url = reverse_lazy("polity_territorys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_territoryListView(ListView):
    """
    Paginated view for listing all the Polity_territory objects.
    """

    model = Polity_territory
    template_name = "sc/polity_territory/polity_territory_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_territorys")

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
            },
        )

        return context


class Polity_territoryListAllView(ListView):
    """
    View for listing all the Polity_territory objects.
    """

    model = Polity_territory
    template_name = "sc/polity_territory/polity_territory_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_territorys_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_territory.objects.all().order_by(order, order2)

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


class Polity_territoryDetailView(DetailView):
    """
    View for displaying the details of a Polity_territory object.
    """

    model = Polity_territory
    template_name = "sc/polity_territory/polity_territory_detail.html"


class Polity_populationCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Polity_population object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_population
    form_class = Polity_populationForm
    template_name = "sc/polity_population/polity_population_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_population-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Polity_populationUpdateView(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_population object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_population
    form_class = Polity_populationForm
    template_name = "sc/polity_population/polity_population_update.html"
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


class Polity_populationDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_population object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polity_population
    success_url = reverse_lazy("polity_populations")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Polity_populationListView(ListView):
    """
    Paginated view for listing all the Polity_population objects.
    """

    model = Polity_population
    template_name = "sc/polity_population/polity_population_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_populations")

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
            },
        )

        return context


class Polity_populationListAllView(ListView):
    """
    View for listing all the Polity_population objects.
    """

    model = Polity_population
    template_name = "sc/polity_population/polity_population_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polity_populations_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Polity_population.objects.all().order_by(order, order2)

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


class Polity_populationDetailView(DetailView):
    """
    View for displaying the details of a Polity_population object.
    """

    model = Polity_population
    template_name = "sc/polity_population/polity_population_detail.html"


class Population_of_the_largest_settlementCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """
    View for creating a new Population_of_the_largest_settlement object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Population_of_the_largest_settlement
    form_class = Population_of_the_largest_settlementForm
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("population_of_the_largest_settlement-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Population_of_the_largest_settlementUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Population_of_the_largest_settlement
    form_class = Population_of_the_largest_settlementForm
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_update.html"  # noqa: E501 pylint: disable=C0301
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


class Population_of_the_largest_settlementDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Population_of_the_largest_settlement object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Population_of_the_largest_settlement
    success_url = reverse_lazy("population_of_the_largest_settlements")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Population_of_the_largest_settlementListView(ListView):
    """
    Paginated view for listing all the Population_of_the_largest_settlement objects.
    """

    model = Population_of_the_largest_settlement
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("population_of_the_largest_settlements")

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
            },
        )

        return context


class Population_of_the_largest_settlementListAllView(ListView):
    """ """

    model = Population_of_the_largest_settlement
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("population_of_the_largest_settlements_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Population_of_the_largest_settlement.objects.all().order_by(
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
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Population_of_the_largest_settlementDetailView(DetailView):
    """ """

    model = Population_of_the_largest_settlement
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_detail.html"  # noqa: E501 pylint: disable=C0301


class Settlement_hierarchyCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Settlement_hierarchy
    form_class = Settlement_hierarchyForm
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("settlement_hierarchy-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Settlement_hierarchyUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Settlement_hierarchy
    form_class = Settlement_hierarchyForm
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_update.html"
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


class Settlement_hierarchyDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Settlement_hierarchy object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Settlement_hierarchy
    success_url = reverse_lazy("settlement_hierarchys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Settlement_hierarchyListView(ListView):
    """
    Paginated view for listing all the Settlement_hierarchy objects.
    """

    model = Settlement_hierarchy
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("settlement_hierarchys")

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
            },
        )

        return context


class Settlement_hierarchyListAllView(ListView):
    """ """

    model = Settlement_hierarchy
    template_name = (
        "sc/settlement_hierarchy/settlement_hierarchy_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("settlement_hierarchys_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Settlement_hierarchy.objects.all().order_by(order, order2)

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


class Settlement_hierarchyDetailView(DetailView):
    """ """

    model = Settlement_hierarchy
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_detail.html"


class Administrative_levelCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Administrative_level
    form_class = Administrative_levelForm
    template_name = "sc/administrative_level/administrative_level_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("administrative_level-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Administrative_levelUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Administrative_level
    form_class = Administrative_levelForm
    template_name = "sc/administrative_level/administrative_level_update.html"
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


class Administrative_levelDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Administrative_level object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Administrative_level
    success_url = reverse_lazy("administrative_levels")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Administrative_levelListView(ListView):
    """
    Paginated view for listing all the Administrative_level objects.
    """

    model = Administrative_level
    template_name = "sc/administrative_level/administrative_level_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("administrative_levels")

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
            },
        )

        return context


class Administrative_levelListAllView(ListView):
    """ """

    model = Administrative_level
    template_name = (
        "sc/administrative_level/administrative_level_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("administrative_levels_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Administrative_level.objects.all().order_by(order, order2)

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


class Administrative_levelDetailView(DetailView):
    """ """

    model = Administrative_level
    template_name = "sc/administrative_level/administrative_level_detail.html"


class Religious_levelCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Religious_level
    form_class = Religious_levelForm
    template_name = "sc/religious_level/religious_level_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("religious_level-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Religious_levelUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Religious_level
    form_class = Religious_levelForm
    template_name = "sc/religious_level/religious_level_update.html"
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


class Religious_levelDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Religious_level object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Religious_level
    success_url = reverse_lazy("religious_levels")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Religious_levelListView(ListView):
    """
    Paginated view for listing all the Religious_level objects.
    """

    model = Religious_level
    template_name = "sc/religious_level/religious_level_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("religious_levels")

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
            },
        )

        return context


class Religious_levelListAllView(ListView):
    """ """

    model = Religious_level
    template_name = "sc/religious_level/religious_level_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("religious_levels_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Religious_level.objects.all().order_by(order, order2)

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


class Religious_levelDetailView(DetailView):
    """ """

    model = Religious_level
    template_name = "sc/religious_level/religious_level_detail.html"


class Military_levelCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Military_level
    form_class = Military_levelForm
    template_name = "sc/military_level/military_level_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("military_level-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Military_levelUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Military_level
    form_class = Military_levelForm
    template_name = "sc/military_level/military_level_update.html"
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


class Military_levelDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Military_level object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Military_level
    success_url = reverse_lazy("military_levels")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Military_levelListView(ListView):
    """
    Paginated view for listing all the Military_level objects.
    """

    model = Military_level
    template_name = "sc/military_level/military_level_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("military_levels")

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
            },
        )

        return context


class Military_levelDetailView(DetailView):
    """ """

    model = Military_level
    template_name = "sc/military_level/military_level_detail.html"


class Professional_military_officerCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_military_officer
    form_class = Professional_military_officerForm
    template_name = "sc/professional_military_officer/professional_military_officer_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_military_officer-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Professional_military_officerUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_military_officer
    form_class = Professional_military_officerForm
    template_name = "sc/professional_military_officer/professional_military_officer_update.html"  # noqa: E501 pylint: disable=C0301
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


class Professional_military_officerDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Professional_military_officer object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_military_officer
    success_url = reverse_lazy("professional_military_officers")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Professional_military_officerListView(ListView):
    """
    Paginated view for listing all the Professional_military_officer objects.
    """

    model = Professional_military_officer
    template_name = "sc/professional_military_officer/professional_military_officer_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_military_officers")

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
            },
        )

        return context


class Professional_military_officerListAllView(ListView):
    """ """

    model = Professional_military_officer
    template_name = "sc/professional_military_officer/professional_military_officer_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_military_officers_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Professional_military_officer.objects.all().order_by(
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
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Professional_military_officerDetailView(DetailView):
    """ """

    model = Professional_military_officer
    template_name = "sc/professional_military_officer/professional_military_officer_detail.html"  # noqa: E501 pylint: disable=C0301


class Professional_soldierCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_soldier
    form_class = Professional_soldierForm
    template_name = "sc/professional_soldier/professional_soldier_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_soldier-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Professional_soldierUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_soldier
    form_class = Professional_soldierForm
    template_name = "sc/professional_soldier/professional_soldier_update.html"
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


class Professional_soldierDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Professional_soldier object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_soldier
    success_url = reverse_lazy("professional_soldiers")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Professional_soldierListView(ListView):
    """
    Paginated view for listing all the Professional_soldier objects.
    """

    model = Professional_soldier
    template_name = "sc/professional_soldier/professional_soldier_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_soldiers")

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
            },
        )

        return context


class Professional_soldierListAllView(ListView):
    """ """

    model = Professional_soldier
    template_name = (
        "sc/professional_soldier/professional_soldier_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_soldiers_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Professional_soldier.objects.all().order_by(order, order2)

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


class Professional_soldierDetailView(DetailView):
    """ """

    model = Professional_soldier
    template_name = "sc/professional_soldier/professional_soldier_detail.html"


class Professional_priesthoodCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_priesthood
    form_class = Professional_priesthoodForm
    template_name = (
        "sc/professional_priesthood/professional_priesthood_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_priesthood-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Professional_priesthoodUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_priesthood
    form_class = Professional_priesthoodForm
    template_name = (
        "sc/professional_priesthood/professional_priesthood_update.html"
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


class Professional_priesthoodDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Professional_priesthood object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_priesthood
    success_url = reverse_lazy("professional_priesthoods")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Professional_priesthoodListView(ListView):
    """
    Paginated view for listing all the Professional_priesthood objects.
    """

    model = Professional_priesthood
    template_name = (
        "sc/professional_priesthood/professional_priesthood_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_priesthoods")

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
            },
        )

        return context


class Professional_priesthoodListAllView(ListView):
    """ """

    model = Professional_priesthood
    template_name = (
        "sc/professional_priesthood/professional_priesthood_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_priesthoods_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Professional_priesthood.objects.all().order_by(order, order2)

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


class Professional_priesthoodDetailView(DetailView):
    """ """

    model = Professional_priesthood
    template_name = (
        "sc/professional_priesthood/professional_priesthood_detail.html"
    )


class Full_time_bureaucratCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Full_time_bureaucrat
    form_class = Full_time_bureaucratForm
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("full_time_bureaucrat-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Full_time_bureaucratUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Full_time_bureaucrat
    form_class = Full_time_bureaucratForm
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_update.html"
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


class Full_time_bureaucratDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Full_time_bureaucrat object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Full_time_bureaucrat
    success_url = reverse_lazy("full_time_bureaucrats")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Full_time_bureaucratListView(ListView):
    """
    Paginated view for listing all the Full_time_bureaucrat objects.
    """

    model = Full_time_bureaucrat
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("full_time_bureaucrats")

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
            },
        )

        return context


class Full_time_bureaucratListAllView(ListView):
    """ """

    model = Full_time_bureaucrat
    template_name = (
        "sc/full_time_bureaucrat/full_time_bureaucrat_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("full_time_bureaucrats_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Full_time_bureaucrat.objects.all().order_by(order, order2)

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


class Full_time_bureaucratDetailView(DetailView):
    """ """

    model = Full_time_bureaucrat
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_detail.html"


class Examination_systemCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Examination_system
    form_class = Examination_systemForm
    template_name = "sc/examination_system/examination_system_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("examination_system-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Examination_systemUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Examination_system
    form_class = Examination_systemForm
    template_name = "sc/examination_system/examination_system_update.html"
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


class Examination_systemDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Examination_system object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Examination_system
    success_url = reverse_lazy("examination_systems")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Examination_systemListView(ListView):
    """
    Paginated view for listing all the Examination_system objects.
    """

    model = Examination_system
    template_name = "sc/examination_system/examination_system_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("examination_systems")

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
            },
        )

        return context


class Examination_systemListAllView(ListView):
    """ """

    model = Examination_system
    template_name = "sc/examination_system/examination_system_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("examination_systems_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Examination_system.objects.all().order_by(order, order2)

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


class Examination_systemDetailView(DetailView):
    """ """

    model = Examination_system
    template_name = "sc/examination_system/examination_system_detail.html"


class Merit_promotionCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Merit_promotion
    form_class = Merit_promotionForm
    template_name = "sc/merit_promotion/merit_promotion_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("merit_promotion-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Merit_promotionUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Merit_promotion
    form_class = Merit_promotionForm
    template_name = "sc/merit_promotion/merit_promotion_update.html"
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


class Merit_promotionDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Merit_promotion object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Merit_promotion
    success_url = reverse_lazy("merit_promotions")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Merit_promotionListView(ListView):
    """
    Paginated view for listing all the Merit_promotion objects.
    """

    model = Merit_promotion
    template_name = "sc/merit_promotion/merit_promotion_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("merit_promotions")

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
            },
        )

        return context


class Merit_promotionListAllView(ListView):
    """ """

    model = Merit_promotion
    template_name = "sc/merit_promotion/merit_promotion_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("merit_promotions_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Merit_promotion.objects.all().order_by(order, order2)

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


class Merit_promotionDetailView(DetailView):
    """ """

    model = Merit_promotion
    template_name = "sc/merit_promotion/merit_promotion_detail.html"


class Specialized_government_buildingCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Specialized_government_building
    form_class = Specialized_government_buildingForm
    template_name = "sc/specialized_government_building/specialized_government_building_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("specialized_government_building-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Specialized_government_buildingUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Specialized_government_building
    form_class = Specialized_government_buildingForm
    template_name = "sc/specialized_government_building/specialized_government_building_update.html"  # noqa: E501 pylint: disable=C0301
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


class Specialized_government_buildingDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Specialized_government_building object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Specialized_government_building
    success_url = reverse_lazy("specialized_government_buildings")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Specialized_government_buildingListView(ListView):
    """
    Paginated view for listing all the Specialized_government_building objects.
    """

    model = Specialized_government_building
    template_name = "sc/specialized_government_building/specialized_government_building_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("specialized_government_buildings")

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
            },
        )

        return context


class Specialized_government_buildingListAllView(ListView):
    """ """

    model = Specialized_government_building
    template_name = "sc/specialized_government_building/specialized_government_building_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("specialized_government_buildings_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Specialized_government_building.objects.all().order_by(
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
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Specialized_government_buildingDetailView(DetailView):
    """ """

    model = Specialized_government_building
    template_name = "sc/specialized_government_building/specialized_government_building_detail.html"  # noqa: E501 pylint: disable=C0301


class Formal_legal_codeCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Formal_legal_code
    form_class = Formal_legal_codeForm
    template_name = "sc/formal_legal_code/formal_legal_code_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("formal_legal_code-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Formal_legal_codeUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Formal_legal_code
    form_class = Formal_legal_codeForm
    template_name = "sc/formal_legal_code/formal_legal_code_update.html"
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


class Formal_legal_codeDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Formal_legal_code object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Formal_legal_code
    success_url = reverse_lazy("formal_legal_codes")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Formal_legal_codeListView(ListView):
    """
    Paginated view for listing all the Formal_legal_code objects.
    """

    model = Formal_legal_code
    template_name = "sc/formal_legal_code/formal_legal_code_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("formal_legal_codes")

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
            },
        )

        return context


class Formal_legal_codeListAllView(ListView):
    """ """

    model = Formal_legal_code
    template_name = "sc/formal_legal_code/formal_legal_code_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("formal_legal_codes_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Formal_legal_code.objects.all().order_by(order, order2)

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


class Formal_legal_codeDetailView(DetailView):
    """ """

    model = Formal_legal_code
    template_name = "sc/formal_legal_code/formal_legal_code_detail.html"


class JudgeCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Judge
    form_class = JudgeForm
    template_name = "sc/judge/judge_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("judge-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class JudgeUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Judge
    form_class = JudgeForm
    template_name = "sc/judge/judge_update.html"
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


class JudgeDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Judge object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Judge
    success_url = reverse_lazy("judges")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class JudgeListView(ListView):
    """
    Paginated view for listing all the Judge objects.
    """

    model = Judge
    template_name = "sc/judge/judge_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("judges")

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
            },
        )

        return context


class JudgeListAllView(ListView):
    """ """

    model = Judge
    template_name = "sc/judge/judge_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("judges_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Judge.objects.all().order_by(order, order2)

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


class JudgeDetailView(DetailView):
    """ """

    model = Judge
    template_name = "sc/judge/judge_detail.html"


class CourtCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Court
    form_class = CourtForm
    template_name = "sc/court/court_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("court-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class CourtUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Court
    form_class = CourtForm
    template_name = "sc/court/court_update.html"
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


class CourtDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Court object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Court
    success_url = reverse_lazy("courts")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CourtListView(ListView):
    """
    Paginated view for listing all the Court objects.
    """

    model = Court
    template_name = "sc/court/court_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("courts")

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
            },
        )

        return context


class CourtListAllView(ListView):
    """ """

    model = Court
    template_name = "sc/court/court_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("courts_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Court.objects.all().order_by(order, order2)

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


class CourtDetailView(DetailView):
    """ """

    model = Court
    template_name = "sc/court/court_detail.html"


class Professional_lawyerCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_lawyer
    form_class = Professional_lawyerForm
    template_name = "sc/professional_lawyer/professional_lawyer_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_lawyer-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Professional_lawyerUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_lawyer
    form_class = Professional_lawyerForm
    template_name = "sc/professional_lawyer/professional_lawyer_update.html"
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


class Professional_lawyerDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Professional_lawyer object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Professional_lawyer
    success_url = reverse_lazy("professional_lawyers")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Professional_lawyerListView(ListView):
    """
    Paginated view for listing all the Professional_lawyer objects.
    """

    model = Professional_lawyer
    template_name = "sc/professional_lawyer/professional_lawyer_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_lawyers")

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
            },
        )

        return context


class Professional_lawyerListAllView(ListView):
    """ """

    model = Professional_lawyer
    template_name = "sc/professional_lawyer/professional_lawyer_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("professional_lawyers_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Professional_lawyer.objects.all().order_by(order, order2)

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


class Professional_lawyerDetailView(DetailView):
    """ """

    model = Professional_lawyer
    template_name = "sc/professional_lawyer/professional_lawyer_detail.html"


class Irrigation_systemCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Irrigation_system
    form_class = Irrigation_systemForm
    template_name = "sc/irrigation_system/irrigation_system_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("irrigation_system-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Irrigation_systemUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Irrigation_system
    form_class = Irrigation_systemForm
    template_name = "sc/irrigation_system/irrigation_system_update.html"
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


class Irrigation_systemDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Irrigation_system object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Irrigation_system
    success_url = reverse_lazy("irrigation_systems")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Irrigation_systemListView(ListView):
    """
    Paginated view for listing all the Irrigation_system objects.
    """

    model = Irrigation_system
    template_name = "sc/irrigation_system/irrigation_system_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("irrigation_systems")

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
            },
        )

        return context


class Irrigation_systemListAllView(ListView):
    """ """

    model = Irrigation_system
    template_name = "sc/irrigation_system/irrigation_system_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("irrigation_systems_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Irrigation_system.objects.all().order_by(order, order2)

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


class Irrigation_systemDetailView(DetailView):
    """ """

    model = Irrigation_system
    template_name = "sc/irrigation_system/irrigation_system_detail.html"


class Drinking_water_supply_systemCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Drinking_water_supply_system
    form_class = Drinking_water_supply_systemForm
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("drinking_water_supply_system-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Drinking_water_supply_systemUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Drinking_water_supply_system
    form_class = Drinking_water_supply_systemForm
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_update.html"  # noqa: E501 pylint: disable=C0301
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


class Drinking_water_supply_systemDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Drinking_water_supply_system object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Drinking_water_supply_system
    success_url = reverse_lazy("drinking_water_supply_systems")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Drinking_water_supply_systemListView(ListView):
    """
    Paginated view for listing all the Drinking_water_supply_system objects.
    """

    model = Drinking_water_supply_system
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("drinking_water_supply_systems")

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
            },
        )

        return context


class Drinking_water_supply_systemListAllView(ListView):
    """ """

    model = Drinking_water_supply_system
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("drinking_water_supply_systems_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Drinking_water_supply_system.objects.all().order_by(
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
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Drinking_water_supply_systemDetailView(DetailView):
    """ """

    model = Drinking_water_supply_system
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_detail.html"  # noqa: E501 pylint: disable=C0301


class MarketCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Market
    form_class = MarketForm
    template_name = "sc/market/market_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("market-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class MarketUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Market
    form_class = MarketForm
    template_name = "sc/market/market_update.html"
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


class MarketDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Market object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Market
    success_url = reverse_lazy("markets")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class MarketListView(ListView):
    """
    Paginated view for listing all the Market objects.
    """

    model = Market
    template_name = "sc/market/market_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("markets")

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
            },
        )

        return context


class MarketListAllView(ListView):
    """ """

    model = Market
    template_name = "sc/market/market_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("markets_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Market.objects.all().order_by(order, order2)

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


class MarketDetailView(DetailView):
    """ """

    model = Market
    template_name = "sc/market/market_detail.html"


class Food_storage_siteCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Food_storage_site
    form_class = Food_storage_siteForm
    template_name = "sc/food_storage_site/food_storage_site_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("food_storage_site-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Food_storage_siteUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Food_storage_site
    form_class = Food_storage_siteForm
    template_name = "sc/food_storage_site/food_storage_site_update.html"
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


class Food_storage_siteDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Food_storage_site object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Food_storage_site
    success_url = reverse_lazy("food_storage_sites")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Food_storage_siteListView(ListView):
    """
    Paginated view for listing all the Food_storage_site objects.
    """

    model = Food_storage_site
    template_name = "sc/food_storage_site/food_storage_site_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("food_storage_sites")

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
            },
        )

        return context


class Food_storage_siteListAllView(ListView):
    """ """

    model = Food_storage_site
    template_name = "sc/food_storage_site/food_storage_site_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("food_storage_sites_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Food_storage_site.objects.all().order_by(order, order2)

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


class Food_storage_siteDetailView(DetailView):
    """ """

    model = Food_storage_site
    template_name = "sc/food_storage_site/food_storage_site_detail.html"


class RoadCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Road
    form_class = RoadForm
    template_name = "sc/road/road_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("road-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class RoadUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Road
    form_class = RoadForm
    template_name = "sc/road/road_update.html"
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


class RoadDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Road object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Road
    success_url = reverse_lazy("roads")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class RoadListView(ListView):
    """
    Paginated view for listing all the Road objects.
    """

    model = Road
    template_name = "sc/road/road_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("roads")

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
            },
        )

        return context


class RoadListAllView(ListView):
    """ """

    model = Road
    template_name = "sc/road/road_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("roads_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Road.objects.all().order_by(order, order2)

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


class RoadDetailView(DetailView):
    """ """

    model = Road
    template_name = "sc/road/road_detail.html"


class BridgeCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Bridge
    form_class = BridgeForm
    template_name = "sc/bridge/bridge_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("bridge-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class BridgeUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Bridge
    form_class = BridgeForm
    template_name = "sc/bridge/bridge_update.html"
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


class BridgeDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Bridge object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Bridge
    success_url = reverse_lazy("bridges")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class BridgeListView(ListView):
    """
    Paginated view for listing all the Bridge objects.
    """

    model = Bridge
    template_name = "sc/bridge/bridge_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("bridges")

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
            },
        )

        return context


class BridgeListAllView(ListView):
    """ """

    model = Bridge
    template_name = "sc/bridge/bridge_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("bridges_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Bridge.objects.all().order_by(order, order2)

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


class BridgeDetailView(DetailView):
    """ """

    model = Bridge
    template_name = "sc/bridge/bridge_detail.html"


class CanalCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Canal
    form_class = CanalForm
    template_name = "sc/canal/canal_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("canal-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class CanalUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Canal
    form_class = CanalForm
    template_name = "sc/canal/canal_update.html"
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


class CanalDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Canal object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Canal
    success_url = reverse_lazy("canals")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CanalListView(ListView):
    """
    Paginated view for listing all the Canal objects.
    """

    model = Canal
    template_name = "sc/canal/canal_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("canals")

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
            },
        )

        return context


class CanalListAllView(ListView):
    """ """

    model = Canal
    template_name = "sc/canal/canal_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("canals_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Canal.objects.all().order_by(order, order2)

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


class CanalDetailView(DetailView):
    """ """

    model = Canal
    template_name = "sc/canal/canal_detail.html"


class PortCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Port
    form_class = PortForm
    template_name = "sc/port/port_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("port-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class PortUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Port
    form_class = PortForm
    template_name = "sc/port/port_update.html"
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


class PortDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Port object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Port
    success_url = reverse_lazy("ports")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class PortListView(ListView):
    """
    Paginated view for listing all the Port objects.
    """

    model = Port
    template_name = "sc/port/port_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("ports")

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
            },
        )

        return context


class PortListAllView(ListView):
    """ """

    model = Port
    template_name = "sc/port/port_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("ports_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Port.objects.all().order_by(order, order2)

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


class PortDetailView(DetailView):
    """ """

    model = Port
    template_name = "sc/port/port_detail.html"


class Mines_or_quarryCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Mines_or_quarry
    form_class = Mines_or_quarryForm
    template_name = "sc/mines_or_quarry/mines_or_quarry_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("mines_or_quarry-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Mines_or_quarryUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Mines_or_quarry
    form_class = Mines_or_quarryForm
    template_name = "sc/mines_or_quarry/mines_or_quarry_update.html"
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


class Mines_or_quarryDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Mines_or_quarry object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Mines_or_quarry
    success_url = reverse_lazy("mines_or_quarrys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Mines_or_quarryListView(ListView):
    """
    Paginated view for listing all the Mines_or_quarry objects.
    """

    model = Mines_or_quarry
    template_name = "sc/mines_or_quarry/mines_or_quarry_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("mines_or_quarrys")

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
            },
        )

        return context


class Mines_or_quarryListAllView(ListView):
    """ """

    model = Mines_or_quarry
    template_name = "sc/mines_or_quarry/mines_or_quarry_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("mines_or_quarrys_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Mines_or_quarry.objects.all().order_by(order, order2)

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


class Mines_or_quarryDetailView(DetailView):
    """ """

    model = Mines_or_quarry
    template_name = "sc/mines_or_quarry/mines_or_quarry_detail.html"


class Mnemonic_deviceCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Mnemonic_device
    form_class = Mnemonic_deviceForm
    template_name = "sc/mnemonic_device/mnemonic_device_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("mnemonic_device-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Mnemonic_deviceUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Mnemonic_device
    form_class = Mnemonic_deviceForm
    template_name = "sc/mnemonic_device/mnemonic_device_update.html"
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


class Mnemonic_deviceDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Mnemonic_device object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Mnemonic_device
    success_url = reverse_lazy("mnemonic_devices")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Mnemonic_deviceListView(ListView):
    """
    Paginated view for listing all the Mnemonic_device objects.
    """

    model = Mnemonic_device
    template_name = "sc/mnemonic_device/mnemonic_device_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("mnemonic_devices")

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
            },
        )

        return context


class Mnemonic_deviceListAllView(ListView):
    """ """

    model = Mnemonic_device
    template_name = "sc/mnemonic_device/mnemonic_device_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("mnemonic_devices_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Mnemonic_device.objects.all().order_by(order, order2)

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


class Mnemonic_deviceDetailView(DetailView):
    """ """

    model = Mnemonic_device
    template_name = "sc/mnemonic_device/mnemonic_device_detail.html"


class Nonwritten_recordCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Nonwritten_record
    form_class = Nonwritten_recordForm
    template_name = "sc/nonwritten_record/nonwritten_record_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("nonwritten_record-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Nonwritten_recordUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Nonwritten_record
    form_class = Nonwritten_recordForm
    template_name = "sc/nonwritten_record/nonwritten_record_update.html"
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


class Nonwritten_recordDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Nonwritten_record object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Nonwritten_record
    success_url = reverse_lazy("nonwritten_records")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Nonwritten_recordListView(ListView):
    """
    Paginated view for listing all the Nonwritten_record objects.
    """

    model = Nonwritten_record
    template_name = "sc/nonwritten_record/nonwritten_record_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("nonwritten_records")

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
            },
        )

        return context


class Nonwritten_recordListAllView(ListView):
    """ """

    model = Nonwritten_record
    template_name = "sc/nonwritten_record/nonwritten_record_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("nonwritten_records_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Nonwritten_record.objects.all().order_by(order, order2)

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


class Nonwritten_recordDetailView(DetailView):
    """ """

    model = Nonwritten_record
    template_name = "sc/nonwritten_record/nonwritten_record_detail.html"


class Written_recordCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Written_record
    form_class = Written_recordForm
    template_name = "sc/written_record/written_record_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("written_record-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Written_recordUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Written_record
    form_class = Written_recordForm
    template_name = "sc/written_record/written_record_update.html"
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


class Written_recordDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Written_record object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Written_record
    success_url = reverse_lazy("written_records")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Written_recordListView(ListView):
    """
    Paginated view for listing all the Written_record objects.
    """

    model = Written_record
    template_name = "sc/written_record/written_record_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("written_records")

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
            },
        )

        return context


class Written_recordListAllView(ListView):
    """ """

    model = Written_record
    template_name = "sc/written_record/written_record_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("written_records_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Written_record.objects.all().order_by(order, order2)

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


class Written_recordDetailView(DetailView):
    """ """

    model = Written_record
    template_name = "sc/written_record/written_record_detail.html"


class ScriptCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Script
    form_class = ScriptForm
    template_name = "sc/script/script_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("script-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class ScriptUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Script
    form_class = ScriptForm
    template_name = "sc/script/script_update.html"
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


class ScriptDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Script object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Script
    success_url = reverse_lazy("scripts")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class ScriptListView(ListView):
    """
    Paginated view for listing all the Script objects.
    """

    model = Script
    template_name = "sc/script/script_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scripts")

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
            },
        )

        return context


class ScriptListAllView(ListView):
    """ """

    model = Script
    template_name = "sc/script/script_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scripts_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Script.objects.all().order_by(order, order2)

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


class ScriptDetailView(DetailView):
    """ """

    model = Script
    template_name = "sc/script/script_detail.html"


class Non_phonetic_writingCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Non_phonetic_writing
    form_class = Non_phonetic_writingForm
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("non_phonetic_writing-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Non_phonetic_writingUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Non_phonetic_writing
    form_class = Non_phonetic_writingForm
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_update.html"
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


class Non_phonetic_writingDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Non_phonetic_writing object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Non_phonetic_writing
    success_url = reverse_lazy("non_phonetic_writings")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Non_phonetic_writingListView(ListView):
    """
    Paginated view for listing all the Non_phonetic_writing objects.
    """

    model = Non_phonetic_writing
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("non_phonetic_writings")

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
            },
        )

        return context


class Non_phonetic_writingListAllView(ListView):
    """ """

    model = Non_phonetic_writing
    template_name = (
        "sc/non_phonetic_writing/non_phonetic_writing_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("non_phonetic_writings_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Non_phonetic_writing.objects.all().order_by(order, order2)

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


class Non_phonetic_writingDetailView(DetailView):
    """ """

    model = Non_phonetic_writing
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_detail.html"


class Phonetic_alphabetic_writingCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Phonetic_alphabetic_writing
    form_class = Phonetic_alphabetic_writingForm
    template_name = (
        "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("phonetic_alphabetic_writing-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Phonetic_alphabetic_writingUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Phonetic_alphabetic_writing
    form_class = Phonetic_alphabetic_writingForm
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_update.html"
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


class Phonetic_alphabetic_writingDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Phonetic_alphabetic_writing object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Phonetic_alphabetic_writing
    success_url = reverse_lazy("phonetic_alphabetic_writings")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Phonetic_alphabetic_writingListView(ListView):
    """
    Paginated view for listing all the Phonetic_alphabetic_writing objects.
    """

    model = Phonetic_alphabetic_writing
    template_name = (
        "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("phonetic_alphabetic_writings")

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
            },
        )

        return context


class Phonetic_alphabetic_writingListAllView(ListView):
    """ """

    model = Phonetic_alphabetic_writing
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("phonetic_alphabetic_writings_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Phonetic_alphabetic_writing.objects.all().order_by(
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
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Phonetic_alphabetic_writingDetailView(DetailView):
    """ """

    model = Phonetic_alphabetic_writing
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_detail.html"


class Lists_tables_and_classificationCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Lists_tables_and_classification
    form_class = Lists_tables_and_classificationForm
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("lists_tables_and_classification-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Lists_tables_and_classificationUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Lists_tables_and_classification
    form_class = Lists_tables_and_classificationForm
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_update.html"  # noqa: E501 pylint: disable=C0301
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


class Lists_tables_and_classificationDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """
    View for deleting an existing Lists_tables_and_classification object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Lists_tables_and_classification
    success_url = reverse_lazy("lists_tables_and_classifications")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Lists_tables_and_classificationListView(ListView):
    """
    Paginated view for listing all the Lists_tables_and_classification objects.
    """

    model = Lists_tables_and_classification
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("lists_tables_and_classifications")

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
            },
        )

        return context


class Lists_tables_and_classificationListAllView(ListView):
    """ """

    model = Lists_tables_and_classification
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("lists_tables_and_classifications_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Lists_tables_and_classification.objects.all().order_by(
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
                "var_section": self.model.Code.section,
                "var_subsection": self.model.Code.subsection,
                "inner_vars": self.model.Code.inner_variables,
                "potential_cols": self.model.Code.potential_cols,
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Lists_tables_and_classificationDetailView(DetailView):
    """ """

    model = Lists_tables_and_classification
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_detail.html"  # noqa: E501 pylint: disable=C0301


class CalendarCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Calendar
    form_class = CalendarForm
    template_name = "sc/calendar/calendar_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("calendar-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class CalendarUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Calendar
    form_class = CalendarForm
    template_name = "sc/calendar/calendar_update.html"
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


class CalendarDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Calendar object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Calendar
    success_url = reverse_lazy("calendars")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CalendarListView(ListView):
    """
    Paginated view for listing all the Calendar objects.
    """

    model = Calendar
    template_name = "sc/calendar/calendar_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("calendars")

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
            },
        )

        return context


class CalendarListAllView(ListView):
    """ """

    model = Calendar
    template_name = "sc/calendar/calendar_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("calendars_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Calendar.objects.all().order_by(order, order2)

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


class CalendarDetailView(DetailView):
    """ """

    model = Calendar
    template_name = "sc/calendar/calendar_detail.html"


class Sacred_textCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sacred_text
    form_class = Sacred_textForm
    template_name = "sc/sacred_text/sacred_text_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sacred_text-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Sacred_textUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sacred_text
    form_class = Sacred_textForm
    template_name = "sc/sacred_text/sacred_text_update.html"
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


class Sacred_textDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Sacred_text object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sacred_text
    success_url = reverse_lazy("sacred_texts")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Sacred_textListView(ListView):
    """
    Paginated view for listing all the Sacred_text objects.
    """

    model = Sacred_text
    template_name = "sc/sacred_text/sacred_text_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sacred_texts")

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
            },
        )

        return context


class Sacred_textListAllView(ListView):
    """ """

    model = Sacred_text
    template_name = "sc/sacred_text/sacred_text_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sacred_texts_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Sacred_text.objects.all().order_by(order, order2)

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


class Sacred_textDetailView(DetailView):
    """ """

    model = Sacred_text
    template_name = "sc/sacred_text/sacred_text_detail.html"


class Religious_literatureCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Religious_literature
    form_class = Religious_literatureForm
    template_name = "sc/religious_literature/religious_literature_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("religious_literature-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Religious_literatureUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Religious_literature
    form_class = Religious_literatureForm
    template_name = "sc/religious_literature/religious_literature_update.html"
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


class Religious_literatureDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Religious_literature object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Religious_literature
    success_url = reverse_lazy("religious_literatures")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Religious_literatureListView(ListView):
    """
    Paginated view for listing all the Religious_literature objects.
    """

    model = Religious_literature
    template_name = "sc/religious_literature/religious_literature_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("religious_literatures")

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
            },
        )

        return context


class Religious_literatureListAllView(ListView):
    """ """

    model = Religious_literature
    template_name = (
        "sc/religious_literature/religious_literature_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("religious_literatures_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Religious_literature.objects.all().order_by(order, order2)

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


class Religious_literatureDetailView(DetailView):
    """ """

    model = Religious_literature
    template_name = "sc/religious_literature/religious_literature_detail.html"


class Practical_literatureCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Practical_literature
    form_class = Practical_literatureForm
    template_name = "sc/practical_literature/practical_literature_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("practical_literature-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Practical_literatureUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Practical_literature
    form_class = Practical_literatureForm
    template_name = "sc/practical_literature/practical_literature_update.html"
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


class Practical_literatureDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Practical_literature object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Practical_literature
    success_url = reverse_lazy("practical_literatures")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Practical_literatureListView(ListView):
    """
    Paginated view for listing all the Practical_literature objects.
    """

    model = Practical_literature
    template_name = "sc/practical_literature/practical_literature_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("practical_literatures")

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
            },
        )

        return context


class Practical_literatureListAllView(ListView):
    """ """

    model = Practical_literature
    template_name = (
        "sc/practical_literature/practical_literature_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("practical_literatures_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Practical_literature.objects.all().order_by(order, order2)

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


class Practical_literatureDetailView(DetailView):
    """ """

    model = Practical_literature
    template_name = "sc/practical_literature/practical_literature_detail.html"


class HistoryCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = History
    form_class = HistoryForm
    template_name = "sc/history/history_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("history-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class HistoryUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = History
    form_class = HistoryForm
    template_name = "sc/history/history_update.html"
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


class HistoryDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing History object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = History
    success_url = reverse_lazy("historys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class HistoryListView(ListView):
    """
    Paginated view for listing all the History objects.
    """

    model = History
    template_name = "sc/history/history_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("historys")

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
            },
        )

        return context


class HistoryListAllView(ListView):
    """ """

    model = History
    template_name = "sc/history/history_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("historys_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return History.objects.all().order_by(order, order2)

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


class HistoryDetailView(DetailView):
    """ """

    model = History
    template_name = "sc/history/history_detail.html"


class PhilosophyCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Philosophy
    form_class = PhilosophyForm
    template_name = "sc/philosophy/philosophy_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("philosophy-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class PhilosophyUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Philosophy
    form_class = PhilosophyForm
    template_name = "sc/philosophy/philosophy_update.html"
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


class PhilosophyDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Philosophy object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Philosophy
    success_url = reverse_lazy("philosophys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class PhilosophyListView(ListView):
    """
    Paginated view for listing all the Philosophy objects.
    """

    model = Philosophy
    template_name = "sc/philosophy/philosophy_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("philosophys")

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
            },
        )

        return context


class PhilosophyListAllView(ListView):
    """ """

    model = Philosophy
    template_name = "sc/philosophy/philosophy_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("philosophys_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Philosophy.objects.all().order_by(order, order2)

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


class PhilosophyDetailView(DetailView):
    """ """

    model = Philosophy
    template_name = "sc/philosophy/philosophy_detail.html"


class Scientific_literatureCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Scientific_literature
    form_class = Scientific_literatureForm
    template_name = "sc/scientific_literature/scientific_literature_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scientific_literature-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Scientific_literatureUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Scientific_literature
    form_class = Scientific_literatureForm
    template_name = (
        "sc/scientific_literature/scientific_literature_update.html"
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


class Scientific_literatureDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Scientific_literature object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Scientific_literature
    success_url = reverse_lazy("scientific_literatures")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Scientific_literatureListView(ListView):
    """
    Paginated view for listing all the Scientific_literature objects.
    """

    model = Scientific_literature
    template_name = "sc/scientific_literature/scientific_literature_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scientific_literatures")

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
            },
        )

        return context


class Scientific_literatureListAllView(ListView):
    """ """

    model = Scientific_literature
    template_name = (
        "sc/scientific_literature/scientific_literature_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scientific_literatures_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Scientific_literature.objects.all().order_by(order, order2)

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


class Scientific_literatureDetailView(DetailView):
    """ """

    model = Scientific_literature
    template_name = (
        "sc/scientific_literature/scientific_literature_detail.html"
    )


class FictionCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Fiction
    form_class = FictionForm
    template_name = "sc/fiction/fiction_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("fiction-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class FictionUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Fiction
    form_class = FictionForm
    template_name = "sc/fiction/fiction_update.html"
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


class FictionDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Fiction object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Fiction
    success_url = reverse_lazy("fictions")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class FictionListView(ListView):
    """
    Paginated view for listing all the Fiction objects.
    """

    model = Fiction
    template_name = "sc/fiction/fiction_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("fictions")

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
            },
        )

        return context


class FictionListAllView(ListView):
    """ """

    model = Fiction
    template_name = "sc/fiction/fiction_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("fictions_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Fiction.objects.all().order_by(order, order2)

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


class FictionDetailView(DetailView):
    """ """

    model = Fiction
    template_name = "sc/fiction/fiction_detail.html"


class ArticleCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Article
    form_class = ArticleForm
    template_name = "sc/article/article_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("article-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Article
    form_class = ArticleForm
    template_name = "sc/article/article_update.html"
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
                "testvar": ["a", "bb", "ccc"],  # TODO: remove?
                "citations_list": Reference.objects.all(),  # TODO: used?
            },
        )

        return context


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Article object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Article
    success_url = reverse_lazy("articles")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class ArticleListView(ListView):
    """
    Paginated view for listing all the Article objects.
    """

    model = Article
    template_name = "sc/article/article_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("articles")

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
            },
        )

        return context


class ArticleListAllView(ListView):
    """ """

    model = Article
    template_name = "sc/article/article_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("articles_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Article.objects.all().order_by(order, order2)

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


class ArticleDetailView(DetailView):
    """ """

    model = Article
    template_name = "sc/article/article_detail.html"


class TokenCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Token
    form_class = TokenForm
    template_name = "sc/token/token_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("token-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class TokenUpdateView(PermissionRequiredMixin, UpdateView):
    """ """

    model = Token
    form_class = TokenForm
    template_name = "sc/token/token_update.html"
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


class TokenDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Token object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Token
    success_url = reverse_lazy("tokens")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class TokenListView(ListView):
    """
    Paginated view for listing all the Token objects.
    """

    model = Token
    template_name = "sc/token/token_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("tokens")

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
            },
        )

        return context


class TokenListAllView(ListView):
    """ """

    model = Token
    template_name = "sc/token/token_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("tokens_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Token.objects.all().order_by(order, order2)

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


class TokenDetailView(DetailView):
    """ """

    model = Token
    template_name = "sc/token/token_detail.html"


class Precious_metalCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Precious_metal
    form_class = Precious_metalForm
    template_name = "sc/precious_metal/precious_metal_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("precious_metal-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Precious_metalUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Precious_metal
    form_class = Precious_metalForm
    template_name = "sc/precious_metal/precious_metal_update.html"
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


class Precious_metalDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Precious_metal object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Precious_metal
    success_url = reverse_lazy("precious_metals")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Precious_metalListView(ListView):
    """
    Paginated view for listing all the Precious_metal objects.
    """

    model = Precious_metal
    template_name = "sc/precious_metal/precious_metal_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("precious_metals")

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
            },
        )

        return context


class Precious_metalListAllView(ListView):
    """ """

    model = Precious_metal
    template_name = "sc/precious_metal/precious_metal_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("precious_metals_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Precious_metal.objects.all().order_by(order, order2)

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


class Precious_metalDetailView(DetailView):
    """ """

    model = Precious_metal
    template_name = "sc/precious_metal/precious_metal_detail.html"


class Foreign_coinCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Foreign_coin
    form_class = Foreign_coinForm
    template_name = "sc/foreign_coin/foreign_coin_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("foreign_coin-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Foreign_coinUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Foreign_coin
    form_class = Foreign_coinForm
    template_name = "sc/foreign_coin/foreign_coin_update.html"
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


class Foreign_coinDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Foreign_coin object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Foreign_coin
    success_url = reverse_lazy("foreign_coins")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Foreign_coinListView(ListView):
    """
    Paginated view for listing all the Foreign_coin objects.
    """

    model = Foreign_coin
    template_name = "sc/foreign_coin/foreign_coin_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("foreign_coins")

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
            },
        )

        return context


class Foreign_coinListAllView(ListView):
    """ """

    model = Foreign_coin
    template_name = "sc/foreign_coin/foreign_coin_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("foreign_coins_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Foreign_coin.objects.all().order_by(order, order2)

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


class Foreign_coinDetailView(DetailView):
    """ """

    model = Foreign_coin
    template_name = "sc/foreign_coin/foreign_coin_detail.html"


class Indigenous_coinCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Indigenous_coin
    form_class = Indigenous_coinForm
    template_name = "sc/indigenous_coin/indigenous_coin_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("indigenous_coin-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Indigenous_coinUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Indigenous_coin
    form_class = Indigenous_coinForm
    template_name = "sc/indigenous_coin/indigenous_coin_update.html"
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


class Indigenous_coinDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Indigenous_coin object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Indigenous_coin
    success_url = reverse_lazy("indigenous_coins")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Indigenous_coinListView(ListView):
    """
    Paginated view for listing all the Indigenous_coin objects.
    """

    model = Indigenous_coin
    template_name = "sc/indigenous_coin/indigenous_coin_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("indigenous_coins")

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
            },
        )

        return context


class Indigenous_coinListAllView(ListView):
    """ """

    model = Indigenous_coin
    template_name = "sc/indigenous_coin/indigenous_coin_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("indigenous_coins_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Indigenous_coin.objects.all().order_by(order, order2)

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


class Indigenous_coinDetailView(DetailView):
    """ """

    model = Indigenous_coin
    template_name = "sc/indigenous_coin/indigenous_coin_detail.html"


class Paper_currencyCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Paper_currency
    form_class = Paper_currencyForm
    template_name = "sc/paper_currency/paper_currency_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("paper_currency-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Paper_currencyUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Paper_currency
    form_class = Paper_currencyForm
    template_name = "sc/paper_currency/paper_currency_update.html"
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


class Paper_currencyDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Paper_currency object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Paper_currency
    success_url = reverse_lazy("paper_currencys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Paper_currencyListView(ListView):
    """
    Paginated view for listing all the Paper_currency objects.
    """

    model = Paper_currency
    template_name = "sc/paper_currency/paper_currency_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("paper_currencys")

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
            },
        )

        return context


class Paper_currencyListAllView(ListView):
    """ """

    model = Paper_currency
    template_name = "sc/paper_currency/paper_currency_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("paper_currencys_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Paper_currency.objects.all().order_by(order, order2)

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


class Paper_currencyDetailView(DetailView):
    """ """

    model = Paper_currency
    template_name = "sc/paper_currency/paper_currency_detail.html"


class CourierCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Courier
    form_class = CourierForm
    template_name = "sc/courier/courier_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("courier-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class CourierUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Courier
    form_class = CourierForm
    template_name = "sc/courier/courier_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": self.model.Code.variable,
            },
        )

        return context


class CourierDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Courier object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Courier
    success_url = reverse_lazy("couriers")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CourierListView(ListView):
    """
    Paginated view for listing all the Courier objects.
    """

    model = Courier
    template_name = "sc/courier/courier_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("couriers")

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
            },
        )

        return context


class CourierListAllView(ListView):
    """ """

    model = Courier
    template_name = "sc/courier/courier_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("couriers_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Courier.objects.all().order_by(order, order2)

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


class CourierDetailView(DetailView):
    """ """

    model = Courier
    template_name = "sc/courier/courier_detail.html"


class Postal_stationCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Postal_station
    form_class = Postal_stationForm
    template_name = "sc/postal_station/postal_station_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("postal_station-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class Postal_stationUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Postal_station
    form_class = Postal_stationForm
    template_name = "sc/postal_station/postal_station_update.html"
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


class Postal_stationDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Postal_station object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Postal_station
    success_url = reverse_lazy("postal_stations")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Postal_stationListView(ListView):
    """
    Paginated view for listing all the Postal_station objects.
    """

    model = Postal_station
    template_name = "sc/postal_station/postal_station_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("postal_stations")

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
            },
        )

        return context


class Postal_stationListAllView(ListView):
    """ """

    model = Postal_station
    template_name = "sc/postal_station/postal_station_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("postal_stations_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return Postal_station.objects.all().order_by(order, order2)

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


class Postal_stationDetailView(DetailView):
    """ """

    model = Postal_station
    template_name = "sc/postal_station/postal_station_detail.html"


class General_postal_serviceCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = General_postal_service
    form_class = General_postal_serviceForm
    template_name = (
        "sc/general_postal_service/general_postal_service_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("general_postal_service-create")

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

        context = dict(context, **{
            "mysection": self.model.Code.section,
            "mysubsection": self.model.Code.subsection,
            "myvar": self.model.Code.variable,
            "my_exp": self.model.Code.description,
            "var_null_meaning": self.model.Code.null_meaning,
            "inner_vars": self.model.Code.inner_variables,
            "potential_cols": self.model.Code.potential_cols,
        })

        # TODO: What are section/subsection and why are they different on the view contexts
        # compared to the model Code attributes?
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"

        return context


class General_postal_serviceUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = General_postal_service
    form_class = General_postal_serviceForm
    template_name = (
        "sc/general_postal_service/general_postal_service_update.html"
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


class General_postal_serviceDeleteView(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing General_postal_service object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = General_postal_service
    success_url = reverse_lazy("general_postal_services")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class General_postal_serviceListView(ListView):
    """
    Paginated view for listing all the General_postal_service objects.
    """

    model = General_postal_service
    template_name = (
        "sc/general_postal_service/general_postal_service_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("general_postal_services")

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
            },
        )

        return context


class General_postal_serviceListAllView(ListView):
    """ """

    model = General_postal_service
    template_name = (
        "sc/general_postal_service/general_postal_service_list_all.html"
    )

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("general_postal_services_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "year_from")
        order2 = self.request.GET.get("orderby2", "year_to")

        return General_postal_service.objects.all().order_by(order, order2)

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


class General_postal_serviceDetailView(DetailView):
    """ """

    model = General_postal_service
    template_name = (
        "sc/general_postal_service/general_postal_service_detail.html"
    )


def scvars_view(request):
    context = get_variable_context(app_name=APP_NAME)
    return render(request, "sc/scvars.html", context=context)


@permission_required("core.view_capital")
def show_problematic_sc_data_table(request):
    """
    View that shows a table of problematic data in the SC app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the rendered problematic data table.
    """
    # Get the context data for the problematic data (with standard conditions)
    context = get_problematic_data_context(APP_NAME)

    # Render the template with the data
    return render(request, "sc/problematic_sc_data_table.html", context)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def dynamic_update_view(
    request,
    object_id,
    form_class,
    model_class,
    x_name,
    myvar,
    my_exp,
    var_section,
    var_subsection,
    delete_url_name,
):
    # Retrieve the object based on the object_id
    my_object = model_class.objects.get(id=object_id)

    if x_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        x_name_with_from = x_name + "_from"
        x_name_with_to = x_name + "_to"
    else:
        x_name_with_from = x_name
        x_name_with_to = None

    if request.method == "POST":
        # Bind the form to the POST data
        my_form = form_class(request.POST, instance=my_object)

        if my_form.is_valid():
            # Save the changes to the object
            my_form.save()
            return redirect(f"{x_name}-detail", pk=my_object.id)

    elif request.method == "GET":
        # Create an instance of the form and populate it with the object's data
        my_form = form_class(instance=my_object)

        if x_name in [
            "largest_communication_distance",
            "fastest_individual_communication",
            "military_level",
        ]:
            context = {
                "form": my_form,
                "object": my_object,
                "delete_url": delete_url_name,
                "extra_var": my_form[x_name_with_from],
                "extra_var2": my_form[x_name_with_to],
                "myvar": myvar,
                "var_section": var_section,
                "var_subsection": var_subsection,
                "my_exp": my_exp,
            }
        else:
            context = {
                "form": my_form,
                "object": my_object,
                "delete_url": delete_url_name,
                "extra_var": my_form[x_name],
                "myvar": myvar,
                "var_section": var_section,
                "var_subsection": var_subsection,
                "my_exp": my_exp,
            }

    return render(request, "sc/sc_update.html", context)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def dynamic_detail_view(request, pk, model_class, myvar, var_name_display):
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    context = {
        "object": obj,
        "myvar": myvar,
        "var_name_display": var_name_display,
        "create_new_url": myvar + "-create",
        "see_all_url": myvar + "s_all",
    }

    return render(request, "sc/sc_detail.html", context)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def dynamic_create_view(
    request, form_class, x_name, myvar, my_exp, var_section, var_subsection
):
    # Retrieve the object based on the object_id
    if x_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        x_name_with_from = x_name + "_from"
        x_name_with_to = x_name + "_to"
    else:
        x_name_with_from = x_name
        x_name_with_to = None

    if request.method == "POST":
        # If the request method is POST, it means the form has been submitted
        my_form = form_class(request.POST)

        if my_form.is_valid():
            # Save the new object to the database
            new_object = my_form.save()
            return redirect(
                f"{x_name}-detail", pk=new_object.id
            )  # Replace 'success_url_name' with your success URL
    elif request.method == "GET":
        my_form = form_class(
            initial={
                "polity": request.GET.get("polity_id_x"),
            }
        )

    if x_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        context = {
            "form": my_form,
            "object": object,
            "extra_var": my_form[x_name_with_from],
            "extra_var2": my_form[x_name_with_to],
            "myvar": myvar,
            "my_exp": my_exp,
            "var_section": var_section,
            "var_subsection": var_subsection,
        }
    else:
        context = {
            "form": my_form,
            "object": object,
            "extra_var": my_form[x_name],
            "myvar": myvar,
            "my_exp": my_exp,
            "var_section": var_section,
            "var_subsection": var_subsection,
        }

    return render(request, "sc/sc_create.html", context)


def generic_list_view(
    request,
    model_class,
    var_name,
    var_name_display,
    var_section,
    var_subsection,
    var_main_desc,
):
    # Retrieve a list of objects from the database (you can customize this query)
    object_list = model_class.objects.all()

    # Create a dictionary with the object IDs as keys and the show_value()
    # method as values
    extra_var_dict = {obj.id: obj.show_value() for obj in object_list}

    orderby = request.GET.get("orderby", None)

    # Apply sorting if orderby is provided and is a valid field name
    if orderby and hasattr(model_class, orderby):
        object_list = object_list.order_by(orderby)

    if var_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        var_name_with_from = var_name + "_from"
        var_exp_new = f'The range of "{var_name_display}" for a polity.'
    else:
        var_name_with_from = var_name
        var_exp_new = (
            f'The absence or presence of "{var_name_display}" for a polity.'
        )

    context = {
        "object_list": object_list,
        "var_name": var_name,
        "create_url": f"{var_name}-create",
        "update_url": f"{var_name}-update",
        "download_url": f"{var_name}-download",
        "pagination_url": f"{var_name}s",
        "metadownload_url": f"{var_name}-metadownload",
        "list_all_url": f"{var_name}s_all",
        "var_name_display": var_name_display,
        "ordering_tag": f"?orderby={var_name_with_from}",
        "var_section": var_section,
        "var_subsection": var_subsection,
        "var_main_desc": var_main_desc,
        "myvar": var_name_display,
        "extra_var_dict": extra_var_dict,
        "inner_vars": {
            var_name_display: {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": var_exp_new,
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
    }

    return render(request, "sc/sc_list_all.html", context)


def confirm_delete_view(request, model_class, pk, var_name):
    check_permissions(request)

    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    context = {
        "var_name": var_name,
        "obj": obj,
        "delete_object": f"{var_name}-delete",
    }

    return render(request, "core/confirm_delete.html", context)


def delete_object_view(request, model_class, pk, var_name):
    check_permissions(request)

    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    # Delete the object
    obj.delete()

    # Redirect to the success URL
    success_url_name = f"{var_name}s_all"
    success_url = reverse(success_url_name)

    # Display a success message
    messages.success(request, f"{var_name} has been deleted successfully.")

    return redirect(success_url)
