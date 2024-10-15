"""
Utility functions used across the Seshat app.
"""

__all__ = [
    "get_model_instance_name",
    "validate_time_range",
    "return_citations",
    "clean_email",
    "check_permissions",
    "get_date",
    "get_models",
    "get_problematic_data_context",
    "convert_to_year_span",
    "remove_html_tags",
    "get_api_results",
    "get_csv_path",
    "get_color",
    "get_filename",
    "get_response",
    "get_headers",
    "get_row",
    "fill_data",
    "get_meta_dict",
    "write_csv",
    "has_add_capital_permission",
    "get_all_data",
    "get_variable_context",
]

import csv
import datetime
import functools
import json
import os
import warnings

from typing import Union

import requests

from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden, HttpResponse
from django.utils.safestring import mark_safe

from .constants import (
    ATTRS_HTML,
    CSV_DELIMITER,
    ICONS,
    LIGHT_COLORS,
    NO_DATA,
    US_STATES_GEOJSON_PATH
)
from .patterns import PATTERNS


def get_model_instance_name(cls) -> str:
    """
    This function is used to return the name of the model instance (in lieu of
    the __str__ representation of the model instance).

    Note:
        The model instance must have the following attributes:
        - name
        - polity (and polity.name)
        - year_from
        - year_to

    Args:
        self (model instance): The model instance.

    Returns:
        str: The name of the model instance.
    """
    if cls.year_from == cls.year_to or ((not cls.year_to) and cls.year_from):
        return f"{cls.name} [for {cls.polity.name} in {cls.year_from}]"

    return f"{cls.name} [for {cls.polity.name} from {cls.year_from} to {cls.year_to}]"


def _wrap_in_warning(string) -> str:
    """
    This private function is used to wrap a string in a warning span.

    Args:
        string (str): The string to wrap.

    Returns:
        str: The string wrapped in a warning span.
    """
    return f"<span {ATTRS_HTML.text_danger}>{ICONS.triangle_exclamation} {string}</span>"


def validate_time_range(cls, limited=False) -> bool:
    """
    This function is used to validate the year_from and year_to fields of the
    model instance (called from each model's clean method).

    Note:
        The model instance must have the following attributes:
        - year_from
        - year_to
        - polity (and polity.start_year and polity.end_year)

    Args:
        cls (model instance): The model instance.

    Returns:
        bool: True if the year_from and year_to fields are valid.

    Raises:
        ValidationError: If the year_from is greater than the year_to.
        ValidationError: If the year_from is out of range.
        ValidationError: If the year_from is earlier than the start year of the
            corresponding polity.
        ValidationError: If the year_to is later than the end year of the corresponding
            polity.
        ValidationError: If the year_to is out of range.
    """
    current_year = get_date("%Y")

    # Check if the start year is greater than the end year.
    if (cls.year_from and cls.year_to) and cls.year_from > cls.year_to:
        string = _wrap_in_warning(
            "The start year is bigger than the end year!"
        )
        raise ValidationError(
            {
                "year_from": mark_safe(string),
            }
        )

    # Check if the start year is out of range.
    if cls.year_from and (cls.year_from > current_year):
        string = _wrap_in_warning("The start year is out of range!")
        raise ValidationError(
            {
                "year_from": mark_safe(string),
            }
        )

    if limited:
        return True

    # Check if the start year is earlier than the start year of the corresponding polity.
    if cls.year_from and (cls.year_from < cls.polity.start_year):
        string = _wrap_in_warning(
            "The start year is earlier than the start year of the corresponding polity!"
        )  # noqa: E501 pylint: disable=C0301
        raise ValidationError(
            {
                "year_from": mark_safe(string),
            }
        )

    # Check if the end year is later than the end year of the corresponding polity.
    if cls.year_to and (cls.year_to > cls.polity.end_year):
        string = _wrap_in_warning(
            "The end year is later than the end year of the corresponding polity!"
        )  # noqa: E501 pylint: disable=C0301
        raise ValidationError(
            {
                "year_to": mark_safe(string),
            }
        )

    # Check if the end year is out of range.
    if cls.year_to and (cls.year_to > current_year):
        string = _wrap_in_warning("The end year is out of range!")
        raise ValidationError(
            {
                "year_to": mark_safe(string),
            }
        )

    return True


