from django.contrib.auth.decorators import permission_required
from django.shortcuts import HttpResponse

import csv
import datetime

from ....utils import get_models, write_csv
from ....constants import CSV_DELIMITER, SUBSECTIONS

from ...models import (
    Long_wall,
    Copper,
    Bronze,
    Iron,
    Steel,
    Javelin,
    Atlatl,
    Sling,
    Self_bow,
    Composite_bow,
    Crossbow,
    Tension_siege_engine,
    Sling_siege_engine,
    Gunpowder_siege_artillery,
    Handheld_firearm,
    War_club,
    Battle_axe,
    Dagger,
    Sword,
    Spear,
    Polearm,
    Dog,
    Donkey,
    Horse,
    Camel,
    Elephant,
    Wood_bark_etc,
    Leather_cloth,
    Shield,
    Helmet,
    Breastplate,
    Limb_protection,
    Scaled_armor,
    Laminar_armor,
    Plate_armor,
    Small_vessels_canoes_etc,
    Merchant_ships_pressed_into_service,
    Specialized_military_vessel,
    Settlements_in_a_defensive_position,
    Wooden_palisade,
    Earth_rampart,
    Ditch,
    Moat,
    Stone_walls_non_mortared,
    Stone_walls_mortared,
    Fortified_camp,
    Complex_fortification,
    Modern_fortification,
    Chainmail,
)
from ...constants import APP_NAME
from .constants import PREFIX


__all__ = [
    # Model-based download views
    "long_wall_download_view",
    "copper_download_view",
    "bronze_download_view",
    "iron_download_view",
    "steel_download_view",
    "javelin_download_view",
    "atlatl_download_view",
    "sling_download_view",
    "self_bow_download_view",
    "composite_bow_download_view",
    "crossbow_download_view",
    "tension_siege_engine_download_view",
    "sling_siege_engine_download_view",
    "gunpowder_siege_artillery_download_view",
    "handheld_firearm_download_view",
    "war_club_download_view",
    "battle_axe_download_view",
    "dagger_download_view",
    "sword_download_view",
    "spear_download_view",
    "polearm_download_view",
    "dog_download_view",
    "donkey_download_view",
    "horse_download_view",
    "camel_download_view",
    "elephant_download_view",
    "wood_bark_etc_download_view",
    "leather_cloth_download_view",
    "shield_download_view",
    "helmet_download_view",
    "breastplate_download_view",
    "limb_protection_download_view",
    "scaled_armor_download_view",
    "laminar_armor_download_view",
    "plate_armor_download_view",
    "small_vessels_canoes_etc_download_view",
    "merchant_ships_pressed_into_service_download_view",
    "specialized_military_vessel_download_view",
    "settlements_in_a_defensive_position_download_view",
    "wooden_palisade_download_view",
    "earth_rampart_download_view",
    "ditch_download_view",
    "moat_download_view",
    "stone_walls_mortared_download_view",
    "stone_walls_non_mortared_download_view",
    "fortified_camp_download_view",
    "complex_fortification_download_view",
    "modern_fortification_download_view",
    "chainmail_download_view",

    # Specialized download views
    "download_csv_naval_technology",
    "download_csv_armor",
    "download_csv_animals_used_in_warfare",
    "download_csv_handheld_weapons",
    "download_csv_projectiles",
    "download_csv_military_use_of_metals",
    "download_csv_fortifications",
    "download_csv_all_wf",
]


