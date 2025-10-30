
from seshat.utils.utils import dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier
from django.db.models.base import Model
# from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.safestring import mark_safe
from django.views.generic.list import ListView

from django.contrib.contenttypes.models import ContentType

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..core.models import Citation, Reference, Polity, Section, Subsection, Country, Variablehierarchy, SeshatPrivateComment, SeshatPrivateCommentPart, SeshatComment, SeshatCommentPart, ScpThroughCtn

from ..core.terms_utils import require_terms_acceptance


from seshat.apps.accounts.models import Seshat_Expert
from django.utils.dateparse import parse_date
from collections import Counter


from seshat.apps.core.forms import SignUpForm, VariablehierarchyFormNew, CitationForm, ReferenceForm, SeshatCommentForm, SeshatCommentPartForm, PolityForm, PolityUpdateForm, CapitalForm, NgaForm, SeshatCommentPartForm2, SeshatCommentPartForm5,  SeshatCommentPartForm10, SeshatPrivateCommentPartForm, ReferenceFormSet2, ReferenceFormSet5, ReferenceFormSet10, CommentPartFormSet, ReferenceWithPageForm, SeshatPrivateCommentForm, ReligionForm, ExpertCheckedForm

from seshat.apps.core.forms import SeshatPrivateCommentPartForm
from django.http import HttpResponseRedirect, response, JsonResponse, HttpResponseForbidden
# from .mycodes import *
from django.conf import settings

from django.urls import reverse, reverse_lazy
from django.db.models import Q, F, IntegerField

from django.views import generic
import csv
import datetime

from django.contrib import messages

from django.core.paginator import Paginator

from django.http import HttpResponse, FileResponse, Http404

from django.forms.models import model_to_dict

import requests
from requests.structures import CaseInsensitiveDict

from django.apps import apps

######EMAIL_CONFIRMATION_BRANCH is the keyword that needs to be searched
from django.core.mail import send_mail

from .mixins import PolityIdMixin
from .var_defs import swapped_dict

from django.db.models.functions import Coalesce, Cast


from .models import Polity_research_assistant, Polity_utm_zone, Polity_original_name, Polity_alternative_name, Polity_peak_years, Polity_duration, Polity_degree_of_centralization, Polity_suprapolity_relations, Polity_capital, Polity_language, Polity_linguistic_family, Polity_language_genus, Polity_religion_genus, Polity_religion_family, Polity_religion, Polity_relationship_to_preceding_entity, Polity_preceding_entity, Polity_succeeding_entity, Polity_supracultural_entity, Polity_scale_of_supracultural_interaction, Polity_alternate_religion_genus, Polity_alternate_religion_family, Polity_alternate_religion, Polity_expert, Polity_editor, Polity_religious_tradition


from .forms import Polity_research_assistantForm, Polity_utm_zoneForm, Polity_original_nameForm, Polity_alternative_nameForm, Polity_peak_yearsForm, Polity_durationForm, Polity_degree_of_centralizationForm, Polity_suprapolity_relationsForm, Polity_capitalForm, Polity_languageForm, Polity_linguistic_familyForm, Polity_language_genusForm, Polity_religion_genusForm, Polity_religion_familyForm, Polity_religionForm, Polity_relationship_to_preceding_entityForm, Polity_preceding_entityForm, Polity_succeeding_entityForm, Polity_supracultural_entityForm, Polity_scale_of_supracultural_interactionForm, Polity_alternate_religion_genusForm, Polity_alternate_religion_familyForm, Polity_alternate_religionForm, Polity_expertForm, Polity_editorForm, Polity_religious_traditionForm

from ..crisisdb.models import Instability_type, Check_choice, INST_EXTENT_CHOICES, INST_INTENSITY_CHOICES

from ..rt.models import Widespread_religion, Official_religion, Elites_religion, Theo_sync_dif_rel, Sync_rel_pra_ind_beli, Religious_fragmentation, Gov_vio_freq_rel_grp, Gov_res_pub_wor, Gov_res_pub_pros, Gov_res_conv, Gov_press_conv, Gov_res_prop_own_for_rel_grp, Tax_rel_adh_act_ins, Gov_obl_rel_grp_ofc_reco, Gov_res_cons_rel_buil, Gov_res_rel_edu, Gov_res_cir_rel_lit, Gov_dis_rel_grp_occ_fun, Soc_vio_freq_rel_grp, Soc_dis_rel_grp_occ_fun, Gov_press_conv_for_aga

BATCH_1_END = datetime.date(2025, 3, 29)
BATCH_2_END = datetime.date(2025, 4, 11)

def get_batch_tag(created_date):
    if created_date < BATCH_1_END:
        return "Batch 1"
    elif created_date < BATCH_2_END:
        return "Batch 2"
    else:
        return "Batch 3"


# Define a custom test function to check for the 'core.add_capital' permission
def has_add_capital_permission(user):
    return user.has_perm('core.add_capital')
        

def generalvars(request):

    app_name = 'general'  # Replace with your app name
    models_1 = apps.get_app_config(app_name).get_models()

    unique_politys = set()
    number_of_all_rows = 0
    number_of_variables = 0
    all_vars_grouped = {}
    all_vars_types = {}

    all_sect_download_links = {}

    for model in models_1:
        model_name = model.__name__
        if model_name in ["Polity_research_assistant", "Polity_editor", "Polity_expert", "Polity_relationship_to_preceding_entity",  "Polity_succeeding_entity"]:
            continue
        s_value = str(model().subsection())
        ss_value = str(model().sub_subsection())

        better_name = "download_csv_" + s_value.replace("-", "_").replace(" ", "_").replace(":", "").lower()
        all_sect_download_links[s_value] = better_name
        if s_value not in all_vars_grouped:
            all_vars_grouped[s_value] = {}
            if ss_value:
                all_vars_grouped[s_value][ss_value] = []
            else:
                all_vars_grouped[s_value]["None"] = []
        else:
            if ss_value:
                all_vars_grouped[s_value][ss_value] = []
            else:
                all_vars_grouped[s_value]["None"] = []

    models = apps.get_app_config(app_name).get_models()

    for model in models:
        model_name = model.__name__
        if model_name in ["Polity_research_assistant", "Polity_editor", "Polity_expert",  "Polity_relationship_to_preceding_entity", "Polity_succeeding_entity"]:
            continue


        subsection_value = str(model().subsection())
        sub_subsection_value = str(model().sub_subsection())
        count = model.objects.count()
        pols_count = Polity.objects.count()
        number_of_all_rows += count
        model_title = model_name.replace("_", " ").title()
        model_create = model_name.lower() + "-create"
        model_download = model_name.lower() + "-download"
        model_metadownload = model_name.lower() + "-metadownload"
        model_all = model_name.lower() + "s_all"
        model_s = model_name.lower() + "s"

        queryset = model.objects.exclude(polity_id__isnull=True)
        filtered_queryset_pres = 0
        filtered_queryset_abs = 0
        filtered_queryset_unk = 0
        filtered_queryset_sus_unk = 0
        filtered_queryset_unc = 0
        filtered_queryset_trans = 0

        politys = queryset.values_list('polity', flat=True).distinct()
        unique_politys.update(politys)
        polities_for_this_var = len(set(politys))


        if model_name.lower() in ['polity_peak_years', 'polity_duration', 'polity_scale_of_supracultural_interaction', ]:
            var_type= "RANGE"
            
            for obj in queryset:

                if obj.show_value() == " - " and obj.tag == "TRS":
                    filtered_queryset_unk +=1
                elif obj.show_value() == " - " and obj.tag == "SSP":
                    filtered_queryset_sus_unk +=1
                elif obj.show_value() == ' - ' or obj.tag == "UND":
                    filtered_queryset_unc +=1
                elif obj.show_value() != ' - ':
                    filtered_queryset_pres +=1

            dif_count = pols_count - polities_for_this_var
            number_of_variables += 1

            to_be_appended = [
                model_title, # v.0
                model_s,
                model_create,
                model_download,
                model_metadownload,
                model_all,          # v.5
                count,
                polities_for_this_var,
                var_type,
                filtered_queryset_pres,
                0, #filtered_queryset_abs,      # v.10
                filtered_queryset_sus_unk,     
                filtered_queryset_unk,
                filtered_queryset_unc,       # v.13
                pols_count,
                dif_count,
                0, #filtered_queryset_trans,
                'Range was coded',
                ]
        elif model_name.lower() in ['polity_original_name', 'polity_alternative_name', 'polity_utm_zone', 'polity_degree_of_centralization', 'polity_supracultural_entity', 
            'polity_religion',
            'polity_religion_genus',                       
            'polity_religion_family',
            'polity_alternate_religion',
            'polity_religious_tradition',
            'polity_alternate_religion_genus',                       
            'polity_alternate_religion_family',
            'polity_language',
            'polity_language_genus',                       
            'polity_linguistic_family'
            ]:
            var_type="TEXT+"

            for obj in queryset:
                if obj.show_value() == ' - ':
                    filtered_queryset_abs +=1
                elif obj.show_value() == "unknown" and obj.tag == "TRS":
                    filtered_queryset_unk +=1
                elif obj.show_value() == "unknown" and obj.tag == "SSP":
                    filtered_queryset_sus_unk +=1
                elif obj.show_value() == 'uncoded' or obj.tag == "UND":
                    filtered_queryset_unc +=1
                elif obj.show_value() != ' - ':
                    filtered_queryset_pres +=1

            dif_count = pols_count - polities_for_this_var
            number_of_variables += 1

            to_be_appended = [
                model_title, # v.0
                model_s,
                model_create,
                model_download,
                model_metadownload,
                model_all,          # v.5
                count,
                polities_for_this_var,
                var_type,
                filtered_queryset_pres,
                filtered_queryset_abs,      # v.10
                filtered_queryset_sus_unk,     
                filtered_queryset_unk,
                filtered_queryset_unc,       # v.13
                pols_count,
                dif_count,
                filtered_queryset_trans,
                'Properly Coded',
                ]

        elif model_name.lower() == 'polity_suprapolity_relations':
            var_type="TEXT+"

            for obj in queryset:
                if obj.other_polity:
                    filtered_queryset_pres +=1
                elif obj.supra_polity_relations in ['none', 'None', ]:
                    filtered_queryset_abs +=1
                elif obj.supra_polity_relations and not obj.other_polity:
                    filtered_queryset_trans +=1
                elif obj.supra_polity_relations == 'unknown'  and obj.tag == "TRS":
                    filtered_queryset_unk +=1
                elif obj.supra_polity_relations == 'unknown'  and obj.tag == "SSP":
                    filtered_queryset_sus_unk +=1
                elif obj.show_value() == 'uncoded' or obj.tag == "UND":
                    filtered_queryset_unc +=1

            dif_count = pols_count - polities_for_this_var
            number_of_variables += 1

            to_be_appended = [
                model_title, # v.0
                model_s,
                model_create,
                model_download,
                model_metadownload,
                model_all,          # v.5
                count,
                polities_for_this_var,
                var_type,
                filtered_queryset_pres,
                filtered_queryset_abs,      # v.10
                filtered_queryset_sus_unk,     
                filtered_queryset_unk,
                filtered_queryset_unc,       # v.13
                pols_count,
                dif_count,
                filtered_queryset_trans,
                'Properly Coded',
                ]
            
        elif model_name.lower() == 'polity_preceding_entity':
            var_type="TEXT+"

            for obj in queryset:
                if obj.other_polity and obj.relationship_to_preceding_entity:
                    filtered_queryset_pres +=1


                elif obj.relationship_to_preceding_entity == 'unknown'  and obj.tag == "SSP":
                    filtered_queryset_sus_unk +=1
                elif obj.relationship_to_preceding_entity == 'unknown'  and obj.tag == "TRS":
                    filtered_queryset_unk +=1
                elif obj.other_polity or obj.merged_old_data or obj.relationship_to_preceding_entity:
                    filtered_queryset_trans +=1
                elif obj.show_value() == ' - ' or obj.tag == "UND":
                    filtered_queryset_unc +=1
                else:
                    pass
                    #print(obj.id, " ", obj.show_value())

            dif_count = pols_count - polities_for_this_var
            number_of_variables += 1

            to_be_appended = [
                model_title, # v.0
                model_s,
                model_create,
                model_download,
                model_metadownload,
                model_all,          # v.5
                count,
                polities_for_this_var,
                var_type,
                filtered_queryset_pres,
                filtered_queryset_abs,      # v.10
                filtered_queryset_sus_unk,     
                filtered_queryset_unk,
                filtered_queryset_unc,       # v.13
                pols_count,
                dif_count,
                filtered_queryset_trans,
                'Properly Coded',
                ]


        elif model_name.lower() == 'polity_capital':
            var_type="TEXT+"

            for obj in queryset:
                if obj.polity_cap and obj.polity_cap.name not in ['None (Absent Capital)', 'none', 'None', 'Unknown']:
                    filtered_queryset_pres +=1
                elif obj.polity_cap and obj.polity_cap.name in ['None (Absent Capital)']:
                    filtered_queryset_abs +=1
                elif obj.polity_cap and obj.polity_cap.name == 'Unknown'  and obj.tag == "TRS":
                    filtered_queryset_unk +=1
                elif obj.polity_cap and obj.polity_cap.name == 'Unknown'  and obj.tag == "SSP":
                    filtered_queryset_sus_unk +=1
                elif not obj.polity_cap and obj.capital and obj.capital not in ["Unknown", "unknown", "NO_VALUE_ON_WIKI"]:
                    filtered_queryset_trans +=1
                elif obj.show_value() == 'uncoded' or obj.tag == "UND":
                    filtered_queryset_unc +=1
                elif str(obj.show_value()) in ['none', 'None', 'None (Absent Capital)']:
                    filtered_queryset_abs +=1
                else:
                    filtered_queryset_pres +=1

            dif_count = pols_count - polities_for_this_var
            number_of_variables += 1

            to_be_appended = [
                model_title, # v.0
                model_s,
                model_create,
                model_download,
                model_metadownload,
                model_all,          # v.5
                count,
                polities_for_this_var,
                var_type,
                filtered_queryset_pres,
                filtered_queryset_abs,      # v.10
                filtered_queryset_sus_unk,     
                filtered_queryset_unk,
                filtered_queryset_unc,       # v.13
                pols_count,
                dif_count,
                filtered_queryset_trans,
                'Properly Coded',
                ]

        else:
            var_type="A/P/U/~"

            for obj in queryset:
                if obj.show_value() == 'Present':
                    filtered_queryset_pres +=1
                if obj.show_value() == 'Absent':
                    filtered_queryset_abs +=1
                if obj.show_value() == "Unknown" and obj.tag == "TRS":
                    filtered_queryset_unk +=1
                if obj.show_value() == "Unknown" and obj.tag == "SSP":
                    filtered_queryset_sus_unk +=1
                if obj.show_value() == 'Uncoded' or obj.tag == "UND":
                    filtered_queryset_unc +=1
                if obj.show_value() == 'Transitional (Present -> Absent)' or obj.show_value() == 'Transitional (Absent -> Present)':
                    filtered_queryset_trans +=1

            dif_count = pols_count - polities_for_this_var
            number_of_variables += 1

            to_be_appended = [
                model_title, # v.0
                model_s,
                model_create,
                model_download,
                model_metadownload,
                model_all,          # v.5
                count,
                polities_for_this_var,
                var_type,
                filtered_queryset_pres,
                filtered_queryset_abs,      # v.10
                filtered_queryset_sus_unk,     
                filtered_queryset_unk,
                filtered_queryset_unc,       # v.13
                pols_count,
                dif_count,
                filtered_queryset_trans,
                'Present'
                ]


        all_vars_types[model_name.lower()] = (var_type, subsection_value, sub_subsection_value)
        if sub_subsection_value:
            all_vars_grouped[subsection_value][sub_subsection_value].append(to_be_appended)
        else:
            all_vars_grouped[subsection_value]["None"].append(to_be_appended)


    context = {}
    context["all_vars_grouped"] = all_vars_grouped
    context["all_sect_download_links"] = all_sect_download_links
    context["all_polities"] = len(unique_politys)
    context["number_of_all_rows"] = number_of_all_rows

    context["number_of_variables"] = number_of_variables

    #print('----------------')
    #print(all_vars_types)
    #print('-----------------')

    return render(request, 'general/generalvars.html', context=context)






