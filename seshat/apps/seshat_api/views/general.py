from rest_framework import viewsets

from ._permissions import ONLY_ADMIN_PERMISSIONS
from ._mixins import (
    FilterBackends,
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)

from ..filters.general import (
    PolityOriginalNameFilter,
    PolityAlternativeNameFilter,
    PolityDurationFilter,
    PolityPeakYearsFilter,
    PolityDegreeOfCentralizationFilter,
    PolitySuprapolityRelationsFilter,
    PolityUTMZoneFilter,
    PolityCapitalFilter,
    PolityLanguageFilter,
    PolityLinguisticFamilyFilter,
    PolityLanguageGenusFilter,
    PolityReligionGenusFilter,
    PolityReligionFamilyFilter,
    PolityReligionFilter,
    PolityRelationshipToPrecedingEntityFilter,
    PolityPrecedingEntityFilter,
    PolitySucceedingEntityFilter,
    PolitySupraculturalEntityFilter,
    PolityScaleOfSupraculturalInteractionFilter,
    PolityAlternateReligionGenusFilter,
    PolityAlternateReligionFamilyFilter,
    PolityAlternateReligionFilter,
    PolityReligiousTraditionFilter,
)

from ..models import (
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
    Polity_religious_tradition,
)

class PolityOriginalNameViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Original Names.
    """

    model = Polity_original_name
    pagination_class = SeshatAPIPagination
    filterset_class = PolityOriginalNameFilter


class PolityAlternativeNameViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Alternative Names.
    """

    model = Polity_alternative_name
    pagination_class = SeshatAPIPagination
    filterset_class = PolityAlternativeNameFilter


class PolityDurationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Durations.
    """

    model = Polity_duration
    pagination_class = SeshatAPIPagination
    filterset_class = PolityDurationFilter


class PolityPeakYearsViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Peak Years.
    """

    model = Polity_peak_years
    pagination_class = SeshatAPIPagination
    filterset_class = PolityPeakYearsFilter


class PolityDegreeOfCentralizationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Degrees of Centralization.
    """

    model = Polity_degree_of_centralization
    pagination_class = SeshatAPIPagination
    filterset_class = PolityDegreeOfCentralizationFilter


class PolitySuprapolityRelationsViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Suprapolity Relations.
    """

    model = Polity_suprapolity_relations
    pagination_class = SeshatAPIPagination
    filterset_class = PolitySuprapolityRelationsFilter


class PolityUTMZoneViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity UTM Zones.
    """

    model = Polity_utm_zone
    pagination_class = SeshatAPIPagination
    filterset_class = PolityUTMZoneFilter


class PolityCapitalViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Capitals.
    """

    model = Polity_capital
    pagination_class = SeshatAPIPagination
    filterset_class = PolityCapitalFilter


class PolityLanguageViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Languages.
    """

    model = Polity_language
    pagination_class = SeshatAPIPagination
    filterset_class = PolityLanguageFilter


class PolityLinguisticFamilyViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Linguistic Families.
    """

    model = Polity_linguistic_family
    pagination_class = SeshatAPIPagination
    filterset_class = PolityLinguisticFamilyFilter


class PolityLanguageGenusViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Language Genuses.
    """

    model = Polity_language_genus
    pagination_class = SeshatAPIPagination
    filterset_class = PolityLanguageGenusFilter


class PolityReligionGenusViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Religion Genuses.
    """

    model = Polity_religion_genus
    pagination_class = SeshatAPIPagination
    filterset_class = PolityReligionGenusFilter


class PolityReligionFamilyViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Religion Families.
    """

    model = Polity_religion_family
    pagination_class = SeshatAPIPagination
    filterset_class = PolityReligionFamilyFilter


class PolityReligionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Religions.
    """

    model = Polity_religion
    pagination_class = SeshatAPIPagination
    filterset_class = PolityReligionFilter


class PolityRelationshipToPrecedingEntityViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Relationships to Preceding Entities.
    """

    model = Polity_relationship_to_preceding_entity
    pagination_class = SeshatAPIPagination
    filterset_class = PolityRelationshipToPrecedingEntityFilter


class PolityPrecedingEntityViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Preceding Entities.
    """

    model = Polity_preceding_entity
    pagination_class = SeshatAPIPagination
    filterset_class = PolityPrecedingEntityFilter


class PolitySucceedingEntityViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Succeeding Entities.
    """

    model = Polity_succeeding_entity
    pagination_class = SeshatAPIPagination
    filterset_class = PolitySucceedingEntityFilter


class PolitySupraculturalEntityViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Supracultural Entities.
    """

    model = Polity_supracultural_entity
    pagination_class = SeshatAPIPagination
    filterset_class = PolitySupraculturalEntityFilter


class PolityScaleOfSupraculturalInteractionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Scales of Supracultural Interaction.
    """

    model = Polity_scale_of_supracultural_interaction
    pagination_class = SeshatAPIPagination
    filterset_class = PolityScaleOfSupraculturalInteractionFilter


class PolityAlternateReligionGenusViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Alternate Religion Genuses.
    """

    model = Polity_alternate_religion_genus
    pagination_class = SeshatAPIPagination
    filterset_class = PolityAlternateReligionGenusFilter


class PolityAlternateReligionFamilyViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Alternate Religion Families.
    """

    model = Polity_alternate_religion_family
    pagination_class = SeshatAPIPagination
    filterset_class = PolityAlternateReligionFamilyFilter


class PolityAlternateReligionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Alternate Religions.
    """

    model = Polity_alternate_religion
    pagination_class = SeshatAPIPagination
    filterset_class = PolityAlternateReligionFilter


class PolityReligiousTraditionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polity Religious Traditions.
    """

    model = Polity_religious_tradition
    pagination_class = SeshatAPIPagination
    filterset_class = PolityReligiousTraditionFilter
