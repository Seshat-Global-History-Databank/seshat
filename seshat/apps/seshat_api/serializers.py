from django.contrib.auth.models import User, Group
from rest_framework import serializers

from ..crisisdb.models import (
    Human_sacrifice,
    External_conflict,
    Internal_conflict,
    External_conflict_side,
    Agricultural_population,
    Arable_land,
    Arable_land_per_farmer,
    Gross_grain_shared_per_agricultural_population,
    Net_grain_shared_per_agricultural_population,
    Surplus,
    Military_expense,
    Silver_inflow,
    Silver_stock,
    Total_population,
    Gdp_per_capita,
    Drought_event,
    Locust_event,
    Socioeconomic_turmoil_event,
    Crop_failure_event,
    Famine_event,
    Disease_outbreak,
)
from ..core.models import Polity, Reference


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    The base serializer for the User model. It is used to serialize the User model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    The base serializer for the Group model. It is used to serialize the Group model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Group
        fields = ["url", "name"]


class ReferenceSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Reference model. It is used to serialize the Reference model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Reference
        fields = ["id", "title", "year", "creator", "zotero_link", "long_name"]


################ End of Base Serializers
################ Beginning of Serializers Imports


class Human_sacrificeSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Human_sacrifice model. It is used to serialize the Human_sacrifice model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Human_sacrifice
        fields = ["year_from", "year_to", "human_sacrifice", "tag"]


class External_conflictSerializer(serializers.ModelSerializer):
    """
    The base serializer for the External_conflict model. It is used to serialize the External_conflict model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = External_conflict
        fields = ["year_from", "year_to", "conflict_name", "tag"]


class Internal_conflictSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Internal_conflict model. It is used to serialize the Internal_conflict model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Internal_conflict
        fields = [
            "year_from",
            "year_to",
            "conflict",
            "expenditure",
            "leader",
            "casualty",
            "tag",
        ]


class External_conflict_sideSerializer(serializers.ModelSerializer):
    """
    The base serializer for the External_conflict_side model. It is used to serialize the External_conflict_side model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = External_conflict_side
        fields = [
            "year_from",
            "year_to",
            "conflict_id",
            "expenditure",
            "leader",
            "casualty",
            "tag",
        ]


class Agricultural_populationSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Agricultural_population model. It is used to serialize the Agricultural_population model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Agricultural_population
        fields = ["year_from", "year_to", "agricultural_population", "tag"]


class Arable_landSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Arable_land model. It is used to serialize the Arable_land model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Arable_land
        fields = ["year_from", "year_to", "arable_land", "tag"]


class Arable_land_per_farmerSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Arable_land_per_farmer model. It is used to serialize the Arable_land_per_farmer model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Arable_land_per_farmer
        fields = ["year_from", "year_to", "arable_land_per_farmer", "tag"]


class Gross_grain_shared_per_agricultural_populationSerializer(
    serializers.ModelSerializer
):
    """
    The base serializer for the Gross_grain_shared_per_agricultural_population model. It is used to serialize the Gross_grain_shared_per_agricultural_population model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gross_grain_shared_per_agricultural_population
        fields = [
            "year_from",
            "year_to",
            "gross_grain_shared_per_agricultural_population",
            "tag",
        ]


class Net_grain_shared_per_agricultural_populationSerializer(
    serializers.ModelSerializer
):
    """
    The base serializer for the Net_grain_shared_per_agricultural_population model. It is used to serialize the Net_grain_shared_per_agricultural_population model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Net_grain_shared_per_agricultural_population
        fields = [
            "year_from",
            "year_to",
            "net_grain_shared_per_agricultural_population",
            "tag",
        ]


class SurplusSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Surplus model. It is used to serialize the Surplus model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Surplus
        fields = ["year_from", "year_to", "surplus", "tag"]


class Military_expenseSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Military_expense model. It is used to serialize the Military_expense model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Military_expense
        fields = ["year_from", "year_to", "conflict", "expenditure", "tag"]


class Silver_inflowSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Silver_inflow model. It is used to serialize the Silver_inflow model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Silver_inflow
        fields = ["year_from", "year_to", "silver_inflow", "tag"]


class Silver_stockSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Silver_stock model. It is used to serialize the Silver_stock model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Silver_stock
        fields = ["year_from", "year_to", "silver_stock", "tag"]


class Total_populationSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Total_population model. It is used to serialize the Total_population model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Total_population
        fields = ["year_from", "year_to", "total_population", "tag"]


class Gdp_per_capitaSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Gdp_per_capita model. It is used to serialize the Gdp_per_capita model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gdp_per_capita
        fields = ["year_from", "year_to", "gdp_per_capita", "tag"]


class Drought_eventSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Drought_event model. It is used to serialize the Drought_event model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Drought_event
        fields = ["year_from", "year_to", "drought_event", "tag"]


