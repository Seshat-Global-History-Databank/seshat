from .models import Widespread_religion, Official_religion, Elites_religion, Theo_sync_dif_rel, Sync_rel_pra_ind_beli, Religious_fragmentation, Gov_vio_freq_rel_grp, Gov_res_pub_wor, Gov_res_pub_pros, Gov_res_conv, Gov_press_conv, Gov_res_prop_own_for_rel_grp, Tax_rel_adh_act_ins, Gov_obl_rel_grp_ofc_reco, Gov_res_cons_rel_buil, Gov_res_rel_edu, Gov_res_cir_rel_lit, Gov_dis_rel_grp_occ_fun, Soc_vio_freq_rel_grp, Soc_dis_rel_grp_occ_fun, Gov_press_conv_for_aga

from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register

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
    'description': Textarea(attrs={'class': 'form-control  mb-3', 'style': 'height: 340px; line-height: 1.2;', 'placeholder':'Add a meaningful description (optional)\nNote: USe §REF§ opening and closing tags to include citations to the description.\nExample: §REF§Chadwick, J. 1976. The Mycenaean World, Cambridge, p.78.§REF§.'}),
    'citations': forms.SelectMultiple(attrs={'class': 'form-control mb-3 js-states js-example-basic-multiple', 'text':'citations[]' , 'style': 'height: 340px', 'multiple': 'multiple'}),
    'tag': forms.RadioSelect(),
    "is_disputed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "is_uncertain" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "expert_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    "drb_reviewed" : forms.CheckboxInput(attrs={'class': 'mb-3', }),
    'finalized': forms.CheckboxInput(attrs={'class': 'mb-3', 'checked': True, }),
}

# class RaForm(forms.ModelForm):
#     class Meta:
#         model = Ra
#         fields = commonfields.copy()
#         fields.append('sc_ra')
#         labels = commonlabels
        
#         widgets = dict(commonwidgets)
#         widgets['sc_ra'] = forms.Select(attrs={'class': 'form-control  mb-3', })

class Widespread_religionForm(forms.ModelForm):
    """
    Form for creating and updating the Widespread_religion model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Widespread_religion
        fields = commonfields.copy()
        fields.append('order')
        fields.append('widespread_religion')
        fields.append('degree_of_prevalence')

        labels = commonlabels
        labels['widespread_religion'] = "&nbsp;<b> Widespread Religion: </b>"
        labels['order'] = "&nbsp;<b> Order: </b>"
        labels['degree_of_prevalence'] = "&nbsp;<b> Degree of Prevalence: </b>"

        widgets = dict(commonwidgets)
        widgets['widespread_religion'] = forms.Select(attrs={'class': 'form-control  mb-3 js-example-basic-single', 'id': 'id_widespread_religion', 'name': 'widespread_religion'})
        widgets['order'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        widgets['degree_of_prevalence'] = forms.Select(attrs={'class': 'form-control  mb-3', })

class Official_religionForm(forms.ModelForm):
    """
    Form for creating and updating creating and updating the Official_religion model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Official_religion
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Official Religion: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3 js-example-basic-single', 'id': 'id_official_religion', 'name': 'official_religion' })
        

class Elites_religionForm(forms.ModelForm):
    """
    Form for creating and updating the Elites_religion model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Elites_religion
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Elites' Religion: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3 js-example-basic-single', 'id': 'id_elites_religion', 'name': 'elites_religion' })
        
##########################################
class Theo_sync_dif_relForm(forms.ModelForm):
    """
    Form for creating and updating the Theo_sync_dif_rel model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Theo_sync_dif_rel
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Theological Syncretism Of Different Religions: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Sync_rel_pra_ind_beliForm(forms.ModelForm):
    """
    Form for creating and updating the Sync_rel_pra_ind_beli model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Sync_rel_pra_ind_beli
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Syncretism Of Religious Practices At The Level Of Individual Believers: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Religious_fragmentationForm(forms.ModelForm):
    """
    Form for creating and updating the Religious_fragmentation model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Religious_fragmentation
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Religious Fragmentation: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_vio_freq_rel_grpForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_vio_freq_rel_grp model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_vio_freq_rel_grp
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Frequency Of Governmental Violence Against Religious Groups: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_res_pub_worForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_pub_wor model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_res_pub_wor
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Government Restrictions On Public Worship: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_res_pub_prosForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_pub_pros model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_res_pub_pros
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Government Restrictions On Public Proselytizing: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_res_convForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_conv model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_res_conv
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Government Restrictions On Conversion: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_press_convForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_press_conv model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_press_conv
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Government Pressure To Convert: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_res_prop_own_for_rel_grpForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_prop_own_for_rel_grp model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_res_prop_own_for_rel_grp
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Government Restrictions On Property Ownership For Adherents Of Any Religious Group: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Tax_rel_adh_act_insForm(forms.ModelForm):
    """
    Form for creating and updating the Tax_rel_adh_act_ins model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Tax_rel_adh_act_ins
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Taxes Based On Religious Adherence Or On Religious Activities And Institutions: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_obl_rel_grp_ofc_recoForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_obl_rel_grp_ofc_reco model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_obl_rel_grp_ofc_reco
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Governmental Obligations For Religious Groups To Apply For Official Recognition: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_res_cons_rel_builForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_cons_rel_buil model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_res_cons_rel_buil
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Government Restrictions On Construction Of Religious Buildings: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_res_rel_eduForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_rel_edu model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_res_rel_edu
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Government Restrictions On Religious Education: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_res_cir_rel_litForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_cir_rel_lit model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_res_cir_rel_lit
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Government Restrictions On Circulation Of Religious Literature: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_dis_rel_grp_occ_funForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_dis_rel_grp_occ_fun model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_dis_rel_grp_occ_fun
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Government Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Soc_vio_freq_rel_grpForm(forms.ModelForm):
    """
    Form for creating and updating the Soc_vio_freq_rel_grp model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Soc_vio_freq_rel_grp
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Frequency Of Societal Violence Against Religious Groups: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Soc_dis_rel_grp_occ_funForm(forms.ModelForm):
    """
    Form for creating and updating the Soc_dis_rel_grp_occ_fun model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Soc_dis_rel_grp_occ_fun
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Societal Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })
        

class Gov_press_conv_for_agaForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_press_conv_for_aga model.
    """
    class Meta:
        """
        :noindex:
        """
        model = Gov_press_conv_for_aga
        fields = commonfields.copy()
        fields.append('coded_value')
        labels = commonlabels
        labels['coded_value'] = "&nbsp;<b> Societal Pressure To Convert Or Against Conversion: </b>"
        widgets = dict(commonwidgets)
        widgets['coded_value'] = forms.Select(attrs={'class': 'form-control  mb-3', })