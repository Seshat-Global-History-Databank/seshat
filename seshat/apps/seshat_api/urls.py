from django.urls import path, include
from rest_framework import routers


# Create router for URLs

router = routers.DefaultRouter()


# Register viewsets for "account" app

# from .views.accounts import (
#     ProfileViewSet,
#     SeshatExpertViewSet,
#     SeshatTaskViewSet,
# )

# router.register(r"account/profiles", ProfileViewSet, basename="api_profile")
# router.register(
#     r"account/seshat-experts",
#     SeshatExpertViewSet,
#     basename="api_seshat-expert",
# )
# router.register(r"account/seshat-tasks", SeshatTaskViewSet, basename="api_seshat-task")


# Register views for "core" app

from .views.core import (
    #PrivateCommentsViewSet,
    #PrivateCommentsPartsViewSet,
    MacroRegionViewSet,
    RegionViewSet,
    NGAViewSet,
    PolityViewSet,
    CapitalViewSet,
    NGAPolityRelationsViewSet,
    CountryViewSet,
    SectionViewSet,
    SubsectionViewSet,
    VariableHierarchyViewSet,
    ReferenceViewSet,
    CitationViewSet,
    SeshatCommentViewSet,
    SeshatCommentPartViewSet,
    ScpThroughCtnViewSet,
    ReligionViewSet,
    CliopatriaViewSet,
    #GADMShapefileViewSet,
    GADMCountriesViewSet,
    GADMProvincesViewSet,
)

# router.register(
#     r"core/private-comments",
#     PrivateCommentsViewSet,
#     basename="api_private-comment",
# )
# router.register(
#     r"core/private-comments-parts",
#     PrivateCommentsPartsViewSet,
#     basename="api_private-comment-part",
# )
router.register(r"core/macro-regions", MacroRegionViewSet, basename="api_macro-region")
router.register(r"core/regions", RegionViewSet, basename="api_region")
router.register(r"core/ngas", NGAViewSet, basename="api_nga")
router.register(r"core/polities", PolityViewSet, basename="api_polity")
router.register(r"core/capitals", CapitalViewSet, basename="api_capital")
router.register(
    r"core/nga-polity-relations",
    NGAPolityRelationsViewSet,
    basename="api_nga-polity-relation",
)
router.register(r"core/countries", CountryViewSet, basename="api_country")
router.register(r"core/sections", SectionViewSet, basename="api_section")
router.register(r"core/subsections", SubsectionViewSet, basename="api_subsection")
router.register(
    r"core/variable-hierarchies",
    VariableHierarchyViewSet,
    basename="api_variable-hierarchy",
)
router.register(r"core/references", ReferenceViewSet, basename="api_reference")
router.register(r"core/citations", CitationViewSet, basename="api_citation")
router.register(r"core/comments", SeshatCommentViewSet, basename="api_seshat-comment")
router.register(
    r"core/comment-parts",
    SeshatCommentPartViewSet,
    basename="api_seshat-comment-part",
)
router.register(
    r"core/comment-parts-through-citations",
    ScpThroughCtnViewSet,
    basename="api_comment-part-through-citation",
)
#router.register(r"core/commons", SeshatCommonViewSet, basename="api_common")
router.register(r"core/religions", ReligionViewSet, basename="api_religion")
router.register(
    r"core/cliopatria-shapefiles",
    CliopatriaViewSet,
    basename="api_cliopatria-shapefile",
)
# router.register(
#     r"core/gadm-shapefiles",
#     GADMShapefileViewSet,
#     basename="api_gadm-shapefile",
# )
router.register(
    r"core/gadm-countries", GADMCountriesViewSet, basename="api_gadm-country"
)
router.register(
    r"core/gadm-provinces",
    GADMProvincesViewSet,
    basename="api_gadm-province",
)


# Register views for "crisisdb" app

from .views.crisisdb import (
    USLocationViewSet,
    USViolenceSubtypeViewSet,
    USViolenceDataSourceViewSet,
    USViolenceViewSet,
    CrisisConsequenceViewSet,
    #PowerTransitionViewSet,
    #HumanSacrificeViewSet,
    ExternalConflictViewSet,
    ExternalConflictSideViewSet,
    AgriculturalPopulationViewSet,
    ArableLandViewSet,
    ArableLandPerFarmerViewSet,
    GrossGrainSharedPerAgriculturalPopulationViewSet,
    NetGrainSharedPerAgriculturalPopulationViewSet,
    SurplusViewSet,
    MilitaryExpenseViewSet,
    SilverInflowViewSet,
    SilverStockViewSet,
    TotalPopulationViewSet,
    GDPPerCapitaViewSet,
    DroughtEventViewSet,
    LocustEventViewSet,
    SocioeconomicTurmoilEventViewSet,
    CropFailureEventViewSet,
    FamineEventViewSet,
    DiseaseOutbreakViewSet,
)

