from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe

from ..core.models import SeshatCommon, Polity
from ..constants import (
    SECTIONS,
    SUBSECTIONS,
    ICONS,
    NO_DATA,
    ATTENTION_TAGS_CHOICES,
    CRISIS_DEFS_EXAMPLES,
    CRISISDB_CHOICES,
    DURATION_DISEASE_OUTBREAK_CHOICES,
    HUMAN_SACRIFICE_HUMAN_SACRIFICE_CHOICES,
    INNER_DURATION_DISEASE_OUTBREAK_CHOICES,
    INNER_MAGNITUDE_DISEASE_OUTBREAK_CHOICES,
    INNER_SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES,
    MAGNITUDE_DISEASE_OUTBREAK_CHOICES,
    POWER_TRANSITIONS_DEFS_EXAMPLES,
    SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES,
    US_STATE_CHOICES,
    VIOLENCE_TYPE_CHOICES,
)
from ..utils import (
    _wrap_in_warning,
    get_model_instance_name,
    validate_time_range,
)

from .mixins import CrisisDBMixin


FIELDS = [
    "decline",
    "collapse",
    "epidemic",
    "downward_mobility",
    "extermination",
    "uprising",
    "revolution",
    "successful_revolution",
    "civil_war",
    "century_plus",
    "fragmentation",
    "capital",
    "conquest",
    "assassination",
    "depose",
    "constitution",
    "labor",
    "unfree_labor",
    "suffrage",
    "public_goods",
    "religion",
]


class Us_location(models.Model):
    """
    Model representing a location in the US.
    """

    city = models.CharField(max_length=300, null=True, blank=True)
    county = models.CharField(max_length=300, null=True, blank=True)
    special_place = models.CharField(max_length=300, null=True, blank=True)
    us_state = models.CharField(
        max_length=5, choices=US_STATE_CHOICES, null=True, blank=True
    )
    attention_tag = models.CharField(
        max_length=30, choices=ATTENTION_TAGS_CHOICES, null=True, blank=True
    )

    class Meta:
        """
        :noindex:
        """

        ordering = ["us_state", "-city", "-county", "-special_place"]

    def __str__(self) -> str:
        components = []

        if self.us_state:
            components.append(
                f"<b>{self.get_us_state_display()} ({self.us_state})</b>"
            )

        if self.city and self.county:
            components.extend([self.city, self.county])
        elif self.city:
            components.append(self.city)
        elif self.county:
            components.append(self.county)
        elif self.special_place:
            components.append(self.special_place)

        components = mark_safe(", ".join(components))

        if not components:
            return "Location (No Data)"

        return components


class Us_violence_subtype(models.Model):
    """
    Model representing a subtype of violence in the US.
    """

    name = models.CharField(max_length=80, null=True, blank=True)
    is_uncertain = models.BooleanField(default=False)

    class Meta:
        """
        :noindex:
        """

        ordering = ["name"]

    def __str__(self) -> str:
        if self.is_uncertain:
            return f"{self.name} (?)"

        return self.name


class Us_violence_data_source(models.Model):
    """
    Model representing a data source for violence in the US.
    """

    name = models.CharField(max_length=300, null=True, blank=True)
    abbreviation = models.CharField(max_length=20, null=True, blank=True)
    url_address = models.URLField(max_length=500, null=True, blank=True)
    is_uncertain = models.BooleanField(default=False)
    attention_tag = models.CharField(
        max_length=30, choices=ATTENTION_TAGS_CHOICES, null=True, blank=True
    )

    class Meta:
        """
        :noindex:
        """

        ordering = ["name"]

    def __str__(self) -> str:
        if self.abbreviation:
            string = f"<b>{self.abbreviation}</b>: {self.name}{' (?)' if self.is_uncertain else ''}"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if self.is_uncertain:
            return f"{self.name} (?)"

        return self.name


