from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

import csv
import datetime

from ..core.forms import SeshatCommentPartForm2

from .var_defs import swapped_dict


def rtvars(request):
    """
    View function for the RT variables page.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the rendered RT variables page.
    """
    app_name = "rt"  # Replace with your app name
    models_1 = apps.get_app_config(app_name).get_models()

    unique_politys = set()
    number_of_all_rows = 0
    number_of_variables = 0
    all_vars_grouped = {}

    all_sect_download_links = {}

    for model in models_1:
        model_name = model.__name__
        if model_name in [
            "RA",
        ]:
            continue
        s_value = str(model().subsection())
        ss_value = str(model().sub_subsection())

        better_name = (
            "download_csv_"
            + s_value.replace("-", "_").replace(" ", "_").replace(":", "").lower()
        )
        all_sect_download_links[s_value] = better_name
        if s_value not in all_vars_grouped:
            all_vars_grouped[s_value] = {}
            if ss_value:
                all_vars_grouped[s_value][ss_value] = []
            else:
                all_vars_grouped[s_value]["None"] = []
        else:
            if ss_value:
                all_vars_grouped[s_value][ss_value] = []
            else:
                all_vars_grouped[s_value]["None"] = []

    models = apps.get_app_config(app_name).get_models()

    for model in models:
        model_name = model.__name__
        if model_name in [
            "RA",
        ]:
            continue
        subsection_value = str(model().subsection())
        sub_subsection_value = str(model().sub_subsection())
        count = model.objects.count()
        number_of_all_rows += count
        model_title = model_name.replace("_", " ").title()
        model_title = swapped_dict[model_name]
        model_create = model_name.lower() + "-create"
        model_download = model_name.lower() + "-download"
        model_metadownload = model_name.lower() + "-metadownload"
        model_all = model_name.lower() + "s_all"
        model_s = model_name.lower() + "s"

        queryset = model.objects.all()
        politys = queryset.values_list("polity", flat=True).distinct()
        unique_politys.update(politys)
        number_of_variables += 1

        to_be_appended = [
            model_title,
            model_s,
            model_create,
            model_download,
            model_metadownload,
            model_all,
            count,
        ]

        if sub_subsection_value:
            all_vars_grouped[subsection_value][sub_subsection_value].append(
                to_be_appended
            )
        else:
            all_vars_grouped[subsection_value]["None"].append(to_be_appended)

    context = {}
    context["all_vars_grouped"] = all_vars_grouped
    context["all_sect_download_links"] = all_sect_download_links
    context["all_polities"] = len(unique_politys)
    context["number_of_all_rows"] = number_of_all_rows

    context["number_of_variables"] = number_of_variables

    return render(request, "rt/rtvars.html", context=context)


