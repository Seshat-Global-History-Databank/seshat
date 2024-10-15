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
        "rt": "Religious Tolerance",
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
        "rt": DotDict(
            {
                "ReligiousLandscape": "Religious Landscape",
                "GovernmentRestrictions": "Government Restrictions",
                "SocietalRestrictions": "Societal Restrictions",
            }
        ),
    }
)

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
        "default": " - ",
        "explanation": "No_Explanations",
        "section": "No_SECTION",
        "subsection": "NO_SUBSECTION",
        "name": "NO_NAME",
        "nga": "NO_NGA_ASSOCIATED",
        "wiki": "No_Value_Provided_in_Old_Wiki",
        "note": "No_Actual_note",
        "no_value": "The value is not available.",
        "nothing": "NOTHING",
        "private_comments": "NO_Private_COMMENTS_TO_SHOW",
        "titles": "NO_TITLES_PROVIDED",
        "ref_no_title": "REFERENCE_WITH_NO_TITLE",
        "ref_no_long_name": "REFERENCE_WITH_NO_LONG_NAME",
        "bad_reference": "BADBADREFERENCE",
        "comment_parts": " Nothing ",
        "descriptions": "No descriptions.",
        "comment": "EMPTY_COMMENT",
    }
)

CSV_DELIMITER = ","  # TODO: this one was set to "|" in the past; not standard


ATTENTION_TAGS_CHOICES = (
    ("NeedsExpertInput", "Needs Expert Input"),
    ("IsInconsistent", "Is Inconsistent"),
    ("IsWrong", "Is Wrong"),
    ("IsOk", "IS OK"),
)

VIOLENCE_TYPE_CHOICES = (
    ("lynching", "lynching"),
    ("riot", "riot"),
    ("executions", "executions"),
    ("war", "war"),
    ("assassination", "assassination"),
    ("compilation", "compilation"),
    ("terrorism", "terrorism"),
    ("insurrection", "insurrection"),
    ("mass suicide", "mass suicide"),
    ("unknown", "unknown"),
    ("revenge", "revenge"),
)

