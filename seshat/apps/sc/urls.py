from django.urls import path

from ..constants import SUBSECTIONS

from .forms import (
    Communal_buildingForm,
    Utilitarian_public_buildingForm,
    Other_utilitarian_public_buildingForm,
    Symbolic_buildingForm,
    Entertainment_buildingForm,
    Knowledge_or_information_buildingForm,
    Special_purpose_siteForm,
    Ceremonial_siteForm,
    Burial_siteForm,
    Trading_emporiaForm,
    EnclosureForm,
    Length_measurement_systemForm,
    Area_measurement_systemForm,
    Volume_measurement_systemForm,
    Weight_measurement_systemForm,
    Time_measurement_systemForm,
    Geometrical_measurement_systemForm,
    Other_measurement_systemForm,
    Debt_and_credit_structureForm,
    Store_of_wealthForm,
    # BridgeForm,  # TODO: This is not currently used, is that correct?
    Source_of_supportForm,
    Occupational_complexityForm,
    Special_purpose_houseForm,
    Other_special_purpose_siteForm,
    Military_levelForm,
    Largest_communication_distanceForm,
    Fastest_individual_communicationForm,
)
from .models import (
    Communal_building,
    Utilitarian_public_building,
    Other_utilitarian_public_building,
    Symbolic_building,
    Entertainment_building,
    Knowledge_or_information_building,
    Special_purpose_site,
    Ceremonial_site,
    Burial_site,
    Trading_emporia,
    Enclosure,
    Length_measurement_system,
    Area_measurement_system,
    Volume_measurement_system,
    Weight_measurement_system,
    Time_measurement_system,
    Geometrical_measurement_system,
    Other_measurement_system,
    Debt_and_credit_structure,
    Store_of_wealth,
    # Bridge,  # TODO: This is not currently used, is that correct?
    Source_of_support,
    Occupational_complexity,
    Special_purpose_house,
    Other_special_purpose_site,
    Military_level,
    Largest_communication_distance,
    Fastest_individual_communication,
)

from . import views
from .specific_views import downloads
from .specific_views import generic
from ..generic_views import (
    GenericConfirmDeleteView,
    GenericCreateView,
    GenericDeleteView,
    # GenericDetailView,
    GenericDownloadView,
    GenericListView,
    GenericMetaDownloadView,
    # GenericUpdateView,
    GenericMultipleDownloadView,
    VariableView,
    ProblematicDataView
)

PREFIX = "social_complexity_"

model_form_pairs = [
    (
        Communal_building,
        Communal_buildingForm,
        "communal_building",
        "Communal Building",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Utilitarian_public_building,
        Utilitarian_public_buildingForm,
        "utilitarian_public_building",
        "Utilitarian Public Building",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Other_utilitarian_public_building,
        Other_utilitarian_public_buildingForm,
        "other_utilitarian_public_building",
        "Other Utilitarian Public Building",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Symbolic_building,
        Symbolic_buildingForm,
        "symbolic_building",
        "Symbolic Building",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Entertainment_building,
        Entertainment_buildingForm,
        "entertainment_building",
        "Entertainment Building",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Knowledge_or_information_building,
        Knowledge_or_information_buildingForm,
        "knowledge_or_information_building",
        "Knowledge Or Information Building",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Special_purpose_site,
        Special_purpose_siteForm,
        "special_purpose_site",
        "Special Purpose Site",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Ceremonial_site,
        Ceremonial_siteForm,
        "ceremonial_site",
        "Ceremonial Site",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Burial_site,
        Burial_siteForm,
        "burial_site",
        "Burial Site",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Trading_emporia,
        Trading_emporiaForm,
        "trading_emporia",
        "Trading Emporia",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Enclosure,
        EnclosureForm,
        "enclosure",
        "Enclosure",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Length_measurement_system,
        Length_measurement_systemForm,
        "length_measurement_system",
        "Length Measurement System",
        "Information",
        "Measurement System",
    ),
    (
        Area_measurement_system,
        Area_measurement_systemForm,
        "area_measurement_system",
        "Area Measurement System",
        "Information",
        "Measurement System",
    ),
    (
        Volume_measurement_system,
        Volume_measurement_systemForm,
        "volume_measurement_system",
        "Volume Measurement System",
        "Information",
        "Measurement System",
    ),
    (
        Weight_measurement_system,
        Weight_measurement_systemForm,
        "weight_measurement_system",
        "Weight Measurement System",
        "Information",
        "Measurement System",
    ),
    (
        Time_measurement_system,
        Time_measurement_systemForm,
        "time_measurement_system",
        "Time Measurement System",
        "Information",
        "Measurement System",
    ),
    (
        Geometrical_measurement_system,
        Geometrical_measurement_systemForm,
        "geometrical_measurement_system",
        "Geometrical Measurement System",
        "Information",
        "Measurement System",
    ),
    (
        Other_measurement_system,
        Other_measurement_systemForm,
        "other_measurement_system",
        "Other Measurement System",
        "Information",
        "Measurement System",
    ),
    (
        Debt_and_credit_structure,
        Debt_and_credit_structureForm,
        "debt_and_credit_structure",
        "Debt And Credit Structure",
        "Information",
        "Money",
    ),
    (
        Store_of_wealth,
        Store_of_wealthForm,
        "store_of_wealth",
        "Store Of Wealth",
        "Information",
        "Money",
    ),
    (
        Source_of_support,
        Source_of_supportForm,
        "source_of_support",
        "Source Of Support",
        "Professions",
        None,
    ),
    (
        Occupational_complexity,
        Occupational_complexityForm,
        "occupational_complexity",
        "Occupational Complexity",
        "Professions",
        None,
    ),
    (
        Special_purpose_house,
        Special_purpose_houseForm,
        "special_purpose_house",
        "Special Purpose House",
        "Specialized Buildings: polity owned",
        None,
    ),
    (
        Other_special_purpose_site,
        Other_special_purpose_siteForm,
        "other_special_purpose_site",
        "Other Special Purpose Site",
        "Special-purpose Sites",
        None,
    ),
    (
        Military_level,
        Military_levelForm,
        "military_level",
        "Military Level",
        "Hierarchical Complexity",
        None,
    ),
    (
        Largest_communication_distance,
        Largest_communication_distanceForm,
        "largest_communication_distance",
        "Largest Communication Distance",
        "Social Scale",
        None,
    ),
    (
        Fastest_individual_communication,
        Fastest_individual_communicationForm,
        "fastest_individual_communication",
        "Fastest Individual Communication",
        "Information",
        "Postal System",
    ),
]

APP_LABEL = "sc"

urlpatterns = [
    path("scvars/", VariableView.as_view(app_label=APP_LABEL), name="scvars"),
    path(
        "problematic_sc_data_table/",
        ProblematicDataView.as_view(
            app_label=APP_LABEL,
            template_name="sc/problematic_sc_data_table.html"
        ),
        name="problematic_sc_data_table",
    ),
    path(
        "download-csv-sc-all/",
        GenericMultipleDownloadView.as_view(
            app_label=APP_LABEL,
            exclude_models=["Ra"],
            prefix="social_complexity_information_"
        ),
        # downloads.download_csv_all_sc,
        name="download_csv_all_sc",
    ),
]

categories = [
    "Social Scale",
    "Professions",
    "Bureaucracy Characteristics",
    "Hierarchical Complexity",
    "Law",
    "Specialized Buildings: polity owned",
    "Transport Infrastructure",
    "Special-Purpose Sites",
    "Information",
]

for category in categories:
    if "polity owned" in category:
        category = category.strip(": polity owned")

    urlified = category.lower().replace("-", "").replace(":", "").replace(" ", "_")
    nospaces = category.replace("-", "").replace(" ", "")

    urlpatterns += [
        path(
            f"download_csv_{urlified}/",
            GenericMultipleDownloadView.as_view(
                app_label=APP_LABEL,
                subsection=SUBSECTIONS.sc[nospaces],
                prefix=f"{PREFIX}{urlified}_",
            ),
            name=f"download_csv_{urlified}",
        )
    ]  # TODO: replace with util function that is now made: get_url_pattern


