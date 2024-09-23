__all__ = []

import csv

from django.contrib.auth.decorators import permission_required

from ....utils import (
    get_date,
    get_models,
    get_response,
)
from ....constants import CSV_DELIMITER

from ...constants import APP_NAME


@permission_required("core.view_capital")
def download_csv_all_rt(request):
    """
    Download all data for all models in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    response = get_response(
        filename=f"religion_tolerance_data_{get_date()}.csv"
    )

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "subsection",
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "value_from",
            "value_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    # Iterate over each row of each model
    for model in get_models(APP_NAME):
        for obj in model.objects.all():
            if obj.__name__ == "Widespread_religion":
                writer.writerow(
                    [
                        obj.subsection(),
                        obj.clean_name_dynamic(),
                        obj.year_from,
                        obj.year_to,
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.show_value_from(),
                        obj.show_value_to(),
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                        obj.drb_reviewed,
                    ]
                )
            else:
                writer.writerow(
                    [
                        obj.subsection(),
                        obj.clean_name_spaced(),
                        obj.year_from,
                        obj.year_to,
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.show_value_from(),
                        obj.show_value_to(),
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                        obj.drb_reviewed,
                    ]
                )

    return response


@permission_required("core.view_capital")
def download_csv_religious_landscape(request):
    """
    Download all data for the Religious Landscape model in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    response = get_response(
        filename=f"religion_tolerance_religious_landscape_{get_date()}.csv"
    )

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "subsection",
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "value_from",
            "value_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    # Iterate over each row of each model
    for model in get_models(APP_NAME, subsection="Religious Landscape"):
        for obj in model.objects.all():
            writer.writerow(
                [
                    obj.subsection(),
                    obj.clean_name(),
                    obj.year_from,
                    obj.year_to,
                    obj.polity.long_name,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.show_value_from(),
                    obj.show_value_to(),
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.is_uncertain,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )

    return response


@permission_required("core.view_capital")
def download_csv_government_restrictions(request):
    """
    Download all data for the Government Restrictions model in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    response = get_response(
        filename=f"religion_tolerance_government_restrictions_{get_date()}.csv"
    )

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "subsection",
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "value_from",
            "value_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    # Iterate over each row of each model
    for model in get_models(APP_NAME, subsection="Government Restrictions"):
        for obj in model.objects.all():
            writer.writerow(
                [
                    obj.subsection(),
                    obj.clean_name(),
                    obj.year_from,
                    obj.year_to,
                    obj.polity.long_name,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.show_value_from(),
                    obj.show_value_to(),
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.is_uncertain,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )

    return response


@permission_required("core.view_capital")
def download_csv_societal_restrictions(request):
    """
    Download all data for the Societal Restrictions model in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    response = get_response(
        filename=f"religion_tolerance_societal_restrictions_{get_date()}.csv"
    )

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "subsection",
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "value_from",
            "value_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    # Iterate over each row of each model
    for model in get_models(APP_NAME, subsection="Social Restrictions"):
        for obj in model.objects.all():
            writer.writerow(
                [
                    obj.subsection(),
                    obj.clean_name(),
                    obj.year_from,
                    obj.year_to,
                    obj.polity.long_name,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.show_value_from(),
                    obj.show_value_to(),
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.is_uncertain,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )

    return response
