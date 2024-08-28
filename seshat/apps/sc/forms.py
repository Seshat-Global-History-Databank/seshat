from django import forms
from django.forms.widgets import Textarea

from .models import Ra, Polity_territory, Polity_population, Population_of_the_largest_settlement, Settlement_hierarchy, Administrative_level, Religious_level, Military_level, Professional_military_officer, Professional_soldier, Professional_priesthood, Full_time_bureaucrat, Examination_system, Merit_promotion, Specialized_government_building, Formal_legal_code, Judge, Court, Professional_lawyer, Irrigation_system, Drinking_water_supply_system, Market, Food_storage_site, Road, Bridge, Canal, Port, Mines_or_quarry, Mnemonic_device, Nonwritten_record, Written_record, Script, Non_phonetic_writing, Phonetic_alphabetic_writing, Lists_tables_and_classification, Calendar, Sacred_text, Religious_literature, Practical_literature, History, Philosophy, Scientific_literature, Fiction, Article, Token, Precious_metal, Foreign_coin, Indigenous_coin, Paper_currency, Courier, Postal_station, General_postal_service, Communal_building, Utilitarian_public_building, Other_utilitarian_public_building, Symbolic_building, Entertainment_building, Knowledge_or_information_building, Special_purpose_site, Ceremonial_site, Burial_site, Trading_emporia, Enclosure, Length_measurement_system, Area_measurement_system, Volume_measurement_system, Weight_measurement_system, Time_measurement_system, Geometrical_measurement_system, Other_measurement_system, Debt_and_credit_structure, Store_of_wealth, Source_of_support, Occupational_complexity, Special_purpose_house, Other_special_purpose_site, Largest_communication_distance, Fastest_individual_communication


commonlabels = {
    'polity': '&nbsp;<b>Polity:</b>',
    'year_from': '&nbsp;<b>Start Year:</b>',
    'year_to': '&nbsp;<b>End Year:</b>',
    'tag': 'Confidence Level',
    'description': "&nbsp; <b> Description: </b>",
    "is_disputed" : "&nbsp; <b> There is a Dispute? </b>",
    "is_uncertain" : "&nbsp; <b> There is Uncertainty? </b>",
    "expert_reviewed" : "&nbsp; <b> Expert Checked? </b>",
    "drb_reviewed" : "&nbsp; Data Review Board Reviewed?",
    'citations': 'Add one or more Citations',
    'finalized': 'This piece of data is verified.',
}

commonfields = ['polity', 'year_from', 'year_to',
                'description', 'tag', 'is_disputed', 'is_uncertain', 'expert_reviewed', 'drb_reviewed', 'finalized', 'citations']

