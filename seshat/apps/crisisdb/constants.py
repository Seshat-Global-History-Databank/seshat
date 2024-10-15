__all__ = [
    "TAGS_DIC",
    "NO_SECTION_DICT",
    "QING_VARS",
]


from ..constants import TAGS

from .forms import (
    Power_transitionForm,
    Crisis_consequenceForm,
    Human_sacrificeForm,
    External_conflictForm,
    Internal_conflictForm,
    External_conflict_sideForm,
    Agricultural_populationForm,
    Arable_landForm,
    Arable_land_per_farmerForm,
    Gross_grain_shared_per_agricultural_populationForm,
    Net_grain_shared_per_agricultural_populationForm,
    SurplusForm,
    Military_expenseForm,
    Silver_inflowForm,
    Silver_stockForm,
    Total_populationForm,
    Gdp_per_capitaForm,
    Drought_eventForm,
    Locust_eventForm,
    Socioeconomic_turmoil_eventForm,
    Crop_failure_eventForm,
    Famine_eventForm,
    Disease_outbreakForm,
    Us_locationForm,
    Us_violence_subtypeForm,
    Us_violence_data_sourceForm,
    Us_violenceForm,
)
from .models import (
    Power_transition,
    Crisis_consequence,
    Human_sacrifice,
    External_conflict,
    Internal_conflict,
    External_conflict_side,
    Agricultural_population,
    Arable_land,
    Arable_land_per_farmer,
    Gross_grain_shared_per_agricultural_population,
    Net_grain_shared_per_agricultural_population,
    Surplus,
    Military_expense,
    Silver_inflow,
    Silver_stock,
    Total_population,
    Gdp_per_capita,
    Drought_event,
    Locust_event,
    Socioeconomic_turmoil_event,
    Crop_failure_event,
    Famine_event,
    Disease_outbreak,
    Us_location,
    Us_violence_subtype,
    Us_violence_data_source,
    Us_violence,
)


# NOTE: TAGS_DIC had some leftover tags from past code - better to generate this
# dynamically
# TAGS_DIC = {
#     "TRS": "Evidenced",
#     "DSP": "Disputed",
#     "SSP": "Suspected",
#     "IFR": "Inferred",
#     "UNK": "Unknown",
# }

TAGS_DIC = dict(TAGS)

# TODO: Can we remove the NO_SECTION_DICT - doesn't look like it does anything?
NO_SECTION_DICT = {
    "myvar": "Z",
}

QING_VARS = {
    "Economy Variables": {
        "Productivity": [
            [
                "Agricultural population",
                "agricultural_populations",
                "agricultural_population-create",
                "agricultural_population-download",
                "agricultural_population-metadownload",
            ],
            [
                "Arable land",
                "arable_lands",
                "arable_land-create",
                "arable_land-download",
                "arable_land-metadownload",
            ],
            [
                "Arable land per farmer",
                "arable_land_per_farmers",
                "arable_land_per_farmer-create",
                "arable_land_per_farmer-download",
                "arable_land_per_farmer-metadownload",
            ],
            [
                "Gross grain shared per agricultural population",
                "gross_grain_shared_per_agricultural_populations",
                "gross_grain_shared_per_agricultural_population-create",
                "gross_grain_shared_per_agricultural_population-download",
                "gross_grain_shared_per_agricultural_population-metadownload",
            ],
            [
                "Net grain shared per agricultural population",
                "net_grain_shared_per_agricultural_populations",
                "net_grain_shared_per_agricultural_population-create",
                "net_grain_shared_per_agricultural_population-download",
                "net_grain_shared_per_agricultural_population-metadownload",
            ],
            [
                "Surplus",
                "surplus",
                "surplus-create",
                "surplus-download",
                "surplus-metadownload",
            ],
            [
                "Gdp per capita",
                "gdp_per_capitas",
                "gdp_per_capita-create",
                "gdp_per_capita-download",
                "gdp_per_capita-metadownload",
            ],
        ],
        "State Finances": [
            [
                "Military expense",
                "military_expenses",
                "military_expense-create",
                "military_expense-download",
                "military_expense-metadownload",
            ],
            [
                "Silver inflow",
                "silver_inflows",
                "silver_inflow-create",
                "silver_inflow-download",
                "silver_inflow-metadownload",
            ],
            [
                "Silver stock",
                "silver_stocks",
                "silver_stock-create",
                "silver_stock-download",
                "silver_stock-metadownload",
            ],
        ],
    },
    "Social Complexity Variables": {
        "Social Scale": [
            [
                "Total population",
                "total_populations",
                "total_population-create",
                "total_population-download",
                "total_population-metadownload",
            ]
        ]
    },
    "Well Being": {
        "Biological Well-Being": [
            [
                "Drought event",
                "drought_events",
                "drought_event-create",
                "drought_event-download",
                "drought_event-metadownload",
            ],
            [
                "Locust event",
                "locust_events",
                "locust_event-create",
                "locust_event-download",
                "locust_event-metadownload",
            ],
            [
                "Socioeconomic turmoil event",
                "socioeconomic_turmoil_events",
                "socioeconomic_turmoil_event-create",
                "socioeconomic_turmoil_event-download",
                "socioeconomic_turmoil_event-metadownload",
            ],
            [
                "Crop failure event",
                "crop_failure_events",
                "crop_failure_event-create",
                "crop_failure_event-download",
                "crop_failure_event-metadownload",
            ],
            [
                "Famine event",
                "famine_events",
                "famine_event-create",
                "famine_event-download",
                "famine_event-metadownload",
            ],
            [
                "Disease outbreak",
                "disease_outbreaks",
                "disease_outbreak-create",
                "disease_outbreak-download",
                "disease_outbreak-metadownload",
            ],
        ]
    },
}

