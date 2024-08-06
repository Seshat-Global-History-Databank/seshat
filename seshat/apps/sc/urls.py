from .models import Communal_building, Utilitarian_public_building, Other_utilitarian_public_building, Symbolic_building, Entertainment_building, Knowledge_or_information_building, Special_purpose_site, Ceremonial_site, Burial_site, Trading_emporia, Enclosure, Length_measurement_system, Area_measurement_system, Volume_measurement_system, Weight_measurement_system, Time_measurement_system, Geometrical_measurement_system, Other_measurement_system, Debt_and_credit_structure, Store_of_wealth, Bridge, Source_of_support, Occupational_complexity, Special_purpose_house, Other_special_purpose_site, Military_level, Largest_communication_distance, Fastest_individual_communication

from django.urls import path

from .forms import Communal_buildingForm, Utilitarian_public_buildingForm, Other_utilitarian_public_buildingForm, Symbolic_buildingForm, Entertainment_buildingForm, Knowledge_or_information_buildingForm, Special_purpose_siteForm, Ceremonial_siteForm, Burial_siteForm, Trading_emporiaForm, EnclosureForm, Length_measurement_systemForm, Area_measurement_systemForm, Volume_measurement_systemForm, Weight_measurement_systemForm, Time_measurement_systemForm, Geometrical_measurement_systemForm, Other_measurement_systemForm, Debt_and_credit_structureForm, Store_of_wealthForm, BridgeForm, Source_of_supportForm, Occupational_complexityForm, Special_purpose_houseForm, Other_special_purpose_siteForm, Military_levelForm, Largest_communication_distanceForm, Fastest_individual_communicationForm


from .views import dynamic_create_view, dynamic_update_view, generic_list_view, generic_download, generic_metadata_download, dynamic_detail_view, confirm_delete_view, delete_object_view
from .var_defs import sc_var_defs


from . import views

model_form_pairs = [
     (Communal_building, Communal_buildingForm, 'communal_building', 'Communal Building', "Specialized Buildings: polity owned", None),
     (Utilitarian_public_building, Utilitarian_public_buildingForm, 'utilitarian_public_building', 'Utilitarian Public Building', "Specialized Buildings: polity owned", None),
     (Other_utilitarian_public_building, Other_utilitarian_public_buildingForm, 'other_utilitarian_public_building', 'Other Utilitarian Public Building', "Specialized Buildings: polity owned", None),
     (Symbolic_building, Symbolic_buildingForm, 'symbolic_building', 'Symbolic Building', "Specialized Buildings: polity owned", None),
     (Entertainment_building, Entertainment_buildingForm, 'entertainment_building', 'Entertainment Building', "Specialized Buildings: polity owned", None),
     (Knowledge_or_information_building, Knowledge_or_information_buildingForm, 'knowledge_or_information_building', 'Knowledge Or Information Building', "Specialized Buildings: polity owned", None),
     (Special_purpose_site, Special_purpose_siteForm, 'special_purpose_site', 'Special Purpose Site', "Specialized Buildings: polity owned", None),
     (Ceremonial_site, Ceremonial_siteForm, 'ceremonial_site', 'Ceremonial Site', "Specialized Buildings: polity owned", None),
     (Burial_site, Burial_siteForm, 'burial_site', 'Burial Site', "Specialized Buildings: polity owned", None),
     (Trading_emporia, Trading_emporiaForm, 'trading_emporia', 'Trading Emporia', "Specialized Buildings: polity owned", None),
     (Enclosure, EnclosureForm, 'enclosure', 'Enclosure', "Specialized Buildings: polity owned", None),
     (Length_measurement_system, Length_measurement_systemForm, 'length_measurement_system', 'Length Measurement System', "Information", "Measurement System"),
     (Area_measurement_system, Area_measurement_systemForm, 'area_measurement_system', 'Area Measurement System', "Information", "Measurement System"),
     (Volume_measurement_system, Volume_measurement_systemForm, 'volume_measurement_system', 'Volume Measurement System', "Information", "Measurement System"),
     (Weight_measurement_system, Weight_measurement_systemForm, 'weight_measurement_system', 'Weight Measurement System', "Information", "Measurement System"),
     (Time_measurement_system, Time_measurement_systemForm, 'time_measurement_system', 'Time Measurement System', "Information", "Measurement System"),
     (Geometrical_measurement_system, Geometrical_measurement_systemForm, 'geometrical_measurement_system', 'Geometrical Measurement System', "Information", "Measurement System"),
     (Other_measurement_system, Other_measurement_systemForm, 'other_measurement_system', 'Other Measurement System', "Information", "Measurement System"),
     (Debt_and_credit_structure, Debt_and_credit_structureForm, 'debt_and_credit_structure', 'Debt And Credit Structure', "Information", "Money"),
     (Store_of_wealth, Store_of_wealthForm, 'store_of_wealth', 'Store Of Wealth', "Information", "Money"),
    (Source_of_support, Source_of_supportForm, 'source_of_support', 'Source Of Support', "Professions", None),
    (Occupational_complexity, Occupational_complexityForm, 'occupational_complexity', 'Occupational Complexity', "Professions", None),
    (Special_purpose_house, Special_purpose_houseForm, 'special_purpose_house', 'Special Purpose House', "Specialized Buildings: polity owned", None),
    (Other_special_purpose_site, Other_special_purpose_siteForm, 'other_special_purpose_site', 'Other Special Purpose Site', "Special-purpose Sites", None),
    (Military_level, Military_levelForm, 'military_level', 'Military Level', "Hierarchical Complexity", None),
     (Largest_communication_distance, Largest_communication_distanceForm, 'largest_communication_distance', 'Largest Communication Distance', "Social Scale", None),
    (Fastest_individual_communication, Fastest_individual_communicationForm, 'fastest_individual_communication', 'Fastest Individual Communication', "Information", "Postal System"),

]


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


# Create URL patterns dynamically for each model-class pair: UPDATE
for model_class, form_class, x_name, myvar, sec, subsec in model_form_pairs:
     urlpatterns.append(
        path(f'{x_name}/update/<int:object_id>/', dynamic_update_view, {
            'form_class': form_class,
            'model_class': model_class,
            'x_name': x_name,
            'myvar': myvar,
            'my_exp': sc_var_defs[x_name],
            'var_section': sec,
            'var_subsection': subsec,
            'delete_url_name': x_name + "-confirm-delete",
        }, name=f'{x_name}-update')
    )
     urlpatterns.append(
        path(f'{x_name}/create/', dynamic_create_view, {
            'form_class': form_class,
            'x_name': x_name,
            'myvar': myvar,
            'my_exp': sc_var_defs[x_name],
            'var_section': sec,
            'var_subsection': subsec,
        }, name=f'{x_name}-create')
     )
     urlpatterns.append(
        path(f'{x_name}s_all/', generic_list_view, {
            'model_class': model_class,
            'var_name': x_name,
            'var_name_display': myvar,
            'var_section': sec,
            'var_subsection': subsec,
            'var_main_desc': sc_var_defs[x_name],
        }, name=f'{x_name}s_all')
     )
     urlpatterns.append(
        path(f'{x_name}download/', generic_download, {
            'model_class': model_class,
            'var_name': x_name,
        }, name=f'{x_name}-download')
     )
     urlpatterns.append(
        path(f'{x_name}metadownload/', generic_metadata_download, {
            'var_name': x_name,
            'var_name_display': myvar,
            'var_section': sec,
            'var_subsection': subsec,
            'var_main_desc': sc_var_defs[x_name],
        }, name=f'{x_name}-metadownload')
     )
     urlpatterns.append(
        path(f'{x_name}/<int:pk>/', dynamic_detail_view, {
          'model_class': model_class,
            'myvar': x_name,
          'var_name_display': myvar,
        }, name=f'{x_name}-detail')
     )
     # urlpatterns.append(
     #    path(f'{x_name}/<int:pk>/delete/', generic_delete_view, {
     #      'model_class': model_class,
     #        'var_name': x_name,
     #    }, name=f'{x_name}-delete')
     # )
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


