from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from ..accounts.models import Seshat_Expert
from ..core.models import SeshatCommon, Polity, Capital
from ..global_constants import (
    POLITY_LANGUAGE_CHOICES,
    POLITY_LANGUAGE_GENUS_CHOICES,
    POLITY_LINGUISTIC_FAMILY_CHOICES,
    SECTIONS,
    SUBSECTIONS,
    STANDARD_SETTINGS
)
from ..global_utils import (
    convert_to_year_span,
    get_model_instance_name,
)

from .mixins import GeneralMixIn
from .constants import (
    POLITY_ALTERNATE_RELIGION_CHOICES,
    POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES,
    POLITY_ALTERNATE_RELIGION_GENUS_CHOICES,
    POLITY_DEGREE_OF_CENTRALIZATION_CHOICES,
    POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES,
    POLITY_RELIGION_CHOICES,
    POLITY_RELIGION_FAMILY_CHOICES,
    POLITY_RELIGION_GENUS_CHOICES,
    POLITY_SUPRAPOLITY_RELATIONS_CHOICES,
    INNER_POLITY_DEGREE_OF_CENTRALIZATION_CHOICES,
    INNER_POLITY_LANGUAGE_GENUS_CHOICES,
    INNER_POLITY_LANGUAGE_CHOICES,
    INNER_POLITY_LINGUISTIC_FAMILY_CHOICES,
    INNER_POLITY_RELIGION_CHOICES,
    INNER_POLITY_RELIGION_FAMILY_CHOICES,
    INNER_POLITY_RELIGION_GENUS_CHOICES,
    INNER_POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES,
    INNER_POLITY_ALTERNATE_RELIGION_CHOICES,
    INNER_POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES,
    INNER_POLITY_ALTERNATE_RELIGION_GENUS_CHOICES,
    INNER_POLITY_SUPRAPOLITY_RELATIONS_CHOICES,
)


BASECLASS = (
    "fw-light text-secondary"  # TODO: Move to global_constants.py/ATTRS_HTML
)