def return_citations(
    cls, join_str: str = ", ", limit: int = 2, custom_func=None
) -> str:
    """
    This function is used to return the citations of the model instance
    (returning the value used in the display_citations method of the model
    instance).

    Note:
        The model instance must have the following attribute:
        - citations

        The model instance must have the following methods:
        - zoteroer

    Args:
        cls (model instance): The model instance.
        join_str (str): The string to join the citations with. Default is ", ".
        limit (int): The maximum number of citations to return. Default is 2.

    Returns:
        str: The citations of the model instance, separated by comma.
    """

    return join_str.join(
        [
            f'<a href="{citation.zotero_link}">{custom_func(citation) if isinstance(custom_func, callable) else citation}"</a>"'  # noqa: E501 pylint: disable=C0301
            for citation in cls.citations.all()[:limit]
        ]
    )


def clean_email(email) -> str:
    """
    A method to clean an email address and check if it contains too many
    dots in the username part.

    Args:
        email (str): The email address.

    Returns:
        str: The email address if it is valid.

    Raises:
        ValidationError: If the email address contains too many dots in the
            username part.
    """
    username, _ = email.split("@")
    username_parts = username.split(".")

    if len(username_parts) > 5:
        raise ValidationError(
            "Email address contains too many dots in the username part."
        )

    return email


def check_permissions(
    request,
    permissions_required="core.add_capital",
    error_msg="You don't have permission to delete this object.",
    error=HttpResponseForbidden,
) -> None:
    """
    This function is used to check if the user has the required permissions.

    Args:
        request (HttpRequest): The request object.
        permissions_required (str): The permissions required.
        error_msg (str): The error message to display.
        error (HttpResponseForbidden): The error response.

    Returns:
        None

    Raises:
        error: If the user does not have the required permissions.
    """
    if not request.user.has_perm(permissions_required):
        return error(error_msg)

    return None


def get_date(fmt=None) -> str:
    """
    This function is used to get the current date in the specified format.

    Args:
        fmt (str): The format of the date.

    Returns:
        str: The current date in the specified format.
    """
    if fmt:
        try:
            return int(datetime.datetime.now().strftime(fmt))
        except ValueError:
            return datetime.datetime.now().strftime(fmt)

    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def get_models(app_name: str, exclude: list = None, subsection=None) -> list:
    """
    This function is used to get all models from an app.

    Args:
        app_name (str): The name of the app.
        exclude (list): A list of names (as strings) of models to exclude.

    Returns:
        list: A list of models from the app.
    """
    if not exclude:
        exclude = []

    # Make all exclude lowercase to avoid case sensitivity
    exclude = [x.lower() for x in exclude]

    # Drop excluded models
    models = [
        model
        for model in apps.get_app_config(app_name).get_models()
        if model.__name__.lower() not in exclude
    ]

    if subsection:
        return [
            model
            for model in models
            if str(model().subsection()) == subsection
        ]

    return models


def get_problematic_data_context(
    app_name: str = "",
    conditions: list = [
        lambda o: o.polity.start_year is not None,
        lambda o: o.year_from is not None,
        lambda o: o.polity.start_year > o.year_from,
    ],
    models: list = None,
) -> dict:
    """
    This function is intended to be used to find problematic data in the database.
    It takes an app name and a list of conditions as lambda functions.
    It returns a context dictionary with the problematic data.

    Args
    ----
    app_name : str
        The name of the app where the models are located.
    conditions : list
        A list of lambda functions that take an object as input and return a boolean value.
    models : list
        A list of models to check. If not provided, all models in the app will be checked.

    Returns
    -------
    context : dict
        A dictionary with the problematic data.

    Raises
    ------
    SyntaxError
        If no conditions are provided.
        If any condition is not callable.
        If no app name or models are provided.
    """
    if not conditions or not isinstance(conditions, list):
        raise SyntaxError(
            "This is not how the function is intended to be used. \
            You need to provide at least one condition as a lambda function inside a list."
        )

    if all(not callable(c) for c in conditions):
        raise SyntaxError("All conditions must be callable.")

    if not app_name and not models:
        raise SyntaxError(
            "You need to provide either an app name or a list of models to check."
        )

    context = {"data": []}

    if not models:
        models = get_models(app_name)

    for model in models:
        for obj in model.objects.all():
            passes = True
            for condition in conditions:
                if not condition(obj):
                    # Exit loop if any condition fails
                    passes = False
                    break

            # Add object to context only if it passed all conditions
            if passes:
                context["data"] += [obj]

    return context


