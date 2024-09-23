# TODO: move the metadata values to the Code attribute on models.

__all__ = [
    # Model-based download views
    "polity_research_assistant_download_view",
    "polity_research_assistant_meta_download_view",
    "polity_utm_zone_download_view",
    "polity_utm_zone_meta_download_view",
    "polity_original_name_download_view",
    "polity_original_name_meta_download_view",
    "polity_alternative_name_download_view",
    "polity_alternative_name_meta_download_view",
    "polity_peak_years_download_view",
    "polity_peak_years_meta_download_view",
    "polity_duration_download_view",
    "polity_duration_meta_download_view",
    "polity_degree_of_centralization_download_view",
    "polity_degree_of_centralization_meta_download_view",
    "polity_suprapolity_relations_download_view",
    "polity_suprapolity_relations_meta_download_view",
    "polity_capital_download_view",
    "polity_capital_meta_download_view",
    "polity_language_download_view",
    "polity_language_meta_download_view",
    "polity_linguistic_family_download_view",
    "polity_linguistic_family_meta_download_view",
    "polity_language_genus_download_view",
    "polity_language_genus_meta_download_view",
    "polity_religion_genus_download_view",
    "polity_religion_genus_meta_download_view",
    "polity_religion_family_download_view",
    "polity_religion_family_meta_download_view",
    "polity_religion_download_view",
    "polity_religion_meta_download_view",
    "polity_relationship_to_preceding_entity_download_view",
    "polity_relationship_to_preceding_entity_meta_download_view",
    "polity_preceding_entity_download_view",
    "polity_preceding_entity_meta_download_view",
    "polity_succeeding_entity_download_view",
    "polity_succeeding_entity_meta_download_view",
    "polity_supracultural_entity_download_view",
    "polity_supracultural_entity_meta_download_view",
    "polity_scale_of_supracultural_interaction_download_view",
    "polity_scale_of_supracultural_interaction_meta_download_view",
    "polity_alternate_religion_genus_download_view",
    "polity_alternate_religion_genus_meta_download_view",
    "polity_alternate_religion_family_download_view",
    "polity_alternate_religion_family_meta_download_view",
    "polity_alternate_religion_download_view",
    "polity_alternate_religion_meta_download_view",
    "polity_expert_download_view",
    "polity_expert_meta_download_view",
    "polity_editor_download_view",
    "polity_editor_meta_download_view",
    "polity_religious_tradition_download_view",
    "polity_religious_tradition_meta_download_view",

    # Specialized download views
    "download_csv_all_general",
]

import csv

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

from ....utils import get_date, get_models, write_csv
from ....constants import (
    CSV_DELIMITER,
    # NO_DATA
)

from ...constants import (
    APP_NAME,
    # INNER_POLITY_DEGREE_OF_CENTRALIZATION_CHOICES,
    # INNER_POLITY_ALTERNATE_RELIGION_CHOICES,
    # INNER_POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES,
    # INNER_POLITY_ALTERNATE_RELIGION_GENUS_CHOICES,
    # INNER_POLITY_LANGUAGE_CHOICES,
    # INNER_POLITY_LINGUISTIC_FAMILY_CHOICES,
    # INNER_POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES,
    # INNER_POLITY_RELIGION_CHOICES,
    # INNER_POLITY_RELIGION_FAMILY_CHOICES,
    # INNER_POLITY_RELIGION_GENUS_CHOICES,
    # INNER_POLITY_SUPRAPOLITY_RELATIONS_CHOICES,
)

from ...models import (
    Polity_research_assistant,
    Polity_utm_zone,
    Polity_original_name,
    Polity_alternative_name,
    Polity_peak_years,
    Polity_duration,
    Polity_degree_of_centralization,
    Polity_suprapolity_relations,
    Polity_capital,
    Polity_language,
    Polity_linguistic_family,
    Polity_language_genus,
    Polity_religion_genus,
    Polity_religion_family,
    Polity_religion,
    Polity_relationship_to_preceding_entity,
    Polity_preceding_entity,
    Polity_succeeding_entity,
    Polity_supracultural_entity,
    Polity_scale_of_supracultural_interaction,
    Polity_alternate_religion_genus,
    Polity_alternate_religion_family,
    Polity_alternate_religion,
    Polity_expert,
    Polity_editor,
    Polity_religious_tradition,
)
from .constants import PREFIX


