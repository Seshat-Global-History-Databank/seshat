# TODO: add __all__

from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from ..core.models import SeshatCommon
from ..accounts.models import Seshat_Expert
from ..constants import (
    ABSENT_PRESENT_CHOICES,
    ABSENT_PRESENT_STRING_LIST,
    SECTIONS,
    SUBSECTIONS,
    NO_DATA,
)

from .constants import SOURCE_OF_SUPPORT_CHOICES
from .mixins import SCMixIn


BASECLASS = (
    "fw-light text-secondary"  # TODO: Move to global_constants.py/ATTRS_HTML
)


class Ra(SeshatCommon, SCMixIn):
    """
    A model to record the research assistant or associate who coded the data.
    """

    name = models.CharField(max_length=100, default="Ra")
    sc_ra = models.ForeignKey(
        Seshat_Expert,
        on_delete=models.SET_NULL,
        null=True,
        related_name="sc_research_assistant",
    )

    _clean_name = "ra"
    _clean_name_spaced = "ra"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Ra"
        verbose_name_plural = "Ras"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.Staff
        variable = "ra"
        notes = NO_DATA.note
        description = "The name of the research assistant or associate who coded the data. If more than one RA made a substantial contribution, list all via separate entries."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "sc_ra": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The RA of Social Complexity Variables",
                "units": None,
                "choices": None,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.sc_ra:
            return NO_DATA.default

        return self.sc_ra

    def show_value_from(self):
        if not self.sc_ra:
            return None

        return self.sc_ra


class Polity_territory(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Polity_territory")
    polity_territory_from = models.IntegerField(blank=True, null=True)
    polity_territory_to = models.IntegerField(blank=True, null=True)

    _clean_name = "polity_territory"
    _clean_name_spaced = "Polity Territory"
    _subsection = "Social Scale"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_territory"
        verbose_name_plural = "Polity_territories"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.SocialScale
        variable = "Polity Territory"
        notes = NO_DATA.note
        description = "Talking about Social Scale, Polity territory is coded in squared kilometers."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "polity_territory_from": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The lower range of polity territory for a polity.",
                "units": "km squared",
                "choices": None,
                "null_meaning": None,
            },
            "polity_territory_to": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The upper range of polity territory for a polity.",
                "units": "km squared",
                "choices": None,
                "null_meaning": None,
            },
        }
        null_meaning = NO_DATA.no_value
        potential_cols = ["Units"]

    def show_value(self):
        if all(
            [
                self.polity_territory_from is not None,
                self.polity_territory_to is not None,
                self.polity_territory_to == self.polity_territory_from,
            ]
        ):
            string = f"{self.polity_territory_from:,} <span class='{BASECLASS} fs-6'> km<sup>2</sup> </span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if all(
            [
                self.polity_territory_from is not None,
                self.polity_territory_to is not None,
            ]
        ):
            string = f"<span class='{BASECLASS}'> [</span>{self.polity_territory_from:,} <span class='{BASECLASS}'> to </span> {self.polity_territory_to:,}<span class='{BASECLASS}'>] </span> <span class='{BASECLASS} fs-6'> km<sup>2</sup> </span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if self.polity_territory_from is not None:
            return f"[{self.polity_territory_from:,}, ...]"

        if self.polity_territory_to is not None:
            return f"[..., {self.polity_territory_to:,}]"

        return NO_DATA.default

    def show_value_from(self):
        if not self.polity_territory_from:
            return "unknown"

        return self.polity_territory_from

    def show_value_to(self):
        if not self.polity_territory_to:
            return None

        return self.polity_territory_to


class Polity_population(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Polity_population")
    polity_population_from = models.IntegerField(blank=True, null=True)
    polity_population_to = models.IntegerField(blank=True, null=True)

    _clean_name = "polity_population"
    _clean_name_spaced = "Polity Population"
    _subsection = "Social Scale"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_population"
        verbose_name_plural = "Polity_populations"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.SocialScale
        variable = "Polity Population"
        notes = NO_DATA.note
        description = "Talking about Social Scale, Polity Population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "polity_population_from": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The lower range of polity population for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
            "polity_population_to": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The upper range of polity population for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if all(
            [
                self.polity_population_from is not None,
                self.polity_population_to is not None,
                self.polity_population_to == self.polity_population_from,
            ]
        ):
            string = f"{self.polity_population_from:,}<span class='{BASECLASS} fs-6'> people </span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if all(
            [
                self.polity_population_from is not None,
                self.polity_population_to is not None,
            ]
        ):
            string = f"<span class='{BASECLASS}'> [</span>{self.polity_population_from:,} <span class='{BASECLASS}'> to </span> {self.polity_population_to:,}<span class='{BASECLASS}'>] </span> <span class='{BASECLASS} fs-6'> people </span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if self.polity_population_from is not None:
            return f"[{self.polity_population_from:,}, ...]"

        if self.polity_population_to is not None:
            return f"[..., {self.polity_population_to:,}]"

        return NO_DATA.default

    def show_value_from(self):
        if not self.polity_population_from:
            return "unknown"

        return self.polity_population_from

    def show_value_to(self):
        if not self.polity_population_to:
            return None

        return self.polity_population_to


class Population_of_the_largest_settlement(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Population_of_the_largest_settlement"
    )
    population_of_the_largest_settlement_from = models.IntegerField(
        blank=True, null=True
    )
    population_of_the_largest_settlement_to = models.IntegerField(
        blank=True, null=True
    )

    _clean_name = "population_of_the_largest_settlement"
    _clean_name_spaced = "Population of the Largest Settlement"
    _subsection = "Social Scale"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Population_of_the_largest_settlement"
        verbose_name_plural = "Population_of_the_largest_settlements"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.SocialScale
        variable = "Population of the Largest Settlement"
        notes = NO_DATA.note
        description = "Talking about Social Scale, Population of the largest settlement is the estimated population of the largest settlement of the polity. Note that the largest settlement could be different from the capital (coded under General Variables). If possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). Note that we are also building a city database - you should consult it as it may already have the needed data."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "population_of_the_largest_settlement_from": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The lower range of population of the largest settlement for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
            "population_of_the_largest_settlement_to": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The upper range of population of the largest settlement for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if all(
            [
                self.population_of_the_largest_settlement_from is not None,
                self.population_of_the_largest_settlement_to is not None,
                self.population_of_the_largest_settlement_to
                == self.population_of_the_largest_settlement_from,
            ]
        ):
            string = f"{self.population_of_the_largest_settlement_from:,} <span class='{BASECLASS} fs-6'> people </span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if all(
            [
                self.population_of_the_largest_settlement_from is not None,
                self.population_of_the_largest_settlement_to is not None,
            ]
        ):
            string = f"<span class='{BASECLASS}'> [</span>{self.population_of_the_largest_settlement_from:,} <span class='{BASECLASS}'> to </span> {self.population_of_the_largest_settlement_to:,}<span class='{BASECLASS}'>] </span> <span class='{BASECLASS} fs-6'> people </span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if self.population_of_the_largest_settlement_from is not None:
            return f"[{self.population_of_the_largest_settlement_from:,}, ...]"

        if self.population_of_the_largest_settlement_to is not None:
            return f"[..., {self.population_of_the_largest_settlement_to:,}]"

        return NO_DATA.default

    def show_value_from(self):
        if not self.population_of_the_largest_settlement_from:
            return "unknown"

        return self.population_of_the_largest_settlement_from

    def show_value_to(self):
        if not self.population_of_the_largest_settlement_to:
            return None

        return self.population_of_the_largest_settlement_to

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse(
            "population_of_the_largest_settlement-detail", args=[str(self.id)]
        )


