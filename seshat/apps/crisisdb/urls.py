from .models import Human_sacrifice, External_conflict, Internal_conflict, External_conflict_side, Agricultural_population, Arable_land, Arable_land_per_farmer, Gross_grain_shared_per_agricultural_population, Net_grain_shared_per_agricultural_population, Surplus, Military_expense, Silver_inflow, Silver_stock, Total_population, Gdp_per_capita, Drought_event, Locust_event, Socioeconomic_turmoil_event, Crop_failure_event, Famine_event, Disease_outbreak, Us_violence, Us_location, Us_violence_subtype, Us_violence_data_source, Power_transition
from django.urls import path

from .views import confirm_delete_view, delete_object_view

from . import views

model_form_pairs = [
     (Us_location, 'us_location', ),
     (Us_violence, 'us_violence', ),
     (Us_violence_subtype, 'us_violence_subtype', ),
     (Us_violence_data_source, 'us_violence_data_source', ),
     (Power_transition, 'power_transition', ),

]

urlpatterns = [
    path('vars/', views.QingVars, name='qing_vars'),
    path('playground/', views.playground, name='playground'),
    path('playgrounddownload/', views.playgrounddownload,
         name="playgrounddownload"),
     #path('fpl_all/', views.fpl_all,name="fpl_all"), 
]

urlpatterns += [
    path('us_locations/', views.UsLocationListView.as_view(), name='us_location_list'),
    path('us_locations/create/', views.UsLocationCreateView.as_view(), name='us_location_create'),
    path('us_locations/<int:pk>/update/', views.UsLocationUpdateView.as_view(), name='us_location_update'),
    
    path('subtypes/', views.UsViolenceSubtypeListView.as_view(), name='subtype_list'),
    path('subtypes/create/', views.UsViolenceSubtypeCreateView.as_view(), name='subtype_create'),
    path('subtypes/<int:pk>/update/', views.UsViolenceSubtypeUpdateView.as_view(), name='subtype_update'),
    
    path('datasources/', views.UsViolenceDataSourceListView.as_view(), name='datasource_list'),
    path('datasources/create/', views.UsViolenceDataSourceCreateView.as_view(), name='datasource_create'),
    path('datasources/<int:pk>/update/', views.UsViolenceDataSourceUpdateView.as_view(), name='datasource_update'),
     
     path('uspvdb_all/', views.UsViolenceListView.as_view(), name='us_violence_list'),
     path('uspvdb/', views.UsViolenceListViewPaginated.as_view(), name='us_violence_paginated'),

    path('uspvdb/create/', views.UsViolenceCreateView.as_view(), name='us_violence_create'),
    path('uspvdb/<int:pk>/update/', views.UsViolenceUpdateView.as_view(), name='us_violence_update'),
     path('uspvdb_download/', views.download_csv_all_american_violence,
         name="us_violence_download"),
     ]


for model_class, x_name in model_form_pairs:
     """
     Programmatically create the following URL patterns for each model:
     - /model_name/<int:pk>/confirm-delete
     - /model_name/<int:pk>/delete/
     """
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
    path('crisis_consequence/create/', views.Crisis_consequenceCreate.as_view(),
         name="crisis_consequence-create"),
     path('crisis_consequence/createheavy/', views.Crisis_consequenceCreateHeavy.as_view(),
         name="crisis_consequence-create_heavy"),
    path('crisis_consequences/', views.Crisis_consequenceListView.as_view(), name='crisis_consequences'),
    path('crisis_consequences_all/', views.Crisis_consequenceListViewAll.as_view(), name='crisis_consequences_all'),
    path('crisis_consequence/<int:pk>', views.Crisis_consequenceDetailView.as_view(),
         name='crisis_consequence-detail'),
    path('crisis_consequence/<int:pk>/update/',
         views.Crisis_consequenceUpdate.as_view(), name="crisis_consequence-update"),
    path('crisis_consequence/<int:pk>/updateheavy/',
         views.Crisis_consequenceUpdateHeavy.as_view(), name="crisis_consequence-update_heavy"),
    path('crisis_consequence/<int:pk>/delete/',
         views.Crisis_consequenceDelete.as_view(), name="crisis_consequence-delete"),
    # Download
    path('crisis_consequencedownload/', views.crisis_consequence_download,
         name="crisis_consequence-download"),
    path('crisis_consequencemetadownload/', views.crisis_consequence_meta_download,
         name="crisis_consequence-metadownload"),
         path('get-citations-dropdown/', views.get_citations_dropdown, name='get_citations_dropdown'),

]

