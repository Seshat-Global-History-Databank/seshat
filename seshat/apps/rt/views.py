from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

import csv

from ..core.forms import SeshatCommentPartForm2
from ..global_utils import (
    check_permissions,
    get_date,
    get_models,
    get_problematic_data_context,
    has_add_capital_permission,
    get_variable_context,
)
from ..global_constants import ABSENT_PRESENT_STRING_LIST, CSV_DELIMITER

from .constants import APP_NAME


def rtvars_view(request):
    """
    View function for the RT variables page.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the rendered RT variables page.
    """
    context = get_variable_context(app_name=APP_NAME)
    return render(request, "rt/rtvars.html", context=context)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def dynamic_detail_view(request, pk, model_class, myvar, var_name_display):
    """
    View function for the detail page of a model.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital'
        permission.

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
    o = get_object_or_404(model_class, pk=pk)

    form_inline_new = SeshatCommentPartForm2(request.POST)

    context = {
        "object": o,
        "myvar": myvar,
        "var_name_display": var_name_display,
        "create_new_url": myvar + "-create",
        "see_all_url": myvar + "s_all",
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
        The access to this view is restricted to users with the 'core.add_capital'
        permission.

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
    elif request.method == "GET":
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
        The access to this view is restricted to users with the 'core.add_capital'
        permission.

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

    elif request.method == "GET":
        # Create an instance of the form and populate it with the object's data
        my_form = form_class(instance=my_object)

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
        The access to this view is restricted to users with the 'core.add_capital'
        permission.

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
        objects = model_class.objects.all().order_by("polity_id", "order")
    else:
        objects = model_class.objects.all()

    extra_var_dict = {o.id: o.show_value() for o in objects}

    orderby = request.GET.get("orderby", None)

    # Apply sorting if orderby is provided and is a valid field name
    if orderby and hasattr(model_class, orderby):
        objects = objects.order_by(orderby)

    var_exp_new = f'The absence or presence of "{var_name_display}" for a polity.'

    if var_name in [
        "official_religion",
        "elites_religion",
    ]:
        ordering_tag_value = "coded_value_id"

    elif var_name in [
        "widespread_religion",
    ]:
        ordering_tag_value = "order"
    else:
        ordering_tag_value = "coded_value"

    context = {
        "object_list": objects,
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
    }

    context["inner_vars"] = {
        var_name_display: {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": var_exp_new,
            "units": None,
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    return render(request, "rt/rt_list_all.html", context)


@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def generic_download_view(request, model_class, var_name):
    """
    Download all data for a given model.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        model_class (Model): The model class of the object.
        var_name (str): The variable name.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"religion_tolerance_{var_name}_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

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

    for o in model_class.objects.all():
        if var_name in ["widespread_religion"]:
            writer.writerow(
                [
                    o.clean_name_dynamic(),
                    o.year_from,
                    o.year_to,
                    o.polity.long_name,
                    o.polity.new_name,
                    o.polity.name,
                    o.show_value_from(),
                    o.get_tag_display(),
                    o.is_disputed,
                    o.is_uncertain,
                    o.expert_reviewed,
                    o.drb_reviewed,
                ]
            )
        else:
            writer.writerow(
                [
                    o.clean_name_spaced(),
                    o.year_from,
                    o.year_to,
                    o.polity.long_name,
                    o.polity.new_name,
                    o.polity.name,
                    o.show_value(),
                    o.get_tag_display(),
                    o.is_disputed,
                    o.is_uncertain,
                    o.expert_reviewed,
                    o.drb_reviewed,
                ]
            )

    return response


@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def generic_metadata_download_view(
    request, var_name, var_name_display, var_section, var_subsection, var_main_desc
):
    """
    Download metadata for a given model.

    Note:
        This function is a generic view function that can be used for any model.
        This view is only accessible to users with the 'add_capital'
        permission.

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
            "choices": ABSENT_PRESENT_STRING_LIST,
            "null_meaning": None,
        }
    }

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

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
        The access to this view is restricted to users with the 'core.add_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        model_class (Model): The model class of the object.
        pk (int): The primary key of the object.
        var_name (str): The variable name.

    Returns:
        HttpResponse: The response object that contains the rendered confirmation page.
    """
    check_permissions(request)

    # Retrieve the object for the given model class
    o = get_object_or_404(model_class, pk=pk)

    context = {
        "var_name": var_name,
        "obj": o,
        "delete_object": f"{var_name}-delete",
    }

    return render(request, "core/confirm_delete.html", context)


