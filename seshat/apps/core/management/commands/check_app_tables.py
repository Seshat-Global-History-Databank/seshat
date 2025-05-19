# your_app/management/commands/check_scv_tables.py

from django.core.management.base import BaseCommand
from django.db import connection

from seshat.apps.core.models import Variablehierarchy, Section


SC_VARIABLES = {'polity_territory': ('RANGE', 'Social Scale', 'None'),
'polity_population': ('RANGE', 'Social Scale', 'None'),
'population_of_the_largest_settlement': ('RANGE', 'Social Scale', 'None'),
'settlement_hierarchy': ('RANGE', 'Hierarchical Complexity', 'None'),
'administrative_level': ('RANGE', 'Hierarchical Complexity', 'None'),
'religious_level': ('RANGE', 'Hierarchical Complexity', 'None'),
'military_level': ('RANGE', 'Hierarchical Complexity', 'None'),
'professional_military_officer': ('A/P/U/~', 'Professions', 'None'),
'professional_soldier': ('A/P/U/~', 'Professions', 'None'),
'professional_priesthood': ('A/P/U/~', 'Professions', 'None'),
'full_time_bureaucrat': ('A/P/U/~', 'Bureaucracy Characteristics', 'None'),
'examination_system': ('A/P/U/~', 'Bureaucracy Characteristics', 'None'),
'merit_promotion': ('A/P/U/~', 'Bureaucracy Characteristics', 'None'),
'specialized_government_building': ('A/P/U/~', 'Bureaucracy Characteristics', 'None'),
'formal_legal_code': ('A/P/U/~', 'Law', 'None'),
'judge': ('A/P/U/~', 'Law', 'None'),
'court': ('A/P/U/~', 'Law', 'None'),
'professional_lawyer': ('A/P/U/~', 'Law', 'None'),
'irrigation_system': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'drinking_water_supply_system': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'market': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'food_storage_site': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'road': ('A/P/U/~', 'Transport Infrastructure', 'None'),
'bridge': ('A/P/U/~', 'Transport Infrastructure', 'None'),
'canal': ('A/P/U/~', 'Transport Infrastructure', 'None'),
'port': ('A/P/U/~', 'Transport Infrastructure', 'None'),
'mines_or_quarry': ('A/P/U/~', 'Special-purpose Sites', 'None'),
'mnemonic_device': ('A/P/U/~', 'Information', 'Writing System'),
'nonwritten_record': ('A/P/U/~', 'Information', 'Writing System'),
'written_record': ('A/P/U/~', 'Information', 'Writing System'),
'script': ('A/P/U/~', 'Information', 'Writing System'),
'non_phonetic_writing': ('A/P/U/~', 'Information', 'Writing System'),
'phonetic_alphabetic_writing': ('A/P/U/~', 'Information', 'Writing System'),
'lists_tables_and_classification': ('A/P/U/~', 'Information', 'Kinds of Written Documents'),
'calendar': ('A/P/U/~', 'Information', 'Kinds of Written Documents'),
'sacred_text': ('A/P/U/~', 'Information', 'Kinds of Written Documents'),
'religious_literature': ('A/P/U/~', 'Information', 'Kinds of Written Documents'),
'practical_literature': ('A/P/U/~', 'Information', 'Kinds of Written Documents'),
'history': ('A/P/U/~', 'Information', 'Kinds of Written Documents'),
'philosophy': ('A/P/U/~', 'Information', 'Kinds of Written Documents'),
'scientific_literature': ('A/P/U/~', 'Information', 'Kinds of Written Documents'),
'fiction': ('A/P/U/~', 'Information', 'Kinds of Written Documents'),
'article': ('A/P/U/~', 'Information', 'Money'),
'token': ('A/P/U/~', 'Information', 'Money'),
'precious_metal': ('A/P/U/~', 'Information', 'Money'),
'foreign_coin': ('A/P/U/~', 'Information', 'Money'),
'indigenous_coin': ('A/P/U/~', 'Information', 'Money'),
'paper_currency': ('A/P/U/~', 'Information', 'Money'),
'courier': ('A/P/U/~', 'Information', 'Postal System'),
'postal_station': ('A/P/U/~', 'Information', 'Postal System'),
'general_postal_service': ('A/P/U/~', 'Information', 'Postal System'),
#'communal_building': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'utilitarian_public_building': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'symbolic_building': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'entertainment_building': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'knowledge_or_information_building': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'other_utilitarian_public_building': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'special_purpose_site': ('A/P/U/~', 'Special-purpose Sites', 'None'),
'ceremonial_site': ('A/P/U/~', 'Special-purpose Sites', 'None'),
'burial_site': ('A/P/U/~', 'Special-purpose Sites', 'None'),
'trading_emporia': ('A/P/U/~', 'Special-purpose Sites', 'None'),
'enclosure': ('A/P/U/~', 'Special-purpose Sites', 'None'),
'length_measurement_system': ('A/P/U/~', 'Information', 'Measurement System'),
'area_measurement_system': ('A/P/U/~', 'Information', 'Measurement System'),
'volume_measurement_system': ('A/P/U/~', 'Information', 'Measurement System'),
'weight_measurement_system': ('A/P/U/~', 'Information', 'Measurement System'),
'time_measurement_system': ('A/P/U/~', 'Information', 'Measurement System'),
'geometrical_measurement_system': ('A/P/U/~', 'Information', 'Measurement System'),
'other_measurement_system': ('A/P/U/~', 'Information', 'Measurement System'),
'debt_and_credit_structure': ('A/P/U/~', 'Information', 'Money'),
'store_of_wealth': ('A/P/U/~', 'Information', 'Money'),
'source_of_support': ('TEXT', 'Professions', 'None'),
'occupational_complexity': ('A/P/U/~', 'Professions', 'None'),
'special_purpose_house': ('A/P/U/~', 'Specialized Buildings: polity owned', 'None'),
'other_special_purpose_site': ('A/P/U/~', 'Special-purpose Sites', 'None'),
'largest_communication_distance': ('RANGE', 'Social Scale', 'None'),
'fastest_individual_communication': ('RANGE', 'Information', 'Postal System')}