urlpatterns += [
    path('power_transition/create/', views.Power_transitionCreate.as_view(),
         name="power_transition-create"),
     path('power_transition/createheavy/', views.Power_transitionCreateHeavy.as_view(),
         name="power_transition-create_heavy"),
    path('power_transitions/', views.Power_transitionListView.as_view(), name='power_transitions'),
    path('power_transitions_list_all/', views.Power_transitionListViewAll.as_view(), name='power_transition_list'),
    path('power_transitions_all/', views.Power_transitionListViewAll.as_view(), name='power_transitions_all'),
    path('power_transition/<int:pk>', views.Power_transitionDetailView.as_view(),
         name='power_transition-detail'),
    path('power_transition/<int:pk>/update/',
         views.Power_transitionUpdate.as_view(), name="power_transition-update"),
    path('power_transition/<int:pk>/updateheavy/',
         views.Power_transitionUpdateHeavy.as_view(), name="power_transition-update_heavy"),
    #path('power_transition/<int:pk>/delete/',
    #     views.Power_transitionDelete.as_view(), name="power_transition-delete"),
    # Download
    path('power_transitiondownload/', views.power_transition_download,
         name="power_transition-download"),
    path('power_transitionmetadownload/', views.power_transition_meta_download,
         name="power_transition-metadownload"),
         # path('get-citations-dropdown/', views.get_citations_dropdown, name='get_citations_dropdown'),

]

urlpatterns += [
    path('human_sacrifice/create/', views.Human_sacrificeCreate.as_view(),
         name="human_sacrifice-create"),

    path('human_sacrifices/', views.Human_sacrificeListView.as_view(), name='human_sacrifices'),
    path('human_sacrifices_all/', views.Human_sacrificeListViewAll.as_view(), name='human_sacrifices_all'),
    path('human_sacrifice/<int:pk>', views.Human_sacrificeDetailView.as_view(),
         name='human_sacrifice-detail'),
    path('human_sacrifice/<int:pk>/update/',
         views.Human_sacrificeUpdate.as_view(), name="human_sacrifice-update"),
    path('human_sacrifice/<int:pk>/delete/',
         views.Human_sacrificeDelete.as_view(), name="human_sacrifice-delete"),
    # Download
    path('human_sacrificedownload/', views.human_sacrifice_download,
         name="human_sacrifice-download"),
    path('human_sacrificemetadownload/', views.human_sacrifice_meta_download,
         name="human_sacrifice-metadownload"),
     path('create_subcomment/<int:hs_instance_id>/', views.create_a_comment_with_a_subcomment, name='create_subcomment'),

]
        

urlpatterns += [
    path('external_conflict/create/', views.External_conflictCreate.as_view(),
         name="external_conflict-create"),

    path('external_conflicts/', views.External_conflictListView.as_view(), name='external_conflicts'),
    path('external_conflict/<int:pk>', views.External_conflictDetailView.as_view(),
         name='external_conflict-detail'),
    path('external_conflict/<int:pk>/update/',
         views.External_conflictUpdate.as_view(), name="external_conflict-update"),
    path('external_conflict/<int:pk>/delete/',
         views.External_conflictDelete.as_view(), name="external_conflict-delete"),
    # Download
    path('external_conflictdownload/', views.external_conflict_download,
         name="external_conflict-download"),
    path('external_conflictmetadownload/', views.external_conflict_meta_download,
         name="external_conflict-metadownload"),
]
        

urlpatterns += [
    path('internal_conflict/create/', views.Internal_conflictCreate.as_view(),
         name="internal_conflict-create"),

    path('internal_conflicts/', views.Internal_conflictListView.as_view(), name='internal_conflicts'),
    path('internal_conflict/<int:pk>', views.Internal_conflictDetailView.as_view(),
         name='internal_conflict-detail'),
    path('internal_conflict/<int:pk>/update/',
         views.Internal_conflictUpdate.as_view(), name="internal_conflict-update"),
    path('internal_conflict/<int:pk>/delete/',
         views.Internal_conflictDelete.as_view(), name="internal_conflict-delete"),
    # Download
    path('internal_conflictdownload/', views.internal_conflict_download,
         name="internal_conflict-download"),
    path('internal_conflictmetadownload/', views.internal_conflict_meta_download,
         name="internal_conflict-metadownload"),
]
        