def has_add_capital_permission(user):
    """
    Check if the user has the 'core.add_capital' permission.

    Note:
        TODO This is built-in functionality in Django. You can use the built-in permission_required decorator instead.

    Args:
        user (User): The user object.

    Returns:
        bool: True if the user has the 'core.add_capital' permission, False otherwise.
    """
    return user.has_perm("core.add_capital")


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def dynamic_detail_view(request, pk, model_class, myvar, var_name_display):
    """
    View function for the detail page of a model.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        pk (int): The primary key of the object.
        model_class (Model): The model class of the object.
        myvar (str): The variable name.
        var_name_display (str): The variable name to display.

    Returns:
        HttpResponse: The response object that contains the rendered detail page.
    """
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)
    form_inline_new = SeshatCommentPartForm2(request.POST)

    context = {
        "object": obj,
        "myvar": myvar,
        "var_name_display": var_name_display,
        "create_new_url": myvar + "-create",
        "see_all_url": myvar + "s_all",
        "letsdo": "Let us do it!!!",
        "form": form_inline_new,
    }

    return render(request, "rt/rt_detail.html", context)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def dynamic_create_view(
    request, form_class, x_name, myvar, my_exp, var_section, var_subsection
):
    """
    View function for the create page of a model.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        form_class (Form): The form class used to create the object.
        x_name (str): The variable name.
        myvar (str): The variable name.
        my_exp (str): The variable explanation.
        var_section (str): The section name.
        var_subsection (str): The subsection name.

    Returns:
        HttpResponse: The response object that contains the rendered create page.
    """
    if x_name in [
        "widespread_religion",
    ]:
        x_name_1 = "order"
        x_name_2 = "widespread_religion"
        x_name_3 = "degree_of_prevalence"

    else:
        x_name_1 = x_name
        x_name_2 = None
        x_name_3 = None

    if request.method == "POST":
        my_form = form_class(request.POST)

        if my_form.is_valid():
            new_object = my_form.save()
            return redirect(f"{x_name}-detail", pk=new_object.id)
    else:
        polity_id_x = request.GET.get("polity_id_x")
        my_form = form_class(
            initial={
                "polity": polity_id_x,
            }
        )

    if x_name in [
        "widespread_religion",
    ]:
        context = {
            "form": my_form,
            "object": object,
            "extra_var": my_form[x_name_1],
            "extra_var2": my_form[x_name_2],
            "extra_var3": my_form[x_name_3],
            "myvar": myvar,
            "my_exp": my_exp,
            "var_section": var_section,
            "var_subsection": var_subsection,
        }
    else:
        context = {
            "form": my_form,
            "object": object,
            "extra_var": my_form["coded_value"],
            "myvar": myvar,
            "my_exp": my_exp,
            "var_section": var_section,
            "var_subsection": var_subsection,
        }

    return render(request, "rt/rt_create.html", context)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def dynamic_update_view(
    request,
    object_id,
    form_class,
    model_class,
    x_name,
    myvar,
    my_exp,
    var_section,
    var_subsection,
    delete_url_name,
):
    """
    View function for the update page of a model.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        object_id (int): The primary key of the object.
        form_class (Form): The form class used to update the object.
        model_class (Model): The model class of the object.
        x_name (str): The variable name.
        myvar (str): The variable name.
        my_exp (str): The variable explanation.
        var_section (str): The section name.
        var_subsection (str): The subsection name.
        delete_url_name (str): The URL name for deleting the object.

    Returns:
        HttpResponse: The response object that contains the rendered update page.
    """
    # Retrieve the object based on the object_id
    my_object = model_class.objects.get(id=object_id)

    if x_name in [
        "widespread_religion",
    ]:
        x_name_1 = "order"
        x_name_2 = "widespread_religion"
        x_name_3 = "degree_of_prevalence"

    else:
        x_name_1 = x_name
        x_name_2 = None
        x_name_3 = None

    if request.method == "POST":
        # Bind the form to the POST data
        my_form = form_class(request.POST, instance=my_object)

        if my_form.is_valid():
            # Save the changes to the object
            my_form.save()
            return redirect(f"{x_name}-detail", pk=my_object.id)

    else:
        # Create an instance of the form and populate it with the object's data
        my_form = form_class(instance=my_object)

        # Define the context with the variables you want to pass to the template
        if x_name in [
            "widespread_religion",
        ]:
            context = {
                "form": my_form,
                "object": my_object,
                "delete_url": delete_url_name,
                "extra_var": my_form[x_name_1],
                "extra_var2": my_form[x_name_2],
                "extra_var3": my_form[x_name_3],
                "myvar": myvar,
                "var_section": var_section,
                "var_subsection": var_subsection,
                "my_exp": my_exp,
            }
        else:
            context = {
                "form": my_form,
                "object": my_object,
                "delete_url": delete_url_name,
                "extra_var": my_form["coded_value"],
                "myvar": myvar,
                "var_section": var_section,
                "var_subsection": var_subsection,
                "my_exp": my_exp,
            }

    return render(request, "rt/rt_update.html", context)


