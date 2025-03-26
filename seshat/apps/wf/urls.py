from .models import Long_wall, Copper, Bronze, Iron, Steel, Javelin, Atlatl, Sling, Self_bow, Composite_bow, Crossbow, Tension_siege_engine, Sling_siege_engine, Gunpowder_siege_artillery, Handheld_firearm, War_club, Battle_axe, Dagger, Sword, Spear, Polearm, Dog, Donkey, Horse, Camel, Elephant, Wood_bark_etc, Leather_cloth, Shield, Helmet, Breastplate, Limb_protection, Scaled_armor, Laminar_armor, Plate_armor, Small_vessels_canoes_etc, Merchant_ships_pressed_into_service, Specialized_military_vessel, Settlements_in_a_defensive_position, Wooden_palisade, Earth_rampart, Ditch, Moat, Stone_walls_non_mortared, Stone_walls_mortared, Fortified_camp, Complex_fortification, Modern_fortification, Chainmail

from .forms import Long_wallForm, CopperForm, BronzeForm, IronForm, SteelForm, JavelinForm, AtlatlForm, SlingForm, Self_bowForm, Composite_bowForm, CrossbowForm, Tension_siege_engineForm, Sling_siege_engineForm, Gunpowder_siege_artilleryForm, Handheld_firearmForm, War_clubForm, Battle_axeForm, DaggerForm, SwordForm, SpearForm, PolearmForm, DogForm, DonkeyForm, HorseForm, CamelForm, ElephantForm, Wood_bark_etcForm, Leather_clothForm, ShieldForm, HelmetForm, BreastplateForm, Limb_protectionForm, Scaled_armorForm, Laminar_armorForm, Plate_armorForm, Small_vessels_canoes_etcForm, Merchant_ships_pressed_into_serviceForm, Specialized_military_vesselForm, Settlements_in_a_defensive_positionForm, Wooden_palisadeForm, Earth_rampartForm, DitchForm, MoatForm, Stone_walls_non_mortaredForm, Stone_walls_mortaredForm, Fortified_campForm, Complex_fortificationForm, Modern_fortificationForm, ChainmailForm



from seshat.apps.general.views import dynamic_create_view, dynamic_update_view, dynamic_update_view_old, generic_list_view, generic_download, generic_json_download, generic_metadata_download, dynamic_detail_view, confirm_delete_view, delete_object_view

from django.urls import path

from .var_defs import wf_var_defs
from . import views

urlpatterns = [
    path('wfvars/', views.wfvars, name='wfvars'),
        path('download-csv-wf-all/', views.download_csv_all_wf,name='download_csv_all_wf'),
     path('problematic_wf_data_table/', views.show_problematic_wf_data_table, name='problematic_wf_data_table'),

]

urlpatterns += [
     path('download_csv_fortifications/', views.download_csv_fortifications,name='download_csv_fortifications'),
     path('download_csv_military_use_of_metals/', views.download_csv_military_use_of_metals,name='download_csv_military_use_of_metals'),
     path('download_csv_projectiles/', views.download_csv_projectiles,name='download_csv_projectiles'),
     path('download_csv_handheld_weapons/', views.download_csv_handheld_weapons,name='download_csv_handheld_weapons'),
     path('download_csv_animals_used_in_warfare/', views.download_csv_animals_used_in_warfare,name='download_csv_animals_used_in_warfare'),
     path('download_csv_armor/', views.download_csv_armor,name='download_csv_armor'),
     path('download_csv_naval_technology/', views.download_csv_naval_technology,name='download_csv_naval_technology'),


]

