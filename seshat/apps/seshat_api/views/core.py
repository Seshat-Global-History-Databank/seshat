from rest_framework import viewsets

from ._permissions import ONLY_ADMIN_PERMISSIONS

from ._mixins import (
    FilterBackends,
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
    SeshatAPIRestrictedPagination
)
from ..filters.core import (
    MacroRegionFilter,
    SeshatRegionFilter,
    NGAFilter,
    PolityFilter,
    CapitalFilter,
    NGAPolityRelationsFilter,
    CountryFilter,
    SectionFilter,
    SubsectionFilter,
    VariableHierarchyFilter,
    ReferenceFilter,
    CitationFilter,
    ReligionFilter,
    CliopatriaFilter,
    GADMShapefileFilter,
    GADMCountriesFilter,
    GADMProvincesFilter,
)

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
    ScpThroughCtn,
    Religion,
    Cliopatria,
    GADMShapefile,
    GADMCountries,
    GADMProvinces,
)


class MacroRegionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Macro Regions.
    """

    model = Macro_region
    pagination_class = SeshatAPIPagination
    filterset_class = MacroRegionFilter


class RegionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Regions.
    """

    model = Seshat_region
    pagination_class = SeshatAPIPagination
    filterset_class = SeshatRegionFilter


class NGAViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing NGAs, Natural Geographic Areas.
    """

    model = Nga
    pagination_class = SeshatAPIPagination
    filterset_class = NGAFilter


class PolityViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polities.
    """

    model = Polity
    pagination_class = SeshatAPIPagination
    filterset_class = PolityFilter
    search_fields = ["@long_name", "@new_name"]


class CapitalViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Capitals.
    """

    model = Capital
    pagination_class = SeshatAPIPagination
    filterset_class = CapitalFilter


class NGAPolityRelationsViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing NGA Polity Relations.
    """

    model = Ngapolityrel
    pagination_class = SeshatAPIPagination
    filterset_class = NGAPolityRelationsFilter


class CountryViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Countries.
    """

    model = Country
    pagination_class = SeshatAPIPagination
    filterset_class = CountryFilter


class SectionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Sections.
    """

    model = Section
    pagination_class = SeshatAPIPagination
    filterset_class = SectionFilter


class SubsectionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Subsections.
    """

    model = Subsection
    pagination_class = SeshatAPIPagination
    filterset_class = SubsectionFilter


class VariableHierarchyViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Variable Hierarchies.
    """

    model = Variablehierarchy
    pagination_class = SeshatAPIPagination
    filterset_class = VariableHierarchyFilter


class ReferenceViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing References.
    """

    model = Reference
    pagination_class = SeshatAPIPagination
    filterset_class = ReferenceFilter


class CitationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Citations.
    """

    model = Citation
    pagination_class = SeshatAPIPagination
    filterset_class = CitationFilter


class ReligionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Religions.
    """

    model = Religion
    pagination_class = SeshatAPIPagination
    filterset_class = ReligionFilter


class CliopatriaViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Cliopatria Shapefiles.
    """

    model = Cliopatria
    pagination_class = SeshatAPIRestrictedPagination
    filterset_class = CliopatriaFilter


class GADMShapefileViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing GADM Shapefiles.
    """

    model = GADMShapefile
    pagination_class = SeshatAPIRestrictedPagination
    filterset_class = GADMShapefileFilter


class GADMCountriesViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing GADM Countries.
    """

    model = GADMCountries
    pagination_class = SeshatAPIRestrictedPagination
    filterset_class = GADMCountriesFilter


from rest_framework.renderers import TemplateHTMLRenderer

class GADMProvincesViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing GADM Provinces.
    """

    model = GADMProvinces
    pagination_class = SeshatAPIRestrictedPagination
    filterset_class = GADMProvincesFilter