class Us_violence(models.Model):
    """
    Model representing a violence event in the US.
    """

    violence_date = models.DateField(null=True, blank=True)
    violence_type = models.CharField(
        max_length=50, choices=VIOLENCE_TYPE_CHOICES, null=True, blank=True
    )
    violence_subtype = models.ManyToManyField(
        Us_violence_subtype,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    fatalities = models.IntegerField(
        validators=[MinValueValidator(0)], blank=True, null=True
    )
    location = models.ManyToManyField(
        Us_location,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    url_address = models.URLField(max_length=500, null=True, blank=True)
    short_data_source = models.ManyToManyField(
        Us_violence_data_source,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    source_details = models.TextField(
        blank=True,
        null=True,
    )
    narrative = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        """
        :noindex:
        """

        ordering = ["-violence_date", "-fatalities"]

    def show_locations(self):
        return " / ".join(str(location) for location in self.location.all())

    def show_narrative_without_quotes(self):
        if not self.narrative:
            return "No_Narrative"

        return self.narrative.replace('"', "'")

    def show_source_details_without_quotes(self):
        if not self.source_details:
            return "No_source_details"

        return self.source_details.replace('"', "'")

    def show_violence_subtypes(self):
        return ", ".join(
            str(subtype) for subtype in self.violence_subtype.all()
        )

    def show_short_data_sources(self):
        return ", ".join(
            str(data_source) for data_source in self.short_data_source.all()
        )

    def __str__(self) -> str:
        location_str = ": " + " and ".join(
            str(location) for location in self.location.all()
        )
        return f"Violence: {self.fatalities} deaths in{location_str}."


class Crisis_consequence(SeshatCommon, CrisisDBMixin):
    """
    Model representing a crisis consequence.
    """

    crisis_case_id = models.CharField(max_length=100)
    other_polity = models.ForeignKey(
        Polity,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related_other",
        related_query_name="%(app_label)s_%(class)s_other",
        null=True,
        blank=True,
    )
    is_first_100 = models.BooleanField(default=False, blank=True, null=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    decline = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    collapse = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    epidemic = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    downward_mobility = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    extermination = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    uprising = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    revolution = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    successful_revolution = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    civil_war = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    century_plus = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    fragmentation = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    capital = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    conquest = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    assassination = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    depose = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    constitution = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    labor = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    unfree_labor = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    suffrage = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    public_goods = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )
    religion = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, null=True, blank=True
    )

    _reverse = "crisis_consequence-detail"
    _clean_name = "crisis_consequence"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Crisis consequence"
        verbose_name_plural = "Crisis consequences"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.Productivity
        variable = "Crisis consequence"
        notes = "Notes for the Variable crisis_consequence are missing!"
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "crisis_consequence": {
                "min": None,
                "max": None,
                "scale": 1000,
                "var_exp_source": None,
                "var_exp": "No Explanations.",
                "units": "mu?",
                "choices": None,
            }
        }
        potential_cols = ["choices"]

    def get_columns_with_value(self, value):
        """
        Return the columns with a given value.

        :noindex:

        Args:
            value (str): The value to search for.

        Returns:
            list: A list of columns with the given value. If no columns have
                the given value, the method returns None.
        """
        columns = []
        for field_name in FIELDS:
            field_value = getattr(self, field_name)

            if field_value and field_value == value:
                columns.append(field_name)

        if not columns:
            return None

        return columns

    def get_columns_with_value_dic(self, value):
        columns = {}
        for field_name in FIELDS:
            field_value = getattr(self, field_name)

            if field_value and field_value == value:
                columns[field_name] = CRISIS_DEFS_EXAMPLES[field_name]

        if not columns:
            return None

        return columns

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name

    def render_absence_presence(self, item):
        """
        Render the absence or presence of a crisis consequence.

        Args:
            item (str): The item to render.

        Returns:
            str: The rendered HTML.
        """
        if item == "P":
            return ICONS.check

        if item == "A":
            return ICONS.xmark

        return "-"

    def clean_decline(self):
        return self.render_absence_presence(self.decline)

    def clean_collapse(self):
        return self.render_absence_presence(self.collapse)

    def show_value(self):
        return get_model_instance_name(self)


class PowerTransitionQuerySet(models.QuerySet):
    def infer_duration(self):
        """
        # TODO
        """
        minimum = (
            self.aggregate(models.Min("year_from"))["year_from__min"] or 0
        )
        maximum = (
            self.aggregate(models.Max("year_from"))["year_from__max"] or 0
        )

        # Return the list
        return [minimum, maximum]


class Power_transition(SeshatCommon, CrisisDBMixin):
    """
    Model representing a power transition.
    """

    predecessor = models.CharField(max_length=200, blank=True, null=True)
    successor = models.CharField(max_length=200, blank=True, null=True)
    reign_number_predecessor = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=400, blank=True, null=True)
    culture_group = models.CharField(max_length=200, blank=True, null=True)
    contested = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, blank=True, null=True
    )
    overturn = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, blank=True, null=True
    )
    predecessor_assassination = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, blank=True, null=True
    )
    intra_elite = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, blank=True, null=True
    )
    military_revolt = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, blank=True, null=True
    )
    popular_uprising = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, blank=True, null=True
    )
    separatist_rebellion = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, blank=True, null=True
    )
    external_invasion = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, blank=True, null=True
    )
    external_interference = models.CharField(
        max_length=5, choices=CRISISDB_CHOICES, blank=True, null=True
    )

    objects = PowerTransitionQuerySet.as_manager()

    _reverse = "power_transition-detail"
    _clean_name = "power_transition"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Power Transition"
        verbose_name_plural = "Power Transitions"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.Productivity
        variable = "Power Transition"
        notes = "Notes for the Variable power_transition are missing!"
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "power_transition": {
                "min": None,
                "max": None,
                "scale": 1000,
                "var_exp_source": None,
                "var_exp": "No Explanations.",
                "units": "mu?",
                "choices": None,
            }
        }
        potential_cols = ["choices"]

    def validate_polity(self) -> bool:
        """
        Validate the polity field of the model instance.

        :noindex:

        Returns:
            bool: True if the polity field is valid.

        Raises:
            ValidationError: If there is no selected Polity.
        """
        if not self.polity:
            string = _wrap_in_warning("There is no selected Polity!")
            raise ValidationError({"polity": mark_safe(string)})

        return True

    def clean(self):
        """ """
        validate_time_range(self, limited=True)
        self.validate_polity()

    def get_columns_with_value(self, value):
        """
        Return the columns with a given value.

        :noindex:

        Args:
            value (str): The value to search for.

        Returns:
            list: A list of columns with the given value. If no columns have
                the given value, the method returns None.
        """
        columns = []
        fields = [
            "contested",
            "overturn",
            "predecessor_assassination",
            "intra_elite",
            "military_revolt",
            "popular_uprising",
            "separatist_rebellion",
            "external_invasion",
            "external_interference",
        ]

        for field_name in fields:
            field_value = getattr(self, field_name)

            if field_value and field_value == value:
                columns.append(field_name)

        if columns:
            return columns
        else:
            return None

    def get_columns_with_value_dic(self, value):
        columns = {}
        fields = [
            "contested",
            "overturn",
            "predecessor_assassination",
            "intra_elite",
            "military_revolt",
            "popular_uprising",
            "separatist_rebellion",
            "external_invasion",
            "external_interference",
        ]

        for field_name in fields:
            field_value = getattr(self, field_name)

            if field_value and field_value == value:
                columns[field_name] = POWER_TRANSITIONS_DEFS_EXAMPLES[
                    field_name
                ]

        if columns:
            return columns
        else:
            return None

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name

    def show_value(self):
        return self.__str__

    def __str__(self) -> str:
        if self.polity and self.predecessor and self.successor:
            return f"Power Transition in {self.polity}: {self.predecessor} was replaced by {self.successor}."  # noqa: E501 pylint: disable=C0301

        return "Power Transition in x: Y was replaced by Z"  # TODO: is this correct?


