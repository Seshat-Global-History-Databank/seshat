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
    comment = serializers.StringRelatedField()

    class Meta:
        model = None
        #fields = ['id', 'year_from',] # '__all__'
        exclude = ['drb_reviewed', 'note', 'finalized', 'created_date', 'modified_date', 'expert_reviewed', 'private_comment', 'citations', 'curator']  # Exclude this field
        depth = SESHAT_API_DEPTH

    #def get_comment(self, obj):
    #    return str(obj.comment) if obj.comment else None

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Extract fields to reposition
        polity_data = rep.pop('polity', None)
        comment_data = rep.pop('comment', None)
        description_data = rep.pop('description', None)

        reordered = {}
        for key, value in rep.items():
            reordered[key] = value

            if key == 'id':
                reordered['polity'] = polity_data

        # Add comment and description at the end
        #if comment_data is not None:
        reordered['comment'] = comment_data
        #if description_data is not None:
        reordered['description'] = description_data

        return reordered


class GeneralLuxuryGoodsSerializer(serializers.ModelSerializer):
    """
    A serializer for all Luxury Goods models across the API.
    """
    polity = PolityShortAPISerializer()
    comment = serializers.StringRelatedField()
    place_of_provenance_pol = PolityShortAPISerializer(many=True, read_only=True)

    class Meta:
        model = None
        #fields = ['id', 'year_from',] # '__all__'
        exclude = ['drb_reviewed', 'note', 'finalized', 'created_date', 'modified_date', 'expert_reviewed', 'private_comment', 'citations', 'curator']  # Exclude this field
        depth = SESHAT_API_DEPTH

    #def get_comment(self, obj):
    #    return str(obj.comment) if obj.comment else None

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Extract fields to reposition
        polity_data = rep.pop('polity', None)
        place_data = rep.pop('place_of_provenance_pol', None)
        comment_data = rep.pop('comment', None)
        description_data = rep.pop('description', None)

        reordered = {}
        for key, value in rep.items():
            reordered[key] = value

            if key == 'id':
                reordered['polity'] = polity_data

            if key == 'coded_value':
                reordered['place_of_provenance_pol'] = place_data

        # Add comment and description at the end
        #if comment_data is not None:
        reordered['comment'] = comment_data
        #if description_data is not None:
        reordered['description'] = description_data

        return reordered

class GeneralAllFieldsSerializer(serializers.ModelSerializer):
    """
    A serializer for all models across the API.
    """
    class Meta:
        model = None
        fields = '__all__'

            
        

