# TODO: fix docstrings in this document

import csv
import time

from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    CreateView,
    # DetailView,
    UpdateView,
    View,
    TemplateView,
)

from .constants import ABSENT_PRESENT_STRING_LIST, CSV_DELIMITER, NO_DATA
from .core.forms import SeshatCommentPartForm2
from .utils import (
    get_date,
    get_response,
    get_models,
    get_variable_context,
    get_problematic_data_context,
)


def get_rowdicts(model_class, var_name, force_from_to=False):
    if force_from_to:
        # used for cross-model downloads when we need to have a _from and _to field
        # in the resulting CSV files
        has_from_and_to = True
    else:
        has_from_and_to = all(
            [
                hasattr(model_class, f"{var_name}_from"),
                hasattr(model_class, f"{var_name}_to"),
            ]
        )

    # Set up rows using list comprehension

    def get_variable_name(obj):
        if hasattr(obj, "clean_name_dynamic"):
            return obj.clean_name_dynamic()

        if hasattr(obj, "clean_name_spaced"):
            return obj.clean_name_spaced()

        if hasattr(obj, "clean_name"):
            return obj.clean_name()

        raise RuntimeError("Could not identify variable name.")

    def get_value(obj, prio=None, fail_value=None):
        if prio:
            val = getattr(obj, prio, "")

            if val:
                return val

            if fail_value:
                return fail_value

        if hasattr(obj, "show_value_from"):
            return obj.show_value_from()

        if hasattr(obj, "show_value"):
            return obj.show_value()

        if hasattr(obj, "coded_value"):
            return obj.coded_value

        return ""

    if has_from_and_to:
        if force_from_to:
            rowdicts = [
                {
                    "subsection": obj.subsection(),
                    "variable_name": get_variable_name(obj),
                    "year_from": obj.year_from,
                    "year_to": obj.year_to,
                    "polity_name": obj.polity.long_name if obj.polity else "",
                    "polity_new_ID": obj.polity.new_name if obj.polity else "",
                    "polity_old_ID": obj.polity.name if obj.polity else "",
                    "value_from": get_value(obj, prio=f"{var_name}_from"),
                    "value_to": get_value(
                        obj, prio=f"{var_name}_to", fail_value=""
                    ),
                    "confidence": obj.get_tag_display(),
                    "is_disputed": obj.is_disputed,
                    "is_uncertain": obj.is_uncertain,
                    "expert_checked": obj.expert_reviewed,
                    "DRB_reviewed": obj.drb_reviewed,
                }
                for obj in model_class.objects.all()
            ]
        else:
            rowdicts = [
                {
                    "variable_name": get_variable_name(obj),
                    "year_from": obj.year_from,
                    "year_to": obj.year_to,
                    "polity_name": obj.polity.long_name if obj.polity else "",
                    "polity_new_ID": obj.polity.new_name if obj.polity else "",
                    "polity_old_ID": obj.polity.name if obj.polity else "",
                    f"{var_name}_from": get_value(
                        obj, prio=f"{var_name}_from"
                    ),
                    f"{var_name}_to": get_value(
                        obj, prio=f"{var_name}_to", fail_value=""
                    ),
                    "confidence": obj.get_tag_display(),
                    "is_disputed": obj.is_disputed,
                    "is_uncertain": obj.is_uncertain,
                    "expert_checked": obj.expert_reviewed,
                    "DRB_reviewed": obj.drb_reviewed,
                }
                for obj in model_class.objects.all()
            ]
    else:
        rowdicts = [
            {
                "variable_name": get_variable_name(obj),
                "year_from": obj.year_from,
                "year_to": obj.year_to,
                "polity_name": obj.polity.long_name if obj.polity else "",
                "polity_new_ID": obj.polity.new_name if obj.polity else "",
                "polity_old_ID": obj.polity.name if obj.polity else "",
                var_name: get_value(obj),
                "confidence": obj.get_tag_display(),
                "is_disputed": obj.is_disputed,
                "is_uncertain": obj.is_uncertain,
                "expert_checked": obj.expert_reviewed,
                "DRB_reviewed": obj.drb_reviewed,
            }
            for obj in model_class.objects.all()
        ]

    return rowdicts


