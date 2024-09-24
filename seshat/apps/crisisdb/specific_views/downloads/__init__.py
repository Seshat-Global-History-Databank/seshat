# TODO: rewrite all these into the general class-based views (GenericDownloadView and
# GenericMetaDownloadView)

__all__ = [
    # Model-based downloads
    "crisis_consequence_download_view",
    "power_transition_download_view",
    "human_sacrifice_download_view",
    "external_conflict_download_view",
    "internal_conflict_download_view",
    "external_conflict_side_download_view",
    "agricultural_population_download_view",
    "arable_land_download_view",
    "arable_land_per_farmer_download_view",
    "gross_grain_shared_per_agricultural_population_download_view",
    "net_grain_shared_per_agricultural_population_download_view",
    "surplus_download_view",
    "military_expense_download_view",
    "silver_inflow_download_view",
    "silver_stock_download_view",
    "total_population_download_view",
    "gdp_per_capita_download_view",
    "drought_event_download_view",
    "locust_event_download_view",
    "socioeconomic_turmoil_event_download_view",
    "crop_failure_event_download_view",
    "famine_event_download_view",
    "disease_outbreak_download_view",
    # Metadata downloads
    "crisis_consequence_meta_download_view",
    "power_transition_meta_download_view",
    "human_sacrifice_meta_download_view",
    "external_conflict_meta_download_view",
    "internal_conflict_meta_download_view",
    "external_conflict_side_meta_download_view",
    "agricultural_population_meta_download_view",
    "arable_land_meta_download_view",
    "arable_land_per_farmer_meta_download_view",
    "gross_grain_shared_per_agricultural_population_meta_download_view",
    "net_grain_shared_per_agricultural_population_meta_download_view",
    "surplus_meta_download_view",
    "military_expense_meta_download_view",
    "silver_inflow_meta_download_view",
    "silver_stock_meta_download_view",
    "total_population_meta_download_view",
    "gdp_per_capita_meta_download_view",
    "drought_event_meta_download_view",
    "locust_event_meta_download_view",
    "socioeconomic_turmoil_event_meta_download_view",
    "crop_failure_event_meta_download_view",
    "famine_event_meta_download_view",
    "disease_outbreak_meta_download_view",
    # Specialized downloads
    "us_violence_download_view",
]

import csv

from django.contrib.auth.decorators import permission_required
# from django.http import HttpResponse

from ...models import (
    Power_transition,
    Crisis_consequence,
    Human_sacrifice,
    External_conflict,
    Internal_conflict,
    External_conflict_side,
    Agricultural_population,
    Arable_land,
    Arable_land_per_farmer,
    Gross_grain_shared_per_agricultural_population,
    Net_grain_shared_per_agricultural_population,
    Surplus,
    Military_expense,
    Silver_inflow,
    Silver_stock,
    Total_population,
    Gdp_per_capita,
    Drought_event,
    Locust_event,
    Socioeconomic_turmoil_event,
    Crop_failure_event,
    Famine_event,
    Disease_outbreak,
    # Us_location,
    # Us_violence_subtype,
    # Us_violence_data_source,
    Us_violence,
)

# from ...constants import (
#     INNER_SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES,
#     INNER_MAGNITUDE_DISEASE_OUTBREAK_CHOICES,
#     INNER_DURATION_DISEASE_OUTBREAK_CHOICES,
# )
from ....constants import (
    CSV_DELIMITER,
)
from ....utils import (
    get_date,
    remove_html_tags,
    get_response,
    write_csv,
)
from .constants import PREFIX, PREFIX_PT


