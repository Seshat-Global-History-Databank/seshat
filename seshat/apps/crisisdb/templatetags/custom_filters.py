from django import template

import re
import uuid

from ...global_utils import get_color


register = template.Library()


@register.filter
def get_columns_with_value(instance, value):
    return instance.get_columns_with_value(value)


@register.filter
def get_columns_with_value_dic(instance, value):
    """
    This filter takes a CrisisDB instance and a value and returns a dictionary with the
    column names as keys and the values as a list of values for the given column name.

    Args:
        instance (CrisisDB): The CrisisDB instance.

    Returns:
        dict: A dictionary with the column names as keys and the values as a list of values
            for the given column name.
    """
    return instance.get_columns_with_value_dic(value)


@register.filter
def replace_underscore_and_capitalize(value):
    """
    This filter takes a string and replaces all the underscores with spaces and capitalizes
    the first letter of each word.

    Args:
        value (str): The string to be processed.

    Returns:
        str: The processed string.
    """
    value = value.replace("_", " ")
    return value.title()


@register.filter
def get_item_from_dic(dictionary, key):
    """
    This filter takes a dictionary and a key and returns the value associated with the key
    in the dictionary.

    Args:
        dictionary (dict): The dictionary.
        key (str): The key to search for in the dictionary.

    Returns:
        Any: The value associated with the key in the dictionary.
    """
    return dictionary.get(key)


@register.filter
def username_from_email(email):
    """
    This filter takes an email address and returns the username part of the email address.

    Args:
        email (str): The email address.

    Returns:
        str: The username part of the email address.
    """
    return email.split("@")[0]


@register.filter
def make_references_look_nicer(value):
    """
    This filter takes a string and replaces all the references in the format
    "§REF§Reference Text§REF§" with a superscript tag that contains a link to the reference
    at the end of the string. The references are displayed in a separate <p> tag
    at the end of the string with a red color.

    Args:
        value (str): The string containing references in the format
            "§REF§Reference Text§REF§".

    Returns:
        str: The string with references replaced by superscript tags and references
            displayed at the end of the string.
    """
    value = value.replace("'", "&rsquo;").replace("\n", "MJD_BNM_NEWLINE_TAG_XYZ")
    pattern = r"§REF§(.*?)§REF§"
    replacement = r"""<sup class="fw-bold" id="sup_{ref_id}">
        <a href="#{ref_id}">[{ref_num}]</a>
    </sup>
    """
    new_string = value
    references = re.findall(pattern, value)

    # Dictionary to store unique reference numbers and their corresponding unique
    # identifiers
    reference_data = {}

    # Assign a unique reference number and identifier to each reference in the order they
    # appear
    for _, reference in enumerate(references):
        if reference not in reference_data:
            ref_num = len(reference_data) + 1
            ref_id = f"ref_{ref_num}_{str(uuid.uuid4())[:8]}"
            reference_data[reference] = {"ref_num": ref_num, "ref_id": ref_id}

        data = reference_data[reference]
        sup_tag = replacement.format(ref_num=data["ref_num"], ref_id=data["ref_id"])
        new_string = new_string.replace(f"§REF§{reference}§REF§", sup_tag, 1)

    # Add the collected references at the end of the string in separate <p> tags with the
    # color red
    if reference_data:
        reference_tags = "\n".join(
            [
                f'<p id="{data["ref_id"]}" class="p-0 m-0 text-secondary"><span class="fw-bold">  <a href="#sup_{data["ref_id"]}">[{data["ref_num"]}]</a></span>: <span>{reference.replace("MJD_BNM_NEWLINE_TAG_XYZ", " ")}</span> </p>'  # noqa: E501 pylint: disable=C0301
                for reference, data in reference_data.items()
            ]
        )
        new_string += reference_tags

    paragraphed_string = new_string.replace("MJD_BNM_NEWLINE_TAG_XYZ", "<br>")

    return paragraphed_string


@register.filter
def give_me_a_color(value):
    """
    This filter takes a value and returns a color from the LIGHT_COLORS list based on the
    value.

    Args:
        value (int): The value to determine the color.

    Returns:
        str: The color from the LIGHT_COLORS list based on the value.
    """
    return get_color(value)