router.register(r"crisisdb/us-locations", USLocationViewSet, basename="api_us-location")
router.register(
    r"crisisdb/us-violence-subtypes",
    USViolenceSubtypeViewSet,
    basename="api_us-violence-subtype",
)
router.register(
    r"crisisdb/us-violence-data-sources",
    USViolenceDataSourceViewSet,
    basename="api_us-violence-data-source",
)
router.register(r"crisisdb/us-violences", USViolenceViewSet, basename="api_us-violence")
router.register(
    r"crisisdb/crisis-consequences",
    CrisisConsequenceViewSet,
    basename="api_crisis-consequence",
)
# router.register(
#     r"crisisdb/power-transitions",
#     PowerTransitionViewSet,
#     basename="api_power-transition",
# )

# router.register(
#     r"crisisdb/human-sacrifices",
#     HumanSacrificeViewSet,
#     basename="api_human-sacrifice",
# )
router.register(
    r"crisisdb/external-conflicts",
    ExternalConflictViewSet,
    basename="api_external-conflict",
)
router.register(
    r"crisisdb/external-conflict-sides",
    ExternalConflictSideViewSet,
    basename="api_external-conflict-side",
)
router.register(
    r"crisisdb/agricultural-populations",
    AgriculturalPopulationViewSet,
    basename="api_agricultural-population",
)
router.register(r"crisisdb/arable-lands", ArableLandViewSet, basename="api_arable-land")
router.register(
    r"crisisdb/arable-land-per-farmer",
    ArableLandPerFarmerViewSet,
    basename="api_arable-land-per-farmer",
)
router.register(
    r"crisisdb/gross-grain-shared-per-agricultural-populations",
    GrossGrainSharedPerAgriculturalPopulationViewSet,
    basename="api_gross-grain-shared-per-agricultural-population",
)
router.register(
    r"crisisdb/net-grain-shared-per-agricultural-populations",
    NetGrainSharedPerAgriculturalPopulationViewSet,
    basename="api_net-grain-shared-per-agricultural-population",
)
router.register(r"crisisdb/surpluses", SurplusViewSet, basename="api_surplus")
router.register(
    r"crisisdb/military-expenses",
    MilitaryExpenseViewSet,
    basename="api_military-expense",
)
router.register(
    r"crisisdb/silver-inflows",
    SilverInflowViewSet,
    basename="api_silver-inflow",
)
router.register(
    r"crisisdb/silver-stocks",
    SilverStockViewSet,
    basename="api_silver-stock",
)
router.register(
    r"crisisdb/total-populations",
    TotalPopulationViewSet,
    basename="api_total-population",
)
router.register(
    r"crisisdb/gdp-per-capitas",
    GDPPerCapitaViewSet,
    basename="api_gdp-per-capita",
)
router.register(
    r"crisisdb/drought-events",
    DroughtEventViewSet,
    basename="api_drought-event",
)
router.register(
    r"crisisdb/locust-events",
    LocustEventViewSet,
    basename="api_locust-event",
)
router.register(
    r"crisisdb/socioeconomic-turmoil-events",
    SocioeconomicTurmoilEventViewSet,
    basename="api_socioeconomic-turmoil-event",
)
router.register(
    r"crisisdb/crop-failure-events",
    CropFailureEventViewSet,
    basename="api_crop-failure-event",
)
router.register(
    r"crisisdb/famine-events",
    FamineEventViewSet,
    basename="api_famine-event",
)
router.register(
    r"crisisdb/disease-outbreaks",
    DiseaseOutbreakViewSet,
    basename="api_disease-outbreak",
)


# app: general

from .views.general import (
    PolityResearchAssistantViewSet,
    PolityOriginalNameViewSet,
    PolityAlternativeNameViewSet,
    PolityDurationViewSet,
    PolityPeakYearsViewSet,
    PolityDegreeOfCentralizationViewSet,
    PolitySuprapolityRelationsViewSet,
    PolityUTMZoneViewSet,
    PolityCapitalViewSet,
    PolityLanguageViewSet,
    PolityLinguisticFamilyViewSet,
    PolityLanguageGenusViewSet,
    PolityReligionGenusViewSet,
    PolityReligionFamilyViewSet,
    PolityReligionViewSet,
    PolityRelationshipToPrecedingEntityViewSet,
    PolityPrecedingEntityViewSet,
    PolitySucceedingEntityViewSet,
    PolitySupraculturalEntityViewSet,
    PolityScaleOfSupraculturalInteractionViewSet,
    PolityAlternateReligionGenusViewSet,
    PolityAlternateReligionFamilyViewSet,
    PolityAlternateReligionViewSet,
    PolityExpertViewSet,
    PolityEditorViewSet,
    PolityReligiousTraditionViewSet,
)

