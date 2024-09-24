__all__ = [
    "get_data_for_polity",
    "get_model_data",
    "get_polity_app_data",
]

import json
import numpy as np
import random
import sys

from django.db.models import Q, Min, Max
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.contrib.gis.geos import GEOSGeometry
from django.core.cache import cache

from ..utils import get_models
from ..constants import (
    ABSENT_PRESENT_CHOICES,
)
from ..patterns import PATTERNS
from ..crisisdb.models import (
    Crisis_consequence,
    Power_transition,
    Human_sacrifice,
)
from ..general.models import (
    Polity_capital,
    Polity_language_genus,
    Polity_language,
    Polity_linguistic_family,
)
from ..core.models import (
    Polity,
    Capital
)
from .models import (
    Citation,
    Reference,
    GADMCountries,
    GADMProvinces,
    VideoShapefile,
)
from .constants import APP_MAP, CATEGORICAL_VARIABLES, WORLD_MAP_INITIAL_POLITY


def get_data_for_polity(polity_id, app_name, models=None):
    """
    Get all data for a given polity ID from a given app.

    Args:
        polity_id (int): The ID of the polity.
        app_name (str): The name of the app.
        models (list): A list of models to get data from.

    Returns:
        dict: A dictionary of all data for the polity.
    """
    if not models:
        models = [
            x.__name__.lower()
            for x in get_models(app_name)
            if getattr(x, "polity", None)
        ]
    else:
        models = [x.lower() for x in models]

    app_content_types = ContentType.objects.filter(
        app_label=app_name, model__in=models
    )

    all_models = [model.model_class() for model in app_content_types]

    return {
        model.__name__: model.objects.filter(polity=polity_id)
        for model in all_models
    }


def get_model_data(model, polity_id, filter_for_other_polity=False):
    """
    Get data for a given model and polity ID.

    Args:
        model (str): The name of the model.
        polity_id (int): The ID of the polity.
        filter_for_other_polity (bool): Whether to filter for the other polity

    Returns:
        dict: A dictionary of all data for the polity.
    """

    if filter_for_other_polity:
        _filter = Q(polity__pk=polity_id) | Q(other_polity__pk=polity_id)
    else:
        _filter = Q(polity__pk=polity_id)

    key = model.__name__.lower()
    dic = {
        key: model.objects.filter(_filter)
    }

    if not dic[key]:
        return {}

    return dic


def get_polity_app_data(
    polity_model, return_all=False, return_freq=True, return_contain=True
):
    """
    Gets all data for a given polity model.

    Args:
        polity_model (Model): The polity model.

    Returns:
        tuple: A tuple containing a dictionary of all data for the polity and a boolean
            value indicating whether the polity has any data
    """
    freq_dic, contain_dic = {}, {}

    apps = ["general", "sc", "wf", "rt"]

    polity_ids = polity_model.objects.all().values_list("id", flat=True)

    polity_id_per_app = {
        app: list(
            set(
                id
                for model in get_models(app)
                for id in model.objects.values_list(
                    "polity_id", flat=True
                ).distinct()
            )
        )
        for app in apps
    }

    if return_freq or return_all:
        freq_dic = {
            label: 0 for label in ["g", "sc", "wf", "rt", "hs", "cc", "pt"]
        }
        freq_dic["hs"] = sum(
            [
                Human_sacrifice.objects.filter(polity=polity_id).exists()
                for polity_id in polity_ids
            ]
        )
        freq_dic["cc"] = sum(
            [
                Crisis_consequence.objects.filter(polity=polity_id).exists()
                for polity_id in polity_ids
            ]
        )
        freq_dic["pt"] = sum(
            [
                Power_transition.objects.filter(polity=polity_id).exists()
                for polity_id in polity_ids
            ]
        )
        freq_dic["g"] = len(polity_id_per_app["general"])
        freq_dic["sc"] = len(polity_id_per_app["sc"])
        freq_dic["wf"] = len(polity_id_per_app["wf"])
        freq_dic["rt"] = len(polity_id_per_app["rt"])

    if return_contain or return_all:
        contain_dic = {
            polity_id: {
                "g": False,
                "sc": False,
                "wf": False,
                "rt": False,
                "hs": False,
                "cc": False,
                "pt": False,
            }
            for polity_id in polity_ids
        }

        # Iterate through each app and mark True in contain_dic where applicable
        for app, key in [
            ("general", "g"),
            ("sc", "sc"),
            ("wf", "wf"),
            ("rt", "rt"),
        ]:
            for polity_id in polity_id_per_app[app]:
                if (
                    polity_id in contain_dic
                ):  # To ensure only relevant polity_ids are marked
                    contain_dic[polity_id][key] = True

    if return_all or (return_contain and return_freq):
        return contain_dic, freq_dic

    if return_contain:
        return contain_dic

    if return_freq:
        return freq_dic


