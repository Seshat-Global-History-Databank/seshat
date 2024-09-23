from django.db import models

from ..core.models import SeshatCommon, Religion
from ..constants import ABSENT_PRESENT_CHOICES
from ..utils import (
    get_model_instance_name,
)

from .constants import FREQUENCY_CHOICES, ORDER_CHOICES, PREVALENCE_CHOICES
from .mixins import RTMixin


class Widespread_religion(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Widespread_religion")
    order = models.CharField(max_length=10, choices=ORDER_CHOICES)
    widespread_religion = models.ForeignKey(
        Religion,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )
    degree_of_prevalence = models.CharField(
        max_length=500, choices=PREVALENCE_CHOICES, null=True, blank=True
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Widespread_religion"
        verbose_name_plural = "Widespread_religions"
        ordering = ["order"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    _clean_name = "widespread_religion"
    _clean_name_spaced = "Widespread Religion"
    _reverse = "widespread_religion-detail"
    _subsection = "Religious Landscape"
    _subsubsection = None

    def clean_name_dynamic(self):
        if self.order == "1":
            return "Most widespread religion"

        if self.order == "2":
            return "Second most widespread religion"

        if self.order == "3":
            return "Third most widespread religion"

        if self.order == "4":
            return "Fourth most widespread religion"

        if self.order == "9":
            return "Other minority religion"

        return "Widespread religion"

    def show_value(self):
        degree_of_prevalence = self.get_degree_of_prevalence_display()
        order_display = self.get_order_display()

        if not self.widespread_religion:
            return " - "

        if not degree_of_prevalence or degree_of_prevalence in [
            "uncoded",
            "unknown",
        ]:
            return f"{order_display}: {self.widespread_religion.religion_name}"

        return f"{order_display}: {self.widespread_religion.religion_name} ({degree_of_prevalence})"  # noqa: E501 pylint: disable=C0301

    def show_value_from(self):
        if not self.widespread_religion:
            return None

        return self.widespread_religion

    def show_value_to(self):
        return None


class Official_religion(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Official_religion")
    coded_value = models.ForeignKey(
        Religion,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Official_religion"
        verbose_name_plural = "Official_religions"

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    _clean_name = "official_religion"
    _clean_name_spaced = "Official Religion"
    _reverse = "official_religion-detail"
    _subsection = "Religious Landscape"
    _subsubsection = None

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.coded_value

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None


class Elites_religion(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Elites_religion")
    coded_value = models.ForeignKey(
        Religion,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Elites_religion"
        verbose_name_plural = "Elites_religions"

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    _clean_name = "elites_religion"
    _clean_name_spaced = "Elites Religion"
    _reverse = "elites_religion-detail"
    _subsection = "Religious Landscape"
    _subsubsection = None

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.coded_value

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None


class Theo_sync_dif_rel(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Theo_sync_dif_rel")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Theo_sync_dif_rel"
        verbose_name_plural = "Theological Syncretism of Different Religionss"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    _clean_name = "theo_sync_dif_rel"
    _clean_name_spaced = "Theological Syncretism of Different Religions"
    _reverse = "theo_sync_dif_rel-detail"
    _subsection = "Religious Landscape"
    _subsubsection = None

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None


class Sync_rel_pra_ind_beli(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Sync_rel_pra_ind_beli")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "sync_rel_pra_ind_beli"
    _clean_name_spaced = (
        "Syncretism of Religious Practices at the Level of Individual Believers"
    )
    _reverse = "sync_rel_pra_ind_beli-detail"
    _subsection = "Religious Landscape"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Sync_rel_pra_ind_beli"
        verbose_name_plural = (
            "Syncretism of Religious Practices at the Level of Individual Believerss"
        )
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None


class Religious_fragmentation(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Religious_fragmentation")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "religious_fragmentation"
    _clean_name_spaced = "Religious Fragmentation"
    _reverse = "religious_fragmentation-detail"
    _subsection = "Religious Landscape"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Religious_fragmentation"
        verbose_name_plural = "Religious Fragmentations"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None


class Gov_vio_freq_rel_grp(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_vio_freq_rel_grp")
    coded_value = models.CharField(max_length=500, choices=FREQUENCY_CHOICES)

    _clean_name = "gov_vio_freq_rel_grp"
    _clean_name_spaced = "Frequency of Governmental Violence Against Religious Groups"
    _reverse = "gov_vio_freq_rel_grp-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_vio_freq_rel_grp"
        verbose_name_plural = (
            "Frequency of Governmental Violence Against Religious Groupss"
        )
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None


class Gov_res_pub_wor(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_res_pub_wor")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_res_pub_wor"
    _clean_name_spaced = "Government Restrictions on Public Worship"
    _reverse = "gov_res_pub_wor-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_res_pub_wor"
        verbose_name_plural = "Government Restrictions on Public Worships"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Gov_res_pub_pros(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_res_pub_pros")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_res_pub_pros"
    _clean_name_spaced = "Government Restrictions on Public Proselytizing"
    _reverse = "gov_res_pub_pros-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_res_pub_pros"
        verbose_name_plural = "Government Restrictions on Public Proselytizings"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Gov_res_conv(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_res_conv")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_res_conv"
    _clean_name_spaced = "Government Restrictions on Conversion"
    _reverse = "gov_res_conv-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_res_conv"
        verbose_name_plural = "Government Restrictions on Conversions"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Gov_press_conv(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_press_conv")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_press_conv"
    _clean_name_spaced = "Government Pressure to Convert"
    _reverse = "gov_press_conv-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_press_conv"
        verbose_name_plural = "Government Pressure to Converts"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Gov_res_prop_own_for_rel_grp(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_res_prop_own_for_rel_grp")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_res_prop_own_for_rel_grp"
    _clean_name_spaced = "Government Restrictions on Property Ownership for Adherents of Any Religious Group"  # noqa: E501 pylint: disable=C0301
    _reverse = "gov_res_prop_own_for_rel_grp-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_res_prop_own_for_rel_grp"
        verbose_name_plural = "Government Restrictions on Property Ownership for Adherents of Any Religious Groups"  # noqa: E501 pylint: disable=C0301
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Tax_rel_adh_act_ins(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Tax_rel_adh_act_ins")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "tax_rel_adh_act_ins"
    _clean_name_spaced = (
        "Taxes Based on Religious Adherence or on Religious Activities and Institutions"
    )
    _reverse = "tax_rel_adh_act_ins-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Tax_rel_adh_act_ins"
        verbose_name_plural = "Taxes Based on Religious Adherence or on Religious Activities and Institutionss"  # noqa: E501   TODO: "Institutionss"?  pylint: disable=C0301
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Gov_obl_rel_grp_ofc_reco(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_obl_rel_grp_ofc_reco")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_obl_rel_grp_ofc_reco"
    _clean_name_spaced = "Governmental Obligations for Religious Groups to Apply for Official Recognition"  # noqa: E501 pylint: disable=C0301
    _reverse = "gov_obl_rel_grp_ofc_reco-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_obl_rel_grp_ofc_reco"
        verbose_name_plural = "Governmental Obligations for Religious Groups to Apply for Official Recognitions"  # noqa: E501 pylint: disable=C0301
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Gov_res_cons_rel_buil(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_res_cons_rel_buil")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_res_cons_rel_buil"
    _clean_name_spaced = (
        "Government Restrictions on Construction of Religious Buildings"
    )
    _reverse = "gov_res_cons_rel_buil-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_res_cons_rel_buil"
        verbose_name_plural = (
            "Government Restrictions on Construction of Religious Buildingss"
        )
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Gov_res_rel_edu(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_res_rel_edu")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_res_rel_edu"
    _clean_name_spaced = "Government Restrictions on Religious Education"
    _reverse = "gov_res_rel_edu-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_res_rel_edu"
        verbose_name_plural = "Government Restrictions on Religious Educations"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Gov_res_cir_rel_lit(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_res_cir_rel_lit")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_res_cir_rel_lit"
    _clean_name_spaced = (
        "Government Restrictions on Circulation of Religious Literature"
    )
    _reverse = "gov_res_cir_rel_lit-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_res_cir_rel_lit"
        verbose_name_plural = (
            "Government Restrictions on Circulation of Religious Literatures"
        )
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Gov_dis_rel_grp_occ_fun(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_dis_rel_grp_occ_fun")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    _clean_name = "gov_dis_rel_grp_occ_fun"
    _clean_name_spaced = "Government Discrimination Against Religious Groups Taking up Certain Occupations or Functions"  # noqa: E501 pylint: disable=C0301
    _reverse = "gov_dis_rel_grp_occ_fun-detail"
    _subsection = "Government Restrictions"
    _subsubsection = None

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_dis_rel_grp_occ_fun"
        verbose_name_plural = "Government Discrimination Against Religious Groups Taking up Certain Occupations or Functionss"  # noqa: E501   TODO: "functionss"?  pylint: disable=C0301
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None

    def __str__(self) -> str:
        return get_model_instance_name(self)


class Soc_vio_freq_rel_grp(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Soc_vio_freq_rel_grp")
    coded_value = models.CharField(max_length=500, choices=FREQUENCY_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Soc_vio_freq_rel_grp"
        verbose_name_plural = "Frequency of Societal Violence Against Religious Groupss"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    _clean_name = "soc_vio_freq_rel_grp"
    _clean_name_spaced = "Frequency of Societal Violence Against Religious Groups"
    _reverse = "soc_vio_freq_rel_grp-detail"
    _subsection = "Societal Restrictions"
    _subsubsection = None

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None


class Soc_dis_rel_grp_occ_fun(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Soc_dis_rel_grp_occ_fun")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Soc_dis_rel_grp_occ_fun"
        verbose_name_plural = "Societal Discrimination Against Religious Groups Taking up Certain Occupations or Functionss"  # noqa: E501   TODO: "Functionss"?  pylint: disable=C0301
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    _clean_name = "soc_dis_rel_grp_occ_fun"
    _clean_name_spaced = "Societal Discrimination Against Religious Groups Taking up Certain Occupations or Functions"  # noqa: E501 pylint: disable=C0301
    _reverse = "soc_dis_rel_grp_occ_fun-detail"
    _subsection = "Societal Restrictions"
    _subsubsection = None

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None


class Gov_press_conv_for_aga(SeshatCommon, RTMixin):
    """ """

    name = models.CharField(max_length=100, default="Gov_press_conv_for_aga")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "Gov_press_conv_for_aga"
        verbose_name_plural = "Societal Pressure to Convert or Against Conversions"
        ordering = ["year_from", "year_to"]

    class Code:
        """
        :noindex:

        ..
            TODO: Create Code for this class
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}

    _clean_name = "gov_press_conv_for_aga"
    _clean_name_spaced = "Societal Pressure to Convert or Against Conversion"
    _reverse = "gov_press_conv_for_aga-detail"
    _subsection = "Societal Restrictions"
    _subsubsection = None

    def show_value(self):
        if not self.coded_value:
            return " - "

        return self.get_coded_value_display()

    def show_value_from(self):
        if not self.coded_value:
            return None

        return self.coded_value

    def show_value_to(self):
        return None
