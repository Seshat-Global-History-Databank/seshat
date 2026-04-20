from .models import Us_location, Us_violence_subtype, Us_violence_data_source, Us_violence, Power_transition, Crisis_consequence, Human_sacrifice, External_conflict, Internal_conflict, External_conflict_side, Agricultural_population, Arable_land, Arable_land_per_farmer, Gross_grain_shared_per_agricultural_population, Net_grain_shared_per_agricultural_population, Surplus, Military_expense, Silver_inflow, Silver_stock, Total_population, Gdp_per_capita, Drought_event, Locust_event, Socioeconomic_turmoil_event, Crop_failure_event, Famine_event, Disease_outbreak, Instability_event, Check_choice, Instability_type
import datetime

from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register

from seshat.apps.general.forms import commonlabels, commonfields, commonwidgets, ExpertReviewedForm
from seshat.apps.accounts.models import Seshat_Expert
from seshat.apps.core.forms import ReferenceWithPageForm, BaseReferenceFormSet


#################


############## American Violence

class Us_locationForm(forms.ModelForm):
    """
    Form for creating and updating a US location.
    """
    class Meta:
        """
        :noindex:
        """
        model = Us_location
        fields = '__all__'

class Us_violence_subtypeForm(forms.ModelForm):
    """
    Form for creating and updating a US violence subtype.
    """
    class Meta:
        """
        :noindex:
        """
        model = Us_violence_subtype
        fields = '__all__'

class Us_violence_data_sourceForm(forms.ModelForm):
    """
    Form for creating and updating a US violence data source.
    """
    class Meta:
        """
        :noindex:
        """
        model = Us_violence_data_source
        fields = '__all__'

