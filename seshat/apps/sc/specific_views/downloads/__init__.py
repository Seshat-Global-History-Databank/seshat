__all__ = [
    "ra_download_view",
    "ra_meta_download_view",
    "polity_territory_download_view",
    "polity_territory_meta_download_view",
    "polity_population_download_view",
    "polity_population_meta_download_view",
    "population_of_the_largest_settlement_download_view",
    "population_of_the_largest_settlement_meta_download_view",
    "settlement_hierarchy_download_view",
    "settlement_hierarchy_meta_download_view",
    "administrative_level_download_view",
    "administrative_level_meta_download_view",
    "religious_level_download_view",
    "religious_level_meta_download_view",
    "military_level_download_view",
    "military_level_meta_download_view",
    "professional_military_officer_download_view",
    "professional_military_officer_meta_download_view",
    "professional_soldier_download_view",
    "professional_soldier_meta_download_view",
    "professional_priesthood_download_view",
    "full_time_bureaucrat_download_view",
    "full_time_bureaucrat_meta_download_view",
    "examination_system_download_view",
    "examination_system_meta_download_view",
    "merit_promotion_download_view",
    "merit_promotion_meta_download_view",
    "specialized_government_building_download_view",
    "specialized_government_building_meta_download_view",
    "formal_legal_code_download_view",
    "formal_legal_code_meta_download_view",
    "judge_download_view",
    "judge_meta_download_view",
    "court_download_view",
    "court_meta_download_view",
    "professional_lawyer_download_view",
    "professional_lawyer_meta_download_view",
    "irrigation_system_download_view",
    "irrigation_system_meta_download_view",
    "drinking_water_supply_system_download_view",
    "drinking_water_supply_system_meta_download_view",
    "market_download_view",
    "market_meta_download_view",
    "food_storage_site_download_view",
    "food_storage_site_meta_download_view",
    "road_download_view",
    "road_meta_download_view",
    "bridge_download_view",
    "bridge_meta_download_view",
    "canal_download_view",
    "canal_meta_download_view",
    "port_download_view",
    "port_meta_download_view",
    "mines_or_quarry_download_view",
    "mines_or_quarry_meta_download_view",
    "mnemonic_device_download_view",
    "mnemonic_device_meta_download_view",
    "nonwritten_record_download_view",
    "nonwritten_record_meta_download_view",
    "written_record_download_view",
    "written_record_meta_download_view",
    "script_download_view",
    "script_meta_download_view",
    "non_phonetic_writing_download_view",
    "non_phonetic_writing_meta_download_view",
    "phonetic_alphabetic_writing_download_view",
    "phonetic_alphabetic_writing_meta_download_view",
    "lists_tables_and_classification_download_view",
    "lists_tables_and_classification_meta_download_view",
    "calendar_download_view",
    "calendar_meta_download_view",
    "sacred_text_download_view",
    "sacred_text_meta_download_view",
    "religious_literature_download_view",
    "religious_literature_meta_download_view",
    "practical_literature_download_view",
    "practical_literature_meta_download_view",
    "history_download_view",
    "history_meta_download_view",
    "philosophy_download_view",
    "philosophy_meta_download_view",
    "scientific_literature_download_view",
    "scientific_literature_meta_download_view",
    "fiction_download_view",
    "fiction_meta_download_view",
    "article_download_view",
    "article_meta_download_view",
    "token_download_view",
    "token_meta_download_view",
    "precious_metal_download_view",
    "precious_metal_meta_download_view",
    "foreign_coin_download_view",
    "foreign_coin_meta_download_view",
    "indigenous_coin_download_view",
    "indigenous_coin_meta_download_view",
    "paper_currency_download_view",
    "paper_currency_meta_download_view",
    "courier_download_view",
    "courier_meta_download_view",
    "postal_station_download_view",
    "postal_station_meta_download_view",
    "general_postal_service_download_view",
    "general_postal_service_meta_download_view",
]

import csv

from django.contrib.auth.decorators import permission_required
from django.shortcuts import HttpResponse

from ....utils import (
    get_date,
    get_models,
    write_csv,
)
from ....constants import (
    CSV_DELIMITER,
    SUBSECTIONS,
)

from ...constants import APP_NAME
from ...models import (
    Ra,
    Polity_territory,
    Polity_population,
    Population_of_the_largest_settlement,
    Settlement_hierarchy,
    Administrative_level,
    Religious_level,
    Military_level,
    Professional_military_officer,
    Professional_soldier,
    Professional_priesthood,
    Full_time_bureaucrat,
    Examination_system,
    Merit_promotion,
    Specialized_government_building,
    Formal_legal_code,
    Judge,
    Court,
    Professional_lawyer,
    Irrigation_system,
    Drinking_water_supply_system,
    Market,
    Food_storage_site,
    Road,
    Bridge,
    Canal,
    Port,
    Mines_or_quarry,
    Mnemonic_device,
    Nonwritten_record,
    Written_record,
    Script,
    Non_phonetic_writing,
    Phonetic_alphabetic_writing,
    Lists_tables_and_classification,
    Calendar,
    Sacred_text,
    Religious_literature,
    Practical_literature,
    History,
    Philosophy,
    Scientific_literature,
    Fiction,
    Article,
    Token,
    Precious_metal,
    Foreign_coin,
    Indigenous_coin,
    Paper_currency,
    Courier,
    Postal_station,
    General_postal_service,
)


