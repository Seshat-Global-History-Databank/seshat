from django.urls import reverse

from ..utils import (
    return_citations,
    validate_time_range,
    get_model_instance_name,
)


class PolityIdMixin:
    """
    Mixin to add the get_initial method to a view that sets the initial value of the polity
    field.
    """

    def get_initial(self):
        """
        Get the initial value of the polity field from the query string.

        Returns:
            dict: The initial value of the polity field.
        """
        initial = super().get_initial()

        polity_id_x = self.request.GET.get("polity_id_x")
        other_polity_id_x = self.request.GET.get("other_polity_id_x")

        if polity_id_x:
            initial["polity"] = polity_id_x

        if other_polity_id_x:
            initial["other_polity"] = other_polity_id_x

        return initial


class GeneralMixIn:
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
        return return_citations(self)

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
            ValidationError: If the year_from is earlier than the start year of the
                corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding
                polity.
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

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return self._clean_name_spaced

    def subsection(self):
        return self._subsection

    def sub_section(self):
        return self._subsection

    def subsubsection(self):
        return self._subsubsection

    def sub_subsection(self):
        return self._subsubsection