@permission_required("core.view_capital")
def long_wall_download_view(request):
    response = write_csv(Long_wall, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def copper_download_view(request):
    response = write_csv(Copper, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def bronze_download_view(request):
    response = write_csv(Bronze, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def iron_download_view(request):
    response = write_csv(Iron, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def steel_download_view(request):
    response = write_csv(Steel, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def javelin_download_view(request):
    response = write_csv(Javelin, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def atlatl_download_view(request):
    response = write_csv(Atlatl, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def sling_download_view(request):
    response = write_csv(Sling, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def self_bow_download_view(request):
    response = write_csv(Self_bow, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def composite_bow_download_view(request):
    response = write_csv(Composite_bow, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def crossbow_download_view(request):
    response = write_csv(Crossbow, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def tension_siege_engine_download_view(request):
    response = write_csv(Tension_siege_engine, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def sling_siege_engine_download_view(request):
    response = write_csv(Sling_siege_engine, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def gunpowder_siege_artillery_download_view(request):
    response = write_csv(Gunpowder_siege_artillery, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def handheld_firearm_download_view(request):
    response = write_csv(Handheld_firearm, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def war_club_download_view(request):
    response = write_csv(War_club, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def battle_axe_download_view(request):
    response = write_csv(Battle_axe, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def dagger_download_view(request):
    response = write_csv(Dagger, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def sword_download_view(request):
    response = write_csv(Sword, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def spear_download_view(request):
    response = write_csv(Spear, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polearm_download_view(request):
    response = write_csv(Polearm, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def dog_download_view(request):
    response = write_csv(Dog, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def donkey_download_view(request):
    response = write_csv(Donkey, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def horse_download_view(request):
    response = write_csv(Horse, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def camel_download_view(request):
    response = write_csv(Camel, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def elephant_download_view(request):
    response = write_csv(Elephant, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def wood_bark_etc_download_view(request):
    response = write_csv(Wood_bark_etc, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def leather_cloth_download_view(request):
    response = write_csv(Leather_cloth, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def shield_download_view(request):
    response = write_csv(Shield, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def helmet_download_view(request):
    response = write_csv(Helmet, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def breastplate_download_view(request):
    response = write_csv(Breastplate, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def limb_protection_download_view(request):
    response = write_csv(Limb_protection, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def scaled_armor_download_view(request):
    response = write_csv(Scaled_armor, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def laminar_armor_download_view(request):
    response = write_csv(Laminar_armor, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def plate_armor_download_view(request):
    response = write_csv(Plate_armor, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def small_vessels_canoes_etc_download_view(request):
    response = write_csv(Small_vessels_canoes_etc, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def merchant_ships_pressed_into_service_download_view(request):
    response = write_csv(Merchant_ships_pressed_into_service, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def specialized_military_vessel_download_view(request):
    response = write_csv(Specialized_military_vessel, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def settlements_in_a_defensive_position_download_view(request):
    response = write_csv(Settlements_in_a_defensive_position, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def wooden_palisade_download_view(request):
    response = write_csv(Wooden_palisade, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def earth_rampart_download_view(request):
    response = write_csv(Earth_rampart, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def ditch_download_view(request):
    response = write_csv(Ditch, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def moat_download_view(request):
    response = write_csv(Moat, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def stone_walls_mortared_download_view(request):
    response = write_csv(Stone_walls_mortared, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def stone_walls_non_mortared_download_view(request):
    response = write_csv(Stone_walls_non_mortared, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def fortified_camp_download_view(request):
    response = write_csv(Fortified_camp, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def complex_fortification_download_view(request):
    response = write_csv(Complex_fortification, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def modern_fortification_download_view(request):
    response = write_csv(Modern_fortification, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def chainmail_download_view(request):
    response = write_csv(Chainmail, prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def long_wall_meta_download_view(request):
    response = write_csv(Long_wall, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def copper_meta_download_view(request):
    response = write_csv(Copper, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def bronze_meta_download_view(request):
    response = write_csv(Bronze, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def iron_meta_download_view(request):
    response = write_csv(Iron, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def steel_meta_download_view(request):
    response = write_csv(Steel, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def javelin_meta_download_view(request):
    response = write_csv(Javelin, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def atlatl_meta_download_view(request):
    response = write_csv(Atlatl, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def sling_meta_download_view(request):
    response = write_csv(Sling, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def self_bow_meta_download_view(request):
    response = write_csv(Self_bow, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def composite_bow_meta_download_view(request):
    response = write_csv(Composite_bow, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def crossbow_meta_download_view(request):
    response = write_csv(Crossbow, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def tension_siege_engine_meta_download_view(request):
    response = write_csv(Tension_siege_engine, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def sling_siege_engine_meta_download_view(request):
    response = write_csv(Sling_siege_engine, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def gunpowder_siege_artillery_meta_download_view(request):
    response = write_csv(Gunpowder_siege_artillery, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def handheld_firearm_meta_download_view(request):
    response = write_csv(Handheld_firearm, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def war_club_meta_download_view(request):
    response = write_csv(War_club, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def battle_axe_meta_download_view(request):
    response = write_csv(Battle_axe, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def dagger_meta_download_view(request):
    response = write_csv(Dagger, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def sword_meta_download_view(request):
    response = write_csv(Sword, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def spear_meta_download_view(request):
    response = write_csv(Spear, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def polearm_meta_download_view(request):
    response = write_csv(Polearm, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def dog_meta_download_view(request):
    response = write_csv(Dog, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def donkey_meta_download_view(request):
    response = write_csv(Donkey, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def horse_meta_download_view(request):
    response = write_csv(Horse, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def camel_meta_download_view(request):
    response = write_csv(Camel, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def elephant_meta_download_view(request):
    response = write_csv(Elephant, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def wood_bark_etc_meta_download_view(request):
    response = write_csv(Wood_bark_etc, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def leather_cloth_meta_download_view(request):
    response = write_csv(Leather_cloth, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def shield_meta_download_view(request):
    response = write_csv(Shield, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def helmet_meta_download_view(request):
    response = write_csv(Helmet, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def breastplate_meta_download_view(request):
    response = write_csv(Breastplate, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def limb_protection_meta_download_view(request):
    response = write_csv(Limb_protection, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def scaled_armor_meta_download_view(request):
    response = write_csv(Scaled_armor, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def laminar_armor_meta_download_view(request):
    response = write_csv(Laminar_armor, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def plate_armor_meta_download_view(request):
    response = write_csv(Plate_armor, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def small_vessels_canoes_etc_meta_download_view(request):
    response = write_csv(Small_vessels_canoes_etc, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def merchant_ships_pressed_into_service_meta_download_view(request):
    response = write_csv(Merchant_ships_pressed_into_service, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def specialized_military_vessel_meta_download_view(request):
    response = write_csv(Specialized_military_vessel, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def settlements_in_a_defensive_position_meta_download_view(request):
    response = write_csv(Settlements_in_a_defensive_position, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def wooden_palisade_meta_download_view(request):
    response = write_csv(Wooden_palisade, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def earth_rampart_meta_download_view(request):
    response = write_csv(Earth_rampart, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def ditch_meta_download_view(request):
    response = write_csv(Ditch, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def moat_meta_download_view(request):
    response = write_csv(Moat, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def stone_walls_mortared_meta_download_view(request):
    response = write_csv(Stone_walls_mortared, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def stone_walls_non_mortared_meta_download_view(request):
    response = write_csv(Stone_walls_non_mortared, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def fortified_camp_meta_download_view(request):
    response = write_csv(Fortified_camp, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def complex_fortification_meta_download_view(request):
    response = write_csv(Complex_fortification, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def modern_fortification_meta_download_view(request):
    response = write_csv(Modern_fortification, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def chainmail_meta_download_view(request):
    response = write_csv(Chainmail, "meta", prefix=PREFIX)
    return response


@permission_required("core.view_capital")
def download_csv_all_wf(request):
    # Create a filename
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_data_{current_datetime}.csv"

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
        ]
    )

    # Iterate over each model
    for model in get_models(APP_NAME):
        # Get all rows of data from the model
        for obj in model.objects.all():
            if obj.clean_name() == "long_wall":
                writer.writerow(
                    [
                        "Military Technologies",
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
                    ]
                )
            else:
                writer.writerow(
                    [
                        "Military Technologies",
                        obj.clean_name(),
                        obj.year_from,
                        obj.year_to,
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.show_value(),
                        None,
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                    ]
                )

    return response


@permission_required("core.view_capital")
def download_csv_fortifications(request):
    # Create a filename
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_fortifications_{current_datetime}.csv"

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
    for model in get_models(APP_NAME, subsection=SUBSECTIONS.wf.Fortifications):
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
def download_csv_military_use_of_metals(request):
    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_military_use_of_metals_{current_datetime}.csv"

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
    for model in get_models(APP_NAME, subsection=SUBSECTIONS.wf.MilitaryUseOfMetals):
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
def download_csv_projectiles(request):
    # Create a filename
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_projectiles_{current_datetime}.csv"

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
    for model in get_models(APP_NAME, subsection=SUBSECTIONS.wf.Projectiles):
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
def download_csv_handheld_weapons(request):
    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_handheld_weapons_{current_datetime}.csv"

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
    for model in get_models(APP_NAME, subsection=SUBSECTIONS.wf.HandheldWeapons):
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
def download_csv_animals_used_in_warfare(request):
    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_animals_used_in_warfare_{current_datetime}.csv"

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
    for model in get_models(APP_NAME, subsection=SUBSECTIONS.wf.AnimalsUsedInWarfare):
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
def download_csv_armor(request):
    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_armor_{current_datetime}.csv"

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
    for model in get_models(APP_NAME, subsection=SUBSECTIONS.wf.Armor):
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
def download_csv_naval_technology(request):
    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_naval_technology_{current_datetime}.csv"

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
    for model in get_models(APP_NAME, subsection=SUBSECTIONS.wf.NavalTechnology):
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