#     path(
#         "download_csv_social_scale/",
#         downloads.download_csv_social_scale,
#         name="download_csv_social_scale",
#     ),
#     path(
#         "download_csv_professions/",
#         downloads.download_csv_professions,
#         name="download_csv_professions",
#     ),
#     path(
#         "download_csv_bureaucracy_characteristics/",
#         downloads.download_csv_bureaucracy_characteristics,
#         name="download_csv_bureaucracy_characteristics",
#     ),
#     path(
#         "download_csv_hierarchical_complexity/",
#         downloads.download_csv_hierarchical_complexity,
#         name="download_csv_hierarchical_complexity",
#     ),
#     path(
#         "download_csv_law/",
#         downloads.download_csv_law,
#         name="download_csv_law",
#     ),
#     path(
#         "download_csv_specialized_buildings_polity_owned/",
#         downloads.download_csv_specialized_buildings_polity_owned,
#         name="download_csv_specialized_buildings_polity_owned",
#     ),
#     path(
#         "download_csv_transport_infrastructure/",
#         downloads.download_csv_transport_infrastructure,
#         name="download_csv_transport_infrastructure",
#     ),
#     path(
#         "download_csv_special_purpose_sites/",
#         downloads.download_csv_special_purpose_sites,
#         name="download_csv_special_purpose_sites",
#     ),
#     path(
#         "download_csv_information/",
#         downloads.download_csv_information,
#         name="download_csv_information",
#     ),