model_form_pairs = [
    (Us_location, Us_locationForm, "us_location"),
    (Us_violence_subtype, Us_violence_subtypeForm, "us_violence_subtype"),
    (
        Us_violence_data_source,
        Us_violence_data_sourceForm,
        "us_violence_data_source",
    ),
    (Us_violence, Us_violenceForm, "us_violence"),
    (Power_transition, Power_transitionForm, "power_transition"),
    (Crisis_consequence, Crisis_consequenceForm, "crisis_consequence"),
    (Human_sacrifice, Human_sacrificeForm, "human_sacrifice"),
    (External_conflict, External_conflictForm, "external_conflict"),
    (Internal_conflict, Internal_conflictForm, "internal_conflict"),
    (
        External_conflict_side,
        External_conflict_sideForm,
        "external_conflict_side",
    ),
    (
        Agricultural_population,
        Agricultural_populationForm,
        "agricultural_population",  # noqa: E501  TODO: I fixed spelling here, which will make previous URLs dysfunctional
    ),
    (Arable_land, Arable_landForm, "arable_land"),
    (
        Arable_land_per_farmer,
        Arable_land_per_farmerForm,
        "arable_land_per_farmer",
    ),
    (
        Gross_grain_shared_per_agricultural_population,
        Gross_grain_shared_per_agricultural_populationForm,
        "gross_grain_shared_per_agricultural_population",
    ),
    (
        Net_grain_shared_per_agricultural_population,
        Net_grain_shared_per_agricultural_populationForm,
        "net_grain_shared_per_agricultural_population",
    ),
    (Surplus, SurplusForm, "surplus"),
    (Military_expense, Military_expenseForm, "military_expense"),
    (Silver_inflow, Silver_inflowForm, "silver_inflow"),
    (Silver_stock, Silver_stockForm, "silver_stock"),
    (Total_population, Total_populationForm, "total_population"),
    (Gdp_per_capita, Gdp_per_capitaForm, "gdp_per_capita"),
    (Drought_event, Drought_eventForm, "drought_event"),
    (Locust_event, Locust_eventForm, "locust_event"),
    (
        Socioeconomic_turmoil_event,
        Socioeconomic_turmoil_eventForm,
        "socioeconomic_turmoil_event",
    ),
    (Crop_failure_event, Crop_failure_eventForm, "crop_failure_event"),
    (Famine_event, Famine_eventForm, "famine_event"),
    (Disease_outbreak, Disease_outbreakForm, "disase_outbreak"),
]