CRISIS_DEFS_EXAMPLES = {
    "decline": f"""
        <p {ATTRS_HTML.text_secondary}>
            {ICONS.caret_right} Significant population decline (a loose guide is <span {ATTRS_HTML.text_green_bold}>a loss of roughly >10%</span> of total population) which may be caused by factors such as natural disasters, epidemic, famine, or ongoing warfare. Specify the extent of the decline where possible.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: During the Ayyubid Sultanate of 1200 there was a devastating famine which forced some parts of the population into cannibalism.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "collapse": f"""
        <p {ATTRS_HTML.text_secondary}>
            <span {ATTRS_HTML.text_green_bold}>Severe decline (e.g., >50%)</span> or dissolution of a population to a point where it is unable to recover. Specify the extent of the collapse of the population where possible. Generally this involves ‘extinction’ or near-extinction of ethnic, linguistic, or other cultural groups.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The Inca Empire suffered catastrophic losses due to the outbreak of smallpox which was quickly followed by the Spanish conquest. The population was approximately 9 million in 1520 before the arrival of the Spanish and fell to 600,000 by 1620.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "epidemic": f"""
        <p {ATTRS_HTML.text_secondary}>
            Severe outbreak of infectious disease which affects a large portion of the population, such as plague, cholera or smallpox. If estimates or exact figures of those infected or killed are known, specify them.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  In 1596 Habsburg Spain suffered a plague which spread across the entire of mainland Spain and killed an estimated 500,000 people in six years.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "downward_mobility": f"""
        <p {ATTRS_HTML.text_secondary}>
            This refers to the downward mobility - such as loss of power, land, title or privilege - among a large portion of the elite and often their supporters. Events concerning an individual, such as a royal family member being exiled, are not considered here.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: After the Genpei Civil War in 1185 all members of the Minamoto clan were removed from their posts at court and exiled.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "extermination": f"""
        <p {ATTRS_HTML.text_secondary}>
            The mass killing and/or expulsion of an elite group such as a clan or a ruler and their noble supporters. The end of a dynasty is not included here unless it was accompanied by the slaughter of a specific elite group.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: Following the Genkō Civil War in 1333, the entire of the Hōjō clan were forced to commit suicide by the reinstated emperor, Go-Daigo.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "uprising": f"""
        <p {ATTRS_HTML.text_secondary}>
            [NB: formerly "Revolution"]. Widespread serious revolt, rebellion, coup d’etat, or uprising which is often violent (but need not be led by armed groups) and/or leads to significant institutional changes in the polity. Note where possible if uprising is led by elites, military officials, popular / laborer groups (rural or urban), or a combination.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The Mexican War of Independence 1810-1821 was a series of simultaneous regional and local armed conflicts against Spanish rule, which led to the break from Spain and the establishment of the Mexican Empire.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "revolution": f"""
        <p {ATTRS_HTML.text_secondary}>
            Revolution is the attempted forcible overthrow of a government through mass mobilization (whether military or civilian or both) in the name of social justice, inclduing national liberation or ethno-nationalist movements, to create new political institutions. This is distinct from rebeliions and other uprisings that do not necesarrily involve mass mobilization or seek systemic / governmental change (though they can). Revolutions is thus here viewed as a special type of Uprising. These definitions follow: Goldstone 2014 Revolutions: A Very Short Introduction | Goldstone, Jack A., Leonid Grinin, and Andrey Korotayev. Handbook of Revolutions in the 21st Century: The New Waves of Revolutions, and the Causes and Effects of Disruptive Political Change. Springer Nature, 2022.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The failed Czech / Bohemian revolts of during the 30 Years War sought to liberate the territory from Habsburg control and reject Catholic influence .
        </p>""",  # noqa: E501 pylint: disable=C0301
    "successful_revolution": f"""
        <p {ATTRS_HTML.text_secondary}>
            A revolution that succeeds in overthrowing the existing ruler / governmental systems and/or creating a new independent polity.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: French Revolution of 1789 was an elite-led mass mobilization leading to the overthrow of the French Monarchy.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "civil_war": f"""
        <p {ATTRS_HTML.text_secondary}>
            A violent conflict between citizens of the same polity, usually between the state and one or more organized groups, or between two or more organized groups following state collapse.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: In 1727 upon the death of Sultan Isma&rsquo;il of the Alaouite Dynasty, a succession crisis between his sons led to factions within court and the country went to war until 1757.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "century_plus": f"""
        <p {ATTRS_HTML.text_secondary}>
            Any crisis which lasts for a century or more. This may be a string of events such as uprisings, war, and disease during the crisis period rather than one long event.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  In Crete during the late fourth century constant elite in-fighting led to a near-collapse of the aristocratic order and constant warfare, which lasted for hundreds of years, between the city states of Gortyn, Kydonia (Chania), Lyttos, Polyrrhenia and Knossos weakened Crete&rsquo;s economy.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "fragmentation": f"""
        <p {ATTRS_HTML.text_secondary}>
            The division of part, or all, of a polity and its territories into quasi-polities or independent states.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: During the civil wars of the State of Jin in the 5th-and-6th centuries BCE, the Han, Wei and Zhao clans formed an alliance to defeat the more powerful Zhi clan. This resulted in the Partition of Jin in 453 BCE whereby Zhi lands and the rest of Jin were divided between the three successor states who were later known as the Three Jins.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "capital": f"""
        <p {ATTRS_HTML.text_secondary}>
            If the state loses control of capital settlement or the capital is destroyed. If it is destroyed, note whether it was at the hands of internal or external forces.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  In 1115-16 northern tribes attacked the ancient Mexican city of Tula (Tollan), defeated the priest-king, and drove him and his supporters out of the city.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "conquest": f"""
        <p {ATTRS_HTML.text_secondary}>
            The conquest and seizure of the polity’s territory by an external force. This could be a significant part of the territory, a city, the capital, or the entire territory.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: In 1517 the Ottoman forces defeated the Mamluks and seized the sultanate capital of Cairo in Egypt which completed their conquest of the entire Middle East.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "assassination": f"""
        <p {ATTRS_HTML.text_secondary}>
            The murder of the ruler of the polity for ideological or political reasons rather than, for example, if they fall in battle. State the type of assassination if possible, such as execution or poisoning, and who ordered or carried out the assassination if known or speculated.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: When Emperor Ping of the Western Han Empire came of age in 5 BCE and made it clear that he resented the regent Duke Wang Mang&rsquo;s former actions, Mang had the emperor poisoned, and arranged for a distant 1 year old relative to be placed on the throne so that he could control him.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "depose": f"""
        <p {ATTRS_HTML.text_secondary}>
            The ruler of the polity is removed, but not killed. Note: this does not include episodes where the ruler is captured by a foreign polity, but refers to cases where the ruler is removed by ‘internal’ foes.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: During the Eastern Jin Dynasty in 372 CE a powerful general plotted to depose the emperor Fei by spreading damaging rumours of impotency and homosexuality and finally forced Empress Dowager Chu to issue an edict deposing Fei.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "constitution": f"""
        <p {ATTRS_HTML.text_secondary}>
            Major constitutional or institutional change such as how rulers gain power or the role of advisory bodies. This includes both increase or loss of &lsquo;democratic&rsquo; or representative governance, such as the transition from representative oligarchy to dictatorship. It also includes a significant shift in political organization such as the reorganization of provinces, new ideas about kingship, or reforms are included.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The Persian Constitutional Revolution of 1906 led to wide-reaching reforms including the establishment of a parliament and elections, and making the power of the Shah contingent to the will of the people, which saw the beginning of a modern era in Iran.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "religion": f"""
        <p {ATTRS_HTML.text_secondary}>
            The major change or reorganization of religious systems or &lsquo;official cult&rsquo; (the set of collective ritual practices that are most closely associated with legitimation of the power structure). This may be the adoption of a new state religion or state support for a particular religious group.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  After the Islamic Almoravid dynasty occupied and acquired the regions of Kawkaw, Takrur, Ghana, and Bornu, local rulers converted to Islam to ensure administrative support, legitimisation, and commercial contacts. While Islam became an imperial cult and the religion of state, most agricultural groups maintained traditional beliefs.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "unfree_labor": f"""
        <p {ATTRS_HTML.text_secondary}>
            Any change to unfree labor laws. Record only positive changes here such as the abolition of or restcrictions on slavery, or the end of serfdom.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: Alexander II freed all in-service serfs and abolished the practice of serfdom in the Emancipation Reform of 1861 in Russia which granted over 23 million people their freedom and the full rights of citizenship in the Russian Empire.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "suffrage": f"""
        <p {ATTRS_HTML.text_secondary}>
            The new inclusion of a group into the polity’s governance. Record only positive changes here such as the right to vote for previously disenfranchised groups.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  In the Early Roman Republic, 494 BCE, the plebeians went on strike, refusing to march to war against a coalition of tribes from central Italy. A settlement was reached when Rome&rsquo;s aristocrats extended to the plebeians the right to vote for certain magistrates, known as the Tribunes of the Plebs (essentially the &lsquo;people&rsquo;s magistrates&rsquo;).
        </p>""",  # noqa: E501 pylint: disable=C0301
    "public_goods": f"""
        <p {ATTRS_HTML.text_secondary}>
            Any public welfare programs or system changes which use significant state resources for the benefit of the wider population. This does not include military spending. Record only positive changes here such as improvement of infrastructure, public places of learning, or health care facilities.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: After a smallpox epidemic, the Habsburg ruler, Maria Theresa (r.1740-1780) ordered the opening of an inoculation center in Vienna.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "labor": f"""
        <p {ATTRS_HTML.text_secondary}>
            Significant change in labor policies, protections, or laws. Record only positive changes here such as the introduction of minimum wage, child labour laws, or worker’s compensation.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The Cotton Mills and Factories Act 1819 in the UK prevented Cotton Mills from employing children under the age of 9-years-old and restricted the working hours of children aged 9-16 years-old to 12 hours per workday.
        </p>""",  # noqa: E501 pylint: disable=C0301
}