WF_VARIABLES = {'long_wall': ('RANGE', 'Fortifications', 'None'),
'copper': ('A/P/U/~', 'Military use of Metals', 'None'),
'bronze': ('A/P/U/~', 'Military use of Metals', 'None'),
'iron': ('A/P/U/~', 'Military use of Metals', 'None'),
'steel': ('A/P/U/~', 'Military use of Metals', 'None'),
'javelin': ('A/P/U/~', 'Projectiles', 'None'),
'atlatl': ('A/P/U/~', 'Projectiles', 'None'),
'sling': ('A/P/U/~', 'Projectiles', 'None'),
'self_bow': ('A/P/U/~', 'Projectiles', 'None'),
'composite_bow': ('A/P/U/~', 'Projectiles', 'None'),
'crossbow': ('A/P/U/~', 'Projectiles', 'None'),
'tension_siege_engine': ('A/P/U/~', 'Projectiles', 'None'),
'sling_siege_engine': ('A/P/U/~', 'Projectiles', 'None'),
'gunpowder_siege_artillery': ('A/P/U/~', 'Projectiles', 'None'),
'handheld_firearm': ('A/P/U/~', 'Projectiles', 'None'),
'war_club': ('A/P/U/~', 'Handheld weapons', 'None'),
'battle_axe': ('A/P/U/~', 'Handheld weapons', 'None'),
'dagger': ('A/P/U/~', 'Handheld weapons', 'None'),
'sword': ('A/P/U/~', 'Handheld weapons', 'None'),
'spear': ('A/P/U/~', 'Handheld weapons', 'None'),
'polearm': ('A/P/U/~', 'Handheld weapons', 'None'),
'dog': ('A/P/U/~', 'Animals used in warfare', 'None'),
'donkey': ('A/P/U/~', 'Animals used in warfare', 'None'),
'horse': ('A/P/U/~', 'Animals used in warfare', 'None'),
'camel': ('A/P/U/~', 'Animals used in warfare', 'None'),
'elephant': ('A/P/U/~', 'Animals used in warfare', 'None'),
'wood_bark_etc': ('A/P/U/~', 'Armor', 'None'),
'leather_cloth': ('A/P/U/~', 'Armor', 'None'),
'shield': ('A/P/U/~', 'Armor', 'None'),
'helmet': ('A/P/U/~', 'Armor', 'None'),
'breastplate': ('A/P/U/~', 'Armor', 'None'),
'limb_protection': ('A/P/U/~', 'Armor', 'None'),
'scaled_armor': ('A/P/U/~', 'Armor', 'None'),
'laminar_armor': ('A/P/U/~', 'Armor', 'None'),
'plate_armor': ('A/P/U/~', 'Armor', 'None'),
'small_vessels_canoes_etc': ('A/P/U/~', 'Naval technology', 'None'),
'merchant_ships_pressed_into_service': ('A/P/U/~', 'Naval technology', 'None'),
'specialized_military_vessel': ('A/P/U/~', 'Naval technology', 'None'),
'settlements_in_a_defensive_position': ('A/P/U/~', 'Fortifications', 'None'),
'wooden_palisade': ('A/P/U/~', 'Fortifications', 'None'),
'earth_rampart': ('A/P/U/~', 'Fortifications', 'None'),
'ditch': ('A/P/U/~', 'Fortifications', 'None'),
'moat': ('A/P/U/~', 'Fortifications', 'None'),
'stone_walls_non_mortared': ('A/P/U/~', 'Fortifications', 'None'),
'stone_walls_mortared': ('A/P/U/~', 'Fortifications', 'None'),
'fortified_camp': ('A/P/U/~', 'Fortifications', 'None'),
'complex_fortification': ('A/P/U/~', 'Fortifications', 'None'),
'modern_fortification': ('A/P/U/~', 'Fortifications', 'None'),
'chainmail': ('A/P/U/~', 'Armor', 'None')}


