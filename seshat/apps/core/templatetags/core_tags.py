from django import template
from django.db import connection
from django.db.models import F
from ..models import Polity, Capital
from ...general.models import Polity_capital, Polity_peak_years
from ..views import get_polity_shape_content

register = template.Library()

@register.inclusion_tag('core/polity_map.html')
def polity_map(pk, test=False):
    """
    This function is used by the polity_map template and gets the specific
    polity shape data and capital information. Sets include_polity_map to False
    if there is no shape data. include_polity_map is used to determine whether
    to display the map on polity_detail.html.

    Args:
        pk (int): The primary key of the polity.

    Returns:
        dict: The content dictionary containing the polity shape data and
            capital information.
    """
    page_id = str(pk)
    polity = Polity.objects.get(id=page_id)
    try:
        if test:
            content = get_polity_shape_content(seshat_id=polity.new_name, tick_number=3)
        else:
            content = get_polity_shape_content(seshat_id=polity.new_name, tick_number=10)
        capitals_info = get_polity_capitals(pk)
        # Set the start and end years to be the same as the polity where missing
        modified_caps = capitals_info
        i = 0
        for capital_info in capitals_info:
            if capital_info['year_from'] == None:
                modified_caps[i]['year_from'] = polity.start_year
            if capital_info['year_to'] == None:
                modified_caps[i]['year_to'] = polity.end_year
            i+=1
        content['capitals_info'] = modified_caps
        content['include_polity_map'] = True
    except:
        content = {}
        content['include_polity_map'] = False

    if content['include_polity_map']:
        # Update the default display year to be the peak year (if it exists)
        try:
            peak_years = Polity_peak_years.objects.get(polity_id=page_id)
            content['display_year'] = peak_years.peak_year_from
        except:
            pass
    
    return {'content': content}

def get_polity_capitals(pk):
    """
    Get all the capitals for a polity and coordinates.

    Args:
        pk (int): The primary key of the polity.

    Returns:
        list: A list of dictionaries containing the capital name, latitude,
            longitude, start year (or 0 or None if they aren't present in the
            database), and end year (or 0 or None if they aren't present in
            the database).
    """
    capitals_info = []
    polity_capitals = Polity_capital.objects.filter(polity_id=pk)
    
    for polity_capital in polity_capitals:
        capitals = Capital.objects.filter(name=polity_capital.capital)
        for capital in capitals:
            capital_info = {}
            if capital.name and capital.latitude and capital.longitude:
                capital_info['capital'] = capital.name
                capital_info['latitude'] = float(capital.latitude)
                capital_info['longitude'] = float(capital.longitude)

                if polity_capital.year_from == 0:
                    capital_info['year_from'] = 0
                elif polity_capital.year_from is not None:
                    capital_info['year_from'] = polity_capital.year_from
                else:
                    capital_info['year_from'] = None
                
                if polity_capital.year_to == 0:
                    capital_info['year_to'] = 0
                elif polity_capital.year_to is not None:
                    capital_info['year_to'] = polity_capital.year_to
                else:
                    capital_info['year_to'] = None
                
                capitals_info.append(capital_info)
    
    return capitals_info
