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
from django_filters import rest_framework as django_filters
from ._mixins import SeshatCommonFilter


class USLocationFilter(django_filters.FilterSet):
    class Meta:
        model = Us_location
        fields = {
            "city": ["exact", "icontains"],
            "county": ["exact", "icontains"],
            "special_place": ["exact", "icontains"],
            "us_state": ["exact", "icontains"],
            "attention_tag": ["exact", "icontains"],
        }


class USViolenceSubtypeFilter(django_filters.FilterSet):
    class Meta:
        model = Us_violence_subtype
        fields = {
            "name": ["exact", "icontains"],
            "is_uncertain": ["exact"],
        }


class USViolenceDataSourceFilter(django_filters.FilterSet):
    class Meta:
        model = Us_violence_data_source
        fields = {
            "name": ["exact", "icontains"],
            "abbreviation": ["exact", "icontains"],
            "url_address": ["exact", "icontains"],
            "is_uncertain": ["exact"],
            "attention_tag": ["exact", "icontains"],
        }


class USViolenceFilter(django_filters.FilterSet):
    # <>+ violence_subtype
    # <> location
    # <> short_data_source
    class Meta:
        model = Us_violence
        fields = {
            "violence_date": [
                "range",
                # "date__lte",
                # "date__gte",
                # "date__exact",
            ],
            "violence_type": ["exact", "icontains"],
            "fatalities": ["range", "exact", "lte", "gte"],
            "url_address": ["exact", "icontains"],
            "source_details": ["icontains"],
            "narrative": ["icontains"],
        }


class CrisisConsequenceFilter(SeshatCommonFilter, django_filters.FilterSet):
    # other_polity
    class Meta:
        model = Crisis_consequence
        fields = {
            "crisis_case_id": ["exact", "icontains"],
            "is_first_100": ["exact"],
            "name": ["exact", "icontains"],
            "decline": ["exact", "icontains"],
            "collapse": ["exact", "icontains"],
            "epidemic": ["exact", "icontains"],
            "downward_mobility": ["exact", "icontains"],
            "extermination": ["exact", "icontains"],
            "uprising": ["exact", "icontains"],
            "revolution": ["exact", "icontains"],
            "successful_revolution": ["exact", "icontains"],
            "civil_war": ["exact", "icontains"],
            "century_plus": ["exact", "icontains"],
            "fragmentation": ["exact", "icontains"],
            "capital": ["exact", "icontains"],
            "conquest": ["exact", "icontains"],
            "assassination": ["exact", "icontains"],
            "depose": ["exact", "icontains"],
            "constitution": ["exact", "icontains"],
            "labor": ["exact", "icontains"],
            "unfree_labor": ["exact", "icontains"],
            "suffrage": ["exact", "icontains"],
            "public_goods": ["exact", "icontains"],
            "religion": ["exact", "icontains"],
        }


class PowerTransitionFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Power_transition
        fields = {
            "predecessor": ["exact", "icontains"],
            "successor": ["exact", "icontains"],
            "reign_number_predecessor": ["range", "lte", "gte", "exact"],
            "name": ["exact", "icontains"],
            "culture_group": ["exact", "icontains"],
            "contested": ["exact", "icontains"],
            "overturn": ["exact", "icontains"],
            "predecessor_assassination": ["exact", "icontains"],
            "intra_elite": ["exact", "icontains"],
            "military_revolt": ["exact", "icontains"],
            "popular_uprising": ["exact", "icontains"],
            "separatist_rebellion": ["exact", "icontains"],
            "external_invasion": ["exact", "icontains"],
            "external_interference": ["exact", "icontains"],
        }


class HumanSacrificeFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Human_sacrifice
        fields = {
            "name": ["exact", "icontains"],
            "human_sacrifice": ["exact", "icontains"],
        }


class ExternalConflictFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = External_conflict
        fields = {
            "name": ["exact", "icontains"],
            "conflict_name": ["exact", "icontains"],
        }


class InternalConflictFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Internal_conflict
        fields = {
            "name": ["exact", "icontains"],
            "conflict": ["exact", "icontains"],
            "leader": ["exact", "icontains"],
            "casualty": ["range", "lte", "gte", "exact"],
            "expenditure": ["range", "lte", "gte", "exact"],
        }


class ExternalConflictSideFilter(SeshatCommonFilter, django_filters.FilterSet):
    # <> conflict
    class Meta:
        model = External_conflict_side
        fields = {
            "name": ["exact", "icontains"],
            "leader": ["exact", "icontains"],
            "casualty": ["range", "lte", "gte", "exact"],
            "expenditure": ["range", "lte", "gte", "exact"],
        }


class AgriculturalPopulationFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Agricultural_population
        fields = {
            "name": ["exact", "icontains"],
            "agricultural_population": ["range", "lte", "gte", "exact"],
        }


class ArableLandFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Arable_land
        fields = {
            "name": ["exact", "icontains"],
            "arable_land": ["range", "lte", "gte", "exact"],
        }


class ArableLandPerFarmerFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Arable_land_per_farmer
        fields = {
            "name": ["exact", "icontains"],
            "arable_land_per_farmer": ["range", "lte", "gte", "exact"],
        }


class GrossGrainSharedPerAgriculturalPopulationFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Gross_grain_shared_per_agricultural_population
        fields = {
            "name": ["exact", "icontains"],
            "gross_grain_shared_per_agricultural_population": [
                "range",
                "lte",
                "gte",
                "exact",
            ],
        }


class NetGrainSharedPerAgriculturalPopulationFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Net_grain_shared_per_agricultural_population
        fields = {
            "name": ["exact", "icontains"],
            "net_grain_shared_per_agricultural_population": [
                "range",
                "lte",
                "gte",
                "exact",
            ],
        }


class SurplusFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Surplus
        fields = {
            "name": ["exact", "icontains"],
            "surplus": ["range", "lte", "gte", "exact"],
        }


class MilitaryExpenseFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Military_expense
        fields = {
            "name": ["exact", "icontains"],
            "conflict": ["exact", "icontains"],
            "expenditure": ["range", "lte", "gte", "exact"],
        }


class SilverInflowFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Silver_inflow
        fields = {
            "name": ["exact", "icontains"],
            "silver_inflow": ["range", "lte", "gte", "exact"],
        }


class SilverStockFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Silver_stock
        fields = {
            "name": ["exact", "icontains"],
            "silver_stock": ["range", "lte", "gte", "exact"],
        }


class TotalPopulationFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Total_population
        fields = {
            "name": ["exact", "icontains"],
            "total_population": ["range", "lte", "gte", "exact"],
        }


class GDPPerCapitaFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gdp_per_capita
        fields = {
            "name": ["exact", "icontains"],
            "gdp_per_capita": ["range", "lte", "gte", "exact"],
        }


class DroughtEventFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Drought_event
        fields = {
            "name": ["exact", "icontains"],
            "drought_event": ["range", "lte", "gte", "exact"],
        }


class LocustEventFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Locust_event
        fields = {
            "name": ["exact", "icontains"],
            "locust_event": ["range", "lte", "gte", "exact"],
        }


class SocioeconomicTurmoilEventFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Socioeconomic_turmoil_event
        fields = {
            "name": ["exact", "icontains"],
            "socioeconomic_turmoil_event": ["range", "lte", "gte", "exact"],
        }


class CropFailureEventFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Crop_failure_event
        fields = {
            "name": ["exact", "icontains"],
            "crop_failure_event": ["range", "lte", "gte", "exact"],
        }


class FamineEventFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Famine_event
        fields = {
            "name": ["exact", "icontains"],
            "famine_event": ["range", "lte", "gte", "exact"],
        }


class DiseaseOutbreakFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Disease_outbreak
        fields = {
            "name": ["exact", "icontains"],
            "latitude": ["range", "lte", "gte", "exact"],
            "longitude": ["range", "lte", "gte", "exact"],
            "elevation": ["range", "lte", "gte", "exact"],
            "sub_category": ["exact", "icontains"],
            "magnitude": ["icontains", "exact"],
            "duration": ["icontains", "exact"],
        }
