"""
All the constants used in the Seshat application.
"""

__all__ = [
    "ABSENT_PRESENT_CHOICES",
    "POLITY_LANGUAGE_CHOICES",
    "POLITY_LANGUAGE_GENUS_CHOICES",
    "POLITY_LINGUISTIC_FAMILY_CHOICES",
    "SECTIONS",
    "SUBSECTIONS",
    "LIGHT_COLORS",
    "COMMON_LABELS",
    "COMMON_FIELDS",
    "ATTRS",
    "MB3_ATTRS",
    "MB3_BOLD_ATTRS",
    "MB1_ATTRS",
    "MB3_SIMPLE_ATTRS",
    "MB1_SIMPLE_ATTRS",
    "COMMON_WIDGETS",
    "CODED_VALUE_WIDGET",
    "ICONS",
    "_ZOTERO_API_KEY",
    "ZOTERO",
    "BASIC_CONTEXT",
    "POLITY_NGA_NAME",
    "CORRECT_YEAR",
    "US_STATES_GEOJSON_PATH",
    "NO_DATA",
    "CSV_DELIMITER",
]


from django import forms
from django.db.models import (
    Case,
    F,
    CharField,
    ExpressionWrapper,
    IntegerField,
    When,
)

from decouple import config, UndefinedValueError
from pyzotero import zotero

from .types import DotDict


def _wrap(label, simple=False):
    """
    Private function to wrap a label in HTML.

    Args:
        label (str): The label to wrap in HTML.

    Returns:
        str: The label wrapped in HTML
    """
    if simple:
        return f"&nbsp;{label}:"
    return f"&nbsp;<b>{label}:</b>"


ABSENT_PRESENT_CHOICES = (
    ("present", "present"),
    ("absent", "absent"),
    ("unknown", "unknown"),
    ("A~P", "Transitional (Absent -> Present)"),
    ("P~A", "Transitional (Present -> Absent)"),
)

ABSENT_PRESENT_STRING_LIST = [f"- {x[1]}" for x in ABSENT_PRESENT_CHOICES]


