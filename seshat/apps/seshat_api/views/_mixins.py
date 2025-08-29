from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..serializers import PolityAPISerializer ,GeneralSerializer, GeneralAllFieldsSerializer, GeneralLuxuryGoodsSerializer

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

    page_size = 50
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


class MixinSeshatAPISerializerNEW:
    def get_serializer_class(self):
        # Set model to self.model
        GeneralSerializer.Meta.model = self.model

        # Set fields to self.fields or apply custom logic
        try:
            # Set fields dynamically or include/exclude specific fields
            if hasattr(self, 'fields'):
                GeneralSerializer.Meta.fields = self.fields
            else:
                GeneralSerializer.Meta.fields = "__all__"
        except AttributeError:
            GeneralSerializer.Meta.fields = "__all__"

        # Modify or exclude fields here if needed
        if hasattr(self, 'exclude_fields'):
            exclude_fields = self.exclude_fields  # A list of field names to exclude
            if exclude_fields:
                #print(exclude_fields)
                # Modify fields to exclude
                fields = GeneralSerializer.Meta.fields
                if fields == "__all__":
                    fields = [field.name for field in self.model._meta.fields]  # Get all fields dynamically
                GeneralSerializer.Meta.fields = [f for f in fields if f not in exclude_fields]

        # Return the dynamically created serializer class
        return GeneralSerializer

    def get_queryset(self):
        return self.model.objects.all()

class MixinSeshatAPISerializer:
    def get_serializer_class(self):
        # Set model to self.model
        GeneralSerializer.Meta.model = self.model

        # Set fields to self.fields
        # try:
        #     print(GeneralSerializer.Meta.exclude_fields

        #     GeneralSerializer.Meta.fields = self.fields
        # except AttributeError:
        #     GeneralSerializer.Meta.fields = "__all__"

        return GeneralSerializer

    def get_queryset(self):
        return self.model.objects.all()
    
class MixinLuxuryGoodsSeshatAPISerializer:
    def get_serializer_class(self):
        # Set model to self.model
        GeneralLuxuryGoodsSerializer.Meta.model = self.model

        return GeneralLuxuryGoodsSerializer

    def get_queryset(self):
        return self.model.objects.all()
    
class MixinSeshatAPISerializerAllFields:
    def get_serializer_class(self):
        # Set model to self.model
        GeneralAllFieldsSerializer.Meta.model = self.model

        return GeneralAllFieldsSerializer

    def get_queryset(self):
        return self.model.objects.all()
    
class MixinSeshatPolity:
    def get_serializer_class(self):
        PolityAPISerializer.Meta.model = self.model

        return PolityAPISerializer
    def get_queryset(self):
        return self.model.objects.all()
    

class FilterBackends:
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ['id',]
