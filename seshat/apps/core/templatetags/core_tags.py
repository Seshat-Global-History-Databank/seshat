from django import template

from ..models import Polity
from ..views import get_polity_shape_content, get_polity_capitals

from ...general.models import Polity_peak_years


register = template.Library()


@register.inclusion_tag("core/polity_map.html")
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
            content = get_polity_shape_content(
                seshat_id=polity.new_name, tick_number=10
            )
        capitals_info = get_polity_capitals(pk)
        # Set the start and end years to be the same as the polity where missing
        modified_caps = capitals_info

        for i, capital_info in enumerate(capitals_info):
            if capital_info["year_from"] is None:
                modified_caps[i]["year_from"] = polity.start_year
            if capital_info["year_to"] is None:
                modified_caps[i]["year_to"] = polity.end_year

        content["capitals_info"] = modified_caps
        content["include_polity_map"] = True
    except:  # noqa: E722  TODO: Don't use bare except
        content = {
            "include_polity_map": False,
        }

    if content["include_polity_map"]:
        # Update the default display year to be the peak year (if it exists)
        try:
            peak_years = Polity_peak_years.objects.get(polity_id=page_id)
            content["display_year"] = peak_years.peak_year_from
        except:  # noqa: E722  TODO: Don't use bare except
            pass

    return {"content": content}
