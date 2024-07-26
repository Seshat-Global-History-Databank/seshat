from ..models import (
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

from django_filters import rest_framework as django_filters
from ._mixins import SeshatCommonFilter


class WidespreadReligionFilter(SeshatCommonFilter, django_filters.FilterSet):
    # <> widespread_religion [Religion]

    class Meta:
        model = Widespread_religion
        fields = {
            "order": ["exact"],
            "degree_of_prevalence": ["exact", "icontains"],
        }


class OfficialReligionFilter(SeshatCommonFilter, django_filters.FilterSet):
    # <> coded_value [Religion]

    class Meta:
        model = Official_religion
        fields = {
        }


class ElitesReligionFilter(SeshatCommonFilter, django_filters.FilterSet):
    # <> coded_value [Religion]

    class Meta:
        model = Elites_religion
        fields = {}


class TheoSyncDifRelFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Theo_sync_dif_rel
        fields = {
            "coded_value": ["exact"],
        }


class SyncRelPraIndBeliFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Sync_rel_pra_ind_beli
        fields = {
            "coded_value": ["exact"],
        }


class ReligiousFragmentationFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Religious_fragmentation
        fields = {
            "coded_value": ["exact"],
        }


class GovVioFreqRelGrpFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_vio_freq_rel_grp
        fields = {
            "coded_value": ["exact"],
        }


class GovResPubWorFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_res_pub_wor
        fields = {
            "coded_value": ["exact"],
        }


class GovResPubProsFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_res_pub_pros
        fields = {
            "coded_value": ["exact"],
        }


class GovResConvFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_res_conv
        fields = {
            "coded_value": ["exact"],
        }


class GovPressConvFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_press_conv
        fields = {
            "coded_value": ["exact"],
        }


class GovResPropOwnForRelGrpFilter(
    SeshatCommonFilter, django_filters.FilterSet
):
    class Meta:
        model = Gov_res_prop_own_for_rel_grp
        fields = {
            "coded_value": ["exact"],
        }


class TaxRelAdhActInsFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Tax_rel_adh_act_ins
        fields = {

        }


class GovOblRelGrpOfcRecoFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_obl_rel_grp_ofc_reco
        fields = {
            "coded_value": ["exact"],
        }


class GovResConsRelBuilFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_res_cons_rel_buil
        fields = {
            "coded_value": ["exact"],
        }


class GovResRelEduFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_res_rel_edu
        fields = {
            "coded_value": ["exact"],
        }


class GovResCirRelLitFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_res_cir_rel_lit
        fields = {
            "coded_value": ["exact"],
        }


class GovDisRelGrpOccFunFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_dis_rel_grp_occ_fun
        fields = {
            "coded_value": ["exact"],
        }


class SocVioFreqRelGrpFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Soc_vio_freq_rel_grp
        fields = {
            "coded_value": ["exact"],
        }


class SocDisRelGrpOccFunFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Soc_dis_rel_grp_occ_fun
        fields = {
            "coded_value": ["exact"],
        }


class GovPressConvForAgaFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = Gov_press_conv_for_aga
        fields = {
            "coded_value": ["exact"],
        }
