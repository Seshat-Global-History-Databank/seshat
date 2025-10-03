from .models import Polity_territory, Polity_population, Population_of_the_largest_settlement, Settlement_hierarchy, Administrative_level, Religious_level, Military_level, Professional_military_officer, Professional_soldier, Professional_priesthood, Full_time_bureaucrat, Examination_system, Merit_promotion, Specialized_government_building, Formal_legal_code, Judge, Court, Professional_lawyer, Irrigation_system, Drinking_water_supply_system, Market, Food_storage_site, Road, Bridge, Canal, Port, Mines_or_quarry, Mnemonic_device, Nonwritten_record, Written_record, Script, Non_phonetic_writing, Phonetic_alphabetic_writing, Lists_tables_and_classification, Calendar, Sacred_text, Religious_literature, Practical_literature, History, Philosophy, Scientific_literature, Fiction, Article, Token, Precious_metal, Foreign_coin, Indigenous_coin, Paper_currency, Courier, Postal_station, General_postal_service, Communal_building, Utilitarian_public_building, Symbolic_building, Entertainment_building, Knowledge_or_information_building, Other_utilitarian_public_building, Special_purpose_site, Ceremonial_site, Burial_site, Trading_emporia, Enclosure, Length_measurement_system, Area_measurement_system, Volume_measurement_system, Weight_measurement_system, Time_measurement_system, Geometrical_measurement_system, Other_measurement_system, Debt_and_credit_structure, Store_of_wealth, Source_of_support, Occupational_complexity, Special_purpose_house, Other_special_purpose_site, Largest_communication_distance, Fastest_individual_communication

from django.urls import path

from .forms import Polity_territoryForm, Polity_populationForm, Population_of_the_largest_settlementForm, Settlement_hierarchyForm, Administrative_levelForm, Religious_levelForm, Military_levelForm, Professional_military_officerForm, Professional_soldierForm, Professional_priesthoodForm, Full_time_bureaucratForm, Examination_systemForm, Merit_promotionForm, Specialized_government_buildingForm, Formal_legal_codeForm, JudgeForm, CourtForm, Professional_lawyerForm, Irrigation_systemForm, Drinking_water_supply_systemForm, MarketForm, Food_storage_siteForm, RoadForm, BridgeForm, CanalForm, PortForm, Mines_or_quarryForm, Mnemonic_deviceForm, Nonwritten_recordForm, Written_recordForm, ScriptForm, Non_phonetic_writingForm, Phonetic_alphabetic_writingForm, Lists_tables_and_classificationForm, CalendarForm, Sacred_textForm, Religious_literatureForm, Practical_literatureForm, HistoryForm, PhilosophyForm, Scientific_literatureForm, FictionForm, ArticleForm, TokenForm, Precious_metalForm, Foreign_coinForm, Indigenous_coinForm, Paper_currencyForm, CourierForm, Postal_stationForm, General_postal_serviceForm, Communal_buildingForm, Utilitarian_public_buildingForm, Symbolic_buildingForm, Entertainment_buildingForm, Knowledge_or_information_buildingForm, Other_utilitarian_public_buildingForm, Special_purpose_siteForm, Ceremonial_siteForm, Burial_siteForm, Trading_emporiaForm, EnclosureForm, Length_measurement_systemForm, Area_measurement_systemForm, Volume_measurement_systemForm, Weight_measurement_systemForm, Time_measurement_systemForm, Geometrical_measurement_systemForm, Other_measurement_systemForm, Debt_and_credit_structureForm, Store_of_wealthForm, Source_of_supportForm, Occupational_complexityForm, Special_purpose_houseForm, Other_special_purpose_siteForm, Largest_communication_distanceForm, Fastest_individual_communicationForm 

from seshat.apps.general.views import dynamic_create_view, dynamic_update_view,  dynamic_update_view_old, generic_list_view, generic_download, generic_json_download, generic_metadata_download, dynamic_detail_view, confirm_delete_view, delete_object_view

from seshat.apps.core.models import Variablehierarchy, Section

from .var_defs import sc_var_defs


from . import views