GENERAL_VARIABLES = {'polity_original_name': ('TEXT', 'Identity and Location', 'None'),
'polity_alternative_name': ('TEXT', 'Identity and Location', 'None'),
'polity_duration': ('RANGE', 'Temporal Bounds', 'None'),
'polity_peak_years': ('RANGE', 'Temporal Bounds', 'None'),
'polity_degree_of_centralization': ('TEXT', 'Political and Cultural Relations', 'None'),
'polity_suprapolity_relations': ('TEXT', 'Political and Cultural Relations', 'None'),
'polity_utm_zone': ('TEXT', 'Identity and Location', 'None'),
'polity_capital': ('TEXT', 'Identity and Location', 'None'),
'polity_language': ('TEXT', 'Language', 'None'),
'polity_linguistic_family': ('TEXT', 'Language', 'None'),
'polity_language_genus': ('TEXT', 'Language', 'None'),
'polity_religion_genus': ('TEXT', 'Religion', 'None'),
'polity_religion_family': ('TEXT', 'Religion', 'None'),
'polity_religion': ('TEXT', 'Religion', 'None'),
'polity_preceding_entity': ('TEXT', 'Political and Cultural Relations', 'None'),
'polity_supracultural_entity': ('TEXT', 'Political and Cultural Relations', 'None'),
'polity_scale_of_supracultural_interaction': ('RANGE', 'Political and Cultural Relations', 'None'),
'polity_alternate_religion_genus': ('TEXT', 'Religion', 'None'),
'polity_alternate_religion_family': ('TEXT', 'Religion', 'None'),
'polity_alternate_religion': ('TEXT', 'Religion', 'None'),
'polity_religious_tradition': ('TEXT', 'Religion', 'None')}


RT_VARIABLES = {'widespread_religion': ('TEXT', 'Religious Demography', 'None'),
'official_religion': ('TEXT', 'Religious Demography', 'None'),
'elites_religion': ('TEXT', 'Religious Demography', 'None'),
#'theo_sync_dif_rel': ('A/P/U/~', 'Religious Demography', 'None'),
#'sync_rel_pra_ind_beli': ('A/P/U/~', 'Religious Demography', 'None'),
'religious_fragmentation': ('A/P/U/~', 'Religious Demography', 'None'),
# 'gov_vio_freq_rel_grp': ('TEXT', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_res_pub_wor': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_res_pub_pros': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_res_conv': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_press_conv': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_res_prop_own_for_rel_grp': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'tax_rel_adh_act_ins': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_obl_rel_grp_ofc_reco': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_res_cons_rel_buil': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_res_rel_edu': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_res_cir_rel_lit': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'gov_dis_rel_grp_occ_fun': ('A/P/U/~', 'Religious Tolerance', 'Government Restrictions'),
# 'soc_vio_freq_rel_grp': ('TEXT', 'Religious Tolerance', 'Societal Restrictions'),
# 'soc_dis_rel_grp_occ_fun': ('A/P/U/~', 'Religious Tolerance', 'Societal Restrictions'),
# 'gov_press_conv_for_aga': ('A/P/U/~', 'Religious Tolerance', 'Societal Restrictions'),
'moralizing_supernatural_punishment_and_reward': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_supernatural_concern_is_primary': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_enforcement_is_certain': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_enforcement_is_broad': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_enforcement_is_targeted': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_enforcement_of_rulers': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_religion_adopted_by_elites': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_religion_adopted_by_commoners': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_enforcement_in_afterlife': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_enforcement_in_this_life': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'moralizing_enforcement_is_agentic': ('A/P/U/~', 'Moralizing Supernatural Punishment and Reward', 'None'),
'human_sacrifice': ('A/P/U/~', 'Human Sacrifice', 'None')}

