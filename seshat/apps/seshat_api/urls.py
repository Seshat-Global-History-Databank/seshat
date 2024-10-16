from django.urls import path, include
from rest_framework import routers


# Create router for URLs

router = routers.DefaultRouter()


# Register viewsets for "account" app

from .views.accounts import (
    ProfileViewSet,
    SeshatTaskViewSet,
)

router.register(r"account/profiles", ProfileViewSet, basename="profile")
router.register(r"account/seshat-tasks", SeshatTaskViewSet, basename="seshat-task")


# Register views for "core" app

from .views.core import (
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
    ReligionViewSet,
    CliopatriaViewSet,
    GADMShapefileViewSet,
    GADMCountriesViewSet,
    GADMProvincesViewSet,
)

router.register(r"core/macro-regions", MacroRegionViewSet, basename="macro-region")
router.register(r"core/regions", RegionViewSet, basename="region")
router.register(r"core/ngas", NGAViewSet, basename="nga")
router.register(r"core/polities", PolityViewSet, basename="polity")
router.register(r"core/capitals", CapitalViewSet, basename="capital")
router.register(
    r"core/nga-polity-relations",
    NGAPolityRelationsViewSet,
    basename="nga-polity-relation",
)
router.register(r"core/countries", CountryViewSet, basename="country")
router.register(r"core/sections", SectionViewSet, basename="section")
router.register(r"core/subsections", SubsectionViewSet, basename="subsection")
router.register(
    r"core/variable-hierarchies",
    VariableHierarchyViewSet,
    basename="variable-hierarchy",
)
router.register(r"core/references", ReferenceViewSet, basename="reference")
router.register(r"core/citations", CitationViewSet, basename="citation")
#router.register(r"core/commons", SeshatCommonViewSet, basename="common")
router.register(r"core/religions", ReligionViewSet, basename="religion")
router.register(
    r"core/cliopatria-shapefiles",
    CliopatriaViewSet,
    basename="cliopatria-shapefile",
)
router.register(
    r"core/gadm-shapefiles",
    GADMShapefileViewSet,
    basename="gadm-shapefile",
)
router.register(
    r"core/gadm-countries", GADMCountriesViewSet, basename="gadm-country"
)
router.register(
    r"core/gadm-provinces",
    GADMProvincesViewSet,
    basename="gadm-province",
)


# Register views for "crisisdb" app