model_form_pairs = [
(Polity_territory, Polity_territoryForm, 'polity_territory', 'Polity Territory', 'Social Scale', None),
(Polity_population, Polity_populationForm, 'polity_population', 'Polity Population', 'Social Scale', None),
(Population_of_the_largest_settlement, Population_of_the_largest_settlementForm, 'population_of_the_largest_settlement', 'Population Of The Largest Settlement', 'Social Scale', None),
(Settlement_hierarchy, Settlement_hierarchyForm, 'settlement_hierarchy', 'Settlement Hierarchy', 'Hierarchical Complexity', None),
(Administrative_level, Administrative_levelForm, 'administrative_level', 'Administrative Level', 'Hierarchical Complexity', None),
(Religious_level, Religious_levelForm, 'religious_level', 'Religious Level', 'Hierarchical Complexity', None),
(Military_level, Military_levelForm, 'military_level', 'Military Level', 'Hierarchical Complexity', None),
(Professional_military_officer, Professional_military_officerForm, 'professional_military_officer', 'Professional Military Officer', 'Professions', None),
(Professional_soldier, Professional_soldierForm, 'professional_soldier', 'Professional Soldier', 'Professions', None),
(Professional_priesthood, Professional_priesthoodForm, 'professional_priesthood', 'Professional Priesthood', 'Professions', None),
(Full_time_bureaucrat, Full_time_bureaucratForm, 'full_time_bureaucrat', 'Full Time Bureaucrat', 'Bureaucracy characteristics', None),
(Examination_system, Examination_systemForm, 'examination_system', 'Examination System', 'Bureaucracy characteristics', None),
(Merit_promotion, Merit_promotionForm, 'merit_promotion', 'Merit Promotion', 'Bureaucracy characteristics', None),
(Specialized_government_building, Specialized_government_buildingForm, 'specialized_government_building', 'Specialized Government Building', 'Bureaucracy characteristics', None),
(Formal_legal_code, Formal_legal_codeForm, 'formal_legal_code', 'Formal Legal Code', 'Law', None),
(Judge, JudgeForm, 'judge', 'Judge', 'Law', None),
(Court, CourtForm, 'court', 'Court', 'Law', None),
(Professional_lawyer, Professional_lawyerForm, 'professional_lawyer', 'Professional Lawyer', 'Law', None),
(Irrigation_system, Irrigation_systemForm, 'irrigation_system', 'Irrigation System', 'Specialized Buildings', None),
(Drinking_water_supply_system, Drinking_water_supply_systemForm, 'drinking_water_supply_system', 'Drinking Water Supply System', 'Specialized Buildings', None),
(Market, MarketForm, 'market', 'Market', 'Specialized Buildings', None),
(Food_storage_site, Food_storage_siteForm, 'food_storage_site', 'Food Storage Site', 'Specialized Buildings', None),
(Road, RoadForm, 'road', 'Road', 'Transport infrastructure', None),
(Bridge, BridgeForm, 'bridge', 'Bridge', 'Transport infrastructure', None),
(Canal, CanalForm, 'canal', 'Canal', 'Transport infrastructure', None),
(Port, PortForm, 'port', 'Port', 'Transport infrastructure', None),
(Mines_or_quarry, Mines_or_quarryForm, 'mines_or_quarry', 'Mines Or Quarry', 'Special purpose sites', None),
(Mnemonic_device, Mnemonic_deviceForm, 'mnemonic_device', 'Mnemonic Device', 'Information', 'Writing Systems'),
(Nonwritten_record, Nonwritten_recordForm, 'nonwritten_record', 'Nonwritten Record', 'Information', 'Writing Systems'),
(Written_record, Written_recordForm, 'written_record', 'Written Record', 'Information', 'Writing Systems'),
(Script, ScriptForm, 'script', 'Script', 'Information', 'Writing Systems'),
(Non_phonetic_writing, Non_phonetic_writingForm, 'non_phonetic_writing', 'Non Phonetic Writing', 'Information', 'Writing Systems'),
(Phonetic_alphabetic_writing, Phonetic_alphabetic_writingForm, 'phonetic_alphabetic_writing', 'Phonetic Alphabetic Writing', 'Information', 'Writing Systems'),
(Lists_tables_and_classification, Lists_tables_and_classificationForm, 'lists_tables_and_classification', 'Lists Tables And Classification', 'Information', 'Kinds of Written Documents'),
(Calendar, CalendarForm, 'calendar', 'Calendar', 'Information', 'Kinds of Written Documents'),
(Sacred_text, Sacred_textForm, 'sacred_text', 'Sacred Text', 'Information', 'Kinds of Written Documents'),
(Religious_literature, Religious_literatureForm, 'religious_literature', 'Religious Literature', 'Information', 'Kinds of Written Documents'),
(Practical_literature, Practical_literatureForm, 'practical_literature', 'Practical Literature', 'Information', 'Kinds of Written Documents'),
(History, HistoryForm, 'history', 'History', 'Information', 'Kinds of Written Documents'),
(Philosophy, PhilosophyForm, 'philosophy', 'Philosophy', 'Information', 'Kinds of Written Documents'),
(Scientific_literature, Scientific_literatureForm, 'scientific_literature', 'Scientific Literature', 'Information', 'Kinds of Written Documents'),
(Fiction, FictionForm, 'fiction', 'Fiction', 'Information', 'Kinds of Written Documents'),
(Article, ArticleForm, 'article', 'Article', 'Information', 'Forms of money'),
(Token, TokenForm, 'token', 'Token', 'Information', 'Forms of money'),
(Precious_metal, Precious_metalForm, 'precious_metal', 'Precious Metal', 'Information', 'Forms of money'),
(Foreign_coin, Foreign_coinForm, 'foreign_coin', 'Foreign Coin', 'Information', 'Forms of money'),
(Indigenous_coin, Indigenous_coinForm, 'indigenous_coin', 'Indigenous Coin', 'Information', 'Forms of money'),
(Paper_currency, Paper_currencyForm, 'paper_currency', 'Paper Currency', 'Information', 'Forms of money'),
(Courier, CourierForm, 'courier', 'Courier', 'Information', 'Postal sytems'),
(Postal_station, Postal_stationForm, 'postal_station', 'Postal Station', 'Information', 'Postal sytems'),
(General_postal_service, General_postal_serviceForm, 'general_postal_service', 'General Postal Service', 'Information', 'Postal sytems'),
(Fastest_individual_communication, Fastest_individual_communicationForm, 'fastest_individual_communication', 'Fastest Individual Communication', 'Information', 'Postal sytems'),
(Communal_building, Communal_buildingForm, 'communal_building', 'communal building', "Specialized Buildings: polity owned", None),
(Utilitarian_public_building, Utilitarian_public_buildingForm, 'utilitarian_public_building', 'Utilitarian Public Building', "Specialized Buildings: polity owned", None),
(Symbolic_building, Symbolic_buildingForm, 'symbolic_building', 'Symbolic Building', "Specialized Buildings: polity owned", None),
(Entertainment_building, Entertainment_buildingForm, 'entertainment_building', 'Entertainment Building', "Specialized Buildings: polity owned", None),
(Knowledge_or_information_building, Knowledge_or_information_buildingForm, 'knowledge_or_information_building', 'Knowledge Or Information Building', "Specialized Buildings: polity owned", None),
(Other_utilitarian_public_building, Other_utilitarian_public_buildingForm, 'other_utilitarian_public_building', 'Other Utilitarian Public Building', "Specialized Buildings: polity owned", None),
(Special_purpose_site, Special_purpose_siteForm, 'special_purpose_site',  'Special Purpose Site', "Specialized Buildings: polity owned", None),
(Ceremonial_site, Ceremonial_siteForm, 'ceremonial_site', 'Ceremonial Site', "Specialized Buildings: polity owned", None),
(Burial_site, Burial_siteForm, 'burial_site', 'Burial Site', "Specialized Buildings: polity owned", None),
(Trading_emporia, Trading_emporiaForm, 'trading_emporia', 'Trading Emporia', "Specialized Buildings: polity owned", None),
(Enclosure, EnclosureForm, 'enclosure', 'Enclosure', "Specialized Buildings: polity owned", None),
(Length_measurement_system, Length_measurement_systemForm, 'length_measurement_system',  'Length Measurement System', "Information", "Measurement System"),
(Area_measurement_system, Area_measurement_systemForm, 'area_measurement_system', 'Area Measurement System', "Information", "Measurement System"),
(Volume_measurement_system, Volume_measurement_systemForm, 'volume_measurement_system', 'Volume Measurement System', "Information", "Measurement System"),
(Weight_measurement_system, Weight_measurement_systemForm, 'weight_measurement_system',  'Weight Measurement System', "Information", "Measurement System"),
(Time_measurement_system, Time_measurement_systemForm, 'time_measurement_system', 'Time Measurement System', "Information", "Measurement System"),
(Geometrical_measurement_system, Geometrical_measurement_systemForm, 'geometrical_measurement_system', 'Geometrical Measurement System', "Information", "Measurement System"),
(Other_measurement_system, Other_measurement_systemForm, 'other_measurement_system', 'Other Measurement System', "Information", "Measurement System"),
(Debt_and_credit_structure, Debt_and_credit_structureForm, 'debt_and_credit_structure', 'Debt And Credit Structure', "Information", "Money"),
(Store_of_wealth, Store_of_wealthForm, 'store_of_wealth', 'Store Of Wealth', "Information", "Money"),
(Source_of_support, Source_of_supportForm, 'source_of_support', 'Source Of Support', "Professions", None),
(Occupational_complexity, Occupational_complexityForm, 'occupational_complexity', 'Occupational Complexity', "Professions", None),
(Special_purpose_house, Special_purpose_houseForm, 'special_purpose_house', 'Special Purpose House', "Specialized Buildings: polity owned", None),
(Other_special_purpose_site, Other_special_purpose_siteForm, 'other_special_purpose_site', 'Other Special Purpose Site', 'Special-purpose Sites', None),
(Largest_communication_distance, Largest_communication_distanceForm, 'largest_communication_distance', 'Largest Communication Distance', 'Social Scale', None),
]

model_form_pairs_qugmented = [[a[0], a[1], a[2], a[2], a[3], a[4], a[5], 'sc'] for a in model_form_pairs]


urlpatterns = [
    path('scvars/', views.scvars, name='scvars'),
     path('problematic_sc_data_table/', views.show_problematic_sc_data_table, name='problematic_sc_data_table'),
    path('download-csv-sc-all/', views.download_csv_all_sc,name='download_csv_all_sc'),
    path('download_csv_social_scale/', views.download_csv_social_scale,name='download_csv_social_scale'),
     path('download_csv_professions/', views.download_csv_professions,name='download_csv_professions'),
     path('download_csv_bureaucracy_characteristics/', views.download_csv_bureaucracy_characteristics,name='download_csv_bureaucracy_characteristics'),
     path('download_csv_hierarchical_complexity/', views.download_csv_hierarchical_complexity,name='download_csv_hierarchical_complexity'),
     path('download_csv_law/', views.download_csv_law,name='download_csv_law'),
     path('download_csv_specialized_buildings_polity_owned/', views.download_csv_specialized_buildings_polity_owned,name='download_csv_specialized_buildings_polity_owned'),
     path('download_csv_transport_infrastructure/', views.download_csv_transport_infrastructure,name='download_csv_transport_infrastructure'),
     path('download_csv_special_purpose_sites/', views.download_csv_special_purpose_sites,name='download_csv_special_purpose_sites'),
     path('download_csv_information/', views.download_csv_information,name='download_csv_information'),
]

#############
# Create URL patterns dynamically for each model-class pair: UPDATE
for model_class, form_class, x_name, coded_value, myvar, sec, subsec, db_section in model_form_pairs_qugmented:
    urlpatterns.append(
        path(f'{x_name}/create/', dynamic_create_view, {
            'form_class': form_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': sc_var_defs.get(x_name, f"NO Desc: {x_name}"),
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
            'my_exp': sc_var_defs.get(x_name, f"NO Desc: {x_name}"),
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
            'my_exp': sc_var_defs.get(x_name, f"NO Desc: {x_name}"),
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
            'var_main_desc': sc_var_defs.get(x_name, f"NO Desc: {x_name}"),

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
            'var_main_desc': sc_var_defs[x_name],
        }, name=f'{x_name}-metadownload')
     )











urlpatterns += [
    path('ra/create_outdated/', views.RaCreate.as_view(),
         name="ra-create-outdated"),

    path('ras/', views.RaListView.as_view(), name='ras'),
    path('ras_all_outdated/', views.RaListViewAll.as_view(), name='ras_all-outdated'),
    path('ra/<int:pk>', views.RaDetailView.as_view(),
         name='ra-detail-outdated'),
    path('ra/<int:pk>/update/',
         views.RaUpdate.as_view(), name="ra-update-outdated"),
    path('ra/<int:pk>/delete/',
         views.RaDelete.as_view(), name="ra-delete-outdated"),
    # Download
    path('radownload/', views.ra_download,
         name="ra-download"),
    path('rametadownload/', views.ra_meta_download,
         name="ra-metadownload"),
]
        

