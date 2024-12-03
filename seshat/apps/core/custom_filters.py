from django import template

register = template.Library()

@register.filter
def get_attributes(obj):
    """
    A custom filter to get all attributes of an object in a template.

    Args:
        obj (object): The object to get attributes from.

    Returns:
        dict: A dictionary of the object's attributes.
    """
    return vars(obj)

@register.filter
def zip_lists(a, b):
    """
    A custom filter to zip two lists together in a template.

    Args:
        a (list): The first list to zip.
        b (list): The second list to zip.

    Returns:
        zip: A zip object of the two lists.
    """
    return zip(a, b)

