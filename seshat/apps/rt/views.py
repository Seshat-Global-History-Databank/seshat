from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from ..utils import (
    get_problematic_data_context,
    get_variable_context,
)

from .constants import APP_NAME


class RTVarsView(TemplateView):
    template_name = "rt/rtvars.html"

    def get_context_data(self, **kwargs) -> dict:
        return get_variable_context(app_name=APP_NAME)


class ProblematicDataView(PermissionRequiredMixin, TemplateView):
    template_name = "rt/problematic_rt_data_table.html"
    permission_required = "core.view_capital"

    def get_context_data(self, **kwargs) -> dict:
        return get_problematic_data_context(app_name=APP_NAME)
