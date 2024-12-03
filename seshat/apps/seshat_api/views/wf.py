from rest_framework import viewsets

from ._mixins import (
    FilterBackends,
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)

from ..filters.wf import (
    LongWallFilter,
    CopperFilter,
    BronzeFilter,
    IronFilter,
    SteelFilter,
    JavelinFilter,
    AtlatlFilter,
    SlingFilter,
    SelfBowFilter,
    CompositeBowFilter,
    CrossbowFilter,
    TensionSiegeEngineFilter,
    SlingSiegeEngineFilter,
    GunpowderSiegeArtilleryFilter,
    HandheldFirearmFilter,
    WarClubFilter,
    BattleAxeFilter,
    DaggerFilter,
    SwordFilter,
    SpearFilter,
    PolearmFilter,
    DogFilter,
    DonkeyFilter,
    HorseFilter,
    CamelFilter,
    ElephantFilter,
    WoodBarkEtcFilter,
    LeatherClothFilter,
    ShieldFilter,
    HelmetFilter,
    BreastplateFilter,
    LimbProtectionFilter,
    ScaledArmorFilter,
    LaminarArmorFilter,
    PlateArmorFilter,
    SmallVesselsCanoesEtcFilter,
    MerchantShipsPressedIntoServiceFilter,
    SpecializedMilitaryVesselFilter,
    SettlementsInADefensivePositionFilter,
    WoodenPalisadeFilter,
    EarthRampartFilter,
    DitchFilter,
    MoatFilter,
    StoneWallsNonMortaredFilter,
    StoneWallsMortaredFilter,
    FortifiedCampFilter,
    ComplexFortificationFilter,
    ModernFortificationFilter,
    ChainmailFilter,
)

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


class LongWallViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Long Walls.
    """

    model = Long_wall
    pagination_class = SeshatAPIPagination
    filterset_class = LongWallFilter


class CopperViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Coppers.
    """

    model = Copper
    pagination_class = SeshatAPIPagination
    filterset_class = CopperFilter


class BronzeViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Bronzes.
    """

    model = Bronze
    pagination_class = SeshatAPIPagination
    filterset_class = BronzeFilter


class IronViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Irons.
    """

    model = Iron
    pagination_class = SeshatAPIPagination
    filterset_class = IronFilter


class SteelViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Steels.
    """

    model = Steel
    pagination_class = SeshatAPIPagination
    filterset_class = SteelFilter


class JavelinViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Javelins.
    """

    model = Javelin
    pagination_class = SeshatAPIPagination
    filterset_class = JavelinFilter


class AtlatlViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Atlatls.
    """

    model = Atlatl
    pagination_class = SeshatAPIPagination
    filterset_class = AtlatlFilter


class SlingViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Slings.
    """

    model = Sling
    pagination_class = SeshatAPIPagination
    filterset_class = SlingFilter


class SelfBowViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Self Bows.
    """

    model = Self_bow
    pagination_class = SeshatAPIPagination
    filterset_class = SelfBowFilter


class CompositeBowViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Composite Bows.
    """

    model = Composite_bow
    pagination_class = SeshatAPIPagination
    filterset_class = CompositeBowFilter


class CrossbowViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Crossbows.
    """

    model = Crossbow
    pagination_class = SeshatAPIPagination
    filterset_class = CrossbowFilter


class TensionSiegeEngineViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Tension Siege Engines.
    """

    model = Tension_siege_engine
    pagination_class = SeshatAPIPagination
    filterset_class = TensionSiegeEngineFilter


class SlingSiegeEngineViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Sling Siege Engines.
    """

    model = Sling_siege_engine
    pagination_class = SeshatAPIPagination
    filterset_class = SlingSiegeEngineFilter


class GunpowderSiegeArtilleryViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Gunpowder Siege Artilleries.
    """

    model = Gunpowder_siege_artillery
    pagination_class = SeshatAPIPagination
    filterset_class = GunpowderSiegeArtilleryFilter


class HandheldFirearmViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Handheld Firearms.
    """

    model = Handheld_firearm
    pagination_class = SeshatAPIPagination
    filterset_class = HandheldFirearmFilter


class WarClubViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing War Clubs.
    """

    model = War_club
    pagination_class = SeshatAPIPagination
    filterset_class = WarClubFilter


class BattleAxeViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Battle Axes.
    """

    model = Battle_axe
    pagination_class = SeshatAPIPagination
    filterset_class = BattleAxeFilter


class DaggerViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Daggers.
    """

    model = Dagger
    pagination_class = SeshatAPIPagination
    filterset_class = DaggerFilter


class SwordViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Swords.
    """

    model = Sword
    pagination_class = SeshatAPIPagination
    filterset_class = SwordFilter


class SpearViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Spears.
    """

    model = Spear
    pagination_class = SeshatAPIPagination
    filterset_class = SpearFilter


class PolearmViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Polearms.
    """

    model = Polearm
    pagination_class = SeshatAPIPagination
    filterset_class = PolearmFilter


class DogViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Dogs.
    """

    model = Dog
    pagination_class = SeshatAPIPagination
    filterset_class = DogFilter


class DonkeyViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Donkeys.
    """

    model = Donkey
    pagination_class = SeshatAPIPagination
    filterset_class = DonkeyFilter


class HorseViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Horses.
    """

    model = Horse
    pagination_class = SeshatAPIPagination
    filterset_class = HorseFilter


class CamelViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Camels.
    """

    model = Camel
    pagination_class = SeshatAPIPagination
    filterset_class = CamelFilter


class ElephantViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Elephants.
    """

    model = Elephant
    pagination_class = SeshatAPIPagination
    filterset_class = ElephantFilter


class WoodBarkEtcViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Wood bark, etc.
    """

    model = Wood_bark_etc
    pagination_class = SeshatAPIPagination
    filterset_class = WoodBarkEtcFilter


class LeatherClothViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Leather Cloth.
    """

    model = Leather_cloth
    pagination_class = SeshatAPIPagination
    filterset_class = LeatherClothFilter


class ShieldViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Shields.
    """

    model = Shield
    pagination_class = SeshatAPIPagination
    filterset_class = ShieldFilter


class HelmetViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Helmets.
    """

    model = Helmet
    pagination_class = SeshatAPIPagination
    filterset_class = HelmetFilter


class BreastplateViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Breastplates.
    """

    model = Breastplate
    pagination_class = SeshatAPIPagination
    filterset_class = BreastplateFilter


class LimbProtectionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Limb Protections.
    """

    model = Limb_protection
    pagination_class = SeshatAPIPagination
    filterset_class = LimbProtectionFilter


class ScaledArmorViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Scaled Armors.
    """

    model = Scaled_armor
    pagination_class = SeshatAPIPagination
    filterset_class = ScaledArmorFilter


class LaminarArmorViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Laminar Armors.
    """

    model = Laminar_armor
    pagination_class = SeshatAPIPagination
    filterset_class = LaminarArmorFilter


class PlateArmorViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Plate Armors.
    """

    model = Plate_armor
    pagination_class = SeshatAPIPagination
    filterset_class = PlateArmorFilter


class SmallVesselsCanoesEtcViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Small Vessels, Canoes, etc.
    """

    model = Small_vessels_canoes_etc
    pagination_class = SeshatAPIPagination
    filterset_class = SmallVesselsCanoesEtcFilter


class MerchantShipPressedIntoServiceViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Merchant Ships Pressed Into Services.
    """

    model = Merchant_ships_pressed_into_service
    pagination_class = SeshatAPIPagination
    filterset_class = MerchantShipsPressedIntoServiceFilter


class SpecializedMilitaryVesselViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Specialized Military Vessels.
    """

    model = Specialized_military_vessel
    pagination_class = SeshatAPIPagination
    filterset_class = SpecializedMilitaryVesselFilter


class SettlementInADefensivePositionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Settlements in a Defensive Position.
    """

    model = Settlements_in_a_defensive_position
    pagination_class = SeshatAPIPagination
    filterset_class = SettlementsInADefensivePositionFilter


class WoodenPalisadeViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Wooden Palisades.
    """

    model = Wooden_palisade
    pagination_class = SeshatAPIPagination
    filterset_class = WoodenPalisadeFilter


class EarthRampartViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Earth Ramparts.
    """

    model = Earth_rampart
    pagination_class = SeshatAPIPagination
    filterset_class = EarthRampartFilter


class DitchViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Ditches.
    """

    model = Ditch
    pagination_class = SeshatAPIPagination
    filterset_class = DitchFilter


class MoatViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Moats.
    """

    model = Moat
    pagination_class = SeshatAPIPagination
    filterset_class = MoatFilter


class StoneWallsNonMortaredViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Stone Walls Non Mortared.
    """

    model = Stone_walls_non_mortared
    pagination_class = SeshatAPIPagination
    filterset_class = StoneWallsNonMortaredFilter


class StoneWallsMortaredViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Stone Walls Mortared.
    """

    model = Stone_walls_mortared
    pagination_class = SeshatAPIPagination
    filterset_class = StoneWallsMortaredFilter


class FortifiedCampViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Fortified Camps.
    """

    model = Fortified_camp
    pagination_class = SeshatAPIPagination
    filterset_class = FortifiedCampFilter


class ComplexFortificationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Complex Fortifications.
    """

    model = Complex_fortification
    pagination_class = SeshatAPIPagination
    filterset_class = ComplexFortificationFilter


class ModernFortificationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Modern Fortifications.
    """

    model = Modern_fortification
    pagination_class = SeshatAPIPagination
    filterset_class = ModernFortificationFilter


class ChainmailViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Chainmails.
    """

    model = Chainmail
    pagination_class = SeshatAPIPagination
    filterset_class = ChainmailFilter
