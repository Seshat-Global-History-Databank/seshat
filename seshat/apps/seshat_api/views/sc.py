from rest_framework import viewsets

from ._permissions import ONLY_ADMIN_PERMISSIONS

from ._mixins import (
    FilterBackends,
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)

from ..filters.sc import (
    RAFilter,
    PolityTerritoryFilter,
    PolityPopulationFilter,
    PopulationOfTheLargestSettlementFilter,
    SettlementHierarchyFilter,
    AdministrativeLevelFilter,
    ReligiousLevelFilter,
    MilitaryLevelFilter,
    ProfessionalMilitaryOfficerFilter,
    ProfessionalSoldierFilter,
    ProfessionalPriesthoodFilter,
    FullTimeBureaucratFilter,
    ExaminationSystemFilter,
    MeritPromotionFilter,
    SpecializedGovernmentBuildingFilter,
    FormalLegalCodeFilter,
    JudgeFilter,
    CourtFilter,
    ProfessionalLawyerFilter,
    IrrigationSystemFilter,
    DrinkingWaterSupplySystemFilter,
    MarketFilter,
    FoodStorageSiteFilter,
    RoadFilter,
    BridgeFilter,
    CanalFilter,
    PortFilter,
    MinesOrQuarryFilter,
    MnemonicDeviceFilter,
    NonwrittenRecordFilter,
    WrittenRecordFilter,
    ScriptFilter,
    NonPhoneticWritingFilter,
    PhoneticAlphabeticWritingFilter,
    ListsTablesAndClassificationFilter,
    CalendarFilter,
    SacredTextFilter,
    ReligiousLiteratureFilter,
    PracticalLiteratureFilter,
    HistoryFilter,
    PhilosophyFilter,
    ScientificLiteratureFilter,
    FictionFilter,
    ArticleFilter,
    TokenFilter,
    PreciousMetalFilter,
    ForeignCoinFilter,
    IndigenousCoinFilter,
    PaperCurrencyFilter,
    CourierFilter,
    PostalStationFilter,
    GeneralPostalServiceFilter,
    CommunalBuildingFilter,
    UtilitarianPublicBuildingFilter,
    SymbolicBuildingFilter,
    EntertainmentBuildingFilter,
    KnowledgeOrInformationBuildingFilter,
    OtherUtilitarianPublicBuildingFilter,
    SpecialPurposeSiteFilter,
    CeremonialSiteFilter,
    BurialSiteFilter,
    TradingEmporiaFilter,
    EnclosureFilter,
    LengthMeasurementSystemFilter,
    AreaMeasurementSystemFilter,
    VolumeMeasurementSystemFilter,
    WeightMeasurementSystemFilter,
    TimeMeasurementSystemFilter,
    GeometricalMeasurementSystemFilter,
    OtherMeasurementSystemFilter,
    DebtAndCreditStructureFilter,
    StoreOfWealthFilter,
    SourceOfSupportFilter,
    OccupationalComplexityFilter,
    SpecialPurposeHouseFilter,
    OtherSpecialPurposeSiteFilter,
    LargestCommunicationDistanceFilter,
    FastestIndividualCommunicationFilter,
)

from ..models import (
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
    Communal_building,
    Utilitarian_public_building,
    Symbolic_building,
    Entertainment_building,
    Knowledge_or_information_building,
    Other_utilitarian_public_building,
    Special_purpose_site,
    Ceremonial_site,
    Burial_site,
    Trading_emporia,
    Enclosure,
    Length_measurement_system,
    Area_measurement_system,
    Volume_measurement_system,
    Weight_measurement_system,
    Time_measurement_system,
    Geometrical_measurement_system,
    Other_measurement_system,
    Debt_and_credit_structure,
    Store_of_wealth,
    Source_of_support,
    Occupational_complexity,
    Special_purpose_house,
    Other_special_purpose_site,
    Largest_communication_distance,
    Fastest_individual_communication,
)


class RAViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing RAs.
    """

    model = Ra
    pagination_class = SeshatAPIPagination
    filterset_class = RAFilter
    permissions_dict = ONLY_ADMIN_PERMISSIONS


class PolityTerritoryViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Territories.
    """

    model = Polity_territory
    pagination_class = SeshatAPIPagination
    filterset_class = PolityTerritoryFilter


class PolityPopulationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Populations.
    """

    model = Polity_population
    pagination_class = SeshatAPIPagination
    filterset_class = PolityPopulationFilter


class PopulationOfTheLargestSettlementViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Population of the Largest Settlements.
    """

    model = Population_of_the_largest_settlement
    pagination_class = SeshatAPIPagination
    filterset_class = PopulationOfTheLargestSettlementFilter


class SettlementHierarchyViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Settlement Hierarchies.
    """

    model = Settlement_hierarchy
    pagination_class = SeshatAPIPagination
    filterset_class = SettlementHierarchyFilter


class AdministrativeLevelViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Administrative Levels.
    """

    model = Administrative_level
    pagination_class = SeshatAPIPagination
    filterset_class = AdministrativeLevelFilter


class ReligiousLevelViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Religious Levels.
    """

    model = Religious_level
    pagination_class = SeshatAPIPagination
    filterset_class = ReligiousLevelFilter


class MilitaryLevelViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Military Levels.
    """

    model = Military_level
    pagination_class = SeshatAPIPagination
    filterset_class = MilitaryLevelFilter


class ProfessionalMilitaryOfficerViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Professional Military Officers.
    """

    model = Professional_military_officer
    pagination_class = SeshatAPIPagination
    filterset_class = ProfessionalMilitaryOfficerFilter


class ProfessionalSoldierViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Professional Soldiers.
    """

    model = Professional_soldier
    pagination_class = SeshatAPIPagination
    filterset_class = ProfessionalSoldierFilter


class ProfessionalPriesthoodViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Professional Priesthoods.
    """

    model = Professional_priesthood
    pagination_class = SeshatAPIPagination
    filterset_class = ProfessionalPriesthoodFilter


class FullTimeBureaucratViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Full Time Bureaucrats.
    """

    model = Full_time_bureaucrat
    pagination_class = SeshatAPIPagination
    filterset_class = FullTimeBureaucratFilter


class ExaminationSystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Examination Systems.
    """

    model = Examination_system
    pagination_class = SeshatAPIPagination
    filterset_class = ExaminationSystemFilter


class MeritPromotionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Merit Promotions.
    """

    model = Merit_promotion
    pagination_class = SeshatAPIPagination
    filterset_class = MeritPromotionFilter


class SpecializedGovernmentBuildingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Specialized Government Buildings.
    """

    model = Specialized_government_building
    pagination_class = SeshatAPIPagination
    filterset_class = SpecializedGovernmentBuildingFilter


class FormalLegalCodeViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Formal Legal Codes.
    """

    model = Formal_legal_code
    pagination_class = SeshatAPIPagination
    filterset_class = FormalLegalCodeFilter


class JudgeViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Judges.
    """

    model = Judge
    pagination_class = SeshatAPIPagination
    filterset_class = JudgeFilter


class CourtViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Courts.
    """

    model = Court
    pagination_class = SeshatAPIPagination
    filterset_class = CourtFilter


class ProfessionalLawyerViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Professional Lawyers.
    """

    model = Professional_lawyer
    pagination_class = SeshatAPIPagination
    filterset_class = ProfessionalLawyerFilter


class IrrigationSystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Irrigation Systems.
    """

    model = Irrigation_system
    pagination_class = SeshatAPIPagination
    filterset_class = IrrigationSystemFilter


class DrinkingWaterSupplySystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Drinking Water Supply Systems.
    """

    model = Drinking_water_supply_system
    pagination_class = SeshatAPIPagination
    filterset_class = DrinkingWaterSupplySystemFilter


class MarketViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Markets.
    """

    model = Market
    pagination_class = SeshatAPIPagination
    filterset_class = MarketFilter


class FoodStorageSiteViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Food Storage Sites.
    """

    model = Food_storage_site
    pagination_class = SeshatAPIPagination
    filterset_class = FoodStorageSiteFilter


class RoadViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Roads.
    """

    model = Road
    pagination_class = SeshatAPIPagination
    filterset_class = RoadFilter


class BridgeViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Bridges.
    """

    model = Bridge
    pagination_class = SeshatAPIPagination
    filterset_class = BridgeFilter


class CanalViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Canals.
    """

    model = Canal
    pagination_class = SeshatAPIPagination
    filterset_class = CanalFilter


class PortViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Ports.
    """

    model = Port
    pagination_class = SeshatAPIPagination
    filterset_class = PortFilter


class MinesOrQuarryViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Mines or Quarries.
    """

    model = Mines_or_quarry
    pagination_class = SeshatAPIPagination
    filterset_class = MinesOrQuarryFilter


class MnemonicDeviceViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Mnemonic Devices.
    """

    model = Mnemonic_device
    pagination_class = SeshatAPIPagination
    filterset_class = MnemonicDeviceFilter


class NonwrittenRecordViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Nonwritten Records.
    """

    model = Nonwritten_record
    pagination_class = SeshatAPIPagination
    filterset_class = NonwrittenRecordFilter


class WrittenRecordViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Written Records.
    """

    model = Written_record
    pagination_class = SeshatAPIPagination
    filterset_class = WrittenRecordFilter


class ScriptViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Scripts.
    """

    model = Script
    pagination_class = SeshatAPIPagination
    filterset_class = ScriptFilter


class NonPhoneticWritingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Non-Phonetic Writings.
    """

    model = Non_phonetic_writing
    pagination_class = SeshatAPIPagination
    filterset_class = NonPhoneticWritingFilter


class PhoneticAlphabeticWritingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Phonetic Alphabetic Writings.
    """

    model = Phonetic_alphabetic_writing
    pagination_class = SeshatAPIPagination
    filterset_class = PhoneticAlphabeticWritingFilter


class ListsTablesAndClassificationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Lists, Tables, and Classifications.
    """

    model = Lists_tables_and_classification
    pagination_class = SeshatAPIPagination
    filterset_class = ListsTablesAndClassificationFilter


class CalendarViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Calendars.
    """

    model = Calendar
    pagination_class = SeshatAPIPagination
    filterset_class = CalendarFilter


class SacredTextViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Sacred Texts.
    """

    model = Sacred_text
    pagination_class = SeshatAPIPagination
    filterset_class = SacredTextFilter


class ReligiousLiteratureViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Religious Literatures.
    """

    model = Religious_literature
    pagination_class = SeshatAPIPagination
    filterset_class = ReligiousLiteratureFilter


class PracticalLiteratureViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Practical Literatures.
    """

    model = Practical_literature
    pagination_class = SeshatAPIPagination
    filterset_class = PracticalLiteratureFilter


class HistoryViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Histories.
    """

    model = History
    pagination_class = SeshatAPIPagination
    filterset_class = HistoryFilter


class PhilosophyViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Philosophies.
    """

    model = Philosophy
    pagination_class = SeshatAPIPagination
    filterset_class = PhilosophyFilter


class ScientificLiteratureViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Scientific Literatures.
    """

    model = Scientific_literature
    pagination_class = SeshatAPIPagination
    filterset_class = ScientificLiteratureFilter


class FictionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Fictions.
    """

    model = Fiction
    pagination_class = SeshatAPIPagination
    filterset_class = FictionFilter


class ArticleViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Articles.
    """

    model = Article
    pagination_class = SeshatAPIPagination
    filterset_class = ArticleFilter


class TokenViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Tokens.
    """

    model = Token
    pagination_class = SeshatAPIPagination
    filterset_class = TokenFilter


class PreciousMetalViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Precious Metals.
    """

    model = Precious_metal
    pagination_class = SeshatAPIPagination
    filterset_class = PreciousMetalFilter


class ForeignCoinViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Foreign Coins.
    """

    model = Foreign_coin
    pagination_class = SeshatAPIPagination
    filterset_class = ForeignCoinFilter


class IndigenousCoinViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Indigenous Coins.
    """

    model = Indigenous_coin
    pagination_class = SeshatAPIPagination
    filterset_class = IndigenousCoinFilter


class PaperCurrencyViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Paper Currencies.
    """

    model = Paper_currency
    pagination_class = SeshatAPIPagination
    filterset_class = PaperCurrencyFilter


class CourierViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Couriers.
    """

    model = Courier
    pagination_class = SeshatAPIPagination
    filterset_class = CourierFilter


class PostalStationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Postal Stations.
    """

    model = Postal_station
    pagination_class = SeshatAPIPagination
    filterset_class = PostalStationFilter


class GeneralPostalServiceViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing General Postal Services.
    """

    model = General_postal_service
    pagination_class = SeshatAPIPagination
    filterset_class = GeneralPostalServiceFilter


class CommunalBuildingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Communal Buildings.
    """

    model = Communal_building
    pagination_class = SeshatAPIPagination
    filterset_class = CommunalBuildingFilter


class UtilitarianPublicBuildingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Utilitarian Public Buildings.
    """

    model = Utilitarian_public_building
    pagination_class = SeshatAPIPagination
    filterset_class = UtilitarianPublicBuildingFilter


class SymbolicBuildingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Symbolic Buildings.
    """

    model = Symbolic_building
    pagination_class = SeshatAPIPagination
    filterset_class = SymbolicBuildingFilter


class EntertainmentBuildingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Entertainment Buildings.
    """

    model = Entertainment_building
    pagination_class = SeshatAPIPagination
    filterset_class = EntertainmentBuildingFilter


class KnowledgeOrInformationBuildingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Knowledge or Information Buildings.
    """

    model = Knowledge_or_information_building
    pagination_class = SeshatAPIPagination
    filterset_class = KnowledgeOrInformationBuildingFilter


class OtherUtilitarianPublicBuildingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Other Utilitarian Public Buildings.
    """

    model = Other_utilitarian_public_building
    pagination_class = SeshatAPIPagination
    filterset_class = OtherUtilitarianPublicBuildingFilter


class SpecialPurposeSiteViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Special Purpose Sites.
    """

    model = Special_purpose_site
    pagination_class = SeshatAPIPagination
    filterset_class = SpecialPurposeSiteFilter


class CeremonialSiteViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Ceremonial Sites.
    """

    model = Ceremonial_site
    pagination_class = SeshatAPIPagination
    filterset_class = CeremonialSiteFilter


class BurialSiteViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Burial Sites.
    """

    model = Burial_site
    pagination_class = SeshatAPIPagination
    filterset_class = BurialSiteFilter


class TradingEmporiaViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Trading Emporias.
    """

    model = Trading_emporia
    pagination_class = SeshatAPIPagination
    filterset_class = TradingEmporiaFilter


class EnclosureViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Enclosures.
    """

    model = Enclosure
    pagination_class = SeshatAPIPagination
    filterset_class = EnclosureFilter


class LengthMeasurementSystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Length Measurement Systems.
    """

    model = Length_measurement_system
    pagination_class = SeshatAPIPagination
    filterset_class = LengthMeasurementSystemFilter


class AreaMeasurementSystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Area Measurement Systems.
    """

    model = Area_measurement_system
    pagination_class = SeshatAPIPagination
    filterset_class = AreaMeasurementSystemFilter


class VolumeMeasurementSystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Volume Measurement Systems.
    """

    model = Volume_measurement_system
    pagination_class = SeshatAPIPagination
    filterset_class = VolumeMeasurementSystemFilter


class WeightMeasurementSystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Weight Measurement Systems.
    """

    model = Weight_measurement_system
    pagination_class = SeshatAPIPagination
    filterset_class = WeightMeasurementSystemFilter


class TimeMeasurementSystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Time Measurement Systems.
    """

    model = Time_measurement_system
    pagination_class = SeshatAPIPagination
    filterset_class = TimeMeasurementSystemFilter


class GeometricalMeasurementSystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Geometrical Measurement Systems.
    """

    model = Geometrical_measurement_system
    pagination_class = SeshatAPIPagination
    filterset_class = GeometricalMeasurementSystemFilter


class OtherMeasurementSystemViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Other Measurement Systems.
    """

    model = Other_measurement_system
    pagination_class = SeshatAPIPagination
    filterset_class = OtherMeasurementSystemFilter


class DebtAndCreditStructureViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Debt and Credit Structures.
    """

    model = Debt_and_credit_structure
    pagination_class = SeshatAPIPagination
    filterset_class = DebtAndCreditStructureFilter


class StoreOfWealthViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Stores of Wealth.
    """

    model = Store_of_wealth
    pagination_class = SeshatAPIPagination
    filterset_class = StoreOfWealthFilter


class SourceOfSupportViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Sources of Support.
    """

    model = Source_of_support
    pagination_class = SeshatAPIPagination
    filterset_class = SourceOfSupportFilter


class OccupationalComplexityViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Occupational Complexities.
    """

    model = Occupational_complexity
    pagination_class = SeshatAPIPagination
    filterset_class = OccupationalComplexityFilter


class SpecialPurposeHouseViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Special Purpose Houses.
    """

    model = Special_purpose_house
    pagination_class = SeshatAPIPagination
    filterset_class = SpecialPurposeHouseFilter


class OtherSpecialPurposeSiteViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Other Special Purpose Sites.
    """

    model = Other_special_purpose_site
    pagination_class = SeshatAPIPagination
    filterset_class = OtherSpecialPurposeSiteFilter


class LargestCommunicationDistanceViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Largest Communication Distances.
    """

    model = Largest_communication_distance
    pagination_class = SeshatAPIPagination
    filterset_class = LargestCommunicationDistanceFilter


class FastestIndividualCommunicationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Fastest Individual Communications.
    """

    model = Fastest_individual_communication
    pagination_class = SeshatAPIPagination
    filterset_class = FastestIndividualCommunicationFilter
