from rest_framework import serializers


SESHAT_API_DEPTH = 3
"""Defines the depth of recursive serialization across all models."""


class GeneralSerializer(serializers.ModelSerializer):
    """
    A serializer for all models across the API.
    """
    class Meta:
        model = None
        fields = '__all__'
        depth = SESHAT_API_DEPTH
