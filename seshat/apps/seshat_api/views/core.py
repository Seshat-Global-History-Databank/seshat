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
    PrivateCommentFilter,
    PrivateCommentsPartFilter,
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
    SeshatCommentFilter,
    SeshatCommentPartFilter,
    ScpThroughCtnFilter,
    ReligionFilter,
    VideoShapefileFilter,
    GADMShapefileFilter,
    GADMCountriesFilter,
    GADMProvincesFilter,
)

from ..models import (
    SeshatPrivateComment,
    SeshatPrivateCommentPart,
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
    SeshatComment,
    SeshatCommentPart,
    ScpThroughCtn,
    Religion,
    Cliopatria,
    GADMShapefile,
    GADMCountries,
    GADMProvinces,
)


class PrivateCommentsViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Seshat Private Comments.
    """

    model = SeshatPrivateComment
    pagination_class = SeshatAPIPagination
    permissions_dict = ONLY_ADMIN_PERMISSIONS
    filterset_class = PrivateCommentFilter


class PrivateCommentsPartsViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Seshat Private Comment Parts.
    """

    model = SeshatPrivateCommentPart
    pagination_class = SeshatAPIPagination
    permissions_dict = ONLY_ADMIN_PERMISSIONS
    filterset_class = PrivateCommentsPartFilter


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


class SeshatCommentViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Seshat Comments.
    """

    model = SeshatComment
    pagination_class = SeshatAPIPagination
    permissions_dict = ONLY_ADMIN_PERMISSIONS
    filterset_class = SeshatCommentFilter


class SeshatCommentPartViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Seshat Comment Parts.
    """

    model = SeshatCommentPart
    pagination_class = SeshatAPIPagination
    permissions_dict = ONLY_ADMIN_PERMISSIONS
    filterset_class = SeshatCommentPartFilter


class ScpThroughCtnViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Seshat Comment Parts' relations to
    Citations.
    """

    model = ScpThroughCtn
    pagination_class = SeshatAPIPagination
    permissions_dict = ONLY_ADMIN_PERMISSIONS
    filterset_class = ScpThroughCtnFilter


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
    A viewset for viewing and editing Video Shapefiles.
    """

    model = Cliopatria
    pagination_class = SeshatAPIRestrictedPagination
    filterset_class = VideoShapefileFilter


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
