from .models import Polity_research_assistant, Polity_utm_zone, Polity_original_name, Polity_alternative_name, Polity_peak_years, Polity_duration, Polity_degree_of_centralization, Polity_suprapolity_relations, Polity_capital, Polity_language, Polity_linguistic_family, Polity_language_genus, Polity_religion_genus, Polity_religion_family, Polity_religion, Polity_relationship_to_preceding_entity, Polity_preceding_entity, Polity_succeeding_entity, Polity_supracultural_entity, Polity_scale_of_supracultural_interaction, Polity_alternate_religion_genus, Polity_alternate_religion_family, Polity_alternate_religion, Polity_expert, Polity_editor, Polity_religious_tradition
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
    "expert_reviewed" : "&nbsp; Expert Checked?",
    "drb_reviewed" : "&nbsp; Data Review Board Reviewed?",
    'citations': 'Add one or more Citations',
    'finalized': 'This piece of data is verified.',
}

commonfields = ['polity', 'year_from', 'year_to',
                'description', 'tag', 'is_disputed', 'expert_reviewed', 'drb_reviewed', 'finalized', 'citations']

commonwidgets = {
    'polity': forms.Select(attrs={'class': 'form-control  mb-3', }),
    'year_from': forms.NumberInput(attrs={'class': 'form-control  mb-3',}),
    'year_to': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),
    'description': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 140px', 'placeholder':'Add a meaningful description (optional)'}),
    'citations': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple', 'text':'citations[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
    'tag': forms.RadioSelect(),
    "is_disputed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "expert_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "drb_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    'finalized': forms.CheckboxInput(attrs={'class': 'mb-3', 'checked': True, }),
}

class Polity_research_assistantForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_research_assistant
        fields = commonfields.copy()
        fields.append('polity_ra')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['polity_ra'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_utm_zoneForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_utm_zone
        fields = commonfields.copy()
        fields.append('utm_zone')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['utm_zone'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_original_nameForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_original_name
        fields = commonfields.copy()
        fields.append('original_name')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['original_name'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_alternative_nameForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_alternative_name
        fields = commonfields.copy()
        fields.append('alternative_name')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['alternative_name'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_peak_yearsForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_peak_years
        fields = commonfields.copy()
        fields.append('peak_year_from')
        fields.append('peak_year_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['peak_year_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['peak_year_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_durationForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_duration
        fields = commonfields.copy()
        fields.append('polity_year_from')
        fields.append('polity_year_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['polity_year_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['polity_year_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_degree_of_centralizationForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_degree_of_centralization
        fields = commonfields.copy()
        fields.append('degree_of_centralization')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['degree_of_centralization'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_suprapolity_relationsForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_suprapolity_relations
        fields = commonfields.copy()
        fields.append('supra_polity_relations')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['supra_polity_relations'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_capitalForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_capital
        fields = commonfields.copy()
        fields.append('capital')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['capital'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_languageForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_language
        fields = commonfields.copy()
        fields.append('language')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['language'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_linguistic_familyForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_linguistic_family
        fields = commonfields.copy()
        fields.append('linguistic_family')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['linguistic_family'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_language_genusForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_language_genus
        fields = commonfields.copy()
        fields.append('language_genus')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['language_genus'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_religion_genusForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_religion_genus
        fields = commonfields.copy()
        fields.append('religion_genus')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['religion_genus'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_religion_familyForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_religion_family
        fields = commonfields.copy()
        fields.append('religion_family')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['religion_family'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_religionForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_religion
        fields = commonfields.copy()
        fields.append('religion')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['religion'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_relationship_to_preceding_entityForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_relationship_to_preceding_entity
        fields = commonfields.copy()
        fields.append('relationship_to_preceding_entity')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['relationship_to_preceding_entity'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_preceding_entityForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_preceding_entity
        fields = commonfields.copy()
        fields.append('preceding_entity')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['preceding_entity'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_succeeding_entityForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_succeeding_entity
        fields = commonfields.copy()
        fields.append('succeeding_entity')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['succeeding_entity'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_supracultural_entityForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_supracultural_entity
        fields = commonfields.copy()
        fields.append('supracultural_entity')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['supracultural_entity'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_scale_of_supracultural_interactionForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_scale_of_supracultural_interaction
        fields = commonfields.copy()
        fields.append('scale_from')
        fields.append('scale_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['scale_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['scale_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_alternate_religion_genusForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_alternate_religion_genus
        fields = commonfields.copy()
        fields.append('alternate_religion_genus')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['alternate_religion_genus'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_alternate_religion_familyForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_alternate_religion_family
        fields = commonfields.copy()
        fields.append('alternate_religion_family')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['alternate_religion_family'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_alternate_religionForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_alternate_religion
        fields = commonfields.copy()
        fields.append('alternate_religion')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['alternate_religion'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_expertForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_expert
        fields = commonfields.copy()
        fields.append('expert')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['expert'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_editorForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_editor
        fields = commonfields.copy()
        fields.append('editor')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['editor'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_religious_traditionForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_religious_tradition
        fields = commonfields.copy()
        fields.append('religious_tradition')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['religious_tradition'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        