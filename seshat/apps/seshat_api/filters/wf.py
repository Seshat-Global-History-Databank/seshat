from ..models import (
    Long_wall,
    Copper,
    Bronze,
    Iron,
    Steel,
    Javelin,
    Atlatl,
    Sling,
    Self_bow,
    Composite_bow,
    Crossbow,
    Tension_siege_engine,
    Sling_siege_engine,
    Gunpowder_siege_artillery,
    Handheld_firearm,
    War_club,
    Battle_axe,
    Dagger,
    Sword,
    Spear,
    Polearm,
    Dog,
    Donkey,
    Horse,
    Camel,
    Elephant,
    Wood_bark_etc,
    Leather_cloth,
    Shield,
    Helmet,
    Breastplate,
    Limb_protection,
    Scaled_armor,
    Laminar_armor,
    Plate_armor,
    Small_vessels_canoes_etc,
    Merchant_ships_pressed_into_service,
    Specialized_military_vessel,
    Settlements_in_a_defensive_position,
    Wooden_palisade,
    Earth_rampart,
    Ditch,
    Moat,
    Stone_walls_non_mortared,
    Stone_walls_mortared,
    Fortified_camp,
    Complex_fortification,
    Modern_fortification,
    Chainmail,
)

from django_filters import rest_framework as django_filters
from ._mixins import SeshatCommonFilter


class LongWallFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Long_wall
        fields = {
            "long_wall_from": ["exact", "lte", "gte"],
            "long_wall_to": ["exact", "lte", "gte"],
        }


class CopperFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Copper
        fields = {
            "copper": ["exact"],
        }


class BronzeFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Bronze
        fields = {
            "bronze": ["exact"],
        }


class IronFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Iron
        fields = {
            "iron": ["exact"],
        }


class SteelFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Steel
        fields = {
            "steel": ["exact"],
        }


class JavelinFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Javelin
        fields = {
            "javelin": ["exact"],
        }


class AtlatlFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Atlatl
        fields = {
            "atlatl": ["exact"],
        }


class SlingFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Sling
        fields = {
            "sling": ["exact"],
        }


class SelfBowFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Self_bow
        fields = {
            "self_bow": ["exact"],
        }


class CompositeBowFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Composite_bow
        fields = {
            "composite_bow": ["exact"],
        }


class CrossbowFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Crossbow
        fields = {
            "crossbow": ["exact"],
        }


class TensionSiegeEngineFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Tension_siege_engine
        fields = {
            "tension_siege_engine": ["exact"],
        }


class SlingSiegeEngineFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Sling_siege_engine
        fields = {
            "sling_siege_engine": ["exact"],
        }


class GunpowderSiegeArtilleryFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Gunpowder_siege_artillery
        fields = {
            "gunpowder_siege_artillery": ["exact"],
        }


class HandheldFirearmFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Handheld_firearm
        fields = {
            "handheld_firearm": ["exact"],
        }


class WarClubFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = War_club
        fields = {
            "war_club": ["exact"],
        }


class BattleAxeFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Battle_axe
        fields = {
            "battle_axe": ["exact"],
        }


class DaggerFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Dagger
        fields = {
            "dagger": ["exact"],
        }


class SwordFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Sword
        fields = {
            "sword": ["exact"],
        }


class SpearFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Spear
        fields = {
            "spear": ["exact"],
        }


class PolearmFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Polearm
        fields = {
            "polearm": ["exact"],
        }


class DogFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Dog
        fields = {
            "dog": ["exact"],
        }


class DonkeyFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Donkey
        fields = {
            "donkey": ["exact"],
        }


class HorseFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Horse
        fields = {
            "horse": ["exact"],
        }


class CamelFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Camel
        fields = {
            "camel": ["exact"],
        }


class ElephantFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Elephant
        fields = {
            "elephant": ["exact"],
        }


class WoodBarkEtcFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Wood_bark_etc
        fields = {
            "wood_bark_etc": ["exact"],
        }


class LeatherClothFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Leather_cloth
        fields = {
            "leather_cloth": ["exact"],
        }


class ShieldFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Shield
        fields = {
            "shield": ["exact"],
        }


class HelmetFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Helmet
        fields = {
            "helmet": ["exact"],
        }


class BreastplateFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Breastplate
        fields = {
            "breastplate": ["exact"],
        }


class LimbProtectionFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Limb_protection
        fields = {
            "limb_protection": ["exact"],
        }


class ScaledArmorFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Scaled_armor
        fields = {
            "scaled_armor": ["exact"],
        }


class LaminarArmorFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Laminar_armor
        fields = {
            "laminar_armor": ["exact"],
        }


class PlateArmorFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Plate_armor
        fields = {
            "plate_armor": ["exact"],
        }


class SmallVesselsCanoesEtcFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Small_vessels_canoes_etc
        fields = {
            "small_vessels_canoes_etc": ["exact"],
        }


class MerchantShipsPressedIntoServiceFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Merchant_ships_pressed_into_service
        fields = {
            "merchant_ships_pressed_into_service": ["exact"],
        }


class SpecializedMilitaryVesselFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Specialized_military_vessel
        fields = {
            "specialized_military_vessel": ["exact"],
        }


class SettlementsInADefensivePositionFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Settlements_in_a_defensive_position
        fields = {
            "settlements_in_a_defensive_position": ["exact"],
        }


class WoodenPalisadeFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Wooden_palisade
        fields = {
            "wooden_palisade": ["exact"],
        }


class EarthRampartFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Earth_rampart
        fields = {
            "earth_rampart": ["exact"],
        }


class DitchFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Ditch
        fields = {
            "ditch": ["exact"],
        }


class MoatFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Moat
        fields = {
            "moat": ["exact"],
        }


class StoneWallsNonMortaredFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Stone_walls_non_mortared
        fields = {
            "stone_walls_non_mortared": ["exact"],
        }


class StoneWallsMortaredFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Stone_walls_mortared
        fields = {
            "stone_walls_mortared": ["exact"],
        }


class FortifiedCampFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Fortified_camp
        fields = {
            "fortified_camp": ["exact"],
        }


class ComplexFortificationFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Complex_fortification
        fields = {
            "complex_fortification": ["exact"],
        }


class ModernFortificationFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Modern_fortification
        fields = {
            "modern_fortification": ["exact"],
        }


class ChainmailFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Chainmail
        fields = {"chainmail": ["exact"]}