def generalvarsold(request):

    app_name = 'general'  # Replace with your app name
    models_1 = apps.get_app_config(app_name).get_models()

    unique_politys = set()
    number_of_all_rows = 0
    number_of_variables = 0

    all_vars_grouped = {}

    all_sect_download_links = {}

    for model in models_1:
        model_name = model.__name__
        if model_name in ["Polity_research_assistant", "Polity_editor", "Polity_expert"]:
            continue
        s_value = str(model().subsection())
        ss_value = str(model().sub_subsection())

        better_name = "download_csv_" + s_value.replace("-", "_").replace(" ", "_").replace(":", "").lower()
        all_sect_download_links[s_value] = better_name
        if s_value not in all_vars_grouped:
            all_vars_grouped[s_value] = {}
            if ss_value:
                all_vars_grouped[s_value][ss_value] = []
            else:
                all_vars_grouped[s_value]["None"] = []
        else:
            if ss_value:
                all_vars_grouped[s_value][ss_value] = []
            else:
                all_vars_grouped[s_value]["None"] = []

    models = apps.get_app_config(app_name).get_models()

    for model in models:
        model_name = model.__name__
        if model_name in ["Polity_research_assistant", "Polity_editor", "Polity_expert"]:
            continue
        subsection_value = str(model().subsection())
        sub_subsection_value = str(model().sub_subsection())
        count = model.objects.count()
        number_of_all_rows += count
        model_title = model_name.replace("_", " ").title()
        model_create = model_name.lower() + "-create"
        model_download = model_name.lower() + "-download"
        model_metadownload = model_name.lower() + "-metadownload"
        model_all = model_name.lower() + "s_all"
        model_s = model_name.lower() + "s"

        queryset = model.objects.exclude(polity_id__isnull=True)
        politys = queryset.values_list('polity', flat=True).distinct()
        unique_politys.update(politys)
        number_of_variables += 1

        to_be_appended = [model_title, model_s, model_create, model_download, model_metadownload, model_all, count]

        if sub_subsection_value:
            all_vars_grouped[subsection_value][sub_subsection_value].append(to_be_appended)
        else:
            all_vars_grouped[subsection_value]["None"].append(to_be_appended)


    context = {}
    context["all_vars_grouped"] = all_vars_grouped
    context["all_sect_download_links"] = all_sect_download_links    
    context["all_polities"] = len(unique_politys)
    context["number_of_all_rows"] = number_of_all_rows

    context["number_of_variables"] = number_of_variables

    return render(request, 'general/generalvars.html', context=context)


@login_required
def download_csv_all_general(request):
    """
    Download a CSV file of all general variables. This includes all models in the "general" app.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    """
    # Fetch all models in the "general" app
    app_name = 'general' 
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"general_data_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['section', 'subsection', 'polity_name', 'polity_new_ID', 'polity_old_ID', 'variable_name', 'value_from', 'value_to', 'year_from', 'year_to',
                   'confidence', 'is_disputed', 'is_uncertain', 'expert_checked',])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        if model in [Polity_research_assistant, Polity_editor, Polity_expert]:
            continue
        items = model.objects.exclude(polity_id__isnull=True)


        for obj in items:
            if obj.clean_name_spaced() == 'Polity Duration':
                writer.writerow(['General Variables',obj.subsection() , obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.clean_name()[7:],
                         obj.polity_year_from, obj.polity_year_to, obj.year_from, obj.year_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed,])
            elif obj.clean_name_spaced() == 'Polity Peak Years':
                writer.writerow(['General Variables',obj.subsection() , obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.clean_name()[7:],
                         obj.peak_year_from, obj.peak_year_to, obj.year_from, obj.year_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed,])
            else:
                if obj.show_value() == "NO_VALUE_ON_WIKI" or obj.show_value() == "NO_VALID_VALUE":
                    continue
                elif "O_VALUE_ON_WIKI" in str(obj.show_value()):
                    continue
                else:
                    writer.writerow(['General Variables',obj.subsection() , obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.clean_name()[7:],
                            obj.show_value(), None,  obj.year_from, obj.year_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed,])

    return response


######EMAIL_CONFIRMATION_BRANCH is the keyword that needs to be searched
def send_test_email():
    """
    Send a test email.

    Returns:
        None
    """
    send_mail(
        'Test Email',
        'This is a test email from Django.',
        'seshatdb@gmail.com',  # Replace with your sender email
        ['benam@csh.ac.at'],  # Replace with recipient email(s)
        fail_silently=False,
    )



###### NEW APPROACH ##############
from seshat.apps.core.forms import  SeshatCommentPartForm2

@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def dynamic_detail_view(request, pk, model_class, myvar, var_name_display, var_section, var_subsection, db_section):
    # Retrieve the object for the given model class
    #import time
    #start_time = time.time()
    obj = get_object_or_404(model_class, pk=pk)
    form_inline_new = SeshatCommentPartForm2(request.POST)

    context = {
        'object': obj,
        "myvar": myvar,
        "var_name_display": var_name_display,
        'create_new_url': myvar+"-create",
        'see_all_url': myvar+"s_all",
        'letsdo': 'Let us do it!!!',
        'form': form_inline_new,
        'db_section': db_section,
        'var_section': var_section,
        'var_subsection': var_subsection,
    }
    #end_time = time.time()
    #print('elapsed_time RT', end_time-start_time)

    return render(request, 'core/generic_templates/generic_detail.html', context)




# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def dynamic_create_view(request, form_class, x_name, coded_value, myvar, my_exp, var_section, var_subsection, db_section):
    x_name_1 = x_name
    x_name_2 = None
    x_name_3 = None


    db_section_mapper = {
        'general': 'General',
        'sc': 'Social Complexity',
        'wf': 'Warfare',
        'ec': 'Economy',
        'rt': 'Religion Variables',
        'crisisdb': 'Crisisdb',
    }

    if coded_value == "power_transition":
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10, x_name_11, x_name_12, x_name_13, x_name_14  =  'name', 'predecessor', 'successor', 'contested', 'overturn', 'predecessor_assassination', 'intra_elite', 'military_revolt', 'popular_uprising', 'separatist_rebellion', 'external_invasion', 'external_interference', 'drb_reviewed', 'description'
    elif coded_value == "widespread_religion":
        x_name_1, x_name_2, x_name_3 = "order", "widespread_religion", "degree_of_prevalence"
    elif x_name == "lux_precious_metal":
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10, x_name_11 =  'name', 'coded_value', 'place_of_provenance_str', 'ruler_consumption', 'ruler_consumption_tag', 'elite_consumption', 'elite_consumption_tag', 'common_people_consumption', 'common_people_consumption_tag', 'which_metals', 'place_of_provenance_pol'
    elif db_section == 'ec':
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10 =  'name', 'coded_value', 'place_of_provenance_str', 'ruler_consumption', 'ruler_consumption_tag', 'elite_consumption', 'elite_consumption_tag', 'common_people_consumption', 'common_people_consumption_tag', 'place_of_provenance_pol'
    elif coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall']:
        x_name_with_from = f'{x_name}_from'
        x_name_with_to = f'{x_name}_to' 
    elif coded_value == 'duration':
        x_name_with_from = 'polity_year_from'
        x_name_with_to = 'polity_year_to'
    elif coded_value == 'peak_years':
        x_name_with_from = 'peak_year_from'
        x_name_with_to = 'peak_year_to'
    elif coded_value == 'scale_of_supracultural_interaction':
        x_name_with_from = 'scale_from'
        x_name_with_to = 'scale_to'

    if request.method == 'POST':
        my_form = form_class(request.POST)
        
        if my_form.is_valid():
            # print(f"ZARAGOOOOOOOOOOOZA (NEW): {my_form.cleaned_data['expert_reviewed_by_me']}.")
            # my_form.instance.expert_reviewed = my_form.cleaned_data['expert_reviewed_by_me']
            logged_in_user = request.user
            new_object = my_form.save(commit=False)
            suggested_experts = my_form.cleaned_data['suggested_expert']  # Adjust the field name
            #is_reviewed_by_me = my_form.cleaned_data['expert_reviewed_by_me']  # Adjust the field name
            try:
                logged_in_staff = Seshat_Expert.objects.get(user=logged_in_user)
            except:
                logged_in_staff = None


            if suggested_experts:
                # create a Prvate Comment to attach parts to it:
                father_private_comment = SeshatPrivateComment.objects.create(text="")
                new_object.private_comment = father_private_comment
                seshat_private_comment_part = SeshatPrivateCommentPart(
                    private_comment_part_text=f"I have coded a new record for the variable '{new_object.name}' on the polity: '{new_object.polity}'. I would appreciate it if you could review it.",
                    private_comment_owner=logged_in_staff, 
                    private_comment= father_private_comment
                )

                #print("####################", new_object)

                seshat_private_comment_part.save()

                seshat_private_comment_part.private_comment_reader.add(*suggested_experts) 
            
            new_object.expert_reviewed = False
            new_object.save()  # Save the object to persist the association
            my_form.save_m2m()



            action = request.POST.get('action')
            if action == 'redirect_one':
                return redirect("polity-detail-main", pk=new_object.polity.id) 
            elif action == 'redirect_two':
                return redirect(f"{x_name}-detail", pk=new_object.id)  # Replace 'success_url_name' with your success URL

            # Add the current user as a curator if they are an instance of Seshat_Expert
            # logged_in_user = request.user

            # try:
            #     seshat_staff_instance = Seshat_Expert.objects.get(user=logged_in_user)
            # except:
            #     seshat_staff_instance = None
            # if seshat_staff_instance:
            #     print("Alllllllloooooooooooooooo: ", logged_in_user)
            #     new_object.curator.add(seshat_staff_instance)

    else:
        polity_id_x = request.GET.get('polity_id_x')
        my_form = form_class(initial= {'polity': polity_id_x,})

    # Prepare the context for invalid form
    context = {
        'form': my_form,
        'object': object,
        "myvar": myvar,
        'var_section': var_section,
        'var_subsection': var_subsection,
        "my_exp": my_exp,
        'db_section_mapper': db_section_mapper[db_section],
        #'expert_reviewed_by_me': my_form['expert_reviewed_by_me']
    }


    if coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall']:
        context.update({
            'extra_var': my_form[x_name_with_from],
            'extra_var2': my_form[x_name_with_to],
        })
    elif coded_value in ['preceding_entity']:
        context.update({
            'extra_var': my_form['other_polity'],
            'extra_var2': my_form['merged_old_data'],
            'extra_var3': my_form['relationship_to_preceding_entity'],
        })
    elif coded_value in ['widespread_religion']:
        context.update({
            'extra_var': my_form[x_name_1],
            'extra_var2': my_form[x_name_2],
            'extra_var3': my_form[x_name_3],
        })
    elif coded_value in ['power_transition']:
        context.update({
            'extra_var': my_form[x_name_1],
            'extra_var2': my_form[x_name_2],
            'extra_var3': my_form[x_name_3],
            'extra_var4': my_form[x_name_4],
            'extra_var5': my_form[x_name_5],
            'extra_var6': my_form[x_name_6],
            'extra_var7': my_form[x_name_7],
            'extra_var8': my_form[x_name_8],
            'extra_var9': my_form[x_name_9],
            'extra_var10': my_form[x_name_10],
            'extra_var11': my_form[x_name_11],
            'extra_var12': my_form[x_name_12],
            'extra_var13': my_form[x_name_13],
            'extra_var14': my_form[x_name_14],

        })
    elif x_name in ['lux_precious_metal'] and db_section == 'ec':
        context.update({
            'extra_var': my_form[x_name_1],
            'extra_var2': my_form[x_name_2],
            'extra_var3': my_form[x_name_3],
            'extra_var4': my_form[x_name_4],
            'extra_var5': my_form[x_name_5],
            'extra_var6': my_form[x_name_6],
            'extra_var7': my_form[x_name_7],
            'extra_var8': my_form[x_name_8],
            'extra_var9': my_form[x_name_9],
            'extra_var10': my_form[x_name_10],
            'extra_var11': my_form[x_name_11],
        })
    elif db_section == 'ec':
        context.update({
            'extra_var': my_form[x_name_1],
            'extra_var2': my_form[x_name_2],
            'extra_var3': my_form[x_name_3],
            'extra_var4': my_form[x_name_4],
            'extra_var5': my_form[x_name_5],
            'extra_var6': my_form[x_name_6],
            'extra_var7': my_form[x_name_7],
            'extra_var8': my_form[x_name_8],
            'extra_var9': my_form[x_name_9],
            'extra_var10': my_form[x_name_10],
        })
    elif coded_value in ['suprapolity_relations']:
        context.update({
            'extra_var': my_form['supra_polity_relations'],
            'extra_var2': my_form['other_polity'],

        })
    elif coded_value in ['duration', 'peak_years', 'scale_of_supracultural_interaction']:
        context.update({
            'extra_var': my_form[x_name_with_from],
            'extra_var2': my_form[x_name_with_to],
        })
    elif coded_value in ['capital',]:
        context.update({
            'extra_var': my_form['polity_cap'], 
        })
    else:
        context.update({
            'extra_var': my_form[coded_value],
        })

    return render(request, 'core/generic_templates/generic_create.html', context)



# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def dynamic_update_view_old(request, object_id, form_class, model_class, x_name, coded_value, myvar, my_exp, var_section, var_subsection, db_section, delete_url_name):
    # Retrieve the object based on the object_id
    my_object = model_class.objects.get(id=object_id)

    db_section_mapper = {
        'general': 'General',
        'sc': 'Social Complexity',
        'wf': 'Warfare',
        'ec': 'Economy',
        'rt': 'Religion Variables',
        'crisisdb': 'Crisisdb',
    }

    if coded_value == "power_transition":
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10, x_name_11, x_name_12, x_name_13, x_name_14  =  'name', 'predecessor', 'successor', 'contested', 'overturn', 'predecessor_assassination', 'intra_elite', 'military_revolt', 'popular_uprising', 'separatist_rebellion', 'external_invasion', 'external_interference', 'drb_reviewed', 'description'
    elif coded_value == "widespread_religion":
        x_name_1, x_name_2, x_name_3 = "order", "widespread_religion", "degree_of_prevalence"
    elif x_name == "lux_precious_metal":
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10, x_name_11 =  'name', 'coded_value', 'place_of_provenance_str', 'ruler_consumption', 'ruler_consumption_tag', 'elite_consumption', 'elite_consumption_tag', 'common_people_consumption', 'common_people_consumption_tag', 'which_metals', 'place_of_provenance_pol'
    elif db_section == 'ec':
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10 =  'name', 'coded_value', 'place_of_provenance_str', 'ruler_consumption', 'ruler_consumption_tag', 'elite_consumption', 'elite_consumption_tag', 'common_people_consumption', 'common_people_consumption_tag', 'place_of_provenance_pol'
    elif coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall' ]:
        x_name_with_from = f'{x_name}_from'
        x_name_with_to = f'{x_name}_to'
    elif coded_value == 'duration':
        x_name_with_from = 'polity_year_from'
        x_name_with_to = 'polity_year_to'
    elif coded_value == 'peak_years':
        x_name_with_from = 'peak_year_from'
        x_name_with_to = 'peak_year_to'
    elif coded_value == 'scale_of_supracultural_interaction':
        x_name_with_from = 'scale_from'
        x_name_with_to = 'scale_to'

    # Handle POST request
    if request.method == 'POST':
        my_form = form_class(request.POST, instance=my_object)

        if my_form.is_valid():
            logged_in_user = request.user
            new_object = my_form.save(commit=False)
            suggested_experts = my_form.cleaned_data['suggested_expert']  # Adjust the field name
            #is_reviewed_by_me = my_form.cleaned_data['expert_reviewed_by_me']  # Adjust the field name
            try:
                logged_in_staff = Seshat_Expert.objects.get(user=logged_in_user)
            except:
                logged_in_staff = None


            if suggested_experts:
                if new_object.private_comment and new_object.private_comment.id != 1:
                    #print('##### ID ######', new_object.private_comment.id)
                    father_private_comment = new_object.private_comment
                else:
                # create a Prvate Comment to attach parts to it:
                    father_private_comment = SeshatPrivateComment.objects.create(text="")
                    new_object.private_comment = father_private_comment
                seshat_private_comment_part = SeshatPrivateCommentPart(
                    private_comment_part_text=f"I have coded a new record for the variable '{new_object.name}' on the polity: '{new_object.polity}'. I would appreciate it if you could review it.",
                    private_comment_owner=logged_in_staff, 
                    private_comment= father_private_comment
                )

                # print("####################", new_object)
                # print(seshat_private_comment_part)
                # print(father_private_comment)
                # print('-----------------------')
                seshat_private_comment_part.save()
                seshat_private_comment_part.private_comment_reader.add(*suggested_experts) 
            
            new_object.expert_reviewed = False
            new_object.save()  # Save the object to persist the association
            my_form.save_m2m()

            
            action = request.POST.get('action')
            if action == 'redirect_one':
                url = reverse("polity-detail-main", kwargs={'pk': new_object.polity.id}) + f"#{x_name}_{new_object.id}"
                return redirect(url)
                #return redirect("polity-detail-main", pk=new_object.polity.id) 
            elif action == 'redirect_two':
                # if the object has some description already
                if new_object.comment:
                    return redirect(f"seshatcomment-update", pk=new_object.comment.id) 
                else:
                    return redirect(f"{x_name}-detail", pk=new_object.id) 
                 # Replace 'success_url_name' with your success URL


        
        # Prepare the context for invalid form
        context = {
            'form': my_form,
            'object': my_object,
            'delete_url': delete_url_name,
            "myvar": myvar,
            'var_section': var_section,
            'var_subsection': var_subsection,
            "my_exp": my_exp,
            #'expert_reviewed_by_me': my_form['expert_reviewed_by_me'],
        }

        if coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall']:
            context.update({
                'extra_var': my_form[x_name_with_from],
                'extra_var2': my_form[x_name_with_to],
            })
        elif coded_value in ['preceding_entity']:
            context.update({
                'extra_var': my_form['other_polity'],
                'extra_var2': my_form['merged_old_data'],
                'extra_var3': my_form['relationship_to_preceding_entity'],
            })
        elif coded_value in ['widespread_religion']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
            })
        elif coded_value in ['power_transition']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
                'extra_var11': my_form[x_name_11],
                'extra_var12': my_form[x_name_12],
                'extra_var13': my_form[x_name_13],
                'extra_var14': my_form[x_name_14],
            })
        elif x_name in ['lux_precious_metal'] and db_section == 'ec':
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
                'extra_var11': my_form[x_name_11],
            })
        elif db_section == 'ec':
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
            })
        elif coded_value in ['suprapolity_relations']:
            context.update({
                'extra_var': my_form['supra_polity_relations'],
                'extra_var2': my_form['other_polity'],
            })
        elif coded_value in ['duration', 'peak_years', 'scale_of_supracultural_interaction']:
            context.update({
                'extra_var': my_form[x_name_with_from],
                'extra_var2': my_form[x_name_with_to],
            })
        elif coded_value in ['capital',]:
            context.update({
                'extra_var': my_form['polity_cap'], 
                'extra_var2': my_form[coded_value], 
            })
        else:
            context.update({
                'extra_var': my_form[coded_value],
            })
    else:
        # Handle GET request (initial form load)
        my_form = form_class(instance=my_object)
        context = {
            'form': my_form,
            'object': my_object,
            'delete_url': delete_url_name,
            "myvar": myvar,
            'var_section': var_section,
            'var_subsection': var_subsection,
            'db_section_mapper': db_section_mapper[db_section],
            "my_exp": my_exp,
            #'expert_reviewed_by_me': my_form['expert_reviewed_by_me']

        }

        if coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall']:
            context.update({
                'extra_var': my_form[x_name_with_from],
                'extra_var2': my_form[x_name_with_to],
            })
        elif coded_value in ['preceding_entity']:
            context.update({
                'extra_var': my_form['other_polity'],
                'extra_var2': my_form['merged_old_data'],
                'extra_var3': my_form['relationship_to_preceding_entity'],
            })
        elif coded_value in ['widespread_religion']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
            })
        elif coded_value in ['power_transition']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
                'extra_var11': my_form[x_name_11],
                'extra_var12': my_form[x_name_12],
                'extra_var13': my_form[x_name_13],
                'extra_var14': my_form[x_name_14],

            })
        elif x_name in ['lux_precious_metal'] and db_section == 'ec':
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
                'extra_var11': my_form[x_name_11],
            })
        elif db_section == 'ec':
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
            })
        elif coded_value in ['suprapolity_relations']:
            context.update({
                'extra_var': my_form['supra_polity_relations'],
                'extra_var2': my_form['other_polity'],
            })
        elif coded_value in ['duration', 'peak_years', 'scale_of_supracultural_interaction']:
            context.update({
                'extra_var': my_form[x_name_with_from],
                'extra_var2': my_form[x_name_with_to],
            })
        elif coded_value in ['capital',]:
            context.update({
                'extra_var': my_form['polity_cap'], 
                'extra_var2': my_form[coded_value], 
            })
        else:
            context.update({
                'extra_var': my_form[coded_value],
            })

    return render(request, 'core/generic_templates/generic_update_old.html', context)

# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def dynamic_update_view(request, object_id, form_class, model_class, x_name, coded_value, myvar, my_exp, var_section, var_subsection, db_section, delete_url_name):
    # Retrieve the object based on the object_id
    my_object = model_class.objects.get(id=object_id)

    db_section_mapper = {
        'general': 'General',
        'sc': 'Social Complexity',
        'wf': 'Warfare',
        'ec': 'Economy',
        'rt': 'Religion Variables',
        'crisisdb': 'Crisisdb',
    }


    another_form = SeshatPrivateCommentPartForm(request.POST)

    
    if coded_value == "power_transition":
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10, x_name_11, x_name_12, x_name_13, x_name_14  =  'name', 'predecessor', 'successor', 'contested', 'overturn', 'predecessor_assassination', 'intra_elite', 'military_revolt', 'popular_uprising', 'separatist_rebellion', 'external_invasion', 'external_interference', 'drb_reviewed', 'description'
    elif coded_value == "widespread_religion":
        x_name_1, x_name_2, x_name_3 = "order", "widespread_religion", "degree_of_prevalence"
    elif x_name == "lux_precious_metal":
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10, x_name_11 =  'name', 'coded_value', 'place_of_provenance_str', 'ruler_consumption', 'ruler_consumption_tag', 'elite_consumption', 'elite_consumption_tag', 'common_people_consumption', 'common_people_consumption_tag', 'which_metals', 'place_of_provenance_pol'
    elif x_name == "instability_event":
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10  =  'name', 'inst_intensity', 'inst_extent', 'llm_description', 'real_event_check', 'general_cot', 'classification_cot', 'ra_check', 'sorokin_rationale', 'inst_type', #'llm_name', 'llm_inst_intensity', 'llm_inst_extent', 'llm_inst_type',
    elif db_section == 'ec':
        x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10 =  'name', 'coded_value', 'place_of_provenance_str', 'ruler_consumption', 'ruler_consumption_tag', 'elite_consumption', 'elite_consumption_tag', 'common_people_consumption', 'common_people_consumption_tag', 'place_of_provenance_pol'
    elif coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall' ]:
        x_name_with_from = f'{x_name}_from'
        x_name_with_to = f'{x_name}_to'
    elif coded_value == 'duration':
        x_name_with_from = 'polity_year_from'
        x_name_with_to = 'polity_year_to'
    elif coded_value == 'peak_years':
        x_name_with_from = 'peak_year_from'
        x_name_with_to = 'peak_year_to'
    elif coded_value == 'scale_of_supracultural_interaction':
        x_name_with_from = 'scale_from'
        x_name_with_to = 'scale_to'


    # Handle POST request
    if request.method == 'POST':
        my_form = form_class(request.POST, instance=my_object)
        #print('zzzzzzzzzzzzzzzz', my_object.id)

        # if "submit_with_formset" in request.POST:
        #     form_inline_new = SeshatCommentPartForm2(request.POST)
        # else:
        #     form_inline_new = SeshatCommentPartForm2()  # Unbound formset (won't be validated)

        if my_form.is_valid():
            #print(f"ZARAGOOOOOOOOOOOZA (NEW): {my_form.cleaned_data['inst_type']}.")
            #my_form.instance.expert_reviewed = my_form.cleaned_data['expert_reviewed_by_me']

                

            logged_in_user = request.user
            new_object = my_form.save(commit=False)
            suggested_experts = my_form.cleaned_data['suggested_expert']
            #if 'ra_check' in my_form.cleaned_data:
            #    all_ra_checks = my_form.cleaned_data['ra_check'] 
            #    all_ra_checks_names = []
            #    for aa in all_ra_checks:
            #        all_ra_checks_names.append(aa.name)
            #print('fffffffffffffffffffff', '; '.join(all_ra_checks_names))
            #is_reviewed_by_me = my_form.cleaned_data['expert_reviewed_by_me']  # Adjust the field name
            try:
                logged_in_staff = Seshat_Expert.objects.get(user=logged_in_user)
            except:
                logged_in_staff = None


            # Update the is_expert_checked attribute


            if suggested_experts:
                if new_object.private_comment and new_object.private_comment.id != 1:
                    #print('##### ID ######', new_object.private_comment.id)
                    father_private_comment = new_object.private_comment
                else:
                # create a Prvate Comment to attach parts to it:
                    father_private_comment = SeshatPrivateComment.objects.create(text="")
                    new_object.private_comment = father_private_comment
                if x_name == "instability_event":
                    seshat_private_comment_part = SeshatPrivateCommentPart(
                        private_comment_part_text=f"We have used LLM to generate a new Instability Event: '{new_object.name}' on the polity: '{new_object.polity}'. I would appreciate it if you could review it.",
                        private_comment_owner=logged_in_staff, 
                        private_comment= father_private_comment
                    )
                else:
                    seshat_private_comment_part = SeshatPrivateCommentPart(
                    private_comment_part_text=f"I have coded a new record for the variable '{new_object.name}' on the polity: '{new_object.polity}'. I would appreciate it if you could review it.",
                    private_comment_owner=logged_in_staff, 
                    private_comment= father_private_comment
                )

                # print("####################", new_object)
                # print(seshat_private_comment_part)
                # print(father_private_comment)

                seshat_private_comment_part.save()

                seshat_private_comment_part.private_comment_reader.add(*suggested_experts) 
            
            new_object.expert_reviewed = False
            # Save ManyToMany relationships
            new_object.save()  # Save the object to persist the association

            #new_object.curator.set([logged_in_staff]) 
            #print(logged_in_staff)
            existing_curators = list(new_object.curator.all())  # Get current curators as a list
            #existing_ra_checks = list(new_object.ra_check.all())  # Get current ra_checks as a list
            #all_ra_checks_names_2 = []
            #for aa in existing_ra_checks:
            #    all_ra_checks_names_2.append(aa.name)
            #print('gggggggggggggggg', '; '.join(all_ra_checks_names_2))

            new_object.save()  # Save the object to persist the association

            my_form.save_m2m()

            #new_object.curator.add(logged_in_staff)
            #new_object.curator.add(logged_in_staff)
            if logged_in_staff not in existing_curators:
                existing_curators.append(logged_in_staff)  # Add only if not already present
            new_object.curator.set(existing_curators)  # Update the ManyToMany field


            #new_object.ra_check.add(logged_in_staff)
            #new_object.ra_check.add(logged_in_staff)
            # existing_ra_checks = []
            # for a_ra_check in all_ra_checks:
            #     #if a_ra_check not in existing_ra_checks:
            #     existing_ra_checks.append(a_ra_check)  # Add only if not already present
            # new_object.ra_check.set(existing_ra_checks)  




            new_object.save()  # Save the object to persist the association

            
            action = request.POST.get('action')
            if action == 'redirect_one':
                url = reverse("polity-detail-main", kwargs={'pk': new_object.polity.id}) + f"#{x_name}_{new_object.id}"
                #print('qqqqqqqqqqqq')

                return redirect(url)
                #return redirect("polity-detail-main", pk=new_object.polity.id) + "#{x_name}"
            elif action == 'redirect_two':
                #print('3333333333333333')
                # if the object has some description already
                if new_object.comment:
                    return redirect(f"seshatcomment-update", pk=new_object.comment.id) 
                else:
                    return redirect(f"{x_name}-detail", pk=new_object.id) 
                 # Replace 'success_url_name' with your success URL


            # Add the current user as a curator if they are an instance of Seshat_Expert
            # logged_in_user = request.user

            # try:
            #     seshat_staff_instance = Seshat_Expert.objects.get(user=logged_in_user)
            # except:
            #     seshat_staff_instance = None
            # if seshat_staff_instance:
            #     print("Alllllllloooooooooooooooo: ", logged_in_user)
            #     new_object.curator.add(seshat_staff_instance)
            #return redirect(f"{x_name}-detail", pk=my_object.id)