urlpatterns += [
    path('polity_territory/create_outdated/', views.Polity_territoryCreate.as_view(),
         name="polity_territory-create-outdated"),

    path('polity_territorys/', views.Polity_territoryListView.as_view(), name='polity_territorys'),
    path('polity_territorys_all_outdated/', views.Polity_territoryListViewAll.as_view(), name='polity_territorys_all-outdated'),
    path('polity_territory/<int:pk>', views.Polity_territoryDetailView.as_view(),
         name='polity_territory-detail-outdated'),
    path('polity_territory/<int:pk>/update/',
         views.Polity_territoryUpdate.as_view(), name="polity_territory-update-outdated"),
    path('polity_territory/<int:pk>/delete/',
         views.Polity_territoryDelete.as_view(), name="polity_territory-delete-outdated"),
    # Download
    path('polity_territorydownload/', views.polity_territory_download,
         name="polity_territory-download"),
    path('polity_territorymetadownload/', views.polity_territory_meta_download,
         name="polity_territory-metadownload"),
]
        

urlpatterns += [
    path('polity_population/create_outdated/', views.Polity_populationCreate.as_view(),
         name="polity_population-create-outdated"),

    path('polity_populations/', views.Polity_populationListView.as_view(), name='polity_populations'),
    path('polity_populations_all_outdated/', views.Polity_populationListViewAll.as_view(), name='polity_populations_all-outdated'),
    path('polity_population/<int:pk>', views.Polity_populationDetailView.as_view(),
         name='polity_population-detail-outdated'),
    path('polity_population/<int:pk>/update/',
         views.Polity_populationUpdate.as_view(), name="polity_population-update-outdated"),
    path('polity_population/<int:pk>/delete/',
         views.Polity_populationDelete.as_view(), name="polity_population-delete-outdated"),
    # Download
    path('polity_populationdownload/', views.polity_population_download,
         name="polity_population-download"),
    path('polity_populationmetadownload/', views.polity_population_meta_download,
         name="polity_population-metadownload"),
]
        

urlpatterns += [
    path('population_of_the_largest_settlement/create_outdated/', views.Population_of_the_largest_settlementCreate.as_view(),
         name="population_of_the_largest_settlement-create-outdated"),

    path('population_of_the_largest_settlements/', views.Population_of_the_largest_settlementListView.as_view(), name='population_of_the_largest_settlements'),
    path('population_of_the_largest_settlements_all_outdated/', views.Population_of_the_largest_settlementListViewAll.as_view(), name='population_of_the_largest_settlements_all-outdated'),
    path('population_of_the_largest_settlement/<int:pk>', views.Population_of_the_largest_settlementDetailView.as_view(),
         name='population_of_the_largest_settlement-detail-outdated'),
    path('population_of_the_largest_settlement/<int:pk>/update/',
         views.Population_of_the_largest_settlementUpdate.as_view(), name="population_of_the_largest_settlement-update-outdated"),
    path('population_of_the_largest_settlement/<int:pk>/delete/',
         views.Population_of_the_largest_settlementDelete.as_view(), name="population_of_the_largest_settlement-delete-outdated"),
    # Download
    path('population_of_the_largest_settlementdownload/', views.population_of_the_largest_settlement_download,
         name="population_of_the_largest_settlement-download"),
    path('population_of_the_largest_settlementmetadownload/', views.population_of_the_largest_settlement_meta_download,
         name="population_of_the_largest_settlement-metadownload"),
]
        

urlpatterns += [
    path('settlement_hierarchy/create_outdated/', views.Settlement_hierarchyCreate.as_view(),
         name="settlement_hierarchy-create-outdated"),

    path('settlement_hierarchys/', views.Settlement_hierarchyListView.as_view(), name='settlement_hierarchys'),
    path('settlement_hierarchys_all_outdated/', views.Settlement_hierarchyListViewAll.as_view(), name='settlement_hierarchys_all-outdated'),
    path('settlement_hierarchy/<int:pk>', views.Settlement_hierarchyDetailView.as_view(),
         name='settlement_hierarchy-detail-outdated'),
    path('settlement_hierarchy/<int:pk>/update/',
         views.Settlement_hierarchyUpdate.as_view(), name="settlement_hierarchy-update-outdated"),
    path('settlement_hierarchy/<int:pk>/delete/',
         views.Settlement_hierarchyDelete.as_view(), name="settlement_hierarchy-delete-outdated"),
    # Download
    path('settlement_hierarchydownload/', views.settlement_hierarchy_download,
         name="settlement_hierarchy-download"),
    path('settlement_hierarchymetadownload/', views.settlement_hierarchy_meta_download,
         name="settlement_hierarchy-metadownload"),
]
        

urlpatterns += [
    path('administrative_level/create_outdated/', views.Administrative_levelCreate.as_view(),
         name="administrative_level-create-outdated"),

    path('administrative_levels/', views.Administrative_levelListView.as_view(), name='administrative_levels'),
    path('administrative_levels_all_outdated/', views.Administrative_levelListViewAll.as_view(), name='administrative_levels_all-outdated'),
    path('administrative_level/<int:pk>', views.Administrative_levelDetailView.as_view(),
         name='administrative_level-detail-outdated'),
    path('administrative_level/<int:pk>/update/',
         views.Administrative_levelUpdate.as_view(), name="administrative_level-update-outdated"),
    path('administrative_level/<int:pk>/delete/',
         views.Administrative_levelDelete.as_view(), name="administrative_level-delete-outdated"),
    # Download
    path('administrative_leveldownload/', views.administrative_level_download,
         name="administrative_level-download"),
    path('administrative_levelmetadownload/', views.administrative_level_meta_download,
         name="administrative_level-metadownload"),
]
        

urlpatterns += [
    path('religious_level/create_outdated/', views.Religious_levelCreate.as_view(),
         name="religious_level-create-outdated"),

    path('religious_levels/', views.Religious_levelListView.as_view(), name='religious_levels'),
    path('religious_levels_all_outdated/', views.Religious_levelListViewAll.as_view(), name='religious_levels_all-outdated'),
    path('religious_level/<int:pk>', views.Religious_levelDetailView.as_view(),
         name='religious_level-detail-outdated'),
    path('religious_level/<int:pk>/update/',
         views.Religious_levelUpdate.as_view(), name="religious_level-update-outdated"),
    path('religious_level/<int:pk>/delete/',
         views.Religious_levelDelete.as_view(), name="religious_level-delete-outdated"),
    # Download
    path('religious_leveldownload/', views.religious_level_download,
         name="religious_level-download"),
    path('religious_levelmetadownload/', views.religious_level_meta_download,
         name="religious_level-metadownload"),
]
        

urlpatterns += [
    path('military_level/create_outdated/', views.Military_levelCreate.as_view(),
         name="military_level-create-outdated"),

    path('military_levels/', views.Military_levelListView.as_view(), name='military_levels'),
    #path('military_levels_all_outdated/', views.Military_levelListViewAll.as_view(), name='military_levels_all-outdated'),
    path('military_level/<int:pk>', views.Military_levelDetailView.as_view(),
         name='military_level-detail-outdated'),
    path('military_level/<int:pk>/update/',
         views.Military_levelUpdate.as_view(), name="military_level-update-outdated"),
    path('military_level/<int:pk>/delete/',
         views.Military_levelDelete.as_view(), name="military_level-delete-outdated"),
    # Download
    path('military_leveldownload/', views.military_level_download,
         name="military_level-download"),
    path('military_levelmetadownload/', views.military_level_meta_download,
         name="military_level-metadownload"),
]
        

urlpatterns += [
    path('professional_military_officer/create_outdated/', views.Professional_military_officerCreate.as_view(),
         name="professional_military_officer-create-outdated"),

    path('professional_military_officers/', views.Professional_military_officerListView.as_view(), name='professional_military_officers'),
    path('professional_military_officers_all_outdated/', views.Professional_military_officerListViewAll.as_view(), name='professional_military_officers_all-outdated'),
    path('professional_military_officer/<int:pk>', views.Professional_military_officerDetailView.as_view(),
         name='professional_military_officer-detail-outdated'),
    path('professional_military_officer/<int:pk>/update/',
         views.Professional_military_officerUpdate.as_view(), name="professional_military_officer-update-outdated"),
    path('professional_military_officer/<int:pk>/delete/',
         views.Professional_military_officerDelete.as_view(), name="professional_military_officer-delete-outdated"),
    # Download
    path('professional_military_officerdownload/', views.professional_military_officer_download,
         name="professional_military_officer-download"),
    path('professional_military_officermetadownload/', views.professional_military_officer_meta_download,
         name="professional_military_officer-metadownload"),
]
        