POLITY_LANGUAGE_CHOICES = (
    ("Polish", "Polish"),
    ("Pashto", "Pashto"),
    ("Persian", "Persian"),
    ("Greek", "Greek"),
    ("Bactrian", "Bactrian"),
    ("Sogdian", "Sogdian"),
    ("Pahlavi", "Pahlavi"),
    ("Brahmi", "Brahmi"),
    ("Kharoshthi", "Kharoshthi"),
    ("Tocharian", "Tocharian"),
    ("Chinese", "Chinese"),
    ("archaic Chinese", "archaic Chinese"),
    ("Xiangxi", "Xiangxi"),
    ("Qiandong", "Qiandong"),
    ("Chuanqiandian", "Chuanqiandian"),
    ("Hmong-Mien", "Hmong-Mien"),
    ("Hmongic", "Hmongic"),
    ("Middle Chinese", "Middle Chinese"),
    ("Jurchen", "Jurchen"),
    ("Khitan", "Khitan"),
    ("Xianbei", "Xianbei"),
    ("Manchu language", "Manchu language"),
    ("Mongolian language", "Mongolian language"),
    ("Atanque", "Atanque"),
    ("Shuar", "Shuar"),
    ("Arabic", "Arabic"),
    ("suspected unknown", "suspected unknown"),
    ("NO_VALUE_ON_WIKI", "NO_VALUE_ON_WIKI"),
    ("Demotic", "Demotic"),
    ("Ancient Egyptian", "Ancient Egyptian"),
    ("Late Egyptian", "Late Egyptian"),
    ("demotic Egyptian", "demotic Egyptian"),
    ("Castilian Spanish", "Castilian Spanish"),
    ("Chuukese", "Chuukese"),
    ("French", "French"),
    ("Langues dOil", "Langues dOil"),
    ("Occitan", "Occitan"),
    ("Latin", "Latin"),
    ("Old Frankish", "Old Frankish"),
    ("Germanic", "Germanic"),
    ("Gallic", "Gallic"),
    ("Gaulish", "Gaulish"),
    ("English", "English"),
    ("Akan", "Akan"),
    ("Twi", "Twi"),
    ("Doric Greek", "Doric Greek"),
    ("Minoan", "Minoan"),
    ("Early Greek", "Early Greek"),
    ("Eteocretan", "Eteocretan"),
    ("Old Hawaiian", "Old Hawaiian"),
    ("Hawaiian", "Hawaiian"),
    ("Iban", "Iban"),
    ("Sanskrit", "Sanskrit"),
    ("Old Javanese", "Old Javanese"),
    ("Middle Javanese", "Middle Javanese"),
    ("Javanese", "Javanese"),
    ("Canaanite", "Canaanite"),
    ("Aramaic", "Aramaic"),
    ("Hebrew", "Hebrew"),
    ("Kannada", "Kannada"),
    ("Urdu", "Urdu"),
    ("A’chik", "A’chik"),
    ("Prakrit", "Prakrit"),
    ("Telugu", "Telugu"),
    ("Tamil", "Tamil"),
    ("Akkadian", "Akkadian"),
    ("Sumerian", "Sumerian"),
    ("Amorite", "Amorite"),
    ("Old Babylonian", "Old Babylonian"),
    ("Mesopotamian Religions", "Mesopotamian Religions"),
    ("Old Persian", "Old Persian"),
    ("Elamite", "Elamite"),
    ("Egyptian", "Egyptian"),
    ("Old Elamite", "Old Elamite"),
    ("Mongolian", "Mongolian"),
    ("native Iranian languages", "native Iranian languages"),
    ("Turkic", "Turkic"),
    ("Turkish", "Turkish"),
    ("Babylonian", "Babylonian"),
    ("Hurrian", "Hurrian"),
    ("Proto-Elamite", "Proto-Elamite"),
    ("Old Norse", "Old Norse"),
    ("Italian", "Italian"),
    ("Middle Japanese", "Middle Japanese"),
    ("Old Japanese", "Old Japanese"),
    ("Late Old Japanese", "Late Old Japanese"),
    ("Japanese", "Japanese"),
    ("Early Modern Japanese", "Early Modern Japanese"),
    ("Old Turkic", "Old Turkic"),
    ("Iranian", "Iranian"),
    ("Old Khmer", "Old Khmer"),
    ("Mon", "Mon"),
    ("Tai", "Tai"),
    ("Khmer", "Khmer"),
    ("Pali", "Pali"),
    ("Phoenician", "Phoenician"),
    ("Berber", "Berber"),
    ("Spanish", "Spanish"),
    ("Portuguese", "Portuguese"),
    ("Bambara", "Bambara"),
    ("Mande", "Mande"),
    ("Songhay", "Songhay"),
    ("Russian", "Russian"),
    ("Georgian", "Georgian"),
    ("Armenian", "Armenian"),
    ("Kereid", "Kereid"),
    ("Tatar", "Tatar"),
    ("Naimans", "Naimans"),
    ("Khalkha", "Khalkha"),
    ("Rouran", "Rouran"),
    ("Xiongnu", "Xiongnu"),
    ("Oirat", "Oirat"),
    ("Zapotec", "Zapotec"),
    ("Icelandic", "Icelandic"),
    ("Aymara", "Aymara"),
    ("Puquina", "Puquina"),
    ("Quechua", "Quechua"),
    ("Orokaiva", "Orokaiva"),
    ("unknown", "unknown"),
    ("Sindhi", "Sindhi"),
    ("Punjabi", "Punjabi"),
    ("Sakha (Yakut)", "Sakha (Yakut)"),
    ("Merotic", "Merotic"),
    ("Coptic", "Coptic"),
    ("Thai", "Thai"),
    ("Proto-Indo-European language", "Proto-Indo-European language"),
    ("Nesite", "Nesite"),
    ("Luwian", "Luwian"),
    ("Hattic", "Hattic"),
    ("Hittite", "Hittite"),
    ("Old Assyrian dialect of Akkadian", "Old Assyrian dialect of Akkadian"),
    ("Indo-European language", "Indo-European language"),
    ("Lydian", "Lydian"),
    ("Ottoman Turkish", "Ottoman Turkish"),
    ("Phrygian", "Phrygian"),
    ("Miami Illinois", "Miami Illinois"),
    ("Cayuga", "Cayuga"),
    ("Mohawk", "Mohawk"),
    ("Oneida", "Oneida"),
    ("Onondaga", "Onondaga"),
    ("Seneca", "Seneca"),
    ("Tuscarora", "Tuscarora"),
    ("Middle Mongolian", "Middle Mongolian"),
    ("Ancient Iranian", "Ancient Iranian"),
    ("Chagatai Turkish", "Chagatai Turkish"),
    ("Sabaic", "Sabaic"),
    ("Mainic", "Mainic"),
    ("Qatabanic", "Qatabanic"),
    ("Hadramawtic", "Hadramawtic"),
    ("Old Arabic", "Old Arabic"),
    ("Susu", "Susu"),
    ("Koranko", "Koranko"),
    ("Limba", "Limba"),
    ("Temne", "Temne"),
    ("Bullom", "Bullom"),
    ("Loko", "Loko"),
    ("Manding", "Manding"),
    ("Krio", "Krio"),
    ("Pulaar", "Pulaar"),
    ("Kissi", "Kissi"),
    ("Krim", "Krim"),
    ("Vai", "Vai"),
    ("Mossi", "Mossi"),
    ("Shona", "Shona"),
    ("Sinhala", "Sinhala"),
    ("Dutch", "Dutch"),
    ("Sinhalese", "Sinhalese"),
    ("Oromo", "Oromo"),
    ("Harari", "Harari"),
    ("Argobba", "Argobba"),
    ("Maay", "Maay"),
    ("Somali", "Somali"),
    ("Harla", "Harla"),
    ("Hadiyya", "Hadiyya"),
    ("Tigrinya", "Tigrinya"),
    ("Funj", "Funj"),
    ("Kafa", "Kafa"),
    ("Yemsa", "Yemsa"),
    ("Qafar", "Qafar"),
    ("Proto-Yoruba", "Proto-Yoruba"),
    ("Yoruba", "Yoruba"),
    ("Bini", "Bini"),
    ("Jukun", "Jukun"),
    ("Ajagbe", "Ajagbe"),
    ("Proto-Yoruboid", "Proto-Yoruboid"),
    ("Sokoto", "Sokoto"),
    ("Hausa", "Hausa"),
    ("Idoma", "Idoma"),
    ("Igbo", "Igbo"),
    ("Nri", "Nri"),
    ("Kanuri", "Kanuri"),
    ("Kanembu", "Kanembu"),
    ("Fongbe", "Fongbe"),
    ("Wolof", "Wolof"),
    ("Sereer", "Sereer"),
    ("Fula", "Fula"),
    ("Luganda", "Luganda"),
    ("Kinyambo", "Kinyambo"),
    ("Kinyarwanda", "Kinyarwanda"),
    ("Runyankore", "Runyankore"),
    ("Kirundi", "Kirundi"),
    ("Fipa", "Fipa"),
    ("Haya", "Haya"),
    ("Old Tamil", "Old Tamil"),
    ("Efik-Ibibio", "Efik-Ibibio"),
    ("Hungarian", "Hungarian"),
    ("Native languages", "Native languages"),
    ("German", "German"),
    ("Czech", "Czech"),
    ("Lombardic", "Lombardic"),
    ("Pukina / Puquina", "Pukina / Puquina"),
    ("Old English", "Old English"),
    ("Middle-Modern Persian", "Middle-Modern Persian"),
    ("Anglo-Norman", "Anglo-Norman"),
    ("Pictish", "Pictish"),
)

