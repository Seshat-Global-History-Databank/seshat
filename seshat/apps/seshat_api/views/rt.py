from rest_framework import viewsets

from ._mixins import (
    FilterBackends,
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)

from ..filters.rt import (
    WidespreadReligionFilter,
    OfficialReligionFilter,
    ElitesReligionFilter,
    TheoSyncDifRelFilter,
    SyncRelPraIndBeliFilter,
    ReligiousFragmentationFilter,
    GovVioFreqRelGrpFilter,
    GovResPubWorFilter,
    GovResPubProsFilter,
    GovResConvFilter,
    GovPressConvFilter,
    GovResPropOwnForRelGrpFilter,
    TaxRelAdhActInsFilter,
    GovOblRelGrpOfcRecoFilter,
    GovResConsRelBuilFilter,
    GovResRelEduFilter,
    GovResCirRelLitFilter,
    GovDisRelGrpOccFunFilter,
    SocVioFreqRelGrpFilter,
    SocDisRelGrpOccFunFilter,
    GovPressConvForAgaFilter,
)

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


class WidespreadReligionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Widespread Religions.
    """

    model = Widespread_religion
    pagination_class = SeshatAPIPagination
    filterset_class = WidespreadReligionFilter


class OfficialReligionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Official Religions.
    """

    model = Official_religion
    pagination_class = SeshatAPIPagination
    filterset_class = OfficialReligionFilter


class ElitesReligionViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Elites Religions.
    """

    model = Elites_religion
    pagination_class = SeshatAPIPagination
    filterset_class = ElitesReligionFilter


class TheoSyncDifRelViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Theological Syncretism of Different Religions.
    """

    model = Theo_sync_dif_rel
    pagination_class = SeshatAPIPagination
    filterset_class = TheoSyncDifRelFilter


class SyncRelPraIndBeliViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Syncretism of Religious Practices at the Level of Individual Believers.
    """

    model = Sync_rel_pra_ind_beli
    pagination_class = SeshatAPIPagination
    filterset_class = SyncRelPraIndBeliFilter


class ReligiousFragmentationViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Religious Fragmentations.
    """

    model = Religious_fragmentation
    pagination_class = SeshatAPIPagination
    filterset_class = ReligiousFragmentationFilter


class GovVioFreqRelGrpViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Frequency of Governmental Violence Against Religious Groups.
    """

    model = Gov_vio_freq_rel_grp
    pagination_class = SeshatAPIPagination
    filterset_class = GovVioFreqRelGrpFilter


class GovResPubWorViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Government Restrictions on Public Worships.
    """

    model = Gov_res_pub_wor
    pagination_class = SeshatAPIPagination
    filterset_class = GovResPubWorFilter


class GovResPubProsViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Government Restrictions on Public Proselytizings.
    """

    model = Gov_res_pub_pros
    pagination_class = SeshatAPIPagination
    filterset_class = GovResPubProsFilter


class GovResConvViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Government Restrictions on Conversions.
    """

    model = Gov_res_conv
    pagination_class = SeshatAPIPagination
    filterset_class = GovResConvFilter


class GovPressConvViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Government Pressures to Converts.
    """

    model = Gov_press_conv
    pagination_class = SeshatAPIPagination
    filterset_class = GovPressConvFilter


class GovResPropOwnForRelGrpViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Government Restrictions on Property Ownership for Adherents of and Religious Groups.
    """

    model = Gov_res_prop_own_for_rel_grp
    pagination_class = SeshatAPIPagination
    filterset_class = GovResPropOwnForRelGrpFilter


class TaxRelAdhActInsViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Taxes Based on Religious Adherence or on Religious Activities and Institutions.
    """

    model = Tax_rel_adh_act_ins
    pagination_class = SeshatAPIPagination
    filterset_class = TaxRelAdhActInsFilter


class GovOblRelGrpOfcRecoViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Governmental Obligations for Religious Groups to Apply for Official Recognitions.
    """

    model = Gov_obl_rel_grp_ofc_reco
    pagination_class = SeshatAPIPagination
    filterset_class = GovOblRelGrpOfcRecoFilter


class GovResConsRelBuilViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Government Restrictions on Construction of Religious Buildings.
    """

    model = Gov_res_cons_rel_buil
    pagination_class = SeshatAPIPagination
    filterset_class = GovResConsRelBuilFilter


class GovResRelEduViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Government Restrictions on Religious Education.
    """

    model = Gov_res_rel_edu
    pagination_class = SeshatAPIPagination
    filterset_class = GovResRelEduFilter


class GovResCirRelLitViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Government Restrictions on Circulation of Religious Literature.
    """

    model = Gov_res_cir_rel_lit
    pagination_class = SeshatAPIPagination
    filterset_class = GovResCirRelLitFilter


class GovDisRelGrpOccFunViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Government Discrimination Against Religious Groups Taking Up Certain Occupations or Functions.
    """

    model = Gov_dis_rel_grp_occ_fun
    pagination_class = SeshatAPIPagination
    filterset_class = GovDisRelGrpOccFunFilter


class SocVioFreqRelGrpViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Social Violence Against Religious Groups.
    """

    model = Soc_vio_freq_rel_grp
    pagination_class = SeshatAPIPagination
    filterset_class = SocVioFreqRelGrpFilter


class SocDisRelGrpOccFunViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Social Discrimination Against Religious Groups Taking Up Certain Occupations or Functions.
    """

    model = Soc_dis_rel_grp_occ_fun
    pagination_class = SeshatAPIPagination
    filterset_class = SocDisRelGrpOccFunFilter


class GovPressConvForAgaViewSet(
    FilterBackends,
    MixinSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    """
    A viewset for viewing and editing Societal Pressure to Convert or Against Conversions.
    """

    model = Gov_press_conv_for_aga
    pagination_class = SeshatAPIPagination
    filterset_class = GovPressConvForAgaFilter