router.register(
    r"general/polity-research-assistants",
    PolityResearchAssistantViewSet,
    basename="api_polity-research-assistant",
)
router.register(
    r"general/polity-original-names",
    PolityOriginalNameViewSet,
    basename="api_polity-original-name",
)
router.register(
    r"general/polity-alternative-names",
    PolityAlternativeNameViewSet,
    basename="api_polity-alternative-name",
)
router.register(
    r"general/polity-durations", PolityDurationViewSet, basename="api_polity-duration"
)
router.register(
    r"general/polity-peak-years", PolityPeakYearsViewSet, basename="api_polity-peak-years"
)
router.register(
    r"general/polity-degree-of-centralizations",
    PolityDegreeOfCentralizationViewSet,
    basename="api_polity-degree-of-centralization",
)
router.register(
    r"general/polity-suprapolities",
    PolitySuprapolityRelationsViewSet,
    basename="api_polity-suprapolity",
)
router.register(
    r"general/polity-utm-timezones",
    PolityUTMZoneViewSet,
    basename="api_polity-utm-timezone",
)
router.register(
    r"general/polity-capitals", PolityCapitalViewSet, basename="api_polity-capital"
)
router.register(
    r"general/polity-languages", PolityLanguageViewSet, basename="api_polity-language"
)
router.register(
    r"general/polity-linguistic-families",
    PolityLinguisticFamilyViewSet,
    basename="api_polity-linguistic-family",
)
router.register(
    r"general/polity-language-genuses",
    PolityLanguageGenusViewSet,
    basename="api_polity-language-genus",
)
router.register(
    r"general/polity-religion-genuses",
    PolityReligionGenusViewSet,
    basename="api_polity-religion-genus",
)
router.register(
    r"general/polity-religion-families",
    PolityReligionFamilyViewSet,
    basename="api_polity-religion-family",
)
router.register(
    r"general/polity-religions", PolityReligionViewSet, basename="api_polity-religion"
)
router.register(
    r"general/polity-relationship-to-preceding-entities",
    PolityRelationshipToPrecedingEntityViewSet,
    basename="api_polity-relationship-to-preceding-entity",
)
router.register(
    r"general/polity-preceding-entities",
    PolityPrecedingEntityViewSet,
    basename="api_polity-preceding-entity",
)
router.register(
    r"general/polity-succeeding-entities",
    PolitySucceedingEntityViewSet,
    basename="api_polity-succeeding-entity",
)
router.register(
    r"general/polity-supracultural-entities",
    PolitySupraculturalEntityViewSet,
    basename="api_polity-supracultural-entity",
)
router.register(
    r"general/polity-scale-of-supracultural-interactions",
    PolityScaleOfSupraculturalInteractionViewSet,
    basename="api_polity-scale-of-supracultural-interaction",
)
router.register(
    r"general/polity-alternate-religion-genuses",
    PolityAlternateReligionGenusViewSet,
    basename="api_polity-alternate-religion-genus",
)
router.register(
    r"general/polity-alternate-religion-families",
    PolityAlternateReligionFamilyViewSet,
    basename="api_polity-alternate-religion-family",
)
router.register(
    r"general/polity-alternate-religions",
    PolityAlternateReligionViewSet,
    basename="api_polity-alternate-religion",
)
router.register(
    r"general/polity-experts", PolityExpertViewSet, basename="api_polity-expert"
)
router.register(
    r"general/polity-editors", PolityEditorViewSet, basename="api_polity-editor"
)
router.register(
    r"general/polity-religious-traditions",
    PolityReligiousTraditionViewSet,
    basename="api_polity-religious-tradition",
)


# Register views for "rt" app

from .views.rt import (
    WidespreadReligionViewSet,
    OfficialReligionViewSet,
    ElitesReligionViewSet,
    TheoSyncDifRelViewSet,
    SyncRelPraIndBeliViewSet,
    ReligiousFragmentationViewSet,
    GovVioFreqRelGrpViewSet,
    GovResPubWorViewSet,
    GovResPubProsViewSet,
    GovResConvViewSet,
    GovPressConvViewSet,
    GovResPropOwnForRelGrpViewSet,
    TaxRelAdhActInsViewSet,
    GovOblRelGrpOfcRecoViewSet,
    GovResConsRelBuilViewSet,
    GovResRelEduViewSet,
    GovResCirRelLitViewSet,
    GovDisRelGrpOccFunViewSet,
    SocVioFreqRelGrpViewSet,
    SocDisRelGrpOccFunViewSet,
    GovPressConvForAgaViewSet,
)