def do_zotero(results, reference_model):
    """
    Process the results from the Zotero API.

    Args:
        results: The results from the Zotero API.

    Returns:
        list: A list of dictionaries containing the processed data.
    """
    references_parent_lst = []
    for _, item in enumerate(results):
        a_key = item["data"]["key"]
        if a_key == "3BQQ8WN8":
            # Skipped because it is not in database
            continue
        if a_key == "RR6R3383":
            # Skipped because title is too big
            continue

        try:
            # We need to make sure that all the changes in Zotero will be reflected here.
            continue
        except:  # noqa: E722  TODO: Don't use bare except
            dic = {}
            try:
                if item["data"]["key"]:
                    tuple_key = item["data"]["key"]
                    dic["key"] = tuple_key
                else:
                    # Key is empty for index: {i}: {item['data']['itemType']}
                    pass
            except:  # noqa: E722  TODO: Don't use bare except
                # No key for item with index: {i}
                pass

            try:
                if item["data"]["itemType"]:
                    tuple_item = item["data"]["itemType"]
                    dic["itemType"] = tuple_item
                else:
                    # itemType is empty for index: {i}: {item['data']['itemType']}
                    pass
            except:  # noqa: E722  TODO: Don't use bare except
                # No itemType for item with index: {i}
                pass

            try:
                num_of_creators = len(item["data"]["creators"])
                if num_of_creators < 4 and num_of_creators > 0:
                    all_creators_list = []
                    for j in range(num_of_creators):
                        if a_key == "MM6AEU7H":
                            # Skipped because it has contributors and not authors
                            continue
                        try:
                            try:
                                good_name = item["data"]["creators"][j][
                                    "lastName"
                                ]
                            except:  # noqa: E722  TODO: Don't use bare except
                                good_name = item["data"]["creators"][j]["name"]
                        except:  # noqa: E722  TODO: Don't use bare except
                            good_name = ("NO_NAMES",)
                        all_creators_list.append(good_name)

                    good_name_with_space = "_".join(all_creators_list)
                    good_name_with_underscore = good_name_with_space.replace(
                        " ", "_"
                    )

                    dic["mainCreator"] = good_name_with_underscore
                elif num_of_creators > 3:
                    try:
                        try:
                            good_name = item["data"]["creators"][0]["lastName"]
                        except KeyError:
                            good_name = item["data"]["creators"][0]["name"]
                    except KeyError:
                        good_name = ("NO_NAME",)

                    good_name_with_space = good_name + "_et_al"
                    good_name_with_underscore = good_name_with_space.replace(
                        " ", "_"
                    )

                    dic["mainCreator"] = good_name_with_underscore
                else:
                    dic["mainCreator"] = "NO_CREATOR"
            except:  # noqa: E722  TODO: Don't use bare except
                # No mainCreator for item with index: {i}: {item['data']['itemType']}
                dic["mainCreator"] = "NO_CREATORS"

            try:
                if item["data"]["date"]:
                    full_date = item["data"]["date"]
                    year = PATTERNS.YEAR.search(full_date)
                    year_int = int(year[0])
                    dic["year"] = year_int
                else:
                    # Year is empty for index {i}: {item['data']['itemType']}
                    dic["year"] = 0
            except:  # noqa: E722  TODO: Don't use bare except
                # No year for index {i}: {item['data']['itemType']}
                dic["year"] = -1

            try:
                try:
                    if item["data"]["bookTitle"]:
                        if a_key == "MM6AEU7H":
                            pass
                        if item["data"]["itemType"] == "bookSection":
                            good_title = (
                                item["data"]["title"]
                                + " (IN) "
                                + item["data"]["bookTitle"]
                            )
                            pass
                        else:
                            good_title = item["data"]["title"]

                        dic["title"] = good_title
                    else:
                        good_title = item["data"]["title"]
                        dic["title"] = good_title

                        if a_key == "MM6AEU7H":
                            pass
                except:  # noqa: E722  TODO: Don't use bare except
                    dic["title"] = item["data"]["title"]
            except:  # noqa: E722  TODO: Don't use bare except
                # No title for item with index: {i}
                pass

            pot_title = dic.get("title")
            if not pot_title:
                pot_title = "NO_TITLE_PROVIDED_IN_ZOTERO"

            newref = reference_model(
                title=pot_title,
                year=dic.get("year"),
                creator=dic.get("mainCreator"),
                zotero_link=dic.get("key"),
            )

            if dic.get("year") < 2040:
                newref.save()
                references_parent_lst.append(dic)

    return references_parent_lst