urlpatterns += [
    path('ra/create/', views.RaCreate.as_view(),
         name="ra-create"),

    path('ras/', views.RaListView.as_view(), name='ras'),
    path('ras_all/', views.RaListViewAll.as_view(), name='ras_all'),
    path('ra/<int:pk>', views.RaDetailView.as_view(),
         name='ra-detail'),
    path('ra/<int:pk>/update/',
         views.RaUpdate.as_view(), name="ra-update"),
    path('ra/<int:pk>/delete/',
         views.RaDelete.as_view(), name="ra-delete"),
    # Download
    path('radownload/', views.ra_download,
         name="ra-download"),
    path('rametadownload/', views.ra_meta_download,
         name="ra-metadownload"),
]
        

urlpatterns += [
    path('polity_territory/create/', views.Polity_territoryCreate.as_view(),
         name="polity_territory-create"),

    path('polity_territorys/', views.Polity_territoryListView.as_view(), name='polity_territorys'),
    path('polity_territorys_all/', views.Polity_territoryListViewAll.as_view(), name='polity_territorys_all'),
    path('polity_territory/<int:pk>', views.Polity_territoryDetailView.as_view(),
         name='polity_territory-detail'),
    path('polity_territory/<int:pk>/update/',
         views.Polity_territoryUpdate.as_view(), name="polity_territory-update"),
    path('polity_territory/<int:pk>/delete/',
         views.Polity_territoryDelete.as_view(), name="polity_territory-delete"),
    # Download
    path('polity_territorydownload/', views.polity_territory_download,
         name="polity_territory-download"),
    path('polity_territorymetadownload/', views.polity_territory_meta_download,
         name="polity_territory-metadownload"),
]
        

urlpatterns += [
    path('polity_population/create/', views.Polity_populationCreate.as_view(),
         name="polity_population-create"),

    path('polity_populations/', views.Polity_populationListView.as_view(), name='polity_populations'),
    path('polity_populations_all/', views.Polity_populationListViewAll.as_view(), name='polity_populations_all'),
    path('polity_population/<int:pk>', views.Polity_populationDetailView.as_view(),
         name='polity_population-detail'),
    path('polity_population/<int:pk>/update/',
         views.Polity_populationUpdate.as_view(), name="polity_population-update"),
    path('polity_population/<int:pk>/delete/',
         views.Polity_populationDelete.as_view(), name="polity_population-delete"),
    # Download
    path('polity_populationdownload/', views.polity_population_download,
         name="polity_population-download"),
    path('polity_populationmetadownload/', views.polity_population_meta_download,
         name="polity_population-metadownload"),
]
        

urlpatterns += [
    path('population_of_the_largest_settlement/create/', views.Population_of_the_largest_settlementCreate.as_view(),
         name="population_of_the_largest_settlement-create"),

    path('population_of_the_largest_settlements/', views.Population_of_the_largest_settlementListView.as_view(), name='population_of_the_largest_settlements'),
    path('population_of_the_largest_settlements_all/', views.Population_of_the_largest_settlementListViewAll.as_view(), name='population_of_the_largest_settlements_all'),
    path('population_of_the_largest_settlement/<int:pk>', views.Population_of_the_largest_settlementDetailView.as_view(),
         name='population_of_the_largest_settlement-detail'),
    path('population_of_the_largest_settlement/<int:pk>/update/',
         views.Population_of_the_largest_settlementUpdate.as_view(), name="population_of_the_largest_settlement-update"),
    path('population_of_the_largest_settlement/<int:pk>/delete/',
         views.Population_of_the_largest_settlementDelete.as_view(), name="population_of_the_largest_settlement-delete"),
    # Download
    path('population_of_the_largest_settlementdownload/', views.population_of_the_largest_settlement_download,
         name="population_of_the_largest_settlement-download"),
    path('population_of_the_largest_settlementmetadownload/', views.population_of_the_largest_settlement_meta_download,
         name="population_of_the_largest_settlement-metadownload"),
]
        

urlpatterns += [
    path('settlement_hierarchy/create/', views.Settlement_hierarchyCreate.as_view(),
         name="settlement_hierarchy-create"),

    path('settlement_hierarchys/', views.Settlement_hierarchyListView.as_view(), name='settlement_hierarchys'),
    path('settlement_hierarchys_all/', views.Settlement_hierarchyListViewAll.as_view(), name='settlement_hierarchys_all'),
    path('settlement_hierarchy/<int:pk>', views.Settlement_hierarchyDetailView.as_view(),
         name='settlement_hierarchy-detail'),
    path('settlement_hierarchy/<int:pk>/update/',
         views.Settlement_hierarchyUpdate.as_view(), name="settlement_hierarchy-update"),
    path('settlement_hierarchy/<int:pk>/delete/',
         views.Settlement_hierarchyDelete.as_view(), name="settlement_hierarchy-delete"),
    # Download
    path('settlement_hierarchydownload/', views.settlement_hierarchy_download,
         name="settlement_hierarchy-download"),
    path('settlement_hierarchymetadownload/', views.settlement_hierarchy_meta_download,
         name="settlement_hierarchy-metadownload"),
]
        

urlpatterns += [
    path('administrative_level/create/', views.Administrative_levelCreate.as_view(),
         name="administrative_level-create"),

    path('administrative_levels/', views.Administrative_levelListView.as_view(), name='administrative_levels'),
    path('administrative_levels_all/', views.Administrative_levelListViewAll.as_view(), name='administrative_levels_all'),
    path('administrative_level/<int:pk>', views.Administrative_levelDetailView.as_view(),
         name='administrative_level-detail'),
    path('administrative_level/<int:pk>/update/',
         views.Administrative_levelUpdate.as_view(), name="administrative_level-update"),
    path('administrative_level/<int:pk>/delete/',
         views.Administrative_levelDelete.as_view(), name="administrative_level-delete"),
    # Download
    path('administrative_leveldownload/', views.administrative_level_download,
         name="administrative_level-download"),
    path('administrative_levelmetadownload/', views.administrative_level_meta_download,
         name="administrative_level-metadownload"),
]
        