urlpatterns += [
    path('professional_soldier/create_outdated/', views.Professional_soldierCreate.as_view(),
         name="professional_soldier-create-outdated"),

    path('professional_soldiers/', views.Professional_soldierListView.as_view(), name='professional_soldiers'),
    path('professional_soldiers_all_outdated/', views.Professional_soldierListViewAll.as_view(), name='professional_soldiers_all-outdated'),
    path('professional_soldier/<int:pk>', views.Professional_soldierDetailView.as_view(),
         name='professional_soldier-detail-outdated'),
    path('professional_soldier/<int:pk>/update/',
         views.Professional_soldierUpdate.as_view(), name="professional_soldier-update-outdated"),
    path('professional_soldier/<int:pk>/delete/',
         views.Professional_soldierDelete.as_view(), name="professional_soldier-delete-outdated"),
    # Download
    path('professional_soldierdownload/', views.professional_soldier_download,
         name="professional_soldier-download"),
    path('professional_soldiermetadownload/', views.professional_soldier_meta_download,
         name="professional_soldier-metadownload"),
]
        

urlpatterns += [
    path('professional_priesthood/create_outdated/', views.Professional_priesthoodCreate.as_view(),
         name="professional_priesthood-create-outdated"),

    path('professional_priesthoods/', views.Professional_priesthoodListView.as_view(), name='professional_priesthoods'),
    path('professional_priesthoods_all_outdated/', views.Professional_priesthoodListViewAll.as_view(), name='professional_priesthoods_all-outdated'),
    path('professional_priesthood/<int:pk>', views.Professional_priesthoodDetailView.as_view(),
         name='professional_priesthood-detail-outdated'),
    path('professional_priesthood/<int:pk>/update/',
         views.Professional_priesthoodUpdate.as_view(), name="professional_priesthood-update-outdated"),
    path('professional_priesthood/<int:pk>/delete/',
         views.Professional_priesthoodDelete.as_view(), name="professional_priesthood-delete-outdated"),
    # Download
    path('professional_priesthooddownload/', views.professional_priesthood_download,
         name="professional_priesthood-download"),
    path('professional_priesthoodmetadownload/', views.professional_priesthood_meta_download,
         name="professional_priesthood-metadownload"),
]
        

urlpatterns += [
    path('full_time_bureaucrat/create_outdated/', views.Full_time_bureaucratCreate.as_view(),
         name="full_time_bureaucrat-create-outdated"),

    path('full_time_bureaucrats/', views.Full_time_bureaucratListView.as_view(), name='full_time_bureaucrats'),
    path('full_time_bureaucrats_all_outdated/', views.Full_time_bureaucratListViewAll.as_view(), name='full_time_bureaucrats_all-outdated'),
    path('full_time_bureaucrat/<int:pk>', views.Full_time_bureaucratDetailView.as_view(),
         name='full_time_bureaucrat-detail-outdated'),
    path('full_time_bureaucrat/<int:pk>/update/',
         views.Full_time_bureaucratUpdate.as_view(), name="full_time_bureaucrat-update-outdated"),
    path('full_time_bureaucrat/<int:pk>/delete/',
         views.Full_time_bureaucratDelete.as_view(), name="full_time_bureaucrat-delete-outdated"),
    # Download
    path('full_time_bureaucratdownload/', views.full_time_bureaucrat_download,
         name="full_time_bureaucrat-download"),
    path('full_time_bureaucratmetadownload/', views.full_time_bureaucrat_meta_download,
         name="full_time_bureaucrat-metadownload"),
]
        

urlpatterns += [
    path('examination_system/create_outdated/', views.Examination_systemCreate.as_view(),
         name="examination_system-create-outdated"),

    path('examination_systems/', views.Examination_systemListView.as_view(), name='examination_systems'),
    path('examination_systems_all_outdated/', views.Examination_systemListViewAll.as_view(), name='examination_systems_all-outdated'),
    path('examination_system/<int:pk>', views.Examination_systemDetailView.as_view(),
         name='examination_system-detail-outdated'),
    path('examination_system/<int:pk>/update/',
         views.Examination_systemUpdate.as_view(), name="examination_system-update-outdated"),
    path('examination_system/<int:pk>/delete/',
         views.Examination_systemDelete.as_view(), name="examination_system-delete-outdated"),
    # Download
    path('examination_systemdownload/', views.examination_system_download,
         name="examination_system-download"),
    path('examination_systemmetadownload/', views.examination_system_meta_download,
         name="examination_system-metadownload"),
]
        

urlpatterns += [
    path('merit_promotion/create_outdated/', views.Merit_promotionCreate.as_view(),
         name="merit_promotion-create-outdated"),

    path('merit_promotions/', views.Merit_promotionListView.as_view(), name='merit_promotions'),
    path('merit_promotions_all_outdated/', views.Merit_promotionListViewAll.as_view(), name='merit_promotions_all-outdated'),
    path('merit_promotion/<int:pk>', views.Merit_promotionDetailView.as_view(),
         name='merit_promotion-detail-outdated'),
    path('merit_promotion/<int:pk>/update/',
         views.Merit_promotionUpdate.as_view(), name="merit_promotion-update-outdated"),
    path('merit_promotion/<int:pk>/delete/',
         views.Merit_promotionDelete.as_view(), name="merit_promotion-delete-outdated"),
    # Download
    path('merit_promotiondownload/', views.merit_promotion_download,
         name="merit_promotion-download"),
    path('merit_promotionmetadownload/', views.merit_promotion_meta_download,
         name="merit_promotion-metadownload"),
]
        

urlpatterns += [
    path('specialized_government_building/create_outdated/', views.Specialized_government_buildingCreate.as_view(),
         name="specialized_government_building-create-outdated"),

    path('specialized_government_buildings/', views.Specialized_government_buildingListView.as_view(), name='specialized_government_buildings'),
    path('specialized_government_buildings_all_outdated/', views.Specialized_government_buildingListViewAll.as_view(), name='specialized_government_buildings_all-outdated'),
    path('specialized_government_building/<int:pk>', views.Specialized_government_buildingDetailView.as_view(),
         name='specialized_government_building-detail-outdated'),
    path('specialized_government_building/<int:pk>/update/',
         views.Specialized_government_buildingUpdate.as_view(), name="specialized_government_building-update-outdated"),
    path('specialized_government_building/<int:pk>/delete/',
         views.Specialized_government_buildingDelete.as_view(), name="specialized_government_building-delete-outdated"),
    # Download
    path('specialized_government_buildingdownload/', views.specialized_government_building_download,
         name="specialized_government_building-download"),
    path('specialized_government_buildingmetadownload/', views.specialized_government_building_meta_download,
         name="specialized_government_building-metadownload"),
]
        

urlpatterns += [
    path('formal_legal_code/create_outdated/', views.Formal_legal_codeCreate.as_view(),
         name="formal_legal_code-create-outdated"),

    path('formal_legal_codes/', views.Formal_legal_codeListView.as_view(), name='formal_legal_codes'),
    path('formal_legal_codes_all_outdated/', views.Formal_legal_codeListViewAll.as_view(), name='formal_legal_codes_all-outdated'),
    path('formal_legal_code/<int:pk>', views.Formal_legal_codeDetailView.as_view(),
         name='formal_legal_code-detail-outdated'),
    path('formal_legal_code/<int:pk>/update/',
         views.Formal_legal_codeUpdate.as_view(), name="formal_legal_code-update-outdated"),
    path('formal_legal_code/<int:pk>/delete/',
         views.Formal_legal_codeDelete.as_view(), name="formal_legal_code-delete-outdated"),
    # Download
    path('formal_legal_codedownload/', views.formal_legal_code_download,
         name="formal_legal_code-download"),
    path('formal_legal_codemetadownload/', views.formal_legal_code_meta_download,
         name="formal_legal_code-metadownload"),
]
        

urlpatterns += [
    path('judge/create_outdated/', views.JudgeCreate.as_view(),
         name="judge-create-outdated"),

    path('judges/', views.JudgeListView.as_view(), name='judges'),
    path('judges_all_outdated/', views.JudgeListViewAll.as_view(), name='judges_all-outdated'),
    path('judge/<int:pk>', views.JudgeDetailView.as_view(),
         name='judge-detail-outdated'),
    path('judge/<int:pk>/update/',
         views.JudgeUpdate.as_view(), name="judge-update-outdated"),
    path('judge/<int:pk>/delete/',
         views.JudgeDelete.as_view(), name="judge-delete-outdated"),
    # Download
    path('judgedownload/', views.judge_download,
         name="judge-download"),
    path('judgemetadownload/', views.judge_meta_download,
         name="judge-metadownload"),
]
        

