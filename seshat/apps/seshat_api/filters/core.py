from ..models import (
    Macro_region,
    Seshat_region,
    Nga,
    Polity,
    Capital,
    Ngapolityrel,
    Country,
    Section,
    Subsection,
    Variablehierarchy,
    Reference,
    Citation,
    Religion,
    Cliopatria,
    GADMShapefile,
    GADMCountries,
    GADMProvinces,
)
from django_filters import rest_framework as django_filters


class MacroRegionFilter(django_filters.FilterSet):
    class Meta:
        model = Macro_region
        fields = {"name": ["icontains", "exact"]}


class SeshatRegionFilter(django_filters.FilterSet):
    # <> mac_region

    class Meta:
        model = Seshat_region
        fields = {
            "name": ["icontains", "exact"],
            "subregions_list": ["icontains", "exact"],
        }


class NGAFilter(django_filters.FilterSet):
    class Meta:
        model = Nga
        fields = {
            "name": ["icontains", "exact"],
            "subregion": ["icontains", "exact"],
            "longitude": ["lte", "gte", "exact"],
            "latitude": ["lte", "gte", "exact"],
            "capital_city": ["icontains", "exact"],
            "nga_code": ["icontains", "exact"],
            "fao_country": ["icontains", "exact"],
            "world_region": ["exact"],
        }


class PolityFilter(django_filters.FilterSet):
    home_seshat_region_contains = django_filters.CharFilter(
        field_name="home_seshat_region__name", lookup_expr="icontains"
    )
    home_nga_name_contains = django_filters.CharFilter(
        field_name="home_nga__name", lookup_expr="icontains"
    )
    home_nga_code = django_filters.CharFilter(
        field_name="home_nga__nga_code", lookup_expr="exact"
    )
    # general_description_contains = django_filters.CharFilter(
    #     field_name="general_description", lookup_expr="icontains"
    # )
    min_nga_longitude = django_filters.NumberFilter(
        field_name="home_nga__longitude", lookup_expr="gte"
    )
    min_nga_latitude = django_filters.NumberFilter(
        field_name="home_nga__latitude", lookup_expr="gte"
    )
    max_nga_longitude = django_filters.NumberFilter(
        field_name="home_nga__longitude", lookup_expr="lte"
    )
    max_nga_latitude = django_filters.NumberFilter(
        field_name="home_nga__latitude", lookup_expr="lte"
    )

    class Meta:
        model = Polity
        # fields = "__all__"  # Generally not considered safe

        fields = {
            "name": ["icontains"],
            "start_year": ["exact", "gt", "lt"],
            "end_year": ["exact", "gt", "lt"],
            "long_name": ["icontains"],
            "new_name": ["icontains"],
            "polity_tag": ["exact"],
            "general_description": ["icontains"],
            "shapefile_name": ["icontains"],
            "created_date": ["range", "date__exact", "date__gt", "date__lt"],
            "modified_date": ["range", "date__exact", "date__gt", "date__lt"],
        }


class CapitalFilter(django_filters.FilterSet):
    class Meta:
        model = Capital
        fields = {
            "name": ["icontains", "exact"],
            "alternative_names": ["icontains", "exact"],
            "current_country": ["icontains", "exact"],
            "latitude": ["lte", "gte", "exact"],
            "longitude": ["lte", "gte", "exact"],
            "year_from": ["lte", "gte", "exact"],
            "year_to": ["lte", "gte", "exact"],
            "url_on_the_map": ["icontains", "exact"],
            "is_verified": ["exact"],
        }


class NGAPolityRelationsFilter(django_filters.FilterSet):
    # <> polity_party
    # <> nga_party

    polity_name_contains = django_filters.CharFilter(
        field_name="polity_party__name", lookup_expr="icontains"
    )
    nga_name_contains = django_filters.CharFilter(
        field_name="nga_party__name", lookup_expr="icontains"
    )

    class Meta:
        model = Ngapolityrel
        fields = {
            "name": ["icontains", "exact"],
            "year_from": ["lte", "gte", "exact"],
            "year_to": ["lte", "gte", "exact"],
            "is_home_nga": ["exact"],
        }


class CountryFilter(django_filters.FilterSet):
    polity_name_contains = django_filters.CharFilter(
        field_name="polity__name", lookup_expr="icontains"
    )

    class Meta:
        model = Country
        fields = {"name": ["icontains", "exact"]}


class SectionFilter(django_filters.FilterSet):
    class Meta:
        model = Section
        fields = {"name": ["icontains", "exact"]}


class SubsectionFilter(django_filters.FilterSet):
    section_name_contains = django_filters.CharFilter(
        field_name="section__name", lookup_expr="icontains"
    )

    class Meta:
        model = Subsection
        fields = {"name": ["icontains", "exact"]}


class VariableHierarchyFilter(django_filters.FilterSet):
    section_name_contains = django_filters.CharFilter(
        field_name="section__name", lookup_expr="icontains"
    )
    subsection_name_contains = django_filters.CharFilter(
        field_name="subsection__name", lookup_expr="icontains"
    )

    class Meta:
        model = Variablehierarchy
        fields = {
            "name": ["icontains", "exact"],
            "is_verified": ["exact"],
            "explanation": ["icontains"],
        }


