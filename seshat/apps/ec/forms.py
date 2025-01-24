import datetime

from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from seshat.apps.general.forms import commonlabels, commonfields, commonwidgets, ExpertReviewedForm
from seshat.apps.accounts.models import Seshat_Expert
from seshat.apps.core.models import Tags, Prec_met_instance


from django.utils.safestring import mark_safe

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register

from .models import Lux_precious_metal, Luxury_fabrics, Luxury_manufactured_goods, Luxury_spices_incense_and_dyes, Luxury_drink_alcohol, Luxury_glass_goods, Lux_fine_ceramic_wares, Lux_precious_stone, Lux_statuary, Luxury_food, Other_luxury_personal_items



class Lux_precious_metalForm(ExpertReviewedForm):

    class Meta:
        model = Lux_precious_metal
        fields = commonfields.copy()
        fields.append('name')
        fields.append('coded_value')
        fields.append('which_metals')
        fields.append('place_of_provenance_pol')
        fields.append('place_of_provenance_str')
        fields.append('ruler_consumption')
        fields.append('ruler_consumption_tag')
        fields.append('elite_consumption')
        fields.append('elite_consumption_tag')
        fields.append('common_people_consumption')
        fields.append('common_people_consumption_tag')

        labels = commonlabels
        labels['which_metals'] = ''  # Set the label for `which_metals`
        labels['coded_value'] = 'Coded Value (abs / pres / etc.)'  # Set the label for `which_metals`

        
        widgets = dict(commonwidgets)
        widgets['name'] = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter instance name'})
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['place_of_provenance_str'] = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the place...'})
        widgets['ruler_consumption'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['ruler_consumption_tag'] = forms.RadioSelect(choices=Tags)
        widgets['elite_consumption'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['elite_consumption_tag'] = forms.RadioSelect()
        widgets['common_people_consumption'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['common_people_consumption_tag'] = forms.RadioSelect()
        widgets['place_of_provenance_pol'] = forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple', 'text':'place_of_provenance_pols[]' , 'style': 'height: 340px', 'multiple': 'multiple'})

    which_metals = forms.ModelMultipleChoiceField(
        queryset=Prec_met_instance.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input checkbox-majid'}),
        required=False,  # Set this to `True` if the field should be mandatory
        label='Which Metals?'  # Set the label for this field explicitly

    )


# Reusable fields for forms
COMMON_FIELDS_LUX = [
    'name', 'coded_value', 'place_of_provenance_pol',
    'place_of_provenance_str', 'ruler_consumption', 'ruler_consumption_tag',
    'elite_consumption', 'elite_consumption_tag', 'common_people_consumption',
    'common_people_consumption_tag',
]

# Reusable labels for forms
COMMON_LABELS_LUX = {
    'coded_value': 'Coded Value (abs / pres / etc.)',
}

# Reusable widgets for forms
COMMON_WIDGETS_LUX = {
    'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter instance name'}),
    'coded_value': forms.Select(attrs={'class': 'form-control mb-3'}),
    'place_of_provenance_str': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the place...'}),
    'ruler_consumption': forms.Select(attrs={'class': 'form-control mb-3'}),
    'ruler_consumption_tag': forms.RadioSelect(choices=Tags),
    'elite_consumption': forms.Select(attrs={'class': 'form-control mb-3'}),
    'elite_consumption_tag': forms.RadioSelect(),
    'common_people_consumption': forms.Select(attrs={'class': 'form-control mb-3'}),
    'common_people_consumption_tag': forms.RadioSelect(),
    'place_of_provenance_pol': forms.SelectMultiple(
        attrs={
            'class': 'form-control mb-3 js-states js-example-basic-multiple',
            'text': 'place_of_provenance_pols[]',
            'style': 'height: 340px',
            'multiple': 'multiple',
        }
    ),
}


class BaseReusableForm(ExpertReviewedForm):
    class Meta:
        fields = COMMON_FIELDS_LUX + commonfields
        labels = {**COMMON_LABELS_LUX, **commonlabels} 
        widgets =  {**COMMON_WIDGETS_LUX, **commonwidgets}

class LuxPreciousMetalForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Lux_precious_metal


class Luxury_fabricsForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Luxury_fabrics  
    

class Luxury_manufactured_goodsForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Luxury_manufactured_goods  
    

class Luxury_spices_incense_and_dyesForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Luxury_spices_incense_and_dyes  
    

class Luxury_drink_alcoholForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Luxury_drink_alcohol  
    

class Luxury_glass_goodsForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Luxury_glass_goods  
    

class Lux_fine_ceramic_waresForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Lux_fine_ceramic_wares  
    

class Lux_precious_stoneForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Lux_precious_stone  
    

class Lux_statuaryForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Lux_statuary  
    

class Luxury_foodForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Luxury_food  
    

class Other_luxury_personal_itemsForm(BaseReusableForm):
    class Meta(BaseReusableForm.Meta):
        model = Other_luxury_personal_items  