class Settlement_hierarchy(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Settlement_hierarchy")
    settlement_hierarchy_from = models.IntegerField(blank=True, null=True)
    settlement_hierarchy_to = models.IntegerField(blank=True, null=True)

    _clean_name = "settlement_hierarchy"
    _clean_name_spaced = "Settlement Hierarchy"
    _subsection = "Hierarchical Complexity"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Settlement_hierarchy"
        verbose_name_plural = "Settlement_hierarchies"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.HierarchicalComplexity
        variable = "Settlement Hierarchy"
        notes = NO_DATA.note
        description = "Talking about Hierarchical Complexity, Settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. As settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). Example: (1) Large City (monumental structures, theatre, market, hospital, central government buildings) (2) City (market, theatre, regional government buildings) (3) Large Town (market, administrative buildings) (4) Town (administrative buildings, storehouse)) (5) Village (shrine) (6) Hamlet (residential only). In the narrative paragraph explain the different levels and list their functions. Provide a (crude) estimate of population sizes. For example, Large Town (market, temple, administrative buildings): 2,000-5,000 inhabitants."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "settlement_hierarchy_from": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The lower range of settlement hierarchy for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
            "settlement_hierarchy_to": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The upper range of settlement hierarchy for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if all(
            [
                self.settlement_hierarchy_from is not None,
                self.settlement_hierarchy_to is not None,
                self.settlement_hierarchy_to == self.settlement_hierarchy_from,
            ]
        ):
            return self.settlement_hierarchy_from

        if all(
            [
                self.settlement_hierarchy_from is not None,
                self.settlement_hierarchy_to is not None,
            ]
        ):
            return f"[{self.settlement_hierarchy_from:,} to {self.settlement_hierarchy_to:,}]"  # noqa: E501 pylint: disable=C0301

        if self.settlement_hierarchy_from is not None:
            return f"[{self.settlement_hierarchy_from:,}, ...]"

        if self.settlement_hierarchy_to is not None:
            return f"[..., {self.settlement_hierarchy_to:,}]"

        return NO_DATA.default

    def show_value_from(self):
        if not self.settlement_hierarchy_from:
            return "unknown"

        return self.settlement_hierarchy_from

    def show_value_to(self):
        if not self.settlement_hierarchy_to:
            return None

        return self.settlement_hierarchy_to


class Administrative_level(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Administrative_level")
    administrative_level_from = models.IntegerField(blank=True, null=True)
    administrative_level_to = models.IntegerField(blank=True, null=True)

    _clean_name = "administrative_level"
    _clean_name_spaced = "Administrative Level"
    _subsection = "Hierarchical Complexity"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Administrative_level"
        verbose_name_plural = "Administrative_levels"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.HierarchicalComplexity
        variable = "Administrative Level"
        notes = NO_DATA.note
        description = "Talking about Hierarchical Complexity, Administrative levels records the administrative levels of a polity. An example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. Note that unlike in settlement hierarchy, here you code people hierarchy. Do not simply copy settlement hierarchy data here. For archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. Note: Often there are more than one concurrent administrative hierarchy. In the example above the hierarchy refers to the territorial government. In addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. For example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. In the narrative paragraph detail what is known about both hierarchies. The machine-readable code should reflect the largest number (the longer chain of command)."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "administrative_level_from": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The lower range of administrative level for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
            "administrative_level_to": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The upper range of administrative level for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if all(
            [
                self.administrative_level_from is not None,
                self.administrative_level_to is not None,
                self.administrative_level_to == self.administrative_level_from,
            ]
        ):
            return self.administrative_level_from

        if all(
            [
                self.administrative_level_from is not None,
                self.administrative_level_to is not None,
            ]
        ):
            return f"[{self.administrative_level_from:,} to {self.administrative_level_to:,}]"  # noqa: E501 pylint: disable=C0301

        if self.administrative_level_from is not None:
            return f"[{self.administrative_level_from:,}, ...]"

        if self.administrative_level_to is not None:
            return f"[..., {self.administrative_level_to:,}]"

        return NO_DATA.default

    def show_value_from(self):
        if not self.administrative_level_from:
            return "unknown"

        return self.administrative_level_from

    def show_value_to(self):
        if not self.administrative_level_to:
            return None

        return self.administrative_level_to


class Religious_level(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Religious_level")
    religious_level_from = models.IntegerField(blank=True, null=True)
    religious_level_to = models.IntegerField(blank=True, null=True)

    _clean_name = "religious_level"
    _clean_name_spaced = "Religious Level"
    _subsection = "Hierarchical Complexity"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Religious_level"
        verbose_name_plural = "Religious_levels"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.HierarchicalComplexity
        variable = "Religious Level"
        notes = NO_DATA.note
        description = "Talking about Hierarchical Complexity, Religious levels records the Religious levels of a polity. Same principle as with Administrative levels. Start with the head of the official cult (if present) coded as: level 1, and work down to the local priest."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "religious_level_from": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The lower range of religious level for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
            "religious_level_to": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The upper range of religious level for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if all(
            [
                self.religious_level_from is not None,
                self.religious_level_to is not None,
                self.religious_level_to == self.religious_level_from,
            ]
        ):
            return self.religious_level_from

        if all(
            [
                self.religious_level_from is not None,
                self.religious_level_to is not None,
            ]
        ):
            return f"[{self.religious_level_from:,} to {self.religious_level_to:,}]"

        if self.religious_level_from is not None:
            return f"[{self.religious_level_from:,}, ...]"

        if self.religious_level_to is not None:
            return f"[..., {self.religious_level_to:,}]"

        return NO_DATA.default

    def show_value_from(self):
        if not self.religious_level_from:
            return "unknown"

        return self.religious_level_from

    def show_value_to(self):
        if not self.religious_level_to:
            return None

        return self.religious_level_to


class Military_level(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Military_level")
    military_level_from = models.IntegerField(blank=True, null=True)
    military_level_to = models.IntegerField(blank=True, null=True)

    _clean_name = "military_level"
    _clean_name_spaced = "Military Level"
    _subsection = "Hierarchical Complexity"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Military_level"
        verbose_name_plural = "Military_levels"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.HierarchicalComplexity
        variable = "Military Level"
        notes = NO_DATA.note
        description = "Talking about Hierarchical Complexity, Military levels records the Military levels of a polity. Same principle as with Administrative levels. Start with the commander-in-chief coded as: level 1, and work down to the private. Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier)."  # noqa: E501 pylint: disable=C0301
        description = """levels. Again, start with the commander-in-chief = level 1 and work down to the private.
Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier).""",  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = "NOTHING"
        inner_variables = {
            "military_level_from": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The lower range of military level for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
            "military_level_to": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The upper range of military level for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            },
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if all(
            [
                self.military_level_from is not None
                and self.military_level_to is not None
                and self.military_level_to == self.military_level_from
            ]
        ):
            return self.military_level_from

        if (
            self.military_level_from is not None
            and self.military_level_to is not None
        ):
            return (
                f"[{self.military_level_from:,} to {self.military_level_to:,}]"
            )

        if self.military_level_from is not None:
            return f"[{self.military_level_from:,}, ...]"

        if self.military_level_to is not None:
            return f"[..., {self.military_level_to:,}]"

        return NO_DATA.default

    def show_value_from(self):
        if not self.military_level_from:
            return "unknown"

        return self.military_level_from

    def show_value_to(self):
        if not self.military_level_to:
            return None

        return self.military_level_to


class Professional_military_officer(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Professional_military_officer"
    )
    professional_military_officer = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "professional_military_officer"
    _clean_name_spaced = "Professional Military Officer"
    _subsection = "Professions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Professional_military_officer"
        verbose_name_plural = "Professional_military_officers"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.Professions
        variable = "Professional Military Officer"
        notes = NO_DATA.note
        description = "Talking about Professions, Professional military officers refer to Full-time Professional military officers."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "professional_military_officer": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of professional military officer for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.professional_military_officer:
            return NO_DATA.default

        return self.get_professional_military_officer_display()

    def show_value_from(self):
        if not self.professional_military_officer:
            return None

        return self.professional_military_officer


class Professional_soldier(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Professional_soldier")
    professional_soldier = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "professional_soldier"
    _clean_name_spaced = "Professional Soldier"
    _subsection = "Professions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Professional_soldier"
        verbose_name_plural = "Professional_soldiers"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.Professions
        variable = "Professional Soldier"
        notes = NO_DATA.note
        description = "Talking about Professions, Professional soldiers refer to Full-time Professional soldiers."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "professional_soldier": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of professional soldier for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.professional_soldier:
            return NO_DATA.default

        return self.get_professional_soldier_display()

    def show_value_from(self):
        if not self.professional_soldier:
            return None

        return self.professional_soldier


class Professional_priesthood(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Professional_priesthood")
    professional_priesthood = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "professional_priesthood"
    _clean_name_spaced = "Professional Priesthood"
    _subsection = "Professions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Professional_priesthood"
        verbose_name_plural = "Professional_priesthoods"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.Professions
        variable = "Professional Priesthood"
        notes = NO_DATA.note
        description = "Talking about Professions, Professional priesthood refers to Full-time Professional priesthood."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "professional_priesthood": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of professional priesthood for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value

    def show_value(self):
        if not self.professional_priesthood:
            return NO_DATA.default

        return self.get_professional_priesthood_display()

    def show_value_from(self):
        if not self.professional_priesthood:
            return None

        return self.professional_priesthood


class Full_time_bureaucrat(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Full_time_bureaucrat")
    full_time_bureaucrat = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "full_time_bureaucrat"
    _clean_name_spaced = "Full Time Bureaucrat"
    _subsection = "Bureaucracy Characteristics"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Full_time_bureaucrat"
        verbose_name_plural = "Full_time_bureaucrats"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.BureaucracyCharacteristics
        variable = "Full Time Bureaucrat"
        notes = NO_DATA.note
        description = "Talking about Bureaucracy characteristics, Full-time bureaucrats refer to Full-time administrative specialists. Code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. Also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. Note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "full_time_bureaucrat": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of full time bureaucrat for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.full_time_bureaucrat:
            return NO_DATA.default

        return self.get_full_time_bureaucrat_display()

    def show_value_from(self):
        if not self.full_time_bureaucrat:
            return None

        return self.full_time_bureaucrat


class Examination_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Examination_system")
    examination_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "examination_system"
    _clean_name_spaced = "Examination System"
    _subsection = "Bureaucracy Characteristics"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Examination_system"
        verbose_name_plural = "Examination_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.BureaucracyCharacteristics
        variable = "Examination System"
        notes = NO_DATA.note
        description = "Talking about Bureaucracy characteristics, The paradigmatic example of an Examination system is the Chinese imperial system."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "examination_system": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of examination system for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.examination_system:
            return NO_DATA.default

        return self.get_examination_system_display()

    def show_value_from(self):
        if not self.examination_system:
            return None

        return self.examination_system


class Merit_promotion(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Merit_promotion")
    merit_promotion = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "merit_promotion"
    _clean_name_spaced = "Merit Promotion"
    _subsection = "Bureaucracy Characteristics"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Merit_promotion"
        verbose_name_plural = "Merit_promotions"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.BureaucracyCharacteristics
        variable = "Merit Promotion"
        notes = NO_DATA.note
        description = "Talking about Bureaucracy characteristics, Merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. When exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "merit_promotion": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of merit promotion for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.merit_promotion:
            return NO_DATA.default

        return self.get_merit_promotion_display()

    def show_value_from(self):
        if not self.merit_promotion:
            return None

        return self.merit_promotion


class Specialized_government_building(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Specialized_government_building"
    )
    specialized_government_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "specialized_government_building"
    _clean_name_spaced = "Specialized Government Building"
    _subsection = "Bureaucracy Characteristics"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Specialized_government_building"
        verbose_name_plural = "Specialized_government_buildings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.BureaucracyCharacteristics
        variable = "Specialized Government Building"
        notes = NO_DATA.note
        description = "Talking about Bureaucracy characteristics, These buildings are where administrative officials are located, and must be distinct from the ruler's palace. They may be used for document storage, registration offices, minting money, etc. Defense structures also are not coded here (see Military). State-owned/operated workshop should also not be coded here."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "specialized_government_building": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of specialized government building for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.specialized_government_building:
            return NO_DATA.default

        return self.get_specialized_government_building_display()

    def show_value_from(self):
        if not self.specialized_government_building:
            return None

        return self.specialized_government_building


class Formal_legal_code(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Formal_legal_code")
    formal_legal_code = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "formal_legal_code"
    _clean_name_spaced = "Formal Legal Code"
    _subsection = "Law"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Formal_legal_code"
        verbose_name_plural = "Formal_legal_codes"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.Law
        variable = "Formal Legal Code"
        notes = NO_DATA.note
        description = "Talking about Law, Formal legal code refers to legal code usually, but not always written down. If not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). Provide a short description."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "formal_legal_code": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of formal legal code for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.formal_legal_code:
            return NO_DATA.default

        return self.get_formal_legal_code_display()

    def show_value_from(self):
        if not self.formal_legal_code:
            return None

        return self.formal_legal_code


class Judge(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Judge")
    judge = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "judge"
    _clean_name_spaced = "Judge"
    _subsection = "Law"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Judge"
        verbose_name_plural = "Judges"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.Law
        variable = "Judge"
        notes = NO_DATA.note
        description = "Talking about Law, judges refers only to full-time professional judges."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "judge": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of judge for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.judge:
            return NO_DATA.default

        return self.get_judge_display()

    def show_value_from(self):
        if not self.judge:
            return None

        return self.judge


class Court(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Court")
    court = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "court"
    _clean_name_spaced = "Court"
    _subsection = "Law"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Court"
        verbose_name_plural = "Courts"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.Law
        variable = "Court"
        notes = NO_DATA.note
        description = "Talking about Law, courts are buildings specialized for legal proceedings only."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "court": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of court for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.court:
            return NO_DATA.default

        return self.get_court_display()

    def show_value_from(self):
        if not self.court:
            return None

        return self.court


class Professional_lawyer(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Professional_lawyer")
    professional_lawyer = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "professional_lawyer"
    _clean_name_spaced = "Professional Lawyer"
    _subsection = "Law"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Professional_lawyer"
        verbose_name_plural = "Professional_lawyers"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.Law
        variable = "Professional Lawyer"
        notes = NO_DATA.note
        description = "Talking about Law, NO_DESCRIPTIONS_IN_CODEBOOK."
        description_source = "NOTHING"
        inner_variables = {
            "professional_lawyer": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of professional lawyer for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.professional_lawyer:
            return NO_DATA.default

        return self.get_professional_lawyer_display()

    def show_value_from(self):
        if not self.professional_lawyer:
            return None

        return self.professional_lawyer


class Irrigation_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Irrigation_system")
    irrigation_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "irrigation_system"
    _clean_name_spaced = "Irrigation System"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Irrigation_system"
        verbose_name_plural = "Irrigation_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.SpecializedBuildings
        variable = "Irrigation System"
        notes = NO_DATA.note
        description = "Talking about Specialized Buildings, irrigation systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "irrigation_system": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of irrigation system for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.irrigation_system:
            return NO_DATA.default

        return self.get_irrigation_system_display()

    def show_value_from(self):
        if not self.irrigation_system:
            return None

        return self.irrigation_system


class Drinking_water_supply_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Drinking_water_supply_system"
    )
    drinking_water_supply_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "drinking_water_supply_system"
    _clean_name_spaced = "Drinking Water Supply System"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Drinking_water_supply_system"
        verbose_name_plural = "Drinking_water_supply_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.SpecializedBuildings
        variable = "Drinking Water Supply System"
        notes = NO_DATA.note
        description = "Talking about Specialized Buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "drinking_water_supply_system": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of drinking water supply system for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.drinking_water_supply_system:
            return NO_DATA.default

        return self.get_drinking_water_supply_system_display()

    def show_value_from(self):
        if not self.drinking_water_supply_system:
            return None

        return self.drinking_water_supply_system


class Market(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Market")
    market = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "market"
    _clean_name_spaced = "Market"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Market"
        verbose_name_plural = "Markets"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.SpecializedBuildings
        variable = "Market"
        notes = NO_DATA.note
        description = "Talking about Specialized Buildings, markets are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "market": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of market for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.market:
            return NO_DATA.default

        return self.get_market_display()

    def show_value_from(self):
        if not self.market:
            return None

        return self.market


class Food_storage_site(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Food_storage_site")
    food_storage_site = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "food_storage_site"
    _clean_name_spaced = "Food Storage Site"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Food_storage_site"
        verbose_name_plural = "Food_storage_sites"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.SpecializedBuildings
        variable = "Food Storage Site"
        notes = NO_DATA.note
        description = "Talking about Specialized Buildings, food storage sites are polity owned (which  includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "food_storage_site": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of food storage site for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.food_storage_site:
            return NO_DATA.default
        return self.get_food_storage_site_display()

    def show_value_from(self):
        if not self.food_storage_site:
            return None

        return self.food_storage_site


class Road(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Road")
    road = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "road"
    _clean_name_spaced = "Road"
    _subsection = "Transport Infrastructure"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Road"
        verbose_name_plural = "Roads"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.TransportInfrastructure
        variable = "Road"
        notes = NO_DATA.note
        description = "Talking about Transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. It excludes streets/accessways within settlements and paths between settlements that develop through repeated use."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "road": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of road for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.road:
            return NO_DATA.default

        return self.get_road_display()

    def show_value_from(self):
        if not self.road:
            return None

        return self.road


class Bridge(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Bridge")
    bridge = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "bridge"
    _clean_name_spaced = "Bridge"
    _subsection = "Transport Infrastructure"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Bridge"
        verbose_name_plural = "Bridges"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.TransportInfrastructure
        variable = "Bridge"
        notes = NO_DATA.note
        description = "Talking about Transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it)."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "bridge": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of bridge for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.bridge:
            return NO_DATA.default

        return self.get_bridge_display()

    def show_value_from(self):
        if not self.bridge:
            return None

        return self.bridge


class Canal(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Canal")
    canal = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "canal"
    _clean_name_spaced = "Canal"
    _subsection = "Transport Infrastructure"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Canal"
        verbose_name_plural = "Canals"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.TransportInfrastructure
        variable = "Canal"
        notes = NO_DATA.note
        description = "Talking about Transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it)."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "canal": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of canal for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.canal:
            return NO_DATA.default

        return self.get_canal_display()

    def show_value_from(self):
        if not self.canal:
            return None

        return self.canal


class Port(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Port")
    port = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "port"
    _clean_name_spaced = "Port"
    _subsection = "Transport Infrastructure"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Port"
        verbose_name_plural = "Ports"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.TransportInfrastructure
        variable = "Port"
        notes = NO_DATA.note
        description = "Talking about Transport infrastructure, Ports include river ports. Direct historical or archaeological evidence of Ports is absent when no port has been excavated or all evidence of such has been obliterated. Indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta Egypt at a time we know there was a timber trade with the Levant). When evidence for the variable itself is available the code is 'present.' When other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). When indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "port": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of port for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.port:
            return NO_DATA.default

        return self.get_port_display()

    def show_value_from(self):
        if not self.port:
            return None

        return self.port


class Mines_or_quarry(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Mines_or_quarry")
    mines_or_quarry = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "mines_or_quarry"
    _clean_name_spaced = "Mines or Quarry"
    _subsection = "Special-purpose Sites"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Mines_or_quarry"
        verbose_name_plural = "Mines_or_quarries"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.SpecialPurposeSites
        variable = "Mines or Quarry"
        notes = NO_DATA.note
        description = (
            "Talking about Special purpose sites, NO_DESCRIPTIONS_IN_CODEBOOK."
        )
        description_source = "NOTHING"
        inner_variables = {
            "mines_or_quarry": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of mines or quarry for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.mines_or_quarry:
            return NO_DATA.default

        return self.get_mines_or_quarry_display()

    def show_value_from(self):
        if not self.mines_or_quarry:
            return None

        return self.mines_or_quarry


class Mnemonic_device(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Mnemonic_device")
    mnemonic_device = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "mnemonic_device"
    _clean_name_spaced = "Mnemonic Device"
    _subsection = "Information"
    _subsubsection = "Writing System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Mnemonic_device"
        verbose_name_plural = "Mnemonic_devices"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WritingSystems
        variable = "Mnemonic Device"
        notes = NO_DATA.note
        description = "Talking about Writing Systems, Mnemonic devices are: For example, tallies."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "mnemonic_device": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of mnemonic device for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.mnemonic_device:
            return NO_DATA.default

        return self.get_mnemonic_device_display()

    def show_value_from(self):
        if not self.mnemonic_device:
            return None

        return self.mnemonic_device


class Nonwritten_record(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Nonwritten_record")
    nonwritten_record = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "nonwritten_record"
    _clean_name_spaced = "Nonwritten Record"
    _subsection = "Information"
    _subsubsection = "Writing System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Nonwritten_record"
        verbose_name_plural = "Nonwritten_records"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WritingSystems
        variable = "Nonwritten Record"
        notes = NO_DATA.note
        description = "Talking about Writing Systems, Nonwritten Records are more extensive than mnemonics, but don't utilize script. Example: quipu; seals and stamps."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "nonwritten_record": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of nonwritten record for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.nonwritten_record:
            return NO_DATA.default

        return self.get_nonwritten_record_display()

    def show_value_from(self):
        if not self.nonwritten_record:
            return None

        return self.nonwritten_record


class Written_record(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Written_record")
    written_record = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "written_record"
    _clean_name_spaced = "Written Record"
    _subsection = "Information"
    _subsubsection = "Writing System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Written_record"
        verbose_name_plural = "Written_records"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WritingSystems
        variable = "Written Record"
        notes = NO_DATA.note
        description = "Talking about Writing Systems, Written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. There must be several sentences strung together, at the very minimum. For example, royal proclamations from Mesopotamia and Egypt qualify as written records."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "written_record": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of written record for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.written_record:
            return NO_DATA.default

        return self.get_written_record_display()

    def show_value_from(self):
        if not self.written_record:
            return None

        return self.written_record


class Script(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Script")
    script = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "script"
    _clean_name_spaced = "Script"
    _subsection = "Information"
    _subsubsection = "Writing System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Script"
        verbose_name_plural = "Scripts"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WritingSystems
        variable = "Script"
        notes = NO_DATA.note
        description = "Talking about Writing Systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "script": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of script for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.script:
            return NO_DATA.default

        return self.get_script_display()

    def show_value_from(self):
        if not self.script:
            return None

        return self.script


class Non_phonetic_writing(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Non_phonetic_writing")
    non_phonetic_writing = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "non_phonetic_writing"
    _clean_name_spaced = "Non Phonetic Writing"
    _subsection = "Information"
    _subsubsection = "Writing System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Non_phonetic_writing"
        verbose_name_plural = "Non_phonetic_writings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WritingSystems
        variable = "Non Phonetic Writing"
        notes = NO_DATA.note
        description = (
            "Talking about Writing Systems, this refers to the kind of script."
        )
        description_source = "NOTHING"
        inner_variables = {
            "non_phonetic_writing": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of non phonetic writing for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.non_phonetic_writing:
            return NO_DATA.default

        return self.get_non_phonetic_writing_display()

    def show_value_from(self):
        if not self.non_phonetic_writing:
            return None

        return self.non_phonetic_writing


class Phonetic_alphabetic_writing(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Phonetic_alphabetic_writing"
    )
    phonetic_alphabetic_writing = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "phonetic_alphabetic_writing"
    _clean_name_spaced = "Phonetic Alphabetic Writing"
    _subsection = "Information"
    _subsubsection = "Writing System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Phonetic_alphabetic_writing"
        verbose_name_plural = "Phonetic_alphabetic_writings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WritingSystems
        variable = "Phonetic Alphabetic Writing"
        notes = NO_DATA.note
        description = (
            "Talking about Writing Systems, this refers to the kind of script."
        )
        description_source = "NOTHING"
        inner_variables = {
            "phonetic_alphabetic_writing": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of phonetic alphabetic writing for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.phonetic_alphabetic_writing:
            return NO_DATA.default

        return self.get_phonetic_alphabetic_writing_display()

    def show_value_from(self):
        if not self.phonetic_alphabetic_writing:
            return None

        return self.phonetic_alphabetic_writing


class Lists_tables_and_classification(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Lists_tables_and_classification"
    )
    lists_tables_and_classification = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "lists_tables_and_classification"
    _clean_name_spaced = "Lists Tables and Classification"
    _subsection = "Information"
    _subsubsection = "Kinds of Written Documents"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Lists_tables_and_classification"
        verbose_name_plural = "Lists_tables_and_classifications"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WrittenDocuments
        variable = "Lists Tables and Classification"
        notes = NO_DATA.note
        description = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "lists_tables_and_classification": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of lists tables and classification for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.lists_tables_and_classification:
            return NO_DATA.default

        return self.get_lists_tables_and_classification_display()

    def show_value_from(self):
        if not self.lists_tables_and_classification:
            return None

        return self.lists_tables_and_classification


class Calendar(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Calendar")
    calendar = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "calendar"
    _clean_name_spaced = "Calendar"
    _subsection = "Information"
    _subsubsection = "Kinds of Written Documents"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Calendar"
        verbose_name_plural = "Calendars"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WrittenDocuments
        variable = "Calendar"
        notes = NO_DATA.note
        description = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "calendar": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of calendar for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.calendar:
            return NO_DATA.default

        return self.get_calendar_display()

    def show_value_from(self):
        if not self.calendar:
            return None

        return self.calendar


class Sacred_text(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Sacred_text")
    sacred_text = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "sacred_text"
    _clean_name_spaced = "Sacred Text"
    _subsection = "Information"
    _subsubsection = "Kinds of Written Documents"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Sacred_text"
        verbose_name_plural = "Sacred_texts"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WrittenDocuments
        variable = "Sacred Text"
        notes = NO_DATA.note
        description = "Talking about Kinds of Written Documents, Sacred Texts originate from supernatural agents (deities), or are directly inspired by them."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "sacred_text": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sacred text for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.sacred_text:
            return NO_DATA.default

        return self.get_sacred_text_display()

    def show_value_from(self):
        if not self.sacred_text:
            return None

        return self.sacred_text


class Religious_literature(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Religious_literature")
    religious_literature = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "religious_literature"
    _clean_name_spaced = "Religious Literature"
    _subsection = "Information"
    _subsubsection = "Kinds of Written Documents"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Religious_literature"
        verbose_name_plural = "Religious_literatures"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WrittenDocuments
        variable = "Religious Literature"
        notes = NO_DATA.note
        description = "Talking about Kinds of Written Documents, Religious literature differs from the sacred texts. For example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "religious_literature": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of religious literature for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.religious_literature:
            return NO_DATA.default

        return self.get_religious_literature_display()

    def show_value_from(self):
        if not self.religious_literature:
            return None

        return self.religious_literature


class Practical_literature(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Practical_literature")
    practical_literature = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "practical_literature"
    _clean_name_spaced = "Practical Literature"
    _subsection = "Information"
    _subsubsection = "Kinds of Written Documents"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Practical_literature"
        verbose_name_plural = "Practical_literatures"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WrittenDocuments
        variable = "Practical Literature"
        notes = NO_DATA.note
        description = "Talking about Kinds of Written Documents, Practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. Letters do not count as practical literature."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "practical_literature": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of practical literature for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.practical_literature:
            return NO_DATA.default

        return self.get_practical_literature_display()

    def show_value_from(self):
        if not self.practical_literature:
            return None

        return self.practical_literature


class History(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="History")
    history = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "history"
    _clean_name_spaced = "History"
    _subsection = "Information"
    _subsubsection = "Kinds of Written Documents"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "History"
        verbose_name_plural = "Histories"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WrittenDocuments
        variable = "History"
        notes = NO_DATA.note
        description = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "history": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of history for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.history:
            return NO_DATA.default

        return self.get_history_display()

    def show_value_from(self):
        if not self.history:
            return None

        return self.history


class Philosophy(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Philosophy")
    philosophy = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "philosophy"
    _clean_name_spaced = "Philosophy"
    _subsection = "Information"
    _subsubsection = "Kinds of Written Documents"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Philosophy"
        verbose_name_plural = "Philosophies"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WrittenDocuments
        variable = "Philosophy"
        notes = NO_DATA.note
        description = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "philosophy": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of philosophy for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.philosophy:
            return NO_DATA.default

        return self.get_philosophy_display()

    def show_value_from(self):
        if not self.philosophy:
            return None

        return self.philosophy


class Scientific_literature(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Scientific_literature")
    scientific_literature = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "scientific_literature"
    _clean_name_spaced = "Scientific Literature"
    _subsection = "Information"
    _subsubsection = "Kinds of Written Documents"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Scientific_literature"
        verbose_name_plural = "Scientific_literatures"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WrittenDocuments
        variable = "Scientific Literature"
        notes = NO_DATA.note
        description = "Talking about Kinds of Written Documents, Scientific literature includes mathematics, natural sciences, social sciences."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "scientific_literature": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of scientific literature for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.scientific_literature:
            return NO_DATA.default

        return self.get_scientific_literature_display()

    def show_value_from(self):
        if not self.scientific_literature:
            return None

        return self.scientific_literature


class Fiction(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Fiction")
    fiction = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "fiction"
    _clean_name_spaced = "Fiction"
    _subsection = "Information"
    _subsubsection = "Kinds of Written Documents"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Fiction"
        verbose_name_plural = "Fictions"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.WrittenDocuments
        variable = "Fiction"
        notes = NO_DATA.note
        description = "Talking about Kinds of Written Documents, fiction includes poetry."
        description_source = "NOTHING"
        inner_variables = {
            "fiction": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of fiction for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.fiction:
            return NO_DATA.default

        return self.get_fiction_display()

    def show_value_from(self):
        if not self.fiction:
            return None

        return self.fiction


class Article(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Article")
    article = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "article"
    _clean_name_spaced = "Article"
    _subsection = "Information"
    _subsubsection = "Money"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.FormsOfMoney
        variable = "Article"
        notes = NO_DATA.note
        description = "Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "article": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of article for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.article:
            return NO_DATA.default

        return self.get_article_display()

    def show_value_from(self):
        if not self.article:
            return None

        return self.article


class Token(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Token")
    token = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "token"
    _clean_name_spaced = "Token"
    _subsection = "Information"
    _subsubsection = "Money"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Token"
        verbose_name_plural = "Tokens"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.FormsOfMoney
        variable = "Token"
        notes = NO_DATA.note
        description = "Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "token": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of token for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.token:
            return NO_DATA.default

        return self.get_token_display()

    def show_value_from(self):
        if not self.token:
            return None

        return self.token


class Precious_metal(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Precious_metal")
    precious_metal = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "precious_metal"
    _clean_name_spaced = "Precious Metal"
    _subsection = "Information"
    _subsubsection = "Money"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Precious_metal"
        verbose_name_plural = "Precious_metals"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.FormsOfMoney
        variable = "Precious Metal"
        notes = NO_DATA.note
        description = "Talking about forms of money, Precious metals are non-coined silver, gold, platinum."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "precious_metal": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of precious metal for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.precious_metal:
            return NO_DATA.default

        return self.get_precious_metal_display()

    def show_value_from(self):
        if not self.precious_metal:
            return None

        return self.precious_metal


class Foreign_coin(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Foreign_coin")
    foreign_coin = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "foreign_coin"
    _clean_name_spaced = "Foreign Coin"
    _subsection = "Information"
    _subsubsection = "Money"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Foreign_coin"
        verbose_name_plural = "Foreign_coins"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.FormsOfMoney
        variable = "Foreign Coin"
        notes = NO_DATA.note
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        inner_variables = {
            "foreign_coin": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of foreign coin for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.foreign_coin:
            return NO_DATA.default

        return self.get_foreign_coin_display()

    def show_value_from(self):
        if not self.foreign_coin:
            return None

        return self.foreign_coin


class Indigenous_coin(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Indigenous_coin")
    indigenous_coin = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "indigenous_coin"
    _clean_name_spaced = "Indigenous Coin"
    _subsection = "Information"
    _subsubsection = "Money"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Indigenous_coin"
        verbose_name_plural = "Indigenous_coins"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.FormsOfMoney
        variable = "Indigenous Coin"
        notes = NO_DATA.note
        description = NO_DATA.explanation
        description_source = NO_DATA.explanation
        inner_variables = {
            "indigenous_coin": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of indigenous coin for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.indigenous_coin:
            return NO_DATA.default

        return self.get_indigenous_coin_display()

    def show_value_from(self):
        if not self.indigenous_coin:
            return None

        return self.indigenous_coin


class Paper_currency(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Paper_currency")
    paper_currency = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "paper_currency"
    _clean_name_spaced = "Paper Currency"
    _subsection = "Information"
    _subsubsection = "Money"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Paper_currency"
        verbose_name_plural = "Paper_currencies"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.FormsOfMoney
        variable = "Paper Currency"
        notes = NO_DATA.note
        description = "Paper currency or another kind of fiat money. Note that this only refers to indigenously produced paper currency. Code absent if colonial money is used."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "paper_currency": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of paper currency for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.paper_currency:
            return NO_DATA.default

        return self.get_paper_currency_display()

    def show_value_from(self):
        if not self.paper_currency:
            return None

        return self.paper_currency


class Courier(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Courier")
    courier = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "courier"
    _clean_name_spaced = "Courier"
    _subsection = "Information"
    _subsubsection = "Postal System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Courier"
        verbose_name_plural = "Couriers"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.PostalSystems
        variable = "Courier"
        notes = NO_DATA.note
        description = "Full-time professional couriers."
        description_source = "NOTHING"
        inner_variables = {
            "courier": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of courier for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.courier:
            return NO_DATA.default

        return self.get_courier_display()

    def show_value_from(self):
        if not self.courier:
            return None

        return self.courier


class Postal_station(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Postal_station")
    postal_station = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "postal_station"
    _clean_name_spaced = "Postal Station"
    _subsection = "Information"
    _subsubsection = "Postal System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Postal_station"
        verbose_name_plural = "Postal_stations"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.PostalSystems
        variable = "Postal Station"
        notes = NO_DATA.note
        description = "Talking about postal systems, Postal stations are specialized buildings exclusively devoted to the postal service. If there is a special building that has other functions than a postal station, we still code postal station as present. The intent is to capture additional infrastructure beyond having a corps of messengers."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "postal_station": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of postal station for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.postal_station:
            return NO_DATA.default

        return self.get_postal_station_display()

    def show_value_from(self):
        if not self.postal_station:
            return None

        return self.postal_station


class General_postal_service(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="General_postal_service")
    general_postal_service = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "general_postal_service"
    _clean_name_spaced = "General Postal Service"
    _subsection = "Information"
    _subsubsection = "Postal System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "General_postal_service"
        verbose_name_plural = "General_postal_services"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.sc
        subsection = SUBSECTIONS.sc.PostalSystems
        variable = "General Postal Service"
        notes = NO_DATA.note
        description = "Talking about postal systems, 'General postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "general_postal_service": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of general postal service for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        null_meaning = NO_DATA.no_value
        potential_cols = []

    def show_value(self):
        if not self.general_postal_service:
            return NO_DATA.default

        return self.get_general_postal_service_display()

    def show_value_from(self):
        if not self.general_postal_service:
            return None

        return self.general_postal_service


class Communal_building(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Communal_building")
    communal_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "communal_building"
    _clean_name_spaced = "Communal Building"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Communal_building"
        verbose_name_plural = "Communal_buildings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Communal Building"
        notes = NO_DATA.note
        description = "This code distinguishes between settlements that consist of only private households (code 'absent') and settlements where there are communal buildings which could be used for a variety of uses (code 'present')."  # From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.communal_building:
            return NO_DATA.default

        return self.get_communal_building_display()

    def show_value_from(self):
        if not self.communal_building:
            return None

        return self.communal_building


class Utilitarian_public_building(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Utilitarian_public_building"
    )
    utilitarian_public_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "utilitarian_public_building"
    _clean_name_spaced = "Utilitarian Public Building"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Utilitarian_public_building"
        verbose_name_plural = "Utilitarian_public_buildings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Utilitarian Public Building"
        notes = NO_DATA.note
        description = "Typical examples include aqueducts, sewers, and granaries. In the narrative paragraph list all utilitarian buildings and give examples of the most impressive/costly/large ones."  # From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.utilitarian_public_building:
            return NO_DATA.default

        return self.get_utilitarian_public_building_display()

    def show_value_from(self):
        if not self.utilitarian_public_building:
            return None

        return self.utilitarian_public_building


class Symbolic_building(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Symbolic_building")
    symbolic_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "symbolic_building"
    _clean_name_spaced = "Symbolic Building"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Symbolic_building"
        verbose_name_plural = "Symbolic_buildings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Symbolic Building"
        notes = NO_DATA.note
        description = "Non-utilitarian constructions that display symbols, or are themselves symbols of the community or polity (or a ruler as a symbol of the polity). Examples include Taj Mahal mausoleum, Trajan's Column, Ashoka's Pillars, Qin Shih Huang's Terracota Army, the Statue of Liberty. Has to be constructed by humans, so sacred groves or mountains are not symbolic buildings. A palace is also not a symbolic building, because it has other, utilitarian functions (houses the ruler)."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.symbolic_building:
            return NO_DATA.default

        return self.get_symbolic_building_display()

    def show_value_from(self):
        if not self.symbolic_building:
            return None

        return self.symbolic_building


class Entertainment_building(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Entertainment_building")
    entertainment_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "entertainment_building"
    _clean_name_spaced = "Entertainment Building"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Entertainment_building"
        verbose_name_plural = "Entertainment_buildings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Entertainment Building"
        notes = NO_DATA.note
        description = "These include theaters, arenas, race tracks."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.entertainment_building:
            return NO_DATA.default

        return self.get_entertainment_building_display()

    def show_value_from(self):
        if not self.entertainment_building:
            return None

        return self.entertainment_building


class Knowledge_or_information_building(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Knowledge_or_information_building"
    )
    knowledge_or_information_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "knowledge_or_information_building"
    _clean_name_spaced = "Knowledge Or Information Building"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Knowledge_or_information_building"
        verbose_name_plural = "Knowledge_or_information_buildings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Knowledge or Information Building"
        notes = NO_DATA.note
        description = "These include astronomic observatories, libraries, and museums."
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.knowledge_or_information_building:
            return NO_DATA.default

        return self.get_knowledge_or_information_building_display()

    def show_value_from(self):
        if not self.knowledge_or_information_building:
            return None

        return self.knowledge_or_information_building


class Other_utilitarian_public_building(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Other_utilitarian_public_building"
    )
    other_utilitarian_public_building = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "other_utilitarian_public_building"
    _clean_name_spaced = "Other Utilitarian Public Building"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Other_utilitarian_public_building"
        verbose_name_plural = "Other_utilitarian_public_buildings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Other Utilitarian Building"
        notes = NO_DATA.note
        description = "Other utilitarian public buildings..."  # From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.other_utilitarian_public_building:
            return NO_DATA.default

        return self.get_other_utilitarian_public_building_display()

    def show_value_from(self):
        if not self.other_utilitarian_public_building:
            return None

        return self.other_utilitarian_public_building


class Special_purpose_site(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Special_purpose_site")
    special_purpose_site = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "special_purpose_site"
    _clean_name_spaced = "Special Purpose Site"
    _subsection = "Special-purpose Sites"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Special_purpose_site"
        verbose_name_plural = "Special_purpose_sites"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Special Purpose Site"
        notes = NO_DATA.note
        description = "Sites not associated with residential areas. This position is primarily useful for coding archaneologically known societies."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.special_purpose_site:
            return NO_DATA.default

        return self.get_special_purpose_site_display()

    def show_value_from(self):
        if not self.special_purpose_site:
            return None

        return self.special_purpose_site


class Ceremonial_site(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Ceremonial_site")
    ceremonial_site = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "ceremonial_site"
    _clean_name_spaced = "Ceremonial Site"
    _subsection = "Special-purpose Sites"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Ceremonial_site"
        verbose_name_plural = "Ceremonial_sites"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Ceremonial Site"
        notes = NO_DATA.note
        description = "No Description"  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.ceremonial_site:
            return NO_DATA.default

        return self.get_ceremonial_site_display()

    def show_value_from(self):
        if not self.ceremonial_site:
            return None

        return self.ceremonial_site


class Burial_site(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Burial_site")
    burial_site = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "burial_site"
    _clean_name_spaced = "Burial Site"
    _subsection = "Special-purpose Sites"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Burial_site"
        verbose_name_plural = "Burial_sites"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Burial Site"
        notes = NO_DATA.note
        description = "Dissociated from settlement, has monumental features."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.burial_site:
            return NO_DATA.default

        return self.get_burial_site_display()

    def show_value_from(self):
        if not self.burial_site:
            return None

        return self.burial_site


class Trading_emporia(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Trading_emporia")
    trading_emporia = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "trading_emporia"
    _clean_name_spaced = "Trading Emporia"
    _subsection = "Special-purpose Sites"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Trading_emporia"
        verbose_name_plural = "Trading_emporias"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Trading Emporium"
        notes = NO_DATA.note
        description = "Trading settlements characterised by their peripheral locations, on the shore at the edge of a polity, a lack of infrastructure (typically those in Europe contained no churches) and often of a short-lived nature. They include isolated caravanserai along trade routes."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.trading_emporia:
            return NO_DATA.default

        return self.get_trading_emporia_display()

    def show_value_from(self):
        if not self.trading_emporia:
            return None

        return self.trading_emporia


class Enclosure(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Enclosure")
    enclosure = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "enclosure"
    _clean_name_spaced = "Enclosure"
    _subsection = "Special-purpose Sites"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Enclosure"
        verbose_name_plural = "Enclosures"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Enclosure"
        notes = NO_DATA.note
        description = "An 'enclosure' is clearly demarcated special-purpose area. It can be separated from surrounding land by earthworks (including banks or ditches), walls, or fencing. It may be as small as a few meters across, or encompass many hectares. It is non-residential, but could serve numerous purposes, both practical (animal pens) as well as religious and ceremonial."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.enclosure:
            return NO_DATA.default

        return self.get_enclosure_display()

    def show_value_from(self):
        if not self.enclosure:
            return None

        return self.enclosure


class Length_measurement_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Length_measurement_system"
    )
    length_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "length_measurement_system"
    _clean_name_spaced = "Length Measurement System"
    _subsection = "Information"
    _subsubsection = "Measurement System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Length_measurement_system"
        verbose_name_plural = "Length_measurement_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Length Measurement System"
        notes = NO_DATA.note
        description = "Textual evidence of length measurement systems. Measurement units are named in sources."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.length_measurement_system:
            return NO_DATA.default

        return self.get_length_measurement_system_display()

    def show_value_from(self):
        if not self.length_measurement_system:
            return None

        return self.length_measurement_system


class Area_measurement_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Area_measurement_system")
    area_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "area_measurement_system"
    _clean_name_spaced = "Area Measurement System"
    _subsection = "Information"
    _subsubsection = "Measurement System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Area_measurement_system"
        verbose_name_plural = "Area_measurement_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Area Measurement System"
        notes = NO_DATA.note
        description = "Textual evidence of area measurement systems. Measurement units are named in sources."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.area_measurement_system:
            return NO_DATA.default

        return self.get_area_measurement_system_display()

    def show_value_from(self):
        if not self.area_measurement_system:
            return None

        return self.area_measurement_system


class Volume_measurement_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Volume_measurement_system"
    )
    volume_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "volume_measurement_system"
    _clean_name_spaced = "Volume Measurement System"
    _subsection = "Information"
    _subsubsection = "Measurement System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Volume_measurement_system"
        verbose_name_plural = "Volume_measurement_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Volume Measurement System"
        notes = NO_DATA.note
        description = 'Textual evidence of volume measurement systems. Measurement units are named in sources. Archaeological evidence includes finding containers of standard volume, etc. (use "inferred present" in such cases)'  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.volume_measurement_system:
            return NO_DATA.default

        return self.get_volume_measurement_system_display()

    def show_value_from(self):
        if not self.volume_measurement_system:
            return None

        return self.volume_measurement_system


class Weight_measurement_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Weight_measurement_system"
    )
    weight_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "weight_measurement_system"
    _clean_name_spaced = "Weight Measurement System"
    _subsection = "Information"
    _subsubsection = "Measurement System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Weight_measurement_system"
        verbose_name_plural = "Weight_measurement_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Weight Measurement System"
        notes = NO_DATA.note
        description = "Textual evidence of weight measurement systems. Measurement units are named in sources."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.weight_measurement_system:
            return NO_DATA.default

        return self.get_weight_measurement_system_display()

    def show_value_from(self):
        if not self.weight_measurement_system:
            return None

        return self.weight_measurement_system


class Time_measurement_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Time_measurement_system")
    time_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "time_measurement_system"
    _clean_name_spaced = "Time Measurement System"
    _subsection = "Information"
    _subsubsection = "Measurement System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Time_measurement_system"
        verbose_name_plural = "Time_measurement_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Time Measurement System"
        notes = NO_DATA.note
        description = "Textual evidence of time measurement systems. Measurement units are named in sources. A natural unit such as 'day' doesn't qualify. Nor does a vague one like 'season'. Archaeological evidence is a clock (e.g., sundial)",  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.time_measurement_system:
            return NO_DATA.default

        return self.get_time_measurement_system_display()

    def show_value_from(self):
        if not self.time_measurement_system:
            return None
        return self.time_measurement_system


class Geometrical_measurement_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Geometrical_measurement_system"
    )
    geometrical_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "geometrical_measurement_system"
    _clean_name_spaced = "Geometrical Measurement System"
    _subsection = "Information"
    _subsubsection = "Measurement System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Geometrical_measurement_system"
        verbose_name_plural = "Geometrical_measurement_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Geometrical Measurement System"
        notes = NO_DATA.note
        description = "Textual evidence of geometrical measurement systems. Measurement units are named in sources.  For example: degree.",  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.geometrical_measurement_system:
            return NO_DATA.default

        return self.get_geometrical_measurement_system_display()

    def show_value_from(self):
        if not self.geometrical_measurement_system:
            return None

        return self.geometrical_measurement_system


class Other_measurement_system(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Other_measurement_system")
    other_measurement_system = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "other_measurement_system"
    _clean_name_spaced = "Other Measurement System"
    _subsection = "Information"
    _subsubsection = "Measurement System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Other_measurement_system"
        verbose_name_plural = "Other_measurement_systems"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Other Measurement System"
        notes = NO_DATA.note
        description = "Textual evidence of more advanced measurement systems: temperature, force, astronomical",  # noqa: E501 pylint: disable=C0301
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.other_measurement_system:
            return NO_DATA.default

        return self.get_other_measurement_system_display()

    def show_value_from(self):
        if not self.other_measurement_system:
            return None

        return self.other_measurement_system


class Debt_and_credit_structure(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Debt_and_credit_structure"
    )
    debt_and_credit_structure = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "debt_and_credit_structure"
    _clean_name_spaced = "Debt And Credit Structure"
    _subsection = "Information"
    _subsubsection = "Money"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Debt_and_credit_structure"
        verbose_name_plural = "Debt_and_credit_structures"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Debt and Credit Structure"
        notes = NO_DATA.note
        description = "Commercial/market practices that take physical form, e.g. a contract on parchment (not just verbal agreements).",  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.debt_and_credit_structure:
            return NO_DATA.default

        return self.get_debt_and_credit_structure_display()

    def show_value_from(self):
        if not self.debt_and_credit_structure:
            return None

        return self.debt_and_credit_structure


class Store_of_wealth(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Store_of_wealth")
    store_of_wealth = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "store_of_wealth"
    _clean_name_spaced = "Store Of Wealth"
    _subsection = "Information"
    _subsubsection = "Money"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Store_of_wealth"
        verbose_name_plural = "Store_of_wealths"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Store of Wealth"
        notes = NO_DATA.note
        description = "Example: hoard, chest for storing valuables, treasury room. Note for the future: perhaps should separate these into individual variables.",  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.store_of_wealth:
            return NO_DATA.default

        return self.get_store_of_wealth_display()

    def show_value_from(self):
        if not self.store_of_wealth:
            return None

        return self.store_of_wealth


class Source_of_support(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Source_of_support")
    source_of_support = models.CharField(
        max_length=500, choices=SOURCE_OF_SUPPORT_CHOICES
    )

    _clean_name = "source_of_support"
    _clean_name_spaced = "Source Of Support"
    _subsection = "Professions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Source_of_support"
        verbose_name_plural = "Source_of_supports"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Source of Support"
        notes = NO_DATA.note
        description = "possible codes: state salary, governed population, land, none. 'State salary' can be paid either in currency or in kind (e.g., koku of rice). 'Governed population' means that the official directly collects tribute from the population (for example, the 'kormlenie' system in Medieval Russia). 'Land' is when the bureaucrats live off land supplied by the state. 'None' is when the state officials are not compensated (example: in the Republican and Principate Rome the magistrates were wealthy individuals who served without salary, motivated by prestige and social or career advancement).",  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.source_of_support:
            return NO_DATA.default

        return self.get_source_of_support_display()

    def show_value_from(self):
        if not self.source_of_support:
            return None

        return self.source_of_support


class Occupational_complexity(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Occupational_complexity")
    occupational_complexity = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "occupational_complexity"
    _clean_name_spaced = "Occupational Complexity"
    _subsection = "Professions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Occupational_complexity"
        verbose_name_plural = "Occupational_complexies"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Occupational Complexity"
        notes = NO_DATA.note
        description = "No Descriptions in the code book."  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.occupational_complexity:
            return NO_DATA.default

        return self.get_occupational_complexity_display()

    def show_value_from(self):
        if not self.occupational_complexity:
            return None

        return self.occupational_complexity


class Special_purpose_house(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(max_length=100, default="Special_purpose_house")
    special_purpose_house = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "special_purpose_house"
    _clean_name_spaced = "Special Purpose House"
    _subsection = "Specialized Buildings: polity owned"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Special_purpose_house"
        verbose_name_plural = "Special Purpose Houses"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Special Purpose House"
        notes = NO_DATA.note
        description = "A normal house used in a distinctive or special manner. This code reflects differentiation between houses.",  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.special_purpose_house:
            return NO_DATA.default

        return self.get_special_purpose_house_display()

    def show_value_from(self):
        if not self.special_purpose_house:
            return self.special_purpose_house

        return None


class Other_special_purpose_site(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Other_special_purpose_site"
    )
    other_special_purpose_site = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    _clean_name = "other_special_purpose_site"
    _clean_name_spaced = "Other Special Purpose Site"
    _subsection = "Special-purpose Sites"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Other_special_purpose_site"
        verbose_name_plural = "Other Special Purpose Sites"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Other Special Purpose House"
        notes = NO_DATA.note
        description = "Other special-purpose sites."  # From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.other_special_purpose_site:
            return NO_DATA.default

        return self.get_other_special_purpose_site_display()

    def show_value_from(self):
        if not self.other_special_purpose_site:
            return None

        return self.other_special_purpose_site


class Largest_communication_distance(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Largest_communication_distance"
    )
    largest_communication_distance_from = models.IntegerField(
        null=True, blank=True
    )
    largest_communication_distance_to = models.IntegerField(
        null=True, blank=True
    )

    _clean_name = "largest_communication_distance"
    _clean_name_spaced = "Largest Communication Distance"
    _subsection = "Social Scale"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Largest_communication_distance"
        verbose_name_plural = "Largest Communication Distances"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Largest Communication Distance"
        notes = NO_DATA.note
        description = """Distance in kilometers between the capital and the furthest provincial capital. Use the figure for the most direct land and/or sea route that was available.
As an alternative for prehistoric communities, measure the distance between largest quasi-capital and furthest village within the quasi-polity.""",  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if all(
            [
                self.largest_communication_distance_from is not None,
                self.largest_communication_distance_to is not None,
                self.largest_communication_distance_to
                == self.largest_communication_distance_from,
            ]
        ):
            return self.largest_communication_distance_from

        if all(
            [
                self.largest_communication_distance_from is not None,
                self.largest_communication_distance_to is not None,
            ]
        ):
            return f"[{self.largest_communication_distance_from:,} to {self.largest_communication_distance_to:,}]"  # noqa: E501 pylint: disable=C0301

        if self.largest_communication_distance_from is not None:
            return f"[{self.largest_communication_distance_from:,}, ...]"

        if self.largest_communication_distance_to is not None:
            return f"[..., {self.largest_communication_distance_to:,}]"

        return NO_DATA.default

    def show_value_from(self):
        if not self.largest_communication_distance_from:
            return "unknown"

        return self.largest_communication_distance_from

    def show_value_to(self):
        if not self.largest_communication_distance_to:
            return None

        return self.largest_communication_distance_to


class Fastest_individual_communication(SeshatCommon, SCMixIn):
    """ """

    name = models.CharField(
        max_length=100, default="Fastest_individual_communication"
    )
    fastest_individual_communication_from = models.IntegerField(
        null=True, blank=True
    )
    fastest_individual_communication_to = models.IntegerField(
        null=True, blank=True
    )

    _clean_name = "fastest_individual_communication"
    _clean_name_spaced = "Fastest Individual Communication"
    _subsection = "Information"
    _subsubsection = "Postal System"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Fastest_individual_communication"
        verbose_name_plural = "Fastest Individual Communications"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = "Fastest Individual Communication"
        notes = NO_DATA.note
        description = "This is the fastest time (in days) an individual can travel from the capital city to the most outlying provincial capital (if one exists), usually keeping within the boundaries of the polity. This might be by ship, horse, horse relay, or on foot, or a combination.",  # noqa: E501 pylint: disable=C0301  From SC_VAR_DEFS
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if all(
            [
                self.fastest_individual_communication_from is not None,
                self.fastest_individual_communication_to is not None,
                self.fastest_individual_communication_to
                == self.fastest_individual_communication_from,
            ]
        ):
            return self.fastest_individual_communication_from

        if all(
            [
                self.fastest_individual_communication_from is not None,
                self.fastest_individual_communication_to is not None,
            ]
        ):
            return f"[{self.fastest_individual_communication_from:,} to {self.fastest_individual_communication_to:,}]"  # noqa: E501 pylint: disable=C0301

        if self.fastest_individual_communication_from is not None:
            return f"[{self.fastest_individual_communication_from:,}, ...]"

        if self.fastest_individual_communication_to is not None:
            return f"[..., {self.fastest_individual_communication_to:,}]"

        return NO_DATA.default

    def show_value_from(self):
        if not self.fastest_individual_communication_from:
            return "unknown"

        return self.fastest_individual_communication_from

    def show_value_to(self):
        if not self.fastest_individual_communication_to:
            return None

        return self.fastest_individual_communication_to