def do_zotero_manually(results, reference_model):
    """
    Process the results from the Zotero API.

    Args:
        results: The results from the Zotero API.

    Returns:
        list: A list of dictionaries containing the processed data.
    """
    references_parent_lst = []
    for item in results:
        key = item["key"]

        if key == "3BQQ8WN8":
            # Skipped because it is not in database
            continue
        if key == "RR6R3383":
            # Skipped because title is too big
            continue

        try:
            reference_model.objects.get(zotero_link=key)
            continue
        except:  # noqa: E722  TODO: Don't use bare except
            dic = {
                "key": key,
                "mainCreator": item["mainCreator"],
                "year": item["year"],
                "title": item["title"],
            }

            newref = reference_model(
                title=dic.get("title"),
                year=dic.get("year"),
                creator=dic.get("mainCreator"),
                zotero_link=dic.get("key"),
            )

            if dic.get("year") < 2040:
                newref.save()
                references_parent_lst.append(dic)

    return references_parent_lst


def update_citations_from_inside_zotero_update():
    """
    This function takes all the references and build a citation for them.

    Args:
        None

    Returns:
        None
    """
    for ref in Reference.objects.all():
        obj, _ = Citation.objects.get_or_create(
            ref=ref, page_from=None, page_to=None
        )
        obj.save()


# TODO: add to seshat.apps.core.views
def get_polity_data_single(polity_id):
    """
    Get the data for a single polity. The returned data includes the number of
    records for each app (general, sc, wf, hs, cc, pt).

    Args:
        polity_id: The ID of the polity.

    Returns:
        dict: The data for the polity.
    """
    data = {
        "hs": Human_sacrifice.objects.filter(polity=polity_id).count(),
        "cc": Crisis_consequence.objects.filter(polity=polity_id).count(),
        "pt": Power_transition.objects.filter(polity=polity_id).count(),
        "g": 0,
        "sc": 0,
        "wf": 0,
    }

    for model in get_models("general"):
        if all(
            [
                hasattr(model, "polity_id"),
                model.objects.filter(polity_id=polity_id),
            ]
        ):
            data["g"] += model.objects.filter(polity_id=polity_id).count()

    for model in get_models("sc"):
        if all(
            [
                hasattr(model, "polity_id"),
                model.objects.filter(polity_id=polity_id),
            ]
        ):
            data["sc"] += model.objects.filter(polity_id=polity_id).count()

    for model in get_models("wf"):
        if all(
            [
                hasattr(model, "polity_id"),
                model.objects.filter(polity_id=polity_id),
            ]
        ):
            data["wf"] += model.objects.filter(polity_id=polity_id).count()

    return data


# TODO: add to seshat.apps.core.views
def get_or_create_citation(reference, page_from, page_to):
    """
    Get or create a Citation instance. If a matching citation already exists, it
    is returned; otherwise, a new one is created.

    Args:
        reference (Reference): The reference.
        page_from (int): The starting page number.
        page_to (int): The ending page number.

    Returns:
        Citation: The Citation instance.
    """
    # Check if a matching citation already exists
    existing_citation = Citation.objects.filter(
        ref=reference, page_from=page_from, page_to=page_to
    ).first()

    # If a matching citation exists, return it; otherwise, create a new one
    return existing_citation or Citation.objects.create(
        ref=reference, page_from=page_from, page_to=page_to
    )