urlpatterns += [
    path('court/create_outdated/', views.CourtCreate.as_view(),
         name="court-create-outdated"),

    path('courts/', views.CourtListView.as_view(), name='courts'),
    path('courts_all_outdated/', views.CourtListViewAll.as_view(), name='courts_all-outdated'),
    path('court/<int:pk>', views.CourtDetailView.as_view(),
         name='court-detail-outdated'),
    path('court/<int:pk>/update/',
         views.CourtUpdate.as_view(), name="court-update-outdated"),
    path('court/<int:pk>/delete/',
         views.CourtDelete.as_view(), name="court-delete-outdated"),
    # Download
    path('courtdownload/', views.court_download,
         name="court-download"),
    path('courtmetadownload/', views.court_meta_download,
         name="court-metadownload"),
]
        

urlpatterns += [
    path('professional_lawyer/create_outdated/', views.Professional_lawyerCreate.as_view(),
         name="professional_lawyer-create-outdated"),

    path('professional_lawyers/', views.Professional_lawyerListView.as_view(), name='professional_lawyers'),
    path('professional_lawyers_all_outdated/', views.Professional_lawyerListViewAll.as_view(), name='professional_lawyers_all-outdated'),
    path('professional_lawyer/<int:pk>', views.Professional_lawyerDetailView.as_view(),
         name='professional_lawyer-detail-outdated'),
    path('professional_lawyer/<int:pk>/update/',
         views.Professional_lawyerUpdate.as_view(), name="professional_lawyer-update-outdated"),
    path('professional_lawyer/<int:pk>/delete/',
         views.Professional_lawyerDelete.as_view(), name="professional_lawyer-delete-outdated"),
    # Download
    path('professional_lawyerdownload/', views.professional_lawyer_download,
         name="professional_lawyer-download"),
    path('professional_lawyermetadownload/', views.professional_lawyer_meta_download,
         name="professional_lawyer-metadownload"),
]
        

urlpatterns += [
    path('irrigation_system/create_outdated/', views.Irrigation_systemCreate.as_view(),
         name="irrigation_system-create-outdated"),

    path('irrigation_systems/', views.Irrigation_systemListView.as_view(), name='irrigation_systems'),
    path('irrigation_systems_all_outdated/', views.Irrigation_systemListViewAll.as_view(), name='irrigation_systems_all-outdated'),
    path('irrigation_system/<int:pk>', views.Irrigation_systemDetailView.as_view(),
         name='irrigation_system-detail-outdated'),
    path('irrigation_system/<int:pk>/update/',
         views.Irrigation_systemUpdate.as_view(), name="irrigation_system-update-outdated"),
    path('irrigation_system/<int:pk>/delete/',
         views.Irrigation_systemDelete.as_view(), name="irrigation_system-delete-outdated"),
    # Download
    path('irrigation_systemdownload/', views.irrigation_system_download,
         name="irrigation_system-download"),
    path('irrigation_systemmetadownload/', views.irrigation_system_meta_download,
         name="irrigation_system-metadownload"),
]
        

urlpatterns += [
    path('drinking_water_supply_system/create_outdated/', views.Drinking_water_supply_systemCreate.as_view(),
         name="drinking_water_supply_system-create-outdated"),

    path('drinking_water_supply_systems/', views.Drinking_water_supply_systemListView.as_view(), name='drinking_water_supply_systems'),
    path('drinking_water_supply_systems_all_outdated/', views.Drinking_water_supply_systemListViewAll.as_view(), name='drinking_water_supply_systems_all-outdated'),
    path('drinking_water_supply_system/<int:pk>', views.Drinking_water_supply_systemDetailView.as_view(),
         name='drinking_water_supply_system-detail-outdated'),
    path('drinking_water_supply_system/<int:pk>/update/',
         views.Drinking_water_supply_systemUpdate.as_view(), name="drinking_water_supply_system-update-outdated"),
    path('drinking_water_supply_system/<int:pk>/delete/',
         views.Drinking_water_supply_systemDelete.as_view(), name="drinking_water_supply_system-delete-outdated"),
    # Download
    path('drinking_water_supply_systemdownload/', views.drinking_water_supply_system_download,
         name="drinking_water_supply_system-download"),
    path('drinking_water_supply_systemmetadownload/', views.drinking_water_supply_system_meta_download,
         name="drinking_water_supply_system-metadownload"),
]
        

urlpatterns += [
    path('market/create_outdated/', views.MarketCreate.as_view(),
         name="market-create-outdated"),

    path('markets/', views.MarketListView.as_view(), name='markets'),
    path('markets_all_outdated/', views.MarketListViewAll.as_view(), name='markets_all-outdated'),
    path('market/<int:pk>', views.MarketDetailView.as_view(),
         name='market-detail-outdated'),
    path('market/<int:pk>/update/',
         views.MarketUpdate.as_view(), name="market-update-outdated"),
    path('market/<int:pk>/delete/',
         views.MarketDelete.as_view(), name="market-delete-outdated"),
    # Download
    path('marketdownload/', views.market_download,
         name="market-download"),
    path('marketmetadownload/', views.market_meta_download,
         name="market-metadownload"),
]
        

urlpatterns += [
    path('food_storage_site/create_outdated/', views.Food_storage_siteCreate.as_view(),
         name="food_storage_site-create-outdated"),

    path('food_storage_sites/', views.Food_storage_siteListView.as_view(), name='food_storage_sites'),
    path('food_storage_sites_all_outdated/', views.Food_storage_siteListViewAll.as_view(), name='food_storage_sites_all-outdated'),
    path('food_storage_site/<int:pk>', views.Food_storage_siteDetailView.as_view(),
         name='food_storage_site-detail-outdated'),
    path('food_storage_site/<int:pk>/update/',
         views.Food_storage_siteUpdate.as_view(), name="food_storage_site-update-outdated"),
    path('food_storage_site/<int:pk>/delete/',
         views.Food_storage_siteDelete.as_view(), name="food_storage_site-delete-outdated"),
    # Download
    path('food_storage_sitedownload/', views.food_storage_site_download,
         name="food_storage_site-download"),
    path('food_storage_sitemetadownload/', views.food_storage_site_meta_download,
         name="food_storage_site-metadownload"),
]
        

urlpatterns += [
    path('road/create_outdated/', views.RoadCreate.as_view(),
         name="road-create-outdated"),

    path('roads/', views.RoadListView.as_view(), name='roads'),
    path('roads_all_outdated/', views.RoadListViewAll.as_view(), name='roads_all-outdated'),
    path('road/<int:pk>', views.RoadDetailView.as_view(),
         name='road-detail-outdated'),
    path('road/<int:pk>/update/',
         views.RoadUpdate.as_view(), name="road-update-outdated"),
    path('road/<int:pk>/delete/',
         views.RoadDelete.as_view(), name="road-delete-outdated"),
    # Download
    path('roaddownload/', views.road_download,
         name="road-download"),
    path('roadmetadownload/', views.road_meta_download,
         name="road-metadownload"),
]
        

urlpatterns += [
    path('bridge/create_outdated/', views.BridgeCreate.as_view(),
         name="bridge-create-outdated"),

    path('bridges/', views.BridgeListView.as_view(), name='bridges'),
    path('bridges_all_outdated/', views.BridgeListViewAll.as_view(), name='bridges_all-outdated'),
    path('bridge/<int:pk>', views.BridgeDetailView.as_view(),
         name='bridge-detail-outdated'),
    path('bridge/<int:pk>/update/',
         views.BridgeUpdate.as_view(), name="bridge-update-outdated"),
    path('bridge/<int:pk>/delete/',
         views.BridgeDelete.as_view(), name="bridge-delete-outdated"),
    # Download
    path('bridgedownload/', views.bridge_download,
         name="bridge-download"),
    path('bridgemetadownload/', views.bridge_meta_download,
         name="bridge-metadownload"),
]
        

urlpatterns += [
    path('canal/create_outdated/', views.CanalCreate.as_view(),
         name="canal-create-outdated"),

    path('canals/', views.CanalListView.as_view(), name='canals'),
    path('canals_all_outdated/', views.CanalListViewAll.as_view(), name='canals_all-outdated'),
    path('canal/<int:pk>', views.CanalDetailView.as_view(),
         name='canal-detail-outdated'),
    path('canal/<int:pk>/update/',
         views.CanalUpdate.as_view(), name="canal-update-outdated"),
    path('canal/<int:pk>/delete/',
         views.CanalDelete.as_view(), name="canal-delete-outdated"),
    # Download
    path('canaldownload/', views.canal_download,
         name="canal-download"),
    path('canalmetadownload/', views.canal_meta_download,
         name="canal-metadownload"),
]
        

