__all__ = [
    "APP_NAME",
    "SOURCE_OF_SUPPORT_CHOICES",
    "SC_VAR_DEFS",
]

APP_NAME = "sc"

SOURCE_OF_SUPPORT_CHOICES = (
    ("state salary", "state salary"),
    ("pensions", "pensions"),
    ("enoblement", "enoblement"),
    ("suspected unknown", "suspected unknown"),
    ("unknown", "unknown"),
    ("land", "land"),
    ("absent", "absent"),
    ("cash", "cash"),
    ("salary", "salary"),
    ("state", "state"),
    ("governed population", "governed population"),
    ("none", "none"),
    ("cattle", "cattle"),
)

SC_VAR_DEFS = {
    "communal_building": "This code distinguishes between settlements that consist of only private households (code 'absent') and settlements where there are communal buildings which could be used for a variety of uses (code 'present').",  # noqa: E501 pylint: disable=C0301
    "utilitarian_public_building": "Typical examples include aqueducts, sewers, and granaries. In the narrative paragraph list all utilitarian buildings and give examples of the most impressive/costly/large ones.",  # noqa: E501 pylint: disable=C0301
    "symbolic_building": "Non-utilitarian constructions that display symbols, or are themselves symbols of the community or polity (or a ruler as a symbol of the polity). Examples include Taj Mahal mausoleum, Trajan's Column, Ashoka's Pillars, Qin Shih Huang's Terracota Army, the Statue of Liberty. Has to be constructed by humans, so sacred groves or mountains are not symbolic buildings. A palace is also not a symbolic building, because it has other, utilitarian functions (houses the ruler).",  # noqa: E501 pylint: disable=C0301
    "entertainment_building": "These include theaters, arenas, race tracks.",
    "knowledge_or_information_building": "These include astronomic observatories, libraries, and museums.",  # noqa: E501 pylint: disable=C0301
    "special_purpose_site": "Sites not associated with residential areas. This position is primarily useful for coding archaneologically known societies.",  # noqa: E501 pylint: disable=C0301
    "ceremonial_site": "No Description",
    "burial_site": "Dissociated from settlement, has monumental features.",
    "trading_emporia": "Trading settlements characterised by their peripheral locations, on the shore at the edge of a polity, a lack of infrastructure (typically those in Europe contained no churches) and often of a short-lived nature. They include isolated caravanserai along trade routes.",  # noqa: E501 pylint: disable=C0301
    "enclosure": "An 'enclosure' is clearly demarcated special-purpose area. It can be separated from surrounding land by earthworks (including banks or ditches), walls, or fencing. It may be as small as a few meters across, or encompass many hectares. It is non-residential, but could serve numerous purposes, both practical (animal pens) as well as religious and ceremonial",  # noqa: E501 pylint: disable=C0301
    "length_measurement_system": "Textual evidence of length measurement systems. Measurement units are named in sources.",  # noqa: E501 pylint: disable=C0301
    "area_measurement_system": "Textual evidence of area measurement systems. Measurement units are named in sources.",  # noqa: E501 pylint: disable=C0301
    "volume_measurement_system": 'Textual evidence of volume measurement systems. Measurement units are named in sources. Archaeological evidence includes finding containers of standard volume, etc. (use "inferred present" in such cases)',  # noqa: E501 pylint: disable=C0301
    "weight_measurement_system": "Textual evidence of weight measurement systems. Measurement units are named in sources.",  # noqa: E501 pylint: disable=C0301
    "time_measurement_system": "Textual evidence of time measurement systems. Measurement units are named in sources. A natural unit such as 'day' doesn't qualify. Nor does a vague one like 'season'. Archaeological evidence is a clock (e.g., sundial)",  # noqa: E501 pylint: disable=C0301
    "geometrical_measurement_system": "Textual evidence of geometrical measurement systems. Measurement units are named in sources.  For example: degree.",  # noqa: E501 pylint: disable=C0301
    "other_measurement_system": "Textual evidence of more advanced measurement systems: temperature, force, astronomical",  # noqa: E501 pylint: disable=C0301
    "debt_and_credit_structure": "Commercial/market practices that take physical form, e.g. a contract on parchment (not just verbal agreements).",  # noqa: E501 pylint: disable=C0301
    "store_of_wealth": "Example: hoard, chest for storing valuables, treasury room. Note for the future: perhaps should separate these into individual variables.",  # noqa: E501 pylint: disable=C0301
    "source_of_support": "possible codes: state salary, governed population, land, none. 'State salary' can be paid either in currency or in kind (e.g., koku of rice). 'Governed population' means that the official directly collects tribute from the population (for example, the 'kormlenie' system in Medieval Russia). 'Land' is when the bureaucrats live off land supplied by the state. 'None' is when the state officials are not compensated (example: in the Republican and Principate Rome the magistrates were wealthy individuals who served without salary, motivated by prestige and social or career advancement).",  # noqa: E501 pylint: disable=C0301
    "other_special_purpose_site": "Other special-purpose sites.",
    "special_purpose_house": "A normal house used in a distinctive or special manner. This code reflects differentiation between houses.",  # noqa: E501 pylint: disable=C0301
    "occupational_complexity": "No Descriptions in the code book.",
    "military_level": """levels. Again, start with the commander-in-chief = level 1 and work down to the private.
Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier).""",  # noqa: E501 pylint: disable=C0301
    "fastest_individual_communication": "This is the fastest time (in days) an individual can travel from the capital city to the most outlying provincial capital (if one exists), usually keeping within the boundaries of the polity. This might be by ship, horse, horse relay, or on foot, or a combination.",  # noqa: E501 pylint: disable=C0301
    "largest_communication_distance": """Distance in kilometers between the capital and the furthest provincial capital. Use the figure for the most direct land and/or sea route that was available.
As an alternative for prehistoric communities, measure the distance between largest quasi-capital and furthest village within the quasi-polity.""",  # noqa: E501 pylint: disable=C0301
    "other_utilitarian_public_building": "Other utilitarian public buildings...",
}
