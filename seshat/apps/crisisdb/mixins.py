from django.urls import reverse

from ..global_utils import (
    return_citations,
    validate_time_range,
    get_model_instance_name,
)
from ..global_constants import ICONS


class CrisisDBMixin:
    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        custom_func = lambda citation: f"{ICONS.book} {citation.full_citation_display()}"
        return return_citations(self, custom_func=custom_func)

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse(self._reverse, args=[self.id])

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        validate_time_range(self)

    def __str__(self) -> str:
        return get_model_instance_name(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return self._clean_name