router.register(
    r"rt/widespread-religions",
    WidespreadReligionViewSet,
    basename="api_widespread-religion",
)
router.register(
    r"rt/official-religions",
    OfficialReligionViewSet,
    basename="api_official-religion",
)
router.register(
    r"rt/elites-religions", ElitesReligionViewSet, basename="api_elites-religion"
)
router.register(
    r"rt/theological-syncretism-of-different-religions",
    TheoSyncDifRelViewSet,
    basename="api_theological-syncretism-of-different-religions",
)
router.register(
    r"rt/syncretism-of-religious-practices-at-the-level-of-individual-believers",
    SyncRelPraIndBeliViewSet,
    basename="api_syncretism-of-religious-practices-at-the-level-of-individual-believers",
)
router.register(
    r"rt/religious-fragmentations",
    ReligiousFragmentationViewSet,
    basename="api_religious-fragmentation",
)
router.register(
    r"rt/frequency-of-governmental-violence-against-religious-groups",
    GovVioFreqRelGrpViewSet,
    basename="api_frequency-of-governmental-violence-against-religious-groups",
)
router.register(
    r"rt/government-restrictions-on-public-worships",
    GovResPubWorViewSet,
    basename="api_government-restrictions-on-public-worships",
)
router.register(
    r"rt/government-restrictions-on-public-proselytizings",
    GovResPubProsViewSet,
    basename="api_government-restrictions-on-public-proselytizings",
)
router.register(
    r"rt/government-restrictions-on-conversions",
    GovResConvViewSet,
    basename="api_government-restrictions-on-conversions",
)
router.register(
    r"rt/government-pressure-to-converts",
    GovPressConvViewSet,
    basename="api_government-pressure-to-converts",
)
router.register(
    r"rt/government-restrictions-on-property-ownership-for-adherents-of-and-religious-groups",
    GovResPropOwnForRelGrpViewSet,
    basename="api_government-restrictions-on-property-ownership-for-adherents-of-and-religious-groups",
)
router.register(
    r"rt/taxes-based-on-religious-adherence-or-on-religious-activities-and-institutions",
    TaxRelAdhActInsViewSet,
    basename="api_taxes-based-on-religious-adherence-or-on-religious-activities-and-institutions",
)
router.register(
    r"rt/governmental-obligations-for-religious-groups-to-apply-for-official-recognitions",
    GovOblRelGrpOfcRecoViewSet,
    basename="api_governmental-obligations-for-religious-groups-to-apply-for-official-recognitions",
)
router.register(
    r"rt/government-restrictions-on-construction-of-religious-buildings",
    GovResConsRelBuilViewSet,
    basename="api_government-restrictions-on-construction-of-religious-buildings",
)
router.register(
    r"rt/government-restrictions-on-religious-educations",
    GovResRelEduViewSet,
    basename="api_government-restrictions-on-religious-educations",
)
router.register(
    r"rt/government-restrictions-on-circulation-of-religious-literatures",
    GovResCirRelLitViewSet,
    basename="api_government-restrictions-on-circulation-of-religious-literatures",
)
router.register(
    r"rt/government-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
    GovDisRelGrpOccFunViewSet,
    basename="api_government-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
)
router.register(
    r"rt/frequency-of-societal-violence-against-religious-groups",
    SocVioFreqRelGrpViewSet,
    basename="api_frequency-of-societal-violence-against-religious-groups",
)
router.register(
    r"rt/societal-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
    SocDisRelGrpOccFunViewSet,
    basename="api_societal-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
)
router.register(
    r"rt/societal-pressure-to-convert-or-against-conversions",
    GovPressConvForAgaViewSet,
    basename="api_societal-pressure-to-convert-or-against-conversions",
)


# Add views for "sc" app to the router