# TODO: add to seshat.apps.core.views
def get_provinces(selected_base_map_gadm="province"):
    """
    Get all the province or country shapes for the map base layer.

    Args:
        selected_base_map_gadm (str): The selected base map GADM level.

    Returns:
        list: A list of dictionaries containing the province or country shapes.
    """

    # Use the appropriate Django ORM query based on the selected baseMapGADM value
    if selected_base_map_gadm == "country":
        rows = GADMCountries.objects.values_list("geom", "COUNTRY")
        provinces = [
            {
                "aggregated_geometry": GEOSGeometry(geom).geojson,
                "country": country,
            }
            for geom, country in rows
            if geom is not None
        ]
    elif selected_base_map_gadm == "province":
        rows = GADMProvinces.objects.values_list(
            "geom", "COUNTRY", "NAME_1", "ENGTYPE_1"
        )
        provinces = [
            {
                "aggregated_geometry": GEOSGeometry(geom).geojson,
                "country": country,
                "province": name,
                "province_type": engtype,
            }
            for geom, country, name, engtype in rows
            if geom is not None
        ]

    return provinces


# TODO: add to seshat.apps.core.views

def get_polity_shape_content(
    displayed_year="all",
    seshat_id="all",
    tick_number=80,
    override_earliest_year=None,
    override_latest_year=None,
):
    """
    This function returns the polity shapes and other content for the map.
    Only one of displayed_year or seshat_id should be set; not both.

    Note:
        seshat_id in VideoShapefile is new_name in Polity.

    Args:
        displayed_year (str): The year to display the polities for. "all" will return all
            polities. Any given year will return polities that were active in that year.
        seshat_id (str): The seshat_id of the polity to display. If a value is provided,
            only the shapes for that polity being returned.

    Returns:
        dict: The content for the polity shapes.
    """

    if displayed_year != "all" and seshat_id != "all":
        raise ValueError(
            "Only one of displayed_year or seshat_id should be set not both."
        )

    if displayed_year != "all":
        rows = VideoShapefile.objects.filter(
            polity_start_year__lte=displayed_year,
            polity_end_year__gte=displayed_year,
        )
    elif seshat_id != "all":
        rows = VideoShapefile.objects.filter(seshat_id=seshat_id)
    else:
        rows = VideoShapefile.objects.all()

    # Convert 'geom' to GeoJSON in the database query
    rows = rows.annotate(geom_json=AsGeoJSON("geom")).values(
        "id",
        "seshat_id",
        "name",
        "polity",
        "start_year",
        "end_year",
        "polity_start_year",
        "polity_end_year",
        "colour",
        "area",
        "geom_json",
    )

    shapes = list(rows)

    seshat_ids = [shape["seshat_id"] for shape in shapes if shape["seshat_id"]]

    polities = Polity.objects.filter(new_name__in=seshat_ids).values(
        "new_name", "id", "long_name"
    )

    polity_info = [
        (polity["new_name"], polity["id"], polity["long_name"])
        for polity in polities
    ]

    seshat_id_page_id = {
        new_name: {"id": id, "long_name": long_name or ""}
        for new_name, id, long_name in polity_info
    }

    if "migrate" not in sys.argv:
        result = VideoShapefile.objects.aggregate(
            min_year=Min("polity_start_year"), max_year=Max("polity_end_year")
        )
        earliest_year = result["min_year"]
        latest_year = result["max_year"]
        initial_displayed_year = earliest_year
    else:
        earliest_year, latest_year = 2014, 2014
        initial_displayed_year = -3400

    if override_earliest_year is not None:
        earliest_year = override_earliest_year
    if override_latest_year is not None:
        latest_year = override_latest_year

    if displayed_year == "all":
        displayed_year = initial_displayed_year

    if seshat_id != "all":  # Used in the polity pages
        earliest_year = min([shape["start_year"] for shape in shapes])
        displayed_year = earliest_year
        latest_year = max([shape["end_year"] for shape in shapes])

    # Get the years for the tick marks on the year slider
    tick_years = [
        round(year)
        for year in np.linspace(earliest_year, latest_year, num=tick_number)
    ]

    context = {
        "shapes": shapes,
        "earliest_year": earliest_year,
        "display_year": displayed_year,
        "tick_years": json.dumps(tick_years),
        "latest_year": latest_year,
        "seshat_id_page_id": seshat_id_page_id,
    }

    return context


