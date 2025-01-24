
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier
from django.db.models.base import Model
# from django.http.response import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from django.shortcuts import render, HttpResponse

import csv
import datetime


from django.http import HttpResponse


from django.apps import apps



from ..core.models import Polity

def ecvars(request):

    app_name = 'ec'  # Replace with your app name
    models_1 = apps.get_app_config(app_name).get_models()

    unique_politys = set()
    number_of_all_rows = 0
    number_of_variables = 0
    all_vars_grouped = {}

    all_sect_download_links = {}

    for model in models_1:
        model_name = model.__name__
        if model_name in ["Ra", 'Precious_metal'] or '_instance' in model_name:
            continue
        s_value = 'Luxury Goods'
        ss_value = None

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
        if model_name in ["Ra", 'Precious_metal'] or '_instance' in model_name:
            continue


        subsection_value = 'Luxury Goods'
        sub_subsection_value = None
        count = model.objects.count()
        pols_count = Polity.objects.count()
        number_of_all_rows += count
        model_title = model_name.replace("_", " ").title()
        model_create = model_name.lower() + "-create"
        model_download = model_name.lower() + "-download"
        model_metadownload = model_name.lower() + "-metadownload"
        model_all = model_name.lower() + "s_all"
        model_s = model_name.lower() + "s"

        queryset = model.objects.all()
        filtered_queryset_pres = 0
        filtered_queryset_abs = 0
        filtered_queryset_unk = 0
        filtered_queryset_sus_unk = 0
        filtered_queryset_unc = 0
        filtered_queryset_trans = 0

        politys = queryset.values_list('polity', flat=True).distinct()
        unique_politys.update(politys)
        polities_for_this_var = len(set(politys))


        if model_name.lower() in ['long_wall', ]:
            var_type= "RANGE"
            
            for obj in queryset:
                if obj.show_value() == "absent" and obj.tag == "TRS":
                    filtered_queryset_abs +=1
                elif obj.show_value() == "unknown" and obj.tag == "SSP":
                    filtered_queryset_sus_unk +=1
                elif obj.show_value() == 'uncoded' or obj.tag == "UND":
                    filtered_queryset_unc +=1
                elif obj.show_value() not in ['absent', 'unknwon', 'uncoded']:
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
                0, #filtered_queryset_trans,
                'Range was coded',
                ]

        elif model_name.lower() == 'xxx':
            var_type="TEXT"

            for obj in queryset:
                if obj.show_value() != ' - ':
                    filtered_queryset_pres +=1
                if obj.show_value() == "unknown" and obj.tag == "TRS":
                    filtered_queryset_unk +=1
                if obj.show_value() == "unknown" and obj.tag == "SSP":
                    filtered_queryset_sus_unk +=1
                if obj.show_value() == 'uncoded' or obj.tag == "UND":
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
                0, #filtered_queryset_abs,      # v.10
                filtered_queryset_sus_unk,     
                filtered_queryset_unk,
                filtered_queryset_unc,       # v.13
                pols_count,
                dif_count,
                0, #filtered_queryset_trans,
                'Coded',
                ]

        else:
            var_type="A/P/U/~"

            for obj in queryset:
                if obj.coded_value == 'present':
                    filtered_queryset_pres +=1
                if obj.coded_value == 'absent':
                    filtered_queryset_abs +=1
                if obj.coded_value == "unknown" and obj.tag == "TRS":
                    filtered_queryset_unk +=1
                if obj.coded_value == "unknown" and obj.tag == "SSP":
                    filtered_queryset_sus_unk +=1
                if obj.coded_value == 'uncoded' or obj.tag == "UND":
                    filtered_queryset_unc +=1
                if obj.coded_value == 'Transitional (Present -> Absent)' or obj.coded_value == 'Transitional (Absent -> Present)':
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

    return render(request, 'ec/ecvars.html', context=context)


@permission_required('core.view_capital')
def download_csv_luxury_goods(request):
    # Fetch all models in the "socomp" app
    app_name = 'ec'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"ec_luxury_goods_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name in ["Ra", 'Precious_metal']:
            continue
        s_value = str(model().subsection())
        if s_value == "Naval technology":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response