POWER_TRANSITIONS_DEFS_EXAMPLES = {
    "contested": "Was it contested for at least 1 year?",
    "overturn": "NO Definition Yet.",
    "predecessor_assassination": "NO Definition Yet.",
    "intra_elite": "NO Definition Yet.",
    "military_revolt": "NO Definition Yet.",
    "popular_uprising": "NO Definition Yet.",
    "separatist_rebellion": "NO Definition Yet.",
    "external_invasion": "NO Definition Yet.",
    "external_interference": "NO Definition Yet.",
}

HUMAN_SACRIFICE_HUMAN_SACRIFICE_CHOICES = (
    ("U", "Unknown"),
    ("P", "Present"),
    ("A~P", "Transitional (Absent -> Present)"),
    ("A", "Absent"),
    ("P~A", "Transitional (Present -> Absent)"),
)

CRISISDB_CHOICES = (
    ("U", "Unknown"),
    ("SU", "Suspected Unknown"),
    ("P", "Present"),
    ("A", "Absent"),
    ("IP", "Inferred Present"),
    ("IA", "Inferred Absent"),
    ("DIS", "Disputed"),
)

SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES = (
    ("Peculiar Epidemics", "Peculiar Epidemics"),
    ("Pestilence", "Pestilence"),
    ("Miasm", "Miasm"),
    ("Pox", "Pox"),
    ("Uncertain Pestilence", "Uncertain Pestilence"),
    ("Dysentery", "Dysentery"),
    ("Malaria", "Malaria"),
    ("Influenza", "Influenza"),
    ("Cholera", "Cholera"),
    ("Diptheria", "Diptheria"),
    ("Plague", "Plague"),
)

MAGNITUDE_DISEASE_OUTBREAK_CHOICES = (
    ("Uncertain", "Uncertain"),
    ("Light", "Light"),
    ("Heavy", "Heavy"),
    ("No description", "No description"),
    ("Heavy- Multiple Times", "Heavy- Multiple Times"),
    ("No Happening", "No Happening"),
    ("Moderate", "Moderate"),
)

DURATION_DISEASE_OUTBREAK_CHOICES = (
    ("No description", "No description"),
    ("Over 90 Days", "Over 90 Days"),
    ("Uncertain", "Uncertain"),
    ("30-60 Days", "30-60 Days"),
    ("1-10 Days", "1-10 Days"),
    ("60-90 Days", "60-90 Days"),
)

US_STATE_CHOICES = (
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
    ("UNK", "UNKNOWN"),
)


INNER_SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES = [
    x[0] for x in SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES
]
INNER_MAGNITUDE_DISEASE_OUTBREAK_CHOICES = [
    x[0] for x in MAGNITUDE_DISEASE_OUTBREAK_CHOICES
]
INNER_DURATION_DISEASE_OUTBREAK_CHOICES = [
    x[0] for x in DURATION_DISEASE_OUTBREAK_CHOICES
]


TAGS = (
    ("TRS", "Confident"),
    ("SSP", "Suspected"),
    ("IFR", "Inferred"),
)