@permission_required("core.view_capital")
def crisis_consequence_download_view(request):
    response = write_csv(Crisis_consequence, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def power_transition_download_view(request):
    response = write_csv(Power_transition, prefix=PREFIX_PT)
    return response


@permission_required("core.view_capital")
def human_sacrifice_download_view(request):
    response = write_csv(Human_sacrifice, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def external_conflict_download_view(request):
    response = write_csv(External_conflict, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def internal_conflict_download_view(request):
    response = write_csv(Internal_conflict, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def external_conflict_side_download_view(request):
    response = write_csv(External_conflict_side, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def agricultural_population_download_view(request):
    response = write_csv(Agricultural_population, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def arable_land_download_view(request):
    response = write_csv(Arable_land, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def arable_land_per_farmer_download_view(request):
    response = write_csv(Arable_land_per_farmer, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def gross_grain_shared_per_agricultural_population_download_view(request):
    response = write_csv(
        Gross_grain_shared_per_agricultural_population, prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def net_grain_shared_per_agricultural_population_download_view(request):
    response = write_csv(
        Net_grain_shared_per_agricultural_population, prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def surplus_download_view(request):
    response = write_csv(Surplus, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def military_expense_download_view(request):
    response = write_csv(Military_expense, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def silver_inflow_download_view(request):
    response = write_csv(Silver_inflow, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def silver_stock_download_view(request):
    response = write_csv(Silver_stock, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def total_population_download_view(request):
    response = write_csv(Total_population, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def gdp_per_capita_download_view(request):
    response = write_csv(Gdp_per_capita, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def drought_event_download_view(request):
    response = write_csv(Drought_event, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def locust_event_download_view(request):
    response = write_csv(Locust_event, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def socioeconomic_turmoil_event_download_view(request):
    response = write_csv(Socioeconomic_turmoil_event, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def crop_failure_event_download_view(request):
    response = write_csv(Crop_failure_event, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def famine_event_download_view(request):
    response = write_csv(Famine_event, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def disease_outbreak_download_view(request):
    response = write_csv(Disease_outbreak, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def crisis_consequence_meta_download_view(request):
    response = write_csv(Crisis_consequence, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def power_transition_meta_download_view(request):
    response = write_csv(Power_transition, "meta", prefix=PREFIX_PT)
    return response


@permission_required("core.view_capital")
def human_sacrifice_meta_download_view(request):
    response = write_csv(Human_sacrifice, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def external_conflict_meta_download_view(request):
    response = write_csv(External_conflict, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def internal_conflict_meta_download_view(request):
    response = write_csv(Internal_conflict, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def external_conflict_side_meta_download_view(request):
    response = write_csv(External_conflict_side, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def agricultural_population_meta_download_view(request):
    response = write_csv(Agricultural_population, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def arable_land_meta_download_view(request):
    response = write_csv(Arable_land, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def arable_land_per_farmer_meta_download_view(request):
    response = write_csv(Arable_land_per_farmer, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def gross_grain_shared_per_agricultural_population_meta_download_view(request):
    response = write_csv(
        Gross_grain_shared_per_agricultural_population, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def net_grain_shared_per_agricultural_population_meta_download_view(request):
    response = write_csv(
        Net_grain_shared_per_agricultural_population, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def surplus_meta_download_view(request):
    response = write_csv(Surplus, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def military_expense_meta_download_view(request):
    response = write_csv(Military_expense, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def silver_inflow_meta_download_view(request):
    response = write_csv(Silver_inflow, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def silver_stock_meta_download_view(request):
    response = write_csv(Silver_stock, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def total_population_meta_download_view(request):
    response = write_csv(Total_population, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def gdp_per_capita_meta_download_view(request):
    response = write_csv(Gdp_per_capita, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def drought_event_meta_download_view(request):
    response = write_csv(Drought_event, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def locust_event_meta_download_view(request):
    response = write_csv(Locust_event, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def socioeconomic_turmoil_event_meta_download_view(request):
    response = write_csv(Socioeconomic_turmoil_event, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def crop_failure_event_meta_download_view(request):
    response = write_csv(Crop_failure_event, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def famine_event_meta_download_view(request):
    response = write_csv(Famine_event, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def disease_outbreak_meta_download_view(request):
    response = write_csv(Disease_outbreak, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def us_violence_download_view(request):
    '''
    Download all Us_violence instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    '''
    response = get_response(filename=f"american_violence_data_{get_date()}.csv")

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "id",
            "date",
            "type",
            "subtypes",
            "locations",
            "fatality",
            "sources",
            "url_address",
            "source_details",
            "narrative",
        ]
    )

    for obj in Us_violence.objects.all().order_by("id"):
        locations_text = remove_html_tags(obj.show_locations())
        short_data_sources_text = remove_html_tags(
            obj.show_short_data_sources()
        )

        writer.writerow(
            [
                obj.id,
                obj.violence_date,
                obj.violence_type,
                obj.show_violence_subtypes(),
                locations_text,
                obj.fatalities,
                short_data_sources_text,
                obj.url_address,
                obj.source_details,
                obj.narrative,
            ]
        )

    return response


"""
@permission_required("core.view_capital")
def crisis_consequence_download_view(request):
    '''
    Download all Crisis_consequence instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = get_response(filename=f"crisis_consequences_{get_date()}.csv")

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity_new_ID",
            "polity_old_ID",
            "polity_long_name",
            "other_polity_new_ID",
            "other_polity_old_ID",
            "other_polity_long_name",
            "crisis_consequence_id",
            "decline",
            "collapse",
            "epidemic",
            "downward_mobility",
            "extermination",
            "uprising",
            "revolution",
            "successful_revolution",
            "civil_war",
            "century_plus",
            "fragmentation",
            "capital",
            "conquest",
            "assassination",
            "depose",
            "constitution",
            "labor",
            "unfree_labor",
            "suffrage",
            "public_goods",
            "religion",
            "description",
        ]
    )

    for obj in Crisis_consequence.objects.all():
        if obj.other_polity and obj.polity:
            writer.writerow(
                [
                    obj.year_from,
                    obj.year_to,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.polity.long_name,
                    obj.other_polity.new_name,
                    obj.other_polity.name,
                    obj.other_polity.long_name,
                    obj.crisis_case_id,
                    obj.decline,
                    obj.collapse,
                    obj.epidemic,
                    obj.downward_mobility,
                    obj.extermination,
                    obj.uprising,
                    obj.revolution,
                    obj.successful_revolution,
                    obj.civil_war,
                    obj.century_plus,
                    obj.fragmentation,
                    obj.capital,
                    obj.conquest,
                    obj.assassination,
                    obj.depose,
                    obj.constitution,
                    obj.labor,
                    obj.unfree_labor,
                    obj.suffrage,
                    obj.public_goods,
                    obj.religion,
                ]
            )
        elif obj.polity:
            writer.writerow(
                [
                    obj.year_from,
                    obj.year_to,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.polity.long_name,
                    "",
                    "",
                    "",
                    obj.crisis_case_id,
                    obj.decline,
                    obj.collapse,
                    obj.epidemic,
                    obj.downward_mobility,
                    obj.extermination,
                    obj.uprising,
                    obj.revolution,
                    obj.successful_revolution,
                    obj.civil_war,
                    obj.century_plus,
                    obj.fragmentation,
                    obj.capital,
                    obj.conquest,
                    obj.assassination,
                    obj.depose,
                    obj.constitution,
                    obj.labor,
                    obj.unfree_labor,
                    obj.suffrage,
                    obj.public_goods,
                    obj.religion,
                ]
            )
        elif obj.other_polity:
            writer.writerow(
                [
                    obj.year_from,
                    obj.year_to,
                    "",
                    "",
                    "",
                    obj.other_polity.new_name,
                    obj.other_polity.name,
                    obj.other_polity.long_name,
                    obj.crisis_case_id,
                    obj.decline,
                    obj.collapse,
                    obj.epidemic,
                    obj.downward_mobility,
                    obj.extermination,
                    obj.uprising,
                    obj.revolution,
                    obj.successful_revolution,
                    obj.civil_war,
                    obj.century_plus,
                    obj.fragmentation,
                    obj.capital,
                    obj.conquest,
                    obj.assassination,
                    obj.depose,
                    obj.constitution,
                    obj.labor,
                    obj.unfree_labor,
                    obj.suffrage,
                    obj.public_goods,
                    obj.religion,
                ]
            )
        else:
            writer.writerow(
                [
                    obj.year_from,
                    obj.year_to,
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    obj.crisis_case_id,
                    obj.decline,
                    obj.collapse,
                    obj.epidemic,
                    obj.downward_mobility,
                    obj.extermination,
                    obj.uprising,
                    obj.revolution,
                    obj.successful_revolution,
                    obj.civil_war,
                    obj.century_plus,
                    obj.fragmentation,
                    obj.capital,
                    obj.conquest,
                    obj.assassination,
                    obj.depose,
                    obj.constitution,
                    obj.labor,
                    obj.unfree_labor,
                    obj.suffrage,
                    obj.public_goods,
                    obj.religion,
                ]
            )

    return response


@permission_required("core.view_capital")
def crisis_consequence_meta_download_view(request):
    '''
    Download the metadata for Crisis_consequence instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = get_response(filename="crisis_consequences_metadata.csv")

    meta_data_dic = {
        "notes": "Notes for the Variable crisis_consequence are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "No Explanations.",
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
    }
    meta_data_dic_inner_vars = {
        "crisis_consequence": {
            "min": None,
            "max": None,
            "scale": 1000,
            "var_exp_source": None,
            "var_exp": "No Explanations.",
            "units": "mu?",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def power_transition_download_view(request):
    '''
    Download all Power_transition instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = get_response(filename=f"power_transitions_{get_date()}.csv")

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "year_from",
            "year_to",
            "predecessor",
            "successor",
            "polity_new_ID",
            "polity_old_ID",
            "polity_long_form_name",
            "conflict_name",
            "contested",
            "overturn",
            "predecessor_assassination",
            "intra_elite",
            "military_revolt",
            "popular_uprising",
            "separatist_rebellion",
            "external_invasion",
            "external_interference",
        ]
    )

    for obj in Power_transition.objects.all():
        if obj.polity:
            writer.writerow(
                [
                    obj.year_from,
                    obj.year_to,
                    obj.predecessor,
                    obj.successor,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.polity.long_name,
                    obj.name,
                    obj.contested,
                    obj.overturn,
                    obj.predecessor_assassination,
                    obj.intra_elite,
                    obj.military_revolt,
                    obj.popular_uprising,
                    obj.separatist_rebellion,
                    obj.external_invasion,
                    obj.external_interference,
                ]
            )
        else:
            writer.writerow(
                [
                    obj.year_from,
                    obj.year_to,
                    obj.predecessor,
                    obj.successor,
                    "",
                    "",
                    "",
                    obj.name,
                    obj.contested,
                    obj.overturn,
                    obj.predecessor_assassination,
                    obj.intra_elite,
                    obj.military_revolt,
                    obj.popular_uprising,
                    obj.separatist_rebellion,
                    obj.external_invasion,
                    obj.external_interference,
                ]
            )

    return response


@permission_required("core.view_capital")
def power_transition_meta_download_view(request):
    '''
    Download the metadata for Power_transition instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = get_response(filename="power_transitions_metadata.csv")

    meta_data_dic = {
        "notes": "Notes for the Variable power_transition are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "No Explanations.",
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
    }
    meta_data_dic_inner_vars = {
        "power_transition": {
            "min": None,
            "max": None,
            "scale": 1000,
            "var_exp_source": None,
            "var_exp": "No Explanations.",
            "units": "mu?",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def human_sacrifice_download_view(request):
    '''
    Download all Human_sacrifice instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    date = get_date()

    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"human_sacrifices_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "human_sacrifice_abbr",
            "human_sacrifice_long",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Human_sacrifice.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.human_sacrifice,
                obj.get_human_sacrifice_display(),
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def human_sacrifice_meta_download_view(request):
    '''
    Download the metadata for Human_sacrifice instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = get_response(filename="human_sacrifices_metadata.csv")

    meta_data_dic = {
        "notes": Human_sacrifice.Code.notes,
        "main_desc": Human_sacrifice.Code.description,
        "main_desc_source": Human_sacrifice.Code.description_source,
        "section": Human_sacrifice.Code.section,
        "subsection": Human_sacrifice.Code.subsection,
        "null_meaning": Human_sacrifice.Code.null_meaning,
    }
    meta_data_dic_inner_vars = Human_sacrifice.Code.inner_variables
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def external_conflict_download_view(request):
    '''
    Download all External_conflict instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="external_conflicts.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "conflict_name",
        ]
    )

    for obj in External_conflict.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.conflict_name,
            ]
        )

    return response


@permission_required("core.view_capital")
def external_conflict_meta_download_view(request):
    '''
    Download the metadata for External_conflict instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="external_conflicts.csv"'
    )

    meta_data_dic = {
        "notes": "This is a new model definition for External conflicts",
        "main_desc": "Main Descriptions for the Variable external_conflict are missing!",
        "main_desc_source": "Main Descriptions for the Variable external_conflict are missing!",  # noqa: E501 pylint: disable=C0301
        "section": "Conflict Variables",
        "subsection": "External Conflicts Subsection",
        "null_meaning": "The value is not available.",
    }
    meta_data_dic_inner_vars = {
        "conflict_name": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The unique name of this external conflict",
            "units": None,
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def internal_conflict_download_view(request):
    '''
    Download all Internal_conflict instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="internal_conflicts.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "conflict",
            "expenditure",
            "leader",
            "casualty",
        ]
    )

    for obj in Internal_conflict.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.conflict,
                obj.expenditure,
                obj.leader,
                obj.casualty,
            ]
        )

    return response


@permission_required("core.view_capital")
def internal_conflict_meta_download_view(request):
    '''
    Download the metadata for Internal_conflict instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="internal_conflicts.csv"'
    )

    meta_data_dic = {
        "notes": "This is a new model definition for internal conflicts",
        "main_desc": "Main Descriptions for the Variable internal_conflict are missing!",
        "main_desc_source": "Main Descriptions for the Variable internal_conflict are missing!",  # noqa: E501 pylint: disable=C0301
        "section": "Conflict Variables",
        "subsection": "Internal Conflicts Subsection",
        "null_meaning": "The value is not available.",
    }
    meta_data_dic_inner_vars = {
        "conflict": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The name of the conflict",
            "units": None,
            "choices": None,
        },
        "expenditure": {
            "min": None,
            "max": None,
            "scale": 1000000,
            "var_exp_source": None,
            "var_exp": "The military expenses in millions silver taels.",
            "units": "silver taels",
            "choices": None,
        },
        "leader": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The leader of the conflict",
            "units": None,
            "choices": None,
        },
        "casualty": {
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "The number of people who died in this conflict.",
            "units": "People",
            "choices": None,
        },
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def external_conflict_side_download_view(request):
    '''
    Download all External_conflict_side instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="external_conflict_sides.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "conflict_id",
            "expenditure",
            "leader",
            "casualty",
        ]
    )

    for obj in External_conflict_side.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.conflict_id,
                obj.expenditure,
                obj.leader,
                obj.casualty,
            ]
        )

    return response


@permission_required("core.view_capital")
def external_conflict_side_meta_download_view(request):
    '''
    Download the metadata for External_conflict_side instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="external_conflict_sides.csv"'
    )

    my_meta_data_dic = {
        "notes": "This is a new model definition for External conflict sides",
        "main_desc": "Main Descriptions for the Variable external_conflict_side are missing!",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "Main Descriptions for the Variable external_conflict_side are missing!",  # noqa: E501 pylint: disable=C0301
        "section": "Conflict Variables",
        "subsection": "External Conflicts Subsection",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "conflict_id": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The external_conflict which is the actual conflict we are talking about",  # noqa: E501 pylint: disable=C0301
            "units": None,
            "choices": None,
        },
        "expenditure": {
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "The military expenses (from this side) in silver taels.",
            "units": "silver taels",
            "choices": None,
        },
        "leader": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The leader of this side of conflict",
            "units": None,
            "choices": None,
        },
        "casualty": {
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "The number of people who died (from this side) in this conflict.",
            "units": "People",
            "choices": None,
        },
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def agricultural_population_download_view(request):
    '''
    Download all Agricultural_population instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="agricultural_populations.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "agricultural_population",
        ]
    )

    for obj in Agricultural_population.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.agricultural_population,
            ]
        )

    return response


@permission_required("core.view_capital")
def agricultural_population_meta_download_view(request):
    '''
    Download the metadata for Agricultural_population instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="agricultural_populations.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable agricultural_population are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "No Explanations.",
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "agricultural_population": {
            "min": 0,
            "max": None,
            "scale": 1000,
            "var_exp_source": None,
            "var_exp": "No Explanations.",
            "units": "People",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def arable_land_download_view(request):
    '''
    Download all Arable_land instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="arable_lands.csv"'

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "arable_land",
        ]
    )

    for obj in Arable_land.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.arable_land,
            ]
        )

    return response


@permission_required("core.view_capital")
def arable_land_meta_download_view(request):
    '''
    Download the metadata for Arable_land instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="arable_lands.csv"'

    my_meta_data_dic = {
        "notes": "Notes for the Variable arable_land are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "No Explanations.",
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "arable_land": {
            "min": None,
            "max": None,
            "scale": 1000,
            "var_exp_source": None,
            "var_exp": "No Explanations.",
            "units": "mu?",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def arable_land_per_farmer_download_view(request):
    '''
    Download all Arable_land_per_farmer instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="arable_land_per_farmers.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "arable_land_per_farmer",
        ]
    )

    for obj in Arable_land_per_farmer.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.arable_land_per_farmer,
            ]
        )

    return response


@permission_required("core.view_capital")
def arable_land_per_farmer_meta_download_view(request):
    '''
    Download the metadata for Arable_land_per_farmer instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="arable_land_per_farmers.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable arable_land_per_farmer are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "No Explanations.",
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "arable_land_per_farmer": {
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "No Explanations.",
            "units": "mu?",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def gross_grain_shared_per_agricultural_population_download_view(request):
    '''
    Download all Gross_grain_shared_per_agricultural_population instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="gross_grain_shared_per_agricultural_populations.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "gross_grain_shared_per_agricultural_population",
        ]
    )

    for obj in Gross_grain_shared_per_agricultural_population.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.gross_grain_shared_per_agricultural_population,
            ]
        )

    return response


@permission_required("core.view_capital")
def gross_grain_shared_per_agricultural_population_meta_download_view(request):
    '''
    Download the metadata for Gross_grain_shared_per_agricultural_population instances as
    CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="gross_grain_shared_per_agricultural_populations.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable gross_grain_shared_per_agricultural_population are missing!",  # noqa: E501 pylint: disable=C0301
        "main_desc": "No Explanations.",
        "main_desc_source": "No Explanations.",
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "gross_grain_shared_per_agricultural_population": {
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "No Explanations.",
            "units": "(catties per capita)",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def net_grain_shared_per_agricultural_population_download_view(request):
    '''
    Download all Net_grain_shared_per_agricultural_population instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="net_grain_shared_per_agricultural_populations.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "net_grain_shared_per_agricultural_population",
        ]
    )

    for obj in Net_grain_shared_per_agricultural_population.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.net_grain_shared_per_agricultural_population,
            ]
        )

    return response


@permission_required("core.view_capital")
def net_grain_shared_per_agricultural_population_meta_download_view(request):
    '''
    Download the metadata for Net_grain_shared_per_agricultural_population instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="net_grain_shared_per_agricultural_populations.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable net_grain_shared_per_agricultural_population are missing!",  # noqa: E501 pylint: disable=C0301
        "main_desc": "No Explanations.",
        "main_desc_source": "No Explanations.",
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "net_grain_shared_per_agricultural_population": {
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "No Explanations.",
            "units": "(catties per capita)",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def surplus_download_view(request):
    '''
    Download all Surplus instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="surplus.csv"'

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "surplus",
        ]
    )

    for obj in Surplus.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.surplus,
            ]
        )

    return response


@permission_required("core.view_capital")
def surplus_meta_download_view(request):
    '''
    Download the metadata for Surplus instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="surplus.csv"'

    my_meta_data_dic = {
        "notes": "Notes for the Variable surplus are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "No Explanations.",
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "surplus": {
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "No Explanations.",
            "units": "(catties per capita)",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def military_expense_download_view(request):
    '''
    Download all Military_expense instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="military_expenses.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "conflict",
            "expenditure",
        ]
    )

    for obj in Military_expense.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.conflict,
                obj.expenditure,
            ]
        )

    return response


@permission_required("core.view_capital")
def military_expense_meta_download_view(request):
    '''
    Download the metadata for Military_expense instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="military_expenses.csv"'
    )

    my_meta_data_dic = {
        "notes": "Not sure about Section and Subsection.",
        "main_desc": "Main Descriptions for the Variable military_expense are missing!",
        "main_desc_source": "Main Descriptions for the Variable military_expense are missing!",  # noqa: E501 pylint: disable=C0301
        "section": "Economy Variables",
        "subsection": "State Finances",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "conflict": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The name of the conflict",
            "units": None,
            "choices": None,
        },
        "expenditure": {
            "min": None,
            "max": None,
            "scale": 1000000,
            "var_exp_source": None,
            "var_exp": "The military expenses in millions silver taels.",
            "units": "silver taels",
            "choices": None,
        },
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def silver_inflow_download_view(request):
    '''
    Download all Silver_inflow instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="silver_inflows.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "silver_inflow",
        ]
    )

    for obj in Silver_inflow.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.silver_inflow,
            ]
        )

    return response


@permission_required("core.view_capital")
def silver_inflow_meta_download_view(request):
    '''
    Download the metadata for Silver_inflow instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="silver_inflows.csv"'
    )

    my_meta_data_dic = {
        "notes": "Needs suoervision on the units and scale.",
        "main_desc": "Silver inflow in Millions of silver taels??",
        "main_desc_source": "Silver inflow in Millions of silver taels??",
        "section": "Economy Variables",
        "subsection": "State Finances",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "silver_inflow": {
            "min": None,
            "max": None,
            "scale": 1000000,
            "var_exp_source": None,
            "var_exp": "Silver inflow in Millions of silver taels??",
            "units": "silver taels??",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def silver_stock_download_view(request):
    '''
    Download all Silver_stock instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="silver_stocks.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "silver_stock",
        ]
    )

    for obj in Silver_stock.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.silver_stock,
            ]
        )

    return response


@permission_required("core.view_capital")
def silver_stock_meta_download_view(request):
    '''
    Download the metadata for Silver_stock instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="silver_stocks.csv"'
    )

    my_meta_data_dic = {
        "notes": "Needs suoervision on the units and scale.",
        "main_desc": "Silver stock in Millions of silver taels??",
        "main_desc_source": "Silver stock in Millions of silver taels??",
        "section": "Economy Variables",
        "subsection": "State Finances",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "silver_stock": {
            "min": None,
            "max": None,
            "scale": 1000000,
            "var_exp_source": None,
            "var_exp": "Silver stock in Millions of silver taels??",
            "units": "silver taels??",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def total_population_download_view(request):
    '''
    Download all Total_population instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="total_populations.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "total_population",
        ]
    )

    for obj in Total_population.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.total_population,
            ]
        )

    return response


@permission_required("core.view_capital")
def total_population_meta_download_view(request):
    '''
    Download the metadata for Total_population instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="total_populations.csv"'
    )

    my_meta_data_dic = {
        "notes": "Note that the population values are scaled.",
        "main_desc": "Total population or simply population, of a given area is the total number of people in that area at a given time.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "Total population or simply population, of a given area is the total number of people in that area at a given time.",  # noqa: E501 pylint: disable=C0301
        "section": "Social Complexity Variables",
        "subsection": "Social Scale",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "total_population": {
            "min": 0,
            "max": None,
            "scale": 1000,
            "var_exp_source": None,
            "var_exp": "The total population of a country (or a polity).",
            "units": "People",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def gdp_per_capita_download_view(request):
    '''
    Download all Gdp_per_capita instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="gdp_per_capitas.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "gdp_per_capita",
        ]
    )

    for obj in Gdp_per_capita.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.gdp_per_capita,
            ]
        )

    return response


@permission_required("core.view_capital")
def gdp_per_capita_meta_download_view(request):
    '''
    Download the metadata for Gdp_per_capita instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="gdp_per_capitas.csv"'
    )

    my_meta_data_dic = {
        "notes": "The exact year based on which the value of Dollar is taken into account is not clear.",  # noqa: E501 pylint: disable=C0301
        "main_desc": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.",  # noqa: E501 pylint: disable=C0301
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "gdp_per_capita": {
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848",  # noqa: E501 pylint: disable=C0301
            "var_exp": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.",  # noqa: E501 pylint: disable=C0301
            "units": "Dollars (in 2009?)",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def drought_event_download_view(request):
    '''
    Download all Drought_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="drought_events.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "drought_event",
        ]
    )

    for obj in Drought_event.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.drought_event,
            ]
        )

    return response


@permission_required("core.view_capital")
def drought_event_meta_download_view(request):
    '''
    Download the metadata for Drought_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="drought_events.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable drought_event are missing!",
        "main_desc": "number of geographic sites indicating drought",
        "main_desc_source": "number of geographic sites indicating drought",
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "drought_event": {
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "number of geographic sites indicating drought",
            "units": "Numbers",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def locust_event_download_view(request):
    '''
    Download all Locust_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="locust_events.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "locust_event",
        ]
    )

    for obj in Locust_event.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.locust_event,
            ]
        )

    return response


@permission_required("core.view_capital")
def locust_event_meta_download_view(request):
    '''
    Download the metadata for Locust_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="locust_events.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable locust_event are missing!",
        "main_desc": "number of geographic sites indicating locusts",
        "main_desc_source": "number of geographic sites indicating locusts",
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "locust_event": {
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "number of geographic sites indicating locusts",
            "units": "Numbers",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def socioeconomic_turmoil_event_download_view(request):
    '''
    Download all Socioeconomic_turmoil_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="socioeconomic_turmoil_events.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "socioeconomic_turmoil_event",
        ]
    )

    for obj in Socioeconomic_turmoil_event.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.socioeconomic_turmoil_event,
            ]
        )

    return response


@permission_required("core.view_capital")
def socioeconomic_turmoil_event_meta_download_view(request):
    '''
    Download the metadata for Socioeconomic_turmoil_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="socioeconomic_turmoil_events.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable socioeconomic_turmoil_event are missing!",
        "main_desc": "number of geographic sites indicating socioeconomic turmoil",
        "main_desc_source": "number of geographic sites indicating socioeconomic turmoil",
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "socioeconomic_turmoil_event": {
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "number of geographic sites indicating socioeconomic turmoil",
            "units": "Numbers",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def crop_failure_event_download_view(request):
    '''
    Download all Crop_failure_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="crop_failure_events.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "crop_failure_event",
        ]
    )

    for obj in Crop_failure_event.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.crop_failure_event,
            ]
        )

    return response


@permission_required("core.view_capital")
def crop_failure_event_meta_download_view(request):
    '''
    Download the metadata for Crop_failure_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="crop_failure_events.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable crop_failure_event are missing!",
        "main_desc": "number of geographic sites indicating crop failure",
        "main_desc_source": "number of geographic sites indicating crop failure",
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "crop_failure_event": {
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "number of geographic sites indicating crop failure",
            "units": "Numbers",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def famine_event_download_view(request):
    '''
    Download all Famine_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="famine_events.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "famine_event",
        ]
    )

    for obj in Famine_event.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.famine_event,
            ]
        )

    return response


@permission_required("core.view_capital")
def famine_event_meta_download_view(request):
    '''
    Download the metadata for Famine_event instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="famine_events.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable famine_event are missing!",
        "main_desc": "number of geographic sites indicating famine",
        "main_desc_source": "number of geographic sites indicating famine",
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "famine_event": {
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "number of geographic sites indicating famine",
            "units": "Numbers",
            "choices": None,
        }
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def disease_outbreak_download_view(request):
    '''
    Download all Disease_outbreak instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="disease_outbreaks.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "year_from",
            "year_to",
            "polity",
            "longitude",
            "latitude",
            "elevation",
            "sub_category",
            "magnitude",
            "duration",
        ]
    )

    for obj in Disease_outbreak.objects.all():
        writer.writerow(
            [
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.longitude,
                obj.latitude,
                obj.elevation,
                obj.sub_category,
                obj.magnitude,
                obj.duration,
            ]
        )

    return response


@permission_required("core.view_capital")
def disease_outbreak_meta_download_view(request):
    '''
    Download the metadata for Disease_outbreak instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="disease_outbreaks.csv"'
    )

    my_meta_data_dic = {
        "notes": "Notes for the Variable disease_outbreak are missing!",
        "main_desc": "A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season.",  # noqa: E501 pylint: disable=C0301
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
    }
    my_meta_data_dic_inner_vars = {
        "longitude": {
            "min": -180,
            "max": 180,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "The longitude (in degrees) of the place where the disease was spread.",  # noqa: E501 pylint: disable=C0301
            "units": "Degrees",
            "choices": None,
        },
        "latitude": {
            "min": -180,
            "max": 180,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "The latitude (in degrees) of the place where the disease was spread.",  # noqa: E501 pylint: disable=C0301
            "units": "Degrees",
            "choices": None,
        },
        "elevation": {
            "min": 0,
            "max": 5000,
            "scale": 1,
            "var_exp_source": None,
            "var_exp": "Elevation from mean sea level (in meters) of the place where the disease was spread.",  # noqa: E501 pylint: disable=C0301
            "units": "Meters",
            "choices": None,
        },
        "sub_category": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The category of the disease.",
            "units": None,
            "choices": INNER_SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES,
        },
        "magnitude": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "How heavy the disease was.",
            "units": None,
            "choices": INNER_MAGNITUDE_DISEASE_OUTBREAK_CHOICES,
        },
        "duration": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "How long the disease lasted.",
            "units": None,
            "choices": INNER_DURATION_DISEASE_OUTBREAK_CHOICES,
        },
    }
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@permission_required("core.view_capital")
def us_violence_download_view(request):
    '''
    Download all Us_violence instances as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.
    '''
    date = get_date()

    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"american_violence_data_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "id",
            "date",
            "type",
            "subtypes",
            "locations",
            "fatality",
            "sources",
            "url_address",
            "source_details",
            "narrative",
        ]
    )

    for obj in Us_violence.objects.all().order_by("id"):
        locations_text = remove_html_tags(obj.show_locations())
        short_data_sources_text = remove_html_tags(
            obj.show_short_data_sources()
        )

        writer.writerow(
            [
                obj.id,
                obj.violence_date,
                obj.violence_type,
                obj.show_violence_subtypes(),
                locations_text,
                obj.fatalities,
                short_data_sources_text,
                obj.url_address,
                obj.source_details,
                obj.narrative,
            ]
        )

    return response
"""