urlpatterns += [
    path('external_conflict_side/create/', views.External_conflict_sideCreate.as_view(),
         name="external_conflict_side-create"),

    path('external_conflict_sides/', views.External_conflict_sideListView.as_view(), name='external_conflict_sides'),
    path('external_conflict_side/<int:pk>', views.External_conflict_sideDetailView.as_view(),
         name='external_conflict_side-detail'),
    path('external_conflict_side/<int:pk>/update/',
         views.External_conflict_sideUpdate.as_view(), name="external_conflict_side-update"),
    path('external_conflict_side/<int:pk>/delete/',
         views.External_conflict_sideDelete.as_view(), name="external_conflict_side-delete"),
    # Download
    path('external_conflict_sidedownload/', views.external_conflict_side_download,
         name="external_conflict_side-download"),
    path('external_conflict_sidemetadownload/', views.external_conflict_side_meta_download,
         name="external_conflict_side-metadownload"),
]
        

urlpatterns += [
    path('agricultural_population/create/', views.Agricultural_populationCreate.as_view(),
         name="agricultural_population-create"),

    path('agricultural_populations/', views.Agricultural_populationListView.as_view(), name='agricultural_populations'),
    path('agricultural_population/<int:pk>', views.Agricultural_populationDetailView.as_view(),
         name='agricultural_population-detail'),
    path('agricultural_population/<int:pk>/update/',
         views.Agricultural_populationUpdate.as_view(), name="agricultural_population-update"),
    path('agricultural_population/<int:pk>/delete/',
         views.Agricultural_populationDelete.as_view(), name="agricultural_population-delete"),
    # Download
    path('agricultural_populationdownload/', views.agricultural_population_download,
         name="agricultural_population-download"),
    path('agricultural_populationmetadownload/', views.agricultural_population_meta_download,
         name="agricultural_population-metadownload"),
]
        

urlpatterns += [
    path('arable_land/create/', views.Arable_landCreate.as_view(),
         name="arable_land-create"),

    path('arable_lands/', views.Arable_landListView.as_view(), name='arable_lands'),
    path('arable_land/<int:pk>', views.Arable_landDetailView.as_view(),
         name='arable_land-detail'),
    path('arable_land/<int:pk>/update/',
         views.Arable_landUpdate.as_view(), name="arable_land-update"),
    path('arable_land/<int:pk>/delete/',
         views.Arable_landDelete.as_view(), name="arable_land-delete"),
    # Download
    path('arable_landdownload/', views.arable_land_download,
         name="arable_land-download"),
    path('arable_landmetadownload/', views.arable_land_meta_download,
         name="arable_land-metadownload"),
]
        

urlpatterns += [
    path('arable_land_per_farmer/create/', views.Arable_land_per_farmerCreate.as_view(),
         name="arable_land_per_farmer-create"),

    path('arable_land_per_farmers/', views.Arable_land_per_farmerListView.as_view(), name='arable_land_per_farmers'),
    path('arable_land_per_farmer/<int:pk>', views.Arable_land_per_farmerDetailView.as_view(),
         name='arable_land_per_farmer-detail'),
    path('arable_land_per_farmer/<int:pk>/update/',
         views.Arable_land_per_farmerUpdate.as_view(), name="arable_land_per_farmer-update"),
    path('arable_land_per_farmer/<int:pk>/delete/',
         views.Arable_land_per_farmerDelete.as_view(), name="arable_land_per_farmer-delete"),
    # Download
    path('arable_land_per_farmerdownload/', views.arable_land_per_farmer_download,
         name="arable_land_per_farmer-download"),
    path('arable_land_per_farmermetadownload/', views.arable_land_per_farmer_meta_download,
         name="arable_land_per_farmer-metadownload"),
]
        