POLITY_LANGUAGE_GENUS_CHOICES = (
    ("NO_VALUE_ON_WIKI", "NO_VALUE_ON_WIKI"),
    ("Afro-Asiatic", "Afro-Asiatic"),
    ("Indo-European", "Indo-European"),
    ("suspected unknown", "suspected unknown"),
)

POLITY_LINGUISTIC_FAMILY_CHOICES = (
    ("Indo-European", "Indo-European"),
    ("Sino-Tibetan", "Sino-Tibetan"),
    ("NO_VALUE_ON_WIKI", "NO_VALUE_ON_WIKI"),
    ("Tungusic", "Tungusic"),
    ("Altaic", "Altaic"),
    ("Mongolic", "Mongolic"),
    ("Chibcha", "Chibcha"),
    ("Chicham", "Chicham"),
    ("Afro-Asiatic", "Afro-Asiatic"),
    ("Oceanic-Austronesian", "Oceanic-Austronesian"),
    ("Celtic", "Celtic"),
    ("Niger-Congo", "Niger-Congo"),
    ("Kwa", "Kwa"),
    ("Hamito-Semitic", "Hamito-Semitic"),
    ("Austronesian", "Austronesian"),
    ("Malayo-Polynesian", "Malayo-Polynesian"),
    ("Semitic", "Semitic"),
    ("Indo-Iranian", "Indo-Iranian"),
    ("Dravidian", "Dravidian"),
    ("isolate language", "isolate language"),
    ("West Semetic", "West Semetic"),
    ("isolate", "isolate"),
    ("suspected unknown", "suspected unknown"),
    ("language isolate", "language isolate"),
    ("none", "none"),
    ("Germanic", "Germanic"),
    ("Japonic", "Japonic"),
    ("Turkic", "Turkic"),
    ("Austro-Asiatic, Mon-Khmer", "Austro-Asiatic, Mon-Khmer"),
    ("Austro-Asiatic", "Austro-Asiatic"),
    ("unknown", "unknown"),
    ("Mande", "Mande"),
    ("Songhay", "Songhay"),
    ("Oghuz", "Oghuz"),
    ("Kartvelian", "Kartvelian"),
    ("Manchu-Tungusic", "Manchu-Tungusic"),
    ("Proto-Mongolic", "Proto-Mongolic"),
    ("Otomanguean", "Otomanguean"),
    ("Proto-Otomanguean", "Proto-Otomanguean"),
    ("Mixe-Zoquean", "Mixe-Zoquean"),
    ("Aymaran", "Aymaran"),
    ("Quechuan", "Quechuan"),
    ("Papuan Languages", "Papuan Languages"),
    ("Tai-Kadai", "Tai-Kadai"),
    ("Algonquian", "Algonquian"),
    ("Iroquois", "Iroquois"),
    ("Iranian", "Iranian"),
    ("Creoles and Pidgins", "Creoles and Pidgins"),
    ("Indo-Aryan", "Indo-Aryan"),
    ("Yoruboid", "Yoruboid"),
    ("Edoid", "Edoid"),
    ("Proto-Bene-Kwa", "Proto-Bene-Kwa"),
    ("Chadic", "Chadic"),
    ("Saharan", "Saharan"),
    ("Southern Dravidian", "Southern Dravidian"),
    ("Uralic", "Uralic"),
    ("Romance", "Romance"),
    ("West Germanic", "West Germanic"),
)