from .views.sc import (
    RAViewSet,
    PolityTerritoryViewSet,
    PolityPopulationViewSet,
    PopulationOfTheLargestSettlementViewSet,
    SettlementHierarchyViewSet,
    AdministrativeLevelViewSet,
    ReligiousLevelViewSet,
    MilitaryLevelViewSet,
    ProfessionalMilitaryOfficerViewSet,
    ProfessionalSoldierViewSet,
    ProfessionalPriesthoodViewSet,
    FullTimeBureaucratViewSet,
    ExaminationSystemViewSet,
    MeritPromotionViewSet,
    SpecializedGovernmentBuildingViewSet,
    FormalLegalCodeViewSet,
    JudgeViewSet,
    CourtViewSet,
    ProfessionalLawyerViewSet,
    IrrigationSystemViewSet,
    DrinkingWaterSupplySystemViewSet,
    MarketViewSet,
    FoodStorageSiteViewSet,
    RoadViewSet,
    BridgeViewSet,
    CanalViewSet,
    PortViewSet,
    MinesOrQuarryViewSet,
    MnemonicDeviceViewSet,
    NonwrittenRecordViewSet,
    WrittenRecordViewSet,
    ScriptViewSet,
    NonPhoneticWritingViewSet,
    PhoneticAlphabeticWritingViewSet,
    ListsTablesAndClassificationViewSet,
    CalendarViewSet,
    SacredTextViewSet,
    ReligiousLiteratureViewSet,
    PracticalLiteratureViewSet,
    HistoryViewSet,
    PhilosophyViewSet,
    ScientificLiteratureViewSet,
    FictionViewSet,
    ArticleViewSet,
    TokenViewSet,
    PreciousMetalViewSet,
    ForeignCoinViewSet,
    IndigenousCoinViewSet,
    PaperCurrencyViewSet,
    CourierViewSet,
    PostalStationViewSet,
    GeneralPostalServiceViewSet,
    CommunalBuildingViewSet,
    UtilitarianPublicBuildingViewSet,
    SymbolicBuildingViewSet,
    EntertainmentBuildingViewSet,
    KnowledgeOrInformationBuildingViewSet,
    OtherUtilitarianPublicBuildingViewSet,
    SpecialPurposeSiteViewSet,
    CeremonialSiteViewSet,
    BurialSiteViewSet,
    TradingEmporiaViewSet,
    EnclosureViewSet,
    LengthMeasurementSystemViewSet,
    AreaMeasurementSystemViewSet,
    VolumeMeasurementSystemViewSet,
    WeightMeasurementSystemViewSet,
    TimeMeasurementSystemViewSet,
    GeometricalMeasurementSystemViewSet,
    OtherMeasurementSystemViewSet,
    DebtAndCreditStructureViewSet,
    StoreOfWealthViewSet,
    SourceOfSupportViewSet,
    OccupationalComplexityViewSet,
    SpecialPurposeHouseViewSet,
    OtherSpecialPurposeSiteViewSet,
    LargestCommunicationDistanceViewSet,
    FastestIndividualCommunicationViewSet,
)