urlpatterns += [
    path('religious_level/create/', views.Religious_levelCreate.as_view(),
         name="religious_level-create"),

    path('religious_levels/', views.Religious_levelListView.as_view(), name='religious_levels'),
    path('religious_levels_all/', views.Religious_levelListViewAll.as_view(), name='religious_levels_all'),
    path('religious_level/<int:pk>', views.Religious_levelDetailView.as_view(),
         name='religious_level-detail'),
    path('religious_level/<int:pk>/update/',
         views.Religious_levelUpdate.as_view(), name="religious_level-update"),
    path('religious_level/<int:pk>/delete/',
         views.Religious_levelDelete.as_view(), name="religious_level-delete"),
    # Download
    path('religious_leveldownload/', views.religious_level_download,
         name="religious_level-download"),
    path('religious_levelmetadownload/', views.religious_level_meta_download,
         name="religious_level-metadownload"),
]
        

urlpatterns += [
    path('military_level/create/', views.Military_levelCreate.as_view(),
         name="military_level-create"),

    path('military_levels/', views.Military_levelListView.as_view(), name='military_levels'),
    #path('military_levels_all/', views.Military_levelListViewAll.as_view(), name='military_levels_all'),
    path('military_level/<int:pk>', views.Military_levelDetailView.as_view(),
         name='military_level-detail'),
    path('military_level/<int:pk>/update/',
         views.Military_levelUpdate.as_view(), name="military_level-update"),
    path('military_level/<int:pk>/delete/',
         views.Military_levelDelete.as_view(), name="military_level-delete"),
    # Download
    path('military_leveldownload/', views.military_level_download,
         name="military_level-download"),
    path('military_levelmetadownload/', views.military_level_meta_download,
         name="military_level-metadownload"),
]
        

urlpatterns += [
    path('professional_military_officer/create/', views.Professional_military_officerCreate.as_view(),
         name="professional_military_officer-create"),

    path('professional_military_officers/', views.Professional_military_officerListView.as_view(), name='professional_military_officers'),
    path('professional_military_officers_all/', views.Professional_military_officerListViewAll.as_view(), name='professional_military_officers_all'),
    path('professional_military_officer/<int:pk>', views.Professional_military_officerDetailView.as_view(),
         name='professional_military_officer-detail'),
    path('professional_military_officer/<int:pk>/update/',
         views.Professional_military_officerUpdate.as_view(), name="professional_military_officer-update"),
    path('professional_military_officer/<int:pk>/delete/',
         views.Professional_military_officerDelete.as_view(), name="professional_military_officer-delete"),
    # Download
    path('professional_military_officerdownload/', views.professional_military_officer_download,
         name="professional_military_officer-download"),
    path('professional_military_officermetadownload/', views.professional_military_officer_meta_download,
         name="professional_military_officer-metadownload"),
]
        

urlpatterns += [
    path('professional_soldier/create/', views.Professional_soldierCreate.as_view(),
         name="professional_soldier-create"),

    path('professional_soldiers/', views.Professional_soldierListView.as_view(), name='professional_soldiers'),
    path('professional_soldiers_all/', views.Professional_soldierListViewAll.as_view(), name='professional_soldiers_all'),
    path('professional_soldier/<int:pk>', views.Professional_soldierDetailView.as_view(),
         name='professional_soldier-detail'),
    path('professional_soldier/<int:pk>/update/',
         views.Professional_soldierUpdate.as_view(), name="professional_soldier-update"),
    path('professional_soldier/<int:pk>/delete/',
         views.Professional_soldierDelete.as_view(), name="professional_soldier-delete"),
    # Download
    path('professional_soldierdownload/', views.professional_soldier_download,
         name="professional_soldier-download"),
    path('professional_soldiermetadownload/', views.professional_soldier_meta_download,
         name="professional_soldier-metadownload"),
]
        

urlpatterns += [
    path('professional_priesthood/create/', views.Professional_priesthoodCreate.as_view(),
         name="professional_priesthood-create"),

    path('professional_priesthoods/', views.Professional_priesthoodListView.as_view(), name='professional_priesthoods'),
    path('professional_priesthoods_all/', views.Professional_priesthoodListViewAll.as_view(), name='professional_priesthoods_all'),
    path('professional_priesthood/<int:pk>', views.Professional_priesthoodDetailView.as_view(),
         name='professional_priesthood-detail'),
    path('professional_priesthood/<int:pk>/update/',
         views.Professional_priesthoodUpdate.as_view(), name="professional_priesthood-update"),
    path('professional_priesthood/<int:pk>/delete/',
         views.Professional_priesthoodDelete.as_view(), name="professional_priesthood-delete"),
    # Download
    path('professional_priesthooddownload/', views.professional_priesthood_download,
         name="professional_priesthood-download"),
    path('professional_priesthoodmetadownload/', views.professional_priesthood_meta_download,
         name="professional_priesthood-metadownload"),
]
        

urlpatterns += [
    path('full_time_bureaucrat/create/', views.Full_time_bureaucratCreate.as_view(),
         name="full_time_bureaucrat-create"),

    path('full_time_bureaucrats/', views.Full_time_bureaucratListView.as_view(), name='full_time_bureaucrats'),
    path('full_time_bureaucrats_all/', views.Full_time_bureaucratListViewAll.as_view(), name='full_time_bureaucrats_all'),
    path('full_time_bureaucrat/<int:pk>', views.Full_time_bureaucratDetailView.as_view(),
         name='full_time_bureaucrat-detail'),
    path('full_time_bureaucrat/<int:pk>/update/',
         views.Full_time_bureaucratUpdate.as_view(), name="full_time_bureaucrat-update"),
    path('full_time_bureaucrat/<int:pk>/delete/',
         views.Full_time_bureaucratDelete.as_view(), name="full_time_bureaucrat-delete"),
    # Download
    path('full_time_bureaucratdownload/', views.full_time_bureaucrat_download,
         name="full_time_bureaucrat-download"),
    path('full_time_bureaucratmetadownload/', views.full_time_bureaucrat_meta_download,
         name="full_time_bureaucrat-metadownload"),
]
        

urlpatterns += [
    path('examination_system/create/', views.Examination_systemCreate.as_view(),
         name="examination_system-create"),

    path('examination_systems/', views.Examination_systemListView.as_view(), name='examination_systems'),
    path('examination_systems_all/', views.Examination_systemListViewAll.as_view(), name='examination_systems_all'),
    path('examination_system/<int:pk>', views.Examination_systemDetailView.as_view(),
         name='examination_system-detail'),
    path('examination_system/<int:pk>/update/',
         views.Examination_systemUpdate.as_view(), name="examination_system-update"),
    path('examination_system/<int:pk>/delete/',
         views.Examination_systemDelete.as_view(), name="examination_system-delete"),
    # Download
    path('examination_systemdownload/', views.examination_system_download,
         name="examination_system-download"),
    path('examination_systemmetadownload/', views.examination_system_meta_download,
         name="examination_system-metadownload"),
]
        