@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def generic_list_view(
    request,
    model_class,
    var_name,
    var_name_display,
    var_section,
    var_subsection,
    var_main_desc,
):
    """
    View function for the list page of a model.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        model_class (Model): The model class of the object.
        var_name (str): The variable name.
        var_name_display (str): The variable name to display.
        var_section (str): The section name.
        var_subsection (str): The subsection name.
        var_main_desc (str): The main description.

    Returns:
        HttpResponse: The response object that contains the rendered list page.
    """
    if var_name in [
        "widespread_religion",
    ]:
        object_list = model_class.objects.all().order_by("polity_id", "order")
    else:
        object_list = model_class.objects.all()

    extra_var_dict = {obj.id: obj.show_value() for obj in object_list}

    orderby = request.GET.get("orderby", None)

    # Apply sorting if orderby is provided and is a valid field name
    if orderby and hasattr(model_class, orderby):
        object_list = object_list.order_by(orderby)

    var_name_with_from = var_name
    var_exp_new = f'The absence or presence of "{var_name_display}" for a polity.'

    if var_name in [
        "official_religion",
        "elites_religion",
    ]:
        ordering_tag_value = "coded_value_id"
    #     # ?orderby=formal_legal_code&orderby2=tag
    elif var_name in [
        "widespread_religion",
    ]:
        ordering_tag_value = "order"
    else:
        ordering_tag_value = "coded_value"

    # Define any additional context variables you want to pass to the template
    context = {
        "object_list": object_list,
        "var_name": var_name,
        "create_url": f"{var_name}-create",
        "update_url": f"{var_name}-update",
        "download_url": f"{var_name}-download",
        "pagination_url": f"{var_name}s",
        "metadownload_url": f"{var_name}-metadownload",
        "list_all_url": f"{var_name}s_all",
        "var_name_display": var_name_display,
        "ordering_tag": f"?orderby={ordering_tag_value}",
        "var_section": var_section,
        "var_subsection": var_subsection,
        "var_main_desc": var_main_desc,
        "myvar": var_name_display,
        "extra_var_dict": extra_var_dict,  # Add the dictionary to the context
        #'extra_var': obj[var_name],
        #'obj_var': my_form[x_name],
        # "myvar": myvar,
        # "my_exp": my_exp,
    }

    context["inner_vars"] = {
        var_name_display: {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": var_exp_new,
            "units": None,
            "choices": "ABSENT_PRESENT_CHOICES",
            "null_meaning": None,
        }
    }

    return render(request, "rt/rt_list_all.html", context)


@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def generic_download(request, model_class, var_name):
    """
    Download all data for a given model.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        model_class (Model): The model class of the object.
        var_name (str): The variable name.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    items = model_class.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"religion_tolerance_{var_name}_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter="|")
    writer.writerow(
        [
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            var_name,
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )
    for obj in items:
        if var_name in ["widespread_religion"]:
            writer.writerow(
                [
                    obj.clean_name_dynamic(),
                    obj.year_from,
                    obj.year_to,
                    obj.polity.long_name,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.show_value_from(),
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.is_uncertain,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )
        else:
            writer.writerow(
                [
                    obj.clean_name_spaced(),
                    obj.year_from,
                    obj.year_to,
                    obj.polity.long_name,
                    obj.polity.new_name,
                    obj.polity.name,
                    obj.show_value(),
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.is_uncertain,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )

    return response


@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def generic_metadata_download(
    request, var_name, var_name_display, var_section, var_subsection, var_main_desc
):
    """
    Download metadata for a given model.

    Note:
        This function is a generic view function that can be used for any model.
        This view is only accessible to users with the 'add_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        var_name (str): The variable name.
        var_name_display (str): The variable name to display.
        var_section (str): The section name.
        var_subsection (str): The subsection name.
        var_main_desc (str): The main description.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="metadata_{var_name}s.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": var_main_desc,
        "main_desc_source": "NOTHING",
        "section": var_section,
        "subsection": var_subsection,
    }
    my_meta_data_dic_inner_vars = {
        "general_postal_service": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": f"The {var_name_display} for a polity.",
            "units": None,
            "choices": "ABSENT_PRESENT_CHOICES",
            "null_meaning": None,
        }
    }

    writer = csv.writer(response, delimiter="|")

    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow(
            [
                k_in,
            ]
        )
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response


@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def confirm_delete_view(request, model_class, pk, var_name):
    """
    View function to confirm the deletion of an object.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        model_class (Model): The model class of the object.
        pk (int): The primary key of the object.
        var_name (str): The variable name.

    Returns:
        HttpResponse: The response object that contains the rendered confirmation page.
    """
    permission_required = "core.add_capital"

    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    # Check if the user has the required permission
    if not request.user.has_perm(permission_required):
        return HttpResponseForbidden("You don't have permission to delete this object.")

    template_name = "core/confirm_delete.html"

    context = {
        "var_name": var_name,
        "obj": obj,
        "delete_object": f"{var_name}-delete",
    }

    return render(request, template_name, context)


