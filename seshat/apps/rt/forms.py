from django import forms

from ..global_constants import (
    _wrap,
    CODED_VALUE_WIDGET,
    COMMON_FIELDS,
    COMMON_LABELS,
    COMMON_WIDGETS,
    ATTRS
)

from .models import (
    Widespread_religion,
    Official_religion,
    Elites_religion,
    Theo_sync_dif_rel,
    Sync_rel_pra_ind_beli,
    Religious_fragmentation,
    Gov_vio_freq_rel_grp,
    Gov_res_pub_wor,
    Gov_res_pub_pros,
    Gov_res_conv,
    Gov_press_conv,
    Gov_res_prop_own_for_rel_grp,
    Tax_rel_adh_act_ins,
    Gov_obl_rel_grp_ofc_reco,
    Gov_res_cons_rel_buil,
    Gov_res_rel_edu,
    Gov_res_cir_rel_lit,
    Gov_dis_rel_grp_occ_fun,
    Soc_vio_freq_rel_grp,
    Soc_dis_rel_grp_occ_fun,
    Gov_press_conv_for_aga,
)


# Add polity + description to COMMON_LABELS
# TODO: Should these be added directly to COMMON_LABELS in global_constants.py?
COMMON_LABELS = dict(
    COMMON_LABELS,
    **{
        "polity": _wrap("Polity"),
        "description": _wrap("Description"),
    }
)


class Widespread_religionForm(forms.ModelForm):
    """
    Form for creating and updating the Widespread_religion model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Widespread_religion
        fields = COMMON_FIELDS + [
            "order",
            "widespread_religion",
            "degree_of_prevalence",
        ]
        labels = dict(
            COMMON_LABELS,
            **{
                "widespread_religion": _wrap("Widespread Religion"),
                "order": _wrap("Order"),
                "degree_of_prevalence": _wrap("Degree of Prevalence"),
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "widespread_religion": forms.Select(
                    attrs={
                        "class": "form-control mb-3 js-example-basic-single",
                        "id": "id_widespread_religion",
                        "name": "widespread_religion",
                    }
                ),
                "order": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "degree_of_prevalence": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Official_religionForm(forms.ModelForm):
    """
    Form for creating and updating creating and updating the Official_religion model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Official_religion
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS, **{"coded_value": _wrap("Official Religion")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "coded_value": forms.Select(
                    attrs={
                        "class": "form-control mb-3 js-example-basic-single",
                        "id": "id_official_religion",
                        "name": "official_religion",
                    }
                )
            }
        )


class Elites_religionForm(forms.ModelForm):
    """
    Form for creating and updating the Elites_religion model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Elites_religion
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS, **{"coded_value": _wrap("Elites' Religion")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "coded_value": forms.Select(
                    attrs={
                        "class": "form-control mb-3 js-example-basic-single",
                        "id": "id_elites_religion",
                        "name": "elites_religion",
                    }
                )
            }
        )


class Theo_sync_dif_relForm(forms.ModelForm):
    """
    Form for creating and updating the Theo_sync_dif_rel model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Theo_sync_dif_rel
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Theological Syncretism Of Different Religions")
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Sync_rel_pra_ind_beliForm(forms.ModelForm):
    """
    Form for creating and updating the syncretism of religious practices at the level of individual believers model.  # noqa: E501 pylint: disable=C0301
    """

    class Meta:
        """
        :noindex:
        """

        model = Sync_rel_pra_ind_beli
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Syncretism Of Religious Practices At The Level Of Individual Believers")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Religious_fragmentationForm(forms.ModelForm):
    """
    Form for creating and updating the Religious_fragmentation model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Religious_fragmentation
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS, **{"coded_value": _wrap("Religious Fragmentation")}
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_vio_freq_rel_grpForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_vio_freq_rel_grp model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_vio_freq_rel_grp
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Frequency Of Governmental Violence Against Religious Groups")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_res_pub_worForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_pub_wor model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_res_pub_wor
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Government Restrictions On Public Worship")
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_res_pub_prosForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_pub_pros model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_res_pub_pros
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Government Restrictions On Public Proselytizing")
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_res_convForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_conv model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_res_conv
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{"coded_value": _wrap("Government Restrictions On Conversion")}
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_press_convForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_press_conv model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_press_conv
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{"coded_value": _wrap("Government Pressure To Convert")}
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_res_prop_own_for_rel_grpForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_prop_own_for_rel_grp model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_res_prop_own_for_rel_grp
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Government Restrictions On Property Ownership For Religious Groups")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Tax_rel_adh_act_insForm(forms.ModelForm):
    """
    Form for creating and updating the Tax_rel_adh_act_ins model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Tax_rel_adh_act_ins
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Taxes Based On Religious Adherence Or On Religious Activities And Institutions")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_obl_rel_grp_ofc_recoForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_obl_rel_grp_ofc_reco model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_obl_rel_grp_ofc_reco
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Governmental Obligations For Religious Groups To Apply For Official Recognition")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_res_cons_rel_builForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_cons_rel_buil model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_res_cons_rel_buil
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Government Restrictions On Construction Of Religious Buildings")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_res_rel_eduForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_rel_edu model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_res_rel_edu
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Government Restrictions On Religious Education")
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_res_cir_rel_litForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_res_cir_rel_lit model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_res_cir_rel_lit
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Government Restrictions On Circulation Of Religious Literature")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_dis_rel_grp_occ_funForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_dis_rel_grp_occ_fun model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_dis_rel_grp_occ_fun
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Government Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Soc_vio_freq_rel_grpForm(forms.ModelForm):
    """
    Form for creating and updating the Soc_vio_freq_rel_grp model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Soc_vio_freq_rel_grp
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Frequency Of Societal Violence Against Religious Groups")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Soc_dis_rel_grp_occ_funForm(forms.ModelForm):
    """
    Form for creating and updating the Soc_dis_rel_grp_occ_fun model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Soc_dis_rel_grp_occ_fun
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Societal Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)


class Gov_press_conv_for_agaForm(forms.ModelForm):
    """
    Form for creating and updating the Gov_press_conv_for_aga model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gov_press_conv_for_aga
        fields = COMMON_FIELDS + ["coded_value"]
        labels = dict(
            COMMON_LABELS,
            **{
                "coded_value": _wrap("Governmental Pressure To Convert Or Against Conversion")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(COMMON_WIDGETS, **CODED_VALUE_WIDGET)
