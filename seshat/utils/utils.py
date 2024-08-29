import django
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

import requests

from requests.structures import CaseInsensitiveDict

from ..apps.core.models import Polity, Variablehierarchy, Section, Subsection
from ..apps.crisisdb.models import Crisis_consequence, Power_transition, Human_sacrifice


vars_dic_for_utils = {
    "external_conflict": {
        "notes": "This is a new model definition fror External conflicts",
        "main_desc": "Main Descriptions for the Variable external_conflict are missing!",
        "main_desc_source": "",
        "cols": 1,
        "section": "Conflict Variables",
        "subsection": "External Conflicts Subsection",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["CharField", "TextInput"],
            "varname": "conflict_name",
            "var_exp": "The unique name of this external conflict",
            "var_exp_source": None,
        },
    },
    "internal_conflict": {
        "notes": "This is a new model definition fror internal conflicts",
        "main_desc": "Main Descriptions for the Variable internal_conflict are missing!",
        "main_desc_source": "",
        "cols": 4,
        "section": "Conflict Variables",
        "subsection": "Internal Conflicts Subsection",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["CharField", "TextInput"],
            "varname": "conflict",
            "var_exp": "The name of the conflict",
            "var_exp_source": None,
        },
        "col2": {
            "dtype": ["DecimalField", "NumberInput"],
            "varname": "expenditure",
            "var_exp": "The military expenses in millions silver taels.",
            "units": "millions silver taels",
            "min": None,
            "max": None,
            "scale": 1,
            "decimal_places": 15,
            "max_digits": 20,
            "var_exp_source": None,
        },
        "col3": {
            "dtype": ["CharField", "TextInput"],
            "varname": "leader",
            "var_exp": "The leader of the conflict",
            "var_exp_source": None,
        },
        "col4": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "casualty",
            "var_exp": "The number of people who died in this conflict.",
            "units": "People",
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "external_conflict_side": {
        "notes": "This is a new model definition fror External conflict sides",
        "main_desc": "Main Descriptions for the Variable external_conflict_side are missing!",
        "main_desc_source": "",
        "cols": 4,
        "section": "Conflict Variables",
        "subsection": "External Conflicts Subsection",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["CharField", "TextInput"],
            "varname": "conflict",
            "var_exp": "The unique name of the conflict",
            "var_exp_source": None,
        },
        "col2": {
            "dtype": ["DecimalField", "NumberInput"],
            "varname": "expenditure",
            "var_exp": "The military expenses (from this side) in silver taels.",
            "units": "silver taels",
            "min": None,
            "max": None,
            "scale": 1,
            "decimal_places": 15,
            "max_digits": 20,
            "var_exp_source": None,
        },
        "col3": {
            "dtype": ["CharField", "TextInput"],
            "varname": "leader",
            "var_exp": "The leader of this side of conflict",
            "var_exp_source": None,
        },
        "col4": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "casualty",
            "var_exp": "The number of people who died (from this side) in this conflict.",
            "units": "People",
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "agricultural_population": {
        "notes": "Notes for the Variable agricultural_population are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "",
        "cols": 1,
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "agricultural_population",
            "var_exp": "No Explanations.",
            "units": "People",
            "min": 0,
            "max": None,
            "scale": 1000,
            "var_exp_source": None,
        },
    },
    "arable_land": {
        "notes": "Notes for the Variable arable_land are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "",
        "cols": 1,
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "arable_land",
            "var_exp": "No Explanations.",
            "units": "mu?",
            "min": None,
            "max": None,
            "scale": 1000,
            "var_exp_source": None,
        },
    },
    "arable_land_per_farmer": {
        "notes": "Notes for the Variable arable_land_per_farmer are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "",
        "cols": 1,
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "arable_land_per_farmer",
            "var_exp": "No Explanations.",
            "units": "mu?",
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "gross_grain_shared_per_agricultural_population": {
        "notes": "Notes for the Variable gross_grain_shared_per_agricultural_population are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "",
        "cols": 1,
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "gross_grain_shared_per_agricultural_population",
            "var_exp": "No Explanations.",
            "units": "(catties per capita)",
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "net_grain_shared_per_agricultural_population": {
        "notes": "Notes for the Variable net_grain_shared_per_agricultural_population are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "",
        "cols": 1,
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "net_grain_shared_per_agricultural_population",
            "var_exp": "No Explanations.",
            "units": "(catties per capita)",
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "surplus": {
        "notes": "Notes for the Variable surplus are missing!",
        "main_desc": "No Explanations.",
        "main_desc_source": "",
        "cols": 1,
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "surplus",
            "var_exp": "No Explanations.",
            "units": "(catties per capita)",
            "min": None,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "military_expense": {
        "notes": "Not sure about Section and Subsection.",
        "main_desc": "Main Descriptions for the Variable military_expense are missing!",
        "main_desc_source": "https://en.wikipedia.org/wiki/Disease_outbreak",
        "cols": 2,
        "section": "Economy Variables",
        "subsection": "State Finances",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["CharField", "TextInput"],
            "varname": "conflict",
            "var_exp": "The name of the conflict",
            "var_exp_source": None,
        },
        "col2": {
            "dtype": ["DecimalField", "NumberInput"],
            "varname": "expenditure",
            "var_exp": "The military expenses in millions silver taels.",
            "units": "millions silver taels",
            "min": None,
            "max": None,
            "scale": 1,
            "decimal_places": 15,
            "max_digits": 20,
            "var_exp_source": None,
        },
    },
    "silver_inflow": {
        "notes": "Needs suoervision on the units and scale.",
        "main_desc": "Silver inflow in Millions of silver taels??",
        "main_desc_source": "",
        "cols": 1,
        "section": "Economy Variables",
        "subsection": "State Finances",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "silver_inflow",
            "var_exp": "Silver inflow in Millions of silver taels??",
            "units": "Millions of silver taels??",
            "min": None,
            "max": None,
            "scale": 1000000,
            "var_exp_source": None,
        },
    },
    "silver_stock": {
        "notes": "Needs suoervision on the units and scale.",
        "main_desc": "Silver stock in Millions of silver taels??",
        "main_desc_source": "",
        "cols": 1,
        "section": "Economy Variables",
        "subsection": "State Finances",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "silver_stock",
            "var_exp": "Silver stock in Millions of silver taels??",
            "units": "Millions of silver taels??",
            "min": None,
            "max": None,
            "scale": 1000000,
            "var_exp_source": None,
        },
    },
    "total_population": {
        "notes": "Note that the population values are scaled.",
        "main_desc": "Total population or simply population, of a given area is the total number of people in that area at a given time.",
        "main_desc_source": "",
        "cols": 1,
        "section": "Social Complexity Variables",
        "subsection": "Social Scale",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "total_population",
            "var_exp": "The total population of a country (or a polity).",
            "units": "People",
            "min": 0,
            "max": None,
            "scale": 1000,
            "var_exp_source": None,
        },
    },
    "gdp_per_capita": {
        "notes": "The exact year based on which the value of Dollar is taken into account is not clear.",
        "main_desc": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.",
        "main_desc_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848",
        "cols": 1,
        "section": "Economy Variables",
        "subsection": "Productivity",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["DecimalField", "NumberInput"],
            "varname": "gdp_per_capita",
            "var_exp": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.",
            "units": "Dollars (in 2009?)",
            "min": None,
            "max": None,
            "scale": 1,
            "decimal_places": 15,
            "max_digits": 20,
            "var_exp_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848",
        },
    },
    "drought_event": {
        "notes": "Notes for the Variable drought_event are missing!",
        "main_desc": "number of geographic sites indicating drought",
        "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",
        "cols": 1,
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "drought_event",
            "var_exp": "number of geographic sites indicating drought",
            "units": "Numbers",
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "locust_event": {
        "notes": "Notes for the Variable locust_event are missing!",
        "main_desc": "number of geographic sites indicating locusts",
        "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",
        "cols": 1,
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "locust_event",
            "var_exp": "number of geographic sites indicating locusts",
            "units": "Numbers",
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "socioeconomic_turmoil_event": {
        "notes": "Notes for the Variable socioeconomic_turmoil_event are missing!",
        "main_desc": "number of geographic sites indicating socioeconomic turmoil",
        "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",
        "cols": 1,
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "socioeconomic_turmoil_event",
            "var_exp": "number of geographic sites indicating socioeconomic turmoil",
            "units": "Numbers",
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "crop_failure_event": {
        "notes": "Notes for the Variable crop_failure_event are missing!",
        "main_desc": "number of geographic sites indicating crop failure",
        "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",
        "cols": 1,
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "crop_failure_event",
            "var_exp": "number of geographic sites indicating crop failure",
            "units": "Numbers",
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "famine_event": {
        "notes": "Notes for the Variable famine_event are missing!",
        "main_desc": "number of geographic sites indicating famine",
        "main_desc_source": "https://www1.ncdc.noaa.gov/pub/data/paleo/historical/asia/china/reaches2020drought-category-sites.txt",
        "cols": 1,
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["IntegerField", "NumberInput"],
            "varname": "famine_event",
            "var_exp": "number of geographic sites indicating famine",
            "units": "Numbers",
            "min": 0,
            "max": None,
            "scale": 1,
            "var_exp_source": None,
        },
    },
    "disease_outbreak": {
        "notes": "Notes for the Variable disease_outbreak are missing!",
        "main_desc": "A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season.",
        "main_desc_source": "https://en.wikipedia.org/wiki/Disease_outbreak",
        "cols": 6,
        "section": "Well Being",
        "subsection": "Biological Well-Being",
        "null_meaning": "The value is not available.",
        "col1": {
            "dtype": ["DecimalField", "NumberInput"],
            "varname": "longitude",
            "var_exp": "The longitude (in degrees) of the place where the disease was spread.",
            "units": "Degrees",
            "min": -180,
            "max": 180,
            "scale": 1,
            "decimal_places": 15,
            "max_digits": 20,
            "var_exp_source": None,
        },
        "col2": {
            "dtype": ["DecimalField", "NumberInput"],
            "varname": "latitude",
            "var_exp": "The latitude (in degrees) of the place where the disease was spread.",
            "units": "Degrees",
            "min": -180,
            "max": 180,
            "scale": 1,
            "decimal_places": 15,
            "max_digits": 20,
            "var_exp_source": None,
        },
        "col3": {
            "dtype": ["DecimalField", "NumberInput"],
            "varname": "elevation",
            "var_exp": "Elevation from mean sea level (in meters) of the place where the disease was spread.",
            "units": "Meters",
            "min": 0,
            "max": 5000,
            "scale": 1,
            "decimal_places": 15,
            "max_digits": 20,
            "var_exp_source": None,
        },
        "col4": {
            "dtype": ["CharField", "Select"],
            "varname": "sub_category",
            "var_exp": "The category of the disease.",
            "var_exp_source": None,
            "choices": [
                "Peculiar Epidemics",
                "Pestilence",
                "Miasm",
                "Pox",
                "Uncertain Pestilence",
                "Dysentery",
                "Malaria",
                "Influenza",
                "Cholera",
                "Diptheria",
                "Plague",
            ],
        },
        "col5": {
            "dtype": ["CharField", "Select"],
            "varname": "magnitude",
            "var_exp": "How heavy the disease was.",
            "var_exp_source": None,
            "choices": [
                "Uncertain",
                "Light",
                "Heavy",
                "No description",
                "Heavy- Multiple Times",
                "No Happening",
                "Moderate",
            ],
        },
        "col6": {
            "dtype": ["CharField", "Select"],
            "varname": "duration",
            "var_exp": "How long the disease lasted.",
            "var_exp_source": None,
            "choices": [
                "No description",
                "Over 90 Days",
                "Uncertain",
                "30-60 Days",
                "1-10 Days",
                "60-90 Days",
            ],
        },
    },
}
"""
vars_dic_for_utils is a dictionary that contains the definitions of all the variables in the database. It is used to generate the models and views for the variables. It is a dictionary of dictionaries, where the key is the name of the variable and the value is a dictionary that contains the following keys:
- notes: A description of the variable.
- main_desc: The main description of the variable.
- main_desc_source: The source of the main description.
- cols: The number of columns in the variable.
- section: The section of the variable.
- subsection: The subsection of the variable.
- null_meaning: The meaning of a null value in the variable.
- col1: A dictionary that contains the definition of the first column of the variable. It contains the following keys:
    - dtype: The data type of the column.
    - varname: The name of the column.
    - var_exp: The explanation of the column.
    - var_exp_source: The source of the explanation.
    - units: The units of the column.
    - min: The minimum value of the column.
    - max: The maximum value of the column.
    - scale: The scale of the column.
    - decimal_places: The number of decimal places in the column.
    - max_digits: The maximum number of digits in the column.
- col2: A dictionary that contains the definition of the second column of the variable. It contains the same keys as col1.
- col3: A dictionary that contains the definition of the third column of the variable. It contains the same keys as col1.
- col4: A dictionary that contains the definition of the fourth column of the variable. It contains the same keys as col1.
- col5: A dictionary that contains the definition of the fifth column of the variable. It contains the same keys as col1.
- col6: A dictionary that contains the definition of the sixth column of the variable. It contains the same keys as col1.
"""


def list_of_all_Polities():
    """
    Returns a list of all polities in the database.

    Returns:
        list: A list of all polity names.
    """
    all_pols = Polity.objects.all()
    pol_names = []
    for pol in all_pols:
        pol_names.append(pol.name)

    return pol_names


def dic_of_all_vars():
    """
    Returns a dictionary of all variables in the database.

    Returns:
        dict: A dictionary of all variables.
    """
    myvars = django.apps.apps.get_models()
    my_vars = {}
    return my_vars


def dic_of_all_vars_with_varhier():
    """
    Returns a dictionary of all variables in the database. This dictionary is
    structured in a way that it can be used to generate a hierarchical
    representation of the variables.

    Returns:
        dict: A dictionary of all variables.
    """
    my_secs = {
        "Economy Variables": {
            "Productivity": [
                "agricultural_population",
                "arable_land",
                "arable_land_per_farmer",
                "gross_grain_shared_per_agricultural_population",
                "net_grain_shared_per_agricultural_population",
                "surplus",
                "gdp_per_capita",
            ],
            "State Finances": ["military_expense", "silver_inflow", "silver_stock"],
        },
        "Social Complexity Variables": {"Social Scale": ["total_population"]},
        "Well Being": {
            "Biological Well-Being": [
                "drought_event",
                "locust_event",
                "socioeconomic_turmoil_event",
                "crop_failure_event",
                "famine_event",
                "disease_outbreak",
            ]
        },
    }

    return my_secs


def dic_of_all_vars_in_sections():
    """
    Returns a dictionary of all variables in the database. This dictionary is
    structured in a way that it can be used to generate a hierarchical
    representation of the variables.

    Note:
        This function does not seem to be used in the current version of the
        application.

    Returns:
        dict: A dictionary of all variables.
    """
    my_vars = {
        "finances": {
            "total_tax": "Total Tax",
            "salt_tax": "Salt Tax",
            "total_revenue": "Total Revenue",
        },
        "goodies": {"bad_boy": "chips", "worse_boy": "cookie eater"},
    }
    return my_vars


def adder(a, b):
    """
    Adds two numbers together.

    Args:
        a (int): The first number to be added.
        b (int): The second number to be added.

    Returns:
        int: The sum of the two numbers.
    """
    print(a + b)


def section_dic_extractor():
    """
    Extracts a dictionary of all sections in the database.

    Returns:
        dict: A dictionary of all sections.
    """
    my_list = Section.objects.all()
    dic_to_be_returned = {}
    for item in list(my_list):
        dic_to_be_returned[item.name] = item.id

    print(dic_to_be_returned)
    return dic_to_be_returned


def subsection_dic_extractor():
    """
    Extracts a dictionary of all subsections in the database.

    Returns:
        dict: A dictionary of all subsections.
    """
    my_list = Subsection.objects.all()
    dic_to_be_returned = {}
    for item in list(my_list):
        dic_to_be_returned[item.name] = item.id

    print(dic_to_be_returned)
    return dic_to_be_returned


def test_for_varhier_dic():
    """
    Extracts a dictionary of all variables in the database. This dictionary is
    structured in a way that it can be used to generate a hierarchical
    representation of the variables.

    Returns:
        dict: A dictionary of all variables.
    """
    all_sections = Section.objects.all()
    all_subsections = Subsection.objects.all()
    all_varhiers = Variablehierarchy.objects.all()

    my_dict, context = {}, {}
    for sect in all_sections:
        my_dict[sect.name] = {}
        for subsect in all_subsections:
            list_of_all_varhiers_in_here = []
            for item in all_varhiers:
                if (
                    item.section.name == sect.name
                    and item.subsection.name == subsect.name
                ):
                    print("We hit it")
                    list_of_all_varhiers_in_here.append(item.name.lower())
            if list_of_all_varhiers_in_here:
                my_dict[sect.name][subsect.name] = list_of_all_varhiers_in_here

    context["my_dict"] = my_dict

    return my_dict


# For now, what I am doing to feed the Qing vars page with the needed links is to call this
# function from the shell, and feed it with the vars_dic on top of this page (which has to
# be a copy of the original vars_dic that we are using in generating models and views and
# all). I then copy and paste the output to the QingVars function in Views. Sounds weird.
def qing_vars_links_creator(vars_dic_for_here):
    """
    Creates a dictionary of all variables in the database. This dictionary is
    structured in a way that it can be used to generate a hierarchical
    representation of the variables.

    Args:
        vars_dic_for_here (dict): A dictionary of all variables.

    Returns:
        dict: A dictionary of all variables.
    """
    varhier_dic = {"Other_Sections": {"Other_Subsections": []}}

    for k, v in vars_dic_for_here.items():
        if v["section"] and v["section"] not in varhier_dic.keys():
            varhier_dic[v["section"]] = {}

    for k, v in vars_dic_for_here.items():
        if v["subsection"] and v["subsection"] not in varhier_dic[v["section"]].keys():
            varhier_dic[v["section"]][v["subsection"]] = []

    for k, v in vars_dic_for_here.items():
        if k not in varhier_dic[v["section"]][v["subsection"]]:
            my_list = [
                k.replace("_", " ").capitalize(),
                k + "s",
                k + "-create",
                k + "-download",
                k + "-metadownload",
            ]
            varhier_dic[v["section"]][v["subsection"]].append(my_list)

    return varhier_dic


def get_all_data_for_a_polity(polity_id, db_name):
    """
    Gets all data for a given polity ID.

    Args:
        polity_id (int): The ID of the polity.
        db_name (str): The name of the database.

    Returns:
        dict: A dictionary of all data for the polity.
    """
    all_vars, a_huge_context_data_dic = [], {}

    for ct in ContentType.objects.all():
        m = ct.model_class()

        if (
            m
            and m.__module__ == f"seshat.apps.{db_name}.models"
            and (
                m.__name__ == "Arable_land"
                or m.__name__ == "Agricultural_population"
                or m.__name__ == "Human_sacrifice"
            )
        ):
            all_vars.append(m.__name__)

            my_data = m.objects.filter(polity=polity_id)

            a_huge_context_data_dic[str(m.__name__)] = my_data

    return a_huge_context_data_dic


def get_all_general_data_for_a_polity_old(polity_id):
    """
    Gets all general data for a given polity ID.

    :private:

    Note:
        This function is not used in the current version of the application.

    Args:
        polity_id (int): The ID of the polity.

    Returns:
        dict: A dictionary of all general data for the polity.
    """
    a_huge_context_data_dic = {}

    for ct in ContentType.objects.all():
        m = ct.model_class()

        if m and m.__module__ == "seshat.apps.general.models":
            my_data = m.objects.filter(polity=polity_id)

            if my_data:
                a_huge_context_data_dic[m.__name__] = my_data

    return a_huge_context_data_dic


def get_all_general_data_for_a_polity(polity_id):
    """
    Gets all data for a given polity ID from the "general" app.

    Args:
        polity_id (int): The ID of the polity.

    Returns:
        tuple: A tuple containing a dictionary of all data for the polity and a boolean value indicating whether the polity has any data.
    """
    app_name = "general"  # Replace with your app name
    models_1 = django.apps.apps.get_app_config(app_name).get_models()
    has_any_data = False

    all_vars_grouped_g = {}
    for model in models_1:
        model_name = model.__name__

        if model_name in [
            "Ra",
            "Polity_editor",
            "Polity_research_assistant",
            "Polity_expert",
            "XYZ",
        ]:
            continue

        s_value = str(model().subsection())
        ss_value = str(model().sub_subsection())

        if s_value not in all_vars_grouped_g:
            all_vars_grouped_g[s_value] = {}

            if ss_value:
                all_vars_grouped_g[s_value][ss_value] = {}
            else:
                all_vars_grouped_g[s_value]["None"] = {}
        else:
            if ss_value:
                all_vars_grouped_g[s_value][ss_value] = {}
            else:
                all_vars_grouped_g[s_value]["None"] = {}

    for ct in ContentType.objects.all():
        m = ct.model_class()

        if m and m.__module__ == "seshat.apps.general.models":
            if hasattr(m, "other_polity"):
                my_data = m.objects.filter(
                    Q(polity=polity_id) | Q(other_polity=polity_id)
                )
            else:
                my_data = m.objects.filter(polity=polity_id)

            if m.__name__ in [
                "Ra",
                "Polity_editor",
                "Polity_research_assistant",
                "Polity_expert",
            ]:
                continue

            if my_data:
                has_any_data = True

                my_s = m().subsection()

                if my_s:
                    all_vars_grouped_g[my_s]["None"][m.__name__] = my_data
                else:
                    print(f"-------------{my_s},")
            else:
                my_s = m().subsection()

                if my_s:
                    all_vars_grouped_g[my_s]["None"][m.__name__] = None
                else:
                    print(f"--------xxx-----{my_s},")

    return all_vars_grouped_g, has_any_data


def get_all_sc_data_for_a_polity(polity_id):
    """
    Gets all data for a given polity ID from the "sc" app.

    Args:
        polity_id (int): The ID of the polity.

    Returns:
        tuple: A tuple containing a dictionary of all data for the polity and a boolean value indicating whether the polity has any data.
    """
    app_name = "sc"  # Replace with your app name
    models_1 = apps.get_app_config(app_name).get_models()
    has_any_data = False

    all_vars_grouped = {}
    for model in models_1:
        if model.__name__ == "Ra":
            continue

        s_value = str(model().subsection())
        ss_value = str(model().sub_subsection())

        if s_value not in all_vars_grouped:
            all_vars_grouped[s_value] = {}

            if ss_value:
                all_vars_grouped[s_value][ss_value] = {}
            else:
                all_vars_grouped[s_value]["None"] = {}
        else:
            if ss_value:
                all_vars_grouped[s_value][ss_value] = {}
            else:
                all_vars_grouped[s_value]["None"] = {}

    for ct in ContentType.objects.all():
        m = ct.model_class()

        if m and m.__module__ == "seshat.apps.sc.models":
            my_data = m.objects.filter(polity=polity_id)

            if m.__name__ == "Ra":
                continue

            if my_data:
                has_any_data = True
                my_s = m().subsection()
                my_ss = m().sub_subsection()

                if my_s and my_ss:
                    all_vars_grouped[my_s][my_ss][m.__name__] = my_data
                elif my_s:
                    all_vars_grouped[my_s]["None"][m.__name__] = my_data
                else:
                    print(f"-------------{my_s}, {my_ss}")

            else:
                my_s = m().subsection()
                my_ss = m().sub_subsection()

                if my_s and my_ss:
                    all_vars_grouped[my_s][my_ss][m.__name__] = my_data
                elif my_s:
                    all_vars_grouped[my_s]["None"][m.__name__] = my_data
                else:
                    print(f"--------xxx-----{my_s},")

    return all_vars_grouped, has_any_data


def get_all_wf_data_for_a_polity(polity_id):
    """
    Gets all data for a given polity ID from the "wf" app.

    Args:
        polity_id (int): The ID of the polity.

    Returns:
        tuple: A tuple containing a dictionary of all data for the polity and a boolean value indicating whether the polity has any data.
    """
    app_name = "wf"  # Replace with your app name
    models_1 = apps.get_app_config(app_name).get_models()

    has_any_data = False

    all_vars_grouped_wf = {}
    for model in models_1:
        model_name = model.__name__

        s_value = str(model().subsection())
        ss_value = str(model().sub_subsection())

        if s_value not in all_vars_grouped_wf:
            all_vars_grouped_wf[s_value] = {}
            if ss_value:
                all_vars_grouped_wf[s_value][ss_value] = {}
            else:
                all_vars_grouped_wf[s_value]["None"] = {}
        else:
            if ss_value:
                all_vars_grouped_wf[s_value][ss_value] = {}
            else:
                all_vars_grouped_wf[s_value]["None"] = {}

    for ct in ContentType.objects.all():
        m = ct.model_class()
        if m and m.__module__ == "seshat.apps.wf.models":
            my_data = m.objects.filter(polity=polity_id)

            if my_data:
                has_any_data = True
                my_s = m().subsection()

                if my_s:
                    all_vars_grouped_wf[my_s]["None"][m.__name__] = my_data
                else:
                    print(f"-------------{my_s},")
            else:
                my_s = m().subsection()

                if my_s:
                    all_vars_grouped_wf[my_s]["None"][m.__name__] = None
                else:
                    print(f"--------xxx-----{my_s},")

    return all_vars_grouped_wf, has_any_data


def get_all_rt_data_for_a_polity(polity_id):
    """
    Gets all data for a given polity ID from the "rt" app.

    Args:
        polity_id (int): The ID of the polity.

    Returns:
        tuple: A tuple containing a dictionary of all data for the polity and a boolean value indicating whether the polity has any data.
    """
    app_name = "rt"  # Replace with your app name
    models_1 = apps.get_app_config(app_name).get_models()

    has_any_data = False
    all_vars_grouped_rt = {}

    for model in models_1:
        model_name = model.__name__
        if model_name in [
            "A_religion",
        ]:
            continue

        s_value = str(model().subsection())

        if s_value not in all_vars_grouped_rt:
            all_vars_grouped_rt[s_value] = {}
            all_vars_grouped_rt[s_value]["None"] = {}
        else:
            all_vars_grouped_rt[s_value]["None"] = {}

    for ct in ContentType.objects.filter(app_label="rt"):
        mm = ct.model_class()
        if mm and mm.__module__ == "seshat.apps.rt.models":
            my_data = mm.objects.filter(polity=polity_id)
            if mm.__name__ in [
                "A_religion",
            ]:
                print("Skipping Religion model")
                continue

            if my_data:
                has_any_data = True
                my_s = mm().subsection()

                if my_s:
                    all_vars_grouped_rt[my_s]["None"][mm.__name__] = my_data
                else:
                    print(f"Invalid subsection for model: {mm.__name__}")
            else:
                my_s = mm().subsection()

                if my_s:
                    all_vars_grouped_rt[my_s]["None"][mm.__name__] = None
                else:
                    print(f"--------xxx-----{my_s},")

    return all_vars_grouped_rt, has_any_data


def get_all_wf_data_for_a_polity_old(polity_id):
    """
    Gets all data for a given polity ID from the "wf" app.

    :private:

    Note:
        This function is not used in the current version of the application.

    Args:
        polity_id (int): The ID of the polity.

    Returns:
        dict: A dictionary of all data for the polity.
    """
    a_huge_context_data_dic = {}
    for ct in ContentType.objects.all():
        m = ct.model_class()
        if m and m.__module__ == "seshat.apps.wf.models":
            my_data = m.objects.filter(polity=polity_id)
            if my_data:
                a_huge_context_data_dic[m.__name__] = my_data
    return a_huge_context_data_dic


def get_all_crisis_cases_data_for_a_polity(polity_id):
    """
    Gets all data for a given polity ID from the "crisisdb" app.

    Args:
        polity_id (int): The ID of the polity.

    Returns:
        dict: A dictionary of all data for the polity.
    """
    my_data = Crisis_consequence.objects.filter(
        Q(polity=polity_id) | Q(other_polity=polity_id)
    )

    a_data_dic = {}
    if my_data:
        a_data_dic["crisis_consequence"] = my_data

    return a_data_dic


def get_all_power_transitions_data_for_a_polity(polity_id):
    """
    Gets all data for a given polity ID from the "rt" app.

    Args:
        polity_id (int): The ID of the polity.

    Returns:
        dict: A dictionary of all data for the polity.
    """
    a_data_dic = {}
    my_data = Power_transition.objects.filter(polity=polity_id)
    if my_data:
        a_data_dic["power_transition"] = my_data

    return a_data_dic


def give_polity_app_data():
    contain_dic = {}
    freq_dic = {
        "g": 0,
        "sc": 0,
        "wf": 0,
        "rt": 0,
        "hs": 0,
        "cc": 0,
        "pt": 0,
    }
    unique_polity_ids_general = set()
    unique_polity_ids_sc = set()
    unique_polity_ids_wf = set()
    unique_polity_ids_rt = set()

    app_models_general = apps.get_app_config("general").get_models()
    app_models_sc = apps.get_app_config("sc").get_models()
    app_models_wf = apps.get_app_config("wf").get_models()
    app_models_rt = apps.get_app_config("rt").get_models()

    for model in app_models_general:
        if hasattr(model, "polity_id"):
            polity_ids_general = model.objects.values_list(
                "polity_id", flat=True
            ).distinct()
            unique_polity_ids_general.update(polity_ids_general)

    for model in app_models_sc:
        if hasattr(model, "polity_id"):
            polity_ids_sc = model.objects.values_list("polity_id", flat=True).distinct()
            unique_polity_ids_sc.update(polity_ids_sc)

    for model in app_models_wf:
        if hasattr(model, "polity_id"):
            polity_ids_wf = model.objects.values_list("polity_id", flat=True).distinct()
            unique_polity_ids_wf.update(polity_ids_wf)

    for model in app_models_rt:
        if hasattr(model, "polity_id"):
            polity_ids_rt = model.objects.values_list("polity_id", flat=True).distinct()
            unique_polity_ids_rt.update(polity_ids_rt)

    all_polity_ids = Polity.objects.values_list("id", flat=True)
    for polity_id in all_polity_ids:
        has_hs = Human_sacrifice.objects.filter(polity=polity_id).exists()

        if has_hs:
            freq_dic["hs"] += 1

        has_cc = Crisis_consequence.objects.filter(
            Q(polity=polity_id) | Q(other_polity=polity_id)
        ).exists()

        if has_cc:
            freq_dic["cc"] += 1
        has_pt = Power_transition.objects.filter(polity=polity_id).exists()

        if has_pt:
            freq_dic["pt"] += 1

        contain_dic[polity_id] = {
            "g": False,
            "sc": False,
            "wf": False,
            "rt": False,
            "hs": has_hs,
            "cc": has_cc,
            "pt": has_pt,
        }

        if polity_id in unique_polity_ids_general:
            contain_dic[polity_id]["g"] = True
            freq_dic["g"] += 1

        if polity_id in unique_polity_ids_sc:
            contain_dic[polity_id]["sc"] = True
            freq_dic["sc"] += 1

        if polity_id in unique_polity_ids_wf:
            contain_dic[polity_id]["wf"] = True
            freq_dic["wf"] += 1

        if polity_id in unique_polity_ids_rt:
            contain_dic[polity_id]["rt"] = True
            freq_dic["rt"] += 1

    return contain_dic, freq_dic


def polity_detail_data_collector(polity_id):
    url = "http://127.0.0.1:8000/api/politys-api/"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    all_my_data = resp.json()["results"]

    # Go through the data and create the proper data to give the function
    for polity_with_everything in all_my_data:
        if polity_with_everything["id"] == polity_id:
            final_response = dict(polity_with_everything)
            break
        else:
            final_response = {}

    return final_response