SECTIONS = DotDict(
    {
        "general": "General Variables",
        "wf": "Warfare Variables",
        "economy": "Economy Variables",
        "conflict": "Conflict Variables",
        "sc": "Social Complexity",
        "wb": "Well Being",
    }
)

SUBSECTIONS = DotDict(
    {
        "wf": DotDict(
            {
                "MilitaryTechnologies": "Military Technologies",
                "MilitaryUseOfMetals": "Military use of Metals",
                "Projectiles": "Projectiles",
                "HandheldWeapons": "Handheld weapons",
                "AnimalsUsedInWarfare": "Animals used in warfare",
                "Armor": "Armor",
                "NavalTechnology": "Naval technology",
                "Fortifications": "Fortifications",
            }
        ),
        "crisisdb": DotDict(
            {
                "Productivity": "Productivity",
                "StateFinances": "State Finances",
                "BiologicalWellbeing": "Biological Well-Being",
                "ExternalConflicts": "External Conflicts Subsection",
                "InternalConflicts": "Internal Conflicts Subsection",
                "SocialScale": "Social Scale",
            }
        ),
        "sc": DotDict(
            {
                "Staff": "Staff",
                "SocialScale": "Social Scale",
                "HierarchicalComplexity": "Hierarchical Complexity",
                "Professions": "Professions",
                "BureaucracyCharacteristics": "Bureaucracy Characteristics",
                "Law": "Law",
                "SpecializedBuildings": "Specialized Buildings",
                "TransportInfrastructure": "Transport infrastructure",
                "SpecialPurposeSites": "Special purpose sites",
                "WritingSystems": "Writing Systems",
                "WrittenDocuments": "Kinds of Written Documents",
                "FormsOfMoney": "Forms of money",
                "PostalSystems": "Postal systems",
                "Information": "Information",
            }
        ),
        "general": DotDict(
            {
                "General": "General",
            }
        ),
    }
)

STANDARD_SETTINGS = DotDict({"null_meaning": "The value is not available."})