@permission_required("core.view_capital")
def polity_research_assistant_download_view(request):
    response = write_csv(Polity_research_assistant, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_utm_zone_download_view(request):
    response = write_csv(Polity_utm_zone, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_original_name_download_view(request):
    response = write_csv(Polity_original_name, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_alternative_name_download_view(request):
    response = write_csv(Polity_alternative_name, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_peak_years_download_view(request):
    response = write_csv(Polity_peak_years, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_duration_download_view(request):
    response = write_csv(Polity_duration, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_degree_of_centralization_download_view(request):
    response = write_csv(Polity_degree_of_centralization, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_suprapolity_relations_download_view(request):
    response = write_csv(Polity_suprapolity_relations, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_capital_download_view(request):
    response = write_csv(Polity_capital, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_language_download_view(request):
    response = write_csv(Polity_language, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_linguistic_family_download_view(request):
    response = write_csv(Polity_linguistic_family, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_language_genus_download_view(request):
    response = write_csv(Polity_language_genus, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_religion_genus_download_view(request):
    response = write_csv(Polity_religion_genus, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_religion_family_download_view(request):
    response = write_csv(Polity_religion_family, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_religion_download_view(request):
    response = write_csv(Polity_religion, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_relationship_to_preceding_entity_download_view(request):
    response = write_csv(
        Polity_relationship_to_preceding_entity, prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def polity_preceding_entity_download_view(request):
    response = write_csv(Polity_preceding_entity, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_succeeding_entity_download_view(request):
    response = write_csv(Polity_succeeding_entity, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_supracultural_entity_download_view(request):
    response = write_csv(Polity_supracultural_entity, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_scale_of_supracultural_interaction_download_view(request):
    response = write_csv(
        Polity_scale_of_supracultural_interaction, prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def polity_alternate_religion_genus_download_view(request):
    response = write_csv(Polity_alternate_religion, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_alternate_religion_family_download_view(request):
    response = write_csv(Polity_alternate_religion, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_alternate_religion_download_view(request):
    response = write_csv(Polity_alternate_religion, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_expert_download_view(request):
    response = write_csv(Polity_expert, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_editor_download_view(request):
    response = write_csv(Polity_editor, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_religious_tradition_download_view(request):
    response = write_csv(Polity_religious_tradition, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_research_assistant_meta_download_view(request):
    response = write_csv(Polity_research_assistant, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_utm_zone_meta_download_view(request):
    response = write_csv(Polity_utm_zone, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_original_name_meta_download_view(request):
    response = write_csv(Polity_original_name, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_alternative_name_meta_download_view(request):
    response = write_csv(Polity_alternative_name, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_peak_years_meta_download_view(request):
    response = write_csv(Polity_peak_years, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_duration_meta_download_view(request):
    response = write_csv(Polity_duration, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_degree_of_centralization_meta_download_view(request):
    response = write_csv(
        Polity_degree_of_centralization, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def polity_suprapolity_relations_meta_download_view(request):
    response = write_csv(Polity_suprapolity_relations, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_capital_meta_download_view(request):
    response = write_csv(Polity_capital, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_language_meta_download_view(request):
    response = write_csv(Polity_language, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_linguistic_family_meta_download_view(request):
    response = write_csv(Polity_linguistic_family, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_language_genus_meta_download_view(request):
    response = write_csv(Polity_language_genus, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_religion_genus_meta_download_view(request):
    response = write_csv(Polity_religion_genus, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_religion_family_meta_download_view(request):
    response = write_csv(Polity_religion_family, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_religion_meta_download_view(request):
    response = write_csv(Polity_religion, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_relationship_to_preceding_entity_meta_download_view(request):
    response = write_csv(
        Polity_relationship_to_preceding_entity, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def polity_preceding_entity_meta_download_view(request):
    response = write_csv(Polity_preceding_entity, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_succeeding_entity_meta_download_view(request):
    response = write_csv(Polity_succeeding_entity, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_supracultural_entity_meta_download_view(request):
    response = write_csv(Polity_supracultural_entity, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_scale_of_supracultural_interaction_meta_download_view(request):
    response = write_csv(
        Polity_scale_of_supracultural_interaction, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def polity_alternate_religion_genus_meta_download_view(request):
    response = write_csv(
        Polity_alternate_religion_genus, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def polity_alternate_religion_family_meta_download_view(request):
    response = write_csv(
        Polity_alternate_religion_family, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def polity_alternate_religion_meta_download_view(request):
    response = write_csv(Polity_alternate_religion, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_expert_meta_download_view(request):
    response = write_csv(Polity_expert, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_editor_meta_download_view(request):
    response = write_csv(Polity_editor, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_religious_tradition_meta_download_view(request):
    response = write_csv(Polity_religious_tradition, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def download_csv_all_general(request):
    '''
    Download a CSV file of all general variables. This includes all models in the "general"
    app.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"general_data_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "section",
            "subsection",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "variable_name",
            "value_from",
            "value_to",
            "year_from",
            "year_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )
    # Iterate over each model
    for model in get_models(
        APP_NAME,
        exclude=[Polity_research_assistant, Polity_editor, Polity_expert],
    ):
        for obj in model.objects.all():
            if obj.clean_name_spaced() == "Polity Duration":
                writer.writerow(
                    [
                        "General Variables",
                        obj.subsection(),
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.clean_name()[7:],
                        obj.polity_year_from,
                        obj.polity_year_to,
                        obj.year_from,
                        obj.year_to,
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                    ]
                )
            elif obj.clean_name_spaced() == "Polity Peak Years":
                writer.writerow(
                    [
                        "General Variables",
                        obj.subsection(),
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.clean_name()[7:],
                        obj.peak_year_from,
                        obj.peak_year_to,
                        obj.year_from,
                        obj.year_to,
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                    ]
                )
            else:
                if any(
                    [
                        obj.show_value() == "NO_VALUE_ON_WIKI",
                        obj.show_value() == "NO_VALID_VALUE",
                    ]
                ):
                    continue
                elif "O_VALUE_ON_WIKI" in str(obj.show_value()):
                    continue
                else:
                    writer.writerow(
                        [
                            "General Variables",
                            obj.subsection(),
                            obj.polity.long_name,
                            obj.polity.new_name,
                            obj.polity.name,
                            obj.clean_name()[7:],
                            obj.show_value(),
                            None,
                            obj.year_from,
                            obj.year_to,
                            obj.get_tag_display(),
                            obj.is_disputed,
                            obj.is_uncertain,
                            obj.expert_reviewed,
                        ]
                    )

    return response


"""
@permission_required("core.view_capital")
def polity_research_assistant_download_view(request):
    '''
    Download a CSV file of all Polity_research_assistant instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_research_assistants.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "polity_ra",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_research_assistant.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.polity_ra,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_research_assistant_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_research_assistant instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_research_assistants.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The RA(s) who worked on a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "Staff",
    }
    my_meta_data_dic_inner_vars = {
        "polity_ra": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The RA of a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
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
def polity_utm_zone_download_view(request):
    '''
    Download a CSV file of all Polity_utm_zone instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_utm_zones.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "utm_zone",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_utm_zone.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.utm_zone,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_utm_zone_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_utm_zone instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_utm_zones.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The UTM Zone of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "utm_zone": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The details of UTM_ZONE.",
            "units": None,
            "choices": None,
            "null_meaning": NO_DATA.wiki,
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
def polity_original_name_download_view(request):
    '''
    Download a CSV file of all Polity_original_name instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_original_names.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "original_name",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_original_name.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.original_name,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_original_name_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_original_name instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_original_names.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The original name of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "original_name": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The details of original_name.",
            "units": None,
            "choices": None,
            "null_meaning": NO_DATA.wiki,
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
def polity_alternative_name_download_view(request):
    '''
    Download a CSV file of all Polity_alternative_name instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_alternative_names.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "alternative_name",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_alternative_name.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.alternative_name,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_alternative_name_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_alternative_name instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_alternative_names.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The alternative name of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "alternative_name": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The details of alternative_name.",
            "units": None,
            "choices": None,
            "null_meaning": NO_DATA.wiki,
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
def polity_peak_years_download_view(request):
    '''
    Download a CSV file of all Polity_peak_years instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_peak_yearss.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "peak_year_from",
            "peak_year_to",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_peak_years.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.peak_year_from,
                obj.peak_year_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_peak_years_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_peak_years instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_peak_yearss.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The peak years of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "peak_year_from": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The beginning of the peak years for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": NO_DATA.wiki,
        },
        "peak_year_to": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The end of the peak years for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": NO_DATA.wiki,
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
def polity_duration_download_view(request):
    '''
    Download a CSV file of all Polity_duration instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_durations.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "polity_year_from",
            "polity_year_to",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_duration.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.polity_year_from,
                obj.polity_year_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_duration_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_duration instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_durations.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The lifetime of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "Temporal Bounds",
    }
    my_meta_data_dic_inner_vars = {
        "polity_year_from": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The beginning year for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": NO_DATA.wiki,
        },
        "polity_year_to": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The end year for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": NO_DATA.wiki,
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
def polity_degree_of_centralization_download_view(request):
    '''
    Download a CSV file of all Polity_degree_of_centralization instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_degree_of_centralizations.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "degree_of_centralization",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_degree_of_centralization.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.degree_of_centralization,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_degree_of_centralization_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_degree_of_centralization instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_degree_of_centralizations.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The degree of centralization of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "degree_of_centralization": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The details of degree_of_centralization.",
            "units": None,
            "choices": INNER_POLITY_DEGREE_OF_CENTRALIZATION_CHOICES,
            "null_meaning": NO_DATA.wiki,
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
def polity_suprapolity_relations_download_view(request):
    '''
    Download a CSV file of all Polity_suprapolity_relations instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_suprapolity_relationss.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "supra_polity_relations",
            "other_polity_id",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_suprapolity_relations.objects.all():
        if obj.other_polity:
            writer.writerow(
                [
                    obj.name,
                    obj.year_from,
                    obj.year_to,
                    obj.polity.long_name,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.supra_polity_relations,
                    obj.other_polity.new_name,
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )
        else:
            writer.writerow(
                [
                    obj.name,
                    obj.year_from,
                    obj.year_to,
                    obj.polity.long_name,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.supra_polity_relations,
                    "-",
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )

    return response


@permission_required("core.view_capital")
def polity_suprapolity_relations_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_suprapolity_relations instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_suprapolity_relationss.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The supra polity relations of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "supra_polity_relations": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The details of supra polity relations.",
            "units": None,
            "choices": INNER_POLITY_SUPRAPOLITY_RELATIONS_CHOICES,
            "null_meaning": NO_DATA.wiki,
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
def polity_capital_download_view(request):
    '''
    Download a CSV file of all Polity_capital instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_capitals.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "capital",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_capital.objects.all():
        if obj.polity_cap:
            writer.writerow(
                [
                    obj.name,
                    obj.year_from,
                    obj.year_to,
                    obj.polity,
                    obj.polity.new_name,
                    obj.polity.name,
                    str(obj.polity_cap),
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )
        else:
            writer.writerow(
                [
                    obj.name,
                    obj.year_from,
                    obj.year_to,
                    obj.polity,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.capital,
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )

    return response


@permission_required("core.view_capital")
def polity_capital_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_capital instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_capitals.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The capital of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "capital": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The capital of a polity.",
            "units": None,
            "choices": None,
            "null_meaning": "This polity did not have a capital.",
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
def polity_language_download_view(request):
    '''
    Download a CSV file of all Polity_language instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_languages.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "language",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_language.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.language,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_language_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_language instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_languages.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The language of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "language": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The language of a polity.",
            "units": None,
            "choices": INNER_POLITY_LANGUAGE_CHOICES,
            "null_meaning": "This polity did not have a language.",
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
def polity_linguistic_family_download_view(request):
    '''
    Download a CSV file of all Polity_linguistic_family instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_linguistic_familys.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "linguistic_family",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_linguistic_family.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.linguistic_family,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_linguistic_family_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_linguistic_family instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_linguistic_familys.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The linguistic family of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "linguistic_family": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The linguistic family of a polity.",
            "units": None,
            "choices": INNER_POLITY_LINGUISTIC_FAMILY_CHOICES,
            "null_meaning": "This polity did not have a linguistic family.",
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
def polity_language_genus_download_view(request):
    '''
    Download a CSV file of all Polity_language_genus instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_language_genuss.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "language_genus",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_language_genus.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.language_genus,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_language_genus_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_language_genus instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_language_genuss.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The language genus of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "language_genus": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The language genus of a polity.",
            "units": None,
            "choices": INNER_POLITY_LINGUISTIC_FAMILY_CHOICES,
            "null_meaning": "This polity did not have a language Genus.",
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
def polity_religion_genus_download_view(request):
    '''
    Download a CSV file of all Polity_religion_genus instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_religion_genuss.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "religion_genus",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_religion_genus.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.religion_genus,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_religion_genus_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_religion_genus instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_religion_genuss.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The religion genus of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "religion_genus": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The religion genus of a polity.",
            "units": None,
            "choices": INNER_POLITY_RELIGION_GENUS_CHOICES,
            "null_meaning": "This polity did not have a religion genus.",
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
def polity_religion_family_download_view(request):
    '''
    Download a CSV file of all Polity_religion_family instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_religion_familys.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "religion_family",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_religion_family.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.religion_family,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_religion_family_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_religion_family instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_religion_familys.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The religion family of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "religion_family": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The religion family of a polity.",
            "units": None,
            "choices": INNER_POLITY_RELIGION_FAMILY_CHOICES,
            "null_meaning": "This polity did not have a religion family.",
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
def polity_religion_download_view(request):
    '''
    Download a CSV file of all Polity_religion instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_religions.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "religion",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_religion.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.religion,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_religion_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_religion instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_religions.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The religion of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "religion": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The religion of a polity.",
            "units": None,
            "choices": INNER_POLITY_RELIGION_CHOICES,
            "null_meaning": "This polity did not have a religion.",
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
def polity_relationship_to_preceding_entity_download_view(request):
    '''
    Download a CSV file of all Polity_relationship_to_preceding_entity instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_relationship_to_preceding_entitys.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "relationship_to_preceding_entity",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_relationship_to_preceding_entity.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.relationship_to_preceding_entity,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_relationship_to_preceding_entity_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_relationship_to_preceding_entity
    instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_relationship_to_preceding_entitys.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The polity relationship to preceding (quasi)polity",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "relationship_to_preceding_entity": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The polity relationship to preceding (quasi)polity",
            "units": None,
            "choices": INNER_POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES,
            "null_meaning": "This polity did not have a relationship to preceding (quasi)polity",  # noqa: E501 pylint: disable=C0301
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
def polity_preceding_entity_download_view(request):
    '''
    Download a CSV file of all Polity_preceding_entity instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_preceding_entitys.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "preceding_entity",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_preceding_entity.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.preceding_entity,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_preceding_entity_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_preceding_entity instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_preceding_entitys.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The preceding entity of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "preceding_entity": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The preceding entity (or the largest settlement) of a polity.",
            "units": None,
            "choices": None,
            "null_meaning": "This polity did not have a preceding entity.",
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
def polity_succeeding_entity_download_view(request):
    '''
    Download a CSV file of all Polity_succeeding_entity instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_succeeding_entitys.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "succeeding_entity",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_succeeding_entity.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.succeeding_entity,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_succeeding_entity_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_succeeding_entity instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_succeeding_entitys.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The succeeding entity of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "succeeding_entity": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The succeeding entity (or the largest settlement) of a polity.",
            "units": None,
            "choices": None,
            "null_meaning": "This polity did not have a succeeding entity.",
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
def polity_supracultural_entity_download_view(request):
    '''
    Download a CSV file of all Polity_supracultural_entity instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_supracultural_entitys.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "supracultural_entity",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_supracultural_entity.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.supracultural_entity,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_supracultural_entity_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_supracultural_entity instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_supracultural_entitys.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The supracultural entity of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "supracultural_entity": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The supracultural entity (or the largest settlement) of a polity.",
            "units": None,
            "choices": None,
            "null_meaning": "This polity did not have a supracultural entity.",
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
def polity_scale_of_supracultural_interaction_download_view(request):
    '''
    Download a CSV file of all Polity_scale_of_supracultural_interaction instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_scale_of_supracultural_interactions.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "scale_from",
            "scale_to",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_scale_of_supracultural_interaction.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.scale_from,
                obj.scale_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_scale_of_supracultural_interaction_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_scale_of_supracultural_interaction
    instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_scale_of_supracultural_interactions.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The scale_of_supra_cultural_interaction of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "scale_from": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The lower scale of supra cultural interactionfor a polity.",
            "units": "km squared",
            "choices": None,
            "null_meaning": NO_DATA.wiki,
        },
        "scale_to": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The upper scale of supra cultural interactionfor a polity.",
            "units": "km squared",
            "choices": None,
            "null_meaning": NO_DATA.wiki,
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
def polity_alternate_religion_genus_download_view(request):
    '''
    Download a CSV file of all Polity_alternate_religion_genus instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_alternate_religion_genuss.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "alternate_religion_genus",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_alternate_religion_genus.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.alternate_religion_genus,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_alternate_religion_genus_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_alternate_religion_genus instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_alternate_religion_genuss.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The alternate religion genus of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "alternate_religion_genus": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The alternate religion genus of a polity.",
            "units": None,
            "choices": INNER_POLITY_ALTERNATE_RELIGION_GENUS_CHOICES,
            "null_meaning": "This polity did not have a alternatereligion genus.",
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
def polity_alternate_religion_family_download_view(request):
    '''
    Download a CSV file of all Polity_alternate_religion_family instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_alternate_religion_familys.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "alternate_religion_family",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_alternate_religion_family.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.alternate_religion_family,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_alternate_religion_family_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_alternate_religion_family instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_alternate_religion_familys.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The alternate religion family of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "alternate_religion_family": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The alternate religion family of a polity.",
            "units": None,
            "choices": INNER_POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES,
            "null_meaning": "This polity did not have a alternate religion family.",
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
def polity_alternate_religion_download_view(request):
    '''
    Download a CSV file of all Polity_alternate_religion instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_alternate_religions.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "alternate_religion",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_alternate_religion.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.alternate_religion,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_alternate_religion_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_alternate_religion instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_alternate_religions.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The alternate religion  of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "alternate_religion": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The alternate religion of a polity.",
            "units": None,
            "choices": INNER_POLITY_ALTERNATE_RELIGION_CHOICES,
            "null_meaning": "This polity did not have a alternate religion .",
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
def polity_expert_download_view(request):
    '''
    Download a CSV file of all Polity_expert instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_experts.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "expert",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_expert.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.expert,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_expert_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_expert instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_experts.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The expert of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "expert": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The expert of a polity.",
            "units": None,
            "choices": None,
            "null_meaning": "This polity did not have an expert.",
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
def polity_editor_download_view(request):
    '''
    Download a CSV file of all Polity_editor instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_editors.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "editor",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_editor.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.editor,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_editor_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_editor instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_editors.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The editor of a polity.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "editor": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The editor of a polity.",
            "units": None,
            "choices": None,
            "null_meaning": "This polity did not have an editor.",
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
def polity_religious_tradition_download_view(request):
    '''
    Download a CSV file of all Polity_religious_tradition instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_religious_traditions.csv"'
    )

    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "religious_tradition",
            "confidence",
            "is_disputed",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_religious_tradition.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.religious_tradition,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_religious_tradition_meta_download_view(request):
    '''
    Download a CSV file of the meta data for Polity_religious_tradition instances.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="polity_religious_traditions.csv"'
    )

    my_meta_data_dic = {
        "notes": None,
        "main_desc": "The details of religious traditions.",
        "main_desc_source": None,
        "section": "General Variables",
        "subsection": "General",
    }
    my_meta_data_dic_inner_vars = {
        "religious_tradition": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The details of religious traditions.",
            "units": None,
            "choices": None,
            "null_meaning": NO_DATA.wiki,
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
def download_csv_all_general(request):
    '''
    Download a CSV file of all general variables. This includes all models in the "general"
    app.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The response object.
    '''
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"general_data_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    writer.writerow(
        [
            "section",
            "subsection",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "variable_name",
            "value_from",
            "value_to",
            "year_from",
            "year_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )
    # Iterate over each model
    for model in get_models(
        APP_NAME,
        exclude=[Polity_research_assistant, Polity_editor, Polity_expert],
    ):
        for obj in model.objects.all():
            if obj.clean_name_spaced() == "Polity Duration":
                writer.writerow(
                    [
                        "General Variables",
                        obj.subsection(),
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.clean_name()[7:],
                        obj.polity_year_from,
                        obj.polity_year_to,
                        obj.year_from,
                        obj.year_to,
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                    ]
                )
            elif obj.clean_name_spaced() == "Polity Peak Years":
                writer.writerow(
                    [
                        "General Variables",
                        obj.subsection(),
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.clean_name()[7:],
                        obj.peak_year_from,
                        obj.peak_year_to,
                        obj.year_from,
                        obj.year_to,
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                    ]
                )
            else:
                if any(
                    [
                        obj.show_value() == "NO_VALUE_ON_WIKI",
                        obj.show_value() == "NO_VALID_VALUE",
                    ]
                ):
                    continue
                elif "O_VALUE_ON_WIKI" in str(obj.show_value()):
                    continue
                else:
                    writer.writerow(
                        [
                            "General Variables",
                            obj.subsection(),
                            obj.polity.long_name,
                            obj.polity.new_name,
                            obj.polity.name,
                            obj.clean_name()[7:],
                            obj.show_value(),
                            None,
                            obj.year_from,
                            obj.year_to,
                            obj.get_tag_display(),
                            obj.is_disputed,
                            obj.is_uncertain,
                            obj.expert_reviewed,
                        ]
                    )

    return response
"""
