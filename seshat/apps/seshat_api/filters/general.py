from ..models import (
    Polity_research_assistant,
    Polity_original_name,
    Polity_alternative_name,
    Polity_duration,
    Polity_peak_years,
    Polity_degree_of_centralization,
    Polity_suprapolity_relations,
    Polity_utm_zone,
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

from django_filters import rest_framework as django_filters
from ._mixins import SeshatCommonFilter


class PolityResearchAssistantFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    # <> polity_ra
    class Meta:
        model = Polity_research_assistant
        fields = {}


class PolityOriginalNameFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_original_name
        fields = {
            "original_name": ["exact", "icontains"],
        }


class PolityAlternativeNameFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_alternative_name
        fields = {
            "alternative_name": ["exact", "icontains"],
        }


class PolityDurationFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_duration
        fields = {}


class PolityPeakYearsFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_peak_years
        fields = {
            "peak_year_from": ["exact", "lte", "gte"],
            "peak_year_to": ["exact", "lte", "gte"],
        }


class PolityDegreeOfCentralizationFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_degree_of_centralization
        fields = {
            "degree_of_centralization": ["exact", "lte", "gte"],
        }


class PolitySuprapolityRelationsFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    # <> other_polity

    class Meta:
        model = Polity_suprapolity_relations
        fields = {
            "supra_polity_relations": ["exact", "icontains"],
        }


class PolityUTMZoneFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_utm_zone
        fields = {
            "utm_zone": ["exact", "icontains"],
        }


class PolityCapitalFilter(SeshatCommonFilter, django_filters.FilterSet):
    # <> polity_cap
    
    class Meta:
        model = Polity_capital
        fields = {
            "capital": ["exact", "icontains"],
        }


class PolityLanguageFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_language
        fields = {
            "language": ["exact", "icontains"],
        }


class PolityLinguisticFamilyFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_linguistic_family
        fields = {
            "linguistic_family": ["exact", "icontains"],
        }


class PolityLanguageGenusFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_language_genus
        fields = {
            "language_genus": ["exact", "icontains"],
        }


class PolityReligionGenusFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_religion_genus
        fields = {
            "religion_genus": ["exact", "icontains"],
        }


class PolityReligionFamilyFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_religion_family
        fields = {
            "religion_family": ["exact", "icontains"],
        }


class PolityReligionFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polity_religion
        fields = {
            "religion": ["exact", "icontains"],
        }


class PolityRelationshipToPrecedingEntityFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_relationship_to_preceding_entity
        fields = {
            "relationship_to_preceding_entity": ["exact", "icontains"],
        }


class PolityPrecedingEntityFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    # <> other_polity

    class Meta:
        model = Polity_preceding_entity
        fields = {
            "merged_old_data": ["exact", "icontains"],
            "relationship_to_preceding_entity": ["exact", "icontains"],
            "preceding_entity": ["exact", "icontains"],
        }


class PolitySucceedingEntityFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_succeeding_entity
        fields = {
            "succeeding_entity": ["exact", "icontains"],
        }


class PolitySupraculturalEntityFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_supracultural_entity
        fields = {
            "supracultural_entity": ["exact", "icontains"],
        }


class PolityScaleOfSupraculturalInteractionFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_scale_of_supracultural_interaction
        fields = {
            "scale_from": ["exact", "lte", "gte"],
            "scale_to": ["exact", "lte", "gte"],
        }


class PolityAlternateReligionGenusFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_alternate_religion_genus
        fields = {
            "alternate_religion_genus": ["exact", "icontains"],
        }


class PolityAlternateReligionFamilyFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_alternate_religion_family
        fields = {
            "alternate_religion_family": ["exact", "icontains"],
        }


class PolityAlternateReligionFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_alternate_religion
        fields = {
            "alternate_religion": ["exact", "icontains"],
        }


class PolityExpertFilter(SeshatCommonFilter, django_filters.FilterSet):
    # <> expert

    class Meta:
        model = Polity_expert
        fields = {}


class PolityEditorFilter(SeshatCommonFilter, django_filters.FilterSet):
    # <> editor

    class Meta:
        model = Polity_editor
        fields = {}


class PolityReligiousTraditionFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Polity_religious_tradition
        fields = {
            "religious_tradition": ["exact", "icontains"],
        }