LIGHT_COLORS = [
    "#e6b8af",
    "#f4cccc",
    "#fce5cd",
    "#fff2cc",
    "#d9ead3",
    "#d0e0e3",
    "#c9daf8",
    "#cfe2f3",
    "#d9d2e9",
    "#ead1dc",
    "#dd7e6b",
    "#ea9999",
    "#f9cb9c",
    "#ffe599",
    "#b6d7a8",
    "#a2c4c9",
    "#a4c2f4",
    "#9fc5e8",
    "#b4a7d6",
    "#d5a6bd",
    "#cc4125",
    "#e06666",
    "#f6b26b",
    "#ffd966",
    "#93c47d",
    "#76a5af",
    "#6d9eeb",
    "#6fa8dc",
    "#8e7cc3",
    "#c27ba0",
]


COMMON_LABELS = {
    "year_from": "Start Year",
    "year_to": "End Year",
    "tag": "Confidence Level",
    "is_disputed": _wrap("There is a Dispute?"),
    "is_uncertain": _wrap("There is Uncertainty?"),
    "expert_reviewed": _wrap("Expert Checked?", True),
    "drb_reviewed": _wrap("Data Review Board Reviewed?", True),
    "citations": "Add one or more Citations",
    "finalized": "This piece of data is verified.",
}

COMMON_FIELDS = [
    "polity",
    "year_from",
    "year_to",
    "description",
    "tag",
    "is_disputed",
    "is_uncertain",
    "expert_reviewed",
    "drb_reviewed",
    "finalized",
    "citations",
]

MB3_ATTRS = {"class": "form-control mb-3"}
MB3_BOLD_ATTRS = {"class": "form-control mb-3 fw-bold"}
MB1_ATTRS = {"class": "form-control mb-1"}
MB3_SIMPLE_ATTRS = {"class": "mb-3"}
MB1_SIMPLE_ATTRS = {"class": "mb-1"}

ATTRS = DotDict(
    {
        "MB3_ATTRS": {"class": "form-control mb-3"},
        "MB3_BOLD_ATTRS": {"class": "form-control mb-3 fw-bold"},
        "MB1_ATTRS": {"class": "form-control mb-1"},
        "MB3_SIMPLE_ATTRS": {"class": "mb-3"},
        "MB1_SIMPLE_ATTRS": {"class": "mb-1"},
    }
)

ATTRS_HTML = DotDict(
    {
        "text_secondary": 'class="text-secondary"',
        "text_secondary_italic": 'class="text-secondary fst-italic"',
        "text_green_bold": 'class="text-success fw-bold"',
        "text_bold": 'class="fw-bold"',
        "text_danger": 'class="text-danger"',
    }
)

COMMON_WIDGETS = {
    "polity": forms.Select(
        attrs={
            "class": "form-control mb-3 js-example-basic-single",
            "id": "id_polity",
            "name": "polity",
        }
    ),
    "year_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
    "year_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
    "description": forms.Textarea(
        attrs=dict(
            MB3_ATTRS,
            **{
                "style": "height: 240px; line-height: 1.2;",
                "placeholder": "Add a meaningful description (optional)\n\
Note: USe §REF§ opening and closing tags to include citations to the description.\n\
Example: §REF§Chadwick, J. 1976. The Mycenaean World, Cambridge, p.78.§REF§.",
            },
        )
    ),
    "citations": forms.SelectMultiple(
        attrs={
            "class": "form-control mb-3 js-states js-example-basic-multiple",
            "text": "citations[]",
            "style": "height: 340px",
            "multiple": "multiple",
        }
    ),
    "tag": forms.RadioSelect(),
    "is_disputed": forms.CheckboxInput(attrs=ATTRS.MB3_SIMPLE_ATTRS),
    "is_uncertain": forms.CheckboxInput(attrs=ATTRS.MB3_SIMPLE_ATTRS),
    "expert_reviewed": forms.CheckboxInput(attrs=ATTRS.MB3_SIMPLE_ATTRS),
    "drb_reviewed": forms.CheckboxInput(attrs=ATTRS.MB3_SIMPLE_ATTRS),
    "finalized": forms.CheckboxInput(
        attrs=dict(MB3_ATTRS, **{"checked": True})
    ),
}

CODED_VALUE_WIDGET = {"coded_value": forms.Select(attrs=ATTRS.MB3_ATTRS)}

ICONS = DotDict(
    {
        "book": '<i class="fa-solid fa-book"></i>',
        "check": '<i class="fa-solid fa-check text-success"></i>',
        "xmark": '<i class="fa-sharp fa-solid fa-xmark text-danger"></i>',
        "triangle_exclamation": '<i class="fa-solid fa-triangle-exclamation"></i>',
        "caret_right": '<i class="fa-solid fa-caret-right"></i>',
    }
)