router.register(
    r"sc/research-assistants", RAViewSet, basename="api_research-assistant"
)
router.register(
    r"sc/polity-territories", PolityTerritoryViewSet, basename="api_polity-territory"
)
router.register(
    r"sc/polity-populations",
    PolityPopulationViewSet,
    basename="api_polity-population",
)
router.register(
    r"sc/population-of-the-largest-settlements",
    PopulationOfTheLargestSettlementViewSet,
    basename="api_population-of-the-largest-settlement",
)
router.register(
    r"sc/settlement-hierarchies",
    SettlementHierarchyViewSet,
    basename="api_settlement-hierarchy",
)
router.register(
    r"sc/administrative-levels",
    AdministrativeLevelViewSet,
    basename="api_administrative-level",
)
router.register(
    r"sc/religious-levels", ReligiousLevelViewSet, basename="api_religious-level"
)
router.register(
    r"sc/military-levels", MilitaryLevelViewSet, basename="api_military-level"
)
router.register(
    r"sc/professional-military-officers",
    ProfessionalMilitaryOfficerViewSet,
    basename="api_professional-military-officer",
)
router.register(
    r"sc/professional-soldiers",
    ProfessionalSoldierViewSet,
    basename="api_professional-soldier",
)
router.register(
    r"sc/professional-priesthoods",
    ProfessionalPriesthoodViewSet,
    basename="api_professional-priesthood",
)
router.register(
    r"sc/full-time-bureaucrats",
    FullTimeBureaucratViewSet,
    basename="api_full-time-bureaucrat",
)
router.register(
    r"sc/examination-systems",
    ExaminationSystemViewSet,
    basename="api_examination-system",
)
router.register(
    r"sc/merit-promotions", MeritPromotionViewSet, basename="api_merit-promotion"
)
router.register(
    r"sc/specialized-government-buildings",
    SpecializedGovernmentBuildingViewSet,
    basename="api_specialized-government-building",
)
router.register(
    r"sc/formal-legal-codes", FormalLegalCodeViewSet, basename="api_formal-legal-code"
)
router.register(r"sc/judges", JudgeViewSet, basename="api_judge")
router.register(r"sc/courts", CourtViewSet, basename="api_court")
router.register(
    r"sc/professional-lawyers",
    ProfessionalLawyerViewSet,
    basename="api_professional-lawyer",
)
router.register(
    r"sc/irrigation-systems",
    IrrigationSystemViewSet,
    basename="api_irrigation-system",
)
router.register(
    r"sc/drinking-water-supplies",
    DrinkingWaterSupplySystemViewSet,
    basename="api_drinking-water-supply-system",
)
router.register(r"sc/markets", MarketViewSet, basename="api_market")
router.register(
    r"sc/food-storage-sites", FoodStorageSiteViewSet, basename="api_food-storage-site"
)
router.register(r"sc/roads", RoadViewSet, basename="api_road")
router.register(r"sc/bridges", BridgeViewSet, basename="api_bridge")
router.register(r"sc/canals", CanalViewSet, basename="api_canal")
router.register(r"sc/ports", PortViewSet, basename="api_port")
router.register(
    r"sc/mines-or-quarries", MinesOrQuarryViewSet, basename="api_mines-or-quarry"
)
router.register(
    r"sc/mnemonic-devices", MnemonicDeviceViewSet, basename="api_mnemonic-device"
)
router.register(
    r"sc/nonwritten-records",
    NonwrittenRecordViewSet,
    basename="api_nonwritten-record",
)
router.register(
    r"sc/written-records", WrittenRecordViewSet, basename="api_written-record"
)
router.register(r"sc/scripts", ScriptViewSet, basename="api_script")
router.register(
    r"sc/non-phonetic-writings",
    NonPhoneticWritingViewSet,
    basename="api_non-phonetic-writing",
)
router.register(
    r"sc/phonetic-alphabetic-writings",
    PhoneticAlphabeticWritingViewSet,
    basename="api_phonetic-alphabetic-writing",
)
router.register(
    r"sc/lists-tables-and-classifications",
    ListsTablesAndClassificationViewSet,
    basename="api_lists-tables-and-classifications",
)
router.register(r"sc/calendars", CalendarViewSet, basename="api_calendar")
router.register(r"sc/sacred-texts", SacredTextViewSet, basename="api_sacred-text")
router.register(
    r"sc/religious-literatures",
    ReligiousLiteratureViewSet,
    basename="api_religious-literature",
)
router.register(
    r"sc/practical-literatures",
    PracticalLiteratureViewSet,
    basename="api_practical-literature",
)
router.register(r"sc/histories", HistoryViewSet, basename="api_history")
router.register(r"sc/philosophies", PhilosophyViewSet, basename="api_philosophy")
router.register(
    r"sc/scientific-literatures",
    ScientificLiteratureViewSet,
    basename="api_scientific-literature",
)
router.register(r"sc/fictions", FictionViewSet, basename="api_fiction")
router.register(r"sc/articles", ArticleViewSet, basename="api_article")
router.register(r"sc/tokens", TokenViewSet, basename="api_token")
router.register(
    r"sc/precious-metals", PreciousMetalViewSet, basename="api_precious-metal"
)
router.register(r"sc/foreign-coins", ForeignCoinViewSet, basename="api_foreign-coin")
router.register(
    r"sc/indigenous-coins", IndigenousCoinViewSet, basename="api_indigenous-coin"
)
router.register(
    r"sc/paper-currencies", PaperCurrencyViewSet, basename="api_paper-currency"
)
router.register(r"sc/couriers", CourierViewSet, basename="api_courier")
router.register(
    r"sc/postal-stations", PostalStationViewSet, basename="api_postal-station"
)
router.register(
    r"sc/general-postal-services",
    GeneralPostalServiceViewSet,
    basename="api_general-postal-service",
)
router.register(
    r"sc/communal-buildings",
    CommunalBuildingViewSet,
    basename="api_communal-building",
)
router.register(
    r"sc/utilitarian-public-buildings",
    UtilitarianPublicBuildingViewSet,
    basename="api_utilitarian-public-building",
)
router.register(
    r"sc/symbolic-buildings",
    SymbolicBuildingViewSet,
    basename="api_symbolic-building",
)
router.register(
    r"sc/entertainment-buildings",
    EntertainmentBuildingViewSet,
    basename="api_entertainment-building",
)
router.register(
    r"sc/knowledge-or-information-buildings",
    KnowledgeOrInformationBuildingViewSet,
    basename="api_knowledge-or-information-building",
)
router.register(
    r"sc/other-utilitarian-public-buildings",
    OtherUtilitarianPublicBuildingViewSet,
    basename="api_other-utilitarian-public-building",
)
router.register(
    r"sc/special-purpose-sites",
    SpecialPurposeSiteViewSet,
    basename="api_special-purpose-site",
)
router.register(
    r"sc/ceremonial-sites", CeremonialSiteViewSet, basename="api_ceremonial-site"
)
router.register(r"sc/burial-sites", BurialSiteViewSet, basename="api_burial-site")
router.register(
    r"sc/trading-emporia", TradingEmporiaViewSet, basename="api_trading-emporium"
)
router.register(r"sc/enclosures", EnclosureViewSet, basename="api_enclosure")
router.register(
    r"sc/length-measurement-systems",
    LengthMeasurementSystemViewSet,
    basename="api_length-measurement-system",
)
router.register(
    r"sc/area-measurement-systems",
    AreaMeasurementSystemViewSet,
    basename="api_area-measurement-system",
)
router.register(
    r"sc/volume-measurement-systems",
    VolumeMeasurementSystemViewSet,
    basename="api_volume-measurement-system",
)
router.register(
    r"sc/weight-measurement-systems",
    WeightMeasurementSystemViewSet,
    basename="api_weight-measurement-system",
)
router.register(
    r"sc/time-measurement-systems",
    TimeMeasurementSystemViewSet,
    basename="api_time-measurement-system",
)
router.register(
    r"sc/geometrical-measurement-systems",
    GeometricalMeasurementSystemViewSet,
    basename="api_geometrical-measurement-system",
)
router.register(
    r"sc/other-measurement-systems",
    OtherMeasurementSystemViewSet,
    basename="api_other-measurement-system",
)
router.register(
    r"sc/debt-and-credit-structures",
    DebtAndCreditStructureViewSet,
    basename="api_debt-and-credit-structure",
)
router.register(
    r"sc/stores-of-wealth", StoreOfWealthViewSet, basename="api_store-of-wealth"
)
router.register(
    r"sc/sources-of-support", SourceOfSupportViewSet, basename="api_source-of-support"
)
router.register(
    r"sc/occupational-complexities",
    OccupationalComplexityViewSet,
    basename="api_occupational-complexity",
)
router.register(
    r"sc/special-purpose-houses",
    SpecialPurposeHouseViewSet,
    basename="api_special-purpose-house",
)
router.register(
    r"sc/other-special-purpose-sites",
    OtherSpecialPurposeSiteViewSet,
    basename="api_other-special-purpose-site",
)
router.register(
    r"sc/largest-communication-distances",
    LargestCommunicationDistanceViewSet,
    basename="api_largest-communication-distance",
)
router.register(
    r"sc/fastest-individual-communications",
    FastestIndividualCommunicationViewSet,
    basename="api_fastest-individual-communication",
)


