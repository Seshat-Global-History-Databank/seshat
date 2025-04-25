
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

import csv
import datetime

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

from .models import Settlement_population


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