class GenericConfirmDeleteView(PermissionRequiredMixin, View):
    permission_required = "core.add_capital"
    model_class = None
    var_name = None
    template = None

    def get(self, request, pk):
        """
        Handle GET requests to confirm the deletion of an object.

        Args:
            request: HttpRequest object
            pk: Primary key of the object to be deleted

        Returns:
            HttpResponse: Renders a confirmation page
        """
        # Check if the model_class is set
        if self.model_class is None:
            raise AttributeError(
                "model_class must be defined for GenericConfirmDeleteView."
            )

        if not self.template:
            raise AttributeError(
                "template must be defined for GenericConfirmDeleteView."
            )

        # Retrieve the object or raise a 404 error if not found
        obj = get_object_or_404(self.model_class, pk=pk)

        context = {
            "var_name": self.var_name,
            "obj": obj,
            "delete_object": f"{self.var_name}-delete",
        }

        return render(request, self.template, context)

    @classmethod
    def as_view(
        cls, model_class=None, var_name=None, template=None, **initkwargs
    ):
        """
        Override the as_view method to allow passing custom model_class and var_name.

        Args:
            model_class: The model class of the object to delete
            var_name: Name of the object to delete

        Returns:
            A callable view.
        """
        initkwargs = {
            "model_class": model_class,
            "var_name": var_name,
            "template": template,
        }

        return super().as_view(**initkwargs)


class GenericDeleteView(PermissionRequiredMixin, View):
    permission_required = "core.add_capital"
    model_class = None
    var_name = None
    redirect = None

    def post(self, request, pk):
        """
        Handle POST requests to confirm the deletion of an object.

        Args:
            request: HttpRequest object
            pk: Primary key of the object to be deleted

        Returns:
            HttpResponse: Renders a confirmation page
        """
        # Check if the model_class is set
        if self.model_class is None:
            raise AttributeError(
                "model_class must be defined for GenericConfirmDeleteView."
            )

        # Retrieve the object or raise a 404 error if not found
        obj = get_object_or_404(self.model_class, pk=pk)

        # Delete the object
        obj.delete()

        # Display a success message
        messages.success(
            request, f"{self.var_name} has been deleted successfully."
        )

        url = reverse(
            self.redirect if self.redirect else f"{self.var_name}_list"
        )

        return redirect(url)

    @classmethod
    def as_view(
        cls, model_class=None, var_name=None, redirect=None, **initkwargs
    ):
        """
        Override the as_view method to allow passing custom model_class and var_name.

        Args:
            model_class: The model class of the object to delete
            var_name: Name of the object to delete

        Returns:
            A callable view.
        """
        initkwargs = {
            "model_class": model_class,
            "var_name": var_name,
            "redirect": redirect,
        }

        return super().as_view(**initkwargs)