# Register views for "wf" app

from .views.wf import (
    LongWallViewSet,
    CopperViewSet,
    BronzeViewSet,
    IronViewSet,
    SteelViewSet,
    JavelinViewSet,
    AtlatlViewSet,
    SlingViewSet,
    SelfBowViewSet,
    CompositeBowViewSet,
    CrossbowViewSet,
    TensionSiegeEngineViewSet,
    SlingSiegeEngineViewSet,
    GunpowderSiegeArtilleryViewSet,
    HandheldFirearmViewSet,
    WarClubViewSet,
    BattleAxeViewSet,
    DaggerViewSet,
    SwordViewSet,
    SpearViewSet,
    PolearmViewSet,
    DogViewSet,
    DonkeyViewSet,
    HorseViewSet,
    CamelViewSet,
    ElephantViewSet,
    WoodBarkEtcViewSet,
    LeatherClothViewSet,
    ShieldViewSet,
    HelmetViewSet,
    BreastplateViewSet,
    LimbProtectionViewSet,
    ScaledArmorViewSet,
    LaminarArmorViewSet,
    PlateArmorViewSet,
    SmallVesselsCanoesEtcViewSet,
    MerchantShipPressedIntoServiceViewSet,
    SpecializedMilitaryVesselViewSet,
    SettlementInADefensivePositionViewSet,
    WoodenPalisadeViewSet,
    EarthRampartViewSet,
    DitchViewSet,
    MoatViewSet,
    StoneWallsNonMortaredViewSet,
    StoneWallsMortaredViewSet,
    FortifiedCampViewSet,
    ComplexFortificationViewSet,
    ModernFortificationViewSet,
    ChainmailViewSet,
)