@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def delete_object_view(request, model_class, pk, var_name):
    """
    View function to delete an object.

    Note:
        This function is a generic view function that can be used for any model.
        The access to this view is restricted to users with the 'core.add_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.
        model_class (Model): The model class of the object.
        pk (int): The primary key of the object.
        var_name (str): The variable name.

    Returns:
        HttpResponse: The response object that contains the rendered confirmation page.
    """
    check_permissions(request)

    # Retrieve the object for the given model class
    o = get_object_or_404(model_class, pk=pk)

    # Delete the object
    o.delete()

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
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"religion_tolerance_data_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

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

    # Iterate over each row of each model
    for model in get_models(APP_NAME):
        # Get all rows of data from the model
        for o in model.objects.all():
            if o.clean_name() == "widespread_religion":
                writer.writerow(
                    [
                        o.subsection(),
                        o.clean_name_dynamic(),
                        o.year_from,
                        o.year_to,
                        o.polity.long_name,
                        o.polity.new_name,
                        o.polity.name,
                        o.show_value_from(),
                        o.show_value_to(),
                        o.get_tag_display(),
                        o.is_disputed,
                        o.is_uncertain,
                        o.expert_reviewed,
                        o.drb_reviewed,
                    ]
                )
            else:
                writer.writerow(
                    [
                        o.subsection(),
                        o.clean_name_spaced(),
                        o.year_from,
                        o.year_to,
                        o.polity.long_name,
                        o.polity.new_name,
                        o.polity.name,
                        o.show_value_from(),
                        o.show_value_to(),
                        o.get_tag_display(),
                        o.is_disputed,
                        o.is_uncertain,
                        o.expert_reviewed,
                        o.drb_reviewed,
                    ]
                )

    return response


@permission_required("core.view_capital")
def show_problematic_rt_data_table(request):
    """
    View that shows a table of problematic data in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the rendered problematic data table.
    """
    # Get the context data for the problematic data (with standard conditions)
    context = get_problematic_data_context(APP_NAME)

    # Render the template with the data
    return render(request, "rt/problematic_rt_data_table.html", context)


@permission_required("core.view_capital")
def download_csv_religious_landscape(request):
    """
    Download all data for the Religious Landscape model in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"religion_tolerance_religious_landscape_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

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

    # Iterate over each row of each model
    for model in get_models(APP_NAME, exclude=["Ra"]):
        subsection = str(model().subsection())

        if subsection == "Religious Landscape":
            for o in model.objects.all():
                writer.writerow(
                    [
                        o.subsection(),
                        o.clean_name(),
                        o.year_from,
                        o.year_to,
                        o.polity.long_name,
                        o.polity.new_name,
                        o.polity.name,
                        o.show_value_from(),
                        o.show_value_to(),
                        o.get_tag_display(),
                        o.is_disputed,
                        o.is_uncertain,
                        o.expert_reviewed,
                        o.drb_reviewed,
                    ]
                )

    return response


@permission_required("core.view_capital")
def download_csv_government_restrictions(request):
    """
    Download all data for the Government Restrictions model in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"religion_tolerance_government_restrictions_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

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

    # Iterate over each row of each model
    for model in get_models(APP_NAME):
        subsection = str(model().subsection())

        if subsection == "Government Restrictions":
            for o in model.objects.all():
                writer.writerow(
                    [
                        o.subsection(),
                        o.clean_name(),
                        o.year_from,
                        o.year_to,
                        o.polity.long_name,
                        o.polity.new_name,
                        o.polity.name,
                        o.show_value_from(),
                        o.show_value_to(),
                        o.get_tag_display(),
                        o.is_disputed,
                        o.is_uncertain,
                        o.expert_reviewed,
                        o.drb_reviewed,
                    ]
                )

    return response


@permission_required("core.view_capital")
def download_csv_societal_restrictions(request):
    """
    Download all data for the Societal Restrictions model in the RT app.

    Note:
        The access to this view is restricted to users with the 'core.view_capital'
        permission.

    Args:
        request (HttpRequest): The request object used to generate this page.

    Returns:
        HttpResponse: The response object that contains the CSV file.
    """
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"religion_tolerance_societal_restrictions_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)

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

    # Iterate over each row of each model
    for model in get_models(APP_NAME):  # skip Ra, but not part of this app?
        subsection = str(model().subsection())

        if subsection == "Societal Restrictions":
            for o in model.objects.all():
                writer.writerow(
                    [
                        o.subsection(),
                        o.clean_name(),
                        o.year_from,
                        o.year_to,
                        o.polity.long_name,
                        o.polity.new_name,
                        o.polity.name,
                        o.show_value_from(),
                        o.show_value_to(),
                        o.get_tag_display(),
                        o.is_disputed,
                        o.is_uncertain,
                        o.expert_reviewed,
                        o.drb_reviewed,
                    ]
                )

    return response