class Human_sacrifice(SeshatCommon, CrisisDBMixin):
    """
    Model representing a human sacrifice.
    """

    name = models.CharField(max_length=100, default="Human_sacrifice")
    human_sacrifice = models.CharField(
        max_length=500, choices=HUMAN_SACRIFICE_HUMAN_SACRIFICE_CHOICES
    )

    _reverse = "human_sacrifice-detail"
    _clean_name = "human_sacrifice"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Human_sacrifice"
        verbose_name_plural = "Human_sacrifices"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.conflict
        subsection = SUBSECTIONS.crisisdb.ExternalConflicts
        variable = "Human Sacrifice"
        notes = "This is a new model definition for Human Sacrifice."
        description = "The deliberate and ritualized killing of a person to please or placate supernatural entities (including gods, spirits, and ancestors) or gain other supernatural benefits."  # noqa: E501 pylint: disable=C0301
        description_source = ""
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "human_sacrifice": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of Human Sacrifice",
                "units": None,
                "choices": ["U", "A;P", "P*", "P", "A~P", "A", "A*", "P~A"],
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = ["choices"]

    def show_value(self):
        return self.get_human_sacrifice_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class External_conflict(SeshatCommon, CrisisDBMixin):
    """
    Model representing an external conflict.
    """

    name = models.CharField(max_length=100, default="External_conflict")
    conflict_name = models.CharField(max_length=500, blank=True, null=True)

    _reverse = "external_conflict-detail"
    _clean_name = "external_conflict"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "External_conflict"
        verbose_name_plural = "External_conflicts"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.conflict
        subsection = SUBSECTIONS.crisisdb.ExternalConflicts
        variable = "External Conflict"
        notes = "This is a new model definition for External conflicts."
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "conflict_name": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The unique name of this external conflict",
                "units": None,
                "choices": None,
            }
        }