router.register(r"wf/long-walls", LongWallViewSet, basename="api_long-wall")
router.register(r"wf/coppers", CopperViewSet, basename="api_copper")
router.register(r"wf/bronzes", BronzeViewSet, basename="api_bronze")
router.register(r"wf/irons", IronViewSet, basename="api_iron")
router.register(r"wf/steels", SteelViewSet, basename="api_steel")
router.register(r"wf/javelins", JavelinViewSet, basename="api_javelin")
router.register(r"wf/atlatls", AtlatlViewSet, basename="api_atlatl")
router.register(r"wf/slings", SlingViewSet, basename="api_sling")
router.register(r"wf/self-bows", SelfBowViewSet, basename="api_self-bow")
router.register(
    r"wf/composite-bows", CompositeBowViewSet, basename="api_composite-bow"
)
router.register(r"wf/crossbows", CrossbowViewSet, basename="api_crossbow")
router.register(
    r"wf/tension-siege-engines",
    TensionSiegeEngineViewSet,
    basename="api_tension-siege-engine",
)
router.register(
    r"wf/sling-siege-engines",
    SlingSiegeEngineViewSet,
    basename="api_sling-siege-engine",
)
router.register(
    r"wf/gunpowder-siege-artilleries",
    GunpowderSiegeArtilleryViewSet,
    basename="api_gunpowder-siege-artillery",
)
router.register(
    r"wf/handheld-firearms", HandheldFirearmViewSet, basename="api_handheld-firearm"
)
router.register(r"wf/war-clubs", WarClubViewSet, basename="api_war-club")
router.register(r"wf/battle-axes", BattleAxeViewSet, basename="api_battle-axe")
router.register(r"wf/daggers", DaggerViewSet, basename="api_dagger")
router.register(r"wf/swords", SwordViewSet, basename="api_sword")
router.register(r"wf/spears", SpearViewSet, basename="api_spear")
router.register(r"wf/polearms", PolearmViewSet, basename="api_polearm")
router.register(r"wf/dogs", DogViewSet, basename="api_dog")
router.register(r"wf/donkeys", DonkeyViewSet, basename="api_donkey")
router.register(r"wf/horses", HorseViewSet, basename="api_horse")
router.register(r"wf/camels", CamelViewSet, basename="api_camel")
router.register(r"wf/elephants", ElephantViewSet, basename="api_elephant")
router.register(r"wf/wood-bark-etc", WoodBarkEtcViewSet, basename="api_wood-bark-etc")
router.register(r"wf/leathers", LeatherClothViewSet, basename="api_leather-cloth")
router.register(r"wf/shields", ShieldViewSet, basename="api_shield")
router.register(r"wf/helmets", HelmetViewSet, basename="api_helmet")
router.register(r"wf/breastplates", BreastplateViewSet, basename="api_breastplate")
router.register(
    r"wf/limb-protections", LimbProtectionViewSet, basename="api_limb-protection"
)
router.register(r"wf/scaled-armors", ScaledArmorViewSet, basename="api_scaled-armor")
router.register(
    r"wf/laminar-armors", LaminarArmorViewSet, basename="api_laminar-armor"
)
router.register(r"wf/plate-armors", PlateArmorViewSet, basename="api_plate-armor")
router.register(
    r"wf/small-vessel-canoe-etc",
    SmallVesselsCanoesEtcViewSet,
    basename="api_small-vessel-canoe-etc",
)
router.register(
    r"wf/merchant-ship-pressed-into-service",
    MerchantShipPressedIntoServiceViewSet,
    basename="api_merchant-ship-pressed-into-service",
)
router.register(
    r"wf/specialized-military-vessels",
    SpecializedMilitaryVesselViewSet,
    basename="api_specialized-military-vessel",
)
router.register(
    r"wf/settlement-in-defensive-positions",
    SettlementInADefensivePositionViewSet,
    basename="api_settlement-in-defensive-position",
)
router.register(
    r"wf/wooden-palisades", WoodenPalisadeViewSet, basename="api_wooden-palisade"
)
router.register(
    r"wf/earth-ramparts", EarthRampartViewSet, basename="api_earth-rampart"
)
router.register(r"wf/ditches", DitchViewSet, basename="api_ditch")
router.register(r"wf/moats", MoatViewSet, basename="api_moat")
router.register(
    r"wf/stone-walls-non-mortared",
    StoneWallsNonMortaredViewSet,
    basename="api_stone-walls-non-mortared",
)
router.register(
    r"wf/stone-walls-mortared",
    StoneWallsMortaredViewSet,
    basename="api_stone-walls-mortared",
)
router.register(
    r"wf/fortified-camps", FortifiedCampViewSet, basename="api_fortified-camp"
)
router.register(
    r"wf/complex-fortifications",
    ComplexFortificationViewSet,
    basename="api_complex-fortification",
)
router.register(
    r"wf/modern-fortifications",
    ModernFortificationViewSet,
    basename="api_modern-fortification",
)
router.register(r"wf/chainmails", ChainmailViewSet, basename="api_chainmail")


# Register all the views with the router

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]

from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]