urlpatterns += [
    path('merit_promotion/create/', views.Merit_promotionCreate.as_view(),
         name="merit_promotion-create"),

    path('merit_promotions/', views.Merit_promotionListView.as_view(), name='merit_promotions'),
    path('merit_promotions_all/', views.Merit_promotionListViewAll.as_view(), name='merit_promotions_all'),
    path('merit_promotion/<int:pk>', views.Merit_promotionDetailView.as_view(),
         name='merit_promotion-detail'),
    path('merit_promotion/<int:pk>/update/',
         views.Merit_promotionUpdate.as_view(), name="merit_promotion-update"),
    path('merit_promotion/<int:pk>/delete/',
         views.Merit_promotionDelete.as_view(), name="merit_promotion-delete"),
    # Download
    path('merit_promotiondownload/', views.merit_promotion_download,
         name="merit_promotion-download"),
    path('merit_promotionmetadownload/', views.merit_promotion_meta_download,
         name="merit_promotion-metadownload"),
]
        

urlpatterns += [
    path('specialized_government_building/create/', views.Specialized_government_buildingCreate.as_view(),
         name="specialized_government_building-create"),

    path('specialized_government_buildings/', views.Specialized_government_buildingListView.as_view(), name='specialized_government_buildings'),
    path('specialized_government_buildings_all/', views.Specialized_government_buildingListViewAll.as_view(), name='specialized_government_buildings_all'),
    path('specialized_government_building/<int:pk>', views.Specialized_government_buildingDetailView.as_view(),
         name='specialized_government_building-detail'),
    path('specialized_government_building/<int:pk>/update/',
         views.Specialized_government_buildingUpdate.as_view(), name="specialized_government_building-update"),
    path('specialized_government_building/<int:pk>/delete/',
         views.Specialized_government_buildingDelete.as_view(), name="specialized_government_building-delete"),
    # Download
    path('specialized_government_buildingdownload/', views.specialized_government_building_download,
         name="specialized_government_building-download"),
    path('specialized_government_buildingmetadownload/', views.specialized_government_building_meta_download,
         name="specialized_government_building-metadownload"),
]
        

urlpatterns += [
    path('formal_legal_code/create/', views.Formal_legal_codeCreate.as_view(),
         name="formal_legal_code-create"),

    path('formal_legal_codes/', views.Formal_legal_codeListView.as_view(), name='formal_legal_codes'),
    path('formal_legal_codes_all/', views.Formal_legal_codeListViewAll.as_view(), name='formal_legal_codes_all'),
    path('formal_legal_code/<int:pk>', views.Formal_legal_codeDetailView.as_view(),
         name='formal_legal_code-detail'),
    path('formal_legal_code/<int:pk>/update/',
         views.Formal_legal_codeUpdate.as_view(), name="formal_legal_code-update"),
    path('formal_legal_code/<int:pk>/delete/',
         views.Formal_legal_codeDelete.as_view(), name="formal_legal_code-delete"),
    # Download
    path('formal_legal_codedownload/', views.formal_legal_code_download,
         name="formal_legal_code-download"),
    path('formal_legal_codemetadownload/', views.formal_legal_code_meta_download,
         name="formal_legal_code-metadownload"),
]
        

urlpatterns += [
    path('judge/create/', views.JudgeCreate.as_view(),
         name="judge-create"),

    path('judges/', views.JudgeListView.as_view(), name='judges'),
    path('judges_all/', views.JudgeListViewAll.as_view(), name='judges_all'),
    path('judge/<int:pk>', views.JudgeDetailView.as_view(),
         name='judge-detail'),
    path('judge/<int:pk>/update/',
         views.JudgeUpdate.as_view(), name="judge-update"),
    path('judge/<int:pk>/delete/',
         views.JudgeDelete.as_view(), name="judge-delete"),
    # Download
    path('judgedownload/', views.judge_download,
         name="judge-download"),
    path('judgemetadownload/', views.judge_meta_download,
         name="judge-metadownload"),
]
        

urlpatterns += [
    path('court/create/', views.CourtCreate.as_view(),
         name="court-create"),

    path('courts/', views.CourtListView.as_view(), name='courts'),
    path('courts_all/', views.CourtListViewAll.as_view(), name='courts_all'),
    path('court/<int:pk>', views.CourtDetailView.as_view(),
         name='court-detail'),
    path('court/<int:pk>/update/',
         views.CourtUpdate.as_view(), name="court-update"),
    path('court/<int:pk>/delete/',
         views.CourtDelete.as_view(), name="court-delete"),
    # Download
    path('courtdownload/', views.court_download,
         name="court-download"),
    path('courtmetadownload/', views.court_meta_download,
         name="court-metadownload"),
]
        

urlpatterns += [
    path('professional_lawyer/create/', views.Professional_lawyerCreate.as_view(),
         name="professional_lawyer-create"),

    path('professional_lawyers/', views.Professional_lawyerListView.as_view(), name='professional_lawyers'),
    path('professional_lawyers_all/', views.Professional_lawyerListViewAll.as_view(), name='professional_lawyers_all'),
    path('professional_lawyer/<int:pk>', views.Professional_lawyerDetailView.as_view(),
         name='professional_lawyer-detail'),
    path('professional_lawyer/<int:pk>/update/',
         views.Professional_lawyerUpdate.as_view(), name="professional_lawyer-update"),
    path('professional_lawyer/<int:pk>/delete/',
         views.Professional_lawyerDelete.as_view(), name="professional_lawyer-delete"),
    # Download
    path('professional_lawyerdownload/', views.professional_lawyer_download,
         name="professional_lawyer-download"),
    path('professional_lawyermetadownload/', views.professional_lawyer_meta_download,
         name="professional_lawyer-metadownload"),
]
        

urlpatterns += [
    path('irrigation_system/create/', views.Irrigation_systemCreate.as_view(),
         name="irrigation_system-create"),

    path('irrigation_systems/', views.Irrigation_systemListView.as_view(), name='irrigation_systems'),
    path('irrigation_systems_all/', views.Irrigation_systemListViewAll.as_view(), name='irrigation_systems_all'),
    path('irrigation_system/<int:pk>', views.Irrigation_systemDetailView.as_view(),
         name='irrigation_system-detail'),
    path('irrigation_system/<int:pk>/update/',
         views.Irrigation_systemUpdate.as_view(), name="irrigation_system-update"),
    path('irrigation_system/<int:pk>/delete/',
         views.Irrigation_systemDelete.as_view(), name="irrigation_system-delete"),
    # Download
    path('irrigation_systemdownload/', views.irrigation_system_download,
         name="irrigation_system-download"),
    path('irrigation_systemmetadownload/', views.irrigation_system_meta_download,
         name="irrigation_system-metadownload"),
]
        

urlpatterns += [
    path('drinking_water_supply_system/create/', views.Drinking_water_supply_systemCreate.as_view(),
         name="drinking_water_supply_system-create"),

    path('drinking_water_supply_systems/', views.Drinking_water_supply_systemListView.as_view(), name='drinking_water_supply_systems'),
    path('drinking_water_supply_systems_all/', views.Drinking_water_supply_systemListViewAll.as_view(), name='drinking_water_supply_systems_all'),
    path('drinking_water_supply_system/<int:pk>', views.Drinking_water_supply_systemDetailView.as_view(),
         name='drinking_water_supply_system-detail'),
    path('drinking_water_supply_system/<int:pk>/update/',
         views.Drinking_water_supply_systemUpdate.as_view(), name="drinking_water_supply_system-update"),
    path('drinking_water_supply_system/<int:pk>/delete/',
         views.Drinking_water_supply_systemDelete.as_view(), name="drinking_water_supply_system-delete"),
    # Download
    path('drinking_water_supply_systemdownload/', views.drinking_water_supply_system_download,
         name="drinking_water_supply_system-download"),
    path('drinking_water_supply_systemmetadownload/', views.drinking_water_supply_system_meta_download,
         name="drinking_water_supply_system-metadownload"),
]
        