urlpatterns += [
    path('gross_grain_shared_per_agricultural_population/create/', views.Gross_grain_shared_per_agricultural_populationCreate.as_view(),
         name="gross_grain_shared_per_agricultural_population-create"),

    path('gross_grain_shared_per_agricultural_populations/', views.Gross_grain_shared_per_agricultural_populationListView.as_view(), name='gross_grain_shared_per_agricultural_populations'),
    path('gross_grain_shared_per_agricultural_population/<int:pk>', views.Gross_grain_shared_per_agricultural_populationDetailView.as_view(),
         name='gross_grain_shared_per_agricultural_population-detail'),
    path('gross_grain_shared_per_agricultural_population/<int:pk>/update/',
         views.Gross_grain_shared_per_agricultural_populationUpdate.as_view(), name="gross_grain_shared_per_agricultural_population-update"),
    path('gross_grain_shared_per_agricultural_population/<int:pk>/delete/',
         views.Gross_grain_shared_per_agricultural_populationDelete.as_view(), name="gross_grain_shared_per_agricultural_population-delete"),
    # Download
    path('gross_grain_shared_per_agricultural_populationdownload/', views.gross_grain_shared_per_agricultural_population_download,
         name="gross_grain_shared_per_agricultural_population-download"),
    path('gross_grain_shared_per_agricultural_populationmetadownload/', views.gross_grain_shared_per_agricultural_population_meta_download,
         name="gross_grain_shared_per_agricultural_population-metadownload"),
]
        

urlpatterns += [
    path('net_grain_shared_per_agricultural_population/create/', views.Net_grain_shared_per_agricultural_populationCreate.as_view(),
         name="net_grain_shared_per_agricultural_population-create"),

    path('net_grain_shared_per_agricultural_populations/', views.Net_grain_shared_per_agricultural_populationListView.as_view(), name='net_grain_shared_per_agricultural_populations'),
    path('net_grain_shared_per_agricultural_population/<int:pk>', views.Net_grain_shared_per_agricultural_populationDetailView.as_view(),
         name='net_grain_shared_per_agricultural_population-detail'),
    path('net_grain_shared_per_agricultural_population/<int:pk>/update/',
         views.Net_grain_shared_per_agricultural_populationUpdate.as_view(), name="net_grain_shared_per_agricultural_population-update"),
    path('net_grain_shared_per_agricultural_population/<int:pk>/delete/',
         views.Net_grain_shared_per_agricultural_populationDelete.as_view(), name="net_grain_shared_per_agricultural_population-delete"),
    # Download
    path('net_grain_shared_per_agricultural_populationdownload/', views.net_grain_shared_per_agricultural_population_download,
         name="net_grain_shared_per_agricultural_population-download"),
    path('net_grain_shared_per_agricultural_populationmetadownload/', views.net_grain_shared_per_agricultural_population_meta_download,
         name="net_grain_shared_per_agricultural_population-metadownload"),
]
        

urlpatterns += [
    path('surplus/create/', views.SurplusCreate.as_view(),
         name="surplus-create"),

    path('surplus/', views.SurplusListView.as_view(), name='surplus'),
    path('surplus/<int:pk>', views.SurplusDetailView.as_view(),
         name='surplus-detail'),
    path('surplus/<int:pk>/update/',
         views.SurplusUpdate.as_view(), name="surplus-update"),
    path('surplus/<int:pk>/delete/',
         views.SurplusDelete.as_view(), name="surplus-delete"),
    # Download
    path('surplusdownload/', views.surplus_download,
         name="surplus-download"),
    path('surplusmetadownload/', views.surplus_meta_download,
         name="surplus-metadownload"),
]
        

urlpatterns += [
    path('military_expense/create/', views.Military_expenseCreate.as_view(),
         name="military_expense-create"),

    path('military_expenses/', views.Military_expenseListView.as_view(), name='military_expenses'),
    path('military_expense/<int:pk>', views.Military_expenseDetailView.as_view(),
         name='military_expense-detail'),
    path('military_expense/<int:pk>/update/',
         views.Military_expenseUpdate.as_view(), name="military_expense-update"),
    path('military_expense/<int:pk>/delete/',
         views.Military_expenseDelete.as_view(), name="military_expense-delete"),
    # Download
    path('military_expensedownload/', views.military_expense_download,
         name="military_expense-download"),
    path('military_expensemetadownload/', views.military_expense_meta_download,
         name="military_expense-metadownload"),
]
        

