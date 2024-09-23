from django import forms

from ..constants import (
    COMMON_FIELDS,
    COMMON_LABELS,
    COMMON_WIDGETS,
    ATTRS,
)

from .models import (
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


class Long_wallForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Long_wall
        fields = COMMON_FIELDS + ["long_wall_from", "long_wall_to"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "long_wall_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "long_wall_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class CopperForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Copper
        fields = COMMON_FIELDS + ["copper"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"copper": forms.RadioSelect()})


class BronzeForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Bronze
        fields = COMMON_FIELDS + ["bronze"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"bronze": forms.RadioSelect()})


class IronForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Iron
        fields = COMMON_FIELDS + ["iron"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"iron": forms.RadioSelect()})


class SteelForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Steel
        fields = COMMON_FIELDS + ["steel"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"steel": forms.RadioSelect()})


class JavelinForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Javelin
        fields = COMMON_FIELDS + ["javelin"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"javelin": forms.RadioSelect()})


class AtlatlForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Atlatl
        fields = COMMON_FIELDS + ["atlatl"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"atlatl": forms.RadioSelect()})


class SlingForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Sling
        fields = COMMON_FIELDS + ["sling"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"sling": forms.RadioSelect()})


class Self_bowForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Self_bow
        fields = COMMON_FIELDS + ["self_bow"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"self_bow": forms.RadioSelect()})


class Composite_bowForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Composite_bow
        fields = COMMON_FIELDS + ["composite_bow"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"composite_bow": forms.RadioSelect()})


class CrossbowForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Crossbow
        fields = COMMON_FIELDS + ["crossbow"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"crossbow": forms.RadioSelect()})


class Tension_siege_engineForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Tension_siege_engine
        fields = COMMON_FIELDS + ["tension_siege_engine"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"tension_siege_engine": forms.RadioSelect()})


class Sling_siege_engineForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Sling_siege_engine
        fields = COMMON_FIELDS + ["sling_siege_engine"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"sling_siege_engine": forms.RadioSelect()})


class Gunpowder_siege_artilleryForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Gunpowder_siege_artillery
        fields = COMMON_FIELDS + ["gunpowder_siege_artillery"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"gunpowder_siege_artillery": forms.RadioSelect()}
        )


class Handheld_firearmForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Handheld_firearm
        fields = COMMON_FIELDS + ["handheld_firearm"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"handheld_firearm": forms.RadioSelect()})


class War_clubForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = War_club
        fields = COMMON_FIELDS + ["war_club"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"war_club": forms.RadioSelect()})


class Battle_axeForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Battle_axe
        fields = COMMON_FIELDS + ["battle_axe"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"battle_axe": forms.RadioSelect()})


class DaggerForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Dagger
        fields = COMMON_FIELDS + ["dagger"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"dagger": forms.RadioSelect()})


class SwordForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Sword
        fields = COMMON_FIELDS + ["sword"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"sword": forms.RadioSelect()})


class SpearForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Spear
        fields = COMMON_FIELDS + ["spear"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"spear": forms.RadioSelect()})


class PolearmForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Polearm
        fields = COMMON_FIELDS + ["polearm"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"polearm": forms.RadioSelect()})


class DogForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Dog
        fields = COMMON_FIELDS + ["dog"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"dog": forms.RadioSelect()})


class DonkeyForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Donkey
        fields = COMMON_FIELDS + ["donkey"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"donkey": forms.RadioSelect()})


class HorseForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Horse
        fields = COMMON_FIELDS + ["horse"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"horse": forms.RadioSelect()})


class CamelForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Camel
        fields = COMMON_FIELDS + ["camel"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"camel": forms.RadioSelect()})


class ElephantForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Elephant
        fields = COMMON_FIELDS + ["elephant"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"elephant": forms.RadioSelect()})