urlpatterns += [
    path('market/create/', views.MarketCreate.as_view(),
         name="market-create"),

    path('markets/', views.MarketListView.as_view(), name='markets'),
    path('markets_all/', views.MarketListViewAll.as_view(), name='markets_all'),
    path('market/<int:pk>', views.MarketDetailView.as_view(),
         name='market-detail'),
    path('market/<int:pk>/update/',
         views.MarketUpdate.as_view(), name="market-update"),
    path('market/<int:pk>/delete/',
         views.MarketDelete.as_view(), name="market-delete"),
    # Download
    path('marketdownload/', views.market_download,
         name="market-download"),
    path('marketmetadownload/', views.market_meta_download,
         name="market-metadownload"),
]
        

urlpatterns += [
    path('food_storage_site/create/', views.Food_storage_siteCreate.as_view(),
         name="food_storage_site-create"),

    path('food_storage_sites/', views.Food_storage_siteListView.as_view(), name='food_storage_sites'),
    path('food_storage_sites_all/', views.Food_storage_siteListViewAll.as_view(), name='food_storage_sites_all'),
    path('food_storage_site/<int:pk>', views.Food_storage_siteDetailView.as_view(),
         name='food_storage_site-detail'),
    path('food_storage_site/<int:pk>/update/',
         views.Food_storage_siteUpdate.as_view(), name="food_storage_site-update"),
    path('food_storage_site/<int:pk>/delete/',
         views.Food_storage_siteDelete.as_view(), name="food_storage_site-delete"),
    # Download
    path('food_storage_sitedownload/', views.food_storage_site_download,
         name="food_storage_site-download"),
    path('food_storage_sitemetadownload/', views.food_storage_site_meta_download,
         name="food_storage_site-metadownload"),
]
        

urlpatterns += [
    path('road/create/', views.RoadCreate.as_view(),
         name="road-create"),

    path('roads/', views.RoadListView.as_view(), name='roads'),
    path('roads_all/', views.RoadListViewAll.as_view(), name='roads_all'),
    path('road/<int:pk>', views.RoadDetailView.as_view(),
         name='road-detail'),
    path('road/<int:pk>/update/',
         views.RoadUpdate.as_view(), name="road-update"),
    path('road/<int:pk>/delete/',
         views.RoadDelete.as_view(), name="road-delete"),
    # Download
    path('roaddownload/', views.road_download,
         name="road-download"),
    path('roadmetadownload/', views.road_meta_download,
         name="road-metadownload"),
]
        

urlpatterns += [
    path('bridge/create/', views.BridgeCreate.as_view(),
         name="bridge-create"),

    path('bridges/', views.BridgeListView.as_view(), name='bridges'),
    path('bridges_all/', views.BridgeListViewAll.as_view(), name='bridges_all'),
    path('bridge/<int:pk>', views.BridgeDetailView.as_view(),
         name='bridge-detail'),
    path('bridge/<int:pk>/update/',
         views.BridgeUpdate.as_view(), name="bridge-update"),
    path('bridge/<int:pk>/delete/',
         views.BridgeDelete.as_view(), name="bridge-delete"),
    # Download
    path('bridgedownload/', views.bridge_download,
         name="bridge-download"),
    path('bridgemetadownload/', views.bridge_meta_download,
         name="bridge-metadownload"),
]
        

urlpatterns += [
    path('canal/create/', views.CanalCreate.as_view(),
         name="canal-create"),

    path('canals/', views.CanalListView.as_view(), name='canals'),
    path('canals_all/', views.CanalListViewAll.as_view(), name='canals_all'),
    path('canal/<int:pk>', views.CanalDetailView.as_view(),
         name='canal-detail'),
    path('canal/<int:pk>/update/',
         views.CanalUpdate.as_view(), name="canal-update"),
    path('canal/<int:pk>/delete/',
         views.CanalDelete.as_view(), name="canal-delete"),
    # Download
    path('canaldownload/', views.canal_download,
         name="canal-download"),
    path('canalmetadownload/', views.canal_meta_download,
         name="canal-metadownload"),
]
        

urlpatterns += [
    path('port/create/', views.PortCreate.as_view(),
         name="port-create"),

    path('ports/', views.PortListView.as_view(), name='ports'),
    path('ports_all/', views.PortListViewAll.as_view(), name='ports_all'),
    path('port/<int:pk>', views.PortDetailView.as_view(),
         name='port-detail'),
    path('port/<int:pk>/update/',
         views.PortUpdate.as_view(), name="port-update"),
    path('port/<int:pk>/delete/',
         views.PortDelete.as_view(), name="port-delete"),
    # Download
    path('portdownload/', views.port_download,
         name="port-download"),
    path('portmetadownload/', views.port_meta_download,
         name="port-metadownload"),
]
        

urlpatterns += [
    path('mines_or_quarry/create/', views.Mines_or_quarryCreate.as_view(),
         name="mines_or_quarry-create"),

    path('mines_or_quarrys/', views.Mines_or_quarryListView.as_view(), name='mines_or_quarrys'),
    path('mines_or_quarrys_all/', views.Mines_or_quarryListViewAll.as_view(), name='mines_or_quarrys_all'),
    path('mines_or_quarry/<int:pk>', views.Mines_or_quarryDetailView.as_view(),
         name='mines_or_quarry-detail'),
    path('mines_or_quarry/<int:pk>/update/',
         views.Mines_or_quarryUpdate.as_view(), name="mines_or_quarry-update"),
    path('mines_or_quarry/<int:pk>/delete/',
         views.Mines_or_quarryDelete.as_view(), name="mines_or_quarry-delete"),
    # Download
    path('mines_or_quarrydownload/', views.mines_or_quarry_download,
         name="mines_or_quarry-download"),
    path('mines_or_quarrymetadownload/', views.mines_or_quarry_meta_download,
         name="mines_or_quarry-metadownload"),
]
        

urlpatterns += [
    path('mnemonic_device/create/', views.Mnemonic_deviceCreate.as_view(),
         name="mnemonic_device-create"),

    path('mnemonic_devices/', views.Mnemonic_deviceListView.as_view(), name='mnemonic_devices'),
    path('mnemonic_devices_all/', views.Mnemonic_deviceListViewAll.as_view(), name='mnemonic_devices_all'),
    path('mnemonic_device/<int:pk>', views.Mnemonic_deviceDetailView.as_view(),
         name='mnemonic_device-detail'),
    path('mnemonic_device/<int:pk>/update/',
         views.Mnemonic_deviceUpdate.as_view(), name="mnemonic_device-update"),
    path('mnemonic_device/<int:pk>/delete/',
         views.Mnemonic_deviceDelete.as_view(), name="mnemonic_device-delete"),
    # Download
    path('mnemonic_devicedownload/', views.mnemonic_device_download,
         name="mnemonic_device-download"),
    path('mnemonic_devicemetadownload/', views.mnemonic_device_meta_download,
         name="mnemonic_device-metadownload"),
]
        

