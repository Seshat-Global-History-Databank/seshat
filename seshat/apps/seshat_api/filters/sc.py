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

from django_filters import rest_framework as django_filters
from ._mixins import SeshatCommonFilter


class RAFilter(SeshatCommonFilter, django_filters.FilterSet):
    # <> sc_ra [Seshat_Expert]

    class Meta:
        model = Ra
        fields = {}


class PolityTerritoryFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_territory
        fields = {
            "polity_territory_from": ["exact", "gte", "lte"],
            "polity_territory_to": ["exact", "gte", "lte"],
        }


class PolityPopulationFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_population
        fields = {
            "polity_population_from": ["exact", "gte", "lte"],
            "polity_population_to": ["exact", "gte", "lte"],
        }


class PopulationOfTheLargestSettlementFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Population_of_the_largest_settlement
        fields = {
            "population_of_the_largest_settlement_from": ["exact", "gte", "lte"],
            "population_of_the_largest_settlement_to": ["exact", "gte", "lte"],
        }


class SettlementHierarchyFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Settlement_hierarchy
        fields = {
            "settlement_hierarchy_from": ["exact", "gte", "lte"],
            "settlement_hierarchy_to": ["exact", "gte", "lte"],
        }


class AdministrativeLevelFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Administrative_level
        fields = {
            "administrative_level_from": ["exact", "gte", "lte"],
            "administrative_level_to": ["exact", "gte", "lte"],
        }


class ReligiousLevelFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Religious_level
        fields = {
            "religious_level_from": ["exact", "gte", "lte"],
            "religious_level_to": ["exact", "gte", "lte"],
        }


class MilitaryLevelFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Military_level
        fields = {
            "military_level_from": ["exact", "gte", "lte"],
            "military_level_to": ["exact", "gte", "lte"],
        }


class ProfessionalMilitaryOfficerFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Professional_military_officer
        fields = {
            "professional_military_officer": ["exact"],
        }


class ProfessionalSoldierFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Professional_soldier
        fields = {
            "professional_soldier": ["exact"],
        }


class ProfessionalPriesthoodFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Professional_priesthood
        fields = {
            "professional_priesthood": ["exact"],
        }


class FullTimeBureaucratFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Full_time_bureaucrat
        fields = {
            "full_time_bureaucrat": ["exact"],
        }


class ExaminationSystemFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Examination_system
        fields = {
            "examination_system": ["exact"],
        }


class MeritPromotionFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Merit_promotion
        fields = {
            "merit_promotion": ["exact"],
        }


class SpecializedGovernmentBuildingFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Specialized_government_building
        fields = {
            "specialized_government_building": ["exact"],
        }


class FormalLegalCodeFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Formal_legal_code
        fields = {
            "formal_legal_code": ["exact"],
        }


class JudgeFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Judge
        fields = {
            "judge": ["exact"],
        }


class CourtFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Court
        fields = {
            "court": ["exact"],
        }


class ProfessionalLawyerFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Professional_lawyer
        fields = {
            "professional_lawyer": ["exact"],
        }


class IrrigationSystemFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Irrigation_system
        fields = {
            "irrigation_system": ["exact"],
        }


class DrinkingWaterSupplySystemFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Drinking_water_supply_system
        fields = {
            "drinking_water_supply_system": ["exact"],
        }


class MarketFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Market
        fields = {
            "market": ["exact"],
        }


class FoodStorageSiteFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Food_storage_site
        fields = {
            "food_storage_site": ["exact"],
        }


class RoadFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Road
        fields = {
            "road": ["exact"],
        }


class BridgeFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Bridge
        fields = {
            "bridge": ["exact"],
        }


class CanalFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Canal
        fields = {
            "canal": ["exact"],
        }


class PortFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Port
        fields = {
            "port": ["exact"],
        }


class MinesOrQuarryFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Mines_or_quarry
        fields = {
            "mines_or_quarry": ["exact"],
        }


class MnemonicDeviceFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Mnemonic_device
        fields = {
            "mnemonic_device": ["exact"],
        }


class NonwrittenRecordFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Nonwritten_record
        fields = {
            "nonwritten_record": ["exact"],
        }


class WrittenRecordFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Written_record
        fields = {
            "written_record": ["exact"],
        }


class ScriptFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Script
        fields = {
            "script": ["exact"],
        }


class NonPhoneticWritingFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Non_phonetic_writing
        fields = {
            "non_phonetic_writing": ["exact"],
        }


class PhoneticAlphabeticWritingFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Phonetic_alphabetic_writing
        fields = {
            "phonetic_alphabetic_writing": ["exact"],
        }


class ListsTablesAndClassificationFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Lists_tables_and_classification
        fields = {
            "lists_tables_and_classification": ["exact"],
        }


class CalendarFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Calendar
        fields = {
            "calendar": ["exact"],
        }


class SacredTextFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Sacred_text
        fields = {
            "sacred_text": ["exact"],
        }


class ReligiousLiteratureFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Religious_literature
        fields = {
            "religious_literature": ["exact"],
        }


class PracticalLiteratureFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Practical_literature
        fields = {
            "practical_literature": ["exact"],
        }


class HistoryFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = History
        fields = {
            "history": ["exact"],
        }


class PhilosophyFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Philosophy
        fields = {
            "philosophy": ["exact"],
        }


class ScientificLiteratureFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Scientific_literature
        fields = {
            "scientific_literature": ["exact"],
        }


class FictionFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Fiction
        fields = {
            "fiction": ["exact"],
        }


class ArticleFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Article
        fields = {
            "article": ["exact"],
        }


class TokenFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Token
        fields = {
            "token": ["exact"],
        }


class PreciousMetalFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Precious_metal
        fields = {
            "precious_metal": ["exact"],
        }


class ForeignCoinFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Foreign_coin
        fields = {
            "foreign_coin": ["exact"],
        }


class IndigenousCoinFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Indigenous_coin
        fields = {
            "indigenous_coin": ["exact"],
        }


class PaperCurrencyFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Paper_currency
        fields = {
            "paper_currency": ["exact"],
        }


class CourierFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Courier
        fields = {
            "courier": ["exact"],
        }


class PostalStationFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Postal_station
        fields = {
            "postal_station": ["exact"],
        }


class GeneralPostalServiceFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = General_postal_service
        fields = {
            "general_postal_service": ["exact"],
        }


class CommunalBuildingFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Communal_building
        fields = {
            "communal_building": ["exact"],
        }


class UtilitarianPublicBuildingFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Utilitarian_public_building
        fields = {
            "utilitarian_public_building": ["exact"],
        }


class SymbolicBuildingFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Symbolic_building
        fields = {
            "symbolic_building": ["exact"],
        }


class EntertainmentBuildingFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Entertainment_building
        fields = {
            "entertainment_building": ["exact"],
        }


class KnowledgeOrInformationBuildingFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Knowledge_or_information_building
        fields = {
            "knowledge_or_information_building": ["exact"],
        }


class OtherUtilitarianPublicBuildingFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Other_utilitarian_public_building
        fields = {
            "other_utilitarian_public_building": ["exact"],
        }


class SpecialPurposeSiteFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Special_purpose_site
        fields = {
            "special_purpose_site": ["exact"],
        }


class CeremonialSiteFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Ceremonial_site
        fields = {
            "ceremonial_site": ["exact"],
        }


class BurialSiteFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Burial_site
        fields = {
            "burial_site": ["exact"],
        }


class TradingEmporiaFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Trading_emporia
        fields = {
            "trading_emporia": ["exact"],
        }


class EnclosureFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Enclosure
        fields = {
            "enclosure": ["exact"],
        }


class LengthMeasurementSystemFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Length_measurement_system
        fields = {
            "length_measurement_system": ["exact"],
        }


class AreaMeasurementSystemFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Area_measurement_system
        fields = {
            "area_measurement_system": ["exact"],
        }


class VolumeMeasurementSystemFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Volume_measurement_system
        fields = {
            "volume_measurement_system": ["exact"],
        }


class WeightMeasurementSystemFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Weight_measurement_system
        fields = {
            "weight_measurement_system": ["exact"],
        }


class TimeMeasurementSystemFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Time_measurement_system
        fields = {
            "time_measurement_system": ["exact"],
        }


class GeometricalMeasurementSystemFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Geometrical_measurement_system
        fields = {
            "geometrical_measurement_system": ["exact"],
        }


class OtherMeasurementSystemFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Other_measurement_system
        fields = {
            "other_measurement_system": ["exact"],
        }


class DebtAndCreditStructureFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Debt_and_credit_structure
        fields = {
            "debt_and_credit_structure": ["exact"],
        }


class StoreOfWealthFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Store_of_wealth
        fields = {
            "store_of_wealth": ["exact"],
        }


class SourceOfSupportFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Source_of_support
        fields = {
            "source_of_support": ["exact"],
        }


class OccupationalComplexityFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Occupational_complexity
        fields = {
            "occupational_complexity": ["exact"],
        }


class SpecialPurposeHouseFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Special_purpose_house
        fields = {
            "special_purpose_house": ["exact"],
        }


class OtherSpecialPurposeSiteFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Other_special_purpose_site
        fields = {
            "other_special_purpose_site": ["exact"],
        }


class LargestCommunicationDistanceFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Largest_communication_distance
        fields = {
            "largest_communication_distance_from": ["exact", "gte", "lte"],
            "largest_communication_distance_to": ["exact", "gte", "lte"],
        }


class FastestIndividualCommunicationFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Fastest_individual_communication
        fields = {
            "fastest_individual_communication_from": ["exact", "gte", "lte"],
            "fastest_individual_communication_to": ["exact", "gte", "lte"],
        }