class Internal_conflict(SeshatCommon, CrisisDBMixin):
    """
    Model representing an internal conflict.
    """

    name = models.CharField(max_length=100, default="Internal_conflict")
    conflict = models.CharField(max_length=500, blank=True, null=True)
    expenditure = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    leader = models.CharField(max_length=500, blank=True, null=True)
    casualty = models.IntegerField(blank=True, null=True)

    _reverse = "internal_conflict-detail"
    _clean_name = "internal_conflict"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Internal_conflict"
        verbose_name_plural = "Internal_conflicts"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.conflict
        subsection = SUBSECTIONS.crisisdb.InternalConflicts
        variable = "Internal Conflict"
        notes = "This is a new model definition for internal conflicts."
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "conflict": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The name of the conflict",
                "units": None,
                "choices": None,
            },
            "expenditure": {
                "min": None,
                "max": None,
                "scale": 1000000,
                "var_exp_source": None,
                "var_exp": "The military expenses in millions silver taels.",
                "units": "silver taels",
                "choices": None,
            },
            "leader": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The leader of the conflict",
                "units": None,
                "choices": None,
            },
            "casualty": {
                "min": None,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "The number of people who died in this conflict.",
                "units": "People",
                "choices": None,
            },
        }


class External_conflict_side(SeshatCommon, CrisisDBMixin):
    """
    Model representing an external conflict side.
    """

    name = models.CharField(max_length=100, default="External_conflict_side")
    conflict_id = models.ForeignKey(
        External_conflict,
        on_delete=models.SET_NULL,
        null=True,
        related_name="External_conflicts",
    )
    expenditure = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    leader = models.CharField(max_length=500, blank=True, null=True)
    casualty = models.IntegerField(blank=True, null=True)

    _reverse = "external_conflict_side-detail"
    _clean_name = "external_conflict_side"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "External_conflict_side"
        verbose_name_plural = "External_conflict_sides"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.conflict
        subsection = SUBSECTIONS.crisisdb.ExternalConflicts
        variable = "External Conflict Side"
        notes = "This is a new model definition for External conflict sides"
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "conflict_id": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The external_conflict which is the actual conflict we are talking about",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": None,
            },
            "expenditure": {
                "min": None,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "The military expenses (from this side) in silver taels.",
                "units": "silver taels",
                "choices": None,
            },
            "leader": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The leader of this side of conflict",
                "units": None,
                "choices": None,
            },
            "casualty": {
                "min": None,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "The number of people who died (from this side) in this conflict.",  # noqa: E501 pylint: disable=C0301
                "units": "People",
                "choices": None,
            },
        }