class Locust_eventSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Locust_event model. It is used to serialize the Locust_event model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Locust_event
        fields = ["year_from", "year_to", "locust_event", "tag"]


class Socioeconomic_turmoil_eventSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Socioeconomic_turmoil_event model. It is used to serialize the Socioeconomic_turmoil_event model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Socioeconomic_turmoil_event
        fields = ["year_from", "year_to", "socioeconomic_turmoil_event", "tag"]


class Crop_failure_eventSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Crop_failure_event model. It is used to serialize the Crop_failure_event model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Crop_failure_event
        fields = ["year_from", "year_to", "crop_failure_event", "tag"]


class Famine_eventSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Famine_event model. It is used to serialize the Famine_event model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Famine_event
        fields = ["year_from", "year_to", "famine_event", "tag"]


class Disease_outbreakSerializer(serializers.ModelSerializer):
    """
    The base serializer for the Disease_outbreak model. It is used to serialize the Disease_outbreak model and return the serialized data in the API response.
    """

    class Meta:
        """
        :noindex:
        """

        model = Disease_outbreak
        fields = [
            "year_from",
            "year_to",
            "longitude",
            "latitude",
            "elevation",
            "sub_category",
            "magnitude",
            "duration",
            "tag",
        ]


class PolitySerializer(serializers.ModelSerializer):
    """
    The base serializer for the Polity model. It is used to serialize the Polity model and return the serialized data in the API response.
    """

    crisisdb_human_sacrifice_related = Human_sacrificeSerializer(
        many=True, read_only=True
    )
    crisisdb_external_conflict_related = External_conflictSerializer(
        many=True, read_only=True
    )
    crisisdb_internal_conflict_related = Internal_conflictSerializer(
        many=True, read_only=True
    )
    crisisdb_external_conflict_side_related = External_conflict_sideSerializer(
        many=True, read_only=True
    )
    crisisdb_agricultural_population_related = Agricultural_populationSerializer(
        many=True, read_only=True
    )
    crisisdb_arable_land_related = Arable_landSerializer(many=True, read_only=True)
    crisisdb_arable_land_per_farmer_related = Arable_land_per_farmerSerializer(
        many=True, read_only=True
    )
    crisisdb_gross_grain_shared_per_agricultural_population_related = (
        Gross_grain_shared_per_agricultural_populationSerializer(
            many=True, read_only=True
        )
    )
    crisisdb_net_grain_shared_per_agricultural_population_related = (
        Net_grain_shared_per_agricultural_populationSerializer(
            many=True, read_only=True
        )
    )
    crisisdb_surplus_related = SurplusSerializer(many=True, read_only=True)
    crisisdb_military_expense_related = Military_expenseSerializer(
        many=True, read_only=True
    )
    crisisdb_silver_inflow_related = Silver_inflowSerializer(many=True, read_only=True)
    crisisdb_silver_stock_related = Silver_stockSerializer(many=True, read_only=True)
    crisisdb_total_population_related = Total_populationSerializer(
        many=True, read_only=True
    )
    crisisdb_gdp_per_capita_related = Gdp_per_capitaSerializer(
        many=True, read_only=True
    )
    crisisdb_drought_event_related = Drought_eventSerializer(many=True, read_only=True)
    crisisdb_locust_event_related = Locust_eventSerializer(many=True, read_only=True)
    crisisdb_socioeconomic_turmoil_event_related = (
        Socioeconomic_turmoil_eventSerializer(many=True, read_only=True)
    )
    crisisdb_crop_failure_event_related = Crop_failure_eventSerializer(
        many=True, read_only=True
    )
    crisisdb_famine_event_related = Famine_eventSerializer(many=True, read_only=True)
    crisisdb_disease_outbreak_related = Disease_outbreakSerializer(
        many=True, read_only=True
    )

    class Meta:
        """
        :noindex:
        """

        model = Polity
        fields = [
            "id",
            "name",
            "start_year",
            "end_year",
            "crisisdb_human_sacrifice_related",
            "crisisdb_external_conflict_related",
            "crisisdb_internal_conflict_related",
            "crisisdb_external_conflict_side_related",
            "crisisdb_agricultural_population_related",
            "crisisdb_arable_land_related",
            "crisisdb_arable_land_per_farmer_related",
            "crisisdb_gross_grain_shared_per_agricultural_population_related",
            "crisisdb_net_grain_shared_per_agricultural_population_related",
            "crisisdb_surplus_related",
            "crisisdb_military_expense_related",
            "crisisdb_silver_inflow_related",
            "crisisdb_silver_stock_related",
            "crisisdb_total_population_related",
            "crisisdb_gdp_per_capita_related",
            "crisisdb_drought_event_related",
            "crisisdb_locust_event_related",
            "crisisdb_socioeconomic_turmoil_event_related",
            "crisisdb_crop_failure_event_related",
            "crisisdb_famine_event_related",
            "crisisdb_disease_outbreak_related",
        ]


################ End of Serializers Imports