#################################   
        #print('yyyyyyyyyyyyyy ', coded_value)
        #print('yyyyyyyyyyyyyy ', my_object.comment)
        if coded_value in ['instability_event'] and not my_object.comment:

            # if "submit_with_formset" in request.POST:
            #     form_inline_new = SeshatCommentPartForm2(request.POST)
            # else:
            #     form_inline_new = SeshatCommentPartForm2()  # Unbound formset (won't be validated)                  
            form_inline_new = SeshatCommentPartForm2(request.POST)
            #action = request.POST.get('action_comment')
            if "submit_with_formset" in request.POST:
                big_father = SeshatComment.objects.create(text='')
                #big_father = SeshatComment.objects.get(id=com_id)
                com_id = big_father.pk
                model_class = apps.get_model(app_label=db_section, model_name=x_name)

                model_instance = get_object_or_404(model_class, id=object_id)
                model_instance.comment = big_father

                logged_in_user = request.user


                try:
                    seshat_staff_instance = Seshat_Expert.objects.get(user=logged_in_user)
                except:
                    seshat_staff_instance = None
                
                model_instance.curator.add(seshat_staff_instance)

                model_instance.save()
                if form_inline_new.is_valid():
                    comment_text = form_inline_new.cleaned_data['comment_text']
                    comment_order = form_inline_new.cleaned_data['comment_order']



                    seshat_comment_part = SeshatCommentPart(comment_part_text=comment_text, comment_order=1, comment_curator=seshat_staff_instance, comment= big_father)

                    seshat_comment_part.save()

                    # Process the formset
                    reference_formset = ReferenceFormSet2(request.POST, prefix='refs')
                    if reference_formset.is_valid():
                        to_be_added = []
                        to_be_deleted_later = []
                        for reference_form in reference_formset:
                            if reference_form.is_valid():
                                try:
                                    reference = reference_form.cleaned_data['ref']
                                    page_from = reference_form.cleaned_data['page_from']
                                    page_to = reference_form.cleaned_data['page_to']
                                    to_be_deleted = reference_form.cleaned_data['DELETE']
                                    parent_pars_inserted = reference_form.cleaned_data['parent_pars']


                                    # Get or create the Citation instance
                                    if page_from and page_to:
                                        citation, created = Citation.objects.get_or_create(
                                            ref=reference,
                                            page_from=int(page_from),
                                            page_to=int(page_to)
                                        )
                                    elif page_from:
                                        citation, created = Citation.objects.get_or_create(
                                            ref=reference,
                                            page_from=int(page_from),
                                            page_to=int(page_from)
                                        )
                                    elif page_to:
                                        citation, created = Citation.objects.get_or_create(
                                            ref=reference,
                                            page_from=int(page_to),
                                            page_to=int(page_to)
                                        )
                                        #print(page_from, "AAAAAAAAAAAAAAAAAAAAND ", page_to)
                                    else:
                                        citation, created = Citation.objects.get_or_create(
                                            ref=reference,
                                            page_from=None,
                                            page_to=None
                                        )

                                    # Associate the Citation with the SeshatCommentPart
                                    if to_be_deleted:
                                        #comment_part.comment_citations.remove(citation)
                                        to_be_deleted_later.append((citation, parent_pars_inserted))
                                    else:
                                        #comment_part.comment_citations.add((citation, parent_pars_inserted))
                                        to_be_added.append((citation, parent_pars_inserted))
                                except:
                                    # print("Formset errors:", reference_formset.errors)  # Errors per form
                                    # print("Non-form errors:", reference_formset.non_form_errors())  
                                    pass  # Handle the exception as per your requirement

                        # seshat_comment_part.comment_citations.clear()
                        # seshat_comment_part.comment_citations.add(*to_be_added)
                        seshat_comment_part.comment_citations_plus.clear()
                        #seshat_comment_part.comment_citations_plus.add(*to_be_added)

                        for item in to_be_added:
                            # Query for an existing row based on citation and SeshatCommentPart
                            scp_through_ctn, created = ScpThroughCtn.objects.get_or_create(
                                seshatcommentpart=seshat_comment_part,
                                citation=item[0],
                                defaults={'parent_paragraphs': item[1]}  # Set defaults including parent_paragraphs
                            )

                            # If the row already exists, update its parent_paragraphs
                            if not created:
                                scp_through_ctn.parent_paragraphs = item[1]
                                scp_through_ctn.save()
                    #print("ALOOOOOOOOOOOOOOOOOOO: ", len(reference_formset))

                    # Check which button was clicked
                    action = request.POST.get('action_comment')
                    if action == 'redirect_one':
                        #print('11111111111111')
                        return redirect(request.META.get('HTTP_REFERER', 'seshat-index')) 
                        #return redirect(reverse('seshatcommentpart-create2', kwargs={'com_id': com_id, 'subcom_order': 2}))
                        # href="{% url 'seshatcommentpart-create2' com_id=subcom.comment_id subcom_order=subcom.comment_order|add:1 %}" 
                        #return redirect('your_first_url_name')  # Replace with your actual URL
                    elif action == 'redirect_two':
                        #print('222222222222222222222')

                        #return redirect('your_second_url_name')  # Replace with yours
                        return redirect(reverse('seshatcomment-update', kwargs={'pk': com_id}))
            #print('555555555555')
            url = reverse("polity-detail-main", kwargs={'pk': new_object.polity.id}) + f"#{x_name}_{new_object.id}"
            return redirect(url)
            #return redirect(request.META.get('HTTP_REFERER', 'seshat-index')) 
        elif coded_value in ['instability_event'] and my_object.comment:
            url = reverse("polity-detail-main", kwargs={'pk': new_object.polity.id}) + f"#{x_name}_{new_object.id}"
            return redirect(url)
        else:
            form_inline_new = None



#####################################################
        # Prepare the context for invalid form
        context = {
            'form': my_form,
            'object': my_object,
            'delete_url': delete_url_name,
            "myvar": myvar,
            'var_section': var_section,
            'var_subsection': var_subsection,
            'db_section_mapper': db_section_mapper[db_section],
            "my_exp": my_exp,
            'another_form': another_form,

            #'expert_reviewed_by_me': my_form['expert_reviewed_by_me']

        }

        if coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall']:
            context.update({
                'extra_var': my_form[x_name_with_from],
                'extra_var2': my_form[x_name_with_to],
            })
        elif coded_value in ['preceding_entity']:
            context.update({
                'extra_var': my_form['other_polity'],
                'extra_var2': my_form['merged_old_data'],
                'extra_var3': my_form['relationship_to_preceding_entity'],
            })
        elif coded_value in ['widespread_religion']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
            })
        elif coded_value in ['power_transition']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
                'extra_var11': my_form[x_name_11],
                'extra_var12': my_form[x_name_12],
                'extra_var13': my_form[x_name_13],
                'extra_var14': my_form[x_name_14],
            })
        elif coded_value in ['instability_event']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
                'form_com': form_inline_new,

            })
        elif x_name in ['lux_precious_metal'] and db_section == 'ec':
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
                'extra_var11': my_form[x_name_11],
            })
        elif db_section == 'ec':
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
            })
        elif coded_value in ['suprapolity_relations']:
            context.update({
                'extra_var': my_form['supra_polity_relations'],
                'extra_var2': my_form['other_polity'],

            })
        elif coded_value in ['duration', 'peak_years', 'scale_of_supracultural_interaction']:
            context.update({
                'extra_var': my_form[x_name_with_from],
                'extra_var2': my_form[x_name_with_to],
            })
        elif coded_value in ['capital',]:
            context.update({
                'extra_var': my_form['polity_cap'], 
                'extra_var2': my_form[coded_value], 
            })
        else:
            context.update({
                'extra_var': my_form[coded_value],
            })
    else:
        # Handle GET request (initial form load)
        my_form = form_class(instance=my_object)

        init_data = ReferenceFormSet2(prefix='refs')
        if  coded_value in ['instability_event'] and not my_object.comment:
            form_inline_new = SeshatCommentPartForm2(initial={'comment_text': my_object.llm_description})
        else:
            form_inline_new = None



        #init_data = ReferenceFormSet2(prefix='refs')
        #form_inline_new.formset = init_data

        #print(form_inline_new.formset)

        context = {
            'form': my_form,
            'object': my_object,
            'delete_url': delete_url_name,
            "myvar": myvar,
            'var_section': var_section,
            'var_subsection': var_subsection,
            'db_section_mapper': db_section_mapper[db_section],
            "my_exp": my_exp,
            'another_form': another_form,
            'form_com': form_inline_new,
            #'com_id': com_id,  # Include com_id in the context
            'subcom_order': 1,  # Include subcom_order in the context
            #'formset': init_data, 
            #'reference_formset': init_data, 

            #'expert_reviewed_by_me': my_form['expert_reviewed_by_me']

        }

        if coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall']:
            context.update({
                'extra_var': my_form[x_name_with_from],
                'extra_var2': my_form[x_name_with_to],
            })
        elif coded_value in ['preceding_entity']:
            context.update({
                'extra_var': my_form['other_polity'],
                'extra_var2': my_form['merged_old_data'],
                'extra_var3': my_form['relationship_to_preceding_entity'],
            })
        elif coded_value in ['widespread_religion']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
            })
        elif coded_value in ['power_transition']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
                'extra_var11': my_form[x_name_11],
                'extra_var12': my_form[x_name_12],
                'extra_var13': my_form[x_name_13],
                'extra_var14': my_form[x_name_14],

            })
        elif coded_value in ['instability_event']:
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
            })
        elif x_name in ['lux_precious_metal'] and db_section == 'ec':
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
                'extra_var11': my_form[x_name_11],
            })
        elif db_section == 'ec':
            context.update({
                'extra_var': my_form[x_name_1],
                'extra_var2': my_form[x_name_2],
                'extra_var3': my_form[x_name_3],
                'extra_var4': my_form[x_name_4],
                'extra_var5': my_form[x_name_5],
                'extra_var6': my_form[x_name_6],
                'extra_var7': my_form[x_name_7],
                'extra_var8': my_form[x_name_8],
                'extra_var9': my_form[x_name_9],
                'extra_var10': my_form[x_name_10],
            })
        elif coded_value in ['suprapolity_relations']:
            context.update({
                'extra_var': my_form['supra_polity_relations'],
                'extra_var2': my_form['other_polity'],

            })
        elif coded_value in ['duration', 'peak_years', 'scale_of_supracultural_interaction']:
            context.update({
                'extra_var': my_form[x_name_with_from],
                'extra_var2': my_form[x_name_with_to],
            })
        elif coded_value in ['capital',]:
            context.update({
                'extra_var': my_form['polity_cap'], 
                'extra_var2': my_form[coded_value], 
            })
        else:
            context.update({
                'extra_var': my_form[coded_value],
            })
    if coded_value in ['instability_event']:
        return render(request, 'core/generic_templates/generic_update_llm.html', context)
    else:
        return render(request, 'core/generic_templates/generic_update.html', context)


# def generic_list_view_old(request, model_class, var_name, var_name_display, var_section, var_subsection, db_section, var_main_desc):
#     if var_name in ["widespread_religion",]:
#         object_list = model_class.objects.all().order_by('polity_id', 'order')
#     else:
#         object_list = model_class.objects.all()
#     #extra_var_dict = {obj.id: obj.__dict__.get(var_name) for obj in object_list}
#     extra_var_dict = {obj.id: obj.show_value() for obj in object_list}

#     orderby = request.GET.get('orderby', None)

#     # Apply sorting if orderby is provided and is a valid field name
#     if orderby and hasattr(model_class, orderby):
#         object_list = object_list.order_by(orderby)

#     var_name_with_from = var_name
#     var_exp_new = f'The absence or presence of "{var_name_display}" for a polity.'

#     # if var_name in ["official_religion", "elites_religion",]:
#     #     ordering_tag_value = "coded_value_id"
#     # #     # ?orderby=formal_legal_code&orderby2=tag
#     # elif var_name in ["widespread_religion",]:
#     #     ordering_tag_value = "order"
#     # else:
#     #     ordering_tag_value = "coded_value"