#############
model_form_pairs = [
     (Long_wall, Long_wallForm, 'long_wall', 'Long Wall', 'Fortifications', None),
     (Copper, CopperForm, 'copper', 'Copper', 'Military use of Metals', None),
     (Bronze, BronzeForm, 'bronze', 'Bronze', 'Military use of Metals', None),
     (Iron, IronForm, 'iron', 'Iron', 'Military use of Metals', None),
     (Steel, SteelForm, 'steel', 'Steel', 'Military use of Metals', None),
     (Javelin, JavelinForm, 'javelin', 'Javelin', 'Projectiles', None),
     (Atlatl, AtlatlForm, 'atlatl', 'Atlatl', 'Projectiles', None),
     (Sling, SlingForm, 'sling', 'Sling', 'Projectiles', None),
     (Self_bow, Self_bowForm, 'self_bow', 'Self Bow', 'Projectiles', None),
     (Composite_bow, Composite_bowForm, 'composite_bow', 'Composite Bow', 'Projectiles', None),
     (Crossbow, CrossbowForm, 'crossbow', 'Crossbow', 'Projectiles', None),
     (Tension_siege_engine, Tension_siege_engineForm, 'tension_siege_engine', 'Tension Siege Engine', 'Projectiles', None),
     (Sling_siege_engine, Sling_siege_engineForm, 'sling_siege_engine', 'Sling Siege Engine', 'Projectiles', None),
     (Gunpowder_siege_artillery, Gunpowder_siege_artilleryForm, 'gunpowder_siege_artillery', 'Gunpowder Siege Artillery', 'Projectiles', None),
     (Handheld_firearm, Handheld_firearmForm, 'handheld_firearm', 'Handheld Firearm', 'Projectiles', None),
     (War_club, War_clubForm, 'war_club', 'War Club', 'Handheld weapons', None),
     (Battle_axe, Battle_axeForm, 'battle_axe', 'Battle Axe', 'Handheld weapons', None),
     (Dagger, DaggerForm, 'dagger', 'Dagger', 'Handheld weapons', None),
     (Sword, SwordForm, 'sword', 'Sword', 'Handheld weapons', None),
     (Spear, SpearForm, 'spear', 'Spear', 'Handheld weapons', None),
     (Polearm, PolearmForm, 'polearm', 'Polearm', 'Handheld weapons', None),
     (Dog, DogForm, 'dog', 'Dog', 'Animals used in warfare', None),
     (Donkey, DonkeyForm, 'donkey', 'Donkey', 'Animals used in warfare', None),
     (Horse, HorseForm, 'horse', 'Horse', 'Animals used in warfare', None),
     (Camel, CamelForm, 'camel', 'Camel', 'Animals used in warfare', None),
     (Elephant, ElephantForm, 'elephant', 'Elephant', 'Animals used in warfare', None),
     (Wood_bark_etc, Wood_bark_etcForm, 'wood_bark_etc', 'Wood Bark Etc', 'Armor', None),
     (Leather_cloth, Leather_clothForm, 'leather_cloth', 'Leather Cloth', 'Armor', None),
     (Shield, ShieldForm, 'shield', 'Shield', 'Armor', None),
     (Helmet, HelmetForm, 'helmet', 'Helmet', 'Armor', None),
     (Breastplate, BreastplateForm, 'breastplate', 'Breastplate', 'Armor', None),
     (Limb_protection, Limb_protectionForm, 'limb_protection', 'Limb Protection', 'Armor', None),
     (Scaled_armor, Scaled_armorForm, 'scaled_armor', 'Scaled Armor', 'Armor', None),
     (Laminar_armor, Laminar_armorForm, 'laminar_armor', 'Laminar Armor', 'Armor', None),
     (Plate_armor, Plate_armorForm, 'plate_armor', 'Plate Armor', 'Armor', None),
     (Small_vessels_canoes_etc, Small_vessels_canoes_etcForm, 'small_vessels_canoes_etc', 'Small Vessels Canoes Etc', 'Naval technology', None),
     (Merchant_ships_pressed_into_service, Merchant_ships_pressed_into_serviceForm, 'merchant_ships_pressed_into_service', 'Merchant Ships Pressed Into Service', 'Naval technology', None),
     (Specialized_military_vessel, Specialized_military_vesselForm, 'specialized_military_vessel', 'Specialized Military Vessel', 'Naval technology', None),
     (Settlements_in_a_defensive_position, Settlements_in_a_defensive_positionForm, 'settlements_in_a_defensive_position', 'Settlements In A Defensive Position', 'Fortifications', None),
     (Wooden_palisade, Wooden_palisadeForm, 'wooden_palisade', 'Wooden Palisade', 'Fortifications', None),
     (Earth_rampart, Earth_rampartForm, 'earth_rampart', 'Earth Rampart', 'Fortifications', None),
     (Ditch, DitchForm, 'ditch', 'Ditch', 'Fortifications', None),
     (Moat, MoatForm, 'moat', 'Moat', 'Fortifications', None),
     (Stone_walls_non_mortared, Stone_walls_non_mortaredForm, 'stone_walls_non_mortared', 'Stone Walls Non Mortared', 'Fortifications', None),
     (Stone_walls_mortared, Stone_walls_mortaredForm, 'stone_walls_mortared', 'Stone Walls Mortared', 'Fortifications', None),
     (Fortified_camp, Fortified_campForm, 'fortified_camp', 'Fortified Camp', 'Fortifications', None),
     (Complex_fortification, Complex_fortificationForm, 'complex_fortification', 'Complex Fortification', 'Fortifications', None),
     (Modern_fortification, Modern_fortificationForm, 'modern_fortification', 'Modern Fortification', 'Fortifications', None),
     (Chainmail, ChainmailForm, 'chainmail', 'Chainmail', 'Armor', None),
]