EC_VARIABLES = {
'lux_precious_metal': ('A/P/U/~', 'Luxury Goods', None),
'luxury_fabrics': ('A/P/U/~', 'Luxury Goods', None),
'luxury_manufactured_goods': ('A/P/U/~', 'Luxury Goods', None),
'luxury_spices_incense_and_dyes': ('A/P/U/~', 'Luxury Goods', None),
'luxury_drink_alcohol': ('A/P/U/~', 'Luxury Goods', None),
'luxury_glass_goods': ('A/P/U/~', 'Luxury Goods', None),
'lux_fine_ceramic_wares': ('A/P/U/~', 'Luxury Goods', None),
'lux_precious_stone': ('A/P/U/~', 'Luxury Goods', None),
'lux_statuary': ('A/P/U/~', 'Luxury Goods', None),
'luxury_food': ('A/P/U/~', 'Luxury Goods', None),
'other_luxury_personal_items': ('A/P/U/~', 'Luxury Goods', None)}



class Command(BaseCommand):
    help = 'Check if all sc_{key} tables exist in the database.'

    def handle(self, *args, **kwargs):


        
        with connection.cursor() as cursor:
            cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname = 'public';")
            existing_tables = {row[0] for row in cursor.fetchall()}

        missing_tables = []

        key_mapper = {
            'luxury_drink_alcohol': 'Luxury Drink/Alcohol'
        }

        all_var_groups = [SC_VARIABLES, WF_VARIABLES, GENERAL_VARIABLES, EC_VARIABLES, RT_VARIABLES, SC_VARIABLES]

        for sect in all_var_groups:
            for key, values in sect.items():
                if key in key_mapper:
                    ggod_key = key_mapper[key]
                elif key.startswith('lux_'):
                    key = key[4:]
                    ggod_key = key.replace("_", ' ').title()
                else:
                    ggod_key = key.replace("_", ' ').title()
                if sect == SC_VARIABLES:
                    table_name = f"sc_{key}"
                elif sect == WF_VARIABLES:
                    table_name = f"wf_{key}"
                elif sect == RT_VARIABLES:
                    table_name = f"rt_{key}"
                elif sect == EC_VARIABLES:
                    table_name = f"ec_{key}"
                elif sect == GENERAL_VARIABLES:
                    table_name = f"general_{key}"
                else:
                    table_name = "Baaaaaaaaaaaaaaaaaaaaaaaaaad"
                    print('Baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdddd')
                print(ggod_key)
                if key == 'precious_metal' and table_name.startswith('ec_'):
                    my_sect = Section.objects.get(name='Luxury Goods')
                    my_v = Variablehierarchy.objects.get(name=ggod_key, section_id=my_sect.id)
                elif key == 'precious_metal' and table_name.startswith('sc_'):
                    my_sect = Section.objects.get(name='Information')
                    my_v = Variablehierarchy.objects.get(name=ggod_key, section_id=my_sect.id)
                else:
                    my_v = Variablehierarchy.objects.get(name=ggod_key)


                if my_v:
                    my_v.data_type = values[0]
                    if values[0] == "A/P/U/~":
                        my_v.data_type_definition = None;# f"{key.replace('_', ' ').title()} must be assigned one of the following values: <br> [Present, Absent, Unknown, Transitional (Absent → Present), or Transitional (Present → Absent)]. <br>These may be optionally tagged as Confident, Inferred, or Suspected. <br>Values can also be marked as Disputed or Uncertain.<br>If the value has a description but lacks proper coding, it will be considered 'Uncoded'." #f"One of the following choices is selected for {my_v}: [Present, Uncoded, Absent, Unknown, Transitional (Absent -> Present), Transitional (Present -> Absent)], potentially augmented with one of the tags [Confident, Inferred, Suspected], Values may also be flagged as Disputed or Uncertain."
                    #my_v.data_unit = values[0]
                    my_v.save()
                    self.stdout.write(self.style.SUCCESS(f"✅✅✅ Found var: {my_v}"))
                else:
                    self.stdout.write(self.style.WARNING(f"\n⚠️ {my_v} oooooooooooooooooooops."))



                if table_name not in existing_tables:
                    self.stdout.write(self.style.ERROR(f"Missing table: {table_name}"))
                    missing_tables.append(table_name)
                else:
                    self.stdout.write(self.style.SUCCESS(f"✅ Found table: {table_name}"))

            if missing_tables:
                self.stdout.write(self.style.WARNING(f"\n⚠️ {len(missing_tables)} missing tables."))
            else:
                self.stdout.write(self.style.SUCCESS(f"\n🎉 All {table_name} exist!"))