urlpatterns += [
    path('nonwritten_record/create/', views.Nonwritten_recordCreate.as_view(),
         name="nonwritten_record-create"),

    path('nonwritten_records/', views.Nonwritten_recordListView.as_view(), name='nonwritten_records'),
    path('nonwritten_records_all/', views.Nonwritten_recordListViewAll.as_view(), name='nonwritten_records_all'),
    path('nonwritten_record/<int:pk>', views.Nonwritten_recordDetailView.as_view(),
         name='nonwritten_record-detail'),
    path('nonwritten_record/<int:pk>/update/',
         views.Nonwritten_recordUpdate.as_view(), name="nonwritten_record-update"),
    path('nonwritten_record/<int:pk>/delete/',
         views.Nonwritten_recordDelete.as_view(), name="nonwritten_record-delete"),
    # Download
    path('nonwritten_recorddownload/', views.nonwritten_record_download,
         name="nonwritten_record-download"),
    path('nonwritten_recordmetadownload/', views.nonwritten_record_meta_download,
         name="nonwritten_record-metadownload"),
]
        

urlpatterns += [
    path('written_record/create/', views.Written_recordCreate.as_view(),
         name="written_record-create"),

    path('written_records/', views.Written_recordListView.as_view(), name='written_records'),
    path('written_records_all/', views.Written_recordListViewAll.as_view(), name='written_records_all'),
    path('written_record/<int:pk>', views.Written_recordDetailView.as_view(),
         name='written_record-detail'),
    path('written_record/<int:pk>/update/',
         views.Written_recordUpdate.as_view(), name="written_record-update"),
    path('written_record/<int:pk>/delete/',
         views.Written_recordDelete.as_view(), name="written_record-delete"),
    # Download
    path('written_recorddownload/', views.written_record_download,
         name="written_record-download"),
    path('written_recordmetadownload/', views.written_record_meta_download,
         name="written_record-metadownload"),
]
        

urlpatterns += [
    path('script/create/', views.ScriptCreate.as_view(),
         name="script-create"),

    path('scripts/', views.ScriptListView.as_view(), name='scripts'),
    path('scripts_all/', views.ScriptListViewAll.as_view(), name='scripts_all'),
    path('script/<int:pk>', views.ScriptDetailView.as_view(),
         name='script-detail'),
    path('script/<int:pk>/update/',
         views.ScriptUpdate.as_view(), name="script-update"),
    path('script/<int:pk>/delete/',
         views.ScriptDelete.as_view(), name="script-delete"),
    # Download
    path('scriptdownload/', views.script_download,
         name="script-download"),
    path('scriptmetadownload/', views.script_meta_download,
         name="script-metadownload"),
]
        

urlpatterns += [
    path('non_phonetic_writing/create/', views.Non_phonetic_writingCreate.as_view(),
         name="non_phonetic_writing-create"),

    path('non_phonetic_writings/', views.Non_phonetic_writingListView.as_view(), name='non_phonetic_writings'),
    path('non_phonetic_writings_all/', views.Non_phonetic_writingListViewAll.as_view(), name='non_phonetic_writings_all'),
    path('non_phonetic_writing/<int:pk>', views.Non_phonetic_writingDetailView.as_view(),
         name='non_phonetic_writing-detail'),
    path('non_phonetic_writing/<int:pk>/update/',
         views.Non_phonetic_writingUpdate.as_view(), name="non_phonetic_writing-update"),
    path('non_phonetic_writing/<int:pk>/delete/',
         views.Non_phonetic_writingDelete.as_view(), name="non_phonetic_writing-delete"),
    # Download
    path('non_phonetic_writingdownload/', views.non_phonetic_writing_download,
         name="non_phonetic_writing-download"),
    path('non_phonetic_writingmetadownload/', views.non_phonetic_writing_meta_download,
         name="non_phonetic_writing-metadownload"),
]
        

urlpatterns += [
    path('phonetic_alphabetic_writing/create/', views.Phonetic_alphabetic_writingCreate.as_view(),
         name="phonetic_alphabetic_writing-create"),

    path('phonetic_alphabetic_writings/', views.Phonetic_alphabetic_writingListView.as_view(), name='phonetic_alphabetic_writings'),
    path('phonetic_alphabetic_writings_all/', views.Phonetic_alphabetic_writingListViewAll.as_view(), name='phonetic_alphabetic_writings_all'),
    path('phonetic_alphabetic_writing/<int:pk>', views.Phonetic_alphabetic_writingDetailView.as_view(),
         name='phonetic_alphabetic_writing-detail'),
    path('phonetic_alphabetic_writing/<int:pk>/update/',
         views.Phonetic_alphabetic_writingUpdate.as_view(), name="phonetic_alphabetic_writing-update"),
    path('phonetic_alphabetic_writing/<int:pk>/delete/',
         views.Phonetic_alphabetic_writingDelete.as_view(), name="phonetic_alphabetic_writing-delete"),
    # Download
    path('phonetic_alphabetic_writingdownload/', views.phonetic_alphabetic_writing_download,
         name="phonetic_alphabetic_writing-download"),
    path('phonetic_alphabetic_writingmetadownload/', views.phonetic_alphabetic_writing_meta_download,
         name="phonetic_alphabetic_writing-metadownload"),
]
        

urlpatterns += [
    path('lists_tables_and_classification/create/', views.Lists_tables_and_classificationCreate.as_view(),
         name="lists_tables_and_classification-create"),

    path('lists_tables_and_classifications/', views.Lists_tables_and_classificationListView.as_view(), name='lists_tables_and_classifications'),
    path('lists_tables_and_classifications_all/', views.Lists_tables_and_classificationListViewAll.as_view(), name='lists_tables_and_classifications_all'),
    path('lists_tables_and_classification/<int:pk>', views.Lists_tables_and_classificationDetailView.as_view(),
         name='lists_tables_and_classification-detail'),
    path('lists_tables_and_classification/<int:pk>/update/',
         views.Lists_tables_and_classificationUpdate.as_view(), name="lists_tables_and_classification-update"),
    path('lists_tables_and_classification/<int:pk>/delete/',
         views.Lists_tables_and_classificationDelete.as_view(), name="lists_tables_and_classification-delete"),
    # Download
    path('lists_tables_and_classificationdownload/', views.lists_tables_and_classification_download,
         name="lists_tables_and_classification-download"),
    path('lists_tables_and_classificationmetadownload/', views.lists_tables_and_classification_meta_download,
         name="lists_tables_and_classification-metadownload"),
]
        

urlpatterns += [
    path('calendar/create/', views.CalendarCreate.as_view(),
         name="calendar-create"),

    path('calendars/', views.CalendarListView.as_view(), name='calendars'),
    path('calendars_all/', views.CalendarListViewAll.as_view(), name='calendars_all'),
    path('calendar/<int:pk>', views.CalendarDetailView.as_view(),
         name='calendar-detail'),
    path('calendar/<int:pk>/update/',
         views.CalendarUpdate.as_view(), name="calendar-update"),
    path('calendar/<int:pk>/delete/',
         views.CalendarDelete.as_view(), name="calendar-delete"),
    # Download
    path('calendardownload/', views.calendar_download,
         name="calendar-download"),
    path('calendarmetadownload/', views.calendar_meta_download,
         name="calendar-metadownload"),
]
        

