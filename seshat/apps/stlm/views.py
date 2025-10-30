
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

import csv
import datetime

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from .models import Settlement_population
from django.apps import apps


@permission_required('core.add_capital')
def generate_stlm_csv_response(request):
    # Fetch all models in the "sc" app
    app_name = 'stlm'
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"settlement_allen_data_{current_datetime}.csv"
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')
    
    # Write the headers
    writer.writerow(['variable_name',  'settlement_name', 'settlement_alternative_names', 'current_country', 'latitude' , 'longitude', 'year_from', 'year_to', 'value', 'certainty', 'scientific_resource' ])
    
    # Iterate over each model and filter by subsection
    for model in app_models:
        if model.__name__ in ["Number_of_ziggurats", "Number_of_palaces", "Number_of_temples", "Defensive_wall", "Tablet", "Seal_indicator"]:
            items = model.objects.exclude(settlement_id__isnull=True)
            for obj in items:
                if obj.settlement:
                    writer.writerow([obj.name,
                            obj.settlement.name, obj.settlement.alternative_names, obj.settlement.current_country_obj.name, obj.settlement.latitude, obj.settlement.longitude,  obj.year_from, obj.year_to, obj.show_value(), obj.tag, obj.general_ref.title])
                else:
                    writer.writerow([obj.name,
                             "no_name", "no_name", "no_name", obj.settlement.latitude, obj.settlement.longitude,  obj.year_from, obj.year_to, obj.show_value(), obj.tag, obj.general_ref.title])

    return response


# Create your views here.
@permission_required('core.add_capital')
def settlement_population_download(request):
    """
    Download all the data of the settlement_population model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    items = Settlement_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_settlement_population_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name',  'settlement_name', 'settlement_alternative_names', 'current_country', 'latitude' , 'longitude', 'year_from', 'year_to', 'population_from', 'population_to', 'certainty', 'scientific_resource' ])

    for obj in items:
        if obj.settlement.current_country_obj:
            writer.writerow([obj.name,
                            obj.settlement.name, obj.settlement.alternative_names, obj.settlement.current_country_obj.name, obj.settlement.latitude, obj.settlement.longitude,  obj.year_from, obj.year_to, obj.population_from, obj.population_to, obj.tag, obj.general_ref.title])
        else:
           writer.writerow([obj.name,
                            obj.settlement.name, obj.settlement.alternative_names, None, obj.settlement.latitude, obj.settlement.longitude,  obj.year_from, obj.year_to, obj.population_from, obj.population_to, obj.tag, obj.general_ref.title])

    return response