urlpatterns += [
    path('port/create_outdated/', views.PortCreate.as_view(),
         name="port-create-outdated"),

    path('ports/', views.PortListView.as_view(), name='ports'),
    path('ports_all_outdated/', views.PortListViewAll.as_view(), name='ports_all-outdated'),
    path('port/<int:pk>', views.PortDetailView.as_view(),
         name='port-detail-outdated'),
    path('port/<int:pk>/update/',
         views.PortUpdate.as_view(), name="port-update-outdated"),
    path('port/<int:pk>/delete/',
         views.PortDelete.as_view(), name="port-delete-outdated"),
    # Download
    path('portdownload/', views.port_download,
         name="port-download"),
    path('portmetadownload/', views.port_meta_download,
         name="port-metadownload"),
]
        

urlpatterns += [
    path('mines_or_quarry/create_outdated/', views.Mines_or_quarryCreate.as_view(),
         name="mines_or_quarry-create-outdated"),

    path('mines_or_quarrys/', views.Mines_or_quarryListView.as_view(), name='mines_or_quarrys'),
    path('mines_or_quarrys_all_outdated/', views.Mines_or_quarryListViewAll.as_view(), name='mines_or_quarrys_all-outdated'),
    path('mines_or_quarry/<int:pk>', views.Mines_or_quarryDetailView.as_view(),
         name='mines_or_quarry-detail-outdated'),
    path('mines_or_quarry/<int:pk>/update/',
         views.Mines_or_quarryUpdate.as_view(), name="mines_or_quarry-update-outdated"),
    path('mines_or_quarry/<int:pk>/delete/',
         views.Mines_or_quarryDelete.as_view(), name="mines_or_quarry-delete-outdated"),
    # Download
    path('mines_or_quarrydownload/', views.mines_or_quarry_download,
         name="mines_or_quarry-download"),
    path('mines_or_quarrymetadownload/', views.mines_or_quarry_meta_download,
         name="mines_or_quarry-metadownload"),
]
        

urlpatterns += [
    path('mnemonic_device/create_outdated/', views.Mnemonic_deviceCreate.as_view(),
         name="mnemonic_device-create-outdated"),

    path('mnemonic_devices/', views.Mnemonic_deviceListView.as_view(), name='mnemonic_devices'),
    path('mnemonic_devices_all_outdated/', views.Mnemonic_deviceListViewAll.as_view(), name='mnemonic_devices_all-outdated'),
    path('mnemonic_device/<int:pk>', views.Mnemonic_deviceDetailView.as_view(),
         name='mnemonic_device-detail-outdated'),
    path('mnemonic_device/<int:pk>/update/',
         views.Mnemonic_deviceUpdate.as_view(), name="mnemonic_device-update-outdated"),
    path('mnemonic_device/<int:pk>/delete/',
         views.Mnemonic_deviceDelete.as_view(), name="mnemonic_device-delete-outdated"),
    # Download
    path('mnemonic_devicedownload/', views.mnemonic_device_download,
         name="mnemonic_device-download"),
    path('mnemonic_devicemetadownload/', views.mnemonic_device_meta_download,
         name="mnemonic_device-metadownload"),
]
        

urlpatterns += [
    path('nonwritten_record/create_outdated/', views.Nonwritten_recordCreate.as_view(),
         name="nonwritten_record-create-outdated"),

    path('nonwritten_records/', views.Nonwritten_recordListView.as_view(), name='nonwritten_records'),
    path('nonwritten_records_all_outdated/', views.Nonwritten_recordListViewAll.as_view(), name='nonwritten_records_all-outdated'),
    path('nonwritten_record/<int:pk>', views.Nonwritten_recordDetailView.as_view(),
         name='nonwritten_record-detail-outdated'),
    path('nonwritten_record/<int:pk>/update/',
         views.Nonwritten_recordUpdate.as_view(), name="nonwritten_record-update-outdated"),
    path('nonwritten_record/<int:pk>/delete/',
         views.Nonwritten_recordDelete.as_view(), name="nonwritten_record-delete-outdated"),
    # Download
    path('nonwritten_recorddownload/', views.nonwritten_record_download,
         name="nonwritten_record-download"),
    path('nonwritten_recordmetadownload/', views.nonwritten_record_meta_download,
         name="nonwritten_record-metadownload"),
]
        

urlpatterns += [
    path('written_record/create_outdated/', views.Written_recordCreate.as_view(),
         name="written_record-create-outdated"),

    path('written_records/', views.Written_recordListView.as_view(), name='written_records'),
    path('written_records_all_outdated/', views.Written_recordListViewAll.as_view(), name='written_records_all-outdated'),
    path('written_record/<int:pk>', views.Written_recordDetailView.as_view(),
         name='written_record-detail-outdated'),
    path('written_record/<int:pk>/update/',
         views.Written_recordUpdate.as_view(), name="written_record-update-outdated"),
    path('written_record/<int:pk>/delete/',
         views.Written_recordDelete.as_view(), name="written_record-delete-outdated"),
    # Download
    path('written_recorddownload/', views.written_record_download,
         name="written_record-download"),
    path('written_recordmetadownload/', views.written_record_meta_download,
         name="written_record-metadownload"),
]
        

urlpatterns += [
    path('script/create_outdated/', views.ScriptCreate.as_view(),
         name="script-create-outdated"),

    path('scripts/', views.ScriptListView.as_view(), name='scripts'),
    path('scripts_all_outdated/', views.ScriptListViewAll.as_view(), name='scripts_all-outdated'),
    path('script/<int:pk>', views.ScriptDetailView.as_view(),
         name='script-detail-outdated'),
    path('script/<int:pk>/update/',
         views.ScriptUpdate.as_view(), name="script-update-outdated"),
    path('script/<int:pk>/delete/',
         views.ScriptDelete.as_view(), name="script-delete-outdated"),
    # Download
    path('scriptdownload/', views.script_download,
         name="script-download"),
    path('scriptmetadownload/', views.script_meta_download,
         name="script-metadownload"),
]
        

urlpatterns += [
    path('non_phonetic_writing/create_outdated/', views.Non_phonetic_writingCreate.as_view(),
         name="non_phonetic_writing-create-outdated"),

    path('non_phonetic_writings/', views.Non_phonetic_writingListView.as_view(), name='non_phonetic_writings'),
    path('non_phonetic_writings_all_outdated/', views.Non_phonetic_writingListViewAll.as_view(), name='non_phonetic_writings_all-outdated'),
    path('non_phonetic_writing/<int:pk>', views.Non_phonetic_writingDetailView.as_view(),
         name='non_phonetic_writing-detail-outdated'),
    path('non_phonetic_writing/<int:pk>/update/',
         views.Non_phonetic_writingUpdate.as_view(), name="non_phonetic_writing-update-outdated"),
    path('non_phonetic_writing/<int:pk>/delete/',
         views.Non_phonetic_writingDelete.as_view(), name="non_phonetic_writing-delete-outdated"),
    # Download
    path('non_phonetic_writingdownload/', views.non_phonetic_writing_download,
         name="non_phonetic_writing-download"),
    path('non_phonetic_writingmetadownload/', views.non_phonetic_writing_meta_download,
         name="non_phonetic_writing-metadownload"),
]
        

urlpatterns += [
    path('phonetic_alphabetic_writing/create_outdated/', views.Phonetic_alphabetic_writingCreate.as_view(),
         name="phonetic_alphabetic_writing-create-outdated"),

    path('phonetic_alphabetic_writings/', views.Phonetic_alphabetic_writingListView.as_view(), name='phonetic_alphabetic_writings'),
    path('phonetic_alphabetic_writings_all_outdated/', views.Phonetic_alphabetic_writingListViewAll.as_view(), name='phonetic_alphabetic_writings_all-outdated'),
    path('phonetic_alphabetic_writing/<int:pk>', views.Phonetic_alphabetic_writingDetailView.as_view(),
         name='phonetic_alphabetic_writing-detail-outdated'),
    path('phonetic_alphabetic_writing/<int:pk>/update/',
         views.Phonetic_alphabetic_writingUpdate.as_view(), name="phonetic_alphabetic_writing-update-outdated"),
    path('phonetic_alphabetic_writing/<int:pk>/delete/',
         views.Phonetic_alphabetic_writingDelete.as_view(), name="phonetic_alphabetic_writing-delete-outdated"),
    # Download
    path('phonetic_alphabetic_writingdownload/', views.phonetic_alphabetic_writing_download,
         name="phonetic_alphabetic_writing-download"),
    path('phonetic_alphabetic_writingmetadownload/', views.phonetic_alphabetic_writing_meta_download,
         name="phonetic_alphabetic_writing-metadownload"),
]
        

