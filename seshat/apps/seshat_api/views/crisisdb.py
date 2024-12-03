from rest_framework import viewsets

from ._mixins import (
    FilterBackends,
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)
from ..filters.crisisdb import (
    USLocationFilter,
    USViolenceSubtypeFilter,
    USViolenceDataSourceFilter,
    USViolenceFilter,
    CrisisConsequenceFilter,
    PowerTransitionFilter,
    HumanSacrificeFilter,
    ExternalConflictFilter,
    InternalConflictFilter,
    ExternalConflictSideFilter,
    AgriculturalPopulationFilter,
    ArableLandFilter,
    ArableLandPerFarmerFilter,
    GrossGrainSharedPerAgriculturalPopulationFilter,
    NetGrainSharedPerAgriculturalPopulationFilter,
    SurplusFilter,
    MilitaryExpenseFilter,
    SilverInflowFilter,
    SilverStockFilter,
    TotalPopulationFilter,
    GDPPerCapitaFilter,
    DroughtEventFilter,
    LocustEventFilter,
    SocioeconomicTurmoilEventFilter,
    CropFailureEventFilter,
    FamineEventFilter,
    DiseaseOutbreakFilter,
)

from ..models import (
    Us_location,
    Us_violence_subtype,
    Us_violence_data_source,
    Us_violence,
    Crisis_consequence,
    Power_transition,
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
)


class USLocationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing US Locations.
    """

    model = Us_location
    pagination_class = SeshatAPIPagination
    filterset_class = USLocationFilter


class USViolenceSubtypeViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing US Violence Subtypes.
    """

    model = Us_violence_subtype
    pagination_class = SeshatAPIPagination
    filterset_class = USViolenceSubtypeFilter


class USViolenceDataSourceViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing US Violence Data Sources.
    """

    model = Us_violence_data_source
    pagination_class = SeshatAPIPagination
    filterset_class = USViolenceDataSourceFilter


class USViolenceViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing US Violence.
    """

    model = Us_violence
    pagination_class = SeshatAPIPagination
    filterset_class = USViolenceFilter


class CrisisConsequenceViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Crisis Consequences.
    """

    model = Crisis_consequence
    pagination_class = SeshatAPIPagination
    filterset_class = CrisisConsequenceFilter


class PowerTransitionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Power Transitions.
    """

    model = Power_transition
    pagination_class = SeshatAPIPagination
    filterset_class = PowerTransitionFilter


class HumanSacrificeViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Human Sacrifices.
    """

    model = Human_sacrifice
    pagination_class = SeshatAPIPagination
    filterset_class = HumanSacrificeFilter


class ExternalConflictViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing External Conflicts.
    """

    model = External_conflict
    pagination_class = SeshatAPIPagination
    filterset_class = ExternalConflictFilter


class InternalConflictViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Internal Conflicts.
    """

    model = Internal_conflict
    pagination_class = SeshatAPIPagination
    filterset_class = InternalConflictFilter


class ExternalConflictSideViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing External Conflict Sides.
    """

    model = External_conflict_side
    pagination_class = SeshatAPIPagination
    filterset_class = ExternalConflictSideFilter


class AgriculturalPopulationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Agricultural Populations.
    """

    model = Agricultural_population
    pagination_class = SeshatAPIPagination
    filterset_class = AgriculturalPopulationFilter


class ArableLandViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Arable Lands.
    """

    model = Arable_land
    pagination_class = SeshatAPIPagination
    filterset_class = ArableLandFilter


class ArableLandPerFarmerViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Arable Land Per Farmers.
    """

    model = Arable_land_per_farmer
    pagination_class = SeshatAPIPagination
    filterset_class = ArableLandPerFarmerFilter


class GrossGrainSharedPerAgriculturalPopulationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Gross Grain Shared Per Agricultural Populations.
    """

    model = Gross_grain_shared_per_agricultural_population
    pagination_class = SeshatAPIPagination
    filterset_class = GrossGrainSharedPerAgriculturalPopulationFilter


class NetGrainSharedPerAgriculturalPopulationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Net Grain Shared Per Agricultural Populations.
    """

    model = Net_grain_shared_per_agricultural_population
    pagination_class = SeshatAPIPagination
    filterset_class = NetGrainSharedPerAgriculturalPopulationFilter


class SurplusViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Surpluses.
    """

    model = Surplus
    pagination_class = SeshatAPIPagination
    filterset_class = SurplusFilter


class MilitaryExpenseViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Military Expenses.
    """

    model = Military_expense
    pagination_class = SeshatAPIPagination
    filterset_class = MilitaryExpenseFilter


class SilverInflowViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Silver Inflows.
    """

    model = Silver_inflow
    pagination_class = SeshatAPIPagination
    filterset_class = SilverInflowFilter


class SilverStockViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Silver Stocks.
    """

    model = Silver_stock
    pagination_class = SeshatAPIPagination
    filterset_class = SilverStockFilter


class TotalPopulationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Total Populations.
    """

    model = Total_population
    pagination_class = SeshatAPIPagination
    filterset_class = TotalPopulationFilter


class GDPPerCapitaViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing GDP Per Capitas.
    """

    model = Gdp_per_capita
    pagination_class = SeshatAPIPagination
    filterset_class = GDPPerCapitaFilter


class DroughtEventViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Drought Events.
    """

    model = Drought_event
    pagination_class = SeshatAPIPagination
    filterset_class = DroughtEventFilter


class LocustEventViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Locust Events.
    """

    model = Locust_event
    pagination_class = SeshatAPIPagination
    filterset_class = LocustEventFilter


class SocioeconomicTurmoilEventViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Socioeconomic Turmoil Events.
    """

    model = Socioeconomic_turmoil_event
    pagination_class = SeshatAPIPagination
    filterset_class = SocioeconomicTurmoilEventFilter


class CropFailureEventViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Crop Failure Events.
    """

    model = Crop_failure_event
    pagination_class = SeshatAPIPagination
    filterset_class = CropFailureEventFilter


class FamineEventViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Famine Events.
    """

    model = Famine_event
    pagination_class = SeshatAPIPagination
    filterset_class = FamineEventFilter


class DiseaseOutbreakViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Disease Outbreaks.
    """

    model = Disease_outbreak
    pagination_class = SeshatAPIPagination
    filterset_class = DiseaseOutbreakFilter