#     # Define any additional context variables you want to pass to the template
#     context = {
#         'object_list': object_list,
#         'var_name': var_name,
#         'create_url': f'{var_name}-create',
#         'update_url': f'{var_name}-update',
#         'update_url_new': f'{var_name}-updatenew',
#         'download_url': f'{var_name}-download',
#         'pagination_url': f'{var_name}s',
#         'metadownload_url':  f'{var_name}-metadownload',
#         'list_all_url':  f'{var_name}s_all',
#         'var_name_display': var_name_display,
#         'ordering_tag': f"?orderby={var_name}",
#         'var_section': var_section,
#         'var_subsection': var_subsection,
#         'var_main_desc': var_main_desc,
#         'myvar': var_name_display,
#         'extra_var_dict': extra_var_dict,  # Add the dictionary to the context
#         #'extra_var': obj[var_name],

#         #'obj_var': my_form[x_name], 
#         #"myvar": myvar,
#         #"my_exp": my_exp,
#     }


#     context["inner_vars"] = {
#         var_name_display: {
#             'min': None,
#             'max': None,
#             'scale': None, 
#             'var_exp_source': None, 
#             'var_exp': var_exp_new,
#             'units': None, 
#             'choices': 'ABSENT_PRESENT_CHOICES', 
#             'null_meaning': None}}

#     return render(request, 'core/generic_templates/generic_list_all.html', context)

#from seshat.utils.utils import list_variable_hierarchies


def generic_list_view(request, model_class, var_name, coded_value, var_name_display, var_section, var_subsection, db_section, var_main_desc):
    # Only enforce authentication and permissions if db_section is not 'rt'
    # special case of RT:
    #rows = list_variable_hierarchies()



    rt_allowed_polities = ["kh_chenla", "pe_wari_emp", "in_kampili_k", "in_kalyani_chalukya_emp", "in_hoysala_k", "et_aksum_emp_3", "et_aksum_emp_2", "ni_proto_yoruboid", "ni_sokoto", "gm_kaabu_emp"]

    if var_name in ["widespread_religion",]:
        object_list = model_class.objects.all().order_by('polity_id', 'order')
    elif var_name in ["instability_event",]:
        object_list = model_class.objects.filter(polity__unreliable_instability_events=False).defer('general_cot', 'classification_cot', 'sorokin_rationale', 'llm_description').order_by('polity_id', 'year_from', 'id')
    else:
        object_list = model_class.objects.all().order_by('polity_id', 'year_from')



    year_from_min = request.GET.get('year_from_min')
    year_to_max = request.GET.get('year_to_max')
    created_before = request.GET.get('created_before')
    selected_batch = request.GET.get('selected_batch')
    polity_id = request.GET.get('polity')
    inst_type_ids = request.GET.getlist("inst_type")  # handles multiple selections
    ra_check_ids = request.GET.getlist("ra_check")
    inst_extent = request.GET.get("inst_extent")
    inst_intensity = request.GET.get("inst_intensity")
    selected_macro = request.GET.get('macro_event')

    name_query = request.GET.get('searched_name', '').strip()



    if inst_type_ids:
        object_list = object_list.filter(inst_type__in=inst_type_ids).distinct()

    if ra_check_ids:
        object_list = object_list.filter(ra_check__in=ra_check_ids).distinct()

    if inst_extent:
        object_list = object_list.filter(inst_extent=inst_extent)

    if inst_intensity:
        object_list = object_list.filter(inst_intensity=inst_intensity)

    if polity_id:
        object_list = object_list.filter(polity__id=polity_id)

    
    # Filter manually if selected
    if selected_macro:
        desired_str = '(macro event: ' + selected_macro.lower()
        object_list = object_list.filter(llm_name__icontains=desired_str)

    if name_query:
        object_list = object_list.filter(name__icontains=name_query)


    # Annotate fallback values
    object_list = object_list.annotate(
        start_year_effective=Coalesce('year_from', F('polity__start_year')),
        end_year_effective=Coalesce('year_to', F('polity__end_year')),
    )

    if year_from_min:
        object_list = object_list.filter(start_year_effective__gte=int(year_from_min))

    if year_to_max:
        object_list = object_list.filter(end_year_effective__lte=int(year_to_max))

    if created_before:
        parsed_date = parse_date(created_before)
        if parsed_date:
            object_list = object_list.filter(created_date__lt=parsed_date)


    if selected_batch:
        if selected_batch == "Batch 1":
            object_list = object_list.filter(created_date__lt=BATCH_1_END)
        elif selected_batch == "Batch 2":
            object_list = object_list.filter(
                created_date__gte=BATCH_1_END,
                created_date__lt=BATCH_2_END
            )
        elif selected_batch == "Batch 3":
            object_list = object_list.filter(created_date__gte=BATCH_2_END)


    #extra_var_dict = {obj.id: obj.__dict__.get(var_name) for obj in object_list}

    if coded_value in ['instability_event',]:
        extra_var_dict = {}
    elif coded_value == "suprapolity_relations":
        extra_var_dict = {obj.id: obj.display_value_2() for obj in object_list}
    #elif var_name == "lux_precious_metal":
    #    extra_var_dict = {obj.id: obj.display_table_value() for obj in #object_list}
    elif db_section == "ec":
        extra_var_dict = {obj.id: obj.display_table_value() for obj in object_list}
    elif coded_value == "preceding_entity":
        extra_var_dict = {obj.id: obj.display_value() for obj in object_list}
    else:
        extra_var_dict = {obj.id: obj.show_value() for obj in object_list}

    orderby = request.GET.get('orderby', None)
    is_descending = False

    if var_name in ['instability_event',]:
        object_list = object_list.annotate(
            inst_intensity_num=Cast(F('inst_intensity'), output_field=IntegerField()),
            inst_extent_num=Cast(F('inst_extent'), output_field=IntegerField())
        )



    if orderby:   
        if orderby.lstrip('-') == 'year_from':
            field = 'start_year_effective'
        elif orderby.lstrip('-') == 'year_to':
            field = 'end_year_effective'
        else:
            field = orderby.lstrip('-')

        # Handle descending
        if orderby in ['inst_intensity', '-inst_intensity']:
            order_field = 'inst_intensity_num'
            if orderby.startswith('-'):
                object_list = object_list.order_by(F(order_field).desc())
                is_descending = True
            else:
                object_list = object_list.order_by(F(order_field).asc())
                is_descending = False

        elif orderby in ['inst_extent', '-inst_extent']:
            order_field = 'inst_extent_num'
            if orderby.startswith('-'):
                object_list = object_list.order_by(F(order_field).desc())
                is_descending = True
            else:
                object_list = object_list.order_by(F(order_field).asc())
                is_descending = False
        elif orderby.startswith('-'):
            object_list = object_list.order_by(F(field).desc(nulls_last=True))
            is_descending = True
        else:
            object_list = object_list.order_by(F(field).asc(nulls_last=True))
            is_descending = False

        order_field = orderby
    else:
        order_field = None

    # Apply sorting if orderby is provided and is a valid field name
    #if orderby and hasattr(model_class, orderby):
    #    object_list = object_list.order_by(orderby)

    if db_section == 'rt' and not request.user.has_perm('core.add_capital'):
        if model_class in {Widespread_religion, Official_religion, Elites_religion, Theo_sync_dif_rel, Sync_rel_pra_ind_beli, Religious_fragmentation, Gov_vio_freq_rel_grp, Gov_res_pub_wor, Gov_res_pub_pros, Gov_res_conv, Gov_press_conv, Gov_res_prop_own_for_rel_grp, Tax_rel_adh_act_ins, Gov_obl_rel_grp_ofc_reco, Gov_res_cons_rel_buil, Gov_res_rel_edu, Gov_res_cir_rel_lit, Gov_dis_rel_grp_occ_fun, Soc_vio_freq_rel_grp, Soc_dis_rel_grp_occ_fun, Gov_press_conv_for_aga}:
            object_list = object_list.filter(polity__new_name__in=rt_allowed_polities)


    # if db_section == 'ec' and not request.user.has_perm('core.add_capital'):
    #     #return HttpResponseForbidden("You do not have permission to access this data.")
    #     return render(request, 'core/permission_denied.html', status=403)

    if var_name in ['power_transition', 'instability_event'] and not request.user.has_perm('core.add_seshatprivatecommentpart'):

        #return HttpResponseForbidden("You do not have permission to access this data.")
        return render(request, 'core/permission_denied.html', status=403)
    
    var_name_with_from = var_name
    var_exp_new = f'The absence or presence of "{var_name_display}" for a polity.'

    # if var_name in ["official_religion", "elites_religion",]:
    #     ordering_tag_value = "coded_value_id"
    # #     # ?orderby=formal_legal_code&orderby2=tag
    # elif var_name in ["widespread_religion",]:
    #     ordering_tag_value = "order"
    # else:
    #     ordering_tag_value = "coded_value"

    if coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall']:
        good_ordering_tag = coded_value + "_from"
    else:
        good_ordering_tag = coded_value 


    # Define any additional context variables you want to pass to the template
    context = {
        'object_list': object_list,
        'var_name': var_name,
        'create_url': f'{var_name}-create',
        'update_url': f'{var_name}-update',
        'update_url_new': f'{var_name}-updatenew',
        'download_url': f'{var_name}-download',
        'json_download_url': f'{var_name}-json-download',
        'pagination_url': f'{var_name}s',
        'metadownload_url':  f'{var_name}-metadownload',
        'list_all_url':  f'{var_name}s_all',
        'var_name_display': var_name_display,
        'ordering_tag': f"?orderby={good_ordering_tag}",
        'des_ordering_tag': f"?orderby=-{good_ordering_tag}",
        'var_section': var_section,
        'var_subsection': var_subsection,
        'var_main_desc': var_main_desc,
        'myvar': var_name_display,
        'extra_var_dict': extra_var_dict,  # Add the dictionary to the context
        #'extra_var': obj[var_name],
        'current_order_field': order_field,
        'is_descending': is_descending,
        'db_section': db_section,

        #'obj_var': my_form[x_name], 
        #"myvar": myvar,
        #"my_exp": my_exp,
    }



    if var_name in ['instability_event',]:
        all_object_list = model_class.objects.filter(polity__unreliable_instability_events=False)
        polity_ids_in_list = all_object_list.values_list('polity_id', flat=True).distinct()
    else:
        all_object_list = model_class.objects.all()
        polity_ids_in_list = all_object_list.values_list('polity_id', flat=True).distinct()

    if var_name in ['instability_event',]:
        paginator = Paginator(object_list, 50)  # Show 100 items per page

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        paginated = True
        context['page_obj'] = page_obj
        context['paginated'] = paginated
        context["instability_types"] = Instability_type.objects.all()
        context["check_choices"] = Check_choice.objects.all()
        macro_events = sorted(set(obj.made_up_macro_event for obj in all_object_list if obj.made_up_macro_event))

        # Get all macro events from the objects
        macro_event_list = [obj.made_up_macro_event for obj in all_object_list if obj.made_up_macro_event]
        macro_event_counts = Counter(macro_event_list)

        # Sort alphabetically by macro event name
        macro_events_with_counts = sorted(macro_event_counts.items(), key=lambda x: (-x[1], x[0]))

        context["macro_events_with_counts"] = macro_events_with_counts

        context["INST_EXTENT_CHOICES"] = INST_EXTENT_CHOICES
        context["INST_INTENSITY_CHOICES"] = INST_INTENSITY_CHOICES
        context["selected_macro"] = selected_macro
        context["macro_events"] = macro_events
        context["name_query"] = name_query

        
        context["selected_inst_type_ids"] = inst_type_ids
        context["selected_ra_check_ids"] = ra_check_ids

    elif var_name in ['widespread_religion',]:
        paginator = Paginator(object_list, 100)  # Show 100 items per page

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        paginated = True
        context['page_obj'] = page_obj
        context['paginated'] = paginated
    else:
        context['page_obj'] = object_list
        context['paginated'] = False



    # After applying all filters to object_list
    polities = Polity.objects.filter(id__in=polity_ids_in_list).order_by('new_name')

    if var_name in ['instability_event',]:
        my_polities = []
        for polity in polities:
            events = model_class.objects.filter(polity=polity).values_list('created_date', flat=True).distinct()
            batches = set()

            for created in events:
                batch = get_batch_tag(created.date())
                batches.add(batch)

            # Convert to sorted list for display order
            batch_list = sorted(batches, key=lambda t: ["Batch 1", "Batch 2", "Batch 3"].index(t))
            setattr(polity, 'batch_list', batch_list)
            my_polities.append(polity)
            context['polities'] = my_polities
            context['unreliable_polities'] = Polity.objects.filter(unreliable_instability_events=True).order_by('new_name')

    else:
        context['polities'] = polities
        context['unreliable_polities'] = None


    context["inner_vars"] = {
        var_name_display: {
            'min': None,
            'max': None,
            'scale': None, 
            'var_exp_source': None, 
            'var_exp': var_exp_new,
            'units': None, 
            'choices': 'ABSENT_PRESENT_CHOICES', 
            'null_meaning': None}}


    if coded_value in ['instability_event']:
        return render(request, 'core/generic_templates/generic_list_llm.html', context)
    else:
        return render(request, 'core/generic_templates/generic_list_all.html', context)
    #return render(request, 'core/generic_templates/generic_list_all.html', context)