class Agricultural_population(SeshatCommon, CrisisDBMixin):
    """
    Model representing an agricultural population.
    """

    name = models.CharField(max_length=100, default="Agricultural_population")
    agricultural_population = models.IntegerField(blank=True, null=True)

    _reverse = "agricultural_population-detail"
    _clean_name = "agricultural_population"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Agricultural_population"
        verbose_name_plural = "Agricultural_populations"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.Productivity
        variable = "Agricultural Population"
        notes = "Notes for the Variable agricultural_population are missing!"
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "agricultural_population": {
                "min": 0,
                "max": None,
                "scale": 1000,
                "var_exp_source": None,
                "var_exp": "No Explanations.",
                "units": "People",
                "choices": None,
            }
        }


class Arable_land(SeshatCommon, CrisisDBMixin):
    """
    Model representing an arable land.
    """

    name = models.CharField(max_length=100, default="Arable_land")
    arable_land = models.IntegerField(blank=True, null=True)

    _reverse = "arable_land-detail"
    _clean_name = "arable_land"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Arable_land"
        verbose_name_plural = "Arable_lands"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.Productivity
        variable = "Arable Land"
        notes = "Notes for the Variable arable_land are missing!"
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "arable_land": {
                "min": None,
                "max": None,
                "scale": 1000,
                "var_exp_source": None,
                "var_exp": "No Explanations.",
                "units": "mu?",
                "choices": None,
            }
        }


class Arable_land_per_farmer(SeshatCommon, CrisisDBMixin):
    """
    Model representing an arable land per farmer.
    """

    name = models.CharField(max_length=100, default="Arable_land_per_farmer")
    arable_land_per_farmer = models.IntegerField(blank=True, null=True)

    _reverse = "arable_land_per_farmer-detail"
    _clean_name = "arable_land_per_farmer"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Arable_land_per_farmer"
        verbose_name_plural = "Arable_land_per_farmers"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.Productivity
        variable = "Arable Land Per Farmer"
        notes = "Notes for the Variable arable_land_per_farmer are missing!"
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "arable_land_per_farmer": {
                "min": None,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "No Explanations.",
                "units": "mu?",
                "choices": None,
            }
        }


class Gross_grain_shared_per_agricultural_population(
    SeshatCommon, CrisisDBMixin
):
    """
    Model representing a gross grain shared per agricultural population.
    """

    name = models.CharField(
        max_length=100,
        default="Gross_grain_shared_per_agricultural_population",
    )
    gross_grain_shared_per_agricultural_population = models.IntegerField(
        blank=True, null=True
    )

    _reverse = "gross_grain_shared_per_agricultural_population-detail"
    _clean_name = "gross_grain_shared_per_agricultural_population"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gross_grain_shared_per_agricultural_population"
        verbose_name_plural = "Gross_grain_shared_per_agricultural_populations"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.Productivity
        variable = "Gross Grain Shared Per Agricultural Population"
        notes = "Notes for the Variable gross_grain_shared_per_agricultural_population are missing!"  # noqa: E501 pylint: disable=C0301
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "gross_grain_shared_per_agricultural_population": {
                "min": None,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "No Explanations.",
                "units": "(catties per capita)",
                "choices": None,
            }
        }


class Net_grain_shared_per_agricultural_population(
    SeshatCommon, CrisisDBMixin
):
    """
    Model representing a net grain shared per agricultural population.
    """

    name = models.CharField(
        max_length=100, default="Net_grain_shared_per_agricultural_population"
    )
    net_grain_shared_per_agricultural_population = models.IntegerField(
        blank=True, null=True
    )

    _reverse = "net_grain_shared_per_agricultural_population-detail"
    _clean_name = "net_grain_shared_per_agricultural_population"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Net_grain_shared_per_agricultural_population"
        verbose_name_plural = "Net_grain_shared_per_agricultural_populations"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.Productivity
        variable = "Net Grain Shared Per Agricultural Population"
        notes = "Notes for the Variable net_grain_shared_per_agricultural_population are missing!"  # noqa: E501 pylint: disable=C0301
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "net_grain_shared_per_agricultural_population": {
                "min": None,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "No Explanations.",
                "units": "(catties per capita)",
                "choices": None,
            }
        }


