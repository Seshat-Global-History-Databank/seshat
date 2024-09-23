from django.db import models
from django.utils.safestring import mark_safe

from ..core.models import SeshatCommon
from ..constants import (
    ABSENT_PRESENT_CHOICES,
    ABSENT_PRESENT_STRING_LIST,
    SECTIONS,
    SUBSECTIONS,
    NO_DATA
)

from .mixins import WFMixIn


BASECLASS = "fw-light text-secondary"  # TODO: Move to global_constants.py/ATTRS_HTML


class Long_wall(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="long_wall")
    long_wall_from = models.IntegerField(blank=True, null=True)
    long_wall_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "long_wall"
        verbose_name_plural = "Long walls"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.MilitaryTechnologies
        variable = "Long Wall"
        notes = "No actual note"
        description = "The absence or presence or height of long walls. (code absent as number zero on the long_wall_from / and for coding  'unknown', keep the long_wall_from and long_wall_to empty and only select the confidence etc.)"  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        null_meaning = "The value is not available."
        inner_variables = {
            "long_wall": {
                "min": None,
                "max": None,
                "scale": None,
                "explanation_source": None,
                "explanation": "The absence or presence or height of long walls for a polity.",  # noqa: E501 pylint: disable=C0301
                "null_meaning": None,
            }
        }
        potential_columns = ["Choices"]

    _clean_name = "long_wall"
    _clean_name_spaced = "Long Wall"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "long_wall-detail"

    def show_value(self):
        if (
            self.long_wall_from is not None
            and self.long_wall_to is not None
            and self.long_wall_to == self.long_wall_from
        ):
            string = f"{self.long_wall_from:,} <span class='{BASECLASS} fs-6'> km</span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if self.long_wall_from is not None and self.long_wall_to is not None:
            string = f"<span class='{BASECLASS}'> [</span>{self.long_wall_from:,} <span class='{BASECLASS}'> to </span> {self.long_wall_to:,}<span class='{BASECLASS}'>] </span> <span class='{BASECLASS} fs-6'> km </span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if self.long_wall_from == 0:
            return "absent"

        if self.long_wall_from is not None:
            string = f"{self.long_wall_from:,} <span class='{BASECLASS} fs-6'> km</span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        if self.long_wall_to is not None:
            string = f"{self.long_wall_to:,} <span class='{BASECLASS} fs-6'> km</span>"  # noqa: E501 pylint: disable=C0301
            return mark_safe(string)

        return "absent"

    def show_value_from(self):
        if self.long_wall_from:
            return self.long_wall_from

        if self.long_wall_from == 0:
            return "absent"

        return "unknown"

    def show_value_to(self):
        if self.long_wall_to is not None:
            return self.long_wall_to

        return None