class GenericListView(PermissionRequiredMixin, View):
    permission_required = "core.add_capital"  # TODO: Do we need this here?
    # raise_exception = True  # Raise 403 if permission is not met
    # login_url = "permission_denied"

    model_class = None
    var_name = None
    var_name_display = None
    var_section = None
    var_subsection = None
    var_main_desc = None
    template = None

    def get(self, request):
        """
        Handle GET requests to list objects for the given model.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: Renders the list view.
        """
        # Ensure model_class is set
        if not self.model_class:
            raise AttributeError("model_class must be defined.")

        if not self.template:
            raise AttributeError("template must be defined.")

        # Retrieve objects
        objects = self.model_class.objects.all()

        # Sorting logic
        orderby = request.GET.get("orderby", None)
        if orderby and hasattr(self.model_class, orderby):
            objects = objects.order_by(orderby)
        else:
            if (
                self.var_name == "widespread_religion"
            ):  # TODO: this should be made more generic...
                objects = objects.order_by("polity_id", "order")

        # Sorting logic
        orderby = request.GET.get("orderby", None)
        if orderby and hasattr(self.model_class, orderby):
            objects = objects.order_by(orderby)
        else:
            if self.var_name == "widespread_religion":
                objects = objects.order_by("polity_id", "order")

        # Define the ordering tag
        if self.var_name in ["official_religion", "elites_religion"]:
            ordering_tag = "coded_value_id"
        elif self.var_name == "widespread_religion":
            ordering_tag = "order"
        else:
            ordering_tag = "coded_value"

        # Context preparation
        context = {
            "object_list": objects,
            "var_name": self.var_name,
            "create_url": f"{self.var_name}-create",
            "update_url": f"{self.var_name}-update",
            "download_url": f"{self.var_name}-download",
            "pagination_url": f"{self.var_name}s",
            "metadownload_url": f"{self.var_name}-metadownload",
            "list_all_url": f"{self.var_name}s_all",
            "var_name_display": self.var_name_display,
            "ordering_tag": f"?orderby={ordering_tag}",
            "var_section": self.var_section,
            "var_subsection": self.var_subsection,
            "var_main_desc": self.var_main_desc,
            "myvar": self.var_name_display,
            "extra_var_dict": {o.id: o.show_value() for o in objects},
        }

        # Add extra information for 'inner_vars'
        context["inner_vars"] = {
            self.var_name_display: {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": f'The absence or presence of "{self.var_name_display}" for a polity.',  # noqa: E501
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }

        return render(request, self.template, context)

    @classmethod
    def as_view(
        cls,
        model_class=None,
        var_name=None,
        var_name_display=None,
        var_section=None,
        var_subsection=None,
        var_main_desc=None,
        template=None,
        **initkwargs,
    ):
        """
        Override the as_view method to pass dynamic variables to the view.

        Args:
            model_class: The model class of the objects to list.
            var_name: The name of the variable.
            var_name_display: The display name of the variable.
            var_section: The section name.
            var_subsection: The subsection name.
            var_main_desc: The main description.
            template: The template to render.

        Returns:
            A callable view.
        """
        initkwargs = {
            "model_class": model_class,
            "var_name": var_name,
            "var_name_display": var_name_display,
            "var_section": var_section,
            "var_subsection": var_subsection,
            "var_main_desc": var_main_desc,
            "template": template,
        }

        return super().as_view(**initkwargs)


class GenericCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "core.add_capital"
    # raise_exception = True
    # login_url = "permission_denied"

    form_class = None
    var_name = None
    myvar = None
    my_exp = None
    var_section = None
    var_subsection = None
    template = None

    def get_template_names(self) -> list:
        if not self.template:
            raise AttributeError(
                "template must be defined for GenericCreateView."
            )

        return [self.template]

    def get_initial(self):
        """Override to populate initial data"""
        polity_id_x = self.request.GET.get("polity_id_x")
        return {"polity": polity_id_x}

    def form_valid(self, form):
        my_object = form.save()
        return redirect(f"{self.var_name}-detail", pk=my_object.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = self.get_form()

        context = dict(
            context,
            **{
                "myvar": self.myvar,
                "my_exp": self.my_exp,
                "var_section": self.var_section,
                "var_subsection": self.var_subsection,
                "var_name_1": self.var_name,
                "var_name_2": None,
                "var_name_3": None,
                "extra_var": None,
                "extra_va2": None,
                "extra_va3r": None,
            },
        )

        if self.var_name == "widespread_religion":
            context["var_name_1"] = "order"
            context["var_name_2"] = "widespread_religion"
            context["var_name_3"] = "degree_of_prevalence"

        elif self.var_name in [
            "largest_communication_distance",
            "fastest_individual_communication",
            "military_level",
        ]:
            context["var_name_1"] = f"{self.var_name}_from"
            context["var_name_2"] = f"{self.var_name}_to"

        if "coded_value" in form:
            context.update({"extra_var": form["coded_value"]})

        if context["var_name_1"]:
            context["extra_var"] = form[context["var_name_1"]]

        if context["var_name_2"]:
            context["extra_var2"] = form[context["var_name_2"]]

        if context["var_name_3"]:
            context["extra_var3"] = form[context["var_name_3"]]

        print("Context", context)

        return context

    @classmethod
    def as_view(
        cls,
        form_class=None,
        var_name=None,
        myvar=None,
        my_exp=None,
        var_section=None,
        var_subsection=None,
        template=None,
        **initkwargs,
    ):
        print("GenericCreateView.as_view called.")
        initkwargs = {
            "form_class": form_class,
            "var_name": var_name,
            "myvar": myvar,
            "my_exp": my_exp,
            "var_section": var_section,
            "var_subsection": var_subsection,
            "template": template,
        }

        return super().as_view(**initkwargs)


class GenericUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "core.add_capital"
    # raise_exception = True
    # login_url = "permission_denied"

    model_class = None
    form_class = None
    var_name = None
    myvar = None
    my_exp = None
    var_section = None
    var_subsection = None
    delete_url_name = None
    template = None

    def get_initial(self) -> dict:
        return super().get_initial()

    def get_object(self, queryset=None):
        return get_object_or_404(self.model_class, id=self.kwargs["object_id"])

    def form_valid(self, form):
        new_object = form.save()
        return redirect(f"{self.var_name}-detail", pk=new_object.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        var_name_1 = (
            "order"
            if self.var_name == "widespread_religion"
            else (
                f"{self.var_name}_from"
                if self.var_name
                in [
                    "largest_communication_distance",
                    "fastest_individual_communication",
                    "military_level",
                ]
                else self.var_name
            )
        )
        var_name_2 = (
            "widespread_religion"
            if self.var_name == "widespread_religion"
            else (
                f"{self.var_name}_to"
                if self.var_name
                in [
                    "largest_communication_distance",
                    "fastest_individual_communication",
                    "military_level",
                ]
                else None
            )
        )
        var_name_3 = (
            "degree_of_prevalence"
            if self.var_name == "widespread_religion"
            else None
        )

        form = self.get_form()

        if self.var_name in [
            "widespread_religion",
            "largest_communication_distance",
            "fastest_individual_communication",
            "military_level",
        ]:
            context.update(
                {
                    "extra_var": form[var_name_1] if var_name_1 else None,
                    "extra_var2": form[var_name_2] if var_name_2 else None,
                    "extra_var3": form[var_name_3] if var_name_3 else None,
                }
            )
        else:
            if "coded_value" in form:
                context.update({"extra_var": form["coded_value"]})

        context.update(
            {
                "extra_var": context.get("extra_var"),
                "extra_var2": context.get("extra_var2"),
                "extra_var3": context.get("extra_var3"),
                "myvar": self.myvar,
                "my_exp": self.my_exp,
                "var_section": self.var_section,
                "var_subsection": self.var_subsection,
                "delete_url": self.delete_url_name,
            }
        )

        return context

    def get_template_names(self) -> list:
        if not self.template:
            raise AttributeError(
                "template must be defined for GenericUpdateView."
            )

        return [self.template]

    @classmethod
    def as_view(
        cls,
        model_class=None,
        form_class=None,
        var_name=None,
        myvar=None,
        my_exp=None,
        var_section=None,
        var_subsection=None,
        delete_url_name=None,
        template=None,
        **initkwargs,
    ):
        initkwargs = {
            "model_class": model_class,
            "form_class": form_class,
            "var_name": var_name,
            "myvar": myvar,
            "my_exp": my_exp,
            "var_section": var_section,
            "var_subsection": var_subsection,
            "delete_url_name": delete_url_name,
            "template": template,
        }

        return super().as_view(**initkwargs)


class GenericDetailView(PermissionRequiredMixin, UpdateView):
    # TODO: run this with gpt/copilot -- something with the form isn't matching here...

    permission_required = "core.add_capital"  # TODO: do we need this here?
    # raise_exception = True
    # login_url = "permission_denied"

    # form_class = SeshatCommentPartForm2
    model_class = None
    myvar = None
    var_name_display = None
    template = None

    def get_object(self, queryset=None):
        return get_object_or_404(self.model_class, pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO: I don't think we should bypass built-in methods like this
        form = SeshatCommentPartForm2(self.request.POST)

        context = dict(
            context,
            **{
                "myvar": self.myvar,
                "var_name_display": self.var_name_display,
                "create_new_url": f"{self.myvar}-create",
                "see_all_url": f"{self.myvar}s_all",
                "form": form,
            },
        )
        return context

    def get_template_names(self) -> list:
        if not self.template:
            raise AttributeError(
                "template must be defined for GenericUpdateView."
            )

        return [self.template]

    @classmethod
    def as_view(
        cls,
        # form_class=None,
        model_class=None,
        myvar=None,
        var_name_display=None,
        template=None,
        **initkwargs,
    ):
        """
        Override the as_view method to pass dynamic variables to the view.

        Args:
            model_class: The model class of the objects to list.
            var_name: The name of the variable.
            var_name_display: The display name of the variable.
            var_section: The section name.
            var_subsection: The subsection name.
            var_main_desc: The main description.
            template: The template to render.

        Returns:
            A callable view.
        """
        initkwargs = {
            # "form_class": form_class,
            "model_class": model_class,
            "myvar": myvar,
            "var_name_display": var_name_display,
            "template": template,
            "form_class": SeshatCommentPartForm2,
        }

        return super().as_view(**initkwargs)


class GenericDownloadView(PermissionRequiredMixin, View):
    permission_required = "core.add_capital"
    model_class = None
    var_name = None
    prefix = None

    def get(self, request):
        """
        Handle GET requests to list objects for the given model.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: Renders the list view.
        """
        # Ensure model_class is set
        if not self.model_class:
            raise AttributeError("model_class must be defined.")

        # Create a HttpResponse
        response = get_response(
            filename=f"{self.prefix}{self.var_name}_{get_date()}.csv"
        )

        # Get rows
        rowdicts = get_rowdicts(
            model_class=self.model_class, var_name=self.var_name
        )

        # Pull field names from the first row's keys
        fieldnames = list(rowdicts[0].keys())

        # Create a writer
        writer = csv.DictWriter(
            response, fieldnames=fieldnames, delimiter=CSV_DELIMITER
        )

        # Write headers + rows
        writer.writeheader()
        writer.writerows(rowdicts)

        # Return
        return response

    @classmethod
    def as_view(
        cls,
        model_class=None,
        var_name=None,
        prefix=None,
        **initkwargs,
    ):
        """
        Override the as_view method to allow passing custom model_class and var_name.

        Args:
            model_class: The model class of the object to delete
            var_name: Name of the object to delete

        Returns:
            A callable view.
        """
        initkwargs = {
            "model_class": model_class,
            "var_name": var_name,
            "prefix": prefix,
        }

        return super().as_view(**initkwargs)


class GenericMetaDownloadView(PermissionRequiredMixin, View):
    # TODO: Note in the original metadata download view, the var_name, var_name_display,
    # var_section, var_subsection, var_main_desc were all provided to the view. In this
    # rewritten model-based view, I have used the "Code" metaclass on the model itself
    # instead.

    permission_required = "core.add_capital"
    model_class = None
    var_name = None

    def get(self, request):
        """
        Handle GET requests to list objects for the given model.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: Renders the list view.
        """
        # Ensure model_class is set
        if not self.model_class:
            raise AttributeError("model_class must be defined.")

        # Create a HttpResponse
        response = get_response(filename=f"metadata_{self.var_name}s.csv")

        metadata_dict = {
            "notes": self.model_class.Code.notes or NO_DATA.note,
            "main_desc": self.model_class.Code.description,
            "main_desc_source": self.model_class.Code.description_source
            or "NOTHING",
            "section": self.model_class.Code.section,
            "subsection": self.model_class.Code.subsection,
        }

        metadata_inner_vars = self.model_class.Code.inner_variables

        writer = csv.writer(response, delimiter=CSV_DELIMITER)

        for k, v in metadata_dict.items():
            writer.writerow([k, v])

        for k_in, v_in in metadata_inner_vars.items():
            writer.writerow(
                [
                    k_in,
                ]
            )

            for inner_key, inner_value in v_in.items():
                if inner_value:
                    writer.writerow([inner_key, inner_value])

        return response

    @classmethod
    def as_view(
        cls,
        model_class=None,
        var_name=None,
        **initkwargs,
    ):
        """
        Override the as_view method to allow passing custom model_class and var_name.

        Args:
            model_class: The model class of the object to delete
            var_name: Name of the object to delete

        Returns:
            A callable view.
        """
        initkwargs = {
            "model_class": model_class,
            "var_name": var_name,
        }

        return super().as_view(**initkwargs)


# TODO: Make a download that collates all models for a subsection and downloads
# TODO: Make a download that collates all models for an app


class GenericMultipleDownloadView(PermissionRequiredMixin, View):
    permission_required = "core.add_capital"
    app_label = None
    subsection = None
    exclude_models = None
    prefix = None

    def get(self, request):
        """
        Handle GET requests to list objects for the given model.

        Args:
            request (HttpRequest): The request object.

        Returns:
            HttpResponse: Renders the list view.
        """
        t1 = time.time()

        # Ensure model_class is set
        if not self.app_label and not self.subsection:
            raise AttributeError("app_label or subsection must be defined.")

        if self.app_label and self.subsection:
            models = get_models(
                self.app_label,
                exclude=self.exclude_models,
                subsection=self.subsection,
            )
        elif self.app_label:
            models = get_models(self.app_label, exclude=self.exclude_models)

        rowdicts = []
        for model_class in models:
            rowdicts += get_rowdicts(
                model_class=model_class,
                var_name=model_class._clean_name,
                force_from_to=True,
            )

        fieldnames = [
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

        # Create a reponse
        response = get_response(filename=f"{self.prefix}{get_date()}.csv")

        # Create a writer
        writer = csv.DictWriter(
            response, fieldnames=fieldnames, delimiter=CSV_DELIMITER
        )

        # Write headers + rows
        writer.writeheader()
        writer.writerows(rowdicts)

        t2 = time.time()

        print((t2 - t1), "time to complete")  # TODO: move to logging

        return response

    @classmethod
    def as_view(
        cls,
        app_label=None,
        subsection=None,
        exclude_models=None,
        prefix=None,
        **initkwargs,
    ):
        """
        # TODO: docstring

        Returns:
            A callable view.
        """
        if not exclude_models:
            exclude_models = []

        initkwargs = {
            "app_label": app_label,
            "subsection": subsection,
            "exclude_models": exclude_models,
            "prefix": prefix,
        }

        return super().as_view(**initkwargs)


class VariableView(TemplateView):
    template_name = None
    app_label = None

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        # Add variable context
        context = dict(
            context, **get_variable_context(app_name=self.app_label)
        )

        return context

    @classmethod
    def as_view(
        cls,
        app_label=None,
        template_name=None,
        **initkwargs,
    ):
        """
        # TODO: docstring

        Returns:
            A callable view.
        """
        initkwargs = {
            "app_label": app_label,
            "template_name": template_name,
        }

        return super().as_view(**initkwargs)


class ProblematicDataView(PermissionRequiredMixin, TemplateView):
    permission_required = "core.view_capital"

    template_name = None
    app_label = None

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        # Add variable context
        context = dict(
            context, **get_problematic_data_context(app_name=self.app_label)
        )

        return context

    @classmethod
    def as_view(
        cls,
        app_label=None,
        template_name=None,
        **initkwargs,
    ):
        """
        # TODO: docstring

        Returns:
            A callable view.
        """
        initkwargs = {
            "app_label": app_label,
            "template_name": template_name,
        }

        return super().as_view(**initkwargs)