class Surplus(SeshatCommon, CrisisDBMixin):
    """
    Model representing a surplus.
    """

    name = models.CharField(max_length=100, default="Surplus")
    surplus = models.IntegerField(blank=True, null=True)

    _reverse = "surplus-detail"
    _clean_name = "surplus"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Surplus"
        verbose_name_plural = "Surplus"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.Productivity
        variable = "Surplus"
        notes = "Notes for the Variable surplus are missing!"
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "surplus": {
                "min": None,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "No Explanations.",
                "units": "(catties per capita)",
                "choices": None,
            }
        }


class Military_expense(SeshatCommon, CrisisDBMixin):
    """
    Model representing a military expense.
    """

    name = models.CharField(max_length=100, default="Military_expense")
    conflict = models.CharField(max_length=500, blank=True, null=True)
    expenditure = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )

    _reverse = "military_expense-detail"
    _clean_name = "military_expense"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Military_expense"
        verbose_name_plural = "Military_expenses"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.StateFinances
        variable = "Military Expense"
        notes = "Not sure about Section and Subsection."
        description = (
            "Main Descriptions for the Variable military_expense are missing!"
        )
        description_source = (
            "Main Descriptions for the Variable military_expense are missing!"
        )
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "conflict": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The name of the conflict",
                "units": None,
                "choices": None,
            },
            "expenditure": {
                "min": None,
                "max": None,
                "scale": 1000000,
                "var_exp_source": None,
                "var_exp": "The military expenses in millions silver taels.",
                "units": "silver taels",
                "choices": None,
            },
        }


class Silver_inflow(SeshatCommon, CrisisDBMixin):
    """
    Model representing a silver inflow.
    """

    name = models.CharField(max_length=100, default="Silver_inflow")
    silver_inflow = models.IntegerField(blank=True, null=True)

    _reverse = "silver_inflow-detail"
    _clean_name = "silver_inflow"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Silver_inflow"
        verbose_name_plural = "Silver_inflows"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.StateFinances
        variable = "Silver Inflow"
        notes = "Needs supervision on the units and scale."
        description = "Silver inflow in Millions of silver taels??"
        description_source = "Silver inflow in Millions of silver taels??"
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "silver_inflow": {
                "min": None,
                "max": None,
                "scale": 1000000,
                "var_exp_source": None,
                "var_exp": "Silver inflow in Millions of silver taels??",
                "units": "silver taels??",
                "choices": None,
            }
        }


class Silver_stock(SeshatCommon, CrisisDBMixin):
    """
    Model representing a silver stock.
    """

    name = models.CharField(max_length=100, default="Silver_stock")
    silver_stock = models.IntegerField(blank=True, null=True)

    _reverse = "silver_stock-detail"
    _clean_name = "silver_stock"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Silver_stock"
        verbose_name_plural = "Silver_stocks"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.StateFinances
        variable = "Silver Stock"
        notes = "Needs supervision on the units and scale."
        description = "Silver stock in Millions of silver taels??"
        description_source = "Silver stock in Millions of silver taels??"
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "silver_stock": {
                "min": None,
                "max": None,
                "scale": 1000000,
                "var_exp_source": None,
                "var_exp": "Silver stock in Millions of silver taels??",
                "units": "silver taels??",
                "choices": None,
            }
        }


class Total_population(SeshatCommon, CrisisDBMixin):
    """
    Model representing a total population.
    """

    name = models.CharField(max_length=100, default="Total_population")
    total_population = models.IntegerField(blank=True, null=True)

    _reverse = "total_population-detail"
    _clean_name = "total_population"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Total_population"
        verbose_name_plural = "Total_populations"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.crisisdb.SocialScale
        variable = "Total Population"
        notes = "Note that the population values are scaled."
        description = "Total population or simply population, of a given area is the total number of people in that area at a given time."  # noqa: E501 pylint: disable=C0301
        description_source = "Total population or simply population, of a given area is the total number of people in that area at a given time."  # noqa: E501 pylint: disable=C0301
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "total_population": {
                "min": 0,
                "max": None,
                "scale": 1000,
                "var_exp_source": None,
                "var_exp": "The total population of a country (or a polity).",
                "units": "People",
                "choices": None,
            }
        }