# TODO: add to seshat.apps.core.views
def get_all_polity_capitals():
    """
    Get capital cities for polities that have them.

    Returns:
        dict: A dictionary containing the capital cities for polities.
    """
    # Try to get the capitals from the cache
    all_capitals_info = cache.get("all_capitals_info")

    if all_capitals_info is None:
        all_capitals_info = {}
        for polity in Polity.objects.all():
            caps = get_polity_capitals(polity.id)

            if caps:
                # Set the start and end years to be the same as the polity where missing
                modified_caps = caps
                i = 0
                for capital_info in caps:
                    if capital_info["year_from"] is None:
                        modified_caps[i]["year_from"] = polity.start_year
                    if capital_info["year_to"] is None:
                        modified_caps[i]["year_to"] = polity.end_year
                    i += 1
                all_capitals_info[polity.new_name] = modified_caps
        # Store the capitals in the cache for 1 hour
        cache.set("all_capitals_info", all_capitals_info, 3600)

    return all_capitals_info


# TODO: add to seshat.apps.core.views
def assign_variables_to_shapes(shapes, app_map):
    """
    Assign the absent/present variables to the shapes.

    Args:
        shapes (list): The shapes to assign the variables to.
        app_map (dict): A dictionary mapping app names to their long names.

    Returns:
        tuple: A tuple containing the shapes and the variables.
    """
    # Try to get the variables from the cache
    variables = cache.get("variables")
    if variables is None:
        variables = {}
        for app_name, app_name_long in app_map.items():
            variables[app_name_long] = {}
            for model in get_models(app_name):
                fields = list(model._meta.get_fields())

                for field in fields:
                    if (
                        hasattr(field, "choices")
                        and field.choices == ABSENT_PRESENT_CHOICES
                    ):
                        # Get the variable name and formatted name
                        if field.name == "coded_value":
                            # Use the class name lower case for rt models where coded_value
                            # is used
                            var_name = model.__name__.lower()
                            var_long = getattr(
                                model._meta,
                                "verbose_name_plural",
                                var_name,
                            )
                            if var_name == var_long:
                                variable_formatted = (
                                    var_name.capitalize().replace("_", " ")
                                )
                            else:
                                variable_formatted = var_long
                        else:  # Use the field name for other models
                            var_name = field.name
                            variable_formatted = (
                                field.name.capitalize().replace("_", " ")
                            )

                        # Get the variable subsection and subsubsection if they exist
                        variable_full_name = variable_formatted

                        instance = model()
                        if hasattr(instance, "subsubsection"):
                            variable_full_name = f"{instance.subsubsection()}: {variable_full_name}"  # noqa: E501

                        if hasattr(instance, "subsection"):
                            variable_full_name = f"{instance.subsection()}: {variable_full_name}"  # noqa: E501

                        variables[app_name_long][var_name] = {
                            "formatted": variable_formatted,
                            "full_name": variable_full_name
                        }

        # Store the variables in the cache for 1 hour
        cache.set("variables", variables, 3600)

    for app_name, app_name_long in app_map.items():
        app_variables_list = list(variables[app_name_long].keys())
        module_path = "seshat.apps." + app_name + ".models"
        module = __import__(
            module_path,
            fromlist=[
                variable.capitalize() for variable in app_variables_list
            ],
        )
        variable_classes = {
            variable: getattr(module, variable.capitalize())
            for variable in app_variables_list
        }

        seshat_ids = [
            shape["seshat_id"]
            for shape in shapes
            if shape["seshat_id"] != "none"
        ]
        polities = {
            polity.new_name: polity
            for polity in Polity.objects.filter(new_name__in=seshat_ids)
        }

        for variable, class_ in variable_classes.items():
            variable_formatted = variables[app_name_long][variable][
                "formatted"
            ]
            variable_objs = {
                obj.polity_id: obj
                for obj in class_.objects.filter(
                    polity_id__in=polities.values()
                )
            }

            all_variable_objs = {}
            for obj in class_.objects.filter(polity_id__in=polities.values()):
                try:
                    variable_value = getattr(obj, variable)
                except AttributeError:
                    # For rt models where coded_value is used
                    variable_value = getattr(obj, "coded_value")
                if obj.polity_id not in all_variable_objs:
                    all_variable_objs[obj.polity_id] = {}
                all_variable_objs[obj.polity_id][variable_value] = [
                    obj.year_from,
                    obj.year_to,
                ]

            for shape in shapes:
                shape[variable_formatted] = "uncoded"  # Default value
                polity = polities.get(shape["seshat_id"])
                if polity:
                    variable_obj = variable_objs.get(polity.id)
                    try:
                        variable_obj_dict = all_variable_objs[polity.id]
                    except KeyError:
                        pass
                    if variable_obj:
                        try:
                            # Absent/present choice
                            shape[variable_formatted] = getattr(
                                variable_obj, variable
                            )
                            shape[variable_formatted + "_dict"] = (
                                variable_obj_dict
                            )
                        except AttributeError:
                            # For rt models where coded_value is used
                            shape[variable_formatted] = getattr(
                                variable_obj, "coded_value"
                            )
                            shape[variable_formatted + "_dict"] = (
                                variable_obj_dict
                            )
                else:
                    shape[variable_formatted] = "no seshat page"

    return shapes, variables


