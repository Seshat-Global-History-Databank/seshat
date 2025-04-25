from rest_framework import serializers


SESHAT_API_DEPTH = 1
"""Defines the depth of recursive serialization across all models."""


class GeneralSerializer(serializers.ModelSerializer):
    """
    A serializer for all models across the API.
    """
    class Meta:
        model = None
        fields = '__all__'
        #exclude_fields = ['drb_reviewed', 'note', 'finalized']  # Exclude this field
        depth = SESHAT_API_DEPTH