urlpatterns += [
    path('sacred_text/create/', views.Sacred_textCreate.as_view(),
         name="sacred_text-create"),

    path('sacred_texts/', views.Sacred_textListView.as_view(), name='sacred_texts'),
    path('sacred_texts_all/', views.Sacred_textListViewAll.as_view(), name='sacred_texts_all'),
    path('sacred_text/<int:pk>', views.Sacred_textDetailView.as_view(),
         name='sacred_text-detail'),
    path('sacred_text/<int:pk>/update/',
         views.Sacred_textUpdate.as_view(), name="sacred_text-update"),
    path('sacred_text/<int:pk>/delete/',
         views.Sacred_textDelete.as_view(), name="sacred_text-delete"),
    # Download
    path('sacred_textdownload/', views.sacred_text_download,
         name="sacred_text-download"),
    path('sacred_textmetadownload/', views.sacred_text_meta_download,
         name="sacred_text-metadownload"),
]
        

urlpatterns += [
    path('religious_literature/create/', views.Religious_literatureCreate.as_view(),
         name="religious_literature-create"),

    path('religious_literatures/', views.Religious_literatureListView.as_view(), name='religious_literatures'),
    path('religious_literatures_all/', views.Religious_literatureListViewAll.as_view(), name='religious_literatures_all'),
    path('religious_literature/<int:pk>', views.Religious_literatureDetailView.as_view(),
         name='religious_literature-detail'),
    path('religious_literature/<int:pk>/update/',
         views.Religious_literatureUpdate.as_view(), name="religious_literature-update"),
    path('religious_literature/<int:pk>/delete/',
         views.Religious_literatureDelete.as_view(), name="religious_literature-delete"),
    # Download
    path('religious_literaturedownload/', views.religious_literature_download,
         name="religious_literature-download"),
    path('religious_literaturemetadownload/', views.religious_literature_meta_download,
         name="religious_literature-metadownload"),
]
        

urlpatterns += [
    path('practical_literature/create/', views.Practical_literatureCreate.as_view(),
         name="practical_literature-create"),

    path('practical_literatures/', views.Practical_literatureListView.as_view(), name='practical_literatures'),
    path('practical_literatures_all/', views.Practical_literatureListViewAll.as_view(), name='practical_literatures_all'),
    path('practical_literature/<int:pk>', views.Practical_literatureDetailView.as_view(),
         name='practical_literature-detail'),
    path('practical_literature/<int:pk>/update/',
         views.Practical_literatureUpdate.as_view(), name="practical_literature-update"),
    path('practical_literature/<int:pk>/delete/',
         views.Practical_literatureDelete.as_view(), name="practical_literature-delete"),
    # Download
    path('practical_literaturedownload/', views.practical_literature_download,
         name="practical_literature-download"),
    path('practical_literaturemetadownload/', views.practical_literature_meta_download,
         name="practical_literature-metadownload"),
]
        

urlpatterns += [
    path('history/create/', views.HistoryCreate.as_view(),
         name="history-create"),

    path('historys/', views.HistoryListView.as_view(), name='historys'),
    path('historys_all/', views.HistoryListViewAll.as_view(), name='historys_all'),
    path('history/<int:pk>', views.HistoryDetailView.as_view(),
         name='history-detail'),
    path('history/<int:pk>/update/',
         views.HistoryUpdate.as_view(), name="history-update"),
    path('history/<int:pk>/delete/',
         views.HistoryDelete.as_view(), name="history-delete"),
    # Download
    path('historydownload/', views.history_download,
         name="history-download"),
    path('historymetadownload/', views.history_meta_download,
         name="history-metadownload"),
]
        

urlpatterns += [
    path('philosophy/create/', views.PhilosophyCreate.as_view(),
         name="philosophy-create"),

    path('philosophys/', views.PhilosophyListView.as_view(), name='philosophys'),
    path('philosophys_all/', views.PhilosophyListViewAll.as_view(), name='philosophys_all'),
    path('philosophy/<int:pk>', views.PhilosophyDetailView.as_view(),
         name='philosophy-detail'),
    path('philosophy/<int:pk>/update/',
         views.PhilosophyUpdate.as_view(), name="philosophy-update"),
    path('philosophy/<int:pk>/delete/',
         views.PhilosophyDelete.as_view(), name="philosophy-delete"),
    # Download
    path('philosophydownload/', views.philosophy_download,
         name="philosophy-download"),
    path('philosophymetadownload/', views.philosophy_meta_download,
         name="philosophy-metadownload"),
]
        

urlpatterns += [
    path('scientific_literature/create/', views.Scientific_literatureCreate.as_view(),
         name="scientific_literature-create"),

    path('scientific_literatures/', views.Scientific_literatureListView.as_view(), name='scientific_literatures'),
    path('scientific_literatures_all/', views.Scientific_literatureListViewAll.as_view(), name='scientific_literatures_all'),
    path('scientific_literature/<int:pk>', views.Scientific_literatureDetailView.as_view(),
         name='scientific_literature-detail'),
    path('scientific_literature/<int:pk>/update/',
         views.Scientific_literatureUpdate.as_view(), name="scientific_literature-update"),
    path('scientific_literature/<int:pk>/delete/',
         views.Scientific_literatureDelete.as_view(), name="scientific_literature-delete"),
    # Download
    path('scientific_literaturedownload/', views.scientific_literature_download,
         name="scientific_literature-download"),
    path('scientific_literaturemetadownload/', views.scientific_literature_meta_download,
         name="scientific_literature-metadownload"),
]
        

urlpatterns += [
    path('fiction/create/', views.FictionCreate.as_view(),
         name="fiction-create"),

    path('fictions/', views.FictionListView.as_view(), name='fictions'),
    path('fictions_all/', views.FictionListViewAll.as_view(), name='fictions_all'),
    path('fiction/<int:pk>', views.FictionDetailView.as_view(),
         name='fiction-detail'),
    path('fiction/<int:pk>/update/',
         views.FictionUpdate.as_view(), name="fiction-update"),
    path('fiction/<int:pk>/delete/',
         views.FictionDelete.as_view(), name="fiction-delete"),
    # Download
    path('fictiondownload/', views.fiction_download,
         name="fiction-download"),
    path('fictionmetadownload/', views.fiction_meta_download,
         name="fiction-metadownload"),
]
        

urlpatterns += [
    path('article/create/', views.ArticleCreate.as_view(),
         name="article-create"),

    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('articles_all/', views.ArticleListViewAll.as_view(), name='articles_all'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(),
         name='article-detail'),
    path('article/<int:pk>/update/',
         views.ArticleUpdate.as_view(), name="article-update"),
    path('article/<int:pk>/delete/',
         views.ArticleDelete.as_view(), name="article-delete"),
    # Download
    path('articledownload/', views.article_download,
         name="article-download"),
    path('articlemetadownload/', views.article_meta_download,
         name="article-metadownload"),
]
        