# TODO: add to seshat.apps.core.views
def assign_categorical_variables_to_shapes(shapes, variables):
    """
    Assign the categorical variables to the shapes.

    Note:
        Currently only language is implemented.

    Args:
        shapes (list): The shapes to assign the variables to.
        variables (dict): The variables to assign to the shapes.

    Returns:
        tuple: A tuple containing the shapes and the variables.
    """
    # Add language variables to the variables
    variables["General Variables"] = {
        "polity_linguistic_family": {
            "formatted": "linguistic_family",
            "full_name": "Linguistic Family",
        },
        "polity_language_genus": {
            "formatted": "language_genus",
            "full_name": "Language Genus",
        },
        "polity_language": {"formatted": "language", "full_name": "Language"},
    }

    # Fetch all polities and store them in a dictionary for quick access
    polities = {polity.new_name: polity for polity in Polity.objects.all()}

    # Fetch all linguistic families, language genuses, and languages and store them in
    # dictionaries for quick access
    linguistic_families = {}
    for lf in Polity_linguistic_family.objects.all():
        if lf.polity_id not in linguistic_families:
            linguistic_families[lf.polity_id] = []
        linguistic_families[lf.polity_id].append(lf)

    language_genuses = {}
    for lg in Polity_language_genus.objects.all():
        if lg.polity_id not in language_genuses:
            language_genuses[lg.polity_id] = []
        language_genuses[lg.polity_id].append(lg)

    languages = {}
    for language in Polity_language.objects.all():
        if language.polity_id not in languages:
            languages[language.polity_id] = []
        languages[language.polity_id].append(language)

    # Add language variable info to polity shapes
    for shape in shapes:
        shape["linguistic_family"] = []
        shape["linguistic_family_dict"] = {}
        shape["language_genus"] = []
        shape["language_genus_dict"] = {}
        shape["language"] = []
        shape["language_dict"] = {}
        if shape["seshat_id"] != "none":  # Skip shapes with no seshat_id
            polity = polities.get(shape["seshat_id"])
            if polity:
                # Get the linguistic family, language genus, and language for the polity
                shape["linguistic_family"].extend(
                    [
                        lf.linguistic_family
                        for lf in linguistic_families.get(polity.id, [])
                    ]
                )
                shape["language_genus"].extend(
                    [
                        lg.language_genus
                        for lg in language_genuses.get(polity.id, [])
                    ]
                )
                shape["language"].extend(
                    [lang.language for lang in languages.get(polity.id, [])]
                )

                # Get the years for the linguistic family, language genus, and language for
                # the polity
                shape["linguistic_family_dict"].update(
                    {
                        lf.linguistic_family: [lf.year_from, lf.year_to]
                        for lf in linguistic_families.get(polity.id, [])
                    }
                )
                shape["language_genus_dict"].update(
                    {
                        lg.language_genus: [lg.year_from, lg.year_to]
                        for lg in language_genuses.get(polity.id, [])
                    }
                )
                shape["language_dict"].update(
                    {
                        lang.language: [lang.year_from, lang.year_to]
                        for lang in languages.get(polity.id, [])
                    }
                )

        # If no linguistic family, language genus, or language was found, append 'Uncoded'
        polity = polities.get(shape["seshat_id"])
        if polity:
            if not shape["linguistic_family"]:
                shape["linguistic_family"].append("Uncoded")
            if not shape["language_genus"]:
                shape["language_genus"].append("Uncoded")
            if not shape["language"]:
                shape["language"].append("Uncoded")
        else:
            if not shape["linguistic_family"]:
                shape["linguistic_family"].append("No Seshat page")
            if not shape["language_genus"]:
                shape["language_genus"].append("No Seshat page")
            if not shape["language"]:
                shape["language"].append("No Seshat page")

    return shapes, variables


