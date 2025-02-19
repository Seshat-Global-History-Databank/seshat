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

class RestrictedPolityFilter(SeshatCommonFilter, django_filters.FilterSet):
    """
    A reusable filter that restricts queryset based on allowed polities.
    If the user has 'add_capital' permission, they get the full dataset.
    """

    ALLOWED_POLITIES = [
        "kh_chenla", "pe_wari_emp", "in_kampili_k", "in_kalyani_chalukya_emp",
        "in_hoysala_k", "et_aksum_emp_3", "et_aksum_emp_2", "ni_proto_yoruboid",
        "ni_sokoto", "gm_kaabu_emp"
    ]

    def filter_queryset(self, queryset):
        request = getattr(self, "request", None)  # Access request safely

        # Allow full queryset if user has permission
        if request and request.user.is_authenticated and request.user.has_perm("core.add_capital"):
            return queryset  

        # Otherwise, apply filtering
        return queryset.filter(polity__new_name__in=self.ALLOWED_POLITIES)

class WidespreadReligionFilter(RestrictedPolityFilter):

    class Meta:
        model = Widespread_religion
        fields = {
            "order": ["exact"],
            "degree_of_prevalence": ["exact", "icontains"],
        }


class OfficialReligionFilter(RestrictedPolityFilter):

    class Meta:
        model = Official_religion
        fields = {
        }


class ElitesReligionFilter(RestrictedPolityFilter):

    class Meta:
        model = Elites_religion
        fields = {}


class TheoSyncDifRelFilter(RestrictedPolityFilter):
    class Meta:
        model = Theo_sync_dif_rel
        fields = {
            "coded_value": ["exact"],
        }


class SyncRelPraIndBeliFilter(RestrictedPolityFilter):
    class Meta:
        model = Sync_rel_pra_ind_beli
        fields = {
            "coded_value": ["exact"],
        }


class ReligiousFragmentationFilter(
    RestrictedPolityFilter
):
    class Meta:
        model = Religious_fragmentation
        fields = {
            "coded_value": ["exact"],
        }


class GovVioFreqRelGrpFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_vio_freq_rel_grp
        fields = {
            "coded_value": ["exact"],
        }


class GovResPubWorFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_res_pub_wor
        fields = {
            "coded_value": ["exact"],
        }


class GovResPubProsFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_res_pub_pros
        fields = {
            "coded_value": ["exact"],
        }


class GovResConvFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_res_conv
        fields = {
            "coded_value": ["exact"],
        }


class GovPressConvFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_press_conv
        fields = {
            "coded_value": ["exact"],
        }


class GovResPropOwnForRelGrpFilter(
    RestrictedPolityFilter
):
    class Meta:
        model = Gov_res_prop_own_for_rel_grp
        fields = {
            "coded_value": ["exact"],
        }


class TaxRelAdhActInsFilter(RestrictedPolityFilter):
    class Meta:
        model = Tax_rel_adh_act_ins
        fields = {

        }


class GovOblRelGrpOfcRecoFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_obl_rel_grp_ofc_reco
        fields = {
            "coded_value": ["exact"],
        }


class GovResConsRelBuilFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_res_cons_rel_buil
        fields = {
            "coded_value": ["exact"],
        }


class GovResRelEduFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_res_rel_edu
        fields = {
            "coded_value": ["exact"],
        }


class GovResCirRelLitFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_res_cir_rel_lit
        fields = {
            "coded_value": ["exact"],
        }


class GovDisRelGrpOccFunFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_dis_rel_grp_occ_fun
        fields = {
            "coded_value": ["exact"],
        }


class SocVioFreqRelGrpFilter(RestrictedPolityFilter):
    class Meta:
        model = Soc_vio_freq_rel_grp
        fields = {
            "coded_value": ["exact"],
        }


class SocDisRelGrpOccFunFilter(RestrictedPolityFilter):
    class Meta:
        model = Soc_dis_rel_grp_occ_fun
        fields = {
            "coded_value": ["exact"],
        }


class GovPressConvForAgaFilter(RestrictedPolityFilter):
    class Meta:
        model = Gov_press_conv_for_aga
        fields = {
            "coded_value": ["exact"],
        }
