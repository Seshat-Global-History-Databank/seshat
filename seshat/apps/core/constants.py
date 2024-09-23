__all__ = [
    "POLITY_TAG_CHOICES",
    "WORLD_REGION_CHOICES",
    "CERTAINTY",
    "TAGS",
    "APS",
    "AP",
    "NFY",
    "UU",
    "AA",
    "U",
    "PP",
    "PS",
    "AS",
    "P_TO_A",
    "A_TO_P",
    "CUSTOM_ORDER",
    "CUSTOM_ORDER_SR",
    "APP_MAP",
    "CATEGORICAL_VARIABLES",
    "WORLD_MAP_INITIAL_DISPLAYED_YEAR",
    "WORLD_MAP_INITIAL_POLITY",
]

from ..constants import (
    POLITY_LINGUISTIC_FAMILY_CHOICES,
    POLITY_LANGUAGE_GENUS_CHOICES,
    POLITY_LANGUAGE_CHOICES,
)

TAGS = (
    ("TRS", "Confident"),
    ("SSP", "Suspected"),
    ("IFR", "Inferred"),
)

APS = "A;P*"
AP = "A;P"
NFY = "NFY"
UU = "U*"
AA = "A"
U = "U"
PP = "P"
PS = "P*"
AS = "A*"
P_TO_A = "P~A"
A_TO_P = "A~P"

POLITY_TAG_CHOICES = (
    ("LEGACY", "Equinox 2020 Polities"),
    ("POL_AFR_EAST", "NEW East African Polities"),  # Africa ----> East Africa*
    ("POL_AFR_WEST", "NEW West African Polities"),  # Africa ---->  West Africa
    (
        "POL_AFR_SA",
        "NEW Southern African Polities",
    ),  # Africa ----> Southern Africa*
    (
        "POL_SA_SI",
        "NEW South East Indian Polities",
    ),  # South Asia ----> Southern India*
    ("CRISISDB_POLITIES", "CrisisDB-specific Polities"),
    ("OTHER_TAG", "Other Polities"),
)

WORLD_REGION_CHOICES = (
    ("Europe", "Europe"),
    ("Southwest Asia", "Southwest Asia"),
    ("Africa", "Africa"),
    ("Central Eurasia", "Central Eurasia"),
    ("South Asia", "South Asia"),
    ("Southeast Asia", "Southeast Asia"),
    ("East Asia", "East Asia"),
    ("Oceania-Australia", "Oceania-Australia"),
    ("North America", "North America"),
    ("South America", "South America"),
)

CERTAINTY = (
    (AP, "scholarly disagreement or uncertainty"),
    (UU, "Suspected Unknown"),
    (AA, "Absent"),
    (PP, "Present"),
    (AS, "Inferred Absent"),
    (PS, "Inferred Present"),
    (NFY, "not applicable; no other code is appropriate"),
    (U, "Unknown"),
    (P_TO_A, "uncertainty about when a given trait disappears"),
    (A_TO_P, "uncertainty about when a given trait appears"),
)


CUSTOM_ORDER = [
    5,
    2,
    11,
    3,
    4,
    9,
    10,
    8,
    7,
    6,
    1,
    23,
    24,
    27,
    26,
    25,
    29,
    28,
    31,
    33,
    32,
    30,
]

CUSTOM_ORDER_SR = [
    20,
    18,
    17,
    15,
    19,
    16,
    3,
    4,
    5,
    7,
    1,
    2,
    6,
    43,
    61,
    62,
    44,
    45,
    10,
    13,
    8,
    9,
    11,
    12,
    14,
    58,
    59,
    38,
    39,
    37,
    36,
    40,
    41,
    42,
    28,
    29,
    30,
    26,
    25,
    27,
    24,
    22,
    23,
    21,
    32,
    31,
    33,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
    123,
    124,
    125,
    126,
    127,
    128,
    129,
    130,
    131,
    132,
    133,
    134,
    135,
    136,
    137,
    138,
    139,
    140,
    141,
    142,
    143,
    144,
    145,
    146,
    147,
    148,
    149,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
]


# Get all the variables used in the map view
APP_MAP = {
    "sc": "Social Complexity Variables",
    "wf": "Warfare Variables (Military Technologies)",
    # TODO: Implemented but temporarily restricted. Uncomment when ready.
    # 'rt': 'Religion Tolerance',
    # TODO: Partially implmented and hardcoded in assign_categorical_variables_to_shapes.
    # 'general': 'General Variables',
}


# Get sorted lists of choices for each categorical variable
CATEGORICAL_VARIABLES = {
    "linguistic_family": sorted(
        [x[0] for x in POLITY_LINGUISTIC_FAMILY_CHOICES]
    ),
    "language_genus": sorted([x[0] for x in POLITY_LANGUAGE_GENUS_CHOICES]),
    "language": sorted([x[0] for x in POLITY_LANGUAGE_CHOICES]),
}

WORLD_MAP_INITIAL_DISPLAYED_YEAR = 117
WORLD_MAP_INITIAL_POLITY = "it_roman_principate"
