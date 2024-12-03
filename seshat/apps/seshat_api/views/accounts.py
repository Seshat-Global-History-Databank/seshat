from rest_framework import viewsets

from ...accounts.models import Profile, Seshat_Expert, Seshat_Task

from ._mixins import (
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)
from ._permissions import ONLY_ADMIN_PERMISSIONS


class ProfileViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ReadOnlyModelViewSet
):
    """
    A viewset for viewing user profiles.
    """

    model = Profile
    pagination_class = SeshatAPIPagination
    lookup_field = "user__username"
    permissions_dict = ONLY_ADMIN_PERMISSIONS


class SeshatExpertViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Seshat Experts.
    """

    model = Seshat_Expert
    pagination_class = SeshatAPIPagination
    lookup_field = "user__username"
    permissions_dict = ONLY_ADMIN_PERMISSIONS


class SeshatTaskViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ReadOnlyModelViewSet
):
    """
    A viewset for viewing Seshat Tasks.
    """

    model = Seshat_Task
    pagination_class = SeshatAPIPagination
    permissions_dict = ONLY_ADMIN_PERMISSIONS
    fields = "__all__"