def convert_to_year_span(year_from: int, year_to: int) -> str:
    """
    This function is used to convert the year_from and year_to fields to a
    year span.

    Args:
        year_from (int): The start year.
        year_to (int): The end year.

    Returns:
        str: The year span.

    Examples:

    >>> convert_to_year_span(1000, 1100)
    "[1000 CE ➜ 1100 CE]"

    >>> convert_to_year_span(-1000, -1100)
    "[1000 BCE ➜ 1100 BCE]"
    """
    # We have no years
    if all([year_from is None, year_to is None]):
        return NO_DATA.default

    # year_from is the same as year_to or we only have a year_from
    if year_from == year_to or year_to is None:
        if year_from < 0:
            return f"{year_from:,} BCE"

        return f"{year_from:,} CE"

    # year_from and year_to are both BCE
    if year_from < 0 > year_to:
        return f"[{year_from:,} BCE ➜ {year_to:,} BCE]"

    # year_from is BCE and year_to is CE
    if year_from < 0 <= year_to:
        return f"[{year_from:,} BCE ➜ {year_to:,} CE]"

    # year_from and year_to are both in CE
    return f"[{year_from:,} CE ➜ {year_to:,} CE]"


def remove_html_tags(text: str) -> str:
    """
    This function is used to remove HTML tags from a string.

    Args:
        text (str): The text containing HTML tags.

    Returns:
        str: The text without HTML tags.

    Examples:

    >>> remove_html_tags("<p>Hello, <strong>world</strong>!</p>")
    "Hello, world!"
    """
    return PATTERNS.HTML_TAGS.sub("", text)


def get_api_results(endpoint: str = "politys-api") -> list:
    """
    This function is used to get the results from the API.

    Args:
        endpoint (str): The endpoint of the API.

    Returns:
        list: The results from the API.
    """
    # Set correct URL
    url = f"http://127.0.0.1:8000/api/{endpoint}"

    # Get response
    resp = requests.get(url, headers={"Accept": "application/json"}, timeout=5)

    return resp.json()["results"]


def get_csv_path(file: str) -> str:
    """
    This function is used to get the path of a given CSV file in the static
    directory.

    Args:
        file (str): The name of the CSV file.

    Returns:
        str: The path of the CSV file.
    """
    return os.path.join(settings.STATIC_ROOT, "csvfiles", file)


def get_color(value: Union[str, int]) -> str:
    """
    Returns a color for a given expert.

    Args:
        value (str | int): The id of the expert.

    Returns:
        str: A color for the expert.
    """
    if isinstance(value, str):
        value = int(value)

    return LIGHT_COLORS[value % 30]


####################################################
# Download views utils                             #
####################################################


def get_filename(model, prefix: str = "") -> str:
    """
    Get the filename for the CSV file from the given model's plural name.

    Args:
        model (Model): The model to get the filename for.

    Returns:
        str: The filename for the CSV file.
    """
    plural_model_name = model._meta.verbose_name_plural.lower().replace(
        " ", "_"
    )
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{prefix}{plural_model_name}_{current_datetime}.csv"


def get_response(model=None, prefix: str = "", filename=None) -> HttpResponse:
    """
    Get the response object for the CSV file.

    Args:
        model (Model): The model to get the response for.

    Returns:
        HttpResponse: The response object for the CSV file.
    """
    if not any([model, filename]):
        raise ValueError("You must provide either a model or a filename.")

    filename = get_filename(model, prefix) if not filename else filename

    return HttpResponse(
        headers={
            "Content-Type": "text/csv",
            "Content-Disposition": f'attachment; filename="{filename}"',
        }
    )


def get_headers(
    model, add_from_to_values: list = ["Long_wall"]
) -> list:  # noqa: E501 pylint: disable=W0102
    """
    Get the headers for the CSV file for the given model.

    Args:
        model (Model): The model to get the headers for.
        add_from_to_values (list): The list of models to add the "from" and "to"
            values for.

    Returns:
        list: The headers for the CSV file.
    """
    rows = [
        "variable_name",
        "year_from",
        "year_to",
        "polity_name",
        "polity_new_ID",
        "polity_old_ID",
    ]

    if model.__name__ in add_from_to_values:
        rows += [
            "long_wall_from",
            "long_wall_to",
        ]
    else:
        model += [model._meta.verbose_name]

    rows += [
        "confidence",
        "is_disputed",
        "is_uncertain",
        "expert_checked",
    ]

    return rows


