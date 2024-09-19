from django.shortcuts import render

from ...constants import APP_NAME
from ....global_utils import get_variable_context


def wfvars_view(request):
    context = get_variable_context(app_name=APP_NAME)
    return render(request, "wf/wfvars.html", context=context)
