from .models import Long_wall, Copper, Bronze, Iron, Steel, Javelin, Atlatl, Sling, Self_bow, Composite_bow, Crossbow, Tension_siege_engine, Sling_siege_engine, Gunpowder_siege_artillery, Handheld_firearm, War_club, Battle_axe, Dagger, Sword, Spear, Polearm, Dog, Donkey, Horse, Camel, Elephant, Wood_bark_etc, Leather_cloth, Shield, Helmet, Breastplate, Limb_protection, Scaled_armor, Laminar_armor, Plate_armor, Small_vessels_canoes_etc, Merchant_ships_pressed_into_service, Specialized_military_vessel, Settlements_in_a_defensive_position, Wooden_palisade, Earth_rampart, Ditch, Moat, Stone_walls_non_mortared, Stone_walls_mortared, Fortified_camp, Complex_fortification, Modern_fortification, Chainmail
import datetime

from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register

commonlabels = {
    'year_from': 'Start Year',
    'year_to': 'End Year',
    'tag': 'Confidence Level',
    "is_disputed" : "&nbsp; <b> There is a Dispute? </b>",
    "is_uncertain" : "&nbsp; <b> There is Uncertainty? </b>",

    "expert_reviewed" : "&nbsp; Expert Checked?",
    "drb_reviewed" : "&nbsp; Data Review Board Reviewed?",
    'citations': 'Add one or more Citations',
    'finalized': 'This piece of data is verified.',
}

commonfields = ['polity', 'year_from', 'year_to',
                'description', 'tag', 'is_disputed', 'is_uncertain', 'expert_reviewed', 'drb_reviewed', 'finalized', 'citations']

commonwidgets = {
    'polity': forms.Select(attrs={'class': 'form-control  mb-1 js-example-basic-single', 'id': 'id_polity', 'name': 'polity'}),    'year_from': forms.NumberInput(attrs={'class': 'form-control  mb-3',}),
    'year_to': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),
    'description': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 140px', 'placeholder':'Add a meaningful description (optional)'}),
    'citations': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple', 'text':'citations[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
    'tag': forms.RadioSelect(),
    "is_disputed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "is_uncertain" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "expert_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "drb_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    'finalized': forms.CheckboxInput(attrs={'class': 'mb-3', 'checked': True, }),
}