urlpatterns += [
    path('lists_tables_and_classification/create_outdated/', views.Lists_tables_and_classificationCreate.as_view(),
         name="lists_tables_and_classification-create-outdated"),

    path('lists_tables_and_classifications/', views.Lists_tables_and_classificationListView.as_view(), name='lists_tables_and_classifications'),
    path('lists_tables_and_classifications_all_outdated/', views.Lists_tables_and_classificationListViewAll.as_view(), name='lists_tables_and_classifications_all-outdated'),
    path('lists_tables_and_classification/<int:pk>', views.Lists_tables_and_classificationDetailView.as_view(),
         name='lists_tables_and_classification-detail-outdated'),
    path('lists_tables_and_classification/<int:pk>/update/',
         views.Lists_tables_and_classificationUpdate.as_view(), name="lists_tables_and_classification-update-outdated"),
    path('lists_tables_and_classification/<int:pk>/delete/',
         views.Lists_tables_and_classificationDelete.as_view(), name="lists_tables_and_classification-delete-outdated"),
    # Download
    path('lists_tables_and_classificationdownload/', views.lists_tables_and_classification_download,
         name="lists_tables_and_classification-download"),
    path('lists_tables_and_classificationmetadownload/', views.lists_tables_and_classification_meta_download,
         name="lists_tables_and_classification-metadownload"),
]
        

urlpatterns += [
    path('calendar/create_outdated/', views.CalendarCreate.as_view(),
         name="calendar-create-outdated"),

    path('calendars/', views.CalendarListView.as_view(), name='calendars'),
    path('calendars_all_outdated/', views.CalendarListViewAll.as_view(), name='calendars_all-outdated'),
    path('calendar/<int:pk>', views.CalendarDetailView.as_view(),
         name='calendar-detail-outdated'),
    path('calendar/<int:pk>/update/',
         views.CalendarUpdate.as_view(), name="calendar-update-outdated"),
    path('calendar/<int:pk>/delete/',
         views.CalendarDelete.as_view(), name="calendar-delete-outdated"),
    # Download
    path('calendardownload/', views.calendar_download,
         name="calendar-download"),
    path('calendarmetadownload/', views.calendar_meta_download,
         name="calendar-metadownload"),
]
        

urlpatterns += [
    path('sacred_text/create_outdated/', views.Sacred_textCreate.as_view(),
         name="sacred_text-create-outdated"),

    path('sacred_texts/', views.Sacred_textListView.as_view(), name='sacred_texts'),
    path('sacred_texts_all_outdated/', views.Sacred_textListViewAll.as_view(), name='sacred_texts_all-outdated'),
    path('sacred_text/<int:pk>', views.Sacred_textDetailView.as_view(),
         name='sacred_text-detail-outdated'),
    path('sacred_text/<int:pk>/update/',
         views.Sacred_textUpdate.as_view(), name="sacred_text-update-outdated"),
    path('sacred_text/<int:pk>/delete/',
         views.Sacred_textDelete.as_view(), name="sacred_text-delete-outdated"),
    # Download
    path('sacred_textdownload/', views.sacred_text_download,
         name="sacred_text-download"),
    path('sacred_textmetadownload/', views.sacred_text_meta_download,
         name="sacred_text-metadownload"),
]
        

urlpatterns += [
    path('religious_literature/create_outdated/', views.Religious_literatureCreate.as_view(),
         name="religious_literature-create-outdated"),

    path('religious_literatures/', views.Religious_literatureListView.as_view(), name='religious_literatures'),
    path('religious_literatures_all_outdated/', views.Religious_literatureListViewAll.as_view(), name='religious_literatures_all-outdated'),
    path('religious_literature/<int:pk>', views.Religious_literatureDetailView.as_view(),
         name='religious_literature-detail-outdated'),
    path('religious_literature/<int:pk>/update/',
         views.Religious_literatureUpdate.as_view(), name="religious_literature-update-outdated"),
    path('religious_literature/<int:pk>/delete/',
         views.Religious_literatureDelete.as_view(), name="religious_literature-delete-outdated"),
    # Download
    path('religious_literaturedownload/', views.religious_literature_download,
         name="religious_literature-download"),
    path('religious_literaturemetadownload/', views.religious_literature_meta_download,
         name="religious_literature-metadownload"),
]
        

urlpatterns += [
    path('practical_literature/create_outdated/', views.Practical_literatureCreate.as_view(),
         name="practical_literature-create-outdated"),

    path('practical_literatures/', views.Practical_literatureListView.as_view(), name='practical_literatures'),
    path('practical_literatures_all_outdated/', views.Practical_literatureListViewAll.as_view(), name='practical_literatures_all-outdated'),
    path('practical_literature/<int:pk>', views.Practical_literatureDetailView.as_view(),
         name='practical_literature-detail-outdated'),
    path('practical_literature/<int:pk>/update/',
         views.Practical_literatureUpdate.as_view(), name="practical_literature-update-outdated"),
    path('practical_literature/<int:pk>/delete/',
         views.Practical_literatureDelete.as_view(), name="practical_literature-delete-outdated"),
    # Download
    path('practical_literaturedownload/', views.practical_literature_download,
         name="practical_literature-download"),
    path('practical_literaturemetadownload/', views.practical_literature_meta_download,
         name="practical_literature-metadownload"),
]
        

urlpatterns += [
    path('history/create_outdated/', views.HistoryCreate.as_view(),
         name="history-create-outdated"),

    path('historys/', views.HistoryListView.as_view(), name='historys'),
    path('historys_all_outdated/', views.HistoryListViewAll.as_view(), name='historys_all-outdated'),
    path('history/<int:pk>', views.HistoryDetailView.as_view(),
         name='history-detail-outdated'),
    path('history/<int:pk>/update/',
         views.HistoryUpdate.as_view(), name="history-update-outdated"),
    path('history/<int:pk>/delete/',
         views.HistoryDelete.as_view(), name="history-delete-outdated"),
    # Download
    path('historydownload/', views.history_download,
         name="history-download"),
    path('historymetadownload/', views.history_meta_download,
         name="history-metadownload"),
]
        

urlpatterns += [
    path('philosophy/create_outdated/', views.PhilosophyCreate.as_view(),
         name="philosophy-create-outdated"),

    path('philosophys/', views.PhilosophyListView.as_view(), name='philosophys'),
    path('philosophys_all_outdated/', views.PhilosophyListViewAll.as_view(), name='philosophys_all-outdated'),
    path('philosophy/<int:pk>', views.PhilosophyDetailView.as_view(),
         name='philosophy-detail-outdated'),
    path('philosophy/<int:pk>/update/',
         views.PhilosophyUpdate.as_view(), name="philosophy-update-outdated"),
    path('philosophy/<int:pk>/delete/',
         views.PhilosophyDelete.as_view(), name="philosophy-delete-outdated"),
    # Download
    path('philosophydownload/', views.philosophy_download,
         name="philosophy-download"),
    path('philosophymetadownload/', views.philosophy_meta_download,
         name="philosophy-metadownload"),
]
        

urlpatterns += [
    path('scientific_literature/create_outdated/', views.Scientific_literatureCreate.as_view(),
         name="scientific_literature-create-outdated"),

    path('scientific_literatures/', views.Scientific_literatureListView.as_view(), name='scientific_literatures'),
    path('scientific_literatures_all_outdated/', views.Scientific_literatureListViewAll.as_view(), name='scientific_literatures_all-outdated'),
    path('scientific_literature/<int:pk>', views.Scientific_literatureDetailView.as_view(),
         name='scientific_literature-detail-outdated'),
    path('scientific_literature/<int:pk>/update/',
         views.Scientific_literatureUpdate.as_view(), name="scientific_literature-update-outdated"),
    path('scientific_literature/<int:pk>/delete/',
         views.Scientific_literatureDelete.as_view(), name="scientific_literature-delete-outdated"),
    # Download
    path('scientific_literaturedownload/', views.scientific_literature_download,
         name="scientific_literature-download"),
    path('scientific_literaturemetadownload/', views.scientific_literature_meta_download,
         name="scientific_literature-metadownload"),
]
        

urlpatterns += [
    path('fiction/create_outdated/', views.FictionCreate.as_view(),
         name="fiction-create-outdated"),

    path('fictions/', views.FictionListView.as_view(), name='fictions'),
    path('fictions_all_outdated/', views.FictionListViewAll.as_view(), name='fictions_all-outdated'),
    path('fiction/<int:pk>', views.FictionDetailView.as_view(),
         name='fiction-detail-outdated'),
    path('fiction/<int:pk>/update/',
         views.FictionUpdate.as_view(), name="fiction-update-outdated"),
    path('fiction/<int:pk>/delete/',
         views.FictionDelete.as_view(), name="fiction-delete-outdated"),
    # Download
    path('fictiondownload/', views.fiction_download,
         name="fiction-download"),
    path('fictionmetadownload/', views.fiction_meta_download,
         name="fiction-metadownload"),
]
        