def get_row(
    model, obj, add_from_to_values: list = ["Long_wall"]
) -> list:  # noqa: E501 pylint: disable=W0102
    """
    Get the row for the given model and object.

    Args:
        model (Model): The model of the object.
        obj (Model instance): The object to get the row for.

    Returns:
        list: The row for the given model and object.
    """
    row = [
        obj.name,
        obj.year_from,
        obj.year_to,
        obj.polity,
        obj.polity.new_name,
        obj.polity.name,
    ]

    if model.__name__ in add_from_to_values:
        row += [
            obj.show_value_from(),
            obj.show_value_to(),
        ]
    else:
        pass  # TODO: this should insert a value??? (show_value?)

    row += [
        obj.get_tag_display(),
        obj.is_disputed,
        obj.is_uncertain,
        obj.expert_reviewed,
    ]

    return row


def fill_data(model, writer):
    """
    Fill the data for the given model.

    Args:
        model (Model): The model to fill the data for.
        writer (csv.writer): The writer object for the CSV file.

    Returns:
        csv.writer: The writer object for the CSV file.
    """
    objects = model.objects.all()

    for obj in objects:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.show_value_from(),
                obj.show_value_to(),
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return writer


def get_meta_dict(model, level="outer"):
    """
    Get the metadata for the given model.

    Args:
        model (Model): The model to get the metadata for.
        level (str): The level of metadata to get.

    Returns:
        dict: The metadata for the given model.

    Raises:
        AttributeError: If the model does not have a "Code" metaclass registered.
        SyntaxError: If the level provided is not "outer" or "inner".
    """
    try:
        model.Code
    except AttributeError as exc:
        raise AttributeError(
            "It seems like the model {model.__name__} does not have a Code metaclass registered."  # noqa: E501 pylint: disable=C0301
        ) from exc

    if level == "outer":
        return {
            "notes": model.Code.notes,
            "main_desc": model.Code.description,
            "main_desc_source": model.Code.description_source,
            "section": model.Code.section,
            "subsection": model.Code.subsection,
        }

    if level == "inner":
        return model.Code.inner_variables

    raise SyntaxError("level provided must be either outer or inner")


def write_csv(model, level="objects", prefix=""):
    """
    Write the CSV file for the given model.

    Args:
        response (HttpResponse): The response object for the CSV file.

    Returns:
        csv.writer: The writer object for the CSV file.
    """
    response = get_response(model, prefix)
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

    if level == "objects":
        writer.writerow(get_headers(model))
        writer = fill_data(model, writer)
    elif level == "meta":
        meta_dic = get_meta_dict(model, "outer")
        meta_dic_inner = get_meta_dict(model, "inner")

        for k, v in meta_dic.items():
            writer.writerow([k, v])

        for k_inner, v_inner in meta_dic_inner.items():
            writer.writerow(
                [
                    k_inner,
                ]
            )

            for inner_key, inner_value in v_inner.items():
                if inner_value:
                    writer.writerow([inner_key, inner_value])

    return response


def _get_context(cls, standard=True, context=None):
    """
    Get the standard context for a view. Private helper function.

    Args:
        cls: The class of the view.

    Returns:
        dict: The standard context for the view.
    """
    _context = {
        "myvar": cls.model.Code.variable,
        "my_exp": cls.model.Code.description,
        "var_null_meaning": cls.model.Code.null_meaning,
        "inner_vars": cls.model.Code.inner_variables,
        "potential_cols": cls.model.Code.potential_cols,
    }

    if not standard:
        _context = {
            "myvar": cls.model.Code.variable,
            "my_exp": cls.model.Code.description,
            "var_null_meaning": cls.model.Code.null_meaning,
            "inner_vars": cls.model.Code.inner_variables,
            "potential_cols": cls.model.Code.potential_cols,
        }

    if context:
        _context = dict(context, **_context)

    return _context


def has_add_capital_permission(user):
    """
    Check if the user has the 'core.add_capital' permission.

    Note:
        TODO: This is built-in functionality in Django. You can use the built-in
        permission_required decorator instead.

    Args:
        user (User): The user object.

    Returns:
        bool: True if the user has the 'core.add_capital' permission, False otherwise.
    """
    return user.has_perm("core.add_capital")


def _query(m, polity):
    """
    Get query for model. Private helper function.

    Args:
        m: The model.
        polity: The polity.

    Returns:
        QuerySet: The query set for the model.
    """
    if hasattr(m, "other_polity"):
        _filter = Q(polity=polity) | Q(other_polity=polity)
    else:
        _filter = Q(polity=polity)

    queryset = m.model_class().objects.filter(_filter)

    return queryset


