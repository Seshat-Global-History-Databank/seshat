from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..serializers import GeneralSerializer

STANDARD_API_PERMISSION = {
    "HEAD": [AllowAny],
    "OPTIONS": [AllowAny],
    "GET": [AllowAny],
    "POST": [IsAuthenticated],
    "PUT": [IsAuthenticated],
    "PATCH": [IsAuthenticated],
    "DELETE": [IsAuthenticated],
}
"""Defines the standard permission for the API, if no other is specified in the view."""


class SeshatAPIPagination(PageNumberPagination):
    """
    Custom pagination class for the API.
    """

    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class SeshatAPIRestrictedPagination(PageNumberPagination):
    """
    Custom pagination class for the API.
    """

    page_size = 1
    page_size_query_param = "page_size"
    max_page_size = 1


class MixinSeshatAPIAuth:
    """
    Mixin class to set the authentication classes for the API.
    """

    def get_permissions(self):
        try:
            permissions_dict = self.permissions_dict
        except AttributeError:
            permissions_dict = STANDARD_API_PERMISSION

        return [
            permission()
            for permission in permissions_dict[self.request.method]
        ]


class MixinSeshatAPISerializer:
    def get_serializer_class(self):
        # Set model to self.model
        GeneralSerializer.Meta.model = self.model

        # Set fields to self.fields
        try:
            GeneralSerializer.Meta.fields = self.fields
        except AttributeError:
            GeneralSerializer.Meta.fields = "__all__"

        return GeneralSerializer

    def get_queryset(self):
        return self.model.objects.all()


class FilterBackends:
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = "__all__"