urlpatterns += [
    path("ra/create/", views.RaCreateView.as_view(), name="ra-create"),
    path("ras/", views.RaListView.as_view(), name="ras"),
    path("ras_all/", views.RaListAllView.as_view(), name="ras_all"),
    path("ra/<int:pk>", views.RaDetailView.as_view(), name="ra-detail"),
    path(
        "ra/<int:pk>/update/", views.RaUpdateView.as_view(), name="ra-update"
    ),
    path(
        "ra/<int:pk>/delete/", views.RaDeleteView.as_view(), name="ra-delete"
    ),
    path("radownload/", downloads.ra_download_view, name="ra-download"),
    path(
        "rametadownload/",
        downloads.ra_meta_download_view,
        name="ra-metadownload",
    ),
    path(
        "polity_territory/create/",
        views.Polity_territoryCreateView.as_view(),
        name="polity_territory-create",
    ),
    path(
        "polity_territorys/",
        views.Polity_territoryListView.as_view(),
        name="polity_territorys",
    ),
    path(
        "polity_territorys_all/",
        views.Polity_territoryListAllView.as_view(),
        name="polity_territorys_all",
    ),
    path(
        "polity_territory/<int:pk>",
        views.Polity_territoryDetailView.as_view(),
        name="polity_territory-detail",
    ),
    path(
        "polity_territory/<int:pk>/update/",
        views.Polity_territoryUpdateView.as_view(),
        name="polity_territory-update",
    ),
    path(
        "polity_territory/<int:pk>/delete/",
        views.Polity_territoryDeleteView.as_view(),
        name="polity_territory-delete",
    ),
    path(
        "polity_territorydownload/",
        downloads.polity_territory_download_view,
        name="polity_territory-download",
    ),
    path(
        "polity_territorymetadownload/",
        downloads.polity_territory_meta_download_view,
        name="polity_territory-metadownload",
    ),
    path(
        "polity_population/create/",
        views.Polity_populationCreateView.as_view(),
        name="polity_population-create",
    ),
    path(
        "polity_populations/",
        views.Polity_populationListView.as_view(),
        name="polity_populations",
    ),
    path(
        "polity_populations_all/",
        views.Polity_populationListAllView.as_view(),
        name="polity_populations_all",
    ),
    path(
        "polity_population/<int:pk>",
        views.Polity_populationDetailView.as_view(),
        name="polity_population-detail",
    ),
    path(
        "polity_population/<int:pk>/update/",
        views.Polity_populationUpdateView.as_view(),
        name="polity_population-update",
    ),
    path(
        "polity_population/<int:pk>/delete/",
        views.Polity_populationDeleteView.as_view(),
        name="polity_population-delete",
    ),
    path(
        "polity_populationdownload/",
        downloads.polity_population_download_view,
        name="polity_population-download",
    ),
    path(
        "polity_populationmetadownload/",
        downloads.polity_population_meta_download_view,
        name="polity_population-metadownload",
    ),
    path(
        "population_of_the_largest_settlement/create/",
        views.Population_of_the_largest_settlementCreateView.as_view(),
        name="population_of_the_largest_settlement-create",
    ),
    path(
        "population_of_the_largest_settlements/",
        views.Population_of_the_largest_settlementListView.as_view(),
        name="population_of_the_largest_settlements",
    ),
    path(
        "population_of_the_largest_settlements_all/",
        views.Population_of_the_largest_settlementListAllView.as_view(),
        name="population_of_the_largest_settlements_all",
    ),
    path(
        "population_of_the_largest_settlement/<int:pk>",
        views.Population_of_the_largest_settlementDetailView.as_view(),
        name="population_of_the_largest_settlement-detail",
    ),
    path(
        "population_of_the_largest_settlement/<int:pk>/update/",
        views.Population_of_the_largest_settlementUpdateView.as_view(),
        name="population_of_the_largest_settlement-update",
    ),
    path(
        "population_of_the_largest_settlement/<int:pk>/delete/",
        views.Population_of_the_largest_settlementDeleteView.as_view(),
        name="population_of_the_largest_settlement-delete",
    ),
    path(
        "population_of_the_largest_settlementdownload/",
        downloads.population_of_the_largest_settlement_download_view,
        name="population_of_the_largest_settlement-download",
    ),
    path(
        "population_of_the_largest_settlementmetadownload/",
        downloads.population_of_the_largest_settlement_meta_download_view,
        name="population_of_the_largest_settlement-metadownload",
    ),
    path(
        "settlement_hierarchy/create/",
        views.Settlement_hierarchyCreateView.as_view(),
        name="settlement_hierarchy-create",
    ),
    path(
        "settlement_hierarchys/",
        views.Settlement_hierarchyListView.as_view(),
        name="settlement_hierarchys",
    ),
    path(
        "settlement_hierarchys_all/",
        views.Settlement_hierarchyListAllView.as_view(),
        name="settlement_hierarchys_all",
    ),
    path(
        "settlement_hierarchy/<int:pk>",
        views.Settlement_hierarchyDetailView.as_view(),
        name="settlement_hierarchy-detail",
    ),
    path(
        "settlement_hierarchy/<int:pk>/update/",
        views.Settlement_hierarchyUpdateView.as_view(),
        name="settlement_hierarchy-update",
    ),
    path(
        "settlement_hierarchy/<int:pk>/delete/",
        views.Settlement_hierarchyDeleteView.as_view(),
        name="settlement_hierarchy-delete",
    ),
    path(
        "settlement_hierarchydownload/",
        downloads.settlement_hierarchy_download_view,
        name="settlement_hierarchy-download",
    ),
    path(
        "settlement_hierarchymetadownload/",
        downloads.settlement_hierarchy_meta_download_view,
        name="settlement_hierarchy-metadownload",
    ),
    path(
        "administrative_level/create/",
        views.Administrative_levelCreateView.as_view(),
        name="administrative_level-create",
    ),
    path(
        "administrative_levels/",
        views.Administrative_levelListView.as_view(),
        name="administrative_levels",
    ),
    path(
        "administrative_levels_all/",
        views.Administrative_levelListAllView.as_view(),
        name="administrative_levels_all",
    ),
    path(
        "administrative_level/<int:pk>",
        views.Administrative_levelDetailView.as_view(),
        name="administrative_level-detail",
    ),
    path(
        "administrative_level/<int:pk>/update/",
        views.Administrative_levelUpdateView.as_view(),
        name="administrative_level-update",
    ),
    path(
        "administrative_level/<int:pk>/delete/",
        views.Administrative_levelDeleteView.as_view(),
        name="administrative_level-delete",
    ),
    path(
        "administrative_leveldownload/",
        downloads.administrative_level_download_view,
        name="administrative_level-download",
    ),
    path(
        "administrative_levelmetadownload/",
        downloads.administrative_level_meta_download_view,
        name="administrative_level-metadownload",
    ),
    path(
        "religious_level/create/",
        views.Religious_levelCreateView.as_view(),
        name="religious_level-create",
    ),
    path(
        "religious_levels/",
        views.Religious_levelListView.as_view(),
        name="religious_levels",
    ),
    path(
        "religious_levels_all/",
        views.Religious_levelListAllView.as_view(),
        name="religious_levels_all",
    ),
    path(
        "religious_level/<int:pk>",
        views.Religious_levelDetailView.as_view(),
        name="religious_level-detail",
    ),
    path(
        "religious_level/<int:pk>/update/",
        views.Religious_levelUpdateView.as_view(),
        name="religious_level-update",
    ),
    path(
        "religious_level/<int:pk>/delete/",
        views.Religious_levelDeleteView.as_view(),
        name="religious_level-delete",
    ),
    path(
        "religious_leveldownload/",
        downloads.religious_level_download_view,
        name="religious_level-download",
    ),
    path(
        "religious_levelmetadownload/",
        downloads.religious_level_meta_download_view,
        name="religious_level-metadownload",
    ),
    # TODO: testing the below commented out as we have it defined automatically below
    # path(
    #     "military_level/create/",
    #     views.Military_levelCreateView.as_view(),
    #     name="military_level-create",
    # ),
    # path(
    #     "military_levels/",
    #     views.Military_levelListView.as_view(),
    #     name="military_levels",
    # ),
    # path(
    #     "military_level/<int:pk>",
    #     views.Military_levelDetailView.as_view(),
    #     name="military_level-detail",
    # ),
    # path(
    #     "military_level/<int:pk>/update/",
    #     views.Military_levelUpdateView.as_view(),
    #     name="military_level-update",
    # ),
    # path(
    #     "military_level/<int:pk>/delete/",
    #     views.Military_levelDeleteView.as_view(),
    #     name="military_level-delete",
    # ),
    # path(
    #     "military_leveldownload/",
    #     downloads.military_level_download_view,
    #     name="military_level-download",
    # ),
    # path(
    #     "military_levelmetadownload/",
    #     downloads.military_level_meta_download_view,
    #     name="military_level-metadownload",
    # ),
    path(
        "professional_military_officer/create/",
        views.Professional_military_officerCreateView.as_view(),
        name="professional_military_officer-create",
    ),
    path(
        "professional_military_officers/",
        views.Professional_military_officerListView.as_view(),
        name="professional_military_officers",
    ),
    path(
        "professional_military_officers_all/",
        views.Professional_military_officerListAllView.as_view(),
        name="professional_military_officers_all",
    ),
    path(
        "professional_military_officer/<int:pk>",
        views.Professional_military_officerDetailView.as_view(),
        name="professional_military_officer-detail",
    ),
    path(
        "professional_military_officer/<int:pk>/update/",
        views.Professional_military_officerUpdateView.as_view(),
        name="professional_military_officer-update",
    ),
    path(
        "professional_military_officer/<int:pk>/delete/",
        views.Professional_military_officerDeleteView.as_view(),
        name="professional_military_officer-delete",
    ),
    path(
        "professional_military_officerdownload/",
        downloads.professional_military_officer_download_view,
        name="professional_military_officer-download",
    ),
    path(
        "professional_military_officermetadownload/",
        downloads.professional_military_officer_meta_download_view,
        name="professional_military_officer-metadownload",
    ),
    path(
        "professional_soldier/create/",
        views.Professional_soldierCreateView.as_view(),
        name="professional_soldier-create",
    ),
    path(
        "professional_soldiers/",
        views.Professional_soldierListView.as_view(),
        name="professional_soldiers",
    ),
    path(
        "professional_soldiers_all/",
        views.Professional_soldierListAllView.as_view(),
        name="professional_soldiers_all",
    ),
    path(
        "professional_soldier/<int:pk>",
        views.Professional_soldierDetailView.as_view(),
        name="professional_soldier-detail",
    ),
    path(
        "professional_soldier/<int:pk>/update/",
        views.Professional_soldierUpdateView.as_view(),
        name="professional_soldier-update",
    ),
    path(
        "professional_soldier/<int:pk>/delete/",
        views.Professional_soldierDeleteView.as_view(),
        name="professional_soldier-delete",
    ),
    path(
        "professional_soldierdownload/",
        downloads.professional_soldier_download_view,
        name="professional_soldier-download",
    ),
    path(
        "professional_soldiermetadownload/",
        downloads.professional_soldier_meta_download_view,
        name="professional_soldier-metadownload",
    ),
    path(
        "professional_priesthood/create/",
        views.Professional_priesthoodCreateView.as_view(),
        name="professional_priesthood-create",
    ),
    path(
        "professional_priesthoods/",
        views.Professional_priesthoodListView.as_view(),
        name="professional_priesthoods",
    ),
    path(
        "professional_priesthoods_all/",
        views.Professional_priesthoodListAllView.as_view(),
        name="professional_priesthoods_all",
    ),
    path(
        "professional_priesthood/<int:pk>",
        views.Professional_priesthoodDetailView.as_view(),
        name="professional_priesthood-detail",
    ),
    path(
        "professional_priesthood/<int:pk>/update/",
        views.Professional_priesthoodUpdateView.as_view(),
        name="professional_priesthood-update",
    ),
    path(
        "professional_priesthood/<int:pk>/delete/",
        views.Professional_priesthoodDeleteView.as_view(),
        name="professional_priesthood-delete",
    ),
    path(
        "professional_priesthooddownload/",
        downloads.professional_priesthood_download_view,
        name="professional_priesthood-download",
    ),
    path(
        "professional_priesthoodmetadownload/",
        downloads.professional_priesthood_meta_download_view,
        name="professional_priesthood-metadownload",
    ),
    path(
        "full_time_bureaucrat/create/",
        views.Full_time_bureaucratCreateView.as_view(),
        name="full_time_bureaucrat-create",
    ),
    path(
        "full_time_bureaucrats/",
        views.Full_time_bureaucratListView.as_view(),
        name="full_time_bureaucrats",
    ),
    path(
        "full_time_bureaucrats_all/",
        views.Full_time_bureaucratListAllView.as_view(),
        name="full_time_bureaucrats_all",
    ),
    path(
        "full_time_bureaucrat/<int:pk>",
        views.Full_time_bureaucratDetailView.as_view(),
        name="full_time_bureaucrat-detail",
    ),
    path(
        "full_time_bureaucrat/<int:pk>/update/",
        views.Full_time_bureaucratUpdateView.as_view(),
        name="full_time_bureaucrat-update",
    ),
    path(
        "full_time_bureaucrat/<int:pk>/delete/",
        views.Full_time_bureaucratDeleteView.as_view(),
        name="full_time_bureaucrat-delete",
    ),
    path(
        "full_time_bureaucratdownload/",
        downloads.full_time_bureaucrat_download_view,
        name="full_time_bureaucrat-download",
    ),
    path(
        "full_time_bureaucratmetadownload/",
        downloads.full_time_bureaucrat_meta_download_view,
        name="full_time_bureaucrat-metadownload",
    ),
    path(
        "examination_system/create/",
        views.Examination_systemCreateView.as_view(),
        name="examination_system-create",
    ),
    path(
        "examination_systems/",
        views.Examination_systemListView.as_view(),
        name="examination_systems",
    ),
    path(
        "examination_systems_all/",
        views.Examination_systemListAllView.as_view(),
        name="examination_systems_all",
    ),
    path(
        "examination_system/<int:pk>",
        views.Examination_systemDetailView.as_view(),
        name="examination_system-detail",
    ),
    path(
        "examination_system/<int:pk>/update/",
        views.Examination_systemUpdateView.as_view(),
        name="examination_system-update",
    ),
    path(
        "examination_system/<int:pk>/delete/",
        views.Examination_systemDeleteView.as_view(),
        name="examination_system-delete",
    ),
    path(
        "examination_systemdownload/",
        downloads.examination_system_download_view,
        name="examination_system-download",
    ),
    path(
        "examination_systemmetadownload/",
        downloads.examination_system_meta_download_view,
        name="examination_system-metadownload",
    ),
    path(
        "merit_promotion/create/",
        views.Merit_promotionCreateView.as_view(),
        name="merit_promotion-create",
    ),
    path(
        "merit_promotions/",
        views.Merit_promotionListView.as_view(),
        name="merit_promotions",
    ),
    path(
        "merit_promotions_all/",
        views.Merit_promotionListAllView.as_view(),
        name="merit_promotions_all",
    ),
    path(
        "merit_promotion/<int:pk>",
        views.Merit_promotionDetailView.as_view(),
        name="merit_promotion-detail",
    ),
    path(
        "merit_promotion/<int:pk>/update/",
        views.Merit_promotionUpdateView.as_view(),
        name="merit_promotion-update",
    ),
    path(
        "merit_promotion/<int:pk>/delete/",
        views.Merit_promotionDeleteView.as_view(),
        name="merit_promotion-delete",
    ),
    path(
        "merit_promotiondownload/",
        downloads.merit_promotion_download_view,
        name="merit_promotion-download",
    ),
    path(
        "merit_promotionmetadownload/",
        downloads.merit_promotion_meta_download_view,
        name="merit_promotion-metadownload",
    ),
    path(
        "specialized_government_building/create/",
        views.Specialized_government_buildingCreateView.as_view(),
        name="specialized_government_building-create",
    ),
    path(
        "specialized_government_buildings/",
        views.Specialized_government_buildingListView.as_view(),
        name="specialized_government_buildings",
    ),
    path(
        "specialized_government_buildings_all/",
        views.Specialized_government_buildingListAllView.as_view(),
        name="specialized_government_buildings_all",
    ),
    path(
        "specialized_government_building/<int:pk>",
        views.Specialized_government_buildingDetailView.as_view(),
        name="specialized_government_building-detail",
    ),
    path(
        "specialized_government_building/<int:pk>/update/",
        views.Specialized_government_buildingUpdateView.as_view(),
        name="specialized_government_building-update",
    ),
    path(
        "specialized_government_building/<int:pk>/delete/",
        views.Specialized_government_buildingDeleteView.as_view(),
        name="specialized_government_building-delete",
    ),
    path(
        "specialized_government_buildingdownload/",
        downloads.specialized_government_building_download_view,
        name="specialized_government_building-download",
    ),
    path(
        "specialized_government_buildingmetadownload/",
        downloads.specialized_government_building_meta_download_view,
        name="specialized_government_building-metadownload",
    ),
    path(
        "formal_legal_code/create/",
        views.Formal_legal_codeCreateView.as_view(),
        name="formal_legal_code-create",
    ),
    path(
        "formal_legal_codes/",
        views.Formal_legal_codeListView.as_view(),
        name="formal_legal_codes",
    ),
    path(
        "formal_legal_codes_all/",
        views.Formal_legal_codeListAllView.as_view(),
        name="formal_legal_codes_all",
    ),
    path(
        "formal_legal_code/<int:pk>",
        views.Formal_legal_codeDetailView.as_view(),
        name="formal_legal_code-detail",
    ),
    path(
        "formal_legal_code/<int:pk>/update/",
        views.Formal_legal_codeUpdateView.as_view(),
        name="formal_legal_code-update",
    ),
    path(
        "formal_legal_code/<int:pk>/delete/",
        views.Formal_legal_codeDeleteView.as_view(),
        name="formal_legal_code-delete",
    ),
    path(
        "formal_legal_codedownload/",
        downloads.formal_legal_code_download_view,
        name="formal_legal_code-download",
    ),
    path(
        "formal_legal_codemetadownload/",
        downloads.formal_legal_code_meta_download_view,
        name="formal_legal_code-metadownload",
    ),
    path(
        "judge/create/", views.JudgeCreateView.as_view(), name="judge-create"
    ),
    path("judges/", views.JudgeListView.as_view(), name="judges"),
    path("judges_all/", views.JudgeListAllView.as_view(), name="judges_all"),
    path(
        "judge/<int:pk>", views.JudgeDetailView.as_view(), name="judge-detail"
    ),
    path(
        "judge/<int:pk>/update/",
        views.JudgeUpdateView.as_view(),
        name="judge-update",
    ),
    path(
        "judge/<int:pk>/delete/",
        views.JudgeDeleteView.as_view(),
        name="judge-delete",
    ),
    path(
        "judgedownload/", downloads.judge_download_view, name="judge-download"
    ),
    path(
        "judgemetadownload/",
        downloads.judge_meta_download_view,
        name="judge-metadownload",
    ),
    path(
        "court/create/", views.CourtCreateView.as_view(), name="court-create"
    ),
    path("courts/", views.CourtListView.as_view(), name="courts"),
    path("courts_all/", views.CourtListAllView.as_view(), name="courts_all"),
    path(
        "court/<int:pk>", views.CourtDetailView.as_view(), name="court-detail"
    ),
    path(
        "court/<int:pk>/update/",
        views.CourtUpdateView.as_view(),
        name="court-update",
    ),
    path(
        "court/<int:pk>/delete/",
        views.CourtDeleteView.as_view(),
        name="court-delete",
    ),
    path(
        "courtdownload/", downloads.court_download_view, name="court-download"
    ),
    path(
        "courtmetadownload/",
        downloads.court_meta_download_view,
        name="court-metadownload",
    ),
    path(
        "professional_lawyer/create/",
        views.Professional_lawyerCreateView.as_view(),
        name="professional_lawyer-create",
    ),
    path(
        "professional_lawyers/",
        views.Professional_lawyerListView.as_view(),
        name="professional_lawyers",
    ),
    path(
        "professional_lawyers_all/",
        views.Professional_lawyerListAllView.as_view(),
        name="professional_lawyers_all",
    ),
    path(
        "professional_lawyer/<int:pk>",
        views.Professional_lawyerDetailView.as_view(),
        name="professional_lawyer-detail",
    ),
    path(
        "professional_lawyer/<int:pk>/update/",
        views.Professional_lawyerUpdateView.as_view(),
        name="professional_lawyer-update",
    ),
    path(
        "professional_lawyer/<int:pk>/delete/",
        views.Professional_lawyerDeleteView.as_view(),
        name="professional_lawyer-delete",
    ),
    path(
        "professional_lawyerdownload/",
        downloads.professional_lawyer_download_view,
        name="professional_lawyer-download",
    ),
    path(
        "professional_lawyermetadownload/",
        downloads.professional_lawyer_meta_download_view,
        name="professional_lawyer-metadownload",
    ),
    path(
        "irrigation_system/create/",
        views.Irrigation_systemCreateView.as_view(),
        name="irrigation_system-create",
    ),
    path(
        "irrigation_systems/",
        views.Irrigation_systemListView.as_view(),
        name="irrigation_systems",
    ),
    path(
        "irrigation_systems_all/",
        views.Irrigation_systemListAllView.as_view(),
        name="irrigation_systems_all",
    ),
    path(
        "irrigation_system/<int:pk>",
        views.Irrigation_systemDetailView.as_view(),
        name="irrigation_system-detail",
    ),
    path(
        "irrigation_system/<int:pk>/update/",
        views.Irrigation_systemUpdateView.as_view(),
        name="irrigation_system-update",
    ),
    path(
        "irrigation_system/<int:pk>/delete/",
        views.Irrigation_systemDeleteView.as_view(),
        name="irrigation_system-delete",
    ),
    path(
        "irrigation_systemdownload/",
        downloads.irrigation_system_download_view,
        name="irrigation_system-download",
    ),
    path(
        "irrigation_systemmetadownload/",
        downloads.irrigation_system_meta_download_view,
        name="irrigation_system-metadownload",
    ),
    path(
        "drinking_water_supply_system/create/",
        views.Drinking_water_supply_systemCreateView.as_view(),
        name="drinking_water_supply_system-create",
    ),
    path(
        "drinking_water_supply_systems/",
        views.Drinking_water_supply_systemListView.as_view(),
        name="drinking_water_supply_systems",
    ),
    path(
        "drinking_water_supply_systems_all/",
        views.Drinking_water_supply_systemListAllView.as_view(),
        name="drinking_water_supply_systems_all",
    ),
    path(
        "drinking_water_supply_system/<int:pk>",
        views.Drinking_water_supply_systemDetailView.as_view(),
        name="drinking_water_supply_system-detail",
    ),
    path(
        "drinking_water_supply_system/<int:pk>/update/",
        views.Drinking_water_supply_systemUpdateView.as_view(),
        name="drinking_water_supply_system-update",
    ),
    path(
        "drinking_water_supply_system/<int:pk>/delete/",
        views.Drinking_water_supply_systemDeleteView.as_view(),
        name="drinking_water_supply_system-delete",
    ),
    path(
        "drinking_water_supply_systemdownload/",
        downloads.drinking_water_supply_system_download_view,
        name="drinking_water_supply_system-download",
    ),
    path(
        "drinking_water_supply_systemmetadownload/",
        downloads.drinking_water_supply_system_meta_download_view,
        name="drinking_water_supply_system-metadownload",
    ),
    path(
        "market/create/",
        views.MarketCreateView.as_view(),
        name="market-create",
    ),
    path("markets/", views.MarketListView.as_view(), name="markets"),
    path(
        "markets_all/", views.MarketListAllView.as_view(), name="markets_all"
    ),
    path(
        "market/<int:pk>",
        views.MarketDetailView.as_view(),
        name="market-detail",
    ),
    path(
        "market/<int:pk>/update/",
        views.MarketUpdateView.as_view(),
        name="market-update",
    ),
    path(
        "market/<int:pk>/delete/",
        views.MarketDeleteView.as_view(),
        name="market-delete",
    ),
    path(
        "marketdownload/",
        downloads.market_download_view,
        name="market-download",
    ),
    path(
        "marketmetadownload/",
        downloads.market_meta_download_view,
        name="market-metadownload",
    ),
    path(
        "food_storage_site/create/",
        views.Food_storage_siteCreateView.as_view(),
        name="food_storage_site-create",
    ),
    path(
        "food_storage_sites/",
        views.Food_storage_siteListView.as_view(),
        name="food_storage_sites",
    ),
    path(
        "food_storage_sites_all/",
        views.Food_storage_siteListAllView.as_view(),
        name="food_storage_sites_all",
    ),
    path(
        "food_storage_site/<int:pk>",
        views.Food_storage_siteDetailView.as_view(),
        name="food_storage_site-detail",
    ),
    path(
        "food_storage_site/<int:pk>/update/",
        views.Food_storage_siteUpdateView.as_view(),
        name="food_storage_site-update",
    ),
    path(
        "food_storage_site/<int:pk>/delete/",
        views.Food_storage_siteDeleteView.as_view(),
        name="food_storage_site-delete",
    ),
    path(
        "food_storage_sitedownload/",
        downloads.food_storage_site_download_view,
        name="food_storage_site-download",
    ),
    path(
        "food_storage_sitemetadownload/",
        downloads.food_storage_site_meta_download_view,
        name="food_storage_site-metadownload",
    ),
    path("road/create/", views.RoadCreateView.as_view(), name="road-create"),
    path("roads/", views.RoadListView.as_view(), name="roads"),
    path("roads_all/", views.RoadListAllView.as_view(), name="roads_all"),
    path("road/<int:pk>", views.RoadDetailView.as_view(), name="road-detail"),
    path(
        "road/<int:pk>/update/",
        views.RoadUpdateView.as_view(),
        name="road-update",
    ),
    path(
        "road/<int:pk>/delete/",
        views.RoadDeleteView.as_view(),
        name="road-delete",
    ),
    path("roaddownload/", downloads.road_download_view, name="road-download"),
    path(
        "roadmetadownload/",
        downloads.road_meta_download_view,
        name="road-metadownload",
    ),
    path(
        "bridge/create/",
        views.BridgeCreateView.as_view(),
        name="bridge-create",
    ),
    path("bridges/", views.BridgeListView.as_view(), name="bridges"),
    path(
        "bridges_all/", views.BridgeListAllView.as_view(), name="bridges_all"
    ),
    path(
        "bridge/<int:pk>",
        views.BridgeDetailView.as_view(),
        name="bridge-detail",
    ),
    path(
        "bridge/<int:pk>/update/",
        views.BridgeUpdateView.as_view(),
        name="bridge-update",
    ),
    path(
        "bridge/<int:pk>/delete/",
        views.BridgeDeleteView.as_view(),
        name="bridge-delete",
    ),
    path(
        "bridgedownload/",
        downloads.bridge_download_view,
        name="bridge-download",
    ),
    path(
        "bridgemetadownload/",
        downloads.bridge_meta_download_view,
        name="bridge-metadownload",
    ),
    path(
        "canal/create/", views.CanalCreateView.as_view(), name="canal-create"
    ),
    path("canals/", views.CanalListView.as_view(), name="canals"),
    path("canals_all/", views.CanalListAllView.as_view(), name="canals_all"),
    path(
        "canal/<int:pk>", views.CanalDetailView.as_view(), name="canal-detail"
    ),
    path(
        "canal/<int:pk>/update/",
        views.CanalUpdateView.as_view(),
        name="canal-update",
    ),
    path(
        "canal/<int:pk>/delete/",
        views.CanalDeleteView.as_view(),
        name="canal-delete",
    ),
    path(
        "canaldownload/", downloads.canal_download_view, name="canal-download"
    ),
    path(
        "canalmetadownload/",
        downloads.canal_meta_download_view,
        name="canal-metadownload",
    ),
    path("port/create/", views.PortCreateView.as_view(), name="port-create"),
    path("ports/", views.PortListView.as_view(), name="ports"),
    path("ports_all/", views.PortListAllView.as_view(), name="ports_all"),
    path("port/<int:pk>", views.PortDetailView.as_view(), name="port-detail"),
    path(
        "port/<int:pk>/update/",
        views.PortUpdateView.as_view(),
        name="port-update",
    ),
    path(
        "port/<int:pk>/delete/",
        views.PortDeleteView.as_view(),
        name="port-delete",
    ),
    path("portdownload/", downloads.port_download_view, name="port-download"),
    path(
        "portmetadownload/",
        downloads.port_meta_download_view,
        name="port-metadownload",
    ),
    path(
        "mines_or_quarry/create/",
        views.Mines_or_quarryCreateView.as_view(),
        name="mines_or_quarry-create",
    ),
    path(
        "mines_or_quarrys/",
        views.Mines_or_quarryListView.as_view(),
        name="mines_or_quarrys",
    ),
    path(
        "mines_or_quarrys_all/",
        views.Mines_or_quarryListAllView.as_view(),
        name="mines_or_quarrys_all",
    ),
    path(
        "mines_or_quarry/<int:pk>",
        views.Mines_or_quarryDetailView.as_view(),
        name="mines_or_quarry-detail",
    ),
    path(
        "mines_or_quarry/<int:pk>/update/",
        views.Mines_or_quarryUpdateView.as_view(),
        name="mines_or_quarry-update",
    ),
    path(
        "mines_or_quarry/<int:pk>/delete/",
        views.Mines_or_quarryDeleteView.as_view(),
        name="mines_or_quarry-delete",
    ),
    path(
        "mines_or_quarrydownload/",
        downloads.mines_or_quarry_download_view,
        name="mines_or_quarry-download",
    ),
    path(
        "mines_or_quarrymetadownload/",
        downloads.mines_or_quarry_meta_download_view,
        name="mines_or_quarry-metadownload",
    ),
    path(
        "mnemonic_device/create/",
        views.Mnemonic_deviceCreateView.as_view(),
        name="mnemonic_device-create",
    ),
    path(
        "mnemonic_devices/",
        views.Mnemonic_deviceListView.as_view(),
        name="mnemonic_devices",
    ),
    path(
        "mnemonic_devices_all/",
        views.Mnemonic_deviceListAllView.as_view(),
        name="mnemonic_devices_all",
    ),
    path(
        "mnemonic_device/<int:pk>",
        views.Mnemonic_deviceDetailView.as_view(),
        name="mnemonic_device-detail",
    ),
    path(
        "mnemonic_device/<int:pk>/update/",
        views.Mnemonic_deviceUpdateView.as_view(),
        name="mnemonic_device-update",
    ),
    path(
        "mnemonic_device/<int:pk>/delete/",
        views.Mnemonic_deviceDeleteView.as_view(),
        name="mnemonic_device-delete",
    ),
    path(
        "mnemonic_devicedownload/",
        downloads.mnemonic_device_download_view,
        name="mnemonic_device-download",
    ),
    path(
        "mnemonic_devicemetadownload/",
        downloads.mnemonic_device_meta_download_view,
        name="mnemonic_device-metadownload",
    ),
    path(
        "nonwritten_record/create/",
        views.Nonwritten_recordCreateView.as_view(),
        name="nonwritten_record-create",
    ),
    path(
        "nonwritten_records/",
        views.Nonwritten_recordListView.as_view(),
        name="nonwritten_records",
    ),
    path(
        "nonwritten_records_all/",
        views.Nonwritten_recordListAllView.as_view(),
        name="nonwritten_records_all",
    ),
    path(
        "nonwritten_record/<int:pk>",
        views.Nonwritten_recordDetailView.as_view(),
        name="nonwritten_record-detail",
    ),
    path(
        "nonwritten_record/<int:pk>/update/",
        views.Nonwritten_recordUpdateView.as_view(),
        name="nonwritten_record-update",
    ),
    path(
        "nonwritten_record/<int:pk>/delete/",
        views.Nonwritten_recordDeleteView.as_view(),
        name="nonwritten_record-delete",
    ),
    path(
        "nonwritten_recorddownload/",
        downloads.nonwritten_record_download_view,
        name="nonwritten_record-download",
    ),
    path(
        "nonwritten_recordmetadownload/",
        downloads.nonwritten_record_meta_download_view,
        name="nonwritten_record-metadownload",
    ),
    path(
        "written_record/create/",
        views.Written_recordCreateView.as_view(),
        name="written_record-create",
    ),
    path(
        "written_records/",
        views.Written_recordListView.as_view(),
        name="written_records",
    ),
    path(
        "written_records_all/",
        views.Written_recordListAllView.as_view(),
        name="written_records_all",
    ),
    path(
        "written_record/<int:pk>",
        views.Written_recordDetailView.as_view(),
        name="written_record-detail",
    ),
    path(
        "written_record/<int:pk>/update/",
        views.Written_recordUpdateView.as_view(),
        name="written_record-update",
    ),
    path(
        "written_record/<int:pk>/delete/",
        views.Written_recordDeleteView.as_view(),
        name="written_record-delete",
    ),
    path(
        "written_recorddownload/",
        downloads.written_record_download_view,
        name="written_record-download",
    ),
    path(
        "written_recordmetadownload/",
        downloads.written_record_meta_download_view,
        name="written_record-metadownload",
    ),
    path(
        "script/create/",
        views.ScriptCreateView.as_view(),
        name="script-create",
    ),
    path("scripts/", views.ScriptListView.as_view(), name="scripts"),
    path(
        "scripts_all/", views.ScriptListAllView.as_view(), name="scripts_all"
    ),
    path(
        "script/<int:pk>",
        views.ScriptDetailView.as_view(),
        name="script-detail",
    ),
    path(
        "script/<int:pk>/update/",
        views.ScriptUpdateView.as_view(),
        name="script-update",
    ),
    path(
        "script/<int:pk>/delete/",
        views.ScriptDeleteView.as_view(),
        name="script-delete",
    ),
    path(
        "scriptdownload/",
        downloads.script_download_view,
        name="script-download",
    ),
    path(
        "scriptmetadownload/",
        downloads.script_meta_download_view,
        name="script-metadownload",
    ),
    path(
        "non_phonetic_writing/create/",
        views.Non_phonetic_writingCreateView.as_view(),
        name="non_phonetic_writing-create",
    ),
    path(
        "non_phonetic_writings/",
        views.Non_phonetic_writingListView.as_view(),
        name="non_phonetic_writings",
    ),
    path(
        "non_phonetic_writings_all/",
        views.Non_phonetic_writingListAllView.as_view(),
        name="non_phonetic_writings_all",
    ),
    path(
        "non_phonetic_writing/<int:pk>",
        views.Non_phonetic_writingDetailView.as_view(),
        name="non_phonetic_writing-detail",
    ),
    path(
        "non_phonetic_writing/<int:pk>/update/",
        views.Non_phonetic_writingUpdateView.as_view(),
        name="non_phonetic_writing-update",
    ),
    path(
        "non_phonetic_writing/<int:pk>/delete/",
        views.Non_phonetic_writingDeleteView.as_view(),
        name="non_phonetic_writing-delete",
    ),
    path(
        "non_phonetic_writingdownload/",
        downloads.non_phonetic_writing_download_view,
        name="non_phonetic_writing-download",
    ),
    path(
        "non_phonetic_writingmetadownload/",
        downloads.non_phonetic_writing_meta_download_view,
        name="non_phonetic_writing-metadownload",
    ),
    path(
        "phonetic_alphabetic_writing/create/",
        views.Phonetic_alphabetic_writingCreateView.as_view(),
        name="phonetic_alphabetic_writing-create",
    ),
    path(
        "phonetic_alphabetic_writings/",
        views.Phonetic_alphabetic_writingListView.as_view(),
        name="phonetic_alphabetic_writings",
    ),
    path(
        "phonetic_alphabetic_writings_all/",
        views.Phonetic_alphabetic_writingListAllView.as_view(),
        name="phonetic_alphabetic_writings_all",
    ),
    path(
        "phonetic_alphabetic_writing/<int:pk>",
        views.Phonetic_alphabetic_writingDetailView.as_view(),
        name="phonetic_alphabetic_writing-detail",
    ),
    path(
        "phonetic_alphabetic_writing/<int:pk>/update/",
        views.Phonetic_alphabetic_writingUpdateView.as_view(),
        name="phonetic_alphabetic_writing-update",
    ),
    path(
        "phonetic_alphabetic_writing/<int:pk>/delete/",
        views.Phonetic_alphabetic_writingDeleteView.as_view(),
        name="phonetic_alphabetic_writing-delete",
    ),
    path(
        "phonetic_alphabetic_writingdownload/",
        downloads.phonetic_alphabetic_writing_download_view,
        name="phonetic_alphabetic_writing-download",
    ),
    path(
        "phonetic_alphabetic_writingmetadownload/",
        downloads.phonetic_alphabetic_writing_meta_download_view,
        name="phonetic_alphabetic_writing-metadownload",
    ),
    path(
        "lists_tables_and_classification/create/",
        views.Lists_tables_and_classificationCreateView.as_view(),
        name="lists_tables_and_classification-create",
    ),
    path(
        "lists_tables_and_classifications/",
        views.Lists_tables_and_classificationListView.as_view(),
        name="lists_tables_and_classifications",
    ),
    path(
        "lists_tables_and_classifications_all/",
        views.Lists_tables_and_classificationListAllView.as_view(),
        name="lists_tables_and_classifications_all",
    ),
    path(
        "lists_tables_and_classification/<int:pk>",
        views.Lists_tables_and_classificationDetailView.as_view(),
        name="lists_tables_and_classification-detail",
    ),
    path(
        "lists_tables_and_classification/<int:pk>/update/",
        views.Lists_tables_and_classificationUpdateView.as_view(),
        name="lists_tables_and_classification-update",
    ),
    path(
        "lists_tables_and_classification/<int:pk>/delete/",
        views.Lists_tables_and_classificationDeleteView.as_view(),
        name="lists_tables_and_classification-delete",
    ),
    path(
        "lists_tables_and_classificationdownload/",
        downloads.lists_tables_and_classification_download_view,
        name="lists_tables_and_classification-download",
    ),
    path(
        "lists_tables_and_classificationmetadownload/",
        downloads.lists_tables_and_classification_meta_download_view,
        name="lists_tables_and_classification-metadownload",
    ),
    path(
        "calendar/create/",
        views.CalendarCreateView.as_view(),
        name="calendar-create",
    ),
    path("calendars/", views.CalendarListView.as_view(), name="calendars"),
    path(
        "calendars_all/",
        views.CalendarListAllView.as_view(),
        name="calendars_all",
    ),
    path(
        "calendar/<int:pk>",
        views.CalendarDetailView.as_view(),
        name="calendar-detail",
    ),
    path(
        "calendar/<int:pk>/update/",
        views.CalendarUpdateView.as_view(),
        name="calendar-update",
    ),
    path(
        "calendar/<int:pk>/delete/",
        views.CalendarDeleteView.as_view(),
        name="calendar-delete",
    ),
    path(
        "calendardownload/",
        downloads.calendar_download_view,
        name="calendar-download",
    ),
    path(
        "calendarmetadownload/",
        downloads.calendar_meta_download_view,
        name="calendar-metadownload",
    ),
    path(
        "sacred_text/create/",
        views.Sacred_textCreateView.as_view(),
        name="sacred_text-create",
    ),
    path(
        "sacred_texts/",
        views.Sacred_textListView.as_view(),
        name="sacred_texts",
    ),
    path(
        "sacred_texts_all/",
        views.Sacred_textListAllView.as_view(),
        name="sacred_texts_all",
    ),
    path(
        "sacred_text/<int:pk>",
        views.Sacred_textDetailView.as_view(),
        name="sacred_text-detail",
    ),
    path(
        "sacred_text/<int:pk>/update/",
        views.Sacred_textUpdateView.as_view(),
        name="sacred_text-update",
    ),
    path(
        "sacred_text/<int:pk>/delete/",
        views.Sacred_textDeleteView.as_view(),
        name="sacred_text-delete",
    ),
    path(
        "sacred_textdownload/",
        downloads.sacred_text_download_view,
        name="sacred_text-download",
    ),
    path(
        "sacred_textmetadownload/",
        downloads.sacred_text_meta_download_view,
        name="sacred_text-metadownload",
    ),
    path(
        "religious_literature/create/",
        views.Religious_literatureCreateView.as_view(),
        name="religious_literature-create",
    ),
    path(
        "religious_literatures/",
        views.Religious_literatureListView.as_view(),
        name="religious_literatures",
    ),
    path(
        "religious_literatures_all/",
        views.Religious_literatureListAllView.as_view(),
        name="religious_literatures_all",
    ),
    path(
        "religious_literature/<int:pk>",
        views.Religious_literatureDetailView.as_view(),
        name="religious_literature-detail",
    ),
    path(
        "religious_literature/<int:pk>/update/",
        views.Religious_literatureUpdateView.as_view(),
        name="religious_literature-update",
    ),
    path(
        "religious_literature/<int:pk>/delete/",
        views.Religious_literatureDeleteView.as_view(),
        name="religious_literature-delete",
    ),
    path(
        "religious_literaturedownload/",
        downloads.religious_literature_download_view,
        name="religious_literature-download",
    ),
    path(
        "religious_literaturemetadownload/",
        downloads.religious_literature_meta_download_view,
        name="religious_literature-metadownload",
    ),
    path(
        "practical_literature/create/",
        views.Practical_literatureCreateView.as_view(),
        name="practical_literature-create",
    ),
    path(
        "practical_literatures/",
        views.Practical_literatureListView.as_view(),
        name="practical_literatures",
    ),
    path(
        "practical_literatures_all/",
        views.Practical_literatureListAllView.as_view(),
        name="practical_literatures_all",
    ),
    path(
        "practical_literature/<int:pk>",
        views.Practical_literatureDetailView.as_view(),
        name="practical_literature-detail",
    ),
    path(
        "practical_literature/<int:pk>/update/",
        views.Practical_literatureUpdateView.as_view(),
        name="practical_literature-update",
    ),
    path(
        "practical_literature/<int:pk>/delete/",
        views.Practical_literatureDeleteView.as_view(),
        name="practical_literature-delete",
    ),
    path(
        "practical_literaturedownload/",
        downloads.practical_literature_download_view,
        name="practical_literature-download",
    ),
    path(
        "practical_literaturemetadownload/",
        downloads.practical_literature_meta_download_view,
        name="practical_literature-metadownload",
    ),
    path(
        "history/create/",
        views.HistoryCreateView.as_view(),
        name="history-create",
    ),
    path("historys/", views.HistoryListView.as_view(), name="historys"),
    path(
        "historys_all/",
        views.HistoryListAllView.as_view(),
        name="historys_all",
    ),
    path(
        "history/<int:pk>",
        views.HistoryDetailView.as_view(),
        name="history-detail",
    ),
    path(
        "history/<int:pk>/update/",
        views.HistoryUpdateView.as_view(),
        name="history-update",
    ),
    path(
        "history/<int:pk>/delete/",
        views.HistoryDeleteView.as_view(),
        name="history-delete",
    ),
    path(
        "historydownload/",
        downloads.history_download_view,
        name="history-download",
    ),
    path(
        "historymetadownload/",
        downloads.history_meta_download_view,
        name="history-metadownload",
    ),
    path(
        "philosophy/create/",
        views.PhilosophyCreateView.as_view(),
        name="philosophy-create",
    ),
    path(
        "philosophys/", views.PhilosophyListView.as_view(), name="philosophys"
    ),
    path(
        "philosophys_all/",
        views.PhilosophyListAllView.as_view(),
        name="philosophys_all",
    ),
    path(
        "philosophy/<int:pk>",
        views.PhilosophyDetailView.as_view(),
        name="philosophy-detail",
    ),
    path(
        "philosophy/<int:pk>/update/",
        views.PhilosophyUpdateView.as_view(),
        name="philosophy-update",
    ),
    path(
        "philosophy/<int:pk>/delete/",
        views.PhilosophyDeleteView.as_view(),
        name="philosophy-delete",
    ),
    path(
        "philosophydownload/",
        downloads.philosophy_download_view,
        name="philosophy-download",
    ),
    path(
        "philosophymetadownload/",
        downloads.philosophy_meta_download_view,
        name="philosophy-metadownload",
    ),
    path(
        "scientific_literature/create/",
        views.Scientific_literatureCreateView.as_view(),
        name="scientific_literature-create",
    ),
    path(
        "scientific_literatures/",
        views.Scientific_literatureListView.as_view(),
        name="scientific_literatures",
    ),
    path(
        "scientific_literatures_all/",
        views.Scientific_literatureListAllView.as_view(),
        name="scientific_literatures_all",
    ),
    path(
        "scientific_literature/<int:pk>",
        views.Scientific_literatureDetailView.as_view(),
        name="scientific_literature-detail",
    ),
    path(
        "scientific_literature/<int:pk>/update/",
        views.Scientific_literatureUpdateView.as_view(),
        name="scientific_literature-update",
    ),
    path(
        "scientific_literature/<int:pk>/delete/",
        views.Scientific_literatureDeleteView.as_view(),
        name="scientific_literature-delete",
    ),
    path(
        "scientific_literaturedownload/",
        downloads.scientific_literature_download_view,
        name="scientific_literature-download",
    ),
    path(
        "scientific_literaturemetadownload/",
        downloads.scientific_literature_meta_download_view,
        name="scientific_literature-metadownload",
    ),
    path(
        "fiction/create/",
        views.FictionCreateView.as_view(),
        name="fiction-create",
    ),
    path("fictions/", views.FictionListView.as_view(), name="fictions"),
    path(
        "fictions_all/",
        views.FictionListAllView.as_view(),
        name="fictions_all",
    ),
    path(
        "fiction/<int:pk>",
        views.FictionDetailView.as_view(),
        name="fiction-detail",
    ),
    path(
        "fiction/<int:pk>/update/",
        views.FictionUpdateView.as_view(),
        name="fiction-update",
    ),
    path(
        "fiction/<int:pk>/delete/",
        views.FictionDeleteView.as_view(),
        name="fiction-delete",
    ),
    path(
        "fictiondownload/",
        downloads.fiction_download_view,
        name="fiction-download",
    ),
    path(
        "fictionmetadownload/",
        downloads.fiction_meta_download_view,
        name="fiction-metadownload",
    ),
    path(
        "article/create/",
        views.ArticleCreateView.as_view(),
        name="article-create",
    ),
    path("articles/", views.ArticleListView.as_view(), name="articles"),
    path(
        "articles_all/",
        views.ArticleListAllView.as_view(),
        name="articles_all",
    ),
    path(
        "article/<int:pk>",
        views.ArticleDetailView.as_view(),
        name="article-detail",
    ),
    path(
        "article/<int:pk>/update/",
        views.ArticleUpdateView.as_view(),
        name="article-update",
    ),
    path(
        "article/<int:pk>/delete/",
        views.ArticleDeleteView.as_view(),
        name="article-delete",
    ),
    path(
        "articledownload/",
        downloads.article_download_view,
        name="article-download",
    ),
    path(
        "articlemetadownload/",
        downloads.article_meta_download_view,
        name="article-metadownload",
    ),
    path(
        "token/create/", views.TokenCreateView.as_view(), name="token-create"
    ),
    path("tokens/", views.TokenListView.as_view(), name="tokens"),
    path("tokens_all/", views.TokenListAllView.as_view(), name="tokens_all"),
    path(
        "token/<int:pk>", views.TokenDetailView.as_view(), name="token-detail"
    ),
    path(
        "token/<int:pk>/update/",
        views.TokenUpdateView.as_view(),
        name="token-update",
    ),
    path(
        "token/<int:pk>/delete/",
        views.TokenDeleteView.as_view(),
        name="token-delete",
    ),
    path(
        "tokendownload/", downloads.token_download_view, name="token-download"
    ),
    path(
        "tokenmetadownload/",
        downloads.token_meta_download_view,
        name="token-metadownload",
    ),
    path(
        "precious_metal/create/",
        views.Precious_metalCreateView.as_view(),
        name="precious_metal-create",
    ),
    path(
        "precious_metals/",
        views.Precious_metalListView.as_view(),
        name="precious_metals",
    ),
    path(
        "precious_metals_all/",
        views.Precious_metalListAllView.as_view(),
        name="precious_metals_all",
    ),
    path(
        "precious_metal/<int:pk>",
        views.Precious_metalDetailView.as_view(),
        name="precious_metal-detail",
    ),
    path(
        "precious_metal/<int:pk>/update/",
        views.Precious_metalUpdateView.as_view(),
        name="precious_metal-update",
    ),
    path(
        "precious_metal/<int:pk>/delete/",
        views.Precious_metalDeleteView.as_view(),
        name="precious_metal-delete",
    ),
    path(
        "precious_metaldownload/",
        downloads.precious_metal_download_view,
        name="precious_metal-download",
    ),
    path(
        "precious_metalmetadownload/",
        downloads.precious_metal_meta_download_view,
        name="precious_metal-metadownload",
    ),
    path(
        "foreign_coin/create/",
        views.Foreign_coinCreateView.as_view(),
        name="foreign_coin-create",
    ),
    path(
        "foreign_coins/",
        views.Foreign_coinListView.as_view(),
        name="foreign_coins",
    ),
    path(
        "foreign_coins_all/",
        views.Foreign_coinListAllView.as_view(),
        name="foreign_coins_all",
    ),
    path(
        "foreign_coin/<int:pk>",
        views.Foreign_coinDetailView.as_view(),
        name="foreign_coin-detail",
    ),
    path(
        "foreign_coin/<int:pk>/update/",
        views.Foreign_coinUpdateView.as_view(),
        name="foreign_coin-update",
    ),
    path(
        "foreign_coin/<int:pk>/delete/",
        views.Foreign_coinDeleteView.as_view(),
        name="foreign_coin-delete",
    ),
    path(
        "foreign_coindownload/",
        downloads.foreign_coin_download_view,
        name="foreign_coin-download",
    ),
    path(
        "foreign_coinmetadownload/",
        downloads.foreign_coin_meta_download_view,
        name="foreign_coin-metadownload",
    ),
    path(
        "indigenous_coin/create/",
        views.Indigenous_coinCreateView.as_view(),
        name="indigenous_coin-create",
    ),
    path(
        "indigenous_coins/",
        views.Indigenous_coinListView.as_view(),
        name="indigenous_coins",
    ),
    path(
        "indigenous_coins_all/",
        views.Indigenous_coinListAllView.as_view(),
        name="indigenous_coins_all",
    ),
    path(
        "indigenous_coin/<int:pk>",
        views.Indigenous_coinDetailView.as_view(),
        name="indigenous_coin-detail",
    ),
    path(
        "indigenous_coin/<int:pk>/update/",
        views.Indigenous_coinUpdateView.as_view(),
        name="indigenous_coin-update",
    ),
    path(
        "indigenous_coin/<int:pk>/delete/",
        views.Indigenous_coinDeleteView.as_view(),
        name="indigenous_coin-delete",
    ),
    path(
        "indigenous_coindownload/",
        downloads.indigenous_coin_download_view,
        name="indigenous_coin-download",
    ),
    path(
        "indigenous_coinmetadownload/",
        downloads.indigenous_coin_meta_download_view,
        name="indigenous_coin-metadownload",
    ),
    path(
        "paper_currency/create/",
        views.Paper_currencyCreateView.as_view(),
        name="paper_currency-create",
    ),
    path(
        "paper_currencys/",
        views.Paper_currencyListView.as_view(),
        name="paper_currencys",
    ),
    path(
        "paper_currencys_all/",
        views.Paper_currencyListAllView.as_view(),
        name="paper_currencys_all",
    ),
    path(
        "paper_currency/<int:pk>",
        views.Paper_currencyDetailView.as_view(),
        name="paper_currency-detail",
    ),
    path(
        "paper_currency/<int:pk>/update/",
        views.Paper_currencyUpdateView.as_view(),
        name="paper_currency-update",
    ),
    path(
        "paper_currency/<int:pk>/delete/",
        views.Paper_currencyDeleteView.as_view(),
        name="paper_currency-delete",
    ),
    path(
        "paper_currencydownload/",
        downloads.paper_currency_download_view,
        name="paper_currency-download",
    ),
    path(
        "paper_currencymetadownload/",
        downloads.paper_currency_meta_download_view,
        name="paper_currency-metadownload",
    ),
    path(
        "courier/create/",
        views.CourierCreateView.as_view(),
        name="courier-create",
    ),
    path("couriers/", views.CourierListView.as_view(), name="couriers"),
    path(
        "couriers_all/",
        views.CourierListAllView.as_view(),
        name="couriers_all",
    ),
    path(
        "courier/<int:pk>",
        views.CourierDetailView.as_view(),
        name="courier-detail",
    ),
    path(
        "courier/<int:pk>/update/",
        views.CourierUpdateView.as_view(),
        name="courier-update",
    ),
    path(
        "courier/<int:pk>/delete/",
        views.CourierDeleteView.as_view(),
        name="courier-delete",
    ),
    path(
        "courierdownload/",
        downloads.courier_download_view,
        name="courier-download",
    ),
    path(
        "couriermetadownload/",
        downloads.courier_meta_download_view,
        name="courier-metadownload",
    ),
    path(
        "postal_station/create/",
        views.Postal_stationCreateView.as_view(),
        name="postal_station-create",
    ),
    path(
        "postal_stations/",
        views.Postal_stationListView.as_view(),
        name="postal_stations",
    ),
    path(
        "postal_stations_all/",
        views.Postal_stationListAllView.as_view(),
        name="postal_stations_all",
    ),
    path(
        "postal_station/<int:pk>",
        views.Postal_stationDetailView.as_view(),
        name="postal_station-detail",
    ),
    path(
        "postal_station/<int:pk>/update/",
        views.Postal_stationUpdateView.as_view(),
        name="postal_station-update",
    ),
    path(
        "postal_station/<int:pk>/delete/",
        views.Postal_stationDeleteView.as_view(),
        name="postal_station-delete",
    ),
    path(
        "postal_stationdownload/",
        downloads.postal_station_download_view,
        name="postal_station-download",
    ),
    path(
        "postal_stationmetadownload/",
        downloads.postal_station_meta_download_view,
        name="postal_station-metadownload",
    ),
    path(
        "general_postal_service/create/",
        views.General_postal_serviceCreateView.as_view(),
        name="general_postal_service-create",
    ),
    path(
        "general_postal_services/",
        views.General_postal_serviceListView.as_view(),
        name="general_postal_services",
    ),
    path(
        "general_postal_services_all/",
        views.General_postal_serviceListAllView.as_view(),
        name="general_postal_services_all",
    ),
    path(
        "general_postal_service/<int:pk>",
        views.General_postal_serviceDetailView.as_view(),
        name="general_postal_service-detail",
    ),
    path(
        "general_postal_service/<int:pk>/update/",
        views.General_postal_serviceUpdateView.as_view(),
        name="general_postal_service-update",
    ),
    path(
        "general_postal_service/<int:pk>/delete/",
        views.General_postal_serviceDeleteView.as_view(),
        name="general_postal_service-delete",
    ),
    path(
        "general_postal_servicedownload/",
        downloads.general_postal_service_download_view,
        name="general_postal_service-download",
    ),
    path(
        "general_postal_servicemetadownload/",
        downloads.general_postal_service_meta_download_view,
        name="general_postal_service-metadownload",
    ),
]