def get_all_data(app_label, polity, exclude=None):
    """
    Get all data for the given polity ID.

    Args:
        app_label: The label of the app.
        polity: The polity.
        exclude: A list of models to exclude.

    Returns:
        bool: True if there is any data, False otherwise.
        dict: A dictionary of all data for the polity.
    """
    if not exclude:
        exclude = [
            "Ra",
            "Polity_editor",
            "Polity_research_assistant",
            "Polity_expert",
        ]

    # Get all models
    models = get_models(app_label, exclude=exclude)

    # Set up sorted_variables
    def get_subsection(model):
        try:
            return str(model()._subsection)
        except AttributeError:
            return "None"

    def get_subsubsection(model):
        try:
            return str(model()._subsubsection)
        except AttributeError:
            return "None"

    sorted_variables = dict(
        {get_subsection(model): {} for model in models},
        **{"None": {"None": {}}},
    )

    for model in models:
        sorted_variables[get_subsection(model)][get_subsubsection(model)] = {}

    # Get models for polity ID

    exclude_names = [x.lower() for x in exclude]
    cts = ContentType.objects.filter(app_label=app_label).exclude(
        model__in=exclude_names
    )

    def try_catch(m):
        try:
            return m.model_class().objects.for_polity(polity)
        except AttributeError:
            print(m, "failed")

    model_data = [
        (
            get_subsection(m.model_class),
            get_subsubsection(m.model_class),
            m.model_class().__name__,
            try_catch(m),
        )
        for m in cts
    ]

    model_data = [
        x for x in model_data if x[3].exists() and not x[2] in exclude
    ]

    for subsection, subsubsection, name, objects in model_data:
        sorted_variables[subsection][subsubsection][name] = objects

    has_any_data = True if model_data else False

    return has_any_data, sorted_variables


def get_variable_context(
    prefix: str = "download_csv_", app_name: str = None, exclude: list = ["Ra"]
) -> dict:
    """
    Get the variable context for the given app name, for the general variable page.

    Args:
        prefix (str): The prefix for the variable name.
        app_name (str): The name of the app.
        exclude (list): A list of models to exclude.

    Returns:
        dict: The variable context for the given app name.
    """
    if not app_name:
        raise ValueError("app_name must be provided")

    all_vars_grouped, section_download_names = {}, {}
    variable_count, row_count = 0, 0
    unique_polities = []

    for model in get_models(app_name, exclude=exclude):
        subsection = str(model().subsection())
        subsubsection = str(model().subsubsection())

        subsection_str = (
            subsection.replace("-", "_")
            .replace(" ", "_")
            .replace(":", "")
            .lower()
        )  # noqa: E501

        section_download_names[subsection] = f"{prefix}{subsection_str}"

        if subsection not in all_vars_grouped:
            all_vars_grouped[subsection] = {}

        if subsubsection not in all_vars_grouped[subsection]:
            all_vars_grouped[subsection][subsubsection] = []

        objects = model.objects.all()
        objects_count = objects.count()

        row_count += objects_count
        variable_count += 1

        unique_polities += objects.values_list("polity", flat=True).distinct()

        model_name = model.__name__
        model_title = model_name.replace("_", " ").title()
        model_create = model_name.lower() + "-create"
        model_download_view = model_name.lower() + "-download"
        model_metadownload = model_name.lower() + "-metadownload"
        model_all = model_name.lower() + "s_all"
        model_s = model_name.lower() + "s"

        lst = [
            model_title,
            model_s,
            model_create,
            model_download_view,
            model_metadownload,
            model_all,
            objects_count,
        ]

        all_vars_grouped[subsection][subsubsection] += [lst]

    return {
        "all_vars_grouped": all_vars_grouped,
        "all_sect_download_view_links": section_download_names,
        "all_polities": len(set(unique_polities)),
        "number_of_all_rows": row_count,
        "number_of_variables": variable_count,
    }


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter("always", DeprecationWarning)  # turn off filter
        warnings.warn(
            f"Call to deprecated function {func.__name__}.",
            category=DeprecationWarning,
            stacklevel=2,
        )
        warnings.simplefilter("default", DeprecationWarning)  # reset filter
        return func(*args, **kwargs)

    return new_func


def load_us_states_geojson():
    try:
        with open(US_STATES_GEOJSON_PATH, "r") as json_file:
            data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    return data