class Gdp_per_capita(SeshatCommon, CrisisDBMixin):
    """
    Model representing a GDP value per capita.
    """

    name = models.CharField(max_length=100, default="Gdp_per_capita")
    gdp_per_capita = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )

    _reverse = "gdp_per_capita-detail"
    _clean_name = "gdp_per_capita"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gdp_per_capita"
        verbose_name_plural = "Gdp_per_capitas"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.economy
        subsection = SUBSECTIONS.crisisdb.Productivity
        variable = "GDP Per Capita"
        notes = "The exact year based on which the value of Dollar is taken into account is not clear."  # noqa: E501 pylint: disable=C0301
        description = "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population."  # noqa: E501 pylint: disable=C0301
        description_source = "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population."  # noqa: E501 pylint: disable=C0301
        inner_variables = {
            "gdp_per_capita": {
                "min": None,
                "max": None,
                "scale": 1,
                "var_exp_source": "https://www.thebalance.com/gdp-per-capita-formula-u-s-compared-to-highest-and-lowest-3305848",  # noqa: E501 pylint: disable=C0301
                "var_exp": "The Gross Domestic Product per capita, or GDP per capita, is a measure of a country's economic output that accounts for its number of people. It divides the country's gross domestic product by its total population.",  # noqa: E501 pylint: disable=C0301
                "units": "Dollars (in 2009?)",
                "choices": None,
            }
        }


class Drought_event(SeshatCommon, CrisisDBMixin):
    """
    Model representing a drought event.
    """

    name = models.CharField(max_length=100, default="Drought_event")
    drought_event = models.IntegerField(blank=True, null=True)

    _reverse = "drought_event-detail"
    _clean_name = "drought_event"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Drought_event"
        verbose_name_plural = "Drought_events"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.wb
        subsection = SUBSECTIONS.crisisdb.BiologicalWellbeing
        variable = "Drought Event"
        notes = "Notes for the Variable drought_event are missing!"
        description = "number of geographic sites indicating drought"
        description_source = "number of geographic sites indicating drought"
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "drought_event": {
                "min": 0,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "number of geographic sites indicating drought",
                "units": "Numbers",
                "choices": None,
            }
        }


class Locust_event(SeshatCommon, CrisisDBMixin):
    """
    Model representing a locust event.
    """

    name = models.CharField(max_length=100, default="Locust_event")
    locust_event = models.IntegerField(blank=True, null=True)

    _reverse = "locust_event-detail"
    _clean_name = "locust_event"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Locust_event"
        verbose_name_plural = "Locust_events"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.wb
        subsection = SUBSECTIONS.crisisdb.BiologicalWellbeing
        variable = "Locust Event"
        notes = "Notes for the Variable locust_event are missing!"
        description = "number of geographic sites indicating locusts"
        description_source = "number of geographic sites indicating locusts"
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "locust_event": {
                "min": 0,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "number of geographic sites indicating locusts",
                "units": "Numbers",
                "choices": None,
            }
        }


class Socioeconomic_turmoil_event(SeshatCommon, CrisisDBMixin):
    """
    Model representing a socioeconomic turmoil event.
    """

    name = models.CharField(
        max_length=100, default="Socioeconomic_turmoil_event"
    )
    socioeconomic_turmoil_event = models.IntegerField(blank=True, null=True)

    _reverse = "socioeconomic_turmoil_event-detail"
    _clean_name = "socioeconomic_turmoil_event"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Socioeconomic_turmoil_event"
        verbose_name_plural = "Socioeconomic_turmoil_events"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.wb
        subsection = SUBSECTIONS.crisisdb.BiologicalWellbeing
        variable = "Socioeconomic Turmoil Event"
        notes = (
            "Notes for the Variable socioeconomic_turmoil_event are missing!"
        )
        description = (
            "number of geographic sites indicating socioeconomic turmoil"
        )
        description_source = (
            "number of geographic sites indicating socioeconomic turmoil"
        )
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "socioeconomic_turmoil_event": {
                "min": 0,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "number of geographic sites indicating socioeconomic turmoil",
                "units": "Numbers",
                "choices": None,
            }
        }