# Create URL patterns dynamically for each model-class pair: UPDATE
for model_class, form_class, x_name, myvar, sec, subsec in model_form_pairs:
    my_exp = model_class.Code.description

    urlpatterns += [
        path(
            f"{x_name}/update/<int:object_id>/",
            generic.generic_update_view,
            {
                "form_class": form_class,
                "model_class": model_class,
                "x_name": x_name,
                "myvar": myvar,
                "my_exp": my_exp,
                "var_section": sec,
                "var_subsection": subsec,
                "delete_url_name": f"{x_name}-confirm-delete",
            },
            name=f"{x_name}-update",
        ),
        path(
            f"{x_name}/create/",
            GenericCreateView.as_view(
                form_class=form_class,
                var_name=x_name,
                myvar=myvar,
                my_exp=my_exp,
                var_section=sec,
                var_subsection=subsec,
                template="sc/sc_create.html",
            ),
            # {
            #     "form_class": form_class,
            #     "x_name": x_name,
            #     "myvar": myvar,
            #     "my_exp": my_exp,
            #     "var_section": sec,
            #     "var_subsection": subsec,
            # },
            name=f"{x_name}-create",
        ),
        path(
            f"{x_name}/<int:pk>/",
            generic.generic_detail_view,
            {
                "model_class": model_class,
                "myvar": x_name,
                "var_name_display": myvar,
            },
            name=f"{x_name}-detail",
        ),
        path(
            f"{x_name}s_all/",
            GenericListView.as_view(
                model_class=model_class,
                var_name=x_name,
                var_name_display=myvar,
                var_section=sec,
                var_subsection=subsec,
                var_main_desc=my_exp,
                template="sc/sc_list_all.html",
            ),
            name=f"{x_name}s_all",
        ),
        path(
            f"{x_name}download/",
            GenericDownloadView.as_view(
                model_class=model_class,
                var_name=x_name,
                prefix="social_complexity_",
            ),
            name=f"{x_name}-download",
        ),
        path(
            f"{x_name}metadownload/",
            GenericMetaDownloadView.as_view(
                model_class=model_class, var_name=x_name
            ),
            name=f"{x_name}-metadownload",
        ),
        path(
            f"{x_name}/<int:pk>/confirm-delete/",
            GenericConfirmDeleteView.as_view(
                model_class=model_class,
                var_name=x_name,
                template="core/confirm_delete.html",
            ),
            name=f"{x_name}-confirm-delete",
        ),
        path(
            f"{x_name}/<int:pk>/delete/",
            GenericDeleteView.as_view(
                model_class=model_class,
                var_name=x_name,
                redirect=f"{x_name}s_all"
            ),
            name=f"{x_name}-delete",
        ),
    ]
