from django.urls import path

from ..generic_views import (
    GenericConfirmDeleteView,
    GenericCreateView,
    GenericDeleteView,
    GenericDetailView,
    GenericDownloadView,
    GenericListView,
    GenericMetaDownloadView,
    GenericUpdateView,
)

from .forms import (
    Widespread_religionForm,
    Official_religionForm,
    Elites_religionForm,
    Theo_sync_dif_relForm,
    Sync_rel_pra_ind_beliForm,
    Religious_fragmentationForm,
    Gov_vio_freq_rel_grpForm,
    Gov_res_pub_worForm,
    Gov_res_pub_prosForm,
    Gov_res_convForm,
    Gov_press_convForm,
    Gov_res_prop_own_for_rel_grpForm,
    Tax_rel_adh_act_insForm,
    Gov_obl_rel_grp_ofc_recoForm,
    Gov_res_cons_rel_builForm,
    Gov_res_rel_eduForm,
    Gov_res_cir_rel_litForm,
    Gov_dis_rel_grp_occ_funForm,
    Soc_vio_freq_rel_grpForm,
    Soc_dis_rel_grp_occ_funForm,
    Gov_press_conv_for_agaForm,
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
from .constants import VARIABLE_DEFINITIONS

from ..generic_views import (
    GenericMultipleDownloadView,
    VariableView,
    ProblematicDataView,
)
from ..constants import SUBSECTIONS

APP_LABEL = "rt"

urlpatterns = [
    path("rtvars/", VariableView.as_view(app_label=APP_LABEL), name="rtvars"),
    path(
        "problematic_rt_data_table/",
        ProblematicDataView.as_view(
            app_label=APP_LABEL
        ),
        name="problematic_rt_data_table",
    ),
    path(
        "download-csv-rt-all/",
        GenericMultipleDownloadView.as_view(
            app_label=APP_LABEL, prefix="religion_tolerance_data_"
        ),
        name="download_csv_all_rt",
    ),
    path(
        "download_csv_religious_landscape/",
        GenericMultipleDownloadView.as_view(
            app_label=APP_LABEL,
            subsection=SUBSECTIONS.rt.ReligiousLandscape,
            prefix="religion_tolerance_religious_landscape_",
        ),
        name="download_csv_religious_landscape",
    ),
    path(
        "download_csv_government_restrictions/",
        GenericMultipleDownloadView.as_view(
            app_label=APP_LABEL,
            subsection=SUBSECTIONS.rt.GovernmentRestrictions,
            prefix="religion_tolerance_government_restrictions_",
        ),
        name="download_csv_government_restrictions",
    ),
    path(
        "download_csv_societal_restrictions/",
        GenericMultipleDownloadView.as_view(
            app_label=APP_LABEL,
            subsection=SUBSECTIONS.rt.SocietalRestrictions,
            prefix="religion_tolerance_societal_restrictions_",
        ),
        name="download_csv_societal_restrictions",
    ),
]


model_form_pairs = [
    (
        Widespread_religion,
        Widespread_religionForm,
        "widespread_religion",
        "Widespread Religion",
        "Religious Landscape",
        None,
    ),
    (
        Official_religion,
        Official_religionForm,
        "official_religion",
        "Official Religion",
        "Religious Landscape",
        None,
    ),
    (
        Elites_religion,
        Elites_religionForm,
        "elites_religion",
        "Elites Religion",
        "Religious Landscape",
        None,
    ),
    (
        Theo_sync_dif_rel,
        Theo_sync_dif_relForm,
        "theo_sync_dif_rel",
        "Theological Syncretism Of Different Religions",
        "Religious Landscape",
        None,
    ),
    (
        Sync_rel_pra_ind_beli,
        Sync_rel_pra_ind_beliForm,
        "sync_rel_pra_ind_beli",
        "Syncretism Of Religious Practices At The Level Of Individual Believers",
        "Religious Landscape",
        None,
    ),
    (
        Religious_fragmentation,
        Religious_fragmentationForm,
        "religious_fragmentation",
        "Religious Fragmentation",
        "Religious Landscape",
        None,
    ),
    (
        Gov_vio_freq_rel_grp,
        Gov_vio_freq_rel_grpForm,
        "gov_vio_freq_rel_grp",
        "Frequency Of Governmental Violence Against Religious Groups",
        "Government Restrictions",
        None,
    ),
    (
        Gov_res_pub_wor,
        Gov_res_pub_worForm,
        "gov_res_pub_wor",
        "Government Restrictions On Public Worship",
        "Government Restrictions",
        None,
    ),
    (
        Gov_res_pub_pros,
        Gov_res_pub_prosForm,
        "gov_res_pub_pros",
        "Government Restrictions On Public Proselytizing",
        "Government Restrictions",
        None,
    ),
    (
        Gov_res_conv,
        Gov_res_convForm,
        "gov_res_conv",
        "Government Restrictions On Conversion",
        "Government Restrictions",
        None,
    ),
    (
        Gov_press_conv,
        Gov_press_convForm,
        "gov_press_conv",
        "Government Pressure To Convert",
        "Government Restrictions",
        None,
    ),
    (
        Gov_res_prop_own_for_rel_grp,
        Gov_res_prop_own_for_rel_grpForm,
        "gov_res_prop_own_for_rel_grp",
        "Government Restrictions On Property Ownership For Adherents Of Any Religious Group",  # noqa: E501 pylint: disable=C0301
        "Government Restrictions",
        None,
    ),
    (
        Tax_rel_adh_act_ins,
        Tax_rel_adh_act_insForm,
        "tax_rel_adh_act_ins",
        "Taxes Based On Religious Adherence Or On Religious Activities And Institutions",
        "Government Restrictions",
        None,
    ),
    (
        Gov_obl_rel_grp_ofc_reco,
        Gov_obl_rel_grp_ofc_recoForm,
        "gov_obl_rel_grp_ofc_reco",
        "Governmental Obligations For Religious Groups To Apply For Official Recognition",
        "Government Restrictions",
        None,
    ),
    (
        Gov_res_cons_rel_buil,
        Gov_res_cons_rel_builForm,
        "gov_res_cons_rel_buil",
        "Government Restrictions On Construction Of Religious Buildings",
        "Government Restrictions",
        None,
    ),
    (
        Gov_res_rel_edu,
        Gov_res_rel_eduForm,
        "gov_res_rel_edu",
        "Government Restrictions On Religious Education",
        "Government Restrictions",
        None,
    ),
    (
        Gov_res_cir_rel_lit,
        Gov_res_cir_rel_litForm,
        "gov_res_cir_rel_lit",
        "Government Restrictions On Circulation Of Religious Literature",
        "Government Restrictions",
        None,
    ),
    (
        Gov_dis_rel_grp_occ_fun,
        Gov_dis_rel_grp_occ_funForm,
        "gov_dis_rel_grp_occ_fun",
        "Government Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions",  # noqa: E501 pylint: disable=C0301
        "Government Restrictions",
        None,
    ),
    (
        Soc_vio_freq_rel_grp,
        Soc_vio_freq_rel_grpForm,
        "soc_vio_freq_rel_grp",
        "Frequency Of Societal Violence Against Religious Groups",
        "Societal Restrictions",
        None,
    ),
    (
        Soc_dis_rel_grp_occ_fun,
        Soc_dis_rel_grp_occ_funForm,
        "soc_dis_rel_grp_occ_fun",
        "Societal Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions",  # noqa: E501 pylint: disable=C0301
        "Societal Restrictions",
        None,
    ),
    (
        Gov_press_conv_for_aga,
        Gov_press_conv_for_agaForm,
        "gov_press_conv_for_aga",
        "Societal Pressure To Convert Or Against Conversion",
        "Societal Restrictions",
        None,
    ),
]


# Create URL patterns dynamically for each model-class pair
for (
    model_class,
    form_class,
    var_name,
    myvar,
    section,
    subsection,
) in model_form_pairs:
    my_exp = VARIABLE_DEFINITIONS[myvar.lower().capitalize()]

    urlpatterns += [
        path(
            f"{var_name}/update/<int:object_id>/",
            GenericUpdateView.as_view(
                form_class=form_class,
                model_class=model_class,
                var_name=var_name,
                myvar=myvar,
                my_exp=my_exp,
                var_section=section,
                var_subsection=subsection,
                delete_url_name=f"{var_name}-confirm-delete",
                template="rt/rt_update.html",
            ),
            name=f"{var_name}-update",
        ),
        path(
            f"{var_name}/create/",
            GenericCreateView.as_view(
                form_class=form_class,
                var_name=var_name,
                myvar=myvar,
                my_exp=my_exp,
                var_section=section,
                var_subsection=subsection,
                template="rt/rt_create.html",
            ),
            name=f"{var_name}-create",
        ),
        path(
            f"{var_name}/<int:pk>/",
            GenericDetailView.as_view(
                # form_class=form_class,
                model_class=model_class,
                myvar=var_name,
                var_name_display=myvar,
                template="rt/rt_detail.html",
            ),
            name=f"{var_name}-detail",
        ),
        path(
            f"{var_name}s_all/",
            GenericListView.as_view(
                template="rt/rt_list_all.html",
                model_class=model_class,
                var_name=var_name,
                var_name_display=myvar,
                var_section=section,
                var_subsection=subsection,
                var_main_desc=my_exp,
            ),
            name=f"{var_name}s_all",
        ),
        path(
            f"{var_name}download/",
            GenericDownloadView.as_view(
                model_class=model_class,
                var_name=var_name,
                prefix="religion_tolerance_",
            ),
            name=f"{var_name}-download",
        ),
        path(
            f"{var_name}metadownload/",
            GenericMetaDownloadView.as_view(
                model_class=model_class,
                var_name=var_name,
            ),
            name=f"{var_name}-metadownload",
        ),
        path(
            f"{var_name}/<int:pk>/confirm-delete/",
            GenericConfirmDeleteView.as_view(
                model_class=model_class,
                var_name=var_name,
                template="core/confirm_delete.html",
            ),
            name=f"{var_name}-confirm-delete",
        ),
        path(
            f"{var_name}/<int:pk>/delete/",
            GenericDeleteView.as_view(
                model_class=model_class,
                var_name=var_name,
                redirect=f"{var_name}s_all",
            ),
            name=f"{var_name}-delete",
        ),
    ]