class Crop_failure_event(SeshatCommon, CrisisDBMixin):
    """
    Model representing a crop failure event.
    """

    name = models.CharField(max_length=100, default="Crop_failure_event")
    crop_failure_event = models.IntegerField(blank=True, null=True)

    _reverse = "crop_failure_event-detail"
    _clean_name = "crop_failure_event"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Crop_failure_event"
        verbose_name_plural = "Crop_failure_events"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.wb
        subsection = SUBSECTIONS.crisisdb.BiologicalWellbeing
        variable = "Crop Failure Event"
        notes = "Notes for the Variable crop_failure_event are missing!"
        description = "number of geographic sites indicating crop failure"
        description_source = (
            "number of geographic sites indicating crop failure"
        )
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "crop_failure_event": {
                "min": 0,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "number of geographic sites indicating crop failure",
                "units": "Numbers",
                "choices": None,
            }
        }


class Famine_event(SeshatCommon, CrisisDBMixin):
    """
    Model representing a famine event.
    """

    name = models.CharField(max_length=100, default="Famine_event")
    famine_event = models.IntegerField(blank=True, null=True)

    _reverse = "famine_event-detail"
    _clean_name = "famine_event"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Famine_event"
        verbose_name_plural = "Famine_events"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.wb
        subsection = SUBSECTIONS.crisisdb.BiologicalWellbeing
        variable = "Famine Event"
        notes = "Notes for the Variable famine_event are missing!"
        description = "number of geographic sites indicating famine"
        description_source = "number of geographic sites indicating famine"
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "famine_event": {
                "min": 0,
                "max": None,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "number of geographic sites indicating famine",
                "units": "Numbers",
                "choices": None,
            }
        }


class Disease_outbreak(SeshatCommon, CrisisDBMixin):
    """
    Model representing a disease outbreak.
    """

    name = models.CharField(max_length=100, default="Disease_outbreak")
    longitude = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    latitude = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    elevation = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    sub_category = models.CharField(
        max_length=500, choices=SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES
    )
    magnitude = models.CharField(
        max_length=500, choices=MAGNITUDE_DISEASE_OUTBREAK_CHOICES
    )
    duration = models.CharField(
        max_length=500, choices=DURATION_DISEASE_OUTBREAK_CHOICES
    )

    _reverse = "disease_outbreak-detail"
    _clean_name = "disease_outbreak"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Disease_outbreak"
        verbose_name_plural = "Disease_outbreaks"

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.wb
        subsection = SUBSECTIONS.crisisdb.BiologicalWellbeing
        variable = "Disease Outbreak"
        notes = "Notes for the Variable disease_outbreak are missing!"
        description = "A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season."  # noqa: E501 pylint: disable=C0301
        description_source = "A sudden increase in occurrences of a disease when cases are in excess of normal expectancy for the location or season."  # noqa: E501 pylint: disable=C0301
        null_meaning = NO_DATA.no_value
        inner_variables = {
            "longitude": {
                "min": -180,
                "max": 180,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "The longitude (in degrees) of the place where the disease was spread.",  # noqa: E501 pylint: disable=C0301
                "units": "Degrees",
                "choices": None,
            },
            "latitude": {
                "min": -180,
                "max": 180,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "The latitude (in degrees) of the place where the disease was spread.",  # noqa: E501 pylint: disable=C0301
                "units": "Degrees",
                "choices": None,
            },
            "elevation": {
                "min": 0,
                "max": 5000,
                "scale": 1,
                "var_exp_source": None,
                "var_exp": "Elevation from mean sea level (in meters) of the place where the disease was spread.",  # noqa: E501 pylint: disable=C0301
                "units": "Meters",
                "choices": None,
            },
            "sub_category": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The category of the disease.",
                "units": None,
                "choices": INNER_SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES,
            },
            "magnitude": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "How heavy the disease was.",
                "units": None,
                "choices": INNER_MAGNITUDE_DISEASE_OUTBREAK_CHOICES,
            },
            "duration": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "How long the disease lasted.",
                "units": None,
                "choices": INNER_DURATION_DISEASE_OUTBREAK_CHOICES,
            },
        }