# TODO: add to seshat.apps.core.views
def random_polity_shape():
    """
    This function is used to get a random polity for the world map initial view.
    It selects a polity with a seshat_id and a start year.

    Use the VideoShapefile model to get the polity shapes.
    Choose one that has a seshat_id.
    Return the seshat_id and start year.

    Returns:
        tuple: A tuple containing the start year and seshat_id.
    """
    max_id = VideoShapefile.objects.filter(seshat_id__isnull=False).aggregate(
        max_id=Max("id")
    )["max_id"]
    while True:
        pk = random.randint(1, max_id)
        shape = VideoShapefile.objects.filter(
            seshat_id__isnull=False, id=pk
        ).first()
        if shape:
            if shape.seshat_id and shape.area > 600000:  # Big empires only
                break
    return shape.start_year, shape.seshat_id


# TODO: add to seshat.apps.core.views
def common_map_view_content(context):
    """
    Set of functions that update the context and run in each map view function.

    Args:
        context (dict): The context for the polity shapes.

    Returns:
        dict: The updated context for the polity shapes.
    """
    # Add in the present/absent variables to view for the shapes
    context["shapes"], context["variables"] = assign_variables_to_shapes(
        context["shapes"], APP_MAP
    )

    # Add in the categorical variables to view for the shapes
    context["shapes"], context["variables"] = (
        assign_categorical_variables_to_shapes(
            context["shapes"], context["variables"]
        )
    )

    # Load the capital cities for polities that have them
    context["all_capitals_info"] = get_all_polity_capitals()

    # Add categorical variable choices to the context for dropdown selection
    context["categorical_variables"] = CATEGORICAL_VARIABLES

    # Set the initial polity to highlight
    context["world_map_initial_polity"] = WORLD_MAP_INITIAL_POLITY

    return context


# TODO: add to seshat.apps.core.views
def get_polity_capitals(pk):
    """
    Get all the capitals for a polity and coordinates.

    Args:
        pk (int): The primary key of the polity.

    Returns:
        list: A list of dictionaries containing the capital name, latitude,
            longitude, start year (or 0 or None if they aren't present in the
            database), and end year (or 0 or None if they aren't present in
            the database).
    """
    capitals_info = []
    for polity_capital in Polity_capital.objects.filter(polity_id=pk):
        capitals = Capital.objects.filter(name=polity_capital.capital)

        for capital in capitals:
            if capital.name and capital.latitude and capital.longitude:
                capital_info = {
                    "capital": capital.name,
                    "latitude": float(capital.latitude),
                    "longitude": float(capital.longitude),
                }

                if polity_capital.year_from == 0:
                    capital_info["year_from"] = 0
                elif polity_capital.year_from is not None:
                    capital_info["year_from"] = polity_capital.year_from
                else:
                    capital_info["year_from"] = None

                if polity_capital.year_to == 0:
                    capital_info["year_to"] = 0
                elif polity_capital.year_to is not None:
                    capital_info["year_to"] = polity_capital.year_to
                else:
                    capital_info["year_to"] = None

                capitals_info.append(capital_info)

    return capitals_info