# Setting up Zotero
# - use ZOTERO.client to access the Zotero API
try:
    _ZOTERO_API_KEY = config("ZOTERO_API_KEY")
except UndefinedValueError:
    print(
        "Zotero key not found - setting to empty string."
    )  # TODO: add logger?
    _ZOTERO_API_KEY = ""

ZOTERO = DotDict(
    {
        "LIBRARY_ID": 1051264,
        "LIBRARY_TYPE": "group",
        "API_KEY": _ZOTERO_API_KEY,
        "BASEURL": "https://www.zotero.org/groups/1051264/seshat_databank/items/",
    }
)
ZOTERO.client = zotero.Zotero(
    ZOTERO.LIBRARY_ID, ZOTERO.LIBRARY_TYPE, ZOTERO.API_KEY
)

BASIC_CONTEXT = {
    "pols_data": [],
    "general_data": [],
    "sc_data": [],
    "wf_data": [],
    "crisisdb": [],
    "pt_data": [],
    "cc_data": [],
    "hs_data": [],
    "sr_data": [],
    "general_examples": [
        (
            "Alternative Name",
            "polity_alternative_names_all",
            "Identity and Location",
        ),
        ("Polity Peak Years", "polity_peak_yearss_all", "Temporal Bounds"),
        ("Polity Capital", "polity_capitals_all", "Identity and Location"),
        ("Polity Language", "polity_languages_all", "Language"),
        ("Polity Religion", "polity_religions_all", "Religion"),
        (
            "Degree of Centralization",
            "polity_degree_of_centralizations_all",
            "Temporal Bounds",
        ),
        (
            "Succeeding Entity",
            "polity_succeeding_entitys_all",
            "Supra-cultural relations",
        ),
        (
            "Relationship to Preceding Entity",
            "polity_relationship_to_preceding_entitys_all",
            "Supra-cultural relations",
        ),
    ],
    "sc_examples": [
        ("Polity Territory", "polity_territorys_all", "Social Scale"),
        ("Polity Population", "polity_populations_all", "Social Scale"),
        (
            "Settlement Hierarchy",
            "settlement_hierarchys_all",
            "Hierarchical Complexity",
        ),
        (
            "Irrigation System",
            "irrigation_systems_all",
            "Specialized Buildings: polity owned",
        ),
        (
            "Merit Promotion",
            "merit_promotions_all",
            "Bureaucracy Characteristics",
        ),
        ("Formal Legal Code", "formal_legal_codes_all", "Law"),
        ("Road", "roads_all", "Transport Infrastructure"),
        (
            "Postal Station",
            "postal_stations_all",
            "Information / Postal System",
        ),
    ],
    "wf_examples": [
        ("Bronze", "bronzes_all", "Military use of Metals"),
        ("Javelin", "javelins_all", "Projectiles"),
        ("Battle Axe", "battle_axes_all", "Handheld Weapons"),
        ("Sword", "swords_all", "Handheld Weapons"),
        ("Horse", "horses_all", "Animals used in warfare"),
        (
            "Small Vessels (canoes, etc)",
            "small_vessels_canoes_etcs_all",
            "Naval technology",
        ),
        ("Shield", "shields_all", "Armor"),
        ("Wooden Palisade", "small_vessels_canoes_etcs_all", "Fortifications"),
    ],
}

POLITY_NGA_NAME = ExpressionWrapper(
    F("polity__home_nga__name"), output_field=CharField()
)

CORRECT_YEAR = Case(
    When(year_from__isnull=False, then=F("year_from")),
    default=F("polity__start_year"),
    output_field=IntegerField(),
)

US_STATES_GEOJSON_PATH = "/home/majid/dev/seshat/seshat/seshat/apps/core/static/geojson/us_states_geojson.json"  # noqa: E501 pylint: disable=C0301

NO_DATA = DotDict(
    {
        "explanation": "No_Explanations",
        "section": "No_SECTION",
        "subsection": "NO_SUBSECTION",
        "name": "NO_NAME",
        "nga": "NO_NGA_ASSOCIATED",
        "wiki": "No_Value_Provided_in_Old_Wiki"
    }
)

CSV_DELIMITER = "|"

STANDARD_CONDITIONS = [
    lambda o: o.polity.start_year is not None,
    lambda o: o.year_from is not None,
    lambda o: o.polity.start_year > o.year_from,
]