class Us_violenceForm(forms.ModelForm):
    """
    Form for creating and updating a US violence.
    """
    class Meta:
        """
        :noindex:
        """
        model = Us_violence
        fields = ["violence_date", "violence_type", "violence_subtype", "fatalities", 
                  "location", "url_address", "short_data_source", "source_details", "narrative",]
        widgets = {
            'violence_date': forms.DateInput(attrs={'class': 'form-control  mb-3', 'placeholder':'Ex: 2022-12-14'}),
            'violence_type': forms.Select(attrs={'class': 'form-control  mb-3', }),
            'violence_subtype': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple-violence-subtype', 'text':'violence_subtypes[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
            'fatalities': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),
            'location': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple-location', 'text':'locations[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
            'url_address': forms.TextInput(attrs={'class': 'form-control  mb-3','placeholder': 'Enter a URL'}),
            'short_data_source': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple-short-data-source', 'text':'short_data_sources[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
            'source_details': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 250px', 'placeholder':'Add a narrative (optional)'}),
            'narrative': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 250px', 'placeholder':'Add a narrative (optional)'}),
        }

###########################
class Crisis_consequenceForm(forms.ModelForm):
    """
    Form for creating and updating a crisis consequence.
    """
    class Meta:
        """
        :noindex:
        """
        model = Crisis_consequence
        fields = commonfields.copy()
        fields.append('crisis_case_id')
        fields.append('name')
        fields.append('other_polity')
        fields.append('is_first_100')
        fields.append('decline')
        fields.append('collapse')
        fields.append('epidemic')
        fields.append('downward_mobility')
        fields.append('extermination')
        fields.append('uprising')
        fields.append('revolution')
        fields.append('successful_revolution')
        fields.append('civil_war')
        fields.append('century_plus')
        fields.append('fragmentation')
        fields.append('fragmentation')
        fields.append('capital')
        fields.append('conquest')
        fields.append('assassination')
        fields.append('depose')
        fields.append('constitution')
        fields.append('labor')
        fields.append('unfree_labor')
        fields.append('suffrage')
        fields.append('public_goods')
        fields.append('religion')


        labels = commonlabels.copy()
        labels["is_first_100"] = "<span class='h5'> Is it a <span class='text-primary text-decoration-underline'> first 100 </span> case? </span>"
        labels['polity'] = "<span class='h5 text-teal'> Polity: </span>"
        labels['name'] = "<span class='h5 text-teal'> Crisis Period Name: </span>"
        labels['other_polity'] = "<span class='h5 text-teal'> Other Polity: </span>"
        labels['crisis_case_id'] = "<span class='h5 text-teal'> Crisis Case Name (ID): </span>"
        labels['year_from'] = "<span class='h5 text-teal'> Crisis Start Year: </span>"
        labels['year_to'] = "<span class='h5 text-teal'> Crisis End Year: </span>"
        labels["decline"] = "<span class='h5 text-teal'> Decline: </span>"
        labels["collapse"] = "<span class='h5 text-teal'> Collapse: </span>"
        labels["epidemic"] = "<span class='h5 text-teal'> Epidemic: </span>"
        labels["downward_mobility"] = "<span class='h5 text-teal'> Downward mobility: </span>"
        labels["extermination"] = "<span class='h5 text-teal'> Extermination: </span>"
        labels["uprising"] = "<span class='h5 text-teal'> Uprising: </span>"
        labels["revolution"] = "<span class='h5 text-teal'> Revolution: </span>"
        labels["successful_revolution"] = "<span class='h5 text-teal'> Successful revolution: </span>"
        labels["civil_war"] = "<span class='h5 text-teal'> Civil war: </span>"
        labels["century_plus"] = "<span class='h5 text-teal'> Century plus: </span>"
        labels["fragmentation"] = "<span class='h5 text-teal'> Fragmentation: </span>"
        labels["capital"] = "<span class='h5 text-teal'> Capital: </span>"
        labels["conquest"] = "<span class='h5 text-teal'> Conquest: </span>"
        labels["assassination"] = "<span class='h5 text-teal'> Assassination: </span>"
        labels["depose"] = "<span class='h5 text-teal'> Depose: </span>"
        labels["constitution"] = "<span class='h5 text-teal'> Constitution: </span>"
        labels["labor"] = "<span class='h5 text-teal'> Labor: </span>"
        labels["unfree_labor"] = "<span class='h5 text-teal'> Unfree labor: </span>"
        labels["suffrage"] = "<span class='h5 text-teal'> Suffrage: </span>"
        labels["public_goods"] = "<span class='h5 text-teal'> Public goods: </span>"
        labels["religion"] = "<span class='h5 text-teal'> Religion: </span>"
        labels["description"] = "<span class='h5 text-teal'> Note: </span>"
        #labels["expert_reviewed"] = "&nbsp; Expert Checked?"
        #labels["drb_reviewed"] = "&nbsp; Data Review Board Reviewed?"

        
        widgets = dict(commonwidgets)
        widgets['crisis_case_id'] = forms.TextInput(attrs={'class': 'form-control  mb-1', })
        widgets['name'] = forms.TextInput(attrs={'class': 'form-control  mb-1', })
        widgets['other_polity'] = forms.Select(attrs={'class': 'form-control  mb-1 js-example-basic-single2', 'id': 'id_polity_other',})
        widgets['is_first_100'] = forms.CheckboxInput(attrs={'class': 'mb-3', })
        widgets['decline'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['collapse'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['epidemic'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['downward_mobility'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['extermination'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['uprising'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['revolution'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['successful_revolution'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['civil_war'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['century_plus'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['fragmentation'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['capital'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['conquest'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['assassination'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['depose'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['constitution'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['labor'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['unfree_labor'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['suffrage'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['public_goods'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['religion'] = forms.Select(attrs={'class': 'form-control  mb-1', })
###########################
####################################

class Power_transitionForm(ExpertReviewedForm):
    """
    Form for creating and updating a power transition.
    """
    class Meta:
        """
        :noindex:
        """
        model = Power_transition
        fields = commonfields.copy()
        fields.append('predecessor')
        fields.append('successor') 
        fields.append('name')
        fields.append('culture_group')
        fields.append('reign_number_predecessor')
        fields.append('contested')
        fields.append('overturn')
        fields.append('predecessor_assassination')
        fields.append('intra_elite')
        fields.append('military_revolt')
        fields.append('popular_uprising')
        fields.append('separatist_rebellion')
        fields.append('external_invasion')
        fields.append('external_interference')


        labels = commonlabels.copy()
        labels['polity'] = "<span class='fs-6'> Polity: </span>"
        labels['name'] = "<span class='fs-6'> Conflict Name: </span>"
        labels['predecessor'] = "<span class='fs-6'> Predecessor: </span>"
        labels['successor'] = "<span class='fs-6'> Successor: </span>"
        labels['reign_number_predecessor'] = "<span class='fs-6'> Reign Number (predecessor): </span>"
        labels['culture_group'] = "<span class='fs-6'> Culture Group: </span>"

        labels['year_from'] = "<span class='fs-6'> Start Year (of Predecessor): </span>"
        labels['year_to'] = "<span class='fs-6'> Transition Year: </span>"
        labels["contested"] = "<span class='fs-6'> Contested: </span>"
        labels["overturn"] = "<span class='fs-6'> Overturn: </span>"
        labels["predecessor_assassination"] = "<span class='fs-6'> Predecessor Assassination: </span>"
        labels["intra_elite"] = "<span class='fs-6'> Intra Elite: </span>"
        labels["military_revolt"] = "<span class='fs-6'> Military Revolt: </span>"
        labels["popular_uprising"] = "<span class='fs-6'> Popular Uprising: </span>"
        labels["separatist_rebellion"] = "<span class='fs-6'> Separatist Rebellion: </span>"
        labels["external_invasion"] = "<span class='fs-6'> External Invasion: </span>"
        labels["external_interference"] = "<span class='fs-6'> External Interference: </span>"
        labels["description"] = "<span class='fs-6'> Description: </span>"
        #labels["expert_reviewed"] = "&nbsp; Expert Checked?"
        #labels["drb_reviewed"] = "&nbsp; Data Review Board Reviewed?"

        
        widgets = dict(commonwidgets)
        widgets['predecessor'] = forms.TextInput(attrs={'class': 'form-control  mb-1', })
        widgets['successor'] = forms.TextInput(attrs={'class': 'form-control  mb-1', })
        widgets['reign_number_predecessor'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['culture_group'] = forms.TextInput(attrs={'class': 'form-control  mb-1', })

        widgets['name'] = forms.TextInput(attrs={'class': 'form-control  mb-1', })
        widgets['contested'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['overturn'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['predecessor_assassination'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['intra_elite'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['military_revolt'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['popular_uprising'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['separatist_rebellion'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['external_invasion'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['external_interference'] = forms.Select(attrs={'class': 'form-control  mb-1', })




class CheckChoiceForm(forms.ModelForm):
    class Meta:
        model = Check_choice
        fields = ['name', 'check_description', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'check_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'color': forms.Select(attrs={'class': 'form-select'}),
        }


# class DisabledByNameCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
#     def __init__(self, *args, disabled_names=None, **kwargs):
#         self.disabled_names = [name.lower() for name in (disabled_names or [])]
#         super().__init__(*args, **kwargs)

#     def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
#         option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)
#         if str(label).lower() in self.disabled_names:
#             option['attrs']['disabled'] = 'disabled'
#             option['attrs']['class'] += ' text-muted'
#             option['selected'] = False  # <- always uncheck
#         return option
    
# DISABLED_INST_TYPE_NAMES = ["Military campaign", "Military Mutiny"]  # example names to disable


class Instability_eventForm(ExpertReviewedForm):
    is_macro_event = forms.TypedChoiceField(
        choices=((False, 'False'), (True, 'True')),
        coerce=lambda value: value in (True, 'True', 'true', '1', 1),
        empty_value=False,
        required=True,
        label='Macroevent',
        widget=forms.Select(attrs={'class': 'form-control mb-1'}),
    )

    #formset = CommentPartFormSet(prefix='commentpart')  # Include formset
    #formset.management_form  # Ensure the management form is included
    inst_type = forms.ModelMultipleChoiceField(
        queryset=Instability_type.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input text-danger'}),
        label='Event Type(s):',
        required=False  # Since it's blank=True in the model
    )
    ra_check = forms.ModelMultipleChoiceField(
        queryset=Check_choice.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input text-danger'}),
        required=False  # Since it's blank=True in the model
    )



    class Meta:

        model = Instability_event
        fields = commonfields.copy()
        fields.append('inst_intensity')
        fields.append('inst_extent') 
        fields.append('name')
        fields.append('is_macro_event')
        #fields.append('llm_inst_intensity')
        #fields.append('llm_inst_extent') 
        #fields.append('llm_name')
        fields.append('llm_description')
        fields.append('general_cot')
        fields.append('classification_cot') 
        fields.append('sorokin_rationale')
        fields.append('real_event_check')
        #fields.append('llm_real_event_check')
        fields.append('inst_type')
        fields.append('ra_check')


        

        labels = commonlabels.copy()
        labels['llm_description'] = "<span class='fs-6'> LLM Description: </span>"
        labels['name'] = "Event Name"
        labels['is_macro_event'] = "Macroevent"
        labels['inst_extent'] = "<span class='fs-6'> Extent: </span>"
        labels['inst_intensity'] = "<span class='fs-6'> Intensity: </span>"
        labels['general_cot'] = "<span class='fs-6'> General Chain of Thought: </span>"
        labels['classification_cot'] = "<span class='fs-6'> Classification Chain of Thought </span>"
        labels['sorokin_rationale'] = "<span class='fs-6'> Sorokin Rationale </span>"
        labels['real_event_check'] = "<span class='fs-6'> Data Point </span>"
        labels['ra_check'] = "<span class='fs-6'> RA Check: </span>"
        labels['inst_type'] = "<span class='fs-6'>Event Type</span>"


        widgets = dict(commonwidgets)
        widgets['inst_extent'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['inst_intensity'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        widgets['llm_description'] = forms.Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 140px'})
        widgets['name'] = forms.TextInput(attrs={'class': 'form-control  mb-1', })
        widgets['general_cot'] = forms.Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 150px', 'readonly': "True"})
        widgets['classification_cot'] = forms.Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 150px', 'readonly': "True"})
        widgets['sorokin_rationale'] = forms.Textarea(attrs={'class': 'form-control  mb-3',  'style': 'height: 100px'})
        widgets['real_event_check'] = forms.Select(attrs={'class': 'form-control  mb-1', })
 
        widgets['inst_type'] = forms.CheckboxSelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple-inst-type', 'text':'inst_types[]' , 'style': 'height: 340px', 'multiple': 'multiple'})
        widgets['ra_check'] = forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})  
        #widgets['inst_llm_ref'] = forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})   

    # def save(self, commit=True):
    #     """Override save() to remove unchecked items from inst_type."""
    #     instance = super().save(commit=False)  # Get the model instance without saving yet

    #     # Get the new selection from the form
    #     new_inst_types = self.cleaned_data.get('inst_type', [])
    #     print(new_inst_types)
    #     #new_ra_checks = self.cleaned_data.get('ra_check', [])
    #     #print(new_ra_checks)

    #     if instance.pk:  # Ensure the instance already exists in the DB
    #         # Remove all previously selected inst_type values that are no longer checked
    #         instance.inst_type.set(new_inst_types)
    #         #instance.ra_check.set(new_ra_checks)


    #     if commit:
    #         instance.save()
    #         self.save_m2m()  # Save many-to-many relations

    #     return instance


class Human_sacrificeForm(ExpertReviewedForm):
    """
    Form for creating and updating a human sacrifice.
    """
    class Meta:
        """
        :noindex:
        """
        model = Human_sacrifice
        fields = commonfields.copy()
        fields.append('human_sacrifice')
        #fields.append('comment')
        #fields.append('is_disputed')
        #fields.append('expert_reviewed')
        #fields.append('drb_reviewed')

        labels = commonlabels.copy()
        #labels["comment"] = "&nbsp; <b> com id </b>"
        #labels["expert_reviewed"] = "&nbsp; Expert Checked?"
        #labels["drb_reviewed"] = "&nbsp; Data Review Board Reviewed?"

        
        widgets = dict(commonwidgets)
        widgets['sub_category'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['human_sacrifice'] = forms.Select(attrs={'class': 'form-control  mb-1', })
        #widgets['comment'] = forms.HiddenInput()

        #widgets["is_disputed"] = forms.CheckboxInput(attrs={'class': 'mb-3', })
        #widgets["expert_reviewed"] = forms.CheckboxInput(attrs={'class': 'mb-3', })
        #widgets["drb_reviewed"] = forms.CheckboxInput(attrs={'class': 'mb-3', })
        

class External_conflictForm(forms.ModelForm):
    """
    Form for creating and updating an external conflict.
    """
    class Meta:
        """
        :noindex:
        """
        model = External_conflict
        fields = commonfields.copy()
        fields.append('conflict_name')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['conflict_name'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        

class Internal_conflictForm(forms.ModelForm):
    """
    Form for creating and updating an internal conflict.
    """
    class Meta:
        """
        :noindex:
        """
        model = Internal_conflict
        fields = commonfields.copy()
        fields.append('conflict')
        fields.append('expenditure')
        fields.append('leader')
        fields.append('casualty')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['conflict'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        widgets['expenditure'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['leader'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        widgets['casualty'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class External_conflict_sideForm(forms.ModelForm):
    """
    Side form for creating and updating an external conflict.
    """
    class Meta:
        """
        :noindex:
        """
        model = External_conflict_side
        fields = commonfields.copy()
        fields.append('conflict_id')
        fields.append('expenditure')
        fields.append('leader')
        fields.append('casualty')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['conflict_id'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['expenditure'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['leader'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        widgets['casualty'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Agricultural_populationForm(forms.ModelForm):
    """
    Form for creating and updating an agricultural population.
    """
    class Meta:
        """
        :noindex:
        """
        model = Agricultural_population
        fields = commonfields.copy()
        fields.append('agricultural_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['agricultural_population'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Arable_landForm(forms.ModelForm):
    """
    Form for creating and updating an arable land.
    """
    class Meta:
        """
        :noindex:
        """
        model = Arable_land
        fields = commonfields.copy()
        fields.append('arable_land')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['arable_land'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Arable_land_per_farmerForm(forms.ModelForm):
    """
    Form for creating and updating an arable land per farmer.
    """
    class Meta:
        """
        :noindex:
        """
        model = Arable_land_per_farmer
        fields = commonfields.copy()
        fields.append('arable_land_per_farmer')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['arable_land_per_farmer'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Gross_grain_shared_per_agricultural_populationForm(forms.ModelForm):
    """
    Form for creating and updating a gross grain shared per agricultural population.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gross_grain_shared_per_agricultural_population
        fields = commonfields.copy()
        fields.append('gross_grain_shared_per_agricultural_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gross_grain_shared_per_agricultural_population'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Net_grain_shared_per_agricultural_populationForm(forms.ModelForm):
    """
    Form for creating and updating a net grain shared per agricultural population.
    """
    class Meta:
        """
        :noindex:
        """
        model = Net_grain_shared_per_agricultural_population
        fields = commonfields.copy()
        fields.append('net_grain_shared_per_agricultural_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['net_grain_shared_per_agricultural_population'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class SurplusForm(forms.ModelForm):
    """
    Form for creating and updating a surplus.
    """
    class Meta:
        """
        :noindex:
        """
        model = Surplus
        fields = commonfields.copy()
        fields.append('surplus')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['surplus'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Military_expenseForm(forms.ModelForm):
    """
    Form for creating and updating a military expense.
    """
    class Meta:
        """
        :noindex:
        """
        model = Military_expense
        fields = commonfields.copy()
        fields.append('conflict')
        fields.append('expenditure')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['conflict'] = forms.TextInput(attrs={'class': 'form-control  mb-3', })
        widgets['expenditure'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Silver_inflowForm(forms.ModelForm):
    """
    Form for creating and updating a silver inflow.
    """
    class Meta:
        """
        :noindex:
        """
        model = Silver_inflow
        fields = commonfields.copy()
        fields.append('silver_inflow')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['silver_inflow'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Silver_stockForm(forms.ModelForm):
    """
    Form for creating and updating a silver stock.
    """
    class Meta:
        """
        :noindex:
        """
        model = Silver_stock
        fields = commonfields.copy()
        fields.append('silver_stock')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['silver_stock'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Total_populationForm(forms.ModelForm):
    """
    Form for creating and updating a total population.
    """
    class Meta:
        """
        :noindex:
        """
        model = Total_population
        fields = commonfields.copy()
        fields.append('total_population')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['total_population'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Gdp_per_capitaForm(forms.ModelForm):
    """
    Form for creating and updating a GDP per capita.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gdp_per_capita
        fields = commonfields.copy()
        fields.append('gdp_per_capita')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['gdp_per_capita'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Drought_eventForm(forms.ModelForm):
    """
    Form for creating and updating a drought event.
    """
    class Meta:
        """
        :noindex:
        """
        model = Drought_event
        fields = commonfields.copy()
        fields.append('drought_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['drought_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Locust_eventForm(forms.ModelForm):
    """
    Form for creating and updating a locust event.
    """
    class Meta:
        """
        :noindex:
        """
        model = Locust_event
        fields = commonfields.copy()
        fields.append('locust_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['locust_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Socioeconomic_turmoil_eventForm(forms.ModelForm):
    """
    Form for creating and updating a socioeconomic turmoil event.
    """
    class Meta:
        """
        :noindex:
        """
        model = Socioeconomic_turmoil_event
        fields = commonfields.copy()
        fields.append('socioeconomic_turmoil_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['socioeconomic_turmoil_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Crop_failure_eventForm(forms.ModelForm):
    """
    Form for creating and updating a crop failure event.
    """
    class Meta:
        """
        :noindex:
        """
        model = Crop_failure_event
        fields = commonfields.copy()
        fields.append('crop_failure_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['crop_failure_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Famine_eventForm(forms.ModelForm):
    """
    Form for creating and updating a famine event.
    """
    class Meta:
        """
        :noindex:
        """
        model = Famine_event
        fields = commonfields.copy()
        fields.append('famine_event')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['famine_event'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Disease_outbreakForm(forms.ModelForm):
    """
    Form for creating and updating a disease outbreak.
    """
    class Meta:
        """
        :noindex:
        """
        model = Disease_outbreak
        fields = commonfields.copy()
        fields.append('longitude')
        fields.append('latitude')
        fields.append('elevation')
        fields.append('sub_category')
        fields.append('magnitude')
        fields.append('duration')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['longitude'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['latitude'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['elevation'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['sub_category'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['magnitude'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['duration'] = forms.Select(attrs={'class': 'form-control  mb-3', })