model_form_pairs_qugmented = [[a[0], a[1], a[2], a[2], a[3], a[4], a[5], 'wf'] for a in model_form_pairs]

# Create URL patterns dynamically for each model-class pair: UPDATE
for model_class, form_class, x_name, coded_value, myvar, sec, subsec, db_section in model_form_pairs_qugmented:
    urlpatterns.append(
        path(f'{x_name}/create/', dynamic_create_view, {
            'form_class': form_class,
            'x_name': x_name,
            'myvar': myvar,            
            'coded_value': coded_value,
            'my_exp': wf_var_defs.get(x_name, f"NO Desc: {x_name}"),
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
        }, name=f'{x_name}-create')
     )
    urlpatterns.append(
        path(f'{x_name}/updatenew/<int:object_id>/', dynamic_update_view, {
            'form_class': form_class,
            'model_class': model_class,
            'x_name': x_name,
            'myvar': myvar,            
            'coded_value': coded_value,
            'my_exp': wf_var_defs.get(x_name, f"NO Desc: {x_name}"),
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
            'delete_url_name': x_name + "-confirm-delete",
        }, name=f'{x_name}-updatenew')
    )
    urlpatterns.append(
        path(f'{x_name}/update_old/<int:object_id>/', dynamic_update_view_old, {
            'form_class': form_class,
            'model_class': model_class,
            'x_name': x_name,
            'myvar': myvar,            
            'coded_value': coded_value,
            'my_exp': wf_var_defs.get(x_name, f"NO Desc: {x_name}"),
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
            'delete_url_name': x_name + "-confirm-delete",
        }, name=f'{x_name}-update')
    )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/', dynamic_detail_view, {
          'model_class': model_class,
          'myvar': x_name,
          'var_section': sec,
          'var_subsection': subsec,
          'db_section': db_section,
          'var_name_display': myvar,
        }, name=f'{x_name}-detail')
     )
    urlpatterns.append(
        path(f'{x_name}s_all/', generic_list_view, {
            'model_class': model_class,
            'var_name': x_name,
            'coded_value': coded_value,
            'var_name_display': myvar,
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
            'var_main_desc': wf_var_defs.get(x_name, f"NO Desc: {x_name}"),

        }, name=f'{x_name}s_all')
     )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/confirm-delete/', confirm_delete_view, {
          'model_class': model_class,
            'var_name': x_name,
        }, name=f'{x_name}-confirm-delete')
     )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/delete/', delete_object_view, {
          'model_class': model_class,
            'var_name': x_name,
        }, name=f'{x_name}-delete')
     )
    urlpatterns.append(
        path(f'{x_name}download/', generic_download, {
            'model_class': model_class,
            'var_name': x_name,
            'x_name': x_name,
            'coded_value': coded_value,
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
        }, name=f'{x_name}-download')
     )
    urlpatterns.append(
        path(f'{x_name}jsondownload/', generic_json_download, {
            'model_class': model_class,
            'var_name': x_name,
            'x_name': x_name,
            'coded_value': coded_value,
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
        }, name=f'{x_name}-json-download')
     )
    urlpatterns.append(
        path(f'{x_name}metadownload/', generic_metadata_download, {
            'var_name': x_name,
            'var_name_display': myvar,
            'var_section': sec,
            'var_subsection': subsec,
            #'db_section': db_section,
            'var_main_desc': wf_var_defs[x_name],
        }, name=f'{x_name}-metadownload')
     )