urlpatterns += [
    path('silver_inflow/create/', views.Silver_inflowCreate.as_view(),
         name="silver_inflow-create"),

    path('silver_inflows/', views.Silver_inflowListView.as_view(), name='silver_inflows'),
    path('silver_inflow/<int:pk>', views.Silver_inflowDetailView.as_view(),
         name='silver_inflow-detail'),
    path('silver_inflow/<int:pk>/update/',
         views.Silver_inflowUpdate.as_view(), name="silver_inflow-update"),
    path('silver_inflow/<int:pk>/delete/',
         views.Silver_inflowDelete.as_view(), name="silver_inflow-delete"),
    # Download
    path('silver_inflowdownload/', views.silver_inflow_download,
         name="silver_inflow-download"),
    path('silver_inflowmetadownload/', views.silver_inflow_meta_download,
         name="silver_inflow-metadownload"),
]
        

urlpatterns += [
    path('silver_stock/create/', views.Silver_stockCreate.as_view(),
         name="silver_stock-create"),

    path('silver_stocks/', views.Silver_stockListView.as_view(), name='silver_stocks'),
    path('silver_stock/<int:pk>', views.Silver_stockDetailView.as_view(),
         name='silver_stock-detail'),
    path('silver_stock/<int:pk>/update/',
         views.Silver_stockUpdate.as_view(), name="silver_stock-update"),
    path('silver_stock/<int:pk>/delete/',
         views.Silver_stockDelete.as_view(), name="silver_stock-delete"),
    # Download
    path('silver_stockdownload/', views.silver_stock_download,
         name="silver_stock-download"),
    path('silver_stockmetadownload/', views.silver_stock_meta_download,
         name="silver_stock-metadownload"),
]
        

urlpatterns += [
    path('total_population/create/', views.Total_populationCreate.as_view(),
         name="total_population-create"),

    path('total_populations/', views.Total_populationListView.as_view(), name='total_populations'),
    path('total_population/<int:pk>', views.Total_populationDetailView.as_view(),
         name='total_population-detail'),
    path('total_population/<int:pk>/update/',
         views.Total_populationUpdate.as_view(), name="total_population-update"),
    path('total_population/<int:pk>/delete/',
         views.Total_populationDelete.as_view(), name="total_population-delete"),
    # Download
    path('total_populationdownload/', views.total_population_download,
         name="total_population-download"),
    path('total_populationmetadownload/', views.total_population_meta_download,
         name="total_population-metadownload"),
]
        

urlpatterns += [
    path('gdp_per_capita/create/', views.Gdp_per_capitaCreate.as_view(),
         name="gdp_per_capita-create"),

    path('gdp_per_capitas/', views.Gdp_per_capitaListView.as_view(), name='gdp_per_capitas'),
    path('gdp_per_capita/<int:pk>', views.Gdp_per_capitaDetailView.as_view(),
         name='gdp_per_capita-detail'),
    path('gdp_per_capita/<int:pk>/update/',
         views.Gdp_per_capitaUpdate.as_view(), name="gdp_per_capita-update"),
    path('gdp_per_capita/<int:pk>/delete/',
         views.Gdp_per_capitaDelete.as_view(), name="gdp_per_capita-delete"),
    # Download
    path('gdp_per_capitadownload/', views.gdp_per_capita_download,
         name="gdp_per_capita-download"),
    path('gdp_per_capitametadownload/', views.gdp_per_capita_meta_download,
         name="gdp_per_capita-metadownload"),
]
        

urlpatterns += [
    path('drought_event/create/', views.Drought_eventCreate.as_view(),
         name="drought_event-create"),

    path('drought_events/', views.Drought_eventListView.as_view(), name='drought_events'),
    path('drought_event/<int:pk>', views.Drought_eventDetailView.as_view(),
         name='drought_event-detail'),
    path('drought_event/<int:pk>/update/',
         views.Drought_eventUpdate.as_view(), name="drought_event-update"),
    path('drought_event/<int:pk>/delete/',
         views.Drought_eventDelete.as_view(), name="drought_event-delete"),
    # Download
    path('drought_eventdownload/', views.drought_event_download,
         name="drought_event-download"),
    path('drought_eventmetadownload/', views.drought_event_meta_download,
         name="drought_event-metadownload"),
]
        

urlpatterns += [
    path('locust_event/create/', views.Locust_eventCreate.as_view(),
         name="locust_event-create"),

    path('locust_events/', views.Locust_eventListView.as_view(), name='locust_events'),
    path('locust_event/<int:pk>', views.Locust_eventDetailView.as_view(),
         name='locust_event-detail'),
    path('locust_event/<int:pk>/update/',
         views.Locust_eventUpdate.as_view(), name="locust_event-update"),
    path('locust_event/<int:pk>/delete/',
         views.Locust_eventDelete.as_view(), name="locust_event-delete"),
    # Download
    path('locust_eventdownload/', views.locust_event_download,
         name="locust_event-download"),
    path('locust_eventmetadownload/', views.locust_event_meta_download,
         name="locust_event-metadownload"),
]
        