urlpatterns += [
    path('article/create_outdated/', views.ArticleCreate.as_view(),
         name="article-create-outdated"),

    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('articles_all_outdated/', views.ArticleListViewAll.as_view(), name='articles_all-outdated'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(),
         name='article-detail-outdated'),
    path('article/<int:pk>/update/',
         views.ArticleUpdate.as_view(), name="article-update-outdated"),
    path('article/<int:pk>/delete/',
         views.ArticleDelete.as_view(), name="article-delete-outdated"),
    # Download
    path('articledownload/', views.article_download,
         name="article-download"),
    path('articlemetadownload/', views.article_meta_download,
         name="article-metadownload"),
]
        

urlpatterns += [
    path('token/create_outdated/', views.TokenCreate.as_view(),
         name="token-create-outdated"),

    path('tokens/', views.TokenListView.as_view(), name='tokens'),
    path('tokens_all_outdated/', views.TokenListViewAll.as_view(), name='tokens_all-outdated'),
    path('token/<int:pk>', views.TokenDetailView.as_view(),
         name='token-detail-outdated'),
    path('token/<int:pk>/update/',
         views.TokenUpdate.as_view(), name="token-update-outdated"),
    path('token/<int:pk>/delete/',
         views.TokenDelete.as_view(), name="token-delete-outdated"),
    # Download
    path('tokendownload/', views.token_download,
         name="token-download"),
    path('tokenmetadownload/', views.token_meta_download,
         name="token-metadownload"),
]
        

urlpatterns += [
    path('precious_metal/create_outdated/', views.Precious_metalCreate.as_view(),
         name="precious_metal-create-outdated"),

    path('precious_metals/', views.Precious_metalListView.as_view(), name='precious_metals'),
    path('precious_metals_all_outdated/', views.Precious_metalListViewAll.as_view(), name='precious_metals_all-outdated'),
    path('precious_metal/<int:pk>', views.Precious_metalDetailView.as_view(),
         name='precious_metal-detail-outdated'),
    path('precious_metal/<int:pk>/update/',
         views.Precious_metalUpdate.as_view(), name="precious_metal-update-outdated"),
    path('precious_metal/<int:pk>/delete/',
         views.Precious_metalDelete.as_view(), name="precious_metal-delete-outdated"),
    # Download
    path('precious_metaldownload/', views.precious_metal_download,
         name="precious_metal-download"),
    path('precious_metalmetadownload/', views.precious_metal_meta_download,
         name="precious_metal-metadownload"),
]
        

urlpatterns += [
    path('foreign_coin/create_outdated/', views.Foreign_coinCreate.as_view(),
         name="foreign_coin-create-outdated"),

    path('foreign_coins/', views.Foreign_coinListView.as_view(), name='foreign_coins'),
    path('foreign_coins_all_outdated/', views.Foreign_coinListViewAll.as_view(), name='foreign_coins_all-outdated'),
    path('foreign_coin/<int:pk>', views.Foreign_coinDetailView.as_view(),
         name='foreign_coin-detail-outdated'),
    path('foreign_coin/<int:pk>/update/',
         views.Foreign_coinUpdate.as_view(), name="foreign_coin-update-outdated"),
    path('foreign_coin/<int:pk>/delete/',
         views.Foreign_coinDelete.as_view(), name="foreign_coin-delete-outdated"),
    # Download
    path('foreign_coindownload/', views.foreign_coin_download,
         name="foreign_coin-download"),
    path('foreign_coinmetadownload/', views.foreign_coin_meta_download,
         name="foreign_coin-metadownload"),
]
        

urlpatterns += [
    path('indigenous_coin/create_outdated/', views.Indigenous_coinCreate.as_view(),
         name="indigenous_coin-create-outdated"),

    path('indigenous_coins/', views.Indigenous_coinListView.as_view(), name='indigenous_coins'),
    path('indigenous_coins_all_outdated/', views.Indigenous_coinListViewAll.as_view(), name='indigenous_coins_all-outdated'),
    path('indigenous_coin/<int:pk>', views.Indigenous_coinDetailView.as_view(),
         name='indigenous_coin-detail-outdated'),
    path('indigenous_coin/<int:pk>/update/',
         views.Indigenous_coinUpdate.as_view(), name="indigenous_coin-update-outdated"),
    path('indigenous_coin/<int:pk>/delete/',
         views.Indigenous_coinDelete.as_view(), name="indigenous_coin-delete-outdated"),
    # Download
    path('indigenous_coindownload/', views.indigenous_coin_download,
         name="indigenous_coin-download"),
    path('indigenous_coinmetadownload/', views.indigenous_coin_meta_download,
         name="indigenous_coin-metadownload"),
]
        

urlpatterns += [
    path('paper_currency/create_outdated/', views.Paper_currencyCreate.as_view(),
         name="paper_currency-create-outdated"),

    path('paper_currencys/', views.Paper_currencyListView.as_view(), name='paper_currencys'),
    path('paper_currencys_all_outdated/', views.Paper_currencyListViewAll.as_view(), name='paper_currencys_all-outdated'),
    path('paper_currency/<int:pk>', views.Paper_currencyDetailView.as_view(),
         name='paper_currency-detail-outdated'),
    path('paper_currency/<int:pk>/update/',
         views.Paper_currencyUpdate.as_view(), name="paper_currency-update-outdated"),
    path('paper_currency/<int:pk>/delete/',
         views.Paper_currencyDelete.as_view(), name="paper_currency-delete-outdated"),
    # Download
    path('paper_currencydownload/', views.paper_currency_download,
         name="paper_currency-download"),
    path('paper_currencymetadownload/', views.paper_currency_meta_download,
         name="paper_currency-metadownload"),
]
        

urlpatterns += [
    path('courier/create_outdated/', views.CourierCreate.as_view(),
         name="courier-create-outdated"),

    path('couriers/', views.CourierListView.as_view(), name='couriers'),
    path('couriers_all_outdated/', views.CourierListViewAll.as_view(), name='couriers_all-outdated'),
    path('courier/<int:pk>', views.CourierDetailView.as_view(),
         name='courier-detail-outdated'),
    path('courier/<int:pk>/update/',
         views.CourierUpdate.as_view(), name="courier-update-outdated"),
    path('courier/<int:pk>/delete/',
         views.CourierDelete.as_view(), name="courier-delete-outdated"),
    # Download
    path('courierdownload/', views.courier_download,
         name="courier-download"),
    path('couriermetadownload/', views.courier_meta_download,
         name="courier-metadownload"),
]
        

urlpatterns += [
    path('postal_station/create_outdated/', views.Postal_stationCreate.as_view(),
         name="postal_station-create-outdated"),

    path('postal_stations/', views.Postal_stationListView.as_view(), name='postal_stations'),
    path('postal_stations_all_outdated/', views.Postal_stationListViewAll.as_view(), name='postal_stations_all-outdated'),
    path('postal_station/<int:pk>', views.Postal_stationDetailView.as_view(),
         name='postal_station-detail-outdated'),
    path('postal_station/<int:pk>/update/',
         views.Postal_stationUpdate.as_view(), name="postal_station-update-outdated"),
    path('postal_station/<int:pk>/delete/',
         views.Postal_stationDelete.as_view(), name="postal_station-delete-outdated"),
    # Download
    path('postal_stationdownload/', views.postal_station_download,
         name="postal_station-download"),
    path('postal_stationmetadownload/', views.postal_station_meta_download,
         name="postal_station-metadownload"),
]
        

urlpatterns += [
    path('general_postal_service/create_outdated/', views.General_postal_serviceCreate.as_view(),
         name="general_postal_service-create-outdated"),

    path('general_postal_services/', views.General_postal_serviceListView.as_view(), name='general_postal_services'),
    path('general_postal_services_all_outdated/', views.General_postal_serviceListViewAll.as_view(), name='general_postal_services_all-outdated'),
    path('general_postal_service/<int:pk>', views.General_postal_serviceDetailView.as_view(),
         name='general_postal_service-detail-outdated'),
    path('general_postal_service/<int:pk>/update/',
         views.General_postal_serviceUpdate.as_view(), name="general_postal_service-update-outdated"),
    path('general_postal_service/<int:pk>/delete/',
         views.General_postal_serviceDelete.as_view(), name="general_postal_service-delete-outdated"),
    # Download
    path('general_postal_servicedownload/', views.general_postal_service_download,
         name="general_postal_service-download"),
    path('general_postal_servicemetadownload/', views.general_postal_service_meta_download,
         name="general_postal_service-metadownload"),
]
        
