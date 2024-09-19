__all__ = [
    "get_data_for_polity",
    "get_model_data",
    "get_polity_app_data",
]

from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from ..global_utils import get_models
from ..crisisdb.models import (
    Crisis_consequence,
    Power_transition,
    Human_sacrifice,
)


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

    return {
        model.model_class()
        .__name__: model.model_class()
        .objects.filter(polity=polity_id)
        for model in app_content_types
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
