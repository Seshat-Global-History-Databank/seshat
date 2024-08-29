from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from datetime import date

from ..core.models import SeshatCommon
from ..accounts.models import Seshat_Expert


ABSENT_PRESENT_CHOICES = (
    ("present", "present"),
    ("absent", "absent"),
    ("unknown", "unknown"),
    ("A~P", "Transitional (Absent -> Present)"),
    ("P~A", "Transitional (Present -> Absent)"),
)

SOURCE_OF_SUPPORT_CHOICES = (
    ("state salary", "state salary"),
    ("pensions", "pensions"),
    ("enoblement", "enoblement"),
    ("suspected unknown", "suspected unknown"),
    ("unknown", "unknown"),
    ("land", "land"),
    ("absent", "absent"),
    ("cash", "cash"),
    ("salary", "salary"),
    ("state", "state"),
    ("governed population", "governed population"),
    ("none", "none"),
    ("cattle", "cattle"),
)


def call_my_name(self):
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
    if self.year_from == self.year_to or ((not self.year_to) and self.year_from):
        return (
            self.name + " [for " + self.polity.name + " in " + str(self.year_from) + "]"
        )
    else:
        return (
            self.name
            + " [for "
            + self.polity.name
            + " from "
            + str(self.year_from)
            + " to "
            + str(self.year_to)
            + "]"
        )