@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def delete_object_view(request, model_class, pk, var_name):
    """
    View function to delete an object.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        model_class (Model): The model class of the object.
        pk (int): The primary key of the object.
        var_name (str): The variable name.

    Returns:
        HttpResponse: The response object that contains the rendered confirmation page.
    """
    permission_required = "core.add_capital"
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    if not request.user.has_perm(permission_required):
        return HttpResponseForbidden("You don't have permission to delete this object.")

    # Delete the object
    obj.delete()

    # Redirect to the success URL
    success_url_name = f"{var_name}s_all"  # Adjust the success URL as needed
    success_url = reverse(success_url_name)

    # Display a success message
    messages.success(request, f"{var_name} has been deleted successfully.")

    return redirect(success_url)


@permission_required("core.view_capital")
def download_csv_all_rt(request):
    """
    Download all data for all models in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    # Fetch all models in the "socomp" app
    app_name = "rt"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"religion_tolerance_data_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    writer.writerow(
        [
            "subsection",
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "value_from",
            "value_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        items = model.objects.all()

        for obj in items:
            if obj.clean_name() == "widespread_religion":
                writer.writerow(
                    [
                        obj.subsection(),
                        obj.clean_name_dynamic(),
                        obj.year_from,
                        obj.year_to,
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.show_value_from(),
                        obj.show_value_to(),
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                        obj.drb_reviewed,
                    ]
                )
            else:
                writer.writerow(
                    [
                        obj.subsection(),
                        obj.clean_name_spaced(),
                        obj.year_from,
                        obj.year_to,
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.show_value_from(),
                        obj.show_value_to(),
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                        obj.drb_reviewed,
                    ]
                )

    return response


@permission_required("core.view_capital")
def show_problematic_rt_data_table(request):
    """
    View that shows a table of problematic data in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the rendered problematic data table.
    """
    # Fetch all models in the "socomp" app
    app_name = "rt"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Collect data from all models
    data = []
    for model in app_models:
        items = model.objects.all()
        for obj in items:
            if (
                obj.polity.start_year is not None
                and obj.year_from is not None
                and obj.polity.start_year > obj.year_from
            ):
                data.append(obj)

    # Render the template with the data
    return render(request, "rt/problematic_rt_data_table.html", {"data": data})


@permission_required("core.view_capital")
def download_csv_religious_landscape(request):
    """
    Download all data for the Religious Landscape model in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    # Fetch all models in the "socomp" app
    app_name = "rt"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"religion_tolerance_religious_landscape_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    writer.writerow(
        [
            "subsection",
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "value_from",
            "value_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Religious Landscape":
            items = model.objects.all()
            for obj in items:
                writer.writerow(
                    [
                        obj.subsection(),
                        obj.clean_name(),
                        obj.year_from,
                        obj.year_to,
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.show_value_from(),
                        obj.show_value_to(),
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                        obj.drb_reviewed,
                    ]
                )

    return response


@permission_required("core.view_capital")
def download_csv_government_restrictions(request):
    """
    Download all data for the Government Restrictions model in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    # Fetch all models in the "socomp" app
    app_name = "rt"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"religion_tolerance_government_restrictions_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    writer.writerow(
        [
            "subsection",
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "value_from",
            "value_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Government Restrictions":
            items = model.objects.all()
            for obj in items:
                writer.writerow(
                    [
                        obj.subsection(),
                        obj.clean_name(),
                        obj.year_from,
                        obj.year_to,
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.show_value_from(),
                        obj.show_value_to(),
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                        obj.drb_reviewed,
                    ]
                )

    return response


@permission_required("core.view_capital")
def download_csv_societal_restrictions(request):
    """
    Download all data for the Societal Restrictions model in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    # Fetch all models in the "socomp" app
    app_name = "rt"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"religion_tolerance_societal_restrictions_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    writer.writerow(
        [
            "subsection",
            "variable_name",
            "year_from",
            "year_to",
            "polity_name",
            "polity_new_ID",
            "polity_old_ID",
            "value_from",
            "value_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
            "DRB_reviewed",
        ]
    )
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Societal Restrictions":
            items = model.objects.all()
            for obj in items:
                writer.writerow(
                    [
                        obj.subsection(),
                        obj.clean_name(),
                        obj.year_from,
                        obj.year_to,
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.show_value_from(),
                        obj.show_value_to(),
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                        obj.drb_reviewed,
                    ]
                )

    return response
