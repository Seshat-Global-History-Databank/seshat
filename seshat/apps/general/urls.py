from .models import Polity_research_assistant, Polity_utm_zone, Polity_original_name, Polity_alternative_name, Polity_peak_years, Polity_duration, Polity_degree_of_centralization, Polity_suprapolity_relations, Polity_capital, Polity_language, Polity_linguistic_family, Polity_language_genus, Polity_religion_genus, Polity_religion_family, Polity_religion, Polity_relationship_to_preceding_entity, Polity_preceding_entity, Polity_succeeding_entity, Polity_supracultural_entity, Polity_scale_of_supracultural_interaction, Polity_alternate_religion_genus, Polity_alternate_religion_family, Polity_alternate_religion, Polity_expert, Polity_editor, Polity_religious_tradition

from .forms import Polity_utm_zoneForm, Polity_original_nameForm, Polity_alternative_nameForm, Polity_peak_yearsForm, Polity_durationForm, Polity_degree_of_centralizationForm, Polity_suprapolity_relationsForm, Polity_capitalForm, Polity_languageForm, Polity_linguistic_familyForm, Polity_language_genusForm, Polity_religion_genusForm, Polity_religion_familyForm, Polity_religionForm, Polity_relationship_to_preceding_entityForm, Polity_preceding_entityForm, Polity_succeeding_entityForm, Polity_supracultural_entityForm, Polity_scale_of_supracultural_interactionForm, Polity_alternate_religion_genusForm, Polity_alternate_religion_familyForm, Polity_alternate_religionForm, Polity_religious_traditionForm

from django.urls import path
from .var_defs import general_var_defs

from . import views

urlpatterns = [
    path('generalvars/', views.generalvars, name='generalvars'),
    path('download-csv-general-all/', views.download_csv_all_general,name='download_csv_all_general'),
]


#####################
model_form_pairs = [
(Polity_utm_zone, Polity_utm_zoneForm, 'polity_utm_zone', 'utm_zone', 'Polity Utm Zone', 'Identity and Location', None, 'general'),
(Polity_original_name, Polity_original_nameForm, 'polity_original_name', 'original_name', 'Polity Original Name', 'Identity and Location', None, 'general'),
(Polity_alternative_name, Polity_alternative_nameForm, 'polity_alternative_name', 'alternative_name', 'Polity Alternative Name', 'Identity and Location', None, 'general'),
(Polity_peak_years, Polity_peak_yearsForm, 'polity_peak_years', 'peak_years', 'Polity Peak Years', 'Temporal Bounds', None, 'general'),
(Polity_duration, Polity_durationForm, 'polity_duration', 'duration', 'Polity Duration', 'Temporal Bounds', None, 'general'),
(Polity_degree_of_centralization, Polity_degree_of_centralizationForm, 'polity_degree_of_centralization', 'degree_of_centralization', 'Polity Degree Of Centralization', 'Political and Cultural Relations', None, 'general'),
(Polity_suprapolity_relations, Polity_suprapolity_relationsForm, 'polity_suprapolity_relations', 'suprapolity_relations', 'Polity Suprapolity Relations', 'Language', None, 'general'),
(Polity_capital, Polity_capitalForm, 'polity_capital', 'capital', 'Polity Capital', 'Identity and Location', None, 'general'),
(Polity_language, Polity_languageForm, 'polity_language', 'language', 'Polity Language', 'Language', None, 'general'),
(Polity_linguistic_family, Polity_linguistic_familyForm, 'polity_linguistic_family', 'linguistic_family', 'Polity Linguistic Family', 'Language', None, 'general'),
(Polity_language_genus, Polity_language_genusForm, 'polity_language_genus', 'language_genus', 'Polity Language Genus', 'Language', None, 'general'),
(Polity_religion_genus, Polity_religion_genusForm, 'polity_religion_genus', 'religion_genus', 'Polity Religion Genus', 'Religion', None, 'general'),
(Polity_religion_family, Polity_religion_familyForm, 'polity_religion_family', 'religion_family', 'Polity Religion Family', 'Religion', None, 'general'),
(Polity_religion, Polity_religionForm, 'polity_religion', 'religion', 'Polity Religion', 'Religion', None, 'general'),
(Polity_relationship_to_preceding_entity, Polity_relationship_to_preceding_entityForm, 'polity_relationship_to_preceding_entity', 'relationship_to_preceding_entity', 'Polity Relationship To Preceding Entity', 'Political and Cultural Relations', None, 'general'),
(Polity_preceding_entity, Polity_preceding_entityForm, 'polity_preceding_entity', 'preceding_entity', 'Polity Preceding Entity', 'Political and Cultural Relations', None, 'general'),
(Polity_succeeding_entity, Polity_succeeding_entityForm, 'polity_succeeding_entity', 'succeeding_entity', 'Polity Succeeding Entity', 'Political and Cultural Relations', None, 'general'),
(Polity_supracultural_entity, Polity_supracultural_entityForm, 'polity_supracultural_entity', 'supracultural_entity', 'Polity Supracultural Entity', 'Political and Cultural Relations', None, 'general'),
(Polity_scale_of_supracultural_interaction, Polity_scale_of_supracultural_interactionForm, 'polity_scale_of_supracultural_interaction', 'scale_of_supracultural_interaction', 'Polity Scale Of Supracultural Interaction', 'Political and Cultural Relations', None, 'general'),
(Polity_alternate_religion_genus, Polity_alternate_religion_genusForm, 'polity_alternate_religion_genus', 'alternate_religion_genus', 'Polity Alternate Religion Genus', 'Religion', None, 'general'),
(Polity_alternate_religion_family, Polity_alternate_religion_familyForm, 'polity_alternate_religion_family', 'alternate_religion_family', 'Polity Alternate Religion Family', 'Religion', None, 'general'),
(Polity_alternate_religion, Polity_alternate_religionForm, 'polity_alternate_religion', 'alternate_religion', 'Polity Alternate Religion', 'Religion', None, 'general'),
(Polity_religious_tradition, Polity_religious_traditionForm, 'polity_religious_tradition', 'religious_tradition', 'Polity Religious Tradition', 'Religion', None, 'general'),

]