def return_citations(self):
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
        self (model instance): The model instance.

    Returns:
        str: The citations of the model instance, separated by comma.
    """
    return ", ".join(
        [
            '<a href="' + citation.zoteroer() + '">' + citation.__str__() + " </a>"
            for citation in self.citations.all()[:2]
        ]
    )


def clean_times(self):
    """
    This function is used to validate the year_from and year_to fields of the
    model instance (called from each model's clean method).

    Note:
        The model instance must have the following attributes:
        - year_from
        - year_to
        - polity (and polity.start_year and polity.end_year)

    Args:
        self (model instance): The model instance.

    Returns:
        None

    Raises:
        ValidationError: If the year_from is greater than the year_to.
        ValidationError: If the year_from is out of range.
        ValidationError: If the year_from is earlier than the start year of the corresponding polity.
        ValidationError: If the year_to is later than the end year of the corresponding polity.
        ValidationError: If the year_to is out of range.
    """
    if (self.year_from and self.year_to) and self.year_from > self.year_to:
        raise ValidationError(
            {
                "year_from": mark_safe(
                    '<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i> The start year is bigger than the end year!</span>'
                ),
            }
        )
    if self.year_from and (self.year_from > date.today().year):
        raise ValidationError(
            {
                "year_from": mark_safe(
                    '<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i> The start year is out of range!</span>'
                ),
            }
        )
    if self.year_from and (self.year_from < self.polity.start_year):
        raise ValidationError(
            {
                "year_from": mark_safe(
                    '<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i> The start year is earlier than the start year of the corresponding polity!</span>'
                ),
            }
        )
    if self.year_to and (self.year_to > self.polity.end_year):
        raise ValidationError(
            {
                "year_to": mark_safe(
                    '<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i>The end year is later than the end year of the corresponding polity!</span>'
                ),
            }
        )
    if self.year_to and (self.year_to > date.today().year):
        raise ValidationError(
            {
                "year_to": mark_safe(
                    '<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i>The end year is out of range!</span>'
                ),
            }
        )


class Ra(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Ra")
    sc_ra = models.ForeignKey(
        Seshat_Expert,
        on_delete=models.SET_NULL,
        null=True,
        related_name="sc_research_assistant",
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Ra"
        verbose_name_plural = "Ras"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "ra"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "ra"

    def show_value(self):
        if self.sc_ra:
            return self.sc_ra
        else:
            return " - "

    def show_value_from(self):
        if self.sc_ra:
            return self.sc_ra
        else:
            return None

    def show_value_to(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("ra-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Polity_territory(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Polity_territory")
    polity_territory_from = models.IntegerField(blank=True, null=True)
    polity_territory_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_territory"
        verbose_name_plural = "Polity_territories"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "polity_territory"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Territory"

    def show_value(self):
        if (
            self.polity_territory_from is not None
            and self.polity_territory_to is not None
            and self.polity_territory_to == self.polity_territory_from
        ):
            return mark_safe(
                f"{self.polity_territory_from:,} <span class='fw-light fs-6 text-secondary'> km<sup>2</sup> </span>"
            )
        elif (
            self.polity_territory_from is not None
            and self.polity_territory_to is not None
        ):
            return mark_safe(
                f"<span class='fw-light text-secondary'> [</span>{self.polity_territory_from:,} <span class='fw-light text-secondary'> to </span> {self.polity_territory_to:,}<span class='fw-light text-secondary'>] </span> <span class='fw-light fs-6 text-secondary'> km<sup>2</sup> </span>"
            )
        elif self.polity_territory_from is not None:
            return f"[{self.polity_territory_from:,}, ...]"
        elif self.polity_territory_to is not None:
            return f"[..., {self.polity_territory_to:,}]"
        else:
            return " - "

    def show_value_from(self):
        if self.polity_territory_from is not None:
            return self.polity_territory_from
        else:
            return "unknown"

    def show_value_to(self):
        if self.polity_territory_to is not None:
            return self.polity_territory_to
        else:
            return None

    def subsection(self):
        return "Social Scale"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("polity_territory-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Polity_population(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Polity_population")
    polity_population_from = models.IntegerField(blank=True, null=True)
    polity_population_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_population"
        verbose_name_plural = "Polity_populations"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "polity_population"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Population"

    def show_value(self):
        if (
            self.polity_population_from is not None
            and self.polity_population_to is not None
            and self.polity_population_to == self.polity_population_from
        ):
            return mark_safe(
                f"{self.polity_population_from:,}<span class='fw-light fs-6 text-secondary'> people </span>"
            )
        elif (
            self.polity_population_from is not None
            and self.polity_population_to is not None
        ):
            return mark_safe(
                f"<span class='fw-light text-secondary'> [</span>{self.polity_population_from:,} <span class='fw-light text-secondary'> to </span> {self.polity_population_to:,}<span class='fw-light text-secondary'>] </span> <span class='fw-light fs-6 text-secondary'> people </span>"
            )
        elif self.polity_population_from is not None:
            return f"[{self.polity_population_from:,}, ...]"
        elif self.polity_population_to is not None:
            return f"[..., {self.polity_population_to:,}]"
        else:
            return " - "

    def show_value_from(self):
        if self.polity_population_from is not None:
            return self.polity_population_from
        else:
            return "unknown"

    def show_value_to(self):
        if self.polity_population_to is not None:
            return self.polity_population_to
        else:
            return None

    def subsection(self):
        return "Social Scale"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("polity_population-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Population_of_the_largest_settlement(SeshatCommon):
    """ """

    name = models.CharField(
        max_length=100, default="Population_of_the_largest_settlement"
    )
    population_of_the_largest_settlement_from = models.IntegerField(
        blank=True, null=True
    )
    population_of_the_largest_settlement_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Population_of_the_largest_settlement"
        verbose_name_plural = "Population_of_the_largest_settlements"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "population_of_the_largest_settlement"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Population of the Largest Settlement"

    def show_value(self):
        if (
            self.population_of_the_largest_settlement_from is not None
            and self.population_of_the_largest_settlement_to is not None
            and self.population_of_the_largest_settlement_to
            == self.population_of_the_largest_settlement_from
        ):
            return mark_safe(
                f"{self.population_of_the_largest_settlement_from:,} <span class='fw-light fs-6 text-secondary'> people </span>"
            )
        elif (
            self.population_of_the_largest_settlement_from is not None
            and self.population_of_the_largest_settlement_to is not None
        ):
            return mark_safe(
                f"<span class='fw-light text-secondary'> [</span>{self.population_of_the_largest_settlement_from:,} <span class='fw-light text-secondary'> to </span> {self.population_of_the_largest_settlement_to:,}<span class='fw-light text-secondary'>] </span> <span class='fw-light fs-6 text-secondary'> people </span>"
            )
        elif self.population_of_the_largest_settlement_from is not None:
            return f"[{self.population_of_the_largest_settlement_from:,}, ...]"
        elif self.population_of_the_largest_settlement_to is not None:
            return f"[..., {self.population_of_the_largest_settlement_to:,}]"
        else:
            return " - "

    def show_value_from(self):
        if self.population_of_the_largest_settlement_from is not None:
            return self.population_of_the_largest_settlement_from
        else:
            return "unknown"

    def show_value_to(self):
        if self.population_of_the_largest_settlement_to is not None:
            return self.population_of_the_largest_settlement_to
        else:
            return None

    def subsection(self):
        return "Social Scale"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse(
            "population_of_the_largest_settlement-detail", args=[str(self.id)]
        )

    def __str__(self) -> str:
        return call_my_name(self)


class Settlement_hierarchy(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Settlement_hierarchy")
    settlement_hierarchy_from = models.IntegerField(blank=True, null=True)
    settlement_hierarchy_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Settlement_hierarchy"
        verbose_name_plural = "Settlement_hierarchies"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "settlement_hierarchy"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Settlement Hierarchy"

    def show_value(self):
        if (
            self.settlement_hierarchy_from is not None
            and self.settlement_hierarchy_to is not None
            and self.settlement_hierarchy_to == self.settlement_hierarchy_from
        ):
            return self.settlement_hierarchy_from
        elif (
            self.settlement_hierarchy_from is not None
            and self.settlement_hierarchy_to is not None
        ):
            return f"[{self.settlement_hierarchy_from:,} to {self.settlement_hierarchy_to:,}]"
        elif self.settlement_hierarchy_from is not None:
            return f"[{self.settlement_hierarchy_from:,}, ...]"
        elif self.settlement_hierarchy_to is not None:
            return f"[..., {self.settlement_hierarchy_to:,}]"
        else:
            return " - "

    def show_value_from(self):
        if self.settlement_hierarchy_from is not None:
            return self.settlement_hierarchy_from
        else:
            return "unknown"

    def show_value_to(self):
        if self.settlement_hierarchy_to is not None:
            return self.settlement_hierarchy_to
        else:
            return None

    def subsection(self):
        return "Hierarchical Complexity"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("settlement_hierarchy-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Administrative_level(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Administrative_level")
    administrative_level_from = models.IntegerField(blank=True, null=True)
    administrative_level_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Administrative_level"
        verbose_name_plural = "Administrative_levels"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "administrative_level"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Administrative Level"

    def show_value(self):
        if (
            self.administrative_level_from is not None
            and self.administrative_level_to is not None
            and self.administrative_level_to == self.administrative_level_from
        ):
            return self.administrative_level_from
        elif (
            self.administrative_level_from is not None
            and self.administrative_level_to is not None
        ):
            return f"[{self.administrative_level_from:,} to {self.administrative_level_to:,}]"
        elif self.administrative_level_from is not None:
            return f"[{self.administrative_level_from:,}, ...]"
        elif self.administrative_level_to is not None:
            return f"[..., {self.administrative_level_to:,}]"
        else:
            return " - "

    def show_value_from(self):
        if self.administrative_level_from is not None:
            return self.administrative_level_from
        else:
            return "unknown"

    def show_value_to(self):
        if self.administrative_level_to is not None:
            return self.administrative_level_to
        else:
            return None

    def subsection(self):
        return "Hierarchical Complexity"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("administrative_level-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Religious_level(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Religious_level")
    religious_level_from = models.IntegerField(blank=True, null=True)
    religious_level_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Religious_level"
        verbose_name_plural = "Religious_levels"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "religious_level"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Religious Level"

    def show_value(self):
        if (
            self.religious_level_from is not None
            and self.religious_level_to is not None
            and self.religious_level_to == self.religious_level_from
        ):
            return self.religious_level_from
        elif (
            self.religious_level_from is not None
            and self.religious_level_to is not None
        ):
            return f"[{self.religious_level_from:,} to {self.religious_level_to:,}]"
        elif self.religious_level_from is not None:
            return f"[{self.religious_level_from:,}, ...]"
        elif self.religious_level_to is not None:
            return f"[..., {self.religious_level_to:,}]"
        else:
            return " - "

    def show_value_from(self):
        if self.religious_level_from is not None:
            return self.religious_level_from
        else:
            return "unknown"

    def show_value_to(self):
        if self.religious_level_to is not None:
            return self.religious_level_to
        else:
            return None

    def subsection(self):
        return "Hierarchical Complexity"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("religious_level-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Military_level(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Military_level")
    military_level_from = models.IntegerField(blank=True, null=True)
    military_level_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Military_level"
        verbose_name_plural = "Military_levels"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "military_level"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Military Level"

    def show_value(self):
        if (
            self.military_level_from is not None
            and self.military_level_to is not None
            and self.military_level_to == self.military_level_from
        ):
            return self.military_level_from
        elif (
            self.military_level_from is not None and self.military_level_to is not None
        ):
            return f"[{self.military_level_from:,} to {self.military_level_to:,}]"
        elif self.military_level_from is not None:
            return f"[{self.military_level_from:,}, ...]"
        elif self.military_level_to is not None:
            return f"[..., {self.military_level_to:,}]"
        else:
            return " - "

    def show_value_from(self):
        if self.military_level_from is not None:
            return self.military_level_from
        else:
            return "unknown"

    def show_value_to(self):
        if self.military_level_to is not None:
            return self.military_level_to
        else:
            return None

    def subsection(self):
        return "Hierarchical Complexity"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("military_level-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Professional_military_officer(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Professional_military_officer")
    professional_military_officer = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Professional_military_officer"
        verbose_name_plural = "Professional_military_officers"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "professional_military_officer"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Professional Military Officer"

    def show_value(self):
        if self.professional_military_officer:
            return self.get_professional_military_officer_display()
        else:
            return " - "

    def show_value_from(self):
        if self.professional_military_officer:
            return self.professional_military_officer
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Professions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("professional_military_officer-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Professional_soldier(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Professional_soldier")
    professional_soldier = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Professional_soldier"
        verbose_name_plural = "Professional_soldiers"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "professional_soldier"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Professional Soldier"

    def show_value(self):
        if self.professional_soldier:
            return self.get_professional_soldier_display()
        else:
            return " - "

    def show_value_from(self):
        if self.professional_soldier:
            return self.professional_soldier
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Professions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("professional_soldier-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Professional_priesthood(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Professional_priesthood")
    professional_priesthood = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Professional_priesthood"
        verbose_name_plural = "Professional_priesthoods"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "professional_priesthood"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Professional Priesthood"

    def show_value(self):
        if self.professional_priesthood:
            return self.get_professional_priesthood_display()
        else:
            return " - "

    def show_value_from(self):
        if self.professional_priesthood:
            return self.professional_priesthood
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Professions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("professional_priesthood-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Full_time_bureaucrat(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Full_time_bureaucrat")
    full_time_bureaucrat = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Full_time_bureaucrat"
        verbose_name_plural = "Full_time_bureaucrats"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "full_time_bureaucrat"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Full Time Bureaucrat"

    def show_value(self):
        if self.full_time_bureaucrat:
            return self.get_full_time_bureaucrat_display()
        else:
            return " - "

    def show_value_from(self):
        if self.full_time_bureaucrat:
            return self.full_time_bureaucrat
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Bureaucracy Characteristics"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("full_time_bureaucrat-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Examination_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Examination_system")
    examination_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Examination_system"
        verbose_name_plural = "Examination_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "examination_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Examination System"

    def show_value(self):
        if self.examination_system:
            return self.get_examination_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.examination_system:
            return self.examination_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Bureaucracy Characteristics"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("examination_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Merit_promotion(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Merit_promotion")
    merit_promotion = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Merit_promotion"
        verbose_name_plural = "Merit_promotions"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "merit_promotion"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Merit Promotion"

    def show_value(self):
        if self.merit_promotion:
            return self.get_merit_promotion_display()
        else:
            return " - "

    def show_value_from(self):
        if self.merit_promotion:
            return self.merit_promotion
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Bureaucracy Characteristics"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("merit_promotion-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Specialized_government_building(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Specialized_government_building")
    specialized_government_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Specialized_government_building"
        verbose_name_plural = "Specialized_government_buildings"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "specialized_government_building"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Specialized Government Building"

    def show_value(self):
        if self.specialized_government_building:
            return self.get_specialized_government_building_display()
        else:
            return " - "

    def show_value_from(self):
        if self.specialized_government_building:
            return self.specialized_government_building
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Bureaucracy Characteristics"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("specialized_government_building-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Formal_legal_code(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Formal_legal_code")
    formal_legal_code = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Formal_legal_code"
        verbose_name_plural = "Formal_legal_codes"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "formal_legal_code"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Formal Legal Code"

    def show_value(self):
        if self.formal_legal_code:
            return self.get_formal_legal_code_display()
        else:
            return " - "

    def show_value_from(self):
        if self.formal_legal_code:
            return self.formal_legal_code
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Law"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("formal_legal_code-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Judge(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Judge")
    judge = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Judge"
        verbose_name_plural = "Judges"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "judge"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Judge"

    def show_value(self):
        if self.judge:
            return self.get_judge_display()
        else:
            return " - "

    def show_value_from(self):
        if self.judge:
            return self.judge
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Law"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("judge-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Court(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Court")
    court = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Court"
        verbose_name_plural = "Courts"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "court"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Court"

    def show_value(self):
        if self.court:
            return self.get_court_display()
        else:
            return " - "

    def show_value_from(self):
        if self.court:
            return self.court
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Law"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("court-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Professional_lawyer(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Professional_lawyer")
    professional_lawyer = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Professional_lawyer"
        verbose_name_plural = "Professional_lawyers"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "professional_lawyer"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Professional Lawyer"

    def show_value(self):
        if self.professional_lawyer:
            return self.get_professional_lawyer_display()
        else:
            return " - "

    def show_value_from(self):
        if self.professional_lawyer:
            return self.professional_lawyer
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Law"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("professional_lawyer-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Irrigation_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Irrigation_system")
    irrigation_system = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Irrigation_system"
        verbose_name_plural = "Irrigation_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "irrigation_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Irrigation System"

    def show_value(self):
        if self.irrigation_system:
            return self.get_irrigation_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.irrigation_system:
            return self.irrigation_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("irrigation_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Drinking_water_supply_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Drinking_water_supply_system")
    drinking_water_supply_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Drinking_water_supply_system"
        verbose_name_plural = "Drinking_water_supply_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "drinking_water_supply_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Drinking Water Supply System"

    def show_value(self):
        if self.drinking_water_supply_system:
            return self.get_drinking_water_supply_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.drinking_water_supply_system:
            return self.drinking_water_supply_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("drinking_water_supply_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Market(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Market")
    market = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Market"
        verbose_name_plural = "Markets"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "market"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Market"

    def show_value(self):
        if self.market:
            return self.get_market_display()
        else:
            return " - "

    def show_value_from(self):
        if self.market:
            return self.market
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("market-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Food_storage_site(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Food_storage_site")
    food_storage_site = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Food_storage_site"
        verbose_name_plural = "Food_storage_sites"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "food_storage_site"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Food Storage Site"

    def show_value(self):
        if self.food_storage_site:
            return self.get_food_storage_site_display()
        else:
            return " - "

    def show_value_from(self):
        if self.food_storage_site:
            return self.food_storage_site
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("food_storage_site-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Road(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Road")
    road = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Road"
        verbose_name_plural = "Roads"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "road"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Road"

    def show_value(self):
        if self.road:
            return self.get_road_display()
        else:
            return " - "

    def show_value_from(self):
        if self.road:
            return self.road
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Transport Infrastructure"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("road-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Bridge(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Bridge")
    bridge = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Bridge"
        verbose_name_plural = "Bridges"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "bridge"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Bridge"

    def show_value(self):
        if self.bridge:
            return self.get_bridge_display()
        else:
            return " - "

    def show_value_from(self):
        if self.bridge:
            return self.bridge
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Transport Infrastructure"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("bridge-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Canal(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Canal")
    canal = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Canal"
        verbose_name_plural = "Canals"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "canal"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Canal"

    def show_value(self):
        if self.canal:
            return self.get_canal_display()
        else:
            return " - "

    def show_value_from(self):
        if self.canal:
            return self.canal
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Transport Infrastructure"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("canal-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Port(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Port")
    port = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Port"
        verbose_name_plural = "Ports"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "port"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Port"

    def show_value(self):
        if self.port:
            return self.get_port_display()
        else:
            return " - "

    def show_value_from(self):
        if self.port:
            return self.port
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Transport Infrastructure"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("port-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Mines_or_quarry(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Mines_or_quarry")
    mines_or_quarry = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Mines_or_quarry"
        verbose_name_plural = "Mines_or_quarries"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "mines_or_quarry"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Mines or Quarry"

    def show_value(self):
        if self.mines_or_quarry:
            return self.get_mines_or_quarry_display()
        else:
            return " - "

    def show_value_from(self):
        if self.mines_or_quarry:
            return self.mines_or_quarry
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Special-purpose Sites"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("mines_or_quarry-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Mnemonic_device(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Mnemonic_device")
    mnemonic_device = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Mnemonic_device"
        verbose_name_plural = "Mnemonic_devices"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "mnemonic_device"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Mnemonic Device"

    def show_value(self):
        if self.mnemonic_device:
            return self.get_mnemonic_device_display()
        else:
            return " - "

    def show_value_from(self):
        if self.mnemonic_device:
            return self.mnemonic_device
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Writing System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("mnemonic_device-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Nonwritten_record(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Nonwritten_record")
    nonwritten_record = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Nonwritten_record"
        verbose_name_plural = "Nonwritten_records"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "nonwritten_record"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Nonwritten Record"

    def show_value(self):
        if self.nonwritten_record:
            return self.get_nonwritten_record_display()
        else:
            return " - "

    def show_value_from(self):
        if self.nonwritten_record:
            return self.nonwritten_record
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Writing System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("nonwritten_record-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Written_record(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Written_record")
    written_record = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Written_record"
        verbose_name_plural = "Written_records"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "written_record"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Written Record"

    def show_value(self):
        if self.written_record:
            return self.get_written_record_display()
        else:
            return " - "

    def show_value_from(self):
        if self.written_record:
            return self.written_record
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Writing System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("written_record-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Script(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Script")
    script = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Script"
        verbose_name_plural = "Scripts"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "script"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Script"

    def show_value(self):
        if self.script:
            return self.get_script_display()
        else:
            return " - "

    def show_value_from(self):
        if self.script:
            return self.script
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Writing System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("script-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Non_phonetic_writing(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Non_phonetic_writing")
    non_phonetic_writing = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Non_phonetic_writing"
        verbose_name_plural = "Non_phonetic_writings"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "non_phonetic_writing"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Non Phonetic Writing"

    def show_value(self):
        if self.non_phonetic_writing:
            return self.get_non_phonetic_writing_display()
        else:
            return " - "

    def show_value_from(self):
        if self.non_phonetic_writing:
            return self.non_phonetic_writing
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Writing System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("non_phonetic_writing-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Phonetic_alphabetic_writing(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Phonetic_alphabetic_writing")
    phonetic_alphabetic_writing = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Phonetic_alphabetic_writing"
        verbose_name_plural = "Phonetic_alphabetic_writings"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "phonetic_alphabetic_writing"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Phonetic Alphabetic Writing"

    def show_value(self):
        if self.phonetic_alphabetic_writing:
            return self.get_phonetic_alphabetic_writing_display()
        else:
            return " - "

    def show_value_from(self):
        if self.phonetic_alphabetic_writing:
            return self.phonetic_alphabetic_writing
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Writing System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("phonetic_alphabetic_writing-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Lists_tables_and_classification(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Lists_tables_and_classification")
    lists_tables_and_classification = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Lists_tables_and_classification"
        verbose_name_plural = "Lists_tables_and_classifications"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "lists_tables_and_classification"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Lists Tables and Classification"

    def show_value(self):
        if self.lists_tables_and_classification:
            return self.get_lists_tables_and_classification_display()
        else:
            return " - "

    def show_value_from(self):
        if self.lists_tables_and_classification:
            return self.lists_tables_and_classification
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Kinds of Written Documents"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("lists_tables_and_classification-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Calendar(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Calendar")
    calendar = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Calendar"
        verbose_name_plural = "Calendars"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "calendar"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Calendar"

    def show_value(self):
        if self.calendar:
            return self.get_calendar_display()
        else:
            return " - "

    def show_value_from(self):
        if self.calendar:
            return self.calendar
        else:
            return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Kinds of Written Documents"

    def show_value_to(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("calendar-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Sacred_text(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Sacred_text")
    sacred_text = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Sacred_text"
        verbose_name_plural = "Sacred_texts"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "sacred_text"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Sacred Text"

    def show_value(self):
        if self.sacred_text:
            return self.get_sacred_text_display()
        else:
            return " - "

    def show_value_from(self):
        if self.sacred_text:
            return self.sacred_text
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Kinds of Written Documents"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("sacred_text-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Religious_literature(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Religious_literature")
    religious_literature = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Religious_literature"
        verbose_name_plural = "Religious_literatures"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "religious_literature"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Religious Literature"

    def show_value(self):
        if self.religious_literature:
            return self.get_religious_literature_display()
        else:
            return " - "

    def show_value_from(self):
        if self.religious_literature:
            return self.religious_literature
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Kinds of Written Documents"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("religious_literature-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Practical_literature(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Practical_literature")
    practical_literature = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Practical_literature"
        verbose_name_plural = "Practical_literatures"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "practical_literature"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Practical Literature"

    def show_value(self):
        if self.practical_literature:
            return self.get_practical_literature_display()
        else:
            return " - "

    def show_value_from(self):
        if self.practical_literature:
            return self.practical_literature
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Kinds of Written Documents"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("practical_literature-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class History(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="History")
    history = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "History"
        verbose_name_plural = "Histories"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "history"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "History"

    def show_value(self):
        if self.history:
            return self.get_history_display()
        else:
            return " - "

    def show_value_from(self):
        if self.history:
            return self.history
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Kinds of Written Documents"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("history-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Philosophy(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Philosophy")
    philosophy = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Philosophy"
        verbose_name_plural = "Philosophies"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "philosophy"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Philosophy"

    def show_value(self):
        if self.philosophy:
            return self.get_philosophy_display()
        else:
            return " - "

    def show_value_from(self):
        if self.philosophy:
            return self.philosophy
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Kinds of Written Documents"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("philosophy-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Scientific_literature(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Scientific_literature")
    scientific_literature = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Scientific_literature"
        verbose_name_plural = "Scientific_literatures"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "scientific_literature"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Scientific Literature"

    def show_value(self):
        if self.scientific_literature:
            return self.get_scientific_literature_display()
        else:
            return " - "

    def show_value_from(self):
        if self.scientific_literature:
            return self.scientific_literature
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Kinds of Written Documents"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("scientific_literature-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Fiction(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Fiction")
    fiction = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Fiction"
        verbose_name_plural = "Fictions"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "fiction"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Fiction"

    def show_value(self):
        if self.fiction:
            return self.get_fiction_display()
        else:
            return " - "

    def show_value_from(self):
        if self.fiction:
            return self.fiction
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Kinds of Written Documents"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("fiction-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Article(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Article")
    article = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "article"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Article"

    def show_value(self):
        if self.article:
            return self.get_article_display()
        else:
            return " - "

    def show_value_from(self):
        if self.article:
            return self.article
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Money"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("article-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Token(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Token")
    token = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Token"
        verbose_name_plural = "Tokens"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "token"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Token"

    def show_value(self):
        if self.token:
            return self.get_token_display()
        else:
            return " - "

    def show_value_from(self):
        if self.token:
            return self.token
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Money"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("token-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Precious_metal(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Precious_metal")
    precious_metal = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Precious_metal"
        verbose_name_plural = "Precious_metals"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "precious_metal"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Precious Metal"

    def show_value(self):
        if self.precious_metal:
            return self.get_precious_metal_display()
        else:
            return " - "

    def show_value_from(self):
        if self.precious_metal:
            return self.precious_metal
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Money"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("precious_metal-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Foreign_coin(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Foreign_coin")
    foreign_coin = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Foreign_coin"
        verbose_name_plural = "Foreign_coins"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "foreign_coin"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Foreign Coin"

    def show_value(self):
        if self.foreign_coin:
            return self.get_foreign_coin_display()
        else:
            return " - "

    def show_value_from(self):
        if self.foreign_coin:
            return self.foreign_coin
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Money"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("foreign_coin-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Indigenous_coin(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Indigenous_coin")
    indigenous_coin = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Indigenous_coin"
        verbose_name_plural = "Indigenous_coins"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "indigenous_coin"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Indigenous Coin"

    def show_value(self):
        if self.indigenous_coin:
            return self.get_indigenous_coin_display()
        else:
            return " - "

    def show_value_from(self):
        if self.indigenous_coin:
            return self.indigenous_coin
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Money"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("indigenous_coin-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Paper_currency(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Paper_currency")
    paper_currency = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Paper_currency"
        verbose_name_plural = "Paper_currencies"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "paper_currency"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Paper Currency"

    def show_value(self):
        if self.paper_currency:
            return self.get_paper_currency_display()
        else:
            return " - "

    def show_value_from(self):
        if self.paper_currency:
            return self.paper_currency
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Money"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("paper_currency-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Courier(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Courier")
    courier = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Courier"
        verbose_name_plural = "Couriers"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "courier"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Courier"

    def show_value(self):
        if self.courier:
            return self.get_courier_display()
        else:
            return " - "

    def show_value_from(self):
        if self.courier:
            return self.courier
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Postal System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("courier-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Postal_station(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Postal_station")
    postal_station = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Postal_station"
        verbose_name_plural = "Postal_stations"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "postal_station"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Postal Station"

    def show_value(self):
        if self.postal_station:
            return self.get_postal_station_display()
        else:
            return " - "

    def show_value_from(self):
        if self.postal_station:
            return self.postal_station
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Postal System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("postal_station-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class General_postal_service(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="General_postal_service")
    general_postal_service = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "General_postal_service"
        verbose_name_plural = "General_postal_services"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "general_postal_service"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "General Postal Service"

    def show_value(self):
        if self.general_postal_service:
            return self.get_general_postal_service_display()
        else:
            return " - "

    def show_value_from(self):
        if self.general_postal_service:
            return self.general_postal_service
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Postal System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("general_postal_service-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Communal_building(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Communal_building")
    communal_building = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Communal_building"
        verbose_name_plural = "Communal_buildings"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "communal_building"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Communal Building"

    def show_value(self):
        if self.communal_building:
            return self.get_communal_building_display()
        else:
            return " - "

    def show_value_from(self):
        if self.communal_building:
            return self.communal_building
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("communal_building-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Utilitarian_public_building(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Utilitarian_public_building")
    utilitarian_public_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Utilitarian_public_building"
        verbose_name_plural = "Utilitarian_public_buildings"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "utilitarian_public_building"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Utilitarian Public Building"

    def show_value(self):
        if self.utilitarian_public_building:
            return self.get_utilitarian_public_building_display()
        else:
            return " - "

    def show_value_from(self):
        if self.utilitarian_public_building:
            return self.utilitarian_public_building
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("utilitarian_public_building-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Symbolic_building(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Symbolic_building")
    symbolic_building = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Symbolic_building"
        verbose_name_plural = "Symbolic_buildings"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "symbolic_building"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Symbolic Building"

    def show_value(self):
        if self.symbolic_building:
            return self.get_symbolic_building_display()
        else:
            return " - "

    def show_value_from(self):
        if self.symbolic_building:
            return self.symbolic_building
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("symbolic_building-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Entertainment_building(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Entertainment_building")
    entertainment_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Entertainment_building"
        verbose_name_plural = "Entertainment_buildings"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "entertainment_building"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Entertainment Building"

    def show_value(self):
        if self.entertainment_building:
            return self.get_entertainment_building_display()
        else:
            return " - "

    def show_value_from(self):
        if self.entertainment_building:
            return self.entertainment_building
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("entertainment_building-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Knowledge_or_information_building(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Knowledge_or_information_building")
    knowledge_or_information_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Knowledge_or_information_building"
        verbose_name_plural = "Knowledge_or_information_buildings"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "knowledge_or_information_building"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Knowledge Or Information Building"

    def show_value(self):
        if self.knowledge_or_information_building:
            return self.get_knowledge_or_information_building_display()
        else:
            return " - "

    def show_value_from(self):
        if self.knowledge_or_information_building:
            return self.knowledge_or_information_building
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("knowledge_or_information_building-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Other_utilitarian_public_building(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Other_utilitarian_public_building")
    other_utilitarian_public_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Other_utilitarian_public_building"
        verbose_name_plural = "Other_utilitarian_public_buildings"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "other_utilitarian_public_building"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Other Utilitarian Public Building"

    def show_value(self):
        if self.other_utilitarian_public_building:
            return self.get_other_utilitarian_public_building_display()
        else:
            return " - "

    def show_value_from(self):
        if self.other_utilitarian_public_building:
            return self.other_utilitarian_public_building
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("other_utilitarian_public_building-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Special_purpose_site(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Special_purpose_site")
    special_purpose_site = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Special_purpose_site"
        verbose_name_plural = "Special_purpose_sites"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "special_purpose_site"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Special Purpose Site"

    def show_value(self):
        if self.special_purpose_site:
            return self.get_special_purpose_site_display()
        else:
            return " - "

    def show_value_from(self):
        if self.special_purpose_site:
            return self.special_purpose_site
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Special-purpose Sites"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("special_purpose_site-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Ceremonial_site(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Ceremonial_site")
    ceremonial_site = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Ceremonial_site"
        verbose_name_plural = "Ceremonial_sites"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "ceremonial_site"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Ceremonial Site"

    def show_value(self):
        if self.ceremonial_site:
            return self.get_ceremonial_site_display()
        else:
            return " - "

    def show_value_from(self):
        if self.ceremonial_site:
            return self.ceremonial_site
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Special-purpose Sites"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("ceremonial_site-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Burial_site(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Burial_site")
    burial_site = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Burial_site"
        verbose_name_plural = "Burial_sites"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "burial_site"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Burial Site"

    def show_value(self):
        if self.burial_site:
            return self.get_burial_site_display()
        else:
            return " - "

    def show_value_from(self):
        if self.burial_site:
            return self.burial_site
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Special-purpose Sites"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("burial_site-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Trading_emporia(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Trading_emporia")
    trading_emporia = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Trading_emporia"
        verbose_name_plural = "Trading_emporias"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "trading_emporia"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Trading Emporia"

    def show_value(self):
        if self.trading_emporia:
            return self.get_trading_emporia_display()
        else:
            return " - "

    def show_value_from(self):
        if self.trading_emporia:
            return self.trading_emporia
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Special-purpose Sites"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("trading_emporia-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Enclosure(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Enclosure")
    enclosure = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Enclosure"
        verbose_name_plural = "Enclosures"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "enclosure"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Enclosure"

    def show_value(self):
        if self.enclosure:
            return self.get_enclosure_display()
        else:
            return " - "

    def show_value_from(self):
        if self.enclosure:
            return self.enclosure
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Special-purpose Sites"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("enclosure-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Length_measurement_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Length_measurement_system")
    length_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Length_measurement_system"
        verbose_name_plural = "Length_measurement_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "length_measurement_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Length Measurement System"

    def show_value(self):
        if self.length_measurement_system:
            return self.get_length_measurement_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.length_measurement_system:
            return self.length_measurement_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Measurement System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("length_measurement_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Area_measurement_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Area_measurement_system")
    area_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Area_measurement_system"
        verbose_name_plural = "Area_measurement_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "area_measurement_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Area Measurement System"

    def show_value(self):
        if self.area_measurement_system:
            return self.get_area_measurement_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.area_measurement_system:
            return self.area_measurement_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Measurement System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("area_measurement_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Volume_measurement_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Volume_measurement_system")
    volume_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Volume_measurement_system"
        verbose_name_plural = "Volume_measurement_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "volume_measurement_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Volume Measurement System"

    def show_value(self):
        if self.volume_measurement_system:
            return self.get_volume_measurement_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.volume_measurement_system:
            return self.volume_measurement_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Measurement System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("volume_measurement_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Weight_measurement_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Weight_measurement_system")
    weight_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Weight_measurement_system"
        verbose_name_plural = "Weight_measurement_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "weight_measurement_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Weight Measurement System"

    def show_value(self):
        if self.weight_measurement_system:
            return self.get_weight_measurement_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.weight_measurement_system:
            return self.weight_measurement_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Measurement System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("weight_measurement_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Time_measurement_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Time_measurement_system")
    time_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Time_measurement_system"
        verbose_name_plural = "Time_measurement_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "time_measurement_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Time Measurement System"

    def show_value(self):
        if self.time_measurement_system:
            return self.get_time_measurement_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.time_measurement_system:
            return self.time_measurement_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Measurement System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("time_measurement_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Geometrical_measurement_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Geometrical_measurement_system")
    geometrical_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Geometrical_measurement_system"
        verbose_name_plural = "Geometrical_measurement_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "geometrical_measurement_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Geometrical Measurement System"

    def show_value(self):
        if self.geometrical_measurement_system:
            return self.get_geometrical_measurement_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.geometrical_measurement_system:
            return self.geometrical_measurement_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Measurement System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("geometrical_measurement_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Other_measurement_system(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Other_measurement_system")
    other_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Other_measurement_system"
        verbose_name_plural = "Other_measurement_systems"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "other_measurement_system"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Other Measurement System"

    def show_value(self):
        if self.other_measurement_system:
            return self.get_other_measurement_system_display()
        else:
            return " - "

    def show_value_from(self):
        if self.other_measurement_system:
            return self.other_measurement_system
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Measurement System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("other_measurement_system-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Debt_and_credit_structure(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Debt_and_credit_structure")
    debt_and_credit_structure = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Debt_and_credit_structure"
        verbose_name_plural = "Debt_and_credit_structures"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "debt_and_credit_structure"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Debt And Credit Structure"

    def show_value(self):
        if self.debt_and_credit_structure:
            return self.get_debt_and_credit_structure_display()
        else:
            return " - "

    def show_value_from(self):
        if self.debt_and_credit_structure:
            return self.debt_and_credit_structure
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Money"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("debt_and_credit_structure-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Store_of_wealth(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Store_of_wealth")
    store_of_wealth = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Store_of_wealth"
        verbose_name_plural = "Store_of_wealths"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "store_of_wealth"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Store Of Wealth"

    def show_value(self):
        if self.store_of_wealth:
            return self.get_store_of_wealth_display()
        else:
            return " - "

    def show_value_from(self):
        if self.store_of_wealth:
            return self.store_of_wealth
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Money"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("store_of_wealth-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Source_of_support(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Source_of_support")
    source_of_support = models.CharField(
        max_length=500, choices=SOURCE_OF_SUPPORT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Source_of_support"
        verbose_name_plural = "Source_of_supports"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "source_of_support"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Source Of Support"

    def show_value(self):
        if self.source_of_support:
            return self.get_source_of_support_display()
        else:
            return " - "

    def show_value_from(self):
        if self.source_of_support:
            return self.source_of_support
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Professions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("source_of_support-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Occupational_complexity(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Occupational_complexity")
    occupational_complexity = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Occupational_complexity"
        verbose_name_plural = "Occupational_complexies"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "occupational_complexity"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Occupational Complexity"

    def show_value(self):
        if self.occupational_complexity:
            return self.get_occupational_complexity_display()
        else:
            return " - "

    def show_value_from(self):
        if self.occupational_complexity:
            return self.occupational_complexity
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Professions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("occupational_complexity-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Special_purpose_house(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Special_purpose_house")
    special_purpose_house = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Special_purpose_house"
        verbose_name_plural = "Special Purpose Houses"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "special_purpose_house"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Special Purpose House"

    def show_value(self):
        if self.special_purpose_house:
            return self.get_special_purpose_house_display()
        else:
            return " - "

    def show_value_from(self):
        if self.special_purpose_house:
            return self.special_purpose_house
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Specialized Buildings: polity owned"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("special_purpose_house-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Other_special_purpose_site(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Other_special_purpose_site")
    other_special_purpose_site = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Other_special_purpose_site"
        verbose_name_plural = "Other Special Purpose Sites"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "other_special_purpose_site"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Other Special Purpose Site"

    def show_value(self):
        if self.other_special_purpose_site:
            return self.get_other_special_purpose_site_display()
        else:
            return " - "

    def show_value_from(self):
        if self.other_special_purpose_site:
            return self.other_special_purpose_site
        else:
            return None

    def show_value_to(self):
        return None

    def subsection(self):
        return "Special-purpose Sites"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("other_special_purpose_site-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Largest_communication_distance(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Largest_communication_distance")
    largest_communication_distance_from = models.IntegerField(null=True, blank=True)
    largest_communication_distance_to = models.IntegerField(null=True, blank=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Largest_communication_distance"
        verbose_name_plural = "Largest Communication Distances"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "largest_communication_distance"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Largest Communication Distance"

    def show_value(self):
        if (
            self.largest_communication_distance_from is not None
            and self.largest_communication_distance_to is not None
            and self.largest_communication_distance_to
            == self.largest_communication_distance_from
        ):
            return self.largest_communication_distance_from
        elif (
            self.largest_communication_distance_from is not None
            and self.largest_communication_distance_to is not None
        ):
            return f"[{self.largest_communication_distance_from:,} to {self.largest_communication_distance_to:,}]"
        elif self.largest_communication_distance_from is not None:
            return f"[{self.largest_communication_distance_from:,}, ...]"
        elif self.largest_communication_distance_to is not None:
            return f"[..., {self.largest_communication_distance_to:,}]"
        else:
            return " - "

    def show_value_from(self):
        if self.largest_communication_distance_from is not None:
            return self.largest_communication_distance_from
        else:
            return "unknown"

    def show_value_to(self):
        if self.largest_communication_distance_to is not None:
            return self.largest_communication_distance_to
        else:
            return None

    def subsection(self):
        return "Social Scale"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("largest_communication_distance-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Fastest_individual_communication(SeshatCommon):
    """ """

    name = models.CharField(max_length=100, default="Fastest_individual_communication")
    fastest_individual_communication_from = models.IntegerField(null=True, blank=True)
    fastest_individual_communication_to = models.IntegerField(null=True, blank=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Fastest_individual_communication"
        verbose_name_plural = "Fastest Individual Communications"
        ordering = ["year_from", "year_to"]

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

    def clean(self):
        clean_times(self)

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
        return "fastest_individual_communication"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Fastest Individual Communication"

    def show_value(self):
        if (
            self.fastest_individual_communication_from is not None
            and self.fastest_individual_communication_to is not None
            and self.fastest_individual_communication_to
            == self.fastest_individual_communication_from
        ):
            return self.fastest_individual_communication_from
        elif (
            self.fastest_individual_communication_from is not None
            and self.fastest_individual_communication_to is not None
        ):
            return f"[{self.fastest_individual_communication_from:,} to {self.fastest_individual_communication_to:,}]"
        elif self.fastest_individual_communication_from is not None:
            return f"[{self.fastest_individual_communication_from:,}, ...]"
        elif self.fastest_individual_communication_to is not None:
            return f"[..., {self.fastest_individual_communication_to:,}]"
        else:
            return " - "

    def show_value_from(self):
        if self.fastest_individual_communication_from is not None:
            return self.fastest_individual_communication_from
        else:
            return "unknown"

    def show_value_to(self):
        if self.fastest_individual_communication_to is not None:
            return self.fastest_individual_communication_to
        else:
            return None

    def subsection(self):
        return "Information"

    def sub_subsection(self):
        return "Postal System"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("fastest_individual_communication-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