from .views.crisisdb import (
    USLocationViewSet,
    USViolenceSubtypeViewSet,
    USViolenceDataSourceViewSet,
    USViolenceViewSet,
    CrisisConsequenceViewSet,
    PowerTransitionViewSet,
    HumanSacrificeViewSet,
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

router.register(r"crisisdb/us-locations", USLocationViewSet, basename="us-location")
router.register(
    r"crisisdb/us-violence-subtypes",
    USViolenceSubtypeViewSet,
    basename="us-violence-subtype",
)
router.register(
    r"crisisdb/us-violence-data-sources",
    USViolenceDataSourceViewSet,
    basename="us-violence-data-source",
)
router.register(r"crisisdb/us-violences", USViolenceViewSet, basename="us-violence")
router.register(
    r"crisisdb/crisis-consequences",
    CrisisConsequenceViewSet,
    basename="crisis-consequence",
)
router.register(
    r"crisisdb/power-transitions",
    PowerTransitionViewSet,
    basename="power-transition",
)

router.register(
    r"crisisdb/human-sacrifices",
    HumanSacrificeViewSet,
    basename="human-sacrifice",
)
router.register(
    r"crisisdb/external-conflicts",
    ExternalConflictViewSet,
    basename="external-conflict",
)
router.register(
    r"crisisdb/external-conflict-sides",
    ExternalConflictSideViewSet,
    basename="external-conflict-side",
)
router.register(
    r"crisisdb/agricultural-populations",
    AgriculturalPopulationViewSet,
    basename="agricultural-population",
)
router.register(r"crisisdb/arable-lands", ArableLandViewSet, basename="arable-land")
router.register(
    r"crisisdb/arable-land-per-farmer",
    ArableLandPerFarmerViewSet,
    basename="arable-land-per-farmer",
)
router.register(
    r"crisisdb/gross-grain-shared-per-agricultural-populations",
    GrossGrainSharedPerAgriculturalPopulationViewSet,
    basename="gross-grain-shared-per-agricultural-population",
)
router.register(
    r"crisisdb/net-grain-shared-per-agricultural-populations",
    NetGrainSharedPerAgriculturalPopulationViewSet,
    basename="net-grain-shared-per-agricultural-population",
)
router.register(r"crisisdb/surpluses", SurplusViewSet, basename="surplus")
router.register(
    r"crisisdb/military-expenses",
    MilitaryExpenseViewSet,
    basename="military-expense",
)
router.register(
    r"crisisdb/silver-inflows",
    SilverInflowViewSet,
    basename="silver-inflow",
)
router.register(
    r"crisisdb/silver-stocks",
    SilverStockViewSet,
    basename="silver-stock",
)
router.register(
    r"crisisdb/total-populations",
    TotalPopulationViewSet,
    basename="total-population",
)
router.register(
    r"crisisdb/gdp-per-capitas",
    GDPPerCapitaViewSet,
    basename="gdp-per-capita",
)
router.register(
    r"crisisdb/drought-events",
    DroughtEventViewSet,
    basename="drought-event",
)
router.register(
    r"crisisdb/locust-events",
    LocustEventViewSet,
    basename="locust-event",
)
router.register(
    r"crisisdb/socioeconomic-turmoil-events",
    SocioeconomicTurmoilEventViewSet,
    basename="socioeconomic-turmoil-event",
)
router.register(
    r"crisisdb/crop-failure-events",
    CropFailureEventViewSet,
    basename="crop-failure-event",
)
router.register(
    r"crisisdb/famine-events",
    FamineEventViewSet,
    basename="famine-event",
)
router.register(
    r"crisisdb/disease-outbreaks",
    DiseaseOutbreakViewSet,
    basename="disease-outbreak",
)


# app: general

from .views.general import (
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
    PolityReligiousTraditionViewSet,
)

router.register(
    r"general/polity-original-names",
    PolityOriginalNameViewSet,
    basename="polity-original-name",
)
router.register(
    r"general/polity-alternative-names",
    PolityAlternativeNameViewSet,
    basename="polity-alternative-name",
)
router.register(
    r"general/polity-durations", PolityDurationViewSet, basename="polity-duration"
)
router.register(
    r"general/polity-peak-years", PolityPeakYearsViewSet, basename="polity-peak-years"
)
router.register(
    r"general/polity-degree-of-centralizations",
    PolityDegreeOfCentralizationViewSet,
    basename="polity-degree-of-centralization",
)
router.register(
    r"general/polity-suprapolities",
    PolitySuprapolityRelationsViewSet,
    basename="polity-suprapolity",
)
router.register(
    r"general/polity-utm-timezones",
    PolityUTMZoneViewSet,
    basename="polity-utm-timezone",
)
router.register(
    r"general/polity-capitals", PolityCapitalViewSet, basename="polity-capital"
)
router.register(
    r"general/polity-languages", PolityLanguageViewSet, basename="polity-language"
)
router.register(
    r"general/polity-linguistic-families",
    PolityLinguisticFamilyViewSet,
    basename="polity-linguistic-family",
)
router.register(
    r"general/polity-language-genuses",
    PolityLanguageGenusViewSet,
    basename="polity-language-genus",
)
router.register(
    r"general/polity-religion-genuses",
    PolityReligionGenusViewSet,
    basename="polity-religion-genus",
)
router.register(
    r"general/polity-religion-families",
    PolityReligionFamilyViewSet,
    basename="polity-religion-family",
)
router.register(
    r"general/polity-religions", PolityReligionViewSet, basename="polity-religion"
)
router.register(
    r"general/polity-relationship-to-preceding-entities",
    PolityRelationshipToPrecedingEntityViewSet,
    basename="polity-relationship-to-preceding-entity",
)
router.register(
    r"general/polity-preceding-entities",
    PolityPrecedingEntityViewSet,
    basename="polity-preceding-entity",
)
router.register(
    r"general/polity-succeeding-entities",
    PolitySucceedingEntityViewSet,
    basename="polity-succeeding-entity",
)
router.register(
    r"general/polity-supracultural-entities",
    PolitySupraculturalEntityViewSet,
    basename="polity-supracultural-entity",
)
router.register(
    r"general/polity-scale-of-supracultural-interactions",
    PolityScaleOfSupraculturalInteractionViewSet,
    basename="polity-scale-of-supracultural-interaction",
)
router.register(
    r"general/polity-alternate-religion-genuses",
    PolityAlternateReligionGenusViewSet,
    basename="polity-alternate-religion-genus",
)
router.register(
    r"general/polity-alternate-religion-families",
    PolityAlternateReligionFamilyViewSet,
    basename="polity-alternate-religion-family",
)
router.register(
    r"general/polity-alternate-religions",
    PolityAlternateReligionViewSet,
    basename="polity-alternate-religion",
)
router.register(
    r"general/polity-religious-traditions",
    PolityReligiousTraditionViewSet,
    basename="polity-religious-tradition",
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
    basename="widespread-religion",
)
router.register(
    r"rt/official-religions",
    OfficialReligionViewSet,
    basename="official-religion",
)
router.register(
    r"rt/elites-religions", ElitesReligionViewSet, basename="elites-religion"
)
router.register(
    r"rt/theological-syncretism-of-different-religions",
    TheoSyncDifRelViewSet,
    basename="theological-syncretism-of-different-religions",
)
router.register(
    r"rt/syncretism-of-religious-practices-at-the-level-of-individual-believers",
    SyncRelPraIndBeliViewSet,
    basename="syncretism-of-religious-practices-at-the-level-of-individual-believers",
)
router.register(
    r"rt/religious-fragmentations",
    ReligiousFragmentationViewSet,
    basename="religious-fragmentation",
)
router.register(
    r"rt/frequency-of-governmental-violence-against-religious-groups",
    GovVioFreqRelGrpViewSet,
    basename="frequency-of-governmental-violence-against-religious-groups",
)
router.register(
    r"rt/government-restrictions-on-public-worships",
    GovResPubWorViewSet,
    basename="government-restrictions-on-public-worships",
)
router.register(
    r"rt/government-restrictions-on-public-proselytizings",
    GovResPubProsViewSet,
    basename="government-restrictions-on-public-proselytizings",
)
router.register(
    r"rt/government-restrictions-on-conversions",
    GovResConvViewSet,
    basename="government-restrictions-on-conversions",
)
router.register(
    r"rt/government-pressure-to-converts",
    GovPressConvViewSet,
    basename="government-pressure-to-converts",
)
router.register(
    r"rt/government-restrictions-on-property-ownership-for-adherents-of-and-religious-groups",
    GovResPropOwnForRelGrpViewSet,
    basename="government-restrictions-on-property-ownership-for-adherents-of-and-religious-groups",
)
router.register(
    r"rt/taxes-based-on-religious-adherence-or-on-religious-activities-and-institutions",
    TaxRelAdhActInsViewSet,
    basename="taxes-based-on-religious-adherence-or-on-religious-activities-and-institutions",
)
router.register(
    r"rt/governmental-obligations-for-religious-groups-to-apply-for-official-recognitions",
    GovOblRelGrpOfcRecoViewSet,
    basename="governmental-obligations-for-religious-groups-to-apply-for-official-recognitions",
)
router.register(
    r"rt/government-restrictions-on-construction-of-religious-buildings",
    GovResConsRelBuilViewSet,
    basename="government-restrictions-on-construction-of-religious-buildings",
)
router.register(
    r"rt/government-restrictions-on-religious-educations",
    GovResRelEduViewSet,
    basename="government-restrictions-on-religious-educations",
)
router.register(
    r"rt/government-restrictions-on-circulation-of-religious-literatures",
    GovResCirRelLitViewSet,
    basename="government-restrictions-on-circulation-of-religious-literatures",
)
router.register(
    r"rt/government-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
    GovDisRelGrpOccFunViewSet,
    basename="government-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
)
router.register(
    r"rt/frequency-of-societal-violence-against-religious-groups",
    SocVioFreqRelGrpViewSet,
    basename="frequency-of-societal-violence-against-religious-groups",
)
router.register(
    r"rt/societal-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
    SocDisRelGrpOccFunViewSet,
    basename="societal-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
)
router.register(
    r"rt/societal-pressure-to-convert-or-against-conversions",
    GovPressConvForAgaViewSet,
    basename="societal-pressure-to-convert-or-against-conversions",
)


# Add views for "sc" app to the router

from .views.sc import (
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
    r"sc/polity-territories", PolityTerritoryViewSet, basename="polity-territory"
)
router.register(
    r"sc/polity-populations",
    PolityPopulationViewSet,
    basename="polity-population",
)
router.register(
    r"sc/population-of-the-largest-settlements",
    PopulationOfTheLargestSettlementViewSet,
    basename="population-of-the-largest-settlement",
)
router.register(
    r"sc/settlement-hierarchies",
    SettlementHierarchyViewSet,
    basename="settlement-hierarchy",
)
router.register(
    r"sc/administrative-levels",
    AdministrativeLevelViewSet,
    basename="administrative-level",
)
router.register(
    r"sc/religious-levels", ReligiousLevelViewSet, basename="religious-level"
)
router.register(
    r"sc/military-levels", MilitaryLevelViewSet, basename="military-level"
)
router.register(
    r"sc/professional-military-officers",
    ProfessionalMilitaryOfficerViewSet,
    basename="professional-military-officer",
)
router.register(
    r"sc/professional-soldiers",
    ProfessionalSoldierViewSet,
    basename="professional-soldier",
)
router.register(
    r"sc/professional-priesthoods",
    ProfessionalPriesthoodViewSet,
    basename="professional-priesthood",
)
router.register(
    r"sc/full-time-bureaucrats",
    FullTimeBureaucratViewSet,
    basename="full-time-bureaucrat",
)
router.register(
    r"sc/examination-systems",
    ExaminationSystemViewSet,
    basename="examination-system",
)
router.register(
    r"sc/merit-promotions", MeritPromotionViewSet, basename="merit-promotion"
)
router.register(
    r"sc/specialized-government-buildings",
    SpecializedGovernmentBuildingViewSet,
    basename="specialized-government-building",
)
router.register(
    r"sc/formal-legal-codes", FormalLegalCodeViewSet, basename="formal-legal-code"
)
router.register(r"sc/judges", JudgeViewSet, basename="judge")
router.register(r"sc/courts", CourtViewSet, basename="court")
router.register(
    r"sc/professional-lawyers",
    ProfessionalLawyerViewSet,
    basename="professional-lawyer",
)
router.register(
    r"sc/irrigation-systems",
    IrrigationSystemViewSet,
    basename="irrigation-system",
)
router.register(
    r"sc/drinking-water-supplies",
    DrinkingWaterSupplySystemViewSet,
    basename="drinking-water-supply-system",
)
router.register(r"sc/markets", MarketViewSet, basename="market")
router.register(
    r"sc/food-storage-sites", FoodStorageSiteViewSet, basename="food-storage-site"
)
router.register(r"sc/roads", RoadViewSet, basename="road")
router.register(r"sc/bridges", BridgeViewSet, basename="bridge")
router.register(r"sc/canals", CanalViewSet, basename="canal")
router.register(r"sc/ports", PortViewSet, basename="port")
router.register(
    r"sc/mines-or-quarries", MinesOrQuarryViewSet, basename="mines-or-quarry"
)
router.register(
    r"sc/mnemonic-devices", MnemonicDeviceViewSet, basename="mnemonic-device"
)
router.register(
    r"sc/nonwritten-records",
    NonwrittenRecordViewSet,
    basename="nonwritten-record",
)
router.register(
    r"sc/written-records", WrittenRecordViewSet, basename="written-record"
)
router.register(r"sc/scripts", ScriptViewSet, basename="script")
router.register(
    r"sc/non-phonetic-writings",
    NonPhoneticWritingViewSet,
    basename="non-phonetic-writing",
)
router.register(
    r"sc/phonetic-alphabetic-writings",
    PhoneticAlphabeticWritingViewSet,
    basename="phonetic-alphabetic-writing",
)
router.register(
    r"sc/lists-tables-and-classifications",
    ListsTablesAndClassificationViewSet,
    basename="lists-tables-and-classifications",
)
router.register(r"sc/calendars", CalendarViewSet, basename="calendar")
router.register(r"sc/sacred-texts", SacredTextViewSet, basename="sacred-text")
router.register(
    r"sc/religious-literatures",
    ReligiousLiteratureViewSet,
    basename="religious-literature",
)
router.register(
    r"sc/practical-literatures",
    PracticalLiteratureViewSet,
    basename="practical-literature",
)
router.register(r"sc/histories", HistoryViewSet, basename="history")
router.register(r"sc/philosophies", PhilosophyViewSet, basename="philosophy")
router.register(
    r"sc/scientific-literatures",
    ScientificLiteratureViewSet,
    basename="scientific-literature",
)
router.register(r"sc/fictions", FictionViewSet, basename="fiction")
router.register(r"sc/articles", ArticleViewSet, basename="article")
router.register(r"sc/tokens", TokenViewSet, basename="token")
router.register(
    r"sc/precious-metals", PreciousMetalViewSet, basename="precious-metal"
)
router.register(r"sc/foreign-coins", ForeignCoinViewSet, basename="foreign-coin")
router.register(
    r"sc/indigenous-coins", IndigenousCoinViewSet, basename="indigenous-coin"
)
router.register(
    r"sc/paper-currencies", PaperCurrencyViewSet, basename="paper-currency"
)
router.register(r"sc/couriers", CourierViewSet, basename="courier")
router.register(
    r"sc/postal-stations", PostalStationViewSet, basename="postal-station"
)
router.register(
    r"sc/general-postal-services",
    GeneralPostalServiceViewSet,
    basename="general-postal-service",
)
router.register(
    r"sc/communal-buildings",
    CommunalBuildingViewSet,
    basename="communal-building",
)
router.register(
    r"sc/utilitarian-public-buildings",
    UtilitarianPublicBuildingViewSet,
    basename="utilitarian-public-building",
)
router.register(
    r"sc/symbolic-buildings",
    SymbolicBuildingViewSet,
    basename="symbolic-building",
)
router.register(
    r"sc/entertainment-buildings",
    EntertainmentBuildingViewSet,
    basename="entertainment-building",
)
router.register(
    r"sc/knowledge-or-information-buildings",
    KnowledgeOrInformationBuildingViewSet,
    basename="knowledge-or-information-building",
)
router.register(
    r"sc/other-utilitarian-public-buildings",
    OtherUtilitarianPublicBuildingViewSet,
    basename="other-utilitarian-public-building",
)
router.register(
    r"sc/special-purpose-sites",
    SpecialPurposeSiteViewSet,
    basename="special-purpose-site",
)
router.register(
    r"sc/ceremonial-sites", CeremonialSiteViewSet, basename="ceremonial-site"
)
router.register(r"sc/burial-sites", BurialSiteViewSet, basename="burial-site")
router.register(
    r"sc/trading-emporia", TradingEmporiaViewSet, basename="trading-emporium"
)
router.register(r"sc/enclosures", EnclosureViewSet, basename="enclosure")
router.register(
    r"sc/length-measurement-systems",
    LengthMeasurementSystemViewSet,
    basename="length-measurement-system",
)
router.register(
    r"sc/area-measurement-systems",
    AreaMeasurementSystemViewSet,
    basename="area-measurement-system",
)
router.register(
    r"sc/volume-measurement-systems",
    VolumeMeasurementSystemViewSet,
    basename="volume-measurement-system",
)
router.register(
    r"sc/weight-measurement-systems",
    WeightMeasurementSystemViewSet,
    basename="weight-measurement-system",
)
router.register(
    r"sc/time-measurement-systems",
    TimeMeasurementSystemViewSet,
    basename="time-measurement-system",
)
router.register(
    r"sc/geometrical-measurement-systems",
    GeometricalMeasurementSystemViewSet,
    basename="geometrical-measurement-system",
)
router.register(
    r"sc/other-measurement-systems",
    OtherMeasurementSystemViewSet,
    basename="other-measurement-system",
)
router.register(
    r"sc/debt-and-credit-structures",
    DebtAndCreditStructureViewSet,
    basename="debt-and-credit-structure",
)
router.register(
    r"sc/stores-of-wealth", StoreOfWealthViewSet, basename="store-of-wealth"
)
router.register(
    r"sc/sources-of-support", SourceOfSupportViewSet, basename="source-of-support"
)
router.register(
    r"sc/occupational-complexities",
    OccupationalComplexityViewSet,
    basename="occupational-complexity",
)
router.register(
    r"sc/special-purpose-houses",
    SpecialPurposeHouseViewSet,
    basename="special-purpose-house",
)
router.register(
    r"sc/other-special-purpose-sites",
    OtherSpecialPurposeSiteViewSet,
    basename="other-special-purpose-site",
)
router.register(
    r"sc/largest-communication-distances",
    LargestCommunicationDistanceViewSet,
    basename="largest-communication-distance",
)
router.register(
    r"sc/fastest-individual-communications",
    FastestIndividualCommunicationViewSet,
    basename="fastest-individual-communication",
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

router.register(r"wf/long-walls", LongWallViewSet, basename="long-wall")
router.register(r"wf/coppers", CopperViewSet, basename="copper")
router.register(r"wf/bronzes", BronzeViewSet, basename="bronze")
router.register(r"wf/irons", IronViewSet, basename="iron")
router.register(r"wf/steels", SteelViewSet, basename="steel")
router.register(r"wf/javelins", JavelinViewSet, basename="javelin")
router.register(r"wf/atlatls", AtlatlViewSet, basename="atlatl")
router.register(r"wf/slings", SlingViewSet, basename="sling")
router.register(r"wf/self-bows", SelfBowViewSet, basename="self-bow")
router.register(
    r"wf/composite-bows", CompositeBowViewSet, basename="composite-bow"
)
router.register(r"wf/crossbows", CrossbowViewSet, basename="crossbow")
router.register(
    r"wf/tension-siege-engines",
    TensionSiegeEngineViewSet,
    basename="tension-siege-engine",
)
router.register(
    r"wf/sling-siege-engines",
    SlingSiegeEngineViewSet,
    basename="sling-siege-engine",
)
router.register(
    r"wf/gunpowder-siege-artilleries",
    GunpowderSiegeArtilleryViewSet,
    basename="gunpowder-siege-artillery",
)
router.register(
    r"wf/handheld-firearms", HandheldFirearmViewSet, basename="handheld-firearm"
)
router.register(r"wf/war-clubs", WarClubViewSet, basename="war-club")
router.register(r"wf/battle-axes", BattleAxeViewSet, basename="battle-axe")
router.register(r"wf/daggers", DaggerViewSet, basename="dagger")
router.register(r"wf/swords", SwordViewSet, basename="sword")
router.register(r"wf/spears", SpearViewSet, basename="spear")
router.register(r"wf/polearms", PolearmViewSet, basename="polearm")
router.register(r"wf/dogs", DogViewSet, basename="dog")
router.register(r"wf/donkeys", DonkeyViewSet, basename="donkey")
router.register(r"wf/horses", HorseViewSet, basename="horse")
router.register(r"wf/camels", CamelViewSet, basename="camel")
router.register(r"wf/elephants", ElephantViewSet, basename="elephant")
router.register(r"wf/wood-bark-etc", WoodBarkEtcViewSet, basename="wood-bark-etc")
router.register(r"wf/leathers", LeatherClothViewSet, basename="leather-cloth")
router.register(r"wf/shields", ShieldViewSet, basename="shield")
router.register(r"wf/helmets", HelmetViewSet, basename="helmet")
router.register(r"wf/breastplates", BreastplateViewSet, basename="breastplate")
router.register(
    r"wf/limb-protections", LimbProtectionViewSet, basename="limb-protection"
)
router.register(r"wf/scaled-armors", ScaledArmorViewSet, basename="scaled-armor")
router.register(
    r"wf/laminar-armors", LaminarArmorViewSet, basename="laminar-armor"
)
router.register(r"wf/plate-armors", PlateArmorViewSet, basename="plate-armor")
router.register(
    r"wf/small-vessel-canoe-etc",
    SmallVesselsCanoesEtcViewSet,
    basename="small-vessel-canoe-etc",
)
router.register(
    r"wf/merchant-ship-pressed-into-service",
    MerchantShipPressedIntoServiceViewSet,
    basename="merchant-ship-pressed-into-service",
)
router.register(
    r"wf/specialized-military-vessels",
    SpecializedMilitaryVesselViewSet,
    basename="specialized-military-vessel",
)
router.register(
    r"wf/settlement-in-defensive-positions",
    SettlementInADefensivePositionViewSet,
    basename="settlement-in-defensive-position",
)
router.register(
    r"wf/wooden-palisades", WoodenPalisadeViewSet, basename="wooden-palisade"
)
router.register(
    r"wf/earth-ramparts", EarthRampartViewSet, basename="earth-rampart"
)
router.register(r"wf/ditches", DitchViewSet, basename="ditch")
router.register(r"wf/moats", MoatViewSet, basename="moat")
router.register(
    r"wf/stone-walls-non-mortared",
    StoneWallsNonMortaredViewSet,
    basename="stone-walls-non-mortared",
)
router.register(
    r"wf/stone-walls-mortared",
    StoneWallsMortaredViewSet,
    basename="stone-walls-mortared",
)
router.register(
    r"wf/fortified-camps", FortifiedCampViewSet, basename="fortified-camp"
)
router.register(
    r"wf/complex-fortifications",
    ComplexFortificationViewSet,
    basename="complex-fortification",
)
router.register(
    r"wf/modern-fortifications",
    ModernFortificationViewSet,
    basename="modern-fortification",
)
router.register(r"wf/chainmails", ChainmailViewSet, basename="chainmail")


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