commonwidgets = {
    'polity': forms.Select(attrs={'class': 'form-control  mb-3 js-example-basic-single', 'id': 'id_polity', 'name': 'polity'}),
    'year_from': forms.NumberInput(attrs={'class': 'form-control  mb-3',}),
    'year_to': forms.NumberInput(attrs={'class': 'form-control  mb-3', }),
    'description': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 240px; line-height: 1.2;', 'placeholder':'Add a meaningful description (optional)\nNote: USe §REF§ opening and closing tags to include citations to the description.\nExample: §REF§Chadwick, J. 1976. The Mycenaean World, Cambridge, p.78.§REF§.'}),
    'citations': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple', 'text':'citations[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
    'tag': forms.RadioSelect(),
    "is_disputed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "is_uncertain" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "expert_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "drb_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    'finalized': forms.CheckboxInput(attrs={'class': 'mb-3', 'checked': True, }),
}

class RaForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Ra
        fields = commonfields.copy()
        fields.append('sc_ra')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['sc_ra'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Polity_territoryForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_territory
        fields = commonfields.copy()
        fields.append('polity_territory_from')
        fields.append('polity_territory_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['polity_territory_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['polity_territory_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Polity_populationForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Polity_population
        fields = commonfields.copy()
        fields.append('polity_population_from')
        fields.append('polity_population_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['polity_population_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['polity_population_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Population_of_the_largest_settlementForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Population_of_the_largest_settlement
        fields = commonfields.copy()
        fields.append('population_of_the_largest_settlement_from')
        fields.append('population_of_the_largest_settlement_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['population_of_the_largest_settlement_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['population_of_the_largest_settlement_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Settlement_hierarchyForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Settlement_hierarchy
        fields = commonfields.copy()
        fields.append('settlement_hierarchy_from')
        fields.append('settlement_hierarchy_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['settlement_hierarchy_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['settlement_hierarchy_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Administrative_levelForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Administrative_level
        fields = commonfields.copy()
        fields.append('administrative_level_from')
        fields.append('administrative_level_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['administrative_level_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['administrative_level_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Religious_levelForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Religious_level
        fields = commonfields.copy()
        fields.append('religious_level_from')
        fields.append('religious_level_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['religious_level_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['religious_level_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Military_levelForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Military_level
        fields = commonfields.copy()
        fields.append('military_level_from')
        fields.append('military_level_to')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['military_level_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['military_level_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        

class Professional_military_officerForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Professional_military_officer
        fields = commonfields.copy()
        fields.append('professional_military_officer')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['professional_military_officer'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Professional_soldierForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Professional_soldier
        fields = commonfields.copy()
        fields.append('professional_soldier')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['professional_soldier'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Professional_priesthoodForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Professional_priesthood
        fields = commonfields.copy()
        fields.append('professional_priesthood')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['professional_priesthood'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Full_time_bureaucratForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Full_time_bureaucrat
        fields = commonfields.copy()
        fields.append('full_time_bureaucrat')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['full_time_bureaucrat'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Examination_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Examination_system
        fields = commonfields.copy()
        fields.append('examination_system')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['examination_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Merit_promotionForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Merit_promotion
        fields = commonfields.copy()
        fields.append('merit_promotion')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['merit_promotion'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Specialized_government_buildingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Specialized_government_building
        fields = commonfields.copy()
        fields.append('specialized_government_building')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['specialized_government_building'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Formal_legal_codeForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Formal_legal_code
        fields = commonfields.copy()
        fields.append('formal_legal_code')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['formal_legal_code'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class JudgeForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Judge
        fields = commonfields.copy()
        fields.append('judge')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['judge'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CourtForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Court
        fields = commonfields.copy()
        fields.append('court')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['court'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Professional_lawyerForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Professional_lawyer
        fields = commonfields.copy()
        fields.append('professional_lawyer')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['professional_lawyer'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Irrigation_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Irrigation_system
        fields = commonfields.copy()
        fields.append('irrigation_system')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['irrigation_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Drinking_water_supply_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Drinking_water_supply_system
        fields = commonfields.copy()
        fields.append('drinking_water_supply_system')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['drinking_water_supply_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class MarketForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Market
        fields = commonfields.copy()
        fields.append('market')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['market'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Food_storage_siteForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Food_storage_site
        fields = commonfields.copy()
        fields.append('food_storage_site')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['food_storage_site'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class RoadForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Road
        fields = commonfields.copy()
        fields.append('road')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['road'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class BridgeForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Bridge
        fields = commonfields.copy()
        fields.append('bridge')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['bridge'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CanalForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Canal
        fields = commonfields.copy()
        fields.append('canal')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['canal'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class PortForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Port
        fields = commonfields.copy()
        fields.append('port')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['port'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Mines_or_quarryForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Mines_or_quarry
        fields = commonfields.copy()
        fields.append('mines_or_quarry')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['mines_or_quarry'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Mnemonic_deviceForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Mnemonic_device
        fields = commonfields.copy()
        fields.append('mnemonic_device')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['mnemonic_device'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Nonwritten_recordForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Nonwritten_record
        fields = commonfields.copy()
        fields.append('nonwritten_record')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['nonwritten_record'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Written_recordForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Written_record
        fields = commonfields.copy()
        fields.append('written_record')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['written_record'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class ScriptForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Script
        fields = commonfields.copy()
        fields.append('script')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['script'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Non_phonetic_writingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Non_phonetic_writing
        fields = commonfields.copy()
        fields.append('non_phonetic_writing')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['non_phonetic_writing'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Phonetic_alphabetic_writingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Phonetic_alphabetic_writing
        fields = commonfields.copy()
        fields.append('phonetic_alphabetic_writing')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['phonetic_alphabetic_writing'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Lists_tables_and_classificationForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Lists_tables_and_classification
        fields = commonfields.copy()
        fields.append('lists_tables_and_classification')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['lists_tables_and_classification'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CalendarForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Calendar
        fields = commonfields.copy()
        fields.append('calendar')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['calendar'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Sacred_textForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Sacred_text
        fields = commonfields.copy()
        fields.append('sacred_text')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['sacred_text'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Religious_literatureForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Religious_literature
        fields = commonfields.copy()
        fields.append('religious_literature')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['religious_literature'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Practical_literatureForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Practical_literature
        fields = commonfields.copy()
        fields.append('practical_literature')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['practical_literature'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class HistoryForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = History
        fields = commonfields.copy()
        fields.append('history')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['history'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class PhilosophyForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Philosophy
        fields = commonfields.copy()
        fields.append('philosophy')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['philosophy'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Scientific_literatureForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Scientific_literature
        fields = commonfields.copy()
        fields.append('scientific_literature')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['scientific_literature'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class FictionForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Fiction
        fields = commonfields.copy()
        fields.append('fiction')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['fiction'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class ArticleForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Article
        fields = commonfields.copy()
        fields.append('article')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['article'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class TokenForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Token
        fields = commonfields.copy()
        fields.append('token')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['token'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Precious_metalForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Precious_metal
        fields = commonfields.copy()
        fields.append('precious_metal')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['precious_metal'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Foreign_coinForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Foreign_coin
        fields = commonfields.copy()
        fields.append('foreign_coin')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['foreign_coin'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Indigenous_coinForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Indigenous_coin
        fields = commonfields.copy()
        fields.append('indigenous_coin')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['indigenous_coin'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Paper_currencyForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Paper_currency
        fields = commonfields.copy()
        fields.append('paper_currency')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['paper_currency'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class CourierForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Courier
        fields = commonfields.copy()
        fields.append('courier')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['courier'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Postal_stationForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Postal_station
        fields = commonfields.copy()
        fields.append('postal_station')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['postal_station'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class General_postal_serviceForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = General_postal_service
        fields = commonfields.copy()
        fields.append('general_postal_service')
        labels = commonlabels
        
        widgets = dict(commonwidgets)
        widgets['general_postal_service'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

# NEW SC vars
class Communal_buildingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Communal_building
        fields = commonfields.copy()
        fields.append('communal_building')
        labels = commonlabels

        labels['communal_building'] = "&nbsp;<b> Communal Building: </b>"
        
        widgets = dict(commonwidgets)
        widgets['communal_building'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        
class Utilitarian_public_buildingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Utilitarian_public_building
        fields = commonfields.copy()
        fields.append('utilitarian_public_building')
        labels = commonlabels

        labels['utilitarian_public_building'] = "&nbsp;<b> Utilitarian Public Building: </b>"
        
        widgets = dict(commonwidgets)
        widgets['utilitarian_public_building'] = forms.Select(attrs={'class': 'form-control  mb-3', })

class Other_utilitarian_public_buildingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Other_utilitarian_public_building
        fields = commonfields.copy()
        fields.append('other_utilitarian_public_building')
        labels = commonlabels

        labels['other_utilitarian_public_building'] = "&nbsp;<b> Other Utilitarian Public Building: </b>"
        
        widgets = dict(commonwidgets)
        widgets['other_utilitarian_public_building'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Symbolic_buildingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Symbolic_building
        fields = commonfields.copy()
        fields.append('symbolic_building')
        labels = commonlabels

        labels['symbolic_building'] = "&nbsp;<b> Symbolic Building: </b>"
        
        widgets = dict(commonwidgets)
        widgets['symbolic_building'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Entertainment_buildingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Entertainment_building
        fields = commonfields.copy()
        fields.append('entertainment_building')
        labels = commonlabels

        labels['entertainment_building'] = "&nbsp;<b> Entertainment Building: </b>"
        
        widgets = dict(commonwidgets)
        widgets['entertainment_building'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Knowledge_or_information_buildingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Knowledge_or_information_building
        fields = commonfields.copy()
        fields.append('knowledge_or_information_building')
        labels = commonlabels

        labels['knowledge_or_information_building'] = "&nbsp;<b> Knowledge Or Information Building: </b>"
        
        widgets = dict(commonwidgets)
        widgets['knowledge_or_information_building'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Special_purpose_siteForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Special_purpose_site
        fields = commonfields.copy()
        fields.append('special_purpose_site')
        labels = commonlabels

        labels['special_purpose_site'] = "&nbsp;<b> Special Purpose Site: </b>"
        
        widgets = dict(commonwidgets)
        widgets['special_purpose_site'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Ceremonial_siteForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Ceremonial_site
        fields = commonfields.copy()
        fields.append('ceremonial_site')
        labels = commonlabels

        labels['ceremonial_site'] = "&nbsp;<b> Ceremonial Site: </b>"
        
        widgets = dict(commonwidgets)
        widgets['ceremonial_site'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Burial_siteForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Burial_site
        fields = commonfields.copy()
        fields.append('burial_site')
        labels = commonlabels

        labels['burial_site'] = "&nbsp;<b> Burial Site: </b>"
        
        widgets = dict(commonwidgets)
        widgets['burial_site'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Trading_emporiaForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Trading_emporia
        fields = commonfields.copy()
        fields.append('trading_emporia')
        labels = commonlabels

        labels['trading_emporia'] = "&nbsp;<b> Trading Emporia: </b>"
        
        widgets = dict(commonwidgets)
        widgets['trading_emporia'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class EnclosureForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Enclosure
        fields = commonfields.copy()
        fields.append('enclosure')
        labels = commonlabels

        labels['enclosure'] = "&nbsp;<b> Enclosure: </b>"
        
        widgets = dict(commonwidgets)
        widgets['enclosure'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Length_measurement_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Length_measurement_system
        fields = commonfields.copy()
        fields.append('length_measurement_system')
        labels = commonlabels

        labels['length_measurement_system'] = "&nbsp;<b> Length Measurement System: </b>"
        
        widgets = dict(commonwidgets)
        widgets['length_measurement_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Area_measurement_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Area_measurement_system
        fields = commonfields.copy()
        fields.append('area_measurement_system')
        labels = commonlabels

        labels['area_measurement_system'] = "&nbsp;<b> Area Measurement System: </b>"
        
        widgets = dict(commonwidgets)
        widgets['area_measurement_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Volume_measurement_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Volume_measurement_system
        fields = commonfields.copy()
        fields.append('volume_measurement_system')
        labels = commonlabels

        labels['volume_measurement_system'] = "&nbsp;<b> Volume Measurement System: </b>"
        
        widgets = dict(commonwidgets)
        widgets['volume_measurement_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Weight_measurement_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Weight_measurement_system
        fields = commonfields.copy()
        fields.append('weight_measurement_system')
        labels = commonlabels

        labels['weight_measurement_system'] = "&nbsp;<b> Weight Measurement System: </b>"
        
        widgets = dict(commonwidgets)
        widgets['weight_measurement_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Time_measurement_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Time_measurement_system
        fields = commonfields.copy()
        fields.append('time_measurement_system')
        labels = commonlabels

        labels['time_measurement_system'] = "&nbsp;<b> Time Measurement System: </b>"
        
        widgets = dict(commonwidgets)
        widgets['time_measurement_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Geometrical_measurement_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Geometrical_measurement_system
        fields = commonfields.copy()
        fields.append('geometrical_measurement_system')
        labels = commonlabels

        labels['geometrical_measurement_system'] = "&nbsp;<b> Geometrical Measurement System: </b>"
        
        widgets = dict(commonwidgets)
        widgets['geometrical_measurement_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Other_measurement_systemForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Other_measurement_system
        fields = commonfields.copy()
        fields.append('other_measurement_system')
        labels = commonlabels

        labels['other_measurement_system'] = "&nbsp;<b> Other Measurement System: </b>"
        
        widgets = dict(commonwidgets)
        widgets['other_measurement_system'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Debt_and_credit_structureForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Debt_and_credit_structure
        fields = commonfields.copy()
        fields.append('debt_and_credit_structure')
        labels = commonlabels

        labels['debt_and_credit_structure'] = "&nbsp;<b> Debt And Credit Structure: </b>"
        
        widgets = dict(commonwidgets)
        widgets['debt_and_credit_structure'] = forms.Select(attrs={'class': 'form-control  mb-3', })


class Store_of_wealthForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Store_of_wealth
        fields = commonfields.copy()
        fields.append('store_of_wealth')
        labels = commonlabels

        labels['store_of_wealth'] = "&nbsp;<b> Store Of Wealth: </b>"
        
        widgets = dict(commonwidgets)
        widgets['store_of_wealth'] = forms.Select(attrs={'class': 'form-control  mb-3', })

class Source_of_supportForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Source_of_support
        fields = commonfields.copy()
        fields.append('source_of_support')
        labels = commonlabels

        labels['source_of_support'] = "&nbsp;<b> Source Of Support: </b>"
        
        widgets = dict(commonwidgets)
        widgets['source_of_support'] = forms.Select(attrs={'class': 'form-control  mb-3', })



class Occupational_complexityForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Occupational_complexity
        fields = commonfields.copy()
        fields.append('occupational_complexity')
        labels = commonlabels
        labels['occupational_complexity'] = "&nbsp;<b> Occupational Complexity: </b>"
        widgets = dict(commonwidgets)
        widgets['occupational_complexity'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Special_purpose_houseForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Special_purpose_house
        fields = commonfields.copy()
        fields.append('special_purpose_house')
        labels = commonlabels
        labels['special_purpose_house'] = "&nbsp;<b> Special Purpose House: </b>"
        widgets = dict(commonwidgets)
        widgets['special_purpose_house'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Other_special_purpose_siteForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Other_special_purpose_site
        fields = commonfields.copy()
        fields.append('other_special_purpose_site')
        labels = commonlabels
        labels['other_special_purpose_site'] = "&nbsp;<b> Other Special Purpose Site: </b>"
        widgets = dict(commonwidgets)
        widgets['other_special_purpose_site'] = forms.Select(attrs={'class': 'form-control  mb-3', })



class Largest_communication_distanceForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Largest_communication_distance
        fields = commonfields.copy()
        fields.append('largest_communication_distance_from')
        fields.append('largest_communication_distance_to')
        labels = commonlabels
        labels['largest_communication_distance_from'] = "&nbsp;<b> Largest Communication Distance (From): </b>"
        labels['largest_communication_distance_to'] = "&nbsp;<b> Largest Communication Distance (To): </b>"
        widgets = dict(commonwidgets)
        widgets['largest_communication_distance_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['largest_communication_distance_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })


class Fastest_individual_communicationForm(forms.ModelForm):
    """
    
    """
    class Meta:
        """
        :noindex:
        """
        model = Fastest_individual_communication
        fields = commonfields.copy()
        fields.append('fastest_individual_communication_from')
        fields.append('fastest_individual_communication_to')
        labels = commonlabels
        labels['fastest_individual_communication_from'] = "&nbsp;<b> Fastest Individual Communication (From): </b>"
        labels['fastest_individual_communication_to'] = "&nbsp;<b> Fastest Individual Communication (To): </b>"
        widgets = dict(commonwidgets)
        widgets['fastest_individual_communication_from'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })
        widgets['fastest_individual_communication_to'] = forms.NumberInput(attrs={'class': 'form-control  mb-3', })