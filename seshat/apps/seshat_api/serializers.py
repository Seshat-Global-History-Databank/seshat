from rest_framework import serializers

from .models import Polity

SESHAT_API_DEPTH = 1
"""Defines the depth of recursive serialization across all models."""

class PolityAPISerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='new_name')  # maps new_name -> name

    class Meta:
        model = Polity
        #fields = ['id', 'year_from',] # '__all__'
        exclude = ['created_date', 'modified_date', 'private_comment_n', 'private_comment', 'new_name']  # Exclude this field
        depth = 1

class PolityShortAPISerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='new_name')  # maps new_name -> name

    class Meta:
        model = Polity
        fields = ['id', 'name', 'long_name', 'start_year', 'end_year'] # '__all__'
        #exclude = ['created_date', 'modified_date', 'private_comment_n', 'private_comment', 'new_name']  # Exclude this field
        depth = 1



class GeneralSerializer(serializers.ModelSerializer):
    """
    A serializer for all models across the API.
    """
    polity = PolityShortAPISerializer()

    class Meta:
        model = None
        #fields = ['id', 'year_from',] # '__all__'
        exclude = ['drb_reviewed', 'note', 'finalized', 'created_date', 'modified_date', 'expert_reviewed', 'private_comment', 'citations', 'curator']  # Exclude this field
        depth = SESHAT_API_DEPTH

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if 'polity' in rep:
            polity_data = rep.pop('polity')
            rep['polity'] = polity_data  # reinsert at the end
        return rep


class GeneralAllFieldsSerializer(serializers.ModelSerializer):
    """
    A serializer for all models across the API.
    """
    class Meta:
        model = None
        fields = '__all__'