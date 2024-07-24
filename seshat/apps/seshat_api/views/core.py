from rest_framework import viewsets

from ._permissions import ONLY_ADMIN_PERMISSIONS

from ._mixins import (
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)

from ...core.models import (
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
    SeshatCommon,
    Religion,
    Cliopatria,
    GADMShapefile,
    GADMCountries,
    GADMProvinces,
)


class PrivateCommentsViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Seshat Private Comments.
    """

    model = SeshatPrivateComment
    pagination_class = SeshatAPIPagination
    permissions_dict = ONLY_ADMIN_PERMISSIONS


class PrivateCommentsPartsViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Seshat Private Comment Parts.
    """

    model = SeshatPrivateCommentPart
    pagination_class = SeshatAPIPagination
    permissions_dict = ONLY_ADMIN_PERMISSIONS


class MacroRegionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Macro Regions.
    """

    model = Macro_region
    pagination_class = SeshatAPIPagination


class RegionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Regions.
    """

    model = Seshat_region
    pagination_class = SeshatAPIPagination


class NGAViewSet(MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet):
    """
    A viewset for viewing and editing NGAs, Natural Geographic Areas.
    """

    model = Nga
    pagination_class = SeshatAPIPagination


class PolityViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polities.
    """

    model = Polity
    pagination_class = SeshatAPIPagination


class CapitalViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Capitals.
    """

    model = Capital
    pagination_class = SeshatAPIPagination


class NGAPolityRelationsViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing NGA Polity Relations.
    """

    model = Ngapolityrel
    pagination_class = SeshatAPIPagination


class CountryViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Countries.
    """

    model = Country
    pagination_class = SeshatAPIPagination


class SectionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Sections.
    """

    model = Section
    pagination_class = SeshatAPIPagination


class SubsectionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Subsections.
    """

    model = Subsection
    pagination_class = SeshatAPIPagination


class VariableHierarchyViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Variable Hierarchies.
    """

    model = Variablehierarchy
    pagination_class = SeshatAPIPagination


class ReferenceViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing References.
    """

    model = Reference
    pagination_class = SeshatAPIPagination


class CitationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Citations.
    """

    model = Citation
    pagination_class = SeshatAPIPagination


class SeshatCommentViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Seshat Comments.
    """

    model = SeshatComment
    pagination_class = SeshatAPIPagination


class SeshatCommentPartViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Seshat Comment Parts.
    """

    model = SeshatCommentPart
    pagination_class = SeshatAPIPagination


class ScpThroughCtnViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Seshat Comment Parts' relations to
    Citations.
    """

    model = ScpThroughCtn
    pagination_class = SeshatAPIPagination


class SeshatCommonViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Seshat Common.
    """

    model = SeshatCommon
    pagination_class = SeshatAPIPagination


class ReligionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Religions.
    """

    model = Religion
    pagination_class = SeshatAPIPagination


class CliopatriaViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Video Shapefiles.
    """

    model = Cliopatria
    pagination_class = SeshatAPIPagination


class GADMShapefileViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing GADM Shapefiles.
    """

    model = GADMShapefile
    pagination_class = SeshatAPIPagination


class GADMCountriesViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing GADM Countries.
    """

    model = GADMCountries
    pagination_class = SeshatAPIPagination


class GADMProvincesViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing GADM Provinces.
    """

    model = GADMProvinces
    pagination_class = SeshatAPIPagination