class ReferenceFilter(django_filters.FilterSet):
    class Meta:
        model = Reference
        fields = {
            "title": ["icontains", "exact"],
            "year": ["lte", "gte", "exact"],
            "creator": ["icontains", "exact"],
            "zotero_link": ["icontains", "exact"],
            "long_name": ["icontains", "exact"],
            "url_link": ["icontains", "exact"],
            "created_date": ["range", "date__lte", "date__gte", "date__exact"],
            "modified_date": ["range", "date__lte", "date__gte", "date__exact"],
        }


class CitationFilter(django_filters.FilterSet):
    reference_title_contains = django_filters.CharFilter(
        field_name="ref__title", lookup_expr="icontains"
    )
    reference_creator_contains = django_filters.CharFilter(
        field_name="ref__creator", lookup_expr="icontains"
    )
    reference_year_lte = django_filters.NumberFilter(
        field_name="ref__year", lookup_expr="lte"
    )
    reference_year_gte = django_filters.NumberFilter(
        field_name="ref__year", lookup_expr="gte"
    )

    class Meta:
        model = Citation
        fields = {
            "page_from": ["lte", "gte", "exact"],
            "page_to": ["lte", "gte", "exact"],
            "created_date": ["range", "date__lte", "date__gte", "date__exact"],
            "modified_date": ["range", "date__lte", "date__gte", "date__exact"],
        }


class ReligionFilter(django_filters.FilterSet):
    class Meta:
        model = Religion
        fields = {
            "name": ["icontains", "exact"],
            "religion_name": ["icontains", "exact"],
            "religion_family": ["icontains", "exact"],
            "religion_genus": ["icontains", "exact"],
        }


class CliopatriaFilter(django_filters.FilterSet):
    class Meta:
        model = Cliopatria
        fields = {
            "name": ["icontains", "exact"],
            "wikipedia_name": ["icontains", "exact"],
            "seshat_id": ["icontains", "exact"],
            "area": ["lte", "gte", "exact"],
            "start_year": ["lte", "gte", "exact"],
            "end_year": ["lte", "gte", "exact"],
            "polity_start_year": ["lte", "gte", "exact"],
            "polity_end_year": ["lte", "gte", "exact"],
            "colour": ["icontains", "exact"],
            "components": ["icontains", "exact"],
            "member_of": ["icontains", "exact"],
        }


class GADMShapefileFilter(django_filters.FilterSet):
    class Meta:
        model = GADMShapefile
        fields = {
            "UID": ["icontains", "exact"],
            "GID_0": ["icontains", "exact"],
            "NAME_0": ["icontains", "exact"],
            "VARNAME_0": ["icontains", "exact"],
            "GID_1": ["icontains", "exact"],
            "NAME_1": ["icontains", "exact"],
            "VARNAME_1": ["icontains", "exact"],
            "NL_NAME_1": ["icontains", "exact"],
            "ISO_1": ["icontains", "exact"],
            "HASC_1": ["icontains", "exact"],
            "CC_1": ["icontains", "exact"],
            "TYPE_1": ["icontains", "exact"],
            "ENGTYPE_1": ["icontains", "exact"],
            "VALIDFR_1": ["icontains", "exact"],
            "GID_2": ["icontains", "exact"],
            "NAME_2": ["icontains", "exact"],
            "VARNAME_2": ["icontains", "exact"],
            "NL_NAME_2": ["icontains", "exact"],
            "HASC_2": ["icontains", "exact"],
            "CC_2": ["icontains", "exact"],
            "TYPE_2": ["icontains", "exact"],
            "ENGTYPE_2": ["icontains", "exact"],
            "VALIDFR_2": ["icontains", "exact"],
            "GID_3": ["icontains", "exact"],
            "NAME_3": ["icontains", "exact"],
            "VARNAME_3": ["icontains", "exact"],
            "NL_NAME_3": ["icontains", "exact"],
            "HASC_3": ["icontains", "exact"],
            "CC_3": ["icontains", "exact"],
            "TYPE_3": ["icontains", "exact"],
            "ENGTYPE_3": ["icontains", "exact"],
            "VALIDFR_3": ["icontains", "exact"],
            "GID_4": ["icontains", "exact"],
            "NAME_4": ["icontains", "exact"],
            "VARNAME_4": ["icontains", "exact"],
            "CC_4": ["icontains", "exact"],
            "TYPE_4": ["icontains", "exact"],
            "ENGTYPE_4": ["icontains", "exact"],
            "VALIDFR_4": ["icontains", "exact"],
            "GID_5": ["icontains", "exact"],
            "NAME_5": ["icontains", "exact"],
            "CC_5": ["icontains", "exact"],
            "TYPE_5": ["icontains", "exact"],
            "ENGTYPE_5": ["icontains", "exact"],
            "GOVERNEDBY": ["icontains", "exact"],
            "SOVEREIGN": ["icontains", "exact"],
            "DISPUTEDBY": ["icontains", "exact"],
            "REGION": ["icontains", "exact"],
            "VARREGION": ["icontains", "exact"],
            "COUNTRY": ["icontains", "exact"],
            "CONTINENT": ["icontains", "exact"],
            "SUBCONT": ["icontains", "exact"],
        }


class GADMCountriesFilter(django_filters.FilterSet):
    class Meta:
        model = GADMCountries
        fields = {
            "COUNTRY": ["icontains", "exact"],
        }


class GADMProvincesFilter(django_filters.FilterSet):
    class Meta:
        model = GADMProvinces
        fields = {
            "COUNTRY": ["icontains", "exact"],
            "NAME_1": ["icontains", "exact"],
            "ENGTYPE_1": ["icontains", "exact"],
        }