urlpatterns += [
    path('token/create/', views.TokenCreate.as_view(),
         name="token-create"),

    path('tokens/', views.TokenListView.as_view(), name='tokens'),
    path('tokens_all/', views.TokenListViewAll.as_view(), name='tokens_all'),
    path('token/<int:pk>', views.TokenDetailView.as_view(),
         name='token-detail'),
    path('token/<int:pk>/update/',
         views.TokenUpdate.as_view(), name="token-update"),
    path('token/<int:pk>/delete/',
         views.TokenDelete.as_view(), name="token-delete"),
    # Download
    path('tokendownload/', views.token_download,
         name="token-download"),
    path('tokenmetadownload/', views.token_meta_download,
         name="token-metadownload"),
]
        

urlpatterns += [
    path('precious_metal/create/', views.Precious_metalCreate.as_view(),
         name="precious_metal-create"),

    path('precious_metals/', views.Precious_metalListView.as_view(), name='precious_metals'),
    path('precious_metals_all/', views.Precious_metalListViewAll.as_view(), name='precious_metals_all'),
    path('precious_metal/<int:pk>', views.Precious_metalDetailView.as_view(),
         name='precious_metal-detail'),
    path('precious_metal/<int:pk>/update/',
         views.Precious_metalUpdate.as_view(), name="precious_metal-update"),
    path('precious_metal/<int:pk>/delete/',
         views.Precious_metalDelete.as_view(), name="precious_metal-delete"),
    # Download
    path('precious_metaldownload/', views.precious_metal_download,
         name="precious_metal-download"),
    path('precious_metalmetadownload/', views.precious_metal_meta_download,
         name="precious_metal-metadownload"),
]
        

urlpatterns += [
    path('foreign_coin/create/', views.Foreign_coinCreate.as_view(),
         name="foreign_coin-create"),

    path('foreign_coins/', views.Foreign_coinListView.as_view(), name='foreign_coins'),
    path('foreign_coins_all/', views.Foreign_coinListViewAll.as_view(), name='foreign_coins_all'),
    path('foreign_coin/<int:pk>', views.Foreign_coinDetailView.as_view(),
         name='foreign_coin-detail'),
    path('foreign_coin/<int:pk>/update/',
         views.Foreign_coinUpdate.as_view(), name="foreign_coin-update"),
    path('foreign_coin/<int:pk>/delete/',
         views.Foreign_coinDelete.as_view(), name="foreign_coin-delete"),
    # Download
    path('foreign_coindownload/', views.foreign_coin_download,
         name="foreign_coin-download"),
    path('foreign_coinmetadownload/', views.foreign_coin_meta_download,
         name="foreign_coin-metadownload"),
]
        

urlpatterns += [
    path('indigenous_coin/create/', views.Indigenous_coinCreate.as_view(),
         name="indigenous_coin-create"),

    path('indigenous_coins/', views.Indigenous_coinListView.as_view(), name='indigenous_coins'),
    path('indigenous_coins_all/', views.Indigenous_coinListViewAll.as_view(), name='indigenous_coins_all'),
    path('indigenous_coin/<int:pk>', views.Indigenous_coinDetailView.as_view(),
         name='indigenous_coin-detail'),
    path('indigenous_coin/<int:pk>/update/',
         views.Indigenous_coinUpdate.as_view(), name="indigenous_coin-update"),
    path('indigenous_coin/<int:pk>/delete/',
         views.Indigenous_coinDelete.as_view(), name="indigenous_coin-delete"),
    # Download
    path('indigenous_coindownload/', views.indigenous_coin_download,
         name="indigenous_coin-download"),
    path('indigenous_coinmetadownload/', views.indigenous_coin_meta_download,
         name="indigenous_coin-metadownload"),
]
        

urlpatterns += [
    path('paper_currency/create/', views.Paper_currencyCreate.as_view(),
         name="paper_currency-create"),

    path('paper_currencys/', views.Paper_currencyListView.as_view(), name='paper_currencys'),
    path('paper_currencys_all/', views.Paper_currencyListViewAll.as_view(), name='paper_currencys_all'),
    path('paper_currency/<int:pk>', views.Paper_currencyDetailView.as_view(),
         name='paper_currency-detail'),
    path('paper_currency/<int:pk>/update/',
         views.Paper_currencyUpdate.as_view(), name="paper_currency-update"),
    path('paper_currency/<int:pk>/delete/',
         views.Paper_currencyDelete.as_view(), name="paper_currency-delete"),
    # Download
    path('paper_currencydownload/', views.paper_currency_download,
         name="paper_currency-download"),
    path('paper_currencymetadownload/', views.paper_currency_meta_download,
         name="paper_currency-metadownload"),
]
        

urlpatterns += [
    path('courier/create/', views.CourierCreate.as_view(),
         name="courier-create"),

    path('couriers/', views.CourierListView.as_view(), name='couriers'),
    path('couriers_all/', views.CourierListViewAll.as_view(), name='couriers_all'),
    path('courier/<int:pk>', views.CourierDetailView.as_view(),
         name='courier-detail'),
    path('courier/<int:pk>/update/',
         views.CourierUpdate.as_view(), name="courier-update"),
    path('courier/<int:pk>/delete/',
         views.CourierDelete.as_view(), name="courier-delete"),
    # Download
    path('courierdownload/', views.courier_download,
         name="courier-download"),
    path('couriermetadownload/', views.courier_meta_download,
         name="courier-metadownload"),
]
        

urlpatterns += [
    path('postal_station/create/', views.Postal_stationCreate.as_view(),
         name="postal_station-create"),

    path('postal_stations/', views.Postal_stationListView.as_view(), name='postal_stations'),
    path('postal_stations_all/', views.Postal_stationListViewAll.as_view(), name='postal_stations_all'),
    path('postal_station/<int:pk>', views.Postal_stationDetailView.as_view(),
         name='postal_station-detail'),
    path('postal_station/<int:pk>/update/',
         views.Postal_stationUpdate.as_view(), name="postal_station-update"),
    path('postal_station/<int:pk>/delete/',
         views.Postal_stationDelete.as_view(), name="postal_station-delete"),
    # Download
    path('postal_stationdownload/', views.postal_station_download,
         name="postal_station-download"),
    path('postal_stationmetadownload/', views.postal_station_meta_download,
         name="postal_station-metadownload"),
]
        

urlpatterns += [
    path('general_postal_service/create/', views.General_postal_serviceCreate.as_view(),
         name="general_postal_service-create"),

    path('general_postal_services/', views.General_postal_serviceListView.as_view(), name='general_postal_services'),
    path('general_postal_services_all/', views.General_postal_serviceListViewAll.as_view(), name='general_postal_services_all'),
    path('general_postal_service/<int:pk>', views.General_postal_serviceDetailView.as_view(),
         name='general_postal_service-detail'),
    path('general_postal_service/<int:pk>/update/',
         views.General_postal_serviceUpdate.as_view(), name="general_postal_service-update"),
    path('general_postal_service/<int:pk>/delete/',
         views.General_postal_serviceDelete.as_view(), name="general_postal_service-delete"),
    # Download
    path('general_postal_servicedownload/', views.general_postal_service_download,
         name="general_postal_service-download"),
    path('general_postal_servicemetadownload/', views.general_postal_service_meta_download,
         name="general_postal_service-metadownload"),
]
        
