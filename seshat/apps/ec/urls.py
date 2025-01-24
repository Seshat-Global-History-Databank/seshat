from .models import Lux_precious_metal, Luxury_fabrics, Luxury_manufactured_goods, Luxury_spices_incense_and_dyes, Luxury_drink_alcohol, Luxury_glass_goods, Lux_fine_ceramic_wares, Lux_precious_stone, Lux_statuary, Luxury_food, Other_luxury_personal_items 

from .forms import Lux_precious_metalForm, Luxury_fabricsForm, Luxury_manufactured_goodsForm, Luxury_spices_incense_and_dyesForm, Luxury_drink_alcoholForm, Luxury_glass_goodsForm, Lux_fine_ceramic_waresForm, Lux_precious_stoneForm, Lux_statuaryForm, Luxury_foodForm, Other_luxury_personal_itemsForm

from seshat.apps.general.views import dynamic_create_view, dynamic_update_view,  dynamic_update_view_old, generic_list_view, generic_download, generic_metadata_download, dynamic_detail_view, confirm_delete_view, delete_object_view

from django.urls import path

from .var_defs import ec_var_defs
from . import views

urlpatterns = [
    path('ecvars/', views.ecvars, name='ecvars'),
    path('download_csv_luxury_goods/', views.download_csv_luxury_goods,name='download_csv_luxury_goods'),
    #     path('download-csv-ec-all/', views.download_csv_all_ec,name='download_csv_all_ec'),
    #  path('problematic_ec_data_table/', views.show_problematic_ec_data_table, name='problematic_ec_data_table'),

]

model_form_pairs_qugmented = [
    (Lux_precious_metal, Lux_precious_metalForm, 'lux_precious_metal', 'coded_value', 'Precious Metal', 'Luxury Goods', None, 'ec'),
    (Luxury_fabrics, Luxury_fabricsForm, 'luxury_fabrics', 'coded_value', 'Luxury Fabrics', 'Luxury Goods', None, 'ec'),
    (Luxury_manufactured_goods, Luxury_manufactured_goodsForm, 'luxury_manufactured_goods', 'coded_value', 'Luxury Manufactured Goods', 'Luxury Goods', None, 'ec'),
    (Luxury_spices_incense_and_dyes, Luxury_spices_incense_and_dyesForm, 'luxury_spices_incense_and_dyes', 'coded_value', 'Luxury Spices Incense And Dyes', 'Luxury Goods', None, 'ec'),
    (Luxury_drink_alcohol, Luxury_drink_alcoholForm, 'luxury_drink_alcohol', 'coded_value', 'Luxury Drink/Alcohol', 'Luxury Goods', None, 'ec'),
    (Luxury_glass_goods, Luxury_glass_goodsForm, 'luxury_glass_goods', 'coded_value', 'Luxury Glass Goods', 'Luxury Goods', None, 'ec'),
    (Lux_fine_ceramic_wares, Lux_fine_ceramic_waresForm, 'lux_fine_ceramic_wares', 'coded_value', 'Fine Ceramic Wares', 'Luxury Goods', None, 'ec'),
    (Lux_precious_stone, Lux_precious_stoneForm, 'lux_precious_stone', 'coded_value', 'Precious Stone', 'Luxury Goods', None, 'ec'),
    (Lux_statuary, Lux_statuaryForm, 'lux_statuary', 'coded_value', 'Statuary', 'Luxury Goods', None, 'ec'),
    (Luxury_food, Luxury_foodForm, 'luxury_food', 'coded_value', 'Luxury Food', 'Luxury Goods', None, 'ec'),
    (Other_luxury_personal_items, Other_luxury_personal_itemsForm, 'other_luxury_personal_items', 'coded_value', 'Other Luxury Personal Items', 'Luxury Goods', None, 'ec'),
    ]

# Create URL patterns dynamically for each model-class pair: UPDATE
for model_class, form_class, x_name, coded_value, myvar, sec, subsec, db_section in model_form_pairs_qugmented:
    urlpatterns.append(
        path(f'{x_name}/create/', dynamic_create_view, {
            'form_class': form_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': ec_var_defs.get(x_name, f"NO Desc: {x_name}"),
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
        }, name=f'{x_name}-create')
     )
    urlpatterns.append(
        path(f'{x_name}/updatenew/<int:object_id>/', dynamic_update_view, {
            'form_class': form_class,
            'model_class': model_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': ec_var_defs.get(x_name, f"NO Desc: {x_name}"),
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
            'delete_url_name': x_name + "-confirm-delete",
        }, name=f'{x_name}-updatenew')
    )
    urlpatterns.append(
        path(f'{x_name}/update_old/<int:object_id>/', dynamic_update_view_old, {
            'form_class': form_class,
            'model_class': model_class,
            'x_name': x_name,
            'myvar': myvar,
            'coded_value': coded_value,
            'my_exp': ec_var_defs.get(x_name, f"NO Desc: {x_name}"),
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
            'delete_url_name': x_name + "-confirm-delete",
        }, name=f'{x_name}-update')
    )
    urlpatterns.append(
        path(f'{x_name}/<int:pk>/', dynamic_detail_view, {
          'model_class': model_class,
          'myvar': x_name,
          'var_section': sec,
          'var_subsection': subsec,
          'db_section': db_section,
          'var_name_display': myvar,
        }, name=f'{x_name}-detail')
     )
    urlpatterns.append(
        path(f'{x_name}s_all/', generic_list_view, {
            'model_class': model_class,
            'var_name': x_name,
            'coded_value': coded_value,
            'var_name_display': myvar,
            'var_section': sec,
            'var_subsection': subsec,
            'db_section': db_section,
            'var_main_desc': ec_var_defs.get(x_name, f"NO Desc: {x_name}"),

        }, name=f'{x_name}s_all')
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
    urlpatterns.append(
        path(f'{x_name}download/', generic_download, {
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
        path(f'{x_name}metadownload/', generic_metadata_download, {
            'var_name': x_name,
            'var_name_display': myvar,
            'var_section': sec,
            'var_subsection': subsec,
            #'db_section': db_section,
            'var_main_desc': ec_var_defs[x_name],
        }, name=f'{x_name}-metadownload')
     )