urlpatterns += [
    path('socioeconomic_turmoil_event/create/', views.Socioeconomic_turmoil_eventCreate.as_view(),
         name="socioeconomic_turmoil_event-create"),

    path('socioeconomic_turmoil_events/', views.Socioeconomic_turmoil_eventListView.as_view(), name='socioeconomic_turmoil_events'),
    path('socioeconomic_turmoil_event/<int:pk>', views.Socioeconomic_turmoil_eventDetailView.as_view(),
         name='socioeconomic_turmoil_event-detail'),
    path('socioeconomic_turmoil_event/<int:pk>/update/',
         views.Socioeconomic_turmoil_eventUpdate.as_view(), name="socioeconomic_turmoil_event-update"),
    path('socioeconomic_turmoil_event/<int:pk>/delete/',
         views.Socioeconomic_turmoil_eventDelete.as_view(), name="socioeconomic_turmoil_event-delete"),
    # Download
    path('socioeconomic_turmoil_eventdownload/', views.socioeconomic_turmoil_event_download,
         name="socioeconomic_turmoil_event-download"),
    path('socioeconomic_turmoil_eventmetadownload/', views.socioeconomic_turmoil_event_meta_download,
         name="socioeconomic_turmoil_event-metadownload"),
]
        

urlpatterns += [
    path('crop_failure_event/create/', views.Crop_failure_eventCreate.as_view(),
         name="crop_failure_event-create"),

    path('crop_failure_events/', views.Crop_failure_eventListView.as_view(), name='crop_failure_events'),
    path('crop_failure_event/<int:pk>', views.Crop_failure_eventDetailView.as_view(),
         name='crop_failure_event-detail'),
    path('crop_failure_event/<int:pk>/update/',
         views.Crop_failure_eventUpdate.as_view(), name="crop_failure_event-update"),
    path('crop_failure_event/<int:pk>/delete/',
         views.Crop_failure_eventDelete.as_view(), name="crop_failure_event-delete"),
    # Download
    path('crop_failure_eventdownload/', views.crop_failure_event_download,
         name="crop_failure_event-download"),
    path('crop_failure_eventmetadownload/', views.crop_failure_event_meta_download,
         name="crop_failure_event-metadownload"),
]
        

urlpatterns += [
    path('famine_event/create/', views.Famine_eventCreate.as_view(),
         name="famine_event-create"),

    path('famine_events/', views.Famine_eventListView.as_view(), name='famine_events'),
    path('famine_event/<int:pk>', views.Famine_eventDetailView.as_view(),
         name='famine_event-detail'),
    path('famine_event/<int:pk>/update/',
         views.Famine_eventUpdate.as_view(), name="famine_event-update"),
    path('famine_event/<int:pk>/delete/',
         views.Famine_eventDelete.as_view(), name="famine_event-delete"),
    # Download
    path('famine_eventdownload/', views.famine_event_download,
         name="famine_event-download"),
    path('famine_eventmetadownload/', views.famine_event_meta_download,
         name="famine_event-metadownload"),
]
        

urlpatterns += [
    path('disease_outbreak/create/', views.Disease_outbreakCreate.as_view(),
         name="disease_outbreak-create"),

    path('disease_outbreaks/', views.Disease_outbreakListView.as_view(), name='disease_outbreaks'),
    path('disease_outbreak/<int:pk>', views.Disease_outbreakDetailView.as_view(),
         name='disease_outbreak-detail'),
    path('disease_outbreak/<int:pk>/update/',
         views.Disease_outbreakUpdate.as_view(), name="disease_outbreak-update"),
    path('disease_outbreak/<int:pk>/delete/',
         views.Disease_outbreakDelete.as_view(), name="disease_outbreak-delete"),
    # Download
    path('disease_outbreakdownload/', views.disease_outbreak_download,
         name="disease_outbreak-download"),
    path('disease_outbreakmetadownload/', views.disease_outbreak_meta_download,
         name="disease_outbreak-metadownload"),
]
        