class Long_wallForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Long_wall
        fields = commonfields.copy()
        fields.append('long_wall_from')
        fields.append('long_wall_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['long_wall_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['long_wall_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })


class CopperForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Copper
        fields = commonfields.copy()
        fields.append('copper')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['copper'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class BronzeForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Bronze
        fields = commonfields.copy()
        fields.append('bronze')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['bronze'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class IronForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Iron
        fields = commonfields.copy()
        fields.append('iron')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['iron'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class SteelForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Steel
        fields = commonfields.copy()
        fields.append('steel')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['steel'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class JavelinForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Javelin
        fields = commonfields.copy()
        fields.append('javelin')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['javelin'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class AtlatlForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Atlatl
        fields = commonfields.copy()
        fields.append('atlatl')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['atlatl'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class SlingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Sling
        fields = commonfields.copy()
        fields.append('sling')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['sling'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Self_bowForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Self_bow
        fields = commonfields.copy()
        fields.append('self_bow')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['self_bow'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Composite_bowForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Composite_bow
        fields = commonfields.copy()
        fields.append('composite_bow')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['composite_bow'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CrossbowForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Crossbow
        fields = commonfields.copy()
        fields.append('crossbow')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['crossbow'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Tension_siege_engineForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Tension_siege_engine
        fields = commonfields.copy()
        fields.append('tension_siege_engine')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['tension_siege_engine'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Sling_siege_engineForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Sling_siege_engine
        fields = commonfields.copy()
        fields.append('sling_siege_engine')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['sling_siege_engine'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gunpowder_siege_artilleryForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Gunpowder_siege_artillery
        fields = commonfields.copy()
        fields.append('gunpowder_siege_artillery')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gunpowder_siege_artillery'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Handheld_firearmForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Handheld_firearm
        fields = commonfields.copy()
        fields.append('handheld_firearm')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['handheld_firearm'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class War_clubForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = War_club
        fields = commonfields.copy()
        fields.append('war_club')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['war_club'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Battle_axeForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Battle_axe
        fields = commonfields.copy()
        fields.append('battle_axe')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['battle_axe'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class DaggerForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Dagger
        fields = commonfields.copy()
        fields.append('dagger')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['dagger'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class SwordForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Sword
        fields = commonfields.copy()
        fields.append('sword')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['sword'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class SpearForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Spear
        fields = commonfields.copy()
        fields.append('spear')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['spear'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class PolearmForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polearm
        fields = commonfields.copy()
        fields.append('polearm')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['polearm'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class DogForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Dog
        fields = commonfields.copy()
        fields.append('dog')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['dog'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class DonkeyForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Donkey
        fields = commonfields.copy()
        fields.append('donkey')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['donkey'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class HorseForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Horse
        fields = commonfields.copy()
        fields.append('horse')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['horse'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CamelForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Camel
        fields = commonfields.copy()
        fields.append('camel')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['camel'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class ElephantForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Elephant
        fields = commonfields.copy()
        fields.append('elephant')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['elephant'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Wood_bark_etcForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Wood_bark_etc
        fields = commonfields.copy()
        fields.append('wood_bark_etc')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['wood_bark_etc'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Leather_clothForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Leather_cloth
        fields = commonfields.copy()
        fields.append('leather_cloth')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['leather_cloth'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class ShieldForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Shield
        fields = commonfields.copy()
        fields.append('shield')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['shield'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class HelmetForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Helmet
        fields = commonfields.copy()
        fields.append('helmet')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['helmet'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class BreastplateForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Breastplate
        fields = commonfields.copy()
        fields.append('breastplate')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['breastplate'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Limb_protectionForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Limb_protection
        fields = commonfields.copy()
        fields.append('limb_protection')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['limb_protection'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Scaled_armorForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Scaled_armor
        fields = commonfields.copy()
        fields.append('scaled_armor')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['scaled_armor'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Laminar_armorForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Laminar_armor
        fields = commonfields.copy()
        fields.append('laminar_armor')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['laminar_armor'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Plate_armorForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Plate_armor
        fields = commonfields.copy()
        fields.append('plate_armor')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['plate_armor'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Small_vessels_canoes_etcForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Small_vessels_canoes_etc
        fields = commonfields.copy()
        fields.append('small_vessels_canoes_etc')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['small_vessels_canoes_etc'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Merchant_ships_pressed_into_serviceForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Merchant_ships_pressed_into_service
        fields = commonfields.copy()
        fields.append('merchant_ships_pressed_into_service')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['merchant_ships_pressed_into_service'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Specialized_military_vesselForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Specialized_military_vessel
        fields = commonfields.copy()
        fields.append('specialized_military_vessel')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['specialized_military_vessel'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Settlements_in_a_defensive_positionForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Settlements_in_a_defensive_position
        fields = commonfields.copy()
        fields.append('settlements_in_a_defensive_position')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['settlements_in_a_defensive_position'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Wooden_palisadeForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Wooden_palisade
        fields = commonfields.copy()
        fields.append('wooden_palisade')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['wooden_palisade'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Earth_rampartForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Earth_rampart
        fields = commonfields.copy()
        fields.append('earth_rampart')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['earth_rampart'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class DitchForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Ditch
        fields = commonfields.copy()
        fields.append('ditch')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['ditch'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class MoatForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Moat
        fields = commonfields.copy()
        fields.append('moat')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['moat'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Stone_walls_non_mortaredForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Stone_walls_non_mortared
        fields = commonfields.copy()
        fields.append('stone_walls_non_mortared')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['stone_walls_non_mortared'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Stone_walls_mortaredForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Stone_walls_mortared
        fields = commonfields.copy()
        fields.append('stone_walls_mortared')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['stone_walls_mortared'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Fortified_campForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Fortified_camp
        fields = commonfields.copy()
        fields.append('fortified_camp')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['fortified_camp'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Complex_fortificationForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Complex_fortification
        fields = commonfields.copy()
        fields.append('complex_fortification')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['complex_fortification'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Modern_fortificationForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Modern_fortification
        fields = commonfields.copy()
        fields.append('modern_fortification')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['modern_fortification'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class ChainmailForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Chainmail
        fields = commonfields.copy()
        fields.append('chainmail')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['chainmail'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        