PREFIX = "social_complexity_"

@permission_required("core.view_capital")
def ra_download_view(request):
    response = write_csv(Ra, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_territory_download_view(request):
    response = write_csv(Polity_territory, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_population_download_view(request):
    response = write_csv(Polity_population, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def population_of_the_largest_settlement_download_view(request):
    response = write_csv(Population_of_the_largest_settlement, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def settlement_hierarchy_download_view(request):
    response = write_csv(Settlement_hierarchy, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def administrative_level_download_view(request):
    response = write_csv(Administrative_level, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def religious_level_download_view(request):
    response = write_csv(Religious_level, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def military_level_download_view(request):
    response = write_csv(Military_level, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def professional_military_officer_download_view(request):
    response = write_csv(Professional_military_officer, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def professional_soldier_download_view(request):
    response = write_csv(Professional_soldier, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def professional_priesthood_download_view(request):
    response = write_csv(Professional_priesthood, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def full_time_bureaucrat_download_view(request):
    response = write_csv(Full_time_bureaucrat, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def examination_system_download_view(request):
    response = write_csv(Examination_system, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def merit_promotion_download_view(request):
    response = write_csv(Merit_promotion, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def specialized_government_building_download_view(request):
    response = write_csv(Specialized_government_building, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def formal_legal_code_download_view(request):
    response = write_csv(Formal_legal_code, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def judge_download_view(request):
    response = write_csv(Judge, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def court_download_view(request):
    response = write_csv(Court, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def professional_lawyer_download_view(request):
    response = write_csv(Professional_lawyer, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def irrigation_system_download_view(request):
    response = write_csv(Irrigation_system, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def drinking_water_supply_system_download_view(request):
    response = write_csv(Drinking_water_supply_system, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def market_download_view(request):
    response = write_csv(Market, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def food_storage_site_download_view(request):
    response = write_csv(Food_storage_site, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def road_download_view(request):
    response = write_csv(Road, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def bridge_download_view(request):
    response = write_csv(Bridge, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def canal_download_view(request):
    response = write_csv(Canal, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def port_download_view(request):
    response = write_csv(Port, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def mines_or_quarry_download_view(request):
    response = write_csv(Mines_or_quarry, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def mnemonic_device_download_view(request):
    response = write_csv(Mnemonic_device, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def nonwritten_record_download_view(request):
    response = write_csv(Nonwritten_record, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def written_record_download_view(request):
    response = write_csv(Written_record, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def script_download_view(request):
    response = write_csv(Script, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def non_phonetic_writing_download_view(request):
    response = write_csv(Non_phonetic_writing, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def phonetic_alphabetic_writing_download_view(request):
    response = write_csv(Phonetic_alphabetic_writing, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def lists_tables_and_classification_download_view(request):
    response = write_csv(Lists_tables_and_classification, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def calendar_download_view(request):
    response = write_csv(Calendar, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def sacred_text_download_view(request):
    response = write_csv(Sacred_text, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def religious_literature_download_view(request):
    response = write_csv(Religious_literature, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def practical_literature_download_view(request):
    response = write_csv(Practical_literature, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def history_download_view(request):
    response = write_csv(History, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def philosophy_download_view(request):
    response = write_csv(Philosophy, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def scientific_literature_download_view(request):
    response = write_csv(Scientific_literature, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def fiction_download_view(request):
    response = write_csv(Fiction, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def article_download_view(request):
    response = write_csv(Article, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def token_download_view(request):
    response = write_csv(Token, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def precious_metal_download_view(request):
    response = write_csv(Precious_metal, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def foreign_coin_download_view(request):
    response = write_csv(Foreign_coin, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def indigenous_coin_download_view(request):
    response = write_csv(Indigenous_coin, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def paper_currency_download_view(request):
    response = write_csv(Paper_currency, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def courier_download_view(request):
    response = write_csv(Courier, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def postal_station_download_view(request):
    response = write_csv(Postal_station, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def general_postal_service_download_view(request):
    response = write_csv(General_postal_service, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def ra_meta_download_view(request):
    response = write_csv(Ra, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_territory_meta_download_view(request):
    response = write_csv(Polity_territory, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polity_population_meta_download_view(request):
    response = write_csv(Polity_population, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def population_of_the_largest_settlement_meta_download_view(request):
    response = write_csv(
        Population_of_the_largest_settlement, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def settlement_hierarchy_meta_download_view(request):
    response = write_csv(Settlement_hierarchy, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def administrative_level_meta_download_view(request):
    response = write_csv(Administrative_level, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def religious_level_meta_download_view(request):
    response = write_csv(Religious_level, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def military_level_meta_download_view(request):
    response = write_csv(Military_level, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def professional_military_officer_meta_download_view(request):
    response = write_csv(Professional_military_officer, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def professional_soldier_meta_download_view(request):
    response = write_csv(Professional_soldier, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def professional_priesthood_meta_download_view(request):
    response = write_csv(Professional_priesthood, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def full_time_bureaucrat_meta_download_view(request):
    response = write_csv(Full_time_bureaucrat, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def examination_system_meta_download_view(request):
    response = write_csv(Examination_system, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def merit_promotion_meta_download_view(request):
    response = write_csv(Merit_promotion, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def specialized_government_building_meta_download_view(request):
    response = write_csv(
        Specialized_government_building, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def formal_legal_code_meta_download_view(request):
    response = write_csv(Formal_legal_code, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def judge_meta_download_view(request):
    response = write_csv(Judge, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def court_meta_download_view(request):
    response = write_csv(Court, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def professional_lawyer_meta_download_view(request):
    response = write_csv(Professional_lawyer, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def irrigation_system_meta_download_view(request):
    response = write_csv(Irrigation_system, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def drinking_water_supply_system_meta_download_view(request):
    response = write_csv(Drinking_water_supply_system, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def market_meta_download_view(request):
    response = write_csv(Market, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def food_storage_site_meta_download_view(request):
    response = write_csv(Food_storage_site, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def road_meta_download_view(request):
    response = write_csv(Road, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def bridge_meta_download_view(request):
    response = write_csv(Bridge, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def canal_meta_download_view(request):
    response = write_csv(Canal, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def port_meta_download_view(request):
    response = write_csv(Port, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def mines_or_quarry_meta_download_view(request):
    response = write_csv(Mines_or_quarry, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def mnemonic_device_meta_download_view(request):
    response = write_csv(Mnemonic_device, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def nonwritten_record_meta_download_view(request):
    response = write_csv(Nonwritten_record, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def written_record_meta_download_view(request):
    response = write_csv(Written_record, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def script_meta_download_view(request):
    response = write_csv(Script, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def non_phonetic_writing_meta_download_view(request):
    response = write_csv(Non_phonetic_writing, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def phonetic_alphabetic_writing_meta_download_view(request):
    response = write_csv(Phonetic_alphabetic_writing, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def lists_tables_and_classification_meta_download_view(request):
    response = write_csv(
        Lists_tables_and_classification, "meta", prefix=PREFIX
    )
    return response


@permission_required("core.view_capital")
def calendar_meta_download_view(request):
    response = write_csv(Calendar, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def sacred_text_meta_download_view(request):
    response = write_csv(Sacred_text, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def religious_literature_meta_download_view(request):
    response = write_csv(Religious_literature, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def practical_literature_meta_download_view(request):
    response = write_csv(Practical_literature, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def history_meta_download_view(request):
    response = write_csv(History, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def philosophy_meta_download_view(request):
    response = write_csv(Philosophy, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def scientific_literature_meta_download_view(request):
    response = write_csv(Scientific_literature, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def fiction_meta_download_view(request):
    response = write_csv(Fiction, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def article_meta_download_view(request):
    response = write_csv(Article, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def token_meta_download_view(request):
    response = write_csv(Token, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def precious_metal_meta_download_view(request):
    response = write_csv(Precious_metal, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def foreign_coin_meta_download_view(request):
    response = write_csv(Foreign_coin, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def indigenous_coin_meta_download_view(request):
    response = write_csv(Indigenous_coin, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def paper_currency_meta_download_view(request):
    response = write_csv(Paper_currency, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def courier_meta_download_view(request):
    response = write_csv(Courier, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def postal_station_meta_download_view(request):
    response = write_csv(Postal_station, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def general_postal_service_meta_download_view(request):
    response = write_csv(General_postal_service, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def download_csv_all_sc(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_data_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(APP_NAME):
        # Get all rows of data from the model
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
def download_csv_social_scale(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_social_scale_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(
        APP_NAME, exclude=["Ra"], subsection=SUBSECTIONS.sc.SocialScale
    ):
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
def download_csv_professions(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_professions_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(
        APP_NAME, exclude=["Ra"], subsection=SUBSECTIONS.sc.Professions
    ):
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
def download_csv_bureaucracy_characteristics(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_bureaucracy_characteristics_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(
        APP_NAME,
        exclude=["Ra"],
        subsection=SUBSECTIONS.sc.BureaucracyCharacteristics,
    ):
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
def download_csv_hierarchical_complexity(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_hierarchical_complexity_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(
        APP_NAME,
        exclude=["Ra"],
        subsection=SUBSECTIONS.sc.HierarchicalComplexity,
    ):
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
def download_csv_law(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_law_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(
        APP_NAME, exclude=["Ra"], subsection=SUBSECTIONS.sc.Law
    ):
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
def download_csv_specialized_buildings_polity_owned(request):
    date = get_date()

    # Create a file name
    file_name = (
        f"social_complexity_specialized_buildings_polity_owned_{date}.csv"
    )

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(
        APP_NAME,
        exclude=["Ra"],
        subsection=SUBSECTIONS.sc.SpecializedBuildings,
    ):
        # TODO: Note the subsection was changed in the line above from "Specialized
        # Buildings: polity owned" to "Specialized Buildings Polity Owned"
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
def download_csv_transport_infrastructure(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_transport_infrastructure_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(
        APP_NAME,
        exclude=["Ra"],
        subsection=SUBSECTIONS.sc.TransportInfrastructure,
    ):
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
def download_csv_special_purpose_sites(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_special_purpose_sites_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(
        APP_NAME, exclude=["Ra"], subsection=SUBSECTIONS.sc.SpecialPurposeSites
    ):
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
def download_csv_information(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_information_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

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

    # Iterate over each model
    for model in get_models(
        APP_NAME, exclude=["Ra"], subsection=SUBSECTIONS.sc.Information
    ):
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


"""
@permission_required("core.view_capital")
def ra_download_view(request):
    '''
    Download all the data in the Ra model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_ra_{date}.csv"
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
            "sc_ra",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Ra.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.sc_ra,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def ra_meta_download_view(request):
    '''
    Download the metadata of the Ra model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="metadata_ras.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The name of the research assistant or associate who coded the data. If more than one RA made a substantial contribution, list all via separate entries.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "staff",
    }
    my_meta_data_dic_inner_vars = {
        "sc_ra": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The RA of Social Complexity Variables",
            "units": None,
            "choices": None,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def polity_territory_download_view(request):
    '''
    Download all the data in the Polity_territory model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_polity_territory_{date}.csv"
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
            "polity_territory_from",
            "polity_territory_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_territory.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.polity_territory_from,
                obj.polity_territory_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_territory_meta_download_view(request):
    '''
    Download the metadata of the Polity_territory model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_polity_territorys.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Social Scale, Polity territory is coded in squared kilometers.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Social Scale",
    }
    my_meta_data_dic_inner_vars = {
        "polity_territory_from": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The lower range of polity territory for a polity.",
            "units": "km squared",
            "choices": None,
            "null_meaning": None,
        },
        "polity_territory_to": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The upper range of polity territory for a polity.",
            "units": "km squared",
            "choices": None,
            "null_meaning": None,
        },
    }

    # Create a CSV writer
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
def polity_population_download_view(request):
    '''
    Download all the data of the Polity_population model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_polity_population_{date}.csv"
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
            "polity_population_from",
            "polity_population_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Polity_population.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.polity_population_from,
                obj.polity_population_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polity_population_meta_download_view(request):
    '''
    Download the metadata of the Polity_population model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    '''
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_polity_populations.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Social Scale, Polity Population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Social Scale",
    }
    my_meta_data_dic_inner_vars = {
        "polity_population_from": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The lower range of polity population for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
        "polity_population_to": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The upper range of polity population for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
    }

    # Create a CSV writer
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
def population_of_the_largest_settlement_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    file_name = (
        f"social_complexity_population_of_the_largest_settlement_{date}.csv"
    )

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
            "population_of_the_largest_settlement_from",
            "population_of_the_largest_settlement_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Population_of_the_largest_settlement.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.population_of_the_largest_settlement_from,
                obj.population_of_the_largest_settlement_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def population_of_the_largest_settlement_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_population_of_the_largest_settlements.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Social Scale, Population of the largest settlement is the estimated population of the largest settlement of the polity. Note that the largest settlement could be different from the capital (coded under General Variables). If possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). Note that we are also building a city database - you should consult it as it may already have the needed data.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Social Scale",
    }
    my_meta_data_dic_inner_vars = {
        "population_of_the_largest_settlement_from": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The lower range of population of the largest settlement for a polity.",  # noqa: E501 pylint: disable=C0301
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
        "population_of_the_largest_settlement_to": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The upper range of population of the largest settlement for a polity.",  # noqa: E501 pylint: disable=C0301
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
    }

    # Create a CSV writer
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
def settlement_hierarchy_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_settlement_hierarchy_{date}.csv"
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
            "settlement_hierarchy_from",
            "settlement_hierarchy_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Settlement_hierarchy.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.settlement_hierarchy_from,
                obj.settlement_hierarchy_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def settlement_hierarchy_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_settlement_hierarchys.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Hierarchical Complexity, Settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. As settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). Example: (1) Large City (monumental structures, theatre, market, hospital, central government buildings) (2) City (market, theatre, regional government buildings) (3) Large Town (market, administrative buildings) (4) Town (administrative buildings, storehouse)) (5) Village (shrine) (6) Hamlet (residential only). In the narrative paragraph explain the different levels and list their functions. Provide a (crude) estimate of population sizes. For example, Large Town (market, temple, administrative buildings): 2,000-5,000 inhabitants.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Hierarchical Complexity",
    }
    my_meta_data_dic_inner_vars = {
        "settlement_hierarchy_from": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The lower range of settlement hierarchy for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
        "settlement_hierarchy_to": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The upper range of settlement hierarchy for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
    }

    # Create a CSV writer
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
def administrative_level_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_administrative_level_{date}.csv"
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
            "administrative_level_from",
            "administrative_level_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Administrative_level.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.administrative_level_from,
                obj.administrative_level_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def administrative_level_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_administrative_levels.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Hierarchical Complexity, Administrative levels records the administrative levels of a polity. An example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. Note that unlike in settlement hierarchy, here you code people hierarchy. Do not simply copy settlement hierarchy data here. For archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. Note: Often there are more than one concurrent administrative hierarchy. In the example above the hierarchy refers to the territorial government. In addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. For example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. In the narrative paragraph detail what is known about both hierarchies. The machine-readable code should reflect the largest number (the longer chain of command).",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Hierarchical Complexity",
    }
    my_meta_data_dic_inner_vars = {
        "administrative_level_from": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The lower range of administrative level for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
        "administrative_level_to": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The upper range of administrative level for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
    }

    # Create a CSV writer
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
def religious_level_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_religious_level_{date}.csv"
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
            "religious_level_from",
            "religious_level_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Religious_level.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.religious_level_from,
                obj.religious_level_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def religious_level_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_religious_levels.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Hierarchical Complexity, Religious levels records the Religious levels of a polity. Same principle as with Administrative levels. Start with the head of the official cult (if present) coded as: level 1, and work down to the local priest.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Hierarchical Complexity",
    }
    my_meta_data_dic_inner_vars = {
        "religious_level_from": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The lower range of religious level for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
        "religious_level_to": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The upper range of religious level for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
    }

    # Create a CSV writer
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
def military_level_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_military_level_{date}.csv"
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
            "military_level_from",
            "military_level_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Military_level.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.military_level_from,
                obj.military_level_to,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def military_level_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_military_levels.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Hierarchical Complexity, Military levels records the Military levels of a polity. Same principle as with Administrative levels. Start with the commander-in-chief coded as: level 1, and work down to the private. Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier).",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Hierarchical Complexity",
    }
    my_meta_data_dic_inner_vars = {
        "military_level_from": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The lower range of military level for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
        "military_level_to": {
            "min": 0,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The upper range of military level for a polity.",
            "units": None,
            "choices": None,
            "null_meaning": None,
        },
    }

    # Create a CSV writer
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
def professional_military_officer_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_professional_military_officer_{date}.csv"
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
            "professional_military_officer",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Professional_military_officer.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.professional_military_officer,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def professional_military_officer_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_professional_military_officers.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Professions, Professional military officers refer to Full-time Professional military officers.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Professions",
    }
    my_meta_data_dic_inner_vars = {
        "professional_military_officer": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of professional military officer for a polity.",  # noqa: E501 pylint: disable=C0301
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def professional_soldier_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_professional_soldier_{date}.csv"
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
            "professional_soldier",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Professional_soldier.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.professional_soldier,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def professional_soldier_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_professional_soldiers.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Professions, Professional soldiers refer to Full-time Professional soldiers.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Professions",
    }
    my_meta_data_dic_inner_vars = {
        "professional_soldier": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of professional soldier for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def professional_priesthood_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_professional_priesthood_{date}.csv"
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
            "professional_priesthood",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Professional_priesthood.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.professional_priesthood,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def professional_priesthood_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_professional_priesthoods.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Professions, Professional priesthood refers to Full-time Professional priesthood.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Professions",
    }
    my_meta_data_dic_inner_vars = {
        "professional_priesthood": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of professional priesthood for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def full_time_bureaucrat_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_full_time_bureaucrat_{date}.csv"
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
            "full_time_bureaucrat",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Full_time_bureaucrat.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.full_time_bureaucrat,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def full_time_bureaucrat_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_full_time_bureaucrats.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Bureaucracy characteristics, Full-time bureaucrats refer to Full-time administrative specialists. Code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. Also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. Note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Bureaucracy characteristics",
    }
    my_meta_data_dic_inner_vars = {
        "full_time_bureaucrat": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of full time bureaucrat for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def examination_system_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_examination_system_{date}.csv"
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
            "examination_system",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Examination_system.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.examination_system,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def examination_system_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_examination_systems.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Bureaucracy characteristics, The paradigmatic example of an Examination system is the Chinese imperial system.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Bureaucracy characteristics",
    }
    my_meta_data_dic_inner_vars = {
        "examination_system": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of examination system for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def merit_promotion_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_merit_promotion_{date}.csv"
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
            "merit_promotion",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Merit_promotion.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.merit_promotion,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def merit_promotion_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_merit_promotions.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Bureaucracy characteristics, Merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. When exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Bureaucracy characteristics",
    }
    my_meta_data_dic_inner_vars = {
        "merit_promotion": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of merit promotion for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def specialized_government_building_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_specialized_government_building_{date}.csv"
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
            "specialized_government_building",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Specialized_government_building.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.specialized_government_building,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def specialized_government_building_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_specialized_government_buildings.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Bureaucracy characteristics, These buildings are where administrative officials are located, and must be distinct from the ruler's palace. They may be used for document storage, registration offices, minting money, etc. Defense structures also are not coded here (see Military). State-owned/operated workshop should also not be coded here.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Bureaucracy characteristics",
    }
    my_meta_data_dic_inner_vars = {
        "specialized_government_building": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of specialized government building for a polity.",  # noqa: E501 pylint: disable=C0301
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def formal_legal_code_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_formal_legal_code_{date}.csv"
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
            "formal_legal_code",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Formal_legal_code.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.formal_legal_code,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def formal_legal_code_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_formal_legal_codes.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Law, Formal legal code refers to legal code usually, but not always written down. If not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). Provide a short description",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Law",
    }
    my_meta_data_dic_inner_vars = {
        "formal_legal_code": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of formal legal code for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def judge_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_judge_{date}.csv"
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
            "judge",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Judge.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.judge,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def judge_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_judges.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Law, judges refers only to full-time professional judges",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Law",
    }
    my_meta_data_dic_inner_vars = {
        "judge": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of judge for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }
    # Create a CSV writer
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
def court_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_court_{date}.csv"
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
            "court",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Court.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.court,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def court_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_courts.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Law, courts are buildings specialized for legal proceedings only.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Law",
    }
    my_meta_data_dic_inner_vars = {
        "court": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of court for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }
    # Create a CSV writer
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
def professional_lawyer_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_professional_lawyer_{date}.csv"
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
            "professional_lawyer",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Professional_lawyer.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.professional_lawyer,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def professional_lawyer_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_professional_lawyers.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Law, NO_DESCRIPTIONS_IN_CODEBOOK.",
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Law",
    }
    my_meta_data_dic_inner_vars = {
        "professional_lawyer": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of professional lawyer for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def irrigation_system_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_irrigation_system_{date}.csv"
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
            "irrigation_system",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Irrigation_system.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.irrigation_system,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def irrigation_system_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_irrigation_systems.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Specialized Buildings, irrigation systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Specialized Buildings",
    }
    my_meta_data_dic_inner_vars = {
        "irrigation_system": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of irrigation system for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def drinking_water_supply_system_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_drinking_water_supply_system_{date}.csv"
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
            "drinking_water_supply_system",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Drinking_water_supply_system.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.drinking_water_supply_system,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def drinking_water_supply_system_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_drinking_water_supply_systems.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Specialized Buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Specialized Buildings",
    }
    my_meta_data_dic_inner_vars = {
        "drinking_water_supply_system": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of drinking water supply system for a polity.",  # noqa: E501 pylint: disable=C0301
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def market_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_market_{date}.csv"
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
            "market",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Market.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.market,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def market_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_markets.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Specialized Buildings, markets are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Specialized Buildings",
    }
    my_meta_data_dic_inner_vars = {
        "market": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of market for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def food_storage_site_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_food_storage_site_{date}.csv"
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
            "food_storage_site",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Food_storage_site.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.food_storage_site,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def food_storage_site_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_food_storage_sites.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Specialized Buildings, food storage sites are polity owned (which  includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Specialized Buildings",
    }
    my_meta_data_dic_inner_vars = {
        "food_storage_site": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of food storage site for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def road_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_road_{date}.csv"
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
            "road",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Road.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.road,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def road_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_roads.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. It excludes streets/accessways within settlements and paths between settlements that develop through repeated use.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Transport infrastructure",
    }
    my_meta_data_dic_inner_vars = {
        "road": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of road for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def bridge_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_bridge_{date}.csv"
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
            "bridge",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Bridge.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.bridge,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def bridge_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_bridges.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it).",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Transport infrastructure",
    }
    my_meta_data_dic_inner_vars = {
        "bridge": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of bridge for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def canal_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_canal_{date}.csv"
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
            "canal",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Canal.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.canal,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def canal_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_canals.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it).",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Transport infrastructure",
    }
    my_meta_data_dic_inner_vars = {
        "canal": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of canal for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def port_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_port_{date}.csv"
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
            "port",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Port.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.port,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def port_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_ports.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Transport infrastructure, Ports include river ports. Direct historical or archaeological evidence of Ports is absent when no port has been excavated or all evidence of such has been obliterated. Indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta Egypt at a time we know there was a timber trade with the Levant). When evidence for the variable itself is available the code is 'present.' When other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). When indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Transport infrastructure",
    }
    my_meta_data_dic_inner_vars = {
        "port": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of port for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def mines_or_quarry_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_mine_or_quarry_{date}.csv"
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
            "mines_or_quarry",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Mines_or_quarry.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.mines_or_quarry,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def mines_or_quarry_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_mines_or_quarrys.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Special purpose sites, NO_DESCRIPTIONS_IN_CODEBOOK",
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Special purpose sites",
    }
    my_meta_data_dic_inner_vars = {
        "mines_or_quarry": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of mines or quarry for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def mnemonic_device_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_mnemonic_device_{date}.csv"
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
            "mnemonic_device",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Mnemonic_device.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.mnemonic_device,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def mnemonic_device_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_mnemonic_devices.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Writing Systems, Mnemonic devices are: For example, tallies",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Writing Systems",
    }
    my_meta_data_dic_inner_vars = {
        "mnemonic_device": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of mnemonic device for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def nonwritten_record_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_nonwritten_record_{date}.csv"
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
            "nonwritten_record",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Nonwritten_record.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.nonwritten_record,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def nonwritten_record_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_nonwritten_records.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Writing Systems, Nonwritten Records are more extensive than mnemonics, but don't utilize script. Example: quipu; seals and stamps",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Writing Systems",
    }
    my_meta_data_dic_inner_vars = {
        "nonwritten_record": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of nonwritten record for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def written_record_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_written_records_{date}.csv"
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
            "written_record",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Written_record.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.written_record,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def written_record_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_written_records.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Writing Systems, Written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. There must be several sentences strung together, at the very minimum. For example, royal proclamations from Mesopotamia and Egypt qualify as written records",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Writing Systems",
    }
    my_meta_data_dic_inner_vars = {
        "written_record": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of written record for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def script_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_script_{date}.csv"
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
            "script",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Script.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.script,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def script_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_scripts.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Writing Systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Writing Systems",
    }
    my_meta_data_dic_inner_vars = {
        "script": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of script for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def non_phonetic_writing_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_non_phonetic_writing_{date}.csv"
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
            "non_phonetic_writing",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Non_phonetic_writing.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.non_phonetic_writing,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def non_phonetic_writing_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_non_phonetic_writings.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Writing Systems, this refers to the kind of script",
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Writing Systems",
    }
    my_meta_data_dic_inner_vars = {
        "non_phonetic_writing": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of non phonetic writing for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def phonetic_alphabetic_writing_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_phonetic_alphabetic_writing_{date}.csv"
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
            "phonetic_alphabetic_writing",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Phonetic_alphabetic_writing.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.phonetic_alphabetic_writing,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def phonetic_alphabetic_writing_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_phonetic_alphabetic_writings.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Writing Systems, this refers to the kind of script",
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Writing Systems",
    }
    my_meta_data_dic_inner_vars = {
        "phonetic_alphabetic_writing": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of phonetic alphabetic writing for a polity.",  # noqa: E501 pylint: disable=C0301
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def lists_tables_and_classification_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_list_table_and_classification_{date}.csv"
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
            "lists_tables_and_classification",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Lists_tables_and_classification.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.lists_tables_and_classification,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def lists_tables_and_classification_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_lists_tables_and_classifications.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Kinds of Written Documents",
    }
    my_meta_data_dic_inner_vars = {
        "lists_tables_and_classification": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of lists tables and classification for a polity.",  # noqa: E501 pylint: disable=C0301
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def calendar_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_calendar_{date}.csv"
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
            "calendar",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Calendar.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.calendar,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def calendar_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_calendars.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Kinds of Written Documents",
    }
    my_meta_data_dic_inner_vars = {
        "calendar": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of calendar for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def sacred_text_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_sacred_text_{date}.csv"
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
            "sacred_text",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Sacred_text.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.sacred_text,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def sacred_text_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_sacred_texts.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Kinds of Written Documents, Sacred Texts originate from supernatural agents (deities), or are directly inspired by them.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Kinds of Written Documents",
    }
    my_meta_data_dic_inner_vars = {
        "sacred_text": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of sacred text for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def religious_literature_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_religious_literature_{date}.csv"
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
            "religious_literature",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Religious_literature.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.religious_literature,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def religious_literature_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_religious_literatures.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Kinds of Written Documents, Religious literature differs from the sacred texts. For example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Kinds of Written Documents",
    }
    my_meta_data_dic_inner_vars = {
        "religious_literature": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of religious literature for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def practical_literature_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_practical_literature_{date}.csv"
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
            "practical_literature",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Practical_literature.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.practical_literature,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def practical_literature_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_practical_literatures.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Kinds of Written Documents, Practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. Letters do not count as practical literature.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Kinds of Written Documents",
    }
    my_meta_data_dic_inner_vars = {
        "practical_literature": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of practical literature for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def history_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_history_{date}.csv"
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
            "history",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in History.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.history,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def history_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_historys.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Kinds of Written Documents",
    }
    my_meta_data_dic_inner_vars = {
        "history": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of history for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def philosophy_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_philosophy_{date}.csv"
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
            "philosophy",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Philosophy.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.philosophy,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def philosophy_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_philosophys.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Kinds of Written Documents",
    }
    my_meta_data_dic_inner_vars = {
        "philosophy": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of philosophy for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def scientific_literature_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_scientific_literature_{date}.csv"
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
            "scientific_literature",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Scientific_literature.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.scientific_literature,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def scientific_literature_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_scientific_literatures.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Kinds of Written Documents, Scientific literature includes mathematics, natural sciences, social sciences",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Kinds of Written Documents",
    }
    my_meta_data_dic_inner_vars = {
        "scientific_literature": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of scientific literature for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def fiction_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_fiction_{date}.csv"
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
            "fiction",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Fiction.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.fiction,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def fiction_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_fictions.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about Kinds of Written Documents, fiction includes poetry.",
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Kinds of Written Documents",
    }
    my_meta_data_dic_inner_vars = {
        "fiction": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of fiction for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def article_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_article_{date}.csv"
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
            "article",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Article.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.article,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def article_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_articles.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Forms of money",
    }
    my_meta_data_dic_inner_vars = {
        "article": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of article for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def token_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_token_{date}.csv"
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
            "token",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Token.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.token,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def token_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_tokens.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Forms of money",
    }
    my_meta_data_dic_inner_vars = {
        "token": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of token for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
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
def precious_metal_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_precious_metal_{date}.csv"
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
            "precious_metal",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Precious_metal.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.precious_metal,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def precious_metal_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_precious_metals.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about forms of money, Precious metals are non-coined silver, gold, platinum",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Forms of money",
    }
    my_meta_data_dic_inner_vars = {
        "precious_metal": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of precious metal for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }
    # Create a CSV writer
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
def foreign_coin_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_foreign_coin_{date}.csv"
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
            "foreign_coin",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Foreign_coin.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.foreign_coin,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def foreign_coin_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_foreign_coins.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "NO_DESCRIPTIONS_IN_CODEBOOK",
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Forms of money",
    }
    my_meta_data_dic_inner_vars = {
        "foreign_coin": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of foreign coin for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }
    # Create a CSV writer
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
def indigenous_coin_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_indigenous_coin_{date}.csv"
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
            "indigenous_coin",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Indigenous_coin.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.indigenous_coin,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def indigenous_coin_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_indigenous_coins.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "NO_DESCRIPTIONS_IN_CODEBOOK",
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Forms of money",
    }
    my_meta_data_dic_inner_vars = {
        "indigenous_coin": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of indigenous coin for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }
    # Create a CSV writer
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
def paper_currency_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_paper_currency_{date}.csv"
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
            "paper_currency",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Paper_currency.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.paper_currency,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def paper_currency_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_paper_currencys.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Paper currency or another kind of fiat money. Note that this only refers to indigenously produced paper currency. Code absent if colonial money is used.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Forms of money",
    }
    my_meta_data_dic_inner_vars = {
        "paper_currency": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of paper currency for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }
    # Create a CSV writer
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
def courier_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_courier_{date}.csv"
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
            "courier",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Courier.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.courier,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def courier_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_couriers.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Full-time professional couriers.",
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Postal systems",
    }
    my_meta_data_dic_inner_vars = {
        "courier": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of courier for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }
    # Create a CSV writer
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
def postal_station_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_postal_station_{date}.csv"
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
            "postal_station",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in Postal_station.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.postal_station,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def postal_station_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_postal_stations.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about postal systems, Postal stations are specialized buildings exclusively devoted to the postal service. If there is a special building that has other functions than a postal station, we still code postal station as present. The intent is to capture additional infrastructure beyond having a corps of messengers.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Postal systems",
    }
    my_meta_data_dic_inner_vars = {
        "postal_station": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of postal station for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }
    # Create a CSV writer
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
def general_postal_service_download_view(request):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_general_postal_service_{date}.csv"
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
            "general_postal_service",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )

    for obj in General_postal_service.objects.all():
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity.long_name,
                obj.polity.new_name,
                obj.polity.name,
                obj.general_postal_service,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
                obj.drb_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def general_postal_service_meta_download_view(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="metadata_general_postal_services.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "Talking about postal systems, 'General postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens.",  # noqa: E501 pylint: disable=C0301
        "main_desc_source": "NOTHING",
        "section": "Social Complexity",
        "subsection": "Postal systems",
    }
    my_meta_data_dic_inner_vars = {
        "general_postal_service": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of general postal service for a polity.",
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }
    # Create a CSV writer
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
"""
