import csv

from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
    user_passes_test,
)
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from ....utils import (
    check_permissions,
    get_date,
    has_add_capital_permission,
)
from ....constants import (
    ABSENT_PRESENT_STRING_LIST,
    CSV_DELIMITER,
)


def generic_list_view(
    request,
    model_class,
    var_name,
    var_name_display,
    var_section,
    var_subsection,
    var_main_desc,
):
    # Retrieve a list of objects from the database (you can customize this query)
    object_list = model_class.objects.all()

    # Create a dictionary with the object IDs as keys and the show_value()
    # method as values
    extra_var_dict = {obj.id: obj.show_value() for obj in object_list}

    orderby = request.GET.get("orderby", None)

    # Apply sorting if orderby is provided and is a valid field name
    if orderby and hasattr(model_class, orderby):
        object_list = object_list.order_by(orderby)

    if var_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        var_name_with_from = var_name + "_from"
        var_exp_new = f'The range of "{var_name_display}" for a polity.'
    else:
        var_name_with_from = var_name
        var_exp_new = (
            f'The absence or presence of "{var_name_display}" for a polity.'
        )

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
        "ordering_tag": f"?orderby={var_name_with_from}",
        "var_section": var_section,
        "var_subsection": var_subsection,
        "var_main_desc": var_main_desc,
        "myvar": var_name_display,
        "extra_var_dict": extra_var_dict,
        "inner_vars": {
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
    }

    return render(request, "sc/sc_list_all.html", context)


@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def generic_download_view(request, model_class, var_name):
    date = get_date()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    # Add filename to response object
    file_name = f"social_complexity_{var_name}_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    if var_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        var_name_with_from = var_name + "_from"
        var_name_with_to = var_name + "_to"
    else:
        var_name_with_from = var_name
        var_name_with_to = None

    # Create a CSV writer
    writer = csv.writer(response, delimiter=CSV_DELIMITER)
    if var_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        writer.writerow(
            [
                "variable_name",
                "year_from",
                "year_to",
                "polity_name",
                "polity_new_ID",
                "polity_old_ID",
                var_name_with_from,
                var_name_with_to,
                "confidence",
                "is_disputed",
                "is_uncertain",
                "expert_checked",
                "DRB_reviewed",
            ]
        )
    else:
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

    for obj in model_class.objects.all():
        if var_name in [
            "largest_communication_distance",
            "fastest_individual_communication",
            "military_level",
        ]:
            dynamic_value_from = getattr(obj, var_name_with_from, "")
            dynamic_value_to = getattr(obj, var_name_with_to, "")
            writer.writerow(
                [
                    obj.name,
                    obj.year_from,
                    obj.year_to,
                    obj.polity.long_name,
                    obj.polity.new_name,
                    obj.polity.name,
                    dynamic_value_from,
                    dynamic_value_to,
                    obj.get_tag_display(),
                    obj.is_disputed,
                    obj.is_uncertain,
                    obj.expert_reviewed,
                    obj.drb_reviewed,
                ]
            )
        else:
            dynamic_value = getattr(obj, var_name, "")
            writer.writerow(
                [
                    obj.name,
                    obj.year_from,
                    obj.year_to,
                    obj.polity.long_name,
                    obj.polity.new_name,
                    obj.polity.name,
                    dynamic_value,
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
def generic_metadata_download_view(
    request,
    var_name,
    var_name_display,
    var_section,
    var_subsection,
    var_main_desc,
):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        f'attachment; filename="metadata_{var_name}s.csv"'
    )

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


def generic_confirm_delete_view(request, model_class, pk, var_name):
    check_permissions(request)

    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    context = {
        "var_name": var_name,
        "obj": obj,
        "delete_object": f"{var_name}-delete",
    }

    return render(request, "core/confirm_delete.html", context)


def generic_delete_object_view(request, model_class, pk, var_name):
    check_permissions(request)

    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    # Delete the object
    obj.delete()

    success_url = reverse(f"{var_name}s_all")

    # Display a success message
    messages.success(request, f"{var_name} has been deleted successfully.")

    return redirect(success_url)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def generic_update_view(
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
    # Retrieve the object based on the object_id
    my_object = model_class.objects.get(id=object_id)

    if x_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        x_name_with_from = x_name + "_from"
        x_name_with_to = x_name + "_to"
    else:
        x_name_with_from = x_name
        x_name_with_to = None

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
            "largest_communication_distance",
            "fastest_individual_communication",
            "military_level",
        ]:
            context = {
                "form": my_form,
                "object": my_object,
                "delete_url": delete_url_name,
                "extra_var": my_form[x_name_with_from],
                "extra_var2": my_form[x_name_with_to],
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
                "extra_var": my_form[x_name],
                "myvar": myvar,
                "var_section": var_section,
                "var_subsection": var_subsection,
                "my_exp": my_exp,
            }

    return render(request, "sc/sc_update.html", context)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def generic_detail_view(request, pk, model_class, myvar, var_name_display):
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    context = {
        "object": obj,
        "myvar": myvar,
        "var_name_display": var_name_display,
        "create_new_url": myvar + "-create",
        "see_all_url": myvar + "s_all",
    }

    return render(request, "sc/sc_detail.html", context)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required("core.add_capital", raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url="permission_denied")
def generic_create_view(
    request, form_class, x_name, myvar, my_exp, var_section, var_subsection
):
    # Retrieve the object based on the object_id
    if x_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        x_name_with_from = x_name + "_from"
        x_name_with_to = x_name + "_to"
    else:
        x_name_with_from = x_name
        x_name_with_to = None

    if request.method == "POST":
        # If the request method is POST, it means the form has been submitted
        my_form = form_class(request.POST)

        if my_form.is_valid():
            # Save the new object to the database
            new_object = my_form.save()
            return redirect(f"{x_name}-detail", pk=new_object.id)
    elif request.method == "GET":
        my_form = form_class(
            initial={
                "polity": request.GET.get("polity_id_x"),
            }
        )

    if x_name in [
        "largest_communication_distance",
        "fastest_individual_communication",
        "military_level",
    ]:
        context = {
            "form": my_form,
            "object": object,
            "extra_var": my_form[x_name_with_from],
            "extra_var2": my_form[x_name_with_to],
            "myvar": myvar,
            "my_exp": my_exp,
            "var_section": var_section,
            "var_subsection": var_subsection,
        }
    else:
        context = {
            "form": my_form,
            "object": object,
            "extra_var": my_form[x_name],
            "myvar": myvar,
            "my_exp": my_exp,
            "var_section": var_section,
            "var_subsection": var_subsection,
        }

    return render(request, "sc/sc_create.html", context)