class Polity_research_assistant(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the research assistants
    of the polities.
    """

    name = models.CharField(
        max_length=100, default="Polity_research_assistant"
    )
    polity_ra = models.ForeignKey(
        Seshat_Expert,
        on_delete=models.SET_NULL,
        null=True,
        related_name="seshat_research_assistant",
    )

    _clean_name = "polity_research_assistant"
    _clean_name_spaced = "Polity Research Assistant"
    _subsection = None  # TODO
    _subsubsection = None  # TODO
    _reverse = "polity_research_assistant-detail"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_research_assistant"
        verbose_name_plural = "Polity_research_assistants"
        ordering = ["polity_ra", "year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = "Staff"
        variable = "Polity Research Assistant"
        notes = None
        description = "The RA(s) who worked on a polity."
        description_source = None
        inner_variables = {
            "polity_ra": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The RA of a polity.",
                "units": None,
                "choices": None,
                "null_meaning": None,
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    def show_value(self):
        """
        Return the name of the research assistant (if it exists, otherwise
        return a dash).

        Returns:
            str: The name of the research assistant (or " - " if it does not exist).
        """
        if not self.polity_ra:
            return " - "

        return self.polity_ra


class Polity_original_name(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the original names of the
    polities.
    """

    name = models.CharField(max_length=100, default="Polity_original_name")
    original_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_original_name"
        verbose_name_plural = "Polity_original_names"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Original Name"
        notes = None
        description = "The original name of a polity."
        description_source = None
        inner_variables = {
            "original_name": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The details of original_name.",
                "units": None,
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_original_name"
    _clean_name_spaced = "Polity Original Name"
    _subsection = "Identity and Location"
    _subsubsection = None
    _reverse = "polity_original_name-detail"

    def show_value(self):
        """
        Return the original name (if it exists, otherwise return a dash).

        Returns:
            str: The original name (or " - " if it does not exist).
        """
        if not self.original_name:
            return " - "

        return self.original_name


class Polity_alternative_name(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the alternative names of
    the polities.
    """

    name = models.CharField(max_length=100, default="Polity_alternative_name")
    alternative_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_alternative_name"
        verbose_name_plural = "Polity_alternative_names"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Alternative Name"
        notes = None
        description = "The alternative name of a polity."
        description_source = None
        inner_variables = {
            "alternative_name": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The details of alternative_name.",
                "units": None,
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_alternative_name"
    _clean_name_spaced = "Polity Alternative Name"
    _subsection = "Identity and Location"
    _subsubsection = None
    _reverse = "polity_alternative_name-detail"

    def show_value(self):
        """
        Return the alternative name (if it exists, otherwise return a dash).

        Returns:
            str: The alternative name (or " - " if it does not exist).
        """
        if not self.alternative_name:
            return " - "

        return self.alternative_name


class Polity_duration(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the duration of the
    polities.
    """

    name = models.CharField(max_length=100, default="Polity_duration")
    polity_year_from = models.IntegerField(blank=True, null=True)
    polity_year_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_duration"
        verbose_name_plural = "Polity_durations"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = "Temporal Bounds"
        variable = "Polity Duration"
        notes = None
        description = "The lifetime of a polity."
        description_source = None
        inner_variables = {
            "polity_year_from": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The beginning year for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            },
            "polity_year_to": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The end year for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            },
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_duration"
    _clean_name_spaced = "Polity Duration"
    _subsection = "Temporal Bounds"
    _subsubsection = None
    _reverse = "polity_duration-detail"

    def show_value(self):
        """
        Return the duration of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The duration of the polity (or " - " if it does not exist on the instance).
        """
        year_from = (
            abs(self.polity_year_from) if self.polity_year_from else None
        )
        year_to = abs(self.polity_year_to) if self.polity_year_to else None

        return convert_to_year_span(year_from, year_to)


class Polity_peak_years(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the peak years of the
    polities.
    """

    name = models.CharField(max_length=100, default="Polity_peak_years")
    peak_year_from = models.IntegerField(blank=True, null=True)
    peak_year_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_peak_years"
        verbose_name_plural = "Polity_peak_years"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = "Temporal Bounds"  # noqa: E501   TODO: This one was set to "General" but I changed it to Temporal Bounds because of data found in seshat.apps.general.views.Polity_peak_yearsUpdateView.get_context_data  pylint: disable=C0301
        variable = "Polity Peak Years"
        notes = None
        description = "The peak years of a polity."
        description_source = None
        inner_variables = {
            "peak_year_from": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The beginning of the peak years for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            },
            "peak_year_to": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The end of the peak years for a polity.",
                "units": None,
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            },
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_peak_years"
    _clean_name_spaced = "Polity Peak Years"
    _subsection = "Temporal Bounds"
    _subsubsection = None
    _reverse = "polity_peak_years-detail"

    def show_value(self):
        """
        Return the peak years of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The peak years of the polity (or " - " if it does not exist on the
                instance).
        """
        year_from = abs(self.peak_year_from) if self.peak_year_from else None
        year_to = abs(self.peak_year_to) if self.peak_year_to else None

        return convert_to_year_span(year_from, year_to)


class Polity_degree_of_centralization(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the degree of
    centralization of the polities.
    """

    name = models.CharField(
        max_length=100, default="Polity_degree_of_centralization"
    )
    degree_of_centralization = models.CharField(
        max_length=500, choices=POLITY_DEGREE_OF_CENTRALIZATION_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_degree_of_centralization"
        verbose_name_plural = "Polity_degree_of_centralizations"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Degree of Centralization"
        notes = None
        description = "The degree of centralization of a polity."
        description_source = None
        inner_variables = {
            "degree_of_centralization": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The details of degree_of_centralization.",
                "units": None,
                "choices": INNER_POLITY_DEGREE_OF_CENTRALIZATION_CHOICES,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            }
        }
        null_value = "The value is not available."
        potential_cols = []

    _clean_name = "polity_degree_of_centralization"
    _clean_name_spaced = "Polity Degree of Centralization"
    _subsection = "Political and Cultural Relations"
    _subsubsection = None
    _reverse = "polity_degree_of_centralization-detail"

    def show_value(self):
        """
        Return the degree of centralisation of the polity (if it exists on the
        instance, otherwise return a dash).

        Returns:
            str: The degree of centralisation of the polity (or " - " if it does not exist
                on the instance).
        """
        if not self.degree_of_centralization:
            return " - "

        return self.get_degree_of_centralization_display()


class Polity_suprapolity_relations(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the supra-polity
    relations of the polities.

    Note:
        Be aware that this variable name deviates from the name. Notice
        supra_polity.
    """

    name = models.CharField(
        max_length=100, default="Polity_suprapolity_relations"
    )
    supra_polity_relations = models.CharField(
        max_length=500, choices=POLITY_SUPRAPOLITY_RELATIONS_CHOICES
    )
    other_polity = models.ForeignKey(
        Polity, models.SET_NULL, blank=True, null=True
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_suprapolity_relations"
        verbose_name_plural = "Polity_suprapolity_relations"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = "Political and Cultural Relations"  # noqa: E501   TODO: This was set to "General" but I changed it to "Political and Cultural Relations" because of data found in seshat.apps.general.views.Polity_suprapolity_relationsUpdateView.get_context_data  pylint: disable=C0301
        variable = "Polity Suprapolity Relations"
        notes = None
        description = """The supra polity relations of a polity. <u>Possible Codes</u>: <br> alliance / nominal allegiance / personal union / vassalage / unknown / none <br>
                <br>
                <b>alliance</b> = belongs to a long-term military-political alliance of independent polities ('long-term' refers to more or less permanent relationship between polities extending over multiple years)<br>
                <b>nominal allegiance</b> = same as 'nominal' under the variable "Degree of centralization" but now reflecting the position of the focal polity within the overarching political authority.<br>
                <b>personal union</b> = the focal polity is united with another, or others, as a result of a dynastic marriage.<br>
                <b>vassalage</b> = corresponding to 'loose' category in the Degree of centralization.""",  # noqa: E501 pylint: disable=C0301
        description_source = None
        inner_variables = {
            "supra_polity_relations": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The details of supra polity relations.",
                "units": None,
                "choices": INNER_POLITY_SUPRAPOLITY_RELATIONS_CHOICES,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_suprapolity_relations"
    _clean_name_spaced = "Polity Suprapolity Relations"
    _subsection = "Political and Cultural Relations"
    _subsubsection = None
    _reverse = "polity_suprapolity_relations-detail"

    def display_value(self):
        if self.supra_polity_relations and self.other_polity and self.polity:
            polity_url = reverse("polity-detail-main", args=[self.polity.id])
            other_polity_url = reverse(
                "polity-detail-main", args=[self.other_polity.id]
            )
            return f"<a data-bs-toggle='tooltip' data-bs-html='true' title='{self.polity.long_name}' href='{polity_url}'>{self.polity.new_name}</a> <span class='badge bg-warning text-dark'><i class='fa-solid fa-left-long'></i> {self.get_supra_polity_relations_display()} <i class='fa-solid fa-right-long'></i></span> <a data-bs-toggle='tooltip' data-bs-html='true' title='{self.other_polity.long_name}' href='{other_polity_url}'>{self.other_polity.new_name}</a>"  # noqa: E501 pylint: disable=C0301

        if self.supra_polity_relations == "none":
            return self.get_supra_polity_relations_display()

        if self.supra_polity_relations:
            return f"{self.get_supra_polity_relations_display()} [---]"

        return " - "

    def show_value(self):
        """
        Return the supra polity relations of the polity (if it exists on the
        instance, otherwise return a dash).

        Returns:
            str: The supra polity relations of the polity (or " - " if it does not exist on
                the instance).
        """
        if self.supra_polity_relations and self.other_polity:
            return f"{self.get_supra_polity_relations_display()} [{self.other_polity.new_name}]"  # noqa: E501 pylint: disable=C0301

        if self.supra_polity_relations:
            return self.get_supra_polity_relations_display()

        return " - "


class Polity_utm_zone(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the UTM zone of the
    polities.
    """

    name = models.CharField(max_length=100, default="Polity_utm_zone")
    utm_zone = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_utm_zone"
        verbose_name_plural = "Polity_utm_zones"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Utm Zone"
        notes = None
        description = "The UTM Zone of a polity."  # noqa: E501   TODO: This was set to "The capital of a polity." -- I updated it. OK?  pylint: disable=C0301
        description_source = None
        inner_variables = {
            "capital": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The UTM Zone of a polity.",  # noqa: E501   TODO: This was set to "The capital of a polity." -- I updated it. OK?  pylint: disable=C0301
                "units": None,
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",  # noqa: E501   TODO: This comes from value provided in seshat.apps.general.views.Polity_utm_zoneCreateView.get_context_data. OK?  pylint: disable=C0301
            }
        }
        null_value = "The value is not available."
        potential_cols = []

    _clean_name = "polity_utm_zone"
    _clean_name_spaced = "Polity Utm Zone"
    _subsection = "Identity and Location"
    _subsubsection = None
    _reverse = "polity_utm_zone-detail"

    def show_value(self):
        """
        Return the UTM zone of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The UTM zone of the polity (or " - " if it does not exist on the instance).
        """
        if not self.utm_zone:
            return " - "

        return self.utm_zone


class Polity_capital(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the capitals of the
    polities.
    """

    name = models.CharField(max_length=100, default="Polity_capital")
    capital = models.CharField(max_length=500, blank=True, null=True)
    polity_cap = models.ForeignKey(
        Capital,
        on_delete=models.SET_NULL,
        null=True,
        related_name="polity_caps",
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_capital"
        verbose_name_plural = "Polity_capitals"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Capital"
        notes = ""
        description = "The capital of a polity is connection point between an existing Polity instance and an existing Capital instance. Optionally, year range associations can be specified. If not provided, it implies that the capital remains constant throughout the entire duration of the polity's existence."  # noqa: E501 pylint: disable=C0301
        description_source = None
        inner_variables = {
            "capital": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The capital of a polity.",
                "units": None,
                "choices": None,
                "null_meaning": "This polity did not have a capital.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_capital"
    _clean_name_spaced = "Polity Capital"
    _subsection = "Identity and Location"
    _subsubsection = None
    _reverse = "polity_capital-detail"

    def show_value(self):
        """
        Return the capital of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The capital of the polity (or " - " if it does not exist on the instance).
        """
        if self.polity_cap:
            return self.polity_cap.name

        if self.capital:
            return self.capital

        return get_model_instance_name(self)

    def __str__(self) -> str:
        return self.show_value()


class Polity_language(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the languages of the
    polities.
    """

    name = models.CharField(max_length=100, default="Polity_language")
    language = models.CharField(
        max_length=500, choices=POLITY_LANGUAGE_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_language"
        verbose_name_plural = "Polity_languages"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Language"
        notes = None
        description = "The language of a polity."
        description_source = None
        inner_variables = {
            "language": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The language of a polity.",
                "units": None,
                "choices": INNER_POLITY_LANGUAGE_CHOICES,
                "null_meaning": "This polity did not have a language.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_language"
    _clean_name_spaced = "Polity Language"
    _subsection = "Language"
    _subsubsection = None
    _reverse = "polity_language-detail"

    def show_value(self):
        """
        Return the language of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The language of the polity (or " - " if it does not exist on the instance).
        """
        if not self.language:
            return " - "

        return self.get_language_display()


class Polity_linguistic_family(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the linguistic family
    of the polities.
    """

    name = models.CharField(max_length=100, default="Polity_linguistic_family")
    linguistic_family = models.CharField(
        max_length=500, choices=POLITY_LINGUISTIC_FAMILY_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_linguistic_family"
        verbose_name_plural = "Polity_linguistic_families"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Linguistic Family"
        notes = None
        description = "The linguistic family of a polity."
        description_source = None
        inner_variables = {
            "linguistic_family": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The linguistic family of a polity.",
                "units": None,
                "choices": INNER_POLITY_LINGUISTIC_FAMILY_CHOICES,
                "null_meaning": "This polity did not have a linguistic family.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_linguistic_family"
    _clean_name_spaced = "Polity Linguistic Family"
    _subsection = "Language"
    _subsubsection = None
    _reverse = "polity_linguistic_family-detail"

    def show_value(self):
        """
        Return the linguistic family of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The linguistic family of the polity (or " - " if it does not exist on the
                instance).
        """
        if not self.linguistic_family:
            return " - "

        return self.get_linguistic_family_display()


class Polity_language_genus(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the language genus of the
    polities.
    """

    name = models.CharField(max_length=100, default="Polity_language_genus")
    language_genus = models.CharField(
        max_length=500, choices=POLITY_LANGUAGE_GENUS_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_language_genus"
        verbose_name_plural = "Polity_language_genus"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Language Genus"
        notes = None
        description = "The language genus of a polity."
        description_source = None
        inner_variables = {
            "language_genus": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The language genus of a polity.",
                "units": None,
                "choices": INNER_POLITY_LANGUAGE_GENUS_CHOICES,
                "null_meaning": "This polity did not have a language Genus.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_language_genus"
    _clean_name_spaced = "Polity Language Genus"
    _subsection = "Language"
    _subsubsection = None
    _reverse = "polity_language_genus-detail"

    def show_value(self):
        """
        Return the language genus of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The language genus of the polity (or " - " if it does not exist on the
                instance).
        """
        if not self.language_genus:
            return " - "

        return self.get_language_genus_display()


class Polity_religion_genus(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the religion genus of the
    polities.
    """

    name = models.CharField(max_length=100, default="Polity_religion_genus")
    religion_genus = models.CharField(
        max_length=500, choices=POLITY_RELIGION_GENUS_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_religion_genus"
        verbose_name_plural = "Polity_religion_genus"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Religion Genus"
        notes = None
        description = "The religion genus of a polity."
        description_source = None
        inner_variables = {
            "religion_genus": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The religion genus of a polity.",
                "units": None,
                "choices": INNER_POLITY_RELIGION_GENUS_CHOICES,
                "null_meaning": "This polity did not have a religion genus.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_religion_genus"
    _clean_name_spaced = "Polity Religion Genus"
    _subsection = "Religion"
    _subsubsection = None
    _reverse = "polity_religion_genus-detail"

    def show_value(self):
        """
        Return the religion genus of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The religion genus of the polity (or " - " if it does not exist on the
                instance).
        """
        if not self.religion_genus:
            return " - "

        return self.get_religion_genus_display()


class Polity_religion_family(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the religion family of the
    """

    name = models.CharField(max_length=100, default="Polity_religion_family")
    religion_family = models.CharField(
        max_length=500, choices=POLITY_RELIGION_FAMILY_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_religion_family"
        verbose_name_plural = "Polity_religion_families"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Religion Family"
        notes = ""
        description = "The religion family of a polity."
        description_source = None
        inner_variables = {
            "religion_family": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The religion family of a polity.",
                "units": None,
                "choices": INNER_POLITY_RELIGION_FAMILY_CHOICES,
                "null_meaning": "This polity did not have a religion family.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_religion_family"
    _clean_name_spaced = "Polity Religion Family"
    _subsection = "Religion"
    _subsubsection = None
    _reverse = "polity_religion_family-detail"

    def show_value(self):
        """
        Return the religion family of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The religion family of the polity (or " - " if it does not exist on the
                instance).
        """
        if not self.religion_family:
            return " - "

        return self.get_religion_family_display()


class Polity_religion(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the religion of the
    polities.
    """

    name = models.CharField(max_length=100, default="Polity_religion")
    religion = models.CharField(
        max_length=500, choices=POLITY_RELIGION_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_religion"
        verbose_name_plural = "Polity_religions"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Religion"
        notes = None
        description = "The religion of a polity."
        description_source = None
        inner_variables = {
            "religion": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The religion of a polity.",
                "units": None,
                "choices": INNER_POLITY_RELIGION_CHOICES,
                "null_meaning": "This polity did not have a religion.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_religion"
    _clean_name_spaced = "Polity Religion"
    _subsection = "Religion"
    _subsubsection = None
    _reverse = "polity_religion-detail"

    def show_value(self):
        """
        Return the religion of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The religion of the polity (or " - " if it does not exist on the instance).
        """
        if not self.religion:
            return " - "

        return self.get_religion_display()


class Polity_relationship_to_preceding_entity(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the relationship of the
    polities to their preceding entities.
    """

    name = models.CharField(
        max_length=100, default="Polity_relationship_to_preceding_entity"
    )
    relationship_to_preceding_entity = models.CharField(
        max_length=500, choices=POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_relationship_to_preceding_entity"
        verbose_name_plural = "Polity_relationship_to_preceding_entities"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Relationship to Preceding Entity"
        notes = None
        description = "The polity relationship to preceding (quasi)polity."
        description_source = None
        inner_variables = {
            "relationship_to_preceding_entity": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The polity relationship to preceding (quasi)polity",
                "units": None,
                "choices": INNER_POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES,
                "null_meaning": "This polity did not have a relationship to preceding (quasi)polity",  # noqa: E501 pylint: disable=C0301
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_relationship_to_preceding_entity"
    _clean_name_spaced = "Polity Relationship to Preceding Entity"
    _subsection = "Political and Cultural Relations"
    _subsubsection = None
    _reverse = "polity_relationship_to_preceding_entity-detail"

    def show_value(self):
        """
        Return the polity's relationship to the preceding entity (if it exists
        on the instance, otherwise return a dash).

        Returns:
            str: The polity's relationship to the preceding entity (or " - " if it does not
                exist on the instance).
        """
        if not self.relationship_to_preceding_entity:
            return " - "

        return self.get_relationship_to_preceding_entity_display()


class Polity_preceding_entity(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the preceding entities of
    the polities.
    """

    name = models.CharField(max_length=100, default="Polity_preceding_entity")
    merged_old_data = models.CharField(max_length=1000, blank=True, null=True)
    relationship_to_preceding_entity = models.CharField(
        max_length=500,
        choices=POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES,
        blank=True,
        null=True,
    )
    preceding_entity = models.CharField(max_length=500, blank=True, null=True)
    other_polity = models.ForeignKey(
        Polity, models.SET_NULL, blank=True, null=True
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_preceding_entity"
        verbose_name_plural = "Polity_preceding_entities"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Preceding Entity"
        notes = None
        description = "The preceding entity of a polity."
        description_source = None
        inner_variables = {
            "preceding_entity": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The preceding entity (or the largest settlement) of a polity.",
                "units": None,
                "choices": None,
                "null_meaning": "This polity did not have a preceding entity.",
            }
        }

    _clean_name = "polity_preceding_entity"
    _clean_name_spaced = "Polity Preceding Entity"
    _subsection = "Political and Cultural Relations"
    _subsubsection = None
    _reverse = "polity_preceding_entity-detail"

    def display_value(self):
        """
        Depending on the instance, return a HTML string with information about
        the instance's other_polity attribute and its relationship to its
        preceding entity, the preceding entity (if it exists) or a dash if the
        preceding entity does not exist on the instance.

        Returns:
            str: A string representation of the instance's other_polity/preceding entity
                relationship or a dash if the preceding entity does not exist on the
                instance.
        """
        if self.preceding_entity and self.other_polity and self.polity:
            polity_url = reverse("polity-detail-main", args=[self.polity.id])
            other_polity_url = reverse(
                "polity-detail-main", args=[self.other_polity.id]
            )
            return f"<a data-bs-toggle='tooltip' data-bs-html='true' title='{self.other_polity.long_name}' href='{other_polity_url}'>{self.other_polity.new_name}</a> <span class='badge bg-secondary text-white'> {self.relationship_to_preceding_entity} &nbsp;&nbsp;<i class='fa-solid fa-right-long'></i></span> <a data-bs-toggle='tooltip' data-bs-html='true' title='{self.polity.long_name}' href='{polity_url}'>{self.polity.new_name}</a>"  # noqa: E501 pylint: disable=C0301

        if self.preceding_entity == "none":
            return self.preceding_entity

        if self.preceding_entity:
            return f"{self.preceding_entity} [---]"

        return " - "

    def show_value(self):
        """
        Return the polity's preceding entity, its long name, and its new name
        (if it exists on the instance, otherwise, if there's a preceding entity,
        return its name, otherwise return a dash).

        Returns:
            str: A string representation of polity's preceding entity (or " - " if it does
                not exist on the instance).
        """
        if self.preceding_entity and self.polity and self.other_polity:
            return f"{self.preceding_entity} [{self.other_polity.new_name}] ---> {self.polity.long_name} [{self.polity.new_name}]"  # noqa: E501 pylint: disable=C0301

        if self.preceding_entity and self.polity:
            return self.preceding_entity

        if self.preceding_entity:
            return self.preceding_entity

        return " - "


class Polity_succeeding_entity(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the succeeding entities of
    the polities.
    """

    name = models.CharField(max_length=100, default="Polity_succeeding_entity")
    succeeding_entity = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_succeeding_entity"
        verbose_name_plural = "Polity_succeeding_entities"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Succeeding Entity"
        notes = None
        description = "The succeeding entity of a polity."
        description_source = None
        inner_variables = {
            "succeeding_entity": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The succeeding entity (or the largest settlement) of a polity.",
                "units": None,
                "choices": None,
                "null_meaning": "This polity did not have a succeeding entity.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_succeeding_entity"
    _clean_name_spaced = "Polity Succeeding Entity"
    _subsection = "Political and Cultural Relations"
    _subsubsection = None
    _reverse = "polity_succeeding_entity-detail"

    def show_value(self):
        """
        Return the succeeding entity of the polity (if it exists on the
        instance, otherwise return a dash).

        Returns:
            str: The succeeding entity of the polity (or " - " if it does not exist on the
                instance).
        """
        if not self.succeeding_entity:
            return " - "

        return self.succeeding_entity


class Polity_supracultural_entity(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the supracultural entity of
    the polities.
    """

    name = models.CharField(
        max_length=100, default="Polity_supracultural_entity"
    )
    supracultural_entity = models.CharField(
        max_length=500, blank=True, null=True
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_supracultural_entity"
        verbose_name_plural = "Polity_supracultural_entities"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Supracultural Entity"
        notes = None
        description = "The supracultural entity of a polity."
        description_source = None
        inner_variables = {
            "supracultural_entity": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The supracultural entity (or the largest settlement) of a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": None,
                "null_meaning": "This polity did not have a supracultural entity.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_supracultural_entity"
    _clean_name_spaced = "Polity Supracultural Entity"
    _subsection = "Political and Cultural Relations"
    _subsubsection = None
    _reverse = "polity_supracultural_entity-detail"

    def show_value(self):
        """
        Return the supracultural entity of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The supracultural entity of the polity (or " - " if it does not exist on
                the instance).
        """
        if not self.supracultural_entity:
            return " - "

        return self.supracultural_entity


class Polity_scale_of_supracultural_interaction(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the scale of supracultural
    interaction of the polities.
    """

    name = models.CharField(
        max_length=100, default="Polity_scale_of_supracultural_interaction"
    )
    scale_from = models.IntegerField(blank=True, null=True)
    scale_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_scale_of_supracultural_interaction"
        verbose_name_plural = "Polity_scale_of_supracultural_interactions"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Scale of Supracultural Interaction"
        notes = None
        description = "The scale_of_supra_cultural_interaction of a polity."
        description_source = None
        inner_variables = {
            "scale_from": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The lower scale of supra cultural interactionfor a polity.",
                "units": "km squared",
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            },
            "scale_to": {
                "min": 0,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The upper scale of supra cultural interactionfor a polity.",
                "units": "km squared",
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            },
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_scale_of_supracultural_interaction"
    _clean_name_spaced = "Polity Scale of Supracultural Interaction"
    _subsection = "Political and Cultural Relations"
    _subsubsection = None
    _reverse = "polity_scale_of_supracultural_interaction-detail"

    def show_value(self):
        """
        Return the polity's scale of supracultural interaction (if it exists
        on the instance, otherwise return a dash).

        Returns:
            str: The supracultural interaction of the polity (or " - " if it does not exist
                on the instance).
        """
        if all(
            [self.scale_from, self.scale_to, self.scale_to == self.scale_from]
        ):
            string = f"{self.scale_from:,} <span class='{BASECLASS} fs-6'> km<sup>2</sup></span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if self.scale_from and self.scale_to:
            string = f"<span class='{BASECLASS}'> [</span>{self.scale_from:,} <span class='{BASECLASS}'> to </span> {self.scale_to:,}<span class='{BASECLASS}'>] </span> <span class='{BASECLASS} fs-6'> km<sup>2</sup></span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if self.scale_from:
            return f"[{self.scale_from:,}"

        if self.scale_to:
            return f"[{self.scale_to:,}"

        return " - "


class Polity_alternate_religion_genus(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the alternate religion genus
    of the polities.
    """

    name = models.CharField(
        max_length=100, default="Polity_alternate_religion_genus"
    )
    alternate_religion_genus = models.CharField(
        max_length=500, choices=POLITY_ALTERNATE_RELIGION_GENUS_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_alternate_religion_genus"
        verbose_name_plural = "Polity_alternate_religion_genus"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Alternate Religion Genus"
        notes = None
        description = "The alternate religion genus of a polity."
        description_source = None
        inner_variables = {
            "alternate_religion_genus": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The alternate religion genus of a polity.",
                "units": None,
                "choices": INNER_POLITY_ALTERNATE_RELIGION_GENUS_CHOICES,
                "null_meaning": "This polity did not have a alternatereligion genus.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_alternate_religion_genus"
    _clean_name_spaced = "Polity Alternate Religion Genus"
    _subsection = "Religion"
    _subsubsection = None
    _reverse = "polity_alternate_religion_genus-detail"

    def show_value(self):
        """
        Return the alternate religion genus of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The alternate religion genus of the polity (or " - " if it does not exist
                on the instance).
        """
        if not self.alternate_religion_genus:
            return " - "

        return self.get_alternate_religion_genus_display()


class Polity_alternate_religion_family(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the alternate religion family
    of the polities.
    """

    name = models.CharField(
        max_length=100, default="Polity_alternate_religion_family"
    )
    alternate_religion_family = models.CharField(
        max_length=500, choices=POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES
    )

    _clean_name = "polity_alternate_religion_family"
    _clean_name_spaced = "Polity Alternate Religion Family"
    _subsection = "Religion"
    _subsubsection = None
    _reverse = "polity_alternate_religion_family-detail"

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_alternate_religion_family"
        verbose_name_plural = "Polity_alternate_religion_families"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Alternate Religion Family"
        notes = None
        description = "The alternate religion family of a polity."
        description_source = None
        inner_variables = {
            "alternate_religion_family": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The alternate religion family of a polity.",
                "units": None,
                "choices": INNER_POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES,
                "null_meaning": "This polity did not have a alternate religion family.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    def show_value(self):
        """
        Return the alternate religion family of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The alternate religion family of the polity (or " - " if it does not exist
                on the instance).
        """
        if not self.alternate_religion_family:
            return " - "

        return self.get_alternate_religion_family_display()


class Polity_alternate_religion(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the alternate religion of
    the polities.
    """

    name = models.CharField(
        max_length=100, default="Polity_alternate_religion"
    )
    alternate_religion = models.CharField(
        max_length=500, choices=POLITY_ALTERNATE_RELIGION_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_alternate_religion"
        verbose_name_plural = "Polity_alternate_religions"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Alternate Religion"
        notes = None
        description = "The alternate religion of a polity."
        description_source = None
        inner_variables = {
            "alternate_religion": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The alternate religion of a polity.",
                "units": None,
                "choices": INNER_POLITY_ALTERNATE_RELIGION_CHOICES,
                "null_meaning": "This polity did not have a alternate religion .",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_alternate_religion"
    _clean_name_spaced = "Polity Alternate Religion"
    _subsection = "Religion"
    _subsubsection = None
    _reverse = "polity_alternate_religion-detail"

    def show_value(self):
        """
        Return the alternate religion of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The alternate religion of the polity (or " - " if it does not exist on the
                instance).
        """
        if not self.alternate_religion:
            return " - "

        return self.get_alternate_religion_display()


class Polity_expert(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the experts of the polities.
    """

    name = models.CharField(max_length=100, default="Polity_expert")
    expert = models.ForeignKey(
        Seshat_Expert,
        on_delete=models.SET_NULL,
        null=True,
        related_name="seshat_expert",
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_expert"
        verbose_name_plural = "Polity_experts"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Expert"
        notes = None
        description = "The expert of a polity."
        description_source = None
        inner_variables = {
            "expert": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The expert of a polity.",
                "units": None,
                "choices": None,
                "null_meaning": "This polity did not have an expert.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_expert"
    _clean_name_spaced = "Polity Expert"
    _subsection = None  # TODO
    _subsubsection = None  # TODO
    _reverse = "polity_expert-detail"

    def show_value(self):
        """
        Return the expert of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The expert of the polity (or " - " if it does not exist on the instance).
        """
        if not self.expert:
            return " - "

        return self.expert


class Polity_editor(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the editors of the polities.
    """

    name = models.CharField(max_length=100, default="Polity_editor")
    editor = models.ForeignKey(
        Seshat_Expert,
        on_delete=models.SET_NULL,
        null=True,
        related_name="seshat_editor",
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_editor"
        verbose_name_plural = "Polity_editors"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Editor"
        notes = None
        description = "The editor of a polity."
        description_source = None
        inner_variables = {
            "editor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The editor of a polity.",
                "units": None,
                "choices": None,
                "null_meaning": "This polity did not have an editor.",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_editor"
    _clean_name_spaced = "Polity Editor"
    _subsection = None  # TODO
    _subsubsection = None  # TODO
    _reverse = "polity_editor-detail"

    def show_value(self):
        """
        Return the editor of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The editor of the polity (or " - " if it does not exist on the instance).
        """
        if not self.editor:
            return " - "

        return self.editor


class Polity_religious_tradition(SeshatCommon, GeneralMixIn):
    """
    This model is used to store the information about the religious tradition of
    the polities.
    """

    name = models.CharField(
        max_length=100, default="Polity_religious_tradition"
    )
    religious_tradition = models.CharField(
        max_length=500, blank=True, null=True
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polity_religious_tradition"
        verbose_name_plural = "Polity_religious_traditions"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:
        """

        section = SECTIONS.general
        subsection = SUBSECTIONS.general.General
        variable = "Polity Religious Tradition"
        notes = None
        description = "The details of religious traditions."
        description_source = None
        inner_variables = {
            "religious_tradition": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The details of religious traditions.",
                "units": None,
                "choices": None,
                "null_meaning": "No_Value_Provided_in_Old_Wiki",
            }
        }
        null_meaning = STANDARD_SETTINGS.null_meaning
        potential_cols = []

    _clean_name = "polity_religious_tradition"
    _clean_name_spaced = "Polity Religious Tradition"
    _subsection = "Religion"
    _subsubsection = None
    _reverse = "polity_religious_tradition-detail"

    def show_value(self):
        """
        Return the religious tradition of the polity (if it exists on the instance,
        otherwise return a dash).

        Returns:
            str: The religious tradition of the polity (or " - " if it does not exist on
                the instance).
        """
        if not self.religious_tradition:
            return " - "

        return self.religious_tradition
