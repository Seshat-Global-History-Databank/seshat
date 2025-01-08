from django.urls import path

from .models import Widespread_religion, Official_religion, Elites_religion, Theo_sync_dif_rel, Sync_rel_pra_ind_beli, Religious_fragmentation, Gov_vio_freq_rel_grp, Gov_res_pub_wor, Gov_res_pub_pros, Gov_res_conv, Gov_press_conv, Gov_res_prop_own_for_rel_grp, Tax_rel_adh_act_ins, Gov_obl_rel_grp_ofc_reco, Gov_res_cons_rel_buil, Gov_res_rel_edu, Gov_res_cir_rel_lit, Gov_dis_rel_grp_occ_fun, Soc_vio_freq_rel_grp, Soc_dis_rel_grp_occ_fun, Gov_press_conv_for_aga

from .forms import Widespread_religionForm, Official_religionForm, Elites_religionForm,Theo_sync_dif_relForm, Sync_rel_pra_ind_beliForm, Religious_fragmentationForm, Gov_vio_freq_rel_grpForm, Gov_res_pub_worForm, Gov_res_pub_prosForm, Gov_res_convForm, Gov_press_convForm, Gov_res_prop_own_for_rel_grpForm, Tax_rel_adh_act_insForm, Gov_obl_rel_grp_ofc_recoForm, Gov_res_cons_rel_builForm, Gov_res_rel_eduForm, Gov_res_cir_rel_litForm, Gov_dis_rel_grp_occ_funForm, Soc_vio_freq_rel_grpForm, Soc_dis_rel_grp_occ_funForm, Gov_press_conv_for_agaForm



from seshat.apps.general.views import dynamic_create_view, dynamic_update_view,  dynamic_update_view_old, generic_list_view, generic_download, generic_metadata_download, dynamic_detail_view, confirm_delete_view, delete_object_view, delete_object_view

from .var_defs import rt_var_defs


from . import views

model_form_pairs = [
    (Widespread_religion, Widespread_religionForm,'widespread_religion', 'widespread_religion', 'Widespread Religion', "Religious Landscape", None, 'rt'),    
    (Official_religion, Official_religionForm, 'coded_value', 'official_religion', 'Official Religion', "Religious Landscape", None, 'rt'),
    (Elites_religion, Elites_religionForm, 'coded_value', 'elites_religion', 'Elites Religion', "Religious Landscape", None, 'rt'),
    (Theo_sync_dif_rel, Theo_sync_dif_relForm, 'coded_value', 'theo_sync_dif_rel', 'Theological Syncretism Of Different Religions', "Religious Landscape", None, 'rt'),
    (Sync_rel_pra_ind_beli, Sync_rel_pra_ind_beliForm, 'coded_value', 'sync_rel_pra_ind_beli', 'Syncretism Of Religious Practices At The Level Of Individual Believers', "Religious Landscape", None, 'rt'),
    (Religious_fragmentation, Religious_fragmentationForm, 'coded_value', 'religious_fragmentation', 'Religious Fragmentation', "Religious Landscape", None, 'rt'),
    (Gov_vio_freq_rel_grp, Gov_vio_freq_rel_grpForm, 'coded_value', 'gov_vio_freq_rel_grp', 'Frequency Of Governmental Violence Against Religious Groups', "Government Restrictions", None, 'rt'),
    (Gov_res_pub_wor, Gov_res_pub_worForm, 'coded_value', 'gov_res_pub_wor', 'Government Restrictions On Public Worship', "Government Restrictions", None, 'rt'),
    (Gov_res_pub_pros, Gov_res_pub_prosForm, 'coded_value', 'gov_res_pub_pros', 'Government Restrictions On Public Proselytizing', "Government Restrictions", None, 'rt'),
    (Gov_res_conv, Gov_res_convForm, 'coded_value', 'gov_res_conv', 'Government Restrictions On Conversion', "Government Restrictions", None, 'rt'),
    (Gov_press_conv, Gov_press_convForm, 'coded_value', 'gov_press_conv', 'Government Pressure To Convert', "Government Restrictions", None, 'rt'),
    (Gov_res_prop_own_for_rel_grp, Gov_res_prop_own_for_rel_grpForm, 'coded_value', 'gov_res_prop_own_for_rel_grp', 'Government Restrictions On Property Ownership For Adherents Of Any Religious Group', "Government Restrictions", None, 'rt'),
    (Tax_rel_adh_act_ins, Tax_rel_adh_act_insForm, 'coded_value', 'tax_rel_adh_act_ins', 'Taxes Based On Religious Adherence Or On Religious Activities And Institutions', "Government Restrictions", None, 'rt'),
    (Gov_obl_rel_grp_ofc_reco, Gov_obl_rel_grp_ofc_recoForm, 'coded_value', 'gov_obl_rel_grp_ofc_reco', 'Governmental Obligations For Religious Groups To Apply For Official Recognition', "Government Restrictions", None, 'rt'),
    (Gov_res_cons_rel_buil, Gov_res_cons_rel_builForm, 'coded_value', 'gov_res_cons_rel_buil', 'Government Restrictions On Construction Of Religious Buildings', "Government Restrictions", None, 'rt'),
    (Gov_res_rel_edu, Gov_res_rel_eduForm, 'coded_value', 'gov_res_rel_edu', 'Government Restrictions On Religious Education', "Government Restrictions", None, 'rt'),
    (Gov_res_cir_rel_lit, Gov_res_cir_rel_litForm, 'coded_value', 'gov_res_cir_rel_lit', 'Government Restrictions On Circulation Of Religious Literature', "Government Restrictions", None, 'rt'),
    (Gov_dis_rel_grp_occ_fun, Gov_dis_rel_grp_occ_funForm, 'coded_value', 'gov_dis_rel_grp_occ_fun', 'Government Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions', "Government Restrictions", None, 'rt'),
    (Soc_vio_freq_rel_grp, Soc_vio_freq_rel_grpForm, 'coded_value', 'soc_vio_freq_rel_grp', 'Frequency Of Societal Violence Against Religious Groups', "Societal Restrictions", None, 'rt'),
    (Soc_dis_rel_grp_occ_fun, Soc_dis_rel_grp_occ_funForm, 'coded_value', 'soc_dis_rel_grp_occ_fun', 'Societal Discrimination Against Religious Groups Taking Up Certain Occupations Or Functions', "Societal Restrictions", None, 'rt'),
    (Gov_press_conv_for_aga, Gov_press_conv_for_agaForm, 'coded_value', 'gov_press_conv_for_aga', 'Societal Pressure To Convert Or Against Conversion', "Societal Restrictions", None, 'rt'),]


