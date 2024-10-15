from django.urls import path

from ..generic_views import (
    GenericMultipleDownloadView,
    GenericDeleteView,
    VariableView,
    ProblematicDataView,
    VariableDetailView,
    DownloadVariableView,
    VariableListView,
    VariablePolityListView,
    GenericMetaDownloadView,
    GenericDownloadView,
    get_url_pattern,
)

from . import views
from .constants import model_form_pairs, categories

APP_LABEL = "wf"
PREFIX = "warfare_"

urlpatterns = [
    path(
        "wfvars/",
        VariableView.as_view(app_label=APP_LABEL),
        name="wfvars",
    ),
    path(
        "problematic_wf_data_table/",
        ProblematicDataView.as_view(
            app_label=APP_LABEL,
            template_name="wf/problematic_wf_data_table.html",
        ),
        name="problematic_wf_data_table",
    ),
    path(
        "download-csv-wf-all/",
        GenericMultipleDownloadView.as_view(
            app_label=APP_LABEL, prefix="warfare_data_"
        ),
        name="download_csv_all_wf",
    ),
]

urlpatterns += get_url_pattern(
    categories=categories,
    model_form_pairs=model_form_pairs,
    views=views,
    app_label=APP_LABEL,
    prefix=PREFIX,
)
