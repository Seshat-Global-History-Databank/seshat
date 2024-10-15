from django.db import models
from django.db.models import Q


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


class MixinQuerySet(models.QuerySet):
    def for_polity(self, polity, other_polity=None):
        """
        Searches the queryset for a search term.

        Args:
            search_term (str): The search term.
            order_by (str): The field to order the queryset by.
            limit (int): The number of objects to return.
            limited_search (bool): Whether to limit the search to the name field.

        """
        # Define the default filter
        _filter = Q(polity=polity)

        # Add other polity filter
        if other_polity:
            if hasattr(self.model, "other_polity"):
                _filter = _filter | Q(other_polity=other_polity)
            else:
                raise ValueError(f"Model {self.model.__name__} does not have other_polity attribute.")  # noqa: E501

        # Filter the queryset
        objects = self.filter(_filter)

        # Return the queryset
        return objects