#     (Polity_alternative_name, Polity_alternative_nameForm, 'polity_alternative_name', 'alternative_name', 'Polity Alternative Name', "Identity and Location", None),
#     (Polity_capital, Polity_capitalForm, 'polity_capital', 'capital', 'Polity Capital', "Identity and Location", None),
#     # Polity_capital
#     (Polity_duration, Polity_durationForm, 'polity_duration', 'polity duration', 'Polity Duration', "Temporal Bounds", None),
#     (Polity_peak_years, Polity_peak_yearsForm, 'polity_peak_years', 'polity peak years', 'Polity Peak Years', "Temporal Bounds", None),
#     (Polity_religious_tradition, Polity_religious_traditionForm, 'polity_religious_tradition', 'religious_tradition', 'Polity Religious Tradition', "Religion", None),]  


# Create URL patterns dynamically for each model-class pair: UPDATE
for model_class, form_class, x_name, coded_value, myvar, sec, subsec, db_section in model_form_pairs:
    urlpatterns.append(
        path(f'{x_name}/create/', views.dynamic_create_view, {
            'form_class': form_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': general_var_defs.get(x_name, f"NO Desc: {myvar.lower().capitalize()}"),
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
        }, name=f'{x_name}-create')
     )
    urlpatterns.append(
        path(f'{x_name}/update_new/<int:object_id>/', views.dynamic_update_view, {
            'form_class': form_class,
            'model_class': model_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': general_var_defs.get(x_name, f"NO Desc: {myvar.lower().capitalize()}"),
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
            'delete_url_name': x_name + "-confirm-delete",
        }, name=f'{x_name}-updatenew')
    )
    urlpatterns.append(
        path(f'{x_name}/update/<int:object_id>/', views.dynamic_update_view_old, {
            'form_class': form_class,
            'model_class': model_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': general_var_defs.get(x_name, f"NO Desc: {myvar.lower().capitalize()}"),
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
            'delete_url_name': x_name + "-confirm-delete",
        }, name=f'{x_name}-update')
    )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/', views.dynamic_detail_view, {
          'model_class': model_class,
          'myvar': x_name,
          'var_name_display': myvar,
          'var_section': sec,
          'var_subsection': subsec,
          'db_section': db_section,
        }, name=f'{x_name}-detail')
     )
    urlpatterns.append(
        path(f'{x_name}s_all/', views.generic_list_view, {
            'model_class': model_class,
            'var_name': x_name,
            'var_name_display': myvar,
            'coded_value': coded_value,
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
            'var_main_desc': general_var_defs.get(x_name, f"NO Desc: {myvar.lower().capitalize()}"),

        }, name=f'{x_name}s_all')
     )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/confirm-delete/', views.confirm_delete_view, {
          'model_class': model_class,
          'var_name': x_name,
        }, name=f'{x_name}-confirm-delete')
     )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/delete/', views.delete_object_view, {
          'model_class': model_class,
            'var_name': x_name,
        }, name=f'{x_name}-delete')
     )
    urlpatterns.append(
        path(f'{x_name}download/', views.generic_download, {
            'model_class': model_class,
            'var_name': x_name,
            'x_name': x_name,
            'coded_value': coded_value,
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
        }, name=f'{x_name}-download')
     )
    urlpatterns.append(
        path(f'{x_name}jsondownload/', views.generic_json_download, {
            'model_class': model_class,
            'var_name': x_name,
            'x_name': x_name,
            'coded_value': coded_value,
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
        }, name=f'{x_name}-json-download')
     )
    urlpatterns.append(
        path(f'{x_name}metadownload/', views.generic_metadata_download, {
            'var_name': x_name,
            'var_name_display': myvar,
            'var_section': sec,
            'var_subsection': subsec,
            'var_main_desc': general_var_defs.get(x_name, f"NO Desc: {myvar.lower().capitalize()}"),        }, name=f'{x_name}-metadownload')
     )