@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def confirm_delete_view(request, model_class, pk, var_name):
    permission_required = 'core.add_capital'
    
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    # Check if the user has the required permission
    if not request.user.has_perm(permission_required):
        return HttpResponseForbidden("You don't have permission to delete this object.")

    template_name = "core/confirm_delete.html"
    
    context = {
        'var_name': var_name,
        'obj': obj,
        'delete_object': f'{var_name}-delete',
    }

    return render(request, template_name, context)

@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def delete_object_view(request, model_class, pk, var_name):
    permission_required = 'core.add_capital'
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    if not request.user.has_perm(permission_required):
        return HttpResponseForbidden("You don't have permission to delete this object.")
    
    # Delete the object
    obj.delete()
    
    # Redirect to the success URL
    success_url_name = f'{var_name}s_all'  # Adjust the success URL as needed
    success_url = reverse(success_url_name)
    
    # Display a success message
    messages.success(request, f"{var_name} has been deleted successfully.")
    
    return redirect(success_url)

@login_required
def generic_download(request, model_class, var_name, x_name, var_section, var_subsection,coded_value, db_section):
    # Fetch all objects for the specified model
    #items = model_class.objects.all()

    if var_name in ["instability_event",]:
        items = model_class.objects.filter(polity__unreliable_instability_events=False)
    else:
        items = model_class.objects.all()

    # special case of RT:
    rt_allowed_polities = ["kh_chenla", "pe_wari_emp", "in_kampili_k", "in_kalyani_chalukya_emp", "in_hoysala_k", "et_aksum_emp_3", "et_aksum_emp_2", "ni_proto_yoruboid", "ni_sokoto", "gm_kaabu_emp"]

    if db_section == 'rt' and not request.user.has_perm('core.add_capital'):  # Assuming 'view_all_polities' is the relevant permission
        if model_class in {Widespread_religion, Official_religion, Elites_religion, Theo_sync_dif_rel, Sync_rel_pra_ind_beli, Religious_fragmentation, Gov_vio_freq_rel_grp, Gov_res_pub_wor, Gov_res_pub_pros, Gov_res_conv, Gov_press_conv, Gov_res_prop_own_for_rel_grp, Tax_rel_adh_act_ins, Gov_obl_rel_grp_ofc_reco, Gov_res_cons_rel_buil, Gov_res_rel_edu, Gov_res_cir_rel_lit, Gov_dis_rel_grp_occ_fun, Soc_vio_freq_rel_grp, Soc_dis_rel_grp_occ_fun, Gov_press_conv_for_aga}:
            items = items.filter(polity__new_name__in=rt_allowed_polities)

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    db_section_mapper = {
        'general': 'general',
        'sc': 'social_complexity',
        'wf': 'warfare',
        'ec': 'Economy',
        'rt': 'religion_tolerance',
        'crisisdb': 'crisisdb',
    }
    file_name = f"{db_section_mapper[db_section]}_{var_name}_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # if var_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
    #     var_name_with_from = var_name + "_from"
    #     var_name_with_to = var_name + "_to"
    # else:
    #     var_name_with_from = var_name
    #     var_name_with_to = None

    writer = csv.writer(response, delimiter='|')

    for loop_number, objj in enumerate(items):
        # convert to dict
        obj = model_to_dict(objj)  # Convert the object to a dictionary

        ##################

        if coded_value == "power_transition":
            x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10, x_name_11, x_name_12  =  'name', 'predecessor', 'successor', 'contested', 'overturn', 'predecessor_assassination', 'intra_elite', 'military_revolt', 'popular_uprising', 'separatist_rebellion', 'external_invasion', 'external_interference', 
        elif coded_value == "preceding_entity":
            x_name, x_name_2, x_name_3, x_name_4, x_name_5  = "other_polity", "merged_old_data", "relationship_to_preceding_entity", 'preceding_polity_new_ID', 'preceding_polity_long_name'
        elif coded_value == "widespread_religion":
            x_name_1, x_name_2, x_name_3 = "order", "widespread_religion", "degree_of_prevalence"
        elif x_name == "lux_precious_metal":
            x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10, x_name_11 =  'name', 'coded_value', 'place_of_provenance_str', 'ruler_consumption', 'ruler_consumption_tag', 'elite_consumption', 'elite_consumption_tag', 'common_people_consumption', 'common_people_consumption_tag', 'which_metals', 'place_of_provenance_pol'
        elif x_name == "instability_event":
            x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6,  x_name_7, x_name_8, x_name_9, x_name_10 =  'name', 'inst_intensity', 'inst_extent', 'real_event_check', 'types', 'RA_checks', 'checking_status', 'sorokin_rationale', 'llm_description', 'made_up_macro_event'
        elif db_section == 'ec':
            x_name_1, x_name_2, x_name_3, x_name_4, x_name_5, x_name_6, x_name_7, x_name_8, x_name_9, x_name_10 =  'name', 'coded_value', 'place_of_provenance_str', 'ruler_consumption', 'ruler_consumption_tag', 'elite_consumption', 'elite_consumption_tag', 'common_people_consumption', 'common_people_consumption_tag', 'place_of_provenance_pol'
        elif coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall' ]:
            x_name_with_from = f'{x_name}_from'
            x_name_with_to = f'{x_name}_to'
        elif coded_value == 'duration':
            x_name_with_from = 'polity_year_from'
            x_name_with_to = 'polity_year_to'
        elif coded_value == 'peak_years':
            x_name_with_from = 'peak_year_from'
            x_name_with_to = 'peak_year_to'
        elif coded_value == 'scale_of_supracultural_interaction':
            x_name_with_from = 'scale_from'
            x_name_with_to = 'scale_to'




        coded_cols = {} 
        if coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', "administrative_level", "settlement_hierarchy", "religious_level", "military_level", "largest_communication_distance", "fastest_individual_communication", 'long_wall']:
            coded_cols.update({
                x_name_with_from: obj[x_name_with_from],
                x_name_with_to: obj[x_name_with_to],
            })
        elif coded_value in ['preceding_entity']:
            other_polity_name = objj.other_polity.new_name if objj.other_polity else None
            other_polity_long_name = objj.other_polity.long_name if objj.other_polity else None
            coded_cols.update({
                #x_name: obj['other_polity'],
                x_name_2: obj['merged_old_data'],
                x_name_3: obj['relationship_to_preceding_entity'],
                x_name_4: other_polity_name,
                x_name_5: other_polity_long_name,
            })
        elif db_section == 'rt' and  coded_value in ['widespread_religion']:
            coded_cols.update({
                x_name_2: objj.widespread_religion,
                x_name_3: objj.get_degree_of_prevalence_display(),
            })
        elif db_section == 'rt' and  x_name in ['official_religion', 'elites_religion']:
            coded_cols.update({
                'religion': objj.coded_value,
            })
        elif db_section == 'rt' and 'freq_' in x_name:
            coded_cols.update({
                'coded_value': objj.get_coded_value_display(),
            })
        elif db_section == 'rt':
            coded_cols.update({
                'coded_value': obj[coded_value],
            })
        elif coded_value in ['power_transition']:
            coded_cols.update({
                x_name_2: obj[x_name_2],
                x_name_3: obj[x_name_3],
                x_name_4: obj[x_name_4],
                x_name_5: obj[x_name_5],
                x_name_6: obj[x_name_6],
                x_name_7: obj[x_name_7],
                x_name_8: obj[x_name_8],
                x_name_9: obj[x_name_9],
                x_name_10: obj[x_name_10],
                x_name_11: obj[x_name_11],
                x_name_12: obj[x_name_12],
                x_name_1: obj[x_name_1],
            })
        elif x_name in ['instability_event']:
            check_status_tag = 'LLM'
            if objj.researchers_list() and objj.seshat_experts_list():
                check_status_tag = 'Expert Checked'
            elif objj.researchers_list() or objj.get_llm_instability_checks_str():
                check_status_tag = 'RA Checked'

            coded_cols.update({
                'event_name': obj[x_name_1],
                'macro_event': objj.made_up_macro_event,
                'year_from': obj['year_from'],
                'year_to': obj['year_to'],
                'intensity': obj[x_name_2],
                'extent': obj[x_name_3],
                'data_point': obj[x_name_4],
                x_name_5: objj.get_instability_types_str(),
                x_name_6: objj.get_llm_instability_checks_str(),
                x_name_7: check_status_tag,
                'rationale': obj[x_name_8],
                x_name_9: obj[x_name_9],
                'batch_number': objj.batch_number,
            })
        elif x_name == "lux_precious_metal":
            place_pols = []
            if obj[x_name_11]:
                for item in obj[x_name_11]:
                    place_pols.append(item.new_name)
            
            place_pols_str = ";".join(place_pols)

            metals_str = []
            if obj[x_name_10]:
                for my_item in obj[x_name_10]:
                    metals_str.append(my_item.metal)
            
            metals_str_str = ";".join(metals_str)


            coded_cols.update({
                x_name_2: obj[x_name_2],
                x_name_10: metals_str_str,
                x_name_3: obj[x_name_3],
                x_name_11: place_pols_str,
                x_name_4: obj[x_name_4],
                x_name_5: obj[x_name_5],
                x_name_6: obj[x_name_6],
                x_name_7: obj[x_name_7],
                x_name_8: obj[x_name_8],
                x_name_9: obj[x_name_9],
            })
        elif db_section == 'ec':
            place_pols = []
            if obj[x_name_10]:
                for item in obj[x_name_10]:
                    place_pols.append(item.new_name)
            
            place_pols_str = ";".join(place_pols)


            coded_cols.update({
                x_name_2: obj[x_name_2],
                x_name_3: obj[x_name_3],
                x_name_10: place_pols_str,
                x_name_4: obj[x_name_4],
                x_name_5: obj[x_name_5],
                x_name_6: obj[x_name_6],
                x_name_7: obj[x_name_7],
                x_name_8: obj[x_name_8],
                x_name_9: obj[x_name_9],
                #x_name_1: obj[x_name_1],
            })
        elif coded_value in ['suprapolity_relations']:
            coded_cols.update({
                x_name: obj['supra_polity_relations'],
                x_name_2: obj['other_polity'],

            })
        elif coded_value in ['duration', 'peak_years', 'scale_of_supracultural_interaction']:
            coded_cols.update({
                x_name_with_from: obj[x_name_with_from],
                x_name_with_to: obj[x_name_with_to],
            })
        elif coded_value in ['capital',]:
            coded_cols.update({
                x_name: obj['polity_cap'], 
                x_name_2: obj[coded_value], 
            })
        else:
            coded_cols.update({
                x_name: obj[coded_value],
            })


        ############

        if objj.seshat_experts_list():
            is_expert_reviewed = True
        else:
            is_expert_reviewed = False

        if x_name in ['instability_event']:
            sublist_1_row = ['variable_set', 'variable_name', 'polity_name', 'polity_new_ID',]
        else:
            sublist_1_row = ['variable_set', 'section', 'subsection', 'variable_name', 'polity_name', 'polity_new_ID',]

        # special case of widespread religion. Merge order into variable name
        if coded_value in ['widespread_religion'] and  objj.polity:
            sublist_1 = [db_section_mapper[db_section].replace('_', ' ').title(), var_section, var_subsection, objj.clean_name_dynamic(), objj.polity.long_name, objj.polity.new_name,]
        elif db_section == 'rt' and objj.polity:
            sublist_1 = [db_section_mapper[db_section].replace('_', ' ').title(), var_section, var_subsection, objj.clean_name_spaced(), objj.polity.long_name, objj.polity.new_name,]
        elif x_name in ['instability_event'] and objj.polity:
            sublist_1 = [db_section_mapper[db_section].replace('_', ' ').title(), objj.clean_name_spaced(), objj.polity.long_name, objj.polity.new_name,]
        elif objj.polity:
            sublist_1 = [db_section_mapper[db_section].replace('_', ' ').title(), var_section, var_subsection, var_name.replace('_', ' ').title(), objj.polity.long_name, objj.polity.new_name,]
        else:
            sublist_1 = [db_section_mapper[db_section].replace('_', ' ').title(), var_section, var_subsection, var_name.replace('_', ' ').title(), '-', '-', '-',]


        if objj.clean_name_spaced() == 'Polity Duration' and objj.polity:
            sublist_3_row = ['confidence', 'is_disputed', 'is_uncertain', 'expert_checked',]
            sublist_3 = [objj.get_tag_display(), objj.is_disputed, objj.is_uncertain, is_expert_reviewed, ]
        elif coded_value in ['power_transition'] and objj.polity:
            sublist_3_row = ['transition_year', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked',]
            sublist_3 = [objj.year_to, objj.get_tag_display(), objj.is_disputed, objj.is_uncertain, is_expert_reviewed, ]
        elif x_name in ['instability_event'] and objj.polity:
            if objj.comment:
                ra_comment = objj.comment.__str__().replace('\n', ' ').replace('<br>', ' ').replace('\r', ' ')
            else:
                ra_comment= None
            sublist_3_row = ['llm_references', 'RA_approved_description', ]
            sublist_3 = [objj.get_llm_instability_refs_str().replace('<b>', '').replace('</b>', ''), ra_comment ]
        else:
            sublist_3_row = ['year_from', 'year_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked',]
            sublist_3 = [objj.year_from, objj.year_to, objj.get_tag_display(), objj.is_disputed, objj.is_uncertain, is_expert_reviewed, ]
        sublist_2 = []
        sublist_2_row = []


        for k, v in coded_cols.items():
            #if objj.clean_name_spaced() == 'Polity Duration':
            #    continue
            sublist_2_row.append(k)
            sublist_2.append(v)

        if loop_number == 0:
            writer.writerow(sublist_1_row + sublist_2_row + sublist_3_row)


        if objj.show_value() == "NO_VALUE_ON_WIKI" or objj.show_value() == "NO_VALID_VALUE":
            continue
        elif "O_VALUE_ON_WIKI" in str(objj.show_value()):
            continue
        else:
            writer.writerow(sublist_1 + sublist_2 + sublist_3)

    return response


def generic_json_download(request, model_class, var_name, x_name, var_section, var_subsection, coded_value, db_section):
    #items = model_class.objects.all()

    if var_name in ["instability_event",]:
        items = model_class.objects.filter(polity__unreliable_instability_events=False)
    else:
        items = model_class.objects.all()
    # Special case of RT filtering
    rt_allowed_polities = [
        "kh_chenla", "pe_wari_emp", "in_kampili_k", "in_kalyani_chalukya_emp", 
        "in_hoysala_k", "et_aksum_emp_3", "et_aksum_emp_2", "ni_proto_yoruboid", 
        "ni_sokoto", "gm_kaabu_emp"
    ]

    if db_section == 'rt' and not request.user.has_perm('core.add_capital'):  # Assuming 'view_all_polities' is the relevant permission
        if model_class in {Widespread_religion, Official_religion, Elites_religion, Theo_sync_dif_rel, Sync_rel_pra_ind_beli, Religious_fragmentation, Gov_vio_freq_rel_grp, Gov_res_pub_wor, Gov_res_pub_pros, Gov_res_conv, Gov_press_conv, Gov_res_prop_own_for_rel_grp, Tax_rel_adh_act_ins, Gov_obl_rel_grp_ofc_reco, Gov_res_cons_rel_buil, Gov_res_rel_edu, Gov_res_cir_rel_lit, Gov_dis_rel_grp_occ_fun, Soc_vio_freq_rel_grp, Soc_dis_rel_grp_occ_fun, Gov_press_conv_for_aga}:
            items = items.filter(polity__new_name__in=rt_allowed_polities)

    # Map database sections
    db_section_mapper = {
        'general': 'general',
        'sc': 'social_complexity',
        'wf': 'warfare',
        'ec': 'Economy',
        'rt': 'religion_tolerance',
        'crisisdb': 'crisisdb',
    }

    data_list = []

    if coded_value == 'preceding_entity':
        x_name_2 = 'merged_old_data'
        x_name_3 = 'relationship_to_preceding_entity'
        x_name_4 = 'other_polity_name'
        x_name_5 = 'other_polity_long_name'

    for objj in items:
        obj = model_to_dict(objj)  # Convert model instance to dictionary

        coded_cols = {}

        if coded_value in ['polity_population', 'polity_territory', 'population_of_the_largest_settlement', 
                           "administrative_level", "settlement_hierarchy", "religious_level", 
                           "military_level", "largest_communication_distance", "fastest_individual_communication", 
                           'long_wall']:
            coded_cols.update({
                f"{x_name}_from": obj.get(f"{x_name}_from"),
                f"{x_name}_to": obj.get(f"{x_name}_to"),
            })
        elif coded_value == "power_transition":
            coded_cols.update({
                "name": obj.get("name"),
                "predecessor": obj.get("predecessor"),
                "successor": obj.get("successor"),
                "contested": obj.get("contested"),
                "overturn": obj.get("overturn"),
                "predecessor_assassination": obj.get("predecessor_assassination"),
                "intra_elite": obj.get("intra_elite"),
                "military_revolt": obj.get("military_revolt"),
                "popular_uprising": obj.get("popular_uprising"),
                "separatist_rebellion": obj.get("separatist_rebellion"),
                "external_invasion": obj.get("external_invasion"),
                "external_interference": obj.get("external_interference"),
            })
        elif coded_value == "widespread_religion":
            coded_cols.update({
                "order": obj.get("order"),
                "widespread_religion": obj.get("widespread_religion"),
                "degree_of_prevalence": obj.get("degree_of_prevalence"),
            })

        elif coded_value == 'preceding_entity':
            other_polity_name = objj.other_polity.new_name if objj.other_polity else None
            other_polity_long_name = objj.other_polity.long_name if objj.other_polity else None
            polity_old_ID = objj.polity.name if objj.polity else None
            polity_new_ID = objj.polity.new_name if objj.polity else None
            polity_long_name = objj.polity.long_name if objj.polity else None
            coded_cols.update({
                x_name: obj.get('other_polity'),
                x_name_2: obj.get('merged_old_data'),
                x_name_3: obj.get('relationship_to_preceding_entity'),
                x_name_4: other_polity_name,
                x_name_5: other_polity_long_name,
            })  
        elif coded_value in ['duration', 'peak_years', 'scale_of_supracultural_interaction']:
            coded_cols.update({
                "from": obj.get(f"{coded_value}_from"),
                "to": obj.get(f"{coded_value}_to"),
            })
        elif coded_value == "capital":
            coded_cols.update({
                "polity_cap": obj.get("polity_cap"),
                "capital": obj.get("capital"),
            })
        else:
            coded_cols[x_name] = obj.get(coded_value)

        # Additional metadata
        data_entry = {
            "variable_set": db_section_mapper[db_section].replace('_', ' ').title(),
            "section": var_section,
            "subsection": var_subsection,
            "variable_name": var_name.replace('_', ' ').title(),
            "polity_name": polity_long_name,
            "polity_new_ID": polity_new_ID,
            "polity_old_ID": polity_old_ID,
            "year_from": objj.year_from,
            "year_to": objj.year_to,
            "confidence": objj.get_tag_display(),
            "is_disputed": objj.is_disputed,
            "is_uncertain": objj.is_uncertain,
            "expert_checked": bool(objj.seshat_experts_list()),  # Check if it has been reviewed
            "coded_values": coded_cols
        }

        # Exclude invalid entries
        if objj.show_value() not in ["NO_VALUE_ON_WIKI", "NO_VALID_VALUE"] and "O_VALUE_ON_WIKI" not in str(objj.show_value()):
            data_list.append(data_entry)

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{db_section_mapper[db_section]}_{var_name}_{current_datetime}.json"
    response = JsonResponse(data_list, safe=False)
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response

    # Return JSON response in browser
    #return JsonResponse(data_list, safe=False)


def generic_json_download_simple(request, model_class, var_name, x_name, var_section, var_subsection,coded_value, db_section):
    # Fetch all objects for the specified model
    #items = model_class.objects.all()

    if var_name in ["instability_event",]:
        items = model_class.objects.filter(polity__unreliable_instability_events=False)
    else:
        items = model_class.objects.all()

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"social_complexity_{var_name}_{current_datetime}.json"

    if var_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
        var_name_with_from = var_name + "_from"
        var_name_with_to = var_name + "_to"
    else:
        var_name_with_from = var_name
        var_name_with_to = None

    data_list = []
    
    for obj in items:
        entry = {
            "variable_name": obj.name,
            "year_from": obj.year_from,
            "year_to": obj.year_to,
            "polity_name": obj.polity.long_name,
            "polity_new_ID": obj.polity.new_name,
            "polity_old_ID": obj.polity.name,
            "confidence": obj.get_tag_display(),
            "is_disputed": obj.is_disputed,
            "is_uncertain": obj.is_uncertain,
            "expert_checked": obj.expert_reviewed,
            "DRB_reviewed": obj.drb_reviewed,
        }

        if var_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
            entry[var_name_with_from] = getattr(obj, var_name_with_from, '')
            entry[var_name_with_to] = getattr(obj, var_name_with_to, '')
        else:
            entry[var_name] = getattr(obj, var_name, '')

        data_list.append(entry)

    response = JsonResponse(data_list, safe=False)
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response


def generic_metadata_download(request, var_name, var_name_display, var_section, var_subsection, var_main_desc):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="metadata_{var_name}s.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': var_main_desc, 'main_desc_source': 'NOTHING', 'section': var_section, 'subsection': var_subsection}
    my_meta_data_dic_inner_vars = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': f'The {var_name_display} for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}

    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response