class Copper(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Copper")
    copper = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Copper"
        verbose_name_plural = "Coppers"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.MilitaryUseOfMetals
        variable = "Copper"
        notes = "No actual note"
        description = "The absence or presence of copper as a military technology used in warfare."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "copper": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of copper for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "copper"
    _clean_name_spaced = "Copper"
    _subsection = SUBSECTIONS.wf.MilitaryUseOfMetals
    _subsubsection = None
    _reverse = "copper-detail"

    def show_value(self):
        if not self.copper:
            return " - "

        return self.get_copper_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Bronze(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Bronze")
    bronze = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Bronze"
        verbose_name_plural = "Bronzes"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.MilitaryUseOfMetals
        variable = "Bronze"
        notes = "No actual note"
        description = "The absence or presence of bronze as a military technology used in warfare. Bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best."  # noqa: E501   # noqa: E501 pylint: disable=C0301  pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "bronze": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of bronze for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "bronze"
    _clean_name_spaced = "Bronze"
    _subsection = SUBSECTIONS.wf.MilitaryUseOfMetals
    _subsubsection = None
    _reverse = "bronze-detail"

    def show_value(self):
        if not self.bronze:
            return " - "

        return self.get_bronze_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Iron(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Iron")
    iron = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Iron"
        verbose_name_plural = "Irons"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.MilitaryUseOfMetals
        variable = ""
        notes = "No actual note"
        description = (
            "The absence or presence of iron as a military technology used in warfare."
        )
        description_source = "NOTHING"
        inner_variables = {
            "iron": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of iron for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "iron"
    _clean_name_spaced = "Iron"
    _subsection = SUBSECTIONS.wf.MilitaryUseOfMetals
    _subsubsection = None
    _reverse = "iron-detail"

    def show_value(self):
        if not self.iron:
            return " - "

        return self.get_iron_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Steel(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Steel")
    steel = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Steel"
        verbose_name_plural = "Steels"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.MilitaryUseOfMetals
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of steel as a military technology used in warfare. Steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "steel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of steel for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "steel"
    _clean_name_spaced = "Steel"
    _subsection = SUBSECTIONS.wf.MilitaryUseOfMetals
    _subsubsection = None
    _reverse = "steel-detail"

    def show_value(self):
        if not self.steel:
            return " - "

        return self.get_steel_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Javelin(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Javelin")
    javelin = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Javelin"
        verbose_name_plural = "Javelins"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Projectiles
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of javelins as a military technology used in warfare. Includes thrown spears."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "javelin": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of javelin for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "javelin"
    _clean_name_spaced = "Javelin"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "javelin-detail"

    def show_value(self):
        if not self.javelin:
            return " - "

        return self.get_javelin_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Atlatl(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Atlatl")
    atlatl = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Atlatl"
        verbose_name_plural = "Atlatls"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Projectiles
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of atlatl as a military technology used in warfare."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "atlatl": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of atlatl for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "atlatl"
    _clean_name_spaced = "Atlatl"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "atlatl-detail"

    def show_value(self):
        if not self.atlatl:
            return " - "

        return self.get_atlatl_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Sling(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Sling")
    sling = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Sling"
        verbose_name_plural = "Slings"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Projectiles
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of slings as a military technology used in warfare."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "sling": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sling for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "sling"
    _clean_name_spaced = "Sling"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "sling-detail"

    def show_value(self):
        if not self.sling:
            return " - "

        return self.get_sling_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Self_bow(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Self_bow")
    self_bow = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Self_bow"
        verbose_name_plural = "Self_bows"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Projectiles
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of self bow as a military technology used in warfare. This is a bow made from a single piece of wood (example: the English/Welsh longbow)."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "self_bow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of self bow for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "self_bow"
    _clean_name_spaced = "Self Bow"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "self_bow-detail"

    def show_value(self):
        if not self.self_bow:
            return " - "

        return self.get_self_bow_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Composite_bow(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Composite_bow")
    composite_bow = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Composite_bow"
        verbose_name_plural = "Composite_bows"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Projectiles
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of composite bow as a military technology used in warfare. This is a bow made from several different materials, usually wood, horn, and sinew. Also known as laminated bow. Recurved bows should be coded here as well, because usually they are composite bows. When there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present)."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "composite_bow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of composite bow for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "composite_bow"
    _clean_name_spaced = "Composite Bow"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "composite_bow-detail"

    def show_value(self):
        if not self.composite_bow:
            return " - "

        return self.get_composite_bow_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Crossbow(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Crossbow")
    crossbow = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Crossbow"
        verbose_name_plural = "Crossbows"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Projectiles
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of crossbow as a military technology used in warfare."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "crossbow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of crossbow for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "crossbow"
    _clean_name_spaced = "Crossbow"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "crossbow-detail"

    def show_value(self):
        if not self.crossbow:
            return " - "

        return self.get_crossbow_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Tension_siege_engine(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Tension_siege_engine")
    tension_siege_engine = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Tension_siege_engine"
        verbose_name_plural = "Tension_siege_engines"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Projectiles
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of tension siege engines as a military technology used in warfare. For example, catapult, onager."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "tension_siege_engine": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of tension siege engine for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "tension_siege_engine"
    _clean_name_spaced = "Tension Siege Engine"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "tension_siege_engine-detail"

    def show_value(self):
        if not self.tension_siege_engine:
            return " - "

        return self.get_tension_siege_engine_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Sling_siege_engine(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Sling_siege_engine")
    sling_siege_engine = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Sling_siege_engine"
        verbose_name_plural = "Sling_siege_engines"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Projectiles
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of sling siege engines as a military technology used in warfare. E.g., trebuchet, innclude mangonels here."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "sling_siege_engine": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sling siege engine for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "sling_siege_engine"
    _clean_name_spaced = "Sling Siege Engine"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "sling_siege_engine-detail"

    def show_value(self):
        if not self.sling_siege_engine:
            return " - "

        return self.get_sling_siege_engine_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Gunpowder_siege_artillery(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Gunpowder_siege_artillery")
    gunpowder_siege_artillery = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gunpowder_siege_artillery"
        verbose_name_plural = "Gunpowder_siege_artilleries"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Projectiles
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of gunpowder siege artillery as a military technology used in warfare. For example, cannon, mortars."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "gunpowder_siege_artillery": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of gunpowder siege artillery for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "gunpowder_siege_artillery"
    _clean_name_spaced = "Gunpowder Siege Artillery"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "gunpowder_siege_artillery-detail"

    def show_value(self):
        if not self.gunpowder_siege_artillery:
            return " - "

        return self.get_gunpowder_siege_artillery_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Handheld_firearm(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Handheld_firearm")
    handheld_firearm = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Handheld_firearm"
        verbose_name_plural = "Handheld_firearms"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.HandheldWeapons
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of handheld firearms as a military technology used in warfare. E.g., muskets, pistols, and rifles."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "handheld_firearm": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of handheld firearm for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "handheld_firearm"
    _clean_name_spaced = "Handheld Firearm"
    _subsection = SUBSECTIONS.wf.Projectiles
    _subsubsection = None
    _reverse = "handheld_firearm-detail"

    def show_value(self):
        if not self.handheld_firearm:
            return " - "

        return self.get_handheld_firearm_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class War_club(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="War_club")
    war_club = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "War_club"
        verbose_name_plural = "War_clubs"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.HandheldWeapons
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of war clubs as a military technology used in warfare. Includes maces."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "war_club": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of war club for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "war_club"
    _clean_name_spaced = "War Club"
    _subsection = SUBSECTIONS.wf.HandheldWeapons
    _subsubsection = None
    _reverse = "war_club-detail"

    def show_value(self):
        if not self.war_club:
            return " - "

        return self.get_war_club_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Battle_axe(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Battle_axe")
    battle_axe = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Battle_axe"
        verbose_name_plural = "Battle_axes"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.HandheldWeapons
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of battle axes as a military technology used in warfare. Axes designed for military use."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "battle_axe": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of battle axe for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "battle_axe"
    _clean_name_spaced = "Battle Axe"
    _subsection = SUBSECTIONS.wf.HandheldWeapons
    _subsubsection = None
    _reverse = "battle_axe-detail"

    def show_value(self):
        if not self.battle_axe:
            return " - "

        return self.get_battle_axe_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Dagger(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Dagger")
    dagger = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Dagger"
        verbose_name_plural = "Daggers"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.HandheldWeapons
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of daggers as a military technology used in warfare. Bladed weapons shorter than 50 cm. Includes knives. Material is not important (coded elsewhere), thus flint daggers should be coded as present."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "dagger": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of dagger for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "dagger"
    _clean_name_spaced = "Dagger"
    _subsection = SUBSECTIONS.wf.HandheldWeapons
    _subsubsection = None
    _reverse = "dagger-detail"

    def show_value(self):
        if not self.dagger:
            return " - "

        return self.get_dagger_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Sword(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Sword")
    sword = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Sword"
        verbose_name_plural = "Swords"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.HandheldWeapons
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of swords as a military technology used in warfare. Bladed weapons longer than 50 cm. A machete is a sword (assuming the blade is probably longer than 50 cm). Material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "sword": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sword for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "sword"
    _clean_name_spaced = "Sword"
    _subsection = SUBSECTIONS.wf.HandheldWeapons
    _subsubsection = None
    _reverse = "sword-detail"

    def show_value(self):
        if not self.sword:
            return " - "

        return self.get_sword_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Spear(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Spear")
    spear = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Spear"
        verbose_name_plural = "Spears"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.HandheldWeapons
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of spears as a military technology used in warfare. Includes lances and pikes. A trident is a spear."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {
            "spear": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of spear for a polity.",
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

    _clean_name = "spear"
    _clean_name_spaced = "Spear"
    _subsection = SUBSECTIONS.wf.HandheldWeapons
    _subsubsection = None
    _reverse = "spear-detail"

    def show_value(self):
        if not self.spear:
            return " - "

        return self.get_spear_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Polearm(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Polearm")
    polearm = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Polearm"
        verbose_name_plural = "Polearms"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.HandheldWeapons
        variable = ""
        notes = "No actual note"
        description = "The absence or presence of polearms as a military technology used in warfare. This category includes halberds, naginatas, and morning stars."  # noqa: E501 pylint: disable=C0301
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "polearm"
    _clean_name_spaced = "Polearm"
    _subsection = SUBSECTIONS.wf.HandheldWeapons
    _subsubsection = None
    _reverse = "polearm-detail"

    def show_value(self):
        if not self.polearm:
            return " - "

        return self.get_polearm_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Dog(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Dog")
    dog = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Dog"
        verbose_name_plural = "Dogs"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "dog"
    _clean_name_spaced = "Dog"
    _subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
    _subsubsection = None
    _reverse = "dog-detail"

    def show_value(self):
        if not self.dog:
            return " - "

        return self.get_dog_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Donkey(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Donkey")
    donkey = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Donkey"
        verbose_name_plural = "Donkeies"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "donkey"
    _clean_name_spaced = "Donkey"
    _subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
    _subsubsection = None
    _reverse = "donkey-detail"

    def show_value(self):
        if not self.donkey:
            return " - "

        return self.get_donkey_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Horse(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Horse")
    horse = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Horse"
        verbose_name_plural = "Horses"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "horse"
    _clean_name_spaced = "Horse"
    _subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
    _subsubsection = None
    _reverse = "horse-detail"

    def show_value(self):
        if not self.horse:
            return " - "

        return self.get_horse_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Camel(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Camel")
    camel = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Camel"
        verbose_name_plural = "Camels"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "camel"
    _clean_name_spaced = "Camel"
    _subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
    _subsubsection = None
    _reverse = "camel-detail"

    def show_value(self):
        if not self.camel:
            return " - "

        return self.get_camel_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Elephant(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Elephant")
    elephant = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Elephant"
        verbose_name_plural = "Elephants"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "elephant"
    _clean_name_spaced = "Elephant"
    _subsection = SUBSECTIONS.wf.AnimalsUsedInWarfare
    _subsubsection = None
    _reverse = "elephant-detail"

    def show_value(self):
        if not self.elephant:
            return " - "

        return self.get_elephant_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Wood_bark_etc(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Wood_bark_etc")
    wood_bark_etc = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Wood_bark_etc"
        verbose_name_plural = "Wood_bark_etcs"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "wood_bark_etc"
    _clean_name_spaced = "Wood Bark Etc"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "wood_bark_etc-detail"

    def show_value(self):
        if not self.wood_bark_etc:
            return " - "

        return self.get_wood_bark_etc_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Leather_cloth(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Leather_cloth")
    leather_cloth = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Leather_cloth"
        verbose_name_plural = "Leather_cloths"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "leather_cloth"
    _clean_name_spaced = "Leather Cloth"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "leather_cloth-detail"

    def show_value(self):
        if not self.leather_cloth:
            return " - "

        return self.get_leather_cloth_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Shield(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Shield")
    shield = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Shield"
        verbose_name_plural = "Shields"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "shield"
    _clean_name_spaced = "Shield"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "shield-detail"

    def show_value(self):
        if not self.shield:
            return " - "

        return self.get_shield_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Helmet(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Helmet")
    helmet = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Helmet"
        verbose_name_plural = "Helmets"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "helmet"
    _clean_name_spaced = "Helmet"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "helmet-detail"

    def show_value(self):
        if not self.helmet:
            return " - "

        return self.get_helmet_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Breastplate(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Breastplate")
    breastplate = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Breastplate"
        verbose_name_plural = "Breastplates"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "breastplate"
    _clean_name_spaced = "Breastplate"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "breastplate-detail"

    def show_value(self):
        if not self.breastplate:
            return " - "

        return self.get_breastplate_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Limb_protection(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Limb_protection")
    limb_protection = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Limb_protection"
        verbose_name_plural = "Limb_protections"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "limb_protection"
    _clean_name_spaced = "Limb Protection"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "limb_protection-detail"

    def show_value(self):
        if not self.limb_protection:
            return " - "

        return self.get_limb_protection_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Scaled_armor(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Scaled_armor")
    scaled_armor = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Scaled_armor"
        verbose_name_plural = "Scaled_armors"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "scaled_armor"
    _clean_name_spaced = "Scaled Armor"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "scaled_armor-detail"

    def show_value(self):
        if not self.scaled_armor:
            return " - "

        return self.get_scaled_armor_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Laminar_armor(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Laminar_armor")
    laminar_armor = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Laminar_armor"
        verbose_name_plural = "Laminar_armors"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "laminar_armor"
    _clean_name_spaced = "Laminar Armor"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "laminar_armor-detail"

    def show_value(self):
        if not self.laminar_armor:
            return " - "

        return self.get_laminar_armor_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Plate_armor(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Plate_armor")
    plate_armor = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Plate_armor"
        verbose_name_plural = "Plate_armors"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "plate_armor"
    _clean_name_spaced = "Plate Armor"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "plate_armor-detail"

    def show_value(self):
        if not self.plate_armor:
            return " - "

        return self.get_plate_armor_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Small_vessels_canoes_etc(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Small_vessels_canoes_etc")
    small_vessels_canoes_etc = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Small_vessels_canoes_etc"
        verbose_name_plural = "Small_vessels_canoes_etcs"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.NavalTechnology
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "small_vessels_canoes_etc"
    _clean_name_spaced = "Small Vessels Canoes Etc"
    _subsection = SUBSECTIONS.wf.NavalTechnology
    _subsubsection = None
    _reverse = "small_vessels_canoes_etc-detail"

    def show_value(self):
        if not self.small_vessels_canoes_etc:
            return " - "

        return self.get_small_vessels_canoes_etc_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Merchant_ships_pressed_into_service(SeshatCommon, WFMixIn):
    name = models.CharField(
        max_length=100, default="Merchant_ships_pressed_into_service"
    )
    merchant_ships_pressed_into_service = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Merchant_ships_pressed_into_service"
        verbose_name_plural = "Merchant_ships_pressed_into_services"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.NavalTechnology
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "merchant_ships_pressed_into_service"
    _clean_name_spaced = "Merchant Ships Pressed Into Service"
    _subsection = SUBSECTIONS.wf.NavalTechnology
    _subsubsection = None
    _reverse = "merchant_ships_pressed_into_service-detail"

    def show_value(self):
        if not self.merchant_ships_pressed_into_service:
            return " - "

        return self.get_merchant_ships_pressed_into_service_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Specialized_military_vessel(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Specialized_military_vessel")
    specialized_military_vessel = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Specialized_military_vessel"
        verbose_name_plural = "Specialized_military_vessels"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.NavalTechnology
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "specialized_military_vessel"
    _clean_name_spaced = "Specialized Military Vessel"
    _subsection = SUBSECTIONS.wf.NavalTechnology
    _subsubsection = None
    _reverse = "specialized_military_vessel-detail"

    def show_value(self):
        if not self.specialized_military_vessel:
            return " - "

        return self.get_specialized_military_vessel_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Settlements_in_a_defensive_position(SeshatCommon, WFMixIn):
    name = models.CharField(
        max_length=100, default="Settlements_in_a_defensive_position"
    )
    settlements_in_a_defensive_position = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Settlements_in_a_defensive_position"
        verbose_name_plural = "Settlements_in_a_defensive_positions"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "settlements_in_a_defensive_position"
    _clean_name_spaced = "Settlements in a Defensive Position"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "settlements_in_a_defensive_position-detail"

    def show_value(self):
        if not self.settlements_in_a_defensive_position:
            return " - "

        return self.get_settlements_in_a_defensive_position_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Wooden_palisade(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Wooden_palisade")
    wooden_palisade = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Wooden_palisade"
        verbose_name_plural = "Wooden_palisades"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "wooden_palisade"
    _clean_name_spaced = "Wooden Palisade"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "wooden_palisade-detail"

    def show_value(self):
        if not self.wooden_palisade:
            return " - "

        return self.get_wooden_palisade_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Earth_rampart(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Earth_rampart")
    earth_rampart = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Earth_rampart"
        verbose_name_plural = "Earth_ramparts"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "earth_rampart"
    _clean_name_spaced = "Earth Rampart"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "earth_rampart-detail"

    def show_value(self):
        if not self.earth_rampart:
            return " - "

        return self.get_earth_rampart_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Ditch(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Ditch")
    ditch = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Ditch"
        verbose_name_plural = "Ditchs"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "ditch"
    _clean_name_spaced = "Ditch"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "ditch-detail"

    def show_value(self):
        if not self.ditch:
            return " - "

        return self.get_ditch_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Moat(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Moat")
    moat = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Moat"
        verbose_name_plural = "Moats"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "moat"
    _clean_name_spaced = "Moat"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "moat-detail"

    def show_value(self):
        if not self.moat:
            return " - "

        return self.get_moat_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Stone_walls_non_mortared(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Stone_walls_non_mortared")
    stone_walls_non_mortared = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Stone_walls_non_mortared"
        verbose_name_plural = "Stone_walls_non_mortareds"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "stone_walls_non_mortared"
    _clean_name_spaced = "Stone Walls Non Mortared"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "stone_walls_non_mortared-detail"

    def show_value(self):
        if not self.stone_walls_non_mortared:
            return " - "

        return self.get_stone_walls_non_mortared_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Stone_walls_mortared(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Stone_walls_mortared")
    stone_walls_mortared = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Stone_walls_mortared"
        verbose_name_plural = "Stone_walls_mortareds"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "stone_walls_mortared"
    _clean_name_spaced = "Stone Walls Mortared"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "stone_walls_mortared-detail"

    def show_value(self):
        if not self.stone_walls_mortared:
            return " - "

        return self.get_stone_walls_mortared_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Fortified_camp(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Fortified_camp")
    fortified_camp = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Fortified_camp"
        verbose_name_plural = "Fortified_camps"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "fortified_camp"
    _clean_name_spaced = "Fortified Camp"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "fortified_camp-detail"

    def show_value(self):
        if not self.fortified_camp:
            return " - "

        return self.get_fortified_camp_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Complex_fortification(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Complex_fortification")
    complex_fortification = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Complex_fortification"
        verbose_name_plural = "Complex_fortifications"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "complex_fortification"
    _clean_name_spaced = "Complex Fortification"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "complex_fortification-detail"

    def show_value(self):
        if not self.complex_fortification:
            return " - "

        return self.get_complex_fortification_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Modern_fortification(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Modern_fortification")
    modern_fortification = models.CharField(
        max_length=500, choices=ABSENT_PRESENT_CHOICES
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Modern_fortification"
        verbose_name_plural = "Modern_fortifications"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Fortifications
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "modern_fortification"
    _clean_name_spaced = "Modern Fortification"
    _subsection = SUBSECTIONS.wf.Fortifications
    _subsubsection = None
    _reverse = "modern_fortification-detail"

    def show_value(self):
        if not self.modern_fortification:
            return " - "

        return self.get_modern_fortification_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name


class Chainmail(SeshatCommon, WFMixIn):
    name = models.CharField(max_length=100, default="Chainmail")
    chainmail = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Chainmail"
        verbose_name_plural = "Chainmails"
        ordering = ["year_from", "year_to"]

    class Code:
        section = SECTIONS.wf
        subsection = SUBSECTIONS.wf.Armor
        variable = ""
        notes = "No actual note"
        description = ""
        description_source = "NOTHING"
        inner_variables = {}

    _clean_name = "chainmail"
    _clean_name_spaced = "Chainmail"
    _subsection = SUBSECTIONS.wf.Armor
    _subsubsection = None
    _reverse = "chainmail-detail"

    def show_value(self):
        if not self.chainmail:
            return " - "

        return self.get_chainmail_display()

    def show_nga(self):
        nga_rel = self.polity.polity_sides.first()

        if not nga_rel:
            return NO_DATA.nga

        return nga_rel.nga_party.name
