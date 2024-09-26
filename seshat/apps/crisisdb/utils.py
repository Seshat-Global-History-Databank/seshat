__all__ = [
    "return_citations",
    "expand_context_from_variable_hierarchy",
]

from ..constants import ICONS, NO_DATA
from ..core.models import Variablehierarchy


def return_citations(cls):
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

    Returns:
        str: The citations of the model instance, separated by comma.
    """
    return "<br />".join(
        [
            f'<a href="{citation.zotero_link}">{ICONS.book} {citation.full_citation_display()}</a>'  # noqa: E501 pylint: disable=C0301
            for citation in cls.citations.all()
        ]
    )


def expand_context_from_variable_hierarchy(
    context: dict, db_name: str, variable_name: str
) -> dict:
    """
    Expand the context data for the view from the Variablehierarchy model.

    Args:
        context (dict): Context data for the view
        variable_name (str): Name of the variable

    Returns:
        dict: Expanded context data for the view

    ..
        Note:

        The old code in this function was dysfunctional and was replaced with
        the current implementation. The old code was:

        > variable_hierarchies = Variablehierarchy.objects.all()
        >
        > if variable_hierarchies:
        >     for item in variable_hierarchies:
        >         if item.name == db_name:
        >             my_exp = item.explanation
        >             my_sec = item.section.name
        >             my_subsec = item.subsection.name
        >             myvar = variable_name
        >             break
        >         else:
        >             my_exp = NO_DATA.explanation
        >             my_sec = NO_DATA.section
        >             my_subsec = NO_DATA.subsection
        >             myvar = variable_name
        >
        >     context = dict(
        >         context,
        >         **{
        >             "mysubsection": my_subsec,
        >             "myvar": myvar,
        >             "my_exp": my_exp,
        >         },
        >     )
        >
        >     return context
    """
    try:
        variable_hierarchy = Variablehierarchy.objects.get(name=db_name)
    except Variablehierarchy.DoesNotExist:
        variable_hierarchy = None

    if variable_hierarchy:
        context = dict(context, **{
            "mysubsection": variable_hierarchy.subsection.name,
            "myvar": variable_hierarchy.name,
            "my_exp": variable_hierarchy.explanation,
        })
    else:
        context = dict(context, **{
            "mysubsection": NO_DATA.subsection,
            "myvar": variable_name,
            "my_exp": NO_DATA.explanation,
        })

    return context