class Wood_bark_etcForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Wood_bark_etc
        fields = COMMON_FIELDS + ["wood_bark_etc"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"wood_bark_etc": forms.RadioSelect()})


class Leather_clothForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Leather_cloth
        fields = COMMON_FIELDS + ["leather_cloth"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"leather_cloth": forms.RadioSelect()})


class ShieldForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Shield
        fields = COMMON_FIELDS + ["shield"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"shield": forms.RadioSelect()})


class HelmetForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Helmet
        fields = COMMON_FIELDS + ["helmet"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"helmet": forms.RadioSelect()})


class BreastplateForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Breastplate
        fields = COMMON_FIELDS + ["breastplate"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"breastplate": forms.RadioSelect()})


class Limb_protectionForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Limb_protection
        fields = COMMON_FIELDS + ["limb_protection"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"limb_protection": forms.RadioSelect()})


class Scaled_armorForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Scaled_armor
        fields = COMMON_FIELDS + ["scaled_armor"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"scaled_armor": forms.RadioSelect()})


class Laminar_armorForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Laminar_armor
        fields = COMMON_FIELDS + ["laminar_armor"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"laminar_armor": forms.RadioSelect()})


class Plate_armorForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Plate_armor
        fields = COMMON_FIELDS + ["plate_armor"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"plate_armor": forms.RadioSelect()})


class Small_vessels_canoes_etcForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Small_vessels_canoes_etc
        fields = COMMON_FIELDS + ["small_vessels_canoes_etc"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"small_vessels_canoes_etc": forms.RadioSelect()}
        )


class Merchant_ships_pressed_into_serviceForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Merchant_ships_pressed_into_service
        fields = COMMON_FIELDS + ["merchant_ships_pressed_into_service"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"merchant_ships_pressed_into_service": forms.RadioSelect()}
        )


class Specialized_military_vesselForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Specialized_military_vessel
        fields = COMMON_FIELDS + ["specialized_military_vessel"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"specialized_military_vessel": forms.RadioSelect()}
        )


class Settlements_in_a_defensive_positionForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Settlements_in_a_defensive_position
        fields = COMMON_FIELDS + ["settlements_in_a_defensive_position"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"settlements_in_a_defensive_position": forms.RadioSelect()}
        )


class Wooden_palisadeForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Wooden_palisade
        fields = COMMON_FIELDS + ["wooden_palisade"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"wooden_palisade": forms.RadioSelect()})


class Earth_rampartForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Earth_rampart
        fields = COMMON_FIELDS + ["earth_rampart"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"earth_rampart": forms.RadioSelect()})


class DitchForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Ditch
        fields = COMMON_FIELDS + ["ditch"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"ditch": forms.RadioSelect()})


class MoatForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Moat
        fields = COMMON_FIELDS + ["moat"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"moat": forms.RadioSelect()})


class Stone_walls_non_mortaredForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Stone_walls_non_mortared
        fields = COMMON_FIELDS + ["stone_walls_non_mortared"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"stone_walls_non_mortared": forms.RadioSelect()}
        )


class Stone_walls_mortaredForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Stone_walls_mortared
        fields = COMMON_FIELDS + ["stone_walls_mortared"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"stone_walls_mortared": forms.RadioSelect()})


class Fortified_campForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Fortified_camp
        fields = COMMON_FIELDS + ["fortified_camp"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"fortified_camp": forms.RadioSelect()})


class Complex_fortificationForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Complex_fortification
        fields = COMMON_FIELDS + ["complex_fortification"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"complex_fortification": forms.RadioSelect()})


class Modern_fortificationForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Modern_fortification
        fields = COMMON_FIELDS + ["modern_fortification"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"modern_fortification": forms.RadioSelect()})


class ChainmailForm(forms.ModelForm):
    """ """

    class Meta:
        """
        :noindex:
        """

        model = Chainmail
        fields = COMMON_FIELDS + ["chainmail"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"chainmail": forms.RadioSelect()})
