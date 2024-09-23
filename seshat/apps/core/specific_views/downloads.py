import csv

from django.contrib.auth.decorators import permission_required
from ...constants import (
    CSV_DELIMITER,
)
from ...utils import (
    get_date,
    get_response,
)
from ..models import Reference, Capital, Polity
from ..utils import get_polity_app_data


@permission_required("core.view_capital")
def referencesdownload_view(request):
    """
    Download all references as a CSV file.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        FileResponse: The response object.
    """
    # Create a response object with CSV content type
    response = get_response(Reference, filename="references.csv")

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(["zotero_link", "creator"])

    for obj in Reference.objects.all():
        writer.writerow([obj.zotero_link, obj.creator])

    return response


@permission_required("core.view_capital")
def capital_download_view(request):
    """
    Download all Capitals as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    # Create a response object with CSV content type
    response = get_response(Capital, filename="capitals.csv")

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "capital",
            "current_country",
            "longitude",
            "latitude",
            "is_verified",
            "note",
        ]
    )

    for obj in Capital.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.current_country,
                obj.longitude,
                obj.latitude,
                obj.is_verified,
                obj.note,
            ]
        )

    return response


@permission_required("core.view_capital")
def download_csv_all_polities_view(request):
    """
    Download a CSV file containing all polities.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    # Create a response object with CSV content type
    response = get_response(filename=f"polities_{get_date()}.csv")

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "macro_region",
            "home_seshat_region",
            "polity_new_ID",
            "polity_old_ID",
            "polity_long_name",
            "start_year",
            "end_year",
            "home_nga",
            "G",
            "SC",
            "WF",
            "RT",
            "HS",
            "CC",
            "PT",
            "polity_tag",
            "shapefile_name",
        ]
    )

    coded_value_data = get_polity_app_data(
        Polity, return_freq=False, return_contain=True
    )

    for obj in Polity.objects.all():
        if obj.home_seshat_region:
            writer.writerow(
                [
                    obj.home_seshat_region.mac_region.name,
                    obj.home_seshat_region.name,
                    obj.new_name,
                    obj.name,
                    obj.long_name,
                    obj.start_year,
                    obj.end_year,
                    obj.home_nga,
                    coded_value_data[obj.id]["g"],
                    coded_value_data[obj.id]["sc"],
                    coded_value_data[obj.id]["wf"],
                    coded_value_data[obj.id]["rt"],
                    coded_value_data[obj.id]["hs"],
                    coded_value_data[obj.id]["cc"],
                    coded_value_data[obj.id]["pt"],
                    obj.get_polity_tag_display(),
                    obj.shapefile_name,
                ]
            )
        else:
            writer.writerow(
                [
                    "None",
                    "None",
                    obj.new_name,
                    obj.name,
                    obj.long_name,
                    obj.start_year,
                    obj.end_year,
                    obj.home_nga,
                    coded_value_data[obj.id]["g"],
                    coded_value_data[obj.id]["sc"],
                    coded_value_data[obj.id]["wf"],
                    coded_value_data[obj.id]["rt"],
                    coded_value_data[obj.id]["hs"],
                    coded_value_data[obj.id]["cc"],
                    coded_value_data[obj.id]["pt"],
                    obj.get_polity_tag_display(),
                    obj.shapefile_name,
                ]
            )

    return response


def download_oldcsv_view(request, file_name):
    """
    Download a CSV file.

    Args:
        request: The request object.
        file_name (str): The name of the file to download.

    Returns:
        FileResponse: The file response.
    """
    return get_response(filename=file_name)