urlpatterns = [
    path('rtvars/', views.rtvars, name='rtvars'),
    path('problematic_rt_data_table/', views.show_problematic_rt_data_table, name='problematic_rt_data_table'),
    path('download-csv-rt-all/', views.download_csv_all_rt,name='download_csv_all_rt'),
    path('download_csv_religious_landscape/', views.download_csv_religious_landscape,name='download_csv_religious_landscape'),
    path('download_csv_government_restrictions/', views.download_csv_government_restrictions,name='download_csv_government_restrictions'),
    path('download_csv_societal_restrictions/', views.download_csv_societal_restrictions,name='download_csv_societal_restrictions'),

    path('get_ref_options/', views.get_ref_options, name='get_ref_options'),
    #  path('download_csv_professions/', views.download_csv_professions,name='download_csv_professions'),
    #  path('download_csv_bureaucracy_characteristics/', views.download_csv_bureaucracy_characteristics,name='download_csv_bureaucracy_characteristics'),
    #  path('download_csv_hierarchical_complexity/', views.download_csv_hierarchical_complexity,name='download_csv_hierarchical_complexity'),
    #  path('download_csv_law/', views.download_csv_law,name='download_csv_law'),
    #  path('download_csv_specialized_buildings_polity_owned/', views.download_csv_specialized_buildings_polity_owned,name='download_csv_specialized_buildings_polity_owned'),
    #  path('download_csv_transport_infrastructure/', views.download_csv_transport_infrastructure,name='download_csv_transport_infrastructure'),
    #  path('download_csv_special_purpose_sites/', views.download_csv_special_purpose_sites,name='download_csv_special_purpose_sites'),
    #  path('download_csv_information/', views.download_csv_information,name='download_csv_information'),
]


# Create URL patterns dynamically for each model-class pair: UPDATE
for model_class, form_class, coded_value, x_name, myvar, sec, subsec, db_section in model_form_pairs:
    urlpatterns.append(
        path(f'{x_name}/updatenew/<int:object_id>/', dynamic_update_view, {
            'form_class': form_class,
            'model_class': model_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': rt_var_defs[myvar.lower().capitalize()],
            'var_section': sec,
            'var_subsection': subsec,
            'delete_url_name': x_name + "-confirm-delete",
        }, name=f'{x_name}-updatenew')
    )
    urlpatterns.append(
        path(f'{x_name}/update/<int:object_id>/', dynamic_update_view_old, {
            'form_class': form_class,
            'model_class': model_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': rt_var_defs[myvar.lower().capitalize()],
            'var_section': sec,
            'var_subsection': subsec,
            'delete_url_name': x_name + "-confirm-delete",
        }, name=f'{x_name}-update')
    )
    urlpatterns.append(
        path(f'{x_name}/create/', dynamic_create_view, {
            'form_class': form_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': rt_var_defs[myvar.lower().capitalize()],
            'var_section': sec,
            'var_subsection': subsec,
        }, name=f'{x_name}-create')
     )
    urlpatterns.append(
        path(f'{x_name}s_all/', generic_list_view, {
            'model_class': model_class,
            'var_name': x_name,
            'coded_value': coded_value,
            'var_name_display': myvar,
            'var_section': sec,
            'var_subsection': subsec,
            'var_main_desc': rt_var_defs[myvar.lower().capitalize()],
        }, name=f'{x_name}s_all')
     )
    urlpatterns.append(
        path(f'{x_name}download/', generic_download, {
            'model_class': model_class,
            'var_name': x_name,
            'x_name': x_name,
            'coded_value': coded_value,
            'db_section': db_section,
        }, name=f'{x_name}-download')
     )
    urlpatterns.append(
        path(f'{x_name}metadownload/', generic_metadata_download, {
            'var_name': x_name,
            'var_name_display': myvar,
            'var_section': sec,
            'var_subsection': subsec,
            'var_main_desc': rt_var_defs[myvar.lower().capitalize()],
        }, name=f'{x_name}-metadownload')
     )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/', dynamic_detail_view, {
          'model_class': model_class,
          'myvar': x_name,
          'var_name_display': myvar,
          'var_section': sec,
          'var_subsection': subsec,
          'db_section': db_section,
        }, name=f'{x_name}-detail')
     )

    urlpatterns.append(
        path(f'{x_name}/<int:pk>/delete/', delete_object_view, {
          'model_class': model_class,
            'var_name': x_name,
        }, name=f'{x_name}-delete')
    )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/confirm-delete/', confirm_delete_view, {
          'model_class': model_class,
            'var_name': x_name,
        }, name=f'{x_name}-confirm-delete')
     )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/delete/', delete_object_view, {
          'model_class': model_class,
            'var_name': x_name,
        }, name=f'{x_name}-delete')
     )

