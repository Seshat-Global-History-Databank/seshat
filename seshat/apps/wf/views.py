from django.apps import apps
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Case, When, IntegerField, F, CharField, ExpressionWrapper
from django.shortcuts import render, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..general.mixins import PolityIdMixin

from .forms import (
    Long_wallForm,
    CopperForm,
    BronzeForm,
    IronForm,
    SteelForm,
    JavelinForm,
    AtlatlForm,
    SlingForm,
    Self_bowForm,
    Composite_bowForm,
    CrossbowForm,
    Tension_siege_engineForm,
    Sling_siege_engineForm,
    Gunpowder_siege_artilleryForm,
    Handheld_firearmForm,
    War_clubForm,
    Battle_axeForm,
    DaggerForm,
    SwordForm,
    SpearForm,
    PolearmForm,
    DogForm,
    DonkeyForm,
    HorseForm,
    CamelForm,
    ElephantForm,
    Wood_bark_etcForm,
    Leather_clothForm,
    ShieldForm,
    HelmetForm,
    BreastplateForm,
    Limb_protectionForm,
    Scaled_armorForm,
    Laminar_armorForm,
    Plate_armorForm,
    Small_vessels_canoes_etcForm,
    Merchant_ships_pressed_into_serviceForm,
    Specialized_military_vesselForm,
    Settlements_in_a_defensive_positionForm,
    Wooden_palisadeForm,
    Earth_rampartForm,
    DitchForm,
    MoatForm,
    Stone_walls_non_mortaredForm,
    Stone_walls_mortaredForm,
    Fortified_campForm,
    Complex_fortificationForm,
    Modern_fortificationForm,
    ChainmailForm,
)
from .models import (
    Long_wall,
    Copper,
    Bronze,
    Iron,
    Steel,
    Javelin,
    Atlatl,
    Sling,
    Self_bow,
    Composite_bow,
    Crossbow,
    Tension_siege_engine,
    Sling_siege_engine,
    Gunpowder_siege_artillery,
    Handheld_firearm,
    War_club,
    Battle_axe,
    Dagger,
    Sword,
    Spear,
    Polearm,
    Dog,
    Donkey,
    Horse,
    Camel,
    Elephant,
    Wood_bark_etc,
    Leather_cloth,
    Shield,
    Helmet,
    Breastplate,
    Limb_protection,
    Scaled_armor,
    Laminar_armor,
    Plate_armor,
    Small_vessels_canoes_etc,
    Merchant_ships_pressed_into_service,
    Specialized_military_vessel,
    Settlements_in_a_defensive_position,
    Wooden_palisade,
    Earth_rampart,
    Ditch,
    Moat,
    Stone_walls_non_mortared,
    Stone_walls_mortared,
    Fortified_camp,
    Complex_fortification,
    Modern_fortification,
    Chainmail,
)

import csv
import datetime


class Long_wallCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Long_wall
    form_class = Long_wallForm
    template_name = "wf/long_wall/long_wall_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("long_wall-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Long Wall"
        context["my_exp"] = (
            "The absence or presence or height of long walls. (code absent as number zero on the long_wall_from / and for coding  'unknown', keep the long_wall_from and long_wall_to empty and only select the confidence etc.)"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "long_wall": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence or height of long walls for a polity.",
                "units": "km",
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Long_wallUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Long_wall
    form_class = Long_wallForm
    template_name = "wf/long_wall/long_wall_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Long Wall"
        context["my_exp"] = (
            "The absence or presence or height of long walls. (code absent as number zero on the long_wall_from / and for coding  'unknown', keep the long_wall_from and long_wall_to empty and only select the confidence etc.)"
        )

        return context


class Long_wallDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Long_wall
    success_url = reverse_lazy("long_walls")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Long_wallListView(generic.ListView):
    """ """

    model = Long_wall
    template_name = "wf/long_wall/long_wall_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("long_walls")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Long Wall"
        context["my_exp"] = "The absence or presence or height of long walls."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military Technologies"
        context["inner_vars"] = {
            "long_wall": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence or height of long walls for a polity.",
                "units": "km",
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Long_wallListViewAll(generic.ListView):
    """ """

    model = Long_wall
    template_name = "wf/long_wall/long_wall_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("long_walls_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Long_wall.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Long Wall"
        context["var_main_desc"] = "The absence or presence or height of long walls."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military Technologies"
        context["inner_vars"] = {
            "long_wall": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence or height of long walls for a polity.",
                "units": "km",
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Long_wallDetailView(generic.DetailView):
    """ """

    model = Long_wall
    template_name = "wf/long_wall/long_wall_detail.html"


@permission_required("core.view_capital")
def long_wall_download(request):
    items = Long_wall.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_long_walls_{current_datetime}.csv"
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
            "long_wall_from",
            "long_wall_to",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.show_value_from(),
                obj.show_value_to(),
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def long_wall_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="long_walls.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence or height of long walls. (code absent as number zero on the long_wall_from / and for coding  'unknown', keep the long_wall_from and long_wall_to empty and only select the confidence etc.)",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Military Technologies",
    }
    my_meta_data_dic_inner_vars = {
        "long_wall": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence or height of long walls for a polity.",
            "units": "km",
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


#########################


class CopperCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Copper
    form_class = CopperForm
    template_name = "wf/copper/copper_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("copper-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Copper"
        context["my_exp"] = (
            "The absence or presence of copper as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "copper": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of copper for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class CopperUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Copper
    form_class = CopperForm
    template_name = "wf/copper/copper_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Copper"
        context["my_exp"] = (
            "The absence or presence of copper as a military technology used in warfare. "
        )

        return context


class CopperDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Copper
    success_url = reverse_lazy("coppers")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CopperListView(generic.ListView):
    """ """

    model = Copper
    template_name = "wf/copper/copper_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("coppers")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Copper"
        context["var_main_desc"] = (
            "The absence or presence of copper as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military use of Metals"
        context["inner_vars"] = {
            "copper": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of copper for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class CopperListViewAll(generic.ListView):
    """ """

    model = Copper
    template_name = "wf/copper/copper_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("coppers_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Copper.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Copper"
        context["var_main_desc"] = (
            "The absence or presence of copper as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military use of Metals"
        context["inner_vars"] = {
            "copper": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of copper for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class CopperDetailView(generic.DetailView):
    """ """

    model = Copper
    template_name = "wf/copper/copper_detail.html"


@permission_required("core.view_capital")
def copper_download(request):
    items = Copper.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_coppers_{current_datetime}.csv"
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
            "copper",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.copper,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def copper_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="coppers.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of copper as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Military use of Metals",
    }
    my_meta_data_dic_inner_vars = {
        "copper": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of copper for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class BronzeCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Bronze
    form_class = BronzeForm
    template_name = "wf/bronze/bronze_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("bronze-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Bronze"
        context["my_exp"] = (
            "The absence or presence of bronze as a military technology used in warfare. Bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "bronze": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of bronze for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class BronzeUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Bronze
    form_class = BronzeForm
    template_name = "wf/bronze/bronze_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Bronze"
        context["my_exp"] = (
            "The absence or presence of bronze as a military technology used in warfare. Bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best."
        )

        return context


class BronzeDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Bronze
    success_url = reverse_lazy("bronzes")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class BronzeListView(generic.ListView):
    """ """

    model = Bronze
    template_name = "wf/bronze/bronze_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("bronzes")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Bronze"
        context["var_main_desc"] = (
            "The absence or presence of bronze as a military technology used in warfare. bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military use of Metals"
        context["inner_vars"] = {
            "bronze": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of bronze for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class BronzeListViewAll(generic.ListView):
    """ """

    model = Bronze
    template_name = "wf/bronze/bronze_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("bronzes_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Bronze.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Bronze"
        context["var_main_desc"] = (
            "The absence or presence of bronze as a military technology used in warfare. bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military use of Metals"
        context["inner_vars"] = {
            "bronze": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of bronze for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class BronzeDetailView(generic.DetailView):
    """ """

    model = Bronze
    template_name = "wf/bronze/bronze_detail.html"


@permission_required("core.view_capital")
def bronze_download(request):
    items = Bronze.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_bronzes_{current_datetime}.csv"
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
            "bronze",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.bronze,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def bronze_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="bronzes.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of bronze as a military technology used in warfare. Bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Military use of Metals",
    }
    my_meta_data_dic_inner_vars = {
        "bronze": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of bronze for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class IronCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Iron
    form_class = IronForm
    template_name = "wf/iron/iron_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("iron-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Iron"
        context["my_exp"] = (
            "The absence or presence of iron as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "iron": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of iron for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class IronUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Iron
    form_class = IronForm
    template_name = "wf/iron/iron_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Iron"
        context["my_exp"] = (
            "The absence or presence of iron as a military technology used in warfare. "
        )

        return context


class IronDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Iron
    success_url = reverse_lazy("irons")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class IronListView(generic.ListView):
    """ """

    model = Iron
    template_name = "wf/iron/iron_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("irons")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Iron"
        context["var_main_desc"] = (
            "The absence or presence of iron as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military use of Metals"
        context["inner_vars"] = {
            "iron": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of iron for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class IronListViewAll(generic.ListView):
    """ """

    model = Iron
    template_name = "wf/iron/iron_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("irons_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Iron.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Iron"
        context["var_main_desc"] = (
            "The absence or presence of iron as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military use of Metals"
        context["inner_vars"] = {
            "iron": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of iron for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class IronDetailView(generic.DetailView):
    """ """

    model = Iron
    template_name = "wf/iron/iron_detail.html"


@permission_required("core.view_capital")
def iron_download(request):
    items = Iron.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_irons_{current_datetime}.csv"
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
            "iron",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.iron,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def iron_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="irons.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of iron as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Military use of Metals",
    }
    my_meta_data_dic_inner_vars = {
        "iron": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of iron for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class SteelCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Steel
    form_class = SteelForm
    template_name = "wf/steel/steel_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("steel-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Steel"
        context["my_exp"] = (
            "The absence or presence of steel as a military technology used in warfare. Steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "steel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of steel for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class SteelUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Steel
    form_class = SteelForm
    template_name = "wf/steel/steel_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Steel"
        context["my_exp"] = (
            "The absence or presence of steel as a military technology used in warfare. Steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best."
        )

        return context


class SteelDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Steel
    success_url = reverse_lazy("steels")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SteelListView(generic.ListView):
    """ """

    model = Steel
    template_name = "wf/steel/steel_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("steels")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Steel"
        context["var_main_desc"] = (
            "The absence or presence of steel as a military technology used in warfare. steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military use of Metals"
        context["inner_vars"] = {
            "steel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of steel for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class SteelListViewAll(generic.ListView):
    """ """

    model = Steel
    template_name = "wf/steel/steel_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("steels_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Steel.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Steel"
        context["var_main_desc"] = (
            "The absence or presence of steel as a military technology used in warfare. steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Military use of Metals"
        context["inner_vars"] = {
            "steel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of steel for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class SteelDetailView(generic.DetailView):
    """ """

    model = Steel
    template_name = "wf/steel/steel_detail.html"


@permission_required("core.view_capital")
def steel_download(request):
    items = Steel.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_steels_{current_datetime}.csv"
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
            "steel",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.steel,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def steel_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="steels.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of steel as a military technology used in warfare. Steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Military use of Metals",
    }
    my_meta_data_dic_inner_vars = {
        "steel": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of steel for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class JavelinCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Javelin
    form_class = JavelinForm
    template_name = "wf/javelin/javelin_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("javelin-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Javelin"
        context["my_exp"] = (
            "The absence or presence of javelins as a military technology used in warfare. Includes thrown spears"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "javelin": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of javelin for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class JavelinUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Javelin
    form_class = JavelinForm
    template_name = "wf/javelin/javelin_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Javelin"
        context["my_exp"] = (
            "The absence or presence of javelins as a military technology used in warfare. Includes thrown spears"
        )

        return context


class JavelinDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Javelin
    success_url = reverse_lazy("javelins")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class JavelinListView(generic.ListView):
    """ """

    model = Javelin
    template_name = "wf/javelin/javelin_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("javelins")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Javelin"
        context["var_main_desc"] = (
            "The absence or presence of javelins as a military technology used in warfare. includes thrown spears"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "javelin": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of javelin for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class JavelinListViewAll(generic.ListView):
    """ """

    model = Javelin
    template_name = "wf/javelin/javelin_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("javelins_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Javelin.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Javelin"
        context["var_main_desc"] = (
            "The absence or presence of javelins as a military technology used in warfare. includes thrown spears"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "javelin": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of javelin for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class JavelinDetailView(generic.DetailView):
    """ """

    model = Javelin
    template_name = "wf/javelin/javelin_detail.html"


@permission_required("core.view_capital")
def javelin_download(request):
    items = Javelin.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_javelins_{current_datetime}.csv"
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
            "javelin",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.javelin,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def javelin_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="javelins.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of javelins as a military technology used in warfare. Includes thrown spears",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "javelin": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of javelin for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class AtlatlCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Atlatl
    form_class = AtlatlForm
    template_name = "wf/atlatl/atlatl_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("atlatl-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Atlatl"
        context["my_exp"] = (
            "The absence or presence of atlatl as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "atlatl": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of atlatl for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class AtlatlUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Atlatl
    form_class = AtlatlForm
    template_name = "wf/atlatl/atlatl_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Atlatl"
        context["my_exp"] = (
            "The absence or presence of atlatl as a military technology used in warfare. "
        )

        return context


class AtlatlDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Atlatl
    success_url = reverse_lazy("atlatls")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class AtlatlListView(generic.ListView):
    """ """

    model = Atlatl
    template_name = "wf/atlatl/atlatl_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("atlatls")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Atlatl"
        context["var_main_desc"] = (
            "The absence or presence of atlatl as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "atlatl": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of atlatl for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class AtlatlListViewAll(generic.ListView):
    """ """

    model = Atlatl
    template_name = "wf/atlatl/atlatl_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("atlatls_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Atlatl.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Atlatl"
        context["var_main_desc"] = (
            "The absence or presence of atlatl as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "atlatl": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of atlatl for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class AtlatlDetailView(generic.DetailView):
    """ """

    model = Atlatl
    template_name = "wf/atlatl/atlatl_detail.html"


@permission_required("core.view_capital")
def atlatl_download(request):
    items = Atlatl.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_atlatls_{current_datetime}.csv"
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
            "atlatl",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.atlatl,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def atlatl_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="atlatls.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of atlatl as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "atlatl": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of atlatl for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class SlingCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling
    form_class = SlingForm
    template_name = "wf/sling/sling_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sling-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Sling"
        context["my_exp"] = (
            "The absence or presence of slings as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "sling": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sling for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class SlingUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling
    form_class = SlingForm
    template_name = "wf/sling/sling_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sling"
        context["my_exp"] = (
            "The absence or presence of slings as a military technology used in warfare. "
        )

        return context


class SlingDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling
    success_url = reverse_lazy("slings")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SlingListView(generic.ListView):
    """ """

    model = Sling
    template_name = "wf/sling/sling_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("slings")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sling"
        context["var_main_desc"] = (
            "The absence or presence of slings as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "sling": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sling for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class SlingListViewAll(generic.ListView):
    """ """

    model = Sling
    template_name = "wf/sling/sling_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("slings_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Sling.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sling"
        context["var_main_desc"] = (
            "The absence or presence of slings as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "sling": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sling for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class SlingDetailView(generic.DetailView):
    """ """

    model = Sling
    template_name = "wf/sling/sling_detail.html"


@permission_required("core.view_capital")
def sling_download(request):
    items = Sling.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_slings_{current_datetime}.csv"
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
            "sling",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.sling,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def sling_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="slings.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of slings as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "sling": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of sling for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Self_bowCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Self_bow
    form_class = Self_bowForm
    template_name = "wf/self_bow/self_bow_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("self_bow-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Self Bow"
        context["my_exp"] = (
            "The absence or presence of self bow as a military technology used in warfare. This is a bow made from a single piece of wood (example: the English/Welsh longbow)"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "self_bow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of self bow for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Self_bowUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Self_bow
    form_class = Self_bowForm
    template_name = "wf/self_bow/self_bow_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Self Bow"
        context["my_exp"] = (
            "The absence or presence of self bow as a military technology used in warfare. This is a bow made from a single piece of wood (example: the English/Welsh longbow)"
        )

        return context


class Self_bowDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Self_bow
    success_url = reverse_lazy("self_bows")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Self_bowListView(generic.ListView):
    """ """

    model = Self_bow
    template_name = "wf/self_bow/self_bow_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("self_bows")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Self Bow"
        context["var_main_desc"] = (
            "The absence or presence of self bow as a military technology used in warfare. this is a bow made from a single piece of wood (example: the english/welsh longbow)"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "self_bow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of self bow for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Self_bowListViewAll(generic.ListView):
    """ """

    model = Self_bow
    template_name = "wf/self_bow/self_bow_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("self_bows_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Self_bow.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Self Bow"
        context["var_main_desc"] = (
            "The absence or presence of self bow as a military technology used in warfare. this is a bow made from a single piece of wood (example: the english/welsh longbow)"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "self_bow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of self bow for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Self_bowDetailView(generic.DetailView):
    """ """

    model = Self_bow
    template_name = "wf/self_bow/self_bow_detail.html"


@permission_required("core.view_capital")
def self_bow_download(request):
    items = Self_bow.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_self_bows_{current_datetime}.csv"
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
            "self_bow",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.self_bow,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def self_bow_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="self_bows.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of self bow as a military technology used in warfare. This is a bow made from a single piece of wood (example: the English/Welsh longbow)",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "self_bow": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of self bow for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Composite_bowCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Composite_bow
    form_class = Composite_bowForm
    template_name = "wf/composite_bow/composite_bow_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("composite_bow-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Composite Bow"
        context["my_exp"] = (
            "The absence or presence of composite bow as a military technology used in warfare. This is a bow made from several different materials, usually wood, horn, and sinew. Also known as laminated bow. Recurved bows should be coded here as well, because usually they are composite bows. When there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present)."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "composite_bow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of composite bow for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Composite_bowUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Composite_bow
    form_class = Composite_bowForm
    template_name = "wf/composite_bow/composite_bow_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Composite Bow"
        context["my_exp"] = (
            "The absence or presence of composite bow as a military technology used in warfare. This is a bow made from several different materials, usually wood, horn, and sinew. Also known as laminated bow. Recurved bows should be coded here as well, because usually they are composite bows. When there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present)."
        )

        return context


class Composite_bowDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Composite_bow
    success_url = reverse_lazy("composite_bows")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Composite_bowListView(generic.ListView):
    """ """

    model = Composite_bow
    template_name = "wf/composite_bow/composite_bow_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("composite_bows")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Composite Bow"
        context["var_main_desc"] = (
            "The absence or presence of composite bow as a military technology used in warfare. this is a bow made from several different materials, usually wood, horn, and sinew. also known as laminated bow. recurved bows should be coded here as well, because usually they are composite bows. when there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present)."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "composite_bow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of composite bow for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Composite_bowListViewAll(generic.ListView):
    """ """

    model = Composite_bow
    template_name = "wf/composite_bow/composite_bow_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("composite_bows_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Composite_bow.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Composite Bow"
        context["var_main_desc"] = (
            "The absence or presence of composite bow as a military technology used in warfare. this is a bow made from several different materials, usually wood, horn, and sinew. also known as laminated bow. recurved bows should be coded here as well, because usually they are composite bows. when there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present)."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "composite_bow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of composite bow for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Composite_bowDetailView(generic.DetailView):
    """ """

    model = Composite_bow
    template_name = "wf/composite_bow/composite_bow_detail.html"


@permission_required("core.view_capital")
def composite_bow_download(request):
    items = Composite_bow.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_composite_bows_{current_datetime}.csv"
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
            "composite_bow",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.composite_bow,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def composite_bow_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="composite_bows.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of composite bow as a military technology used in warfare. This is a bow made from several different materials, usually wood, horn, and sinew. Also known as laminated bow. Recurved bows should be coded here as well, because usually they are composite bows. When there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present).",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "composite_bow": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of composite bow for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class CrossbowCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Crossbow
    form_class = CrossbowForm
    template_name = "wf/crossbow/crossbow_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("crossbow-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Crossbow"
        context["my_exp"] = (
            "The absence or presence of crossbow as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "crossbow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of crossbow for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class CrossbowUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Crossbow
    form_class = CrossbowForm
    template_name = "wf/crossbow/crossbow_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Crossbow"
        context["my_exp"] = (
            "The absence or presence of crossbow as a military technology used in warfare. "
        )

        return context


class CrossbowDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Crossbow
    success_url = reverse_lazy("crossbows")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CrossbowListView(generic.ListView):
    """ """

    model = Crossbow
    template_name = "wf/crossbow/crossbow_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("crossbows")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Crossbow"
        context["var_main_desc"] = (
            "The absence or presence of crossbow as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "crossbow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of crossbow for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class CrossbowListViewAll(generic.ListView):
    """ """

    model = Crossbow
    template_name = "wf/crossbow/crossbow_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("crossbows_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Crossbow.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Crossbow"
        context["var_main_desc"] = (
            "The absence or presence of crossbow as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "crossbow": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of crossbow for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class CrossbowDetailView(generic.DetailView):
    """ """

    model = Crossbow
    template_name = "wf/crossbow/crossbow_detail.html"


@permission_required("core.view_capital")
def crossbow_download(request):
    items = Crossbow.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_crossbows_{current_datetime}.csv"
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
            "crossbow",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.crossbow,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def crossbow_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="crossbows.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of crossbow as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "crossbow": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of crossbow for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Tension_siege_engineCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Tension_siege_engine
    form_class = Tension_siege_engineForm
    template_name = "wf/tension_siege_engine/tension_siege_engine_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("tension_siege_engine-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Tension Siege Engine"
        context["my_exp"] = (
            "The absence or presence of tension siege engines as a military technology used in warfare. For example, catapult, onager"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "tension_siege_engine": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of tension siege engine for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Tension_siege_engineUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Tension_siege_engine
    form_class = Tension_siege_engineForm
    template_name = "wf/tension_siege_engine/tension_siege_engine_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Tension Siege Engine"
        context["my_exp"] = (
            "The absence or presence of tension siege engines as a military technology used in warfare. For example, catapult, onager"
        )

        return context


class Tension_siege_engineDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Tension_siege_engine
    success_url = reverse_lazy("tension_siege_engines")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Tension_siege_engineListView(generic.ListView):
    """ """

    model = Tension_siege_engine
    template_name = "wf/tension_siege_engine/tension_siege_engine_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("tension_siege_engines")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Tension Siege Engine"
        context["var_main_desc"] = (
            "The absence or presence of tension siege engines as a military technology used in warfare. for example, catapult, onager"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "tension_siege_engine": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of tension siege engine for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Tension_siege_engineListViewAll(generic.ListView):
    """ """

    model = Tension_siege_engine
    template_name = "wf/tension_siege_engine/tension_siege_engine_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("tension_siege_engines_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Tension_siege_engine.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Tension Siege Engine"
        context["var_main_desc"] = (
            "The absence or presence of tension siege engines as a military technology used in warfare. for example, catapult, onager"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "tension_siege_engine": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of tension siege engine for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Tension_siege_engineDetailView(generic.DetailView):
    """ """

    model = Tension_siege_engine
    template_name = "wf/tension_siege_engine/tension_siege_engine_detail.html"


@permission_required("core.view_capital")
def tension_siege_engine_download(request):
    items = Tension_siege_engine.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_tension_siege_engines_{current_datetime}.csv"
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
            "tension_siege_engine",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.tension_siege_engine,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def tension_siege_engine_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="tension_siege_engines.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of tension siege engines as a military technology used in warfare. For example, catapult, onager",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "tension_siege_engine": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of tension siege engine for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Sling_siege_engineCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling_siege_engine
    form_class = Sling_siege_engineForm
    template_name = "wf/sling_siege_engine/sling_siege_engine_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sling_siege_engine-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Sling Siege Engine"
        context["my_exp"] = (
            "The absence or presence of sling siege engines as a military technology used in warfare. E.g., trebuchet, innclude mangonels here"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "sling_siege_engine": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sling siege engine for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Sling_siege_engineUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling_siege_engine
    form_class = Sling_siege_engineForm
    template_name = "wf/sling_siege_engine/sling_siege_engine_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sling Siege Engine"
        context["my_exp"] = (
            "The absence or presence of sling siege engines as a military technology used in warfare. E.g., trebuchet, innclude mangonels here"
        )

        return context


class Sling_siege_engineDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling_siege_engine
    success_url = reverse_lazy("sling_siege_engines")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Sling_siege_engineListView(generic.ListView):
    """ """

    model = Sling_siege_engine
    template_name = "wf/sling_siege_engine/sling_siege_engine_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sling_siege_engines")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sling Siege Engine"
        context["var_main_desc"] = (
            "The absence or presence of sling siege engines as a military technology used in warfare. e.g., trebuchet, innclude mangonels here"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "sling_siege_engine": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sling siege engine for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Sling_siege_engineListViewAll(generic.ListView):
    """ """

    model = Sling_siege_engine
    template_name = "wf/sling_siege_engine/sling_siege_engine_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sling_siege_engines_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Sling_siege_engine.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sling Siege Engine"
        context["var_main_desc"] = (
            "The absence or presence of sling siege engines as a military technology used in warfare. e.g., trebuchet, innclude mangonels here"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "sling_siege_engine": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sling siege engine for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Sling_siege_engineDetailView(generic.DetailView):
    """ """

    model = Sling_siege_engine
    template_name = "wf/sling_siege_engine/sling_siege_engine_detail.html"


@permission_required("core.view_capital")
def sling_siege_engine_download(request):
    items = Sling_siege_engine.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_sling_siege_engines_{current_datetime}.csv"
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
            "sling_siege_engine",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.sling_siege_engine,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def sling_siege_engine_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="sling_siege_engines.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of sling siege engines as a military technology used in warfare. E.g., trebuchet, innclude mangonels here",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "sling_siege_engine": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of sling siege engine for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Gunpowder_siege_artilleryCreate(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Gunpowder_siege_artillery
    form_class = Gunpowder_siege_artilleryForm
    template_name = "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("gunpowder_siege_artillery-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Gunpowder Siege Artillery"
        context["my_exp"] = (
            "The absence or presence of gunpowder siege artillery as a military technology used in warfare. For example, cannon, mortars."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "gunpowder_siege_artillery": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of gunpowder siege artillery for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Gunpowder_siege_artilleryUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Gunpowder_siege_artillery
    form_class = Gunpowder_siege_artilleryForm
    template_name = "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gunpowder Siege Artillery"
        context["my_exp"] = (
            "The absence or presence of gunpowder siege artillery as a military technology used in warfare. For example, cannon, mortars."
        )

        return context


class Gunpowder_siege_artilleryDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Gunpowder_siege_artillery
    success_url = reverse_lazy("gunpowder_siege_artillerys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Gunpowder_siege_artilleryListView(generic.ListView):
    """ """

    model = Gunpowder_siege_artillery
    template_name = "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("gunpowder_siege_artillerys")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gunpowder Siege Artillery"
        context["var_main_desc"] = (
            "The absence or presence of gunpowder siege artillery as a military technology used in warfare. for example, cannon, mortars."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "gunpowder_siege_artillery": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of gunpowder siege artillery for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Gunpowder_siege_artilleryListViewAll(generic.ListView):
    """ """

    model = Gunpowder_siege_artillery
    template_name = (
        "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_list_all.html"
    )

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("gunpowder_siege_artillerys_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Gunpowder_siege_artillery.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Gunpowder Siege Artillery"
        context["var_main_desc"] = (
            "The absence or presence of gunpowder siege artillery as a military technology used in warfare. for example, cannon, mortars."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "gunpowder_siege_artillery": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of gunpowder siege artillery for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Gunpowder_siege_artilleryDetailView(generic.DetailView):
    """ """

    model = Gunpowder_siege_artillery
    template_name = "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_detail.html"


@permission_required("core.view_capital")
def gunpowder_siege_artillery_download(request):
    items = Gunpowder_siege_artillery.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_gunpowder_siege_artillerys_{current_datetime}.csv"
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
            "gunpowder_siege_artillery",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.gunpowder_siege_artillery,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def gunpowder_siege_artillery_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="gunpowder_siege_artillerys.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of gunpowder siege artillery as a military technology used in warfare. For example, cannon, mortars.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "gunpowder_siege_artillery": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of gunpowder siege artillery for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Handheld_firearmCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Handheld_firearm
    form_class = Handheld_firearmForm
    template_name = "wf/handheld_firearm/handheld_firearm_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("handheld_firearm-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Handheld Firearm"
        context["my_exp"] = (
            "The absence or presence of handheld firearms as a military technology used in warfare. E.g., muskets, pistols, and rifles"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "handheld_firearm": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of handheld firearm for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Handheld_firearmUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Handheld_firearm
    form_class = Handheld_firearmForm
    template_name = "wf/handheld_firearm/handheld_firearm_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Handheld Firearm"
        context["my_exp"] = (
            "The absence or presence of handheld firearms as a military technology used in warfare. E.g., muskets, pistols, and rifles"
        )

        return context


class Handheld_firearmDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Handheld_firearm
    success_url = reverse_lazy("handheld_firearms")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Handheld_firearmListView(generic.ListView):
    """ """

    model = Handheld_firearm
    template_name = "wf/handheld_firearm/handheld_firearm_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("handheld_firearms")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Handheld Firearm"
        context["var_main_desc"] = (
            "The absence or presence of handheld firearms as a military technology used in warfare. e.g., muskets, pistols, and rifles"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "handheld_firearm": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of handheld firearm for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Handheld_firearmListViewAll(generic.ListView):
    """ """

    model = Handheld_firearm
    template_name = "wf/handheld_firearm/handheld_firearm_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("handheld_firearms_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Handheld_firearm.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Handheld Firearm"
        context["var_main_desc"] = (
            "The absence or presence of handheld firearms as a military technology used in warfare. e.g., muskets, pistols, and rifles"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Projectiles"
        context["inner_vars"] = {
            "handheld_firearm": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of handheld firearm for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Handheld_firearmDetailView(generic.DetailView):
    """ """

    model = Handheld_firearm
    template_name = "wf/handheld_firearm/handheld_firearm_detail.html"


@permission_required("core.view_capital")
def handheld_firearm_download(request):
    items = Handheld_firearm.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_handheld_firearms_{current_datetime}.csv"
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
            "handheld_firearm",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.handheld_firearm,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def handheld_firearm_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="handheld_firearms.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of handheld firearms as a military technology used in warfare. E.g., muskets, pistols, and rifles",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Projectiles",
    }
    my_meta_data_dic_inner_vars = {
        "handheld_firearm": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of handheld firearm for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class War_clubCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = War_club
    form_class = War_clubForm
    template_name = "wf/war_club/war_club_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("war_club-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "War Club"
        context["my_exp"] = (
            "The absence or presence of war clubs as a military technology used in warfare. Includes maces"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "war_club": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of war club for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class War_clubUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = War_club
    form_class = War_clubForm
    template_name = "wf/war_club/war_club_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "War Club"
        context["my_exp"] = (
            "The absence or presence of war clubs as a military technology used in warfare. Includes maces"
        )

        return context


class War_clubDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = War_club
    success_url = reverse_lazy("war_clubs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class War_clubListView(generic.ListView):
    """ """

    model = War_club
    template_name = "wf/war_club/war_club_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("war_clubs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "War Club"
        context["var_main_desc"] = (
            "The absence or presence of war clubs as a military technology used in warfare. includes maces"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "war_club": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of war club for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class War_clubListViewAll(generic.ListView):
    """ """

    model = War_club
    template_name = "wf/war_club/war_club_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("war_clubs_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            War_club.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "War Club"
        context["var_main_desc"] = (
            "The absence or presence of war clubs as a military technology used in warfare. includes maces"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "war_club": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of war club for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class War_clubDetailView(generic.DetailView):
    """ """

    model = War_club
    template_name = "wf/war_club/war_club_detail.html"


@permission_required("core.view_capital")
def war_club_download(request):
    items = War_club.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_war_clubs_{current_datetime}.csv"
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
            "war_club",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.war_club,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def war_club_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="war_clubs.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of war clubs as a military technology used in warfare. Includes maces",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Handheld weapons",
    }
    my_meta_data_dic_inner_vars = {
        "war_club": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of war club for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Battle_axeCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Battle_axe
    form_class = Battle_axeForm
    template_name = "wf/battle_axe/battle_axe_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("battle_axe-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Battle Axe"
        context["my_exp"] = (
            "The absence or presence of battle axes as a military technology used in warfare. Axes designed for military use."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "battle_axe": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of battle axe for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Battle_axeUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Battle_axe
    form_class = Battle_axeForm
    template_name = "wf/battle_axe/battle_axe_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Battle Axe"
        context["my_exp"] = (
            "The absence or presence of battle axes as a military technology used in warfare. Axes designed for military use."
        )

        return context


class Battle_axeDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Battle_axe
    success_url = reverse_lazy("battle_axes")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Battle_axeListView(generic.ListView):
    """ """

    model = Battle_axe
    template_name = "wf/battle_axe/battle_axe_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("battle_axes")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Battle Axe"
        context["var_main_desc"] = (
            "The absence or presence of battle axes as a military technology used in warfare. axes designed for military use."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "battle_axe": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of battle axe for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Battle_axeListViewAll(generic.ListView):
    """ """

    model = Battle_axe
    template_name = "wf/battle_axe/battle_axe_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("battle_axes_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Battle_axe.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Battle Axe"
        context["var_main_desc"] = (
            "The absence or presence of battle axes as a military technology used in warfare. axes designed for military use."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "battle_axe": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of battle axe for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Battle_axeDetailView(generic.DetailView):
    """ """

    model = Battle_axe
    template_name = "wf/battle_axe/battle_axe_detail.html"


@permission_required("core.view_capital")
def battle_axe_download(request):
    items = Battle_axe.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_battle_axes_{current_datetime}.csv"
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
            "battle_axe",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.battle_axe,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def battle_axe_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="battle_axes.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of battle axes as a military technology used in warfare. Axes designed for military use.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Handheld weapons",
    }
    my_meta_data_dic_inner_vars = {
        "battle_axe": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of battle axe for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class DaggerCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dagger
    form_class = DaggerForm
    template_name = "wf/dagger/dagger_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("dagger-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Dagger"
        context["my_exp"] = (
            "The absence or presence of daggers as a military technology used in warfare. Bladed weapons shorter than 50 cm. Includes knives. Material is not important (coded elsewhere), thus flint daggers should be coded as present."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "dagger": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of dagger for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class DaggerUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dagger
    form_class = DaggerForm
    template_name = "wf/dagger/dagger_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Dagger"
        context["my_exp"] = (
            "The absence or presence of daggers as a military technology used in warfare. Bladed weapons shorter than 50 cm. Includes knives. Material is not important (coded elsewhere), thus flint daggers should be coded as present."
        )

        return context


class DaggerDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dagger
    success_url = reverse_lazy("daggers")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class DaggerListView(generic.ListView):
    """ """

    model = Dagger
    template_name = "wf/dagger/dagger_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("daggers")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Dagger"
        context["var_main_desc"] = (
            "The absence or presence of daggers as a military technology used in warfare. bladed weapons shorter than 50 cm. includes knives. material is not important (coded elsewhere), thus flint daggers should be coded as present."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "dagger": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of dagger for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class DaggerListViewAll(generic.ListView):
    """ """

    model = Dagger
    template_name = "wf/dagger/dagger_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("daggers_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Dagger.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Dagger"
        context["var_main_desc"] = (
            "The absence or presence of daggers as a military technology used in warfare. bladed weapons shorter than 50 cm. includes knives. material is not important (coded elsewhere), thus flint daggers should be coded as present."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "dagger": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of dagger for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class DaggerDetailView(generic.DetailView):
    """ """

    model = Dagger
    template_name = "wf/dagger/dagger_detail.html"


@permission_required("core.view_capital")
def dagger_download(request):
    items = Dagger.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_daggers_{current_datetime}.csv"
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
            "dagger",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.dagger,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def dagger_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="daggers.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of daggers as a military technology used in warfare. Bladed weapons shorter than 50 cm. Includes knives. Material is not important (coded elsewhere), thus flint daggers should be coded as present.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Handheld weapons",
    }
    my_meta_data_dic_inner_vars = {
        "dagger": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of dagger for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class SwordCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sword
    form_class = SwordForm
    template_name = "wf/sword/sword_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sword-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Sword"
        context["my_exp"] = (
            "The absence or presence of swords as a military technology used in warfare. Bladed weapons longer than 50 cm. A machete is a sword (assuming the blade is probably longer than 50 cm). Material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "sword": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sword for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class SwordUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sword
    form_class = SwordForm
    template_name = "wf/sword/sword_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sword"
        context["my_exp"] = (
            "The absence or presence of swords as a military technology used in warfare. Bladed weapons longer than 50 cm. A machete is a sword (assuming the blade is probably longer than 50 cm). Material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present."
        )

        return context


class SwordDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sword
    success_url = reverse_lazy("swords")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SwordListView(generic.ListView):
    """ """

    model = Sword
    template_name = "wf/sword/sword_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("swords")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sword"
        context["var_main_desc"] = (
            "The absence or presence of swords as a military technology used in warfare. bladed weapons longer than 50 cm. a machete is a sword (assuming the blade is probably longer than 50 cm). material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "sword": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sword for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class SwordListViewAll(generic.ListView):
    """ """

    model = Sword
    template_name = "wf/sword/sword_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("swords_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Sword.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sword"
        context["var_main_desc"] = (
            "The absence or presence of swords as a military technology used in warfare. bladed weapons longer than 50 cm. a machete is a sword (assuming the blade is probably longer than 50 cm). material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "sword": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sword for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class SwordDetailView(generic.DetailView):
    """ """

    model = Sword
    template_name = "wf/sword/sword_detail.html"


@permission_required("core.view_capital")
def sword_download(request):
    items = Sword.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_swords_{current_datetime}.csv"
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
            "sword",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.sword,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def sword_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="swords.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of swords as a military technology used in warfare. Bladed weapons longer than 50 cm. A machete is a sword (assuming the blade is probably longer than 50 cm). Material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Handheld weapons",
    }
    my_meta_data_dic_inner_vars = {
        "sword": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of sword for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class SpearCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Spear
    form_class = SpearForm
    template_name = "wf/spear/spear_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("spear-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Spear"
        context["my_exp"] = (
            "The absence or presence of spears as a military technology used in warfare. Includes lances and pikes. A trident is a spear."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "spear": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of spear for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class SpearUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Spear
    form_class = SpearForm
    template_name = "wf/spear/spear_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Spear"
        context["my_exp"] = (
            "The absence or presence of spears as a military technology used in warfare. Includes lances and pikes. A trident is a spear."
        )

        return context


class SpearDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Spear
    success_url = reverse_lazy("spears")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SpearListView(generic.ListView):
    """ """

    model = Spear
    template_name = "wf/spear/spear_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("spears")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Spear"
        context["var_main_desc"] = (
            "The absence or presence of spears as a military technology used in warfare. includes lances and pikes. a trident is a spear."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "spear": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of spear for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class SpearListViewAll(generic.ListView):
    """ """

    model = Spear
    template_name = "wf/spear/spear_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("spears_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Spear.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Spear"
        context["var_main_desc"] = (
            "The absence or presence of spears as a military technology used in warfare. includes lances and pikes. a trident is a spear."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "spear": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of spear for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class SpearDetailView(generic.DetailView):
    """ """

    model = Spear
    template_name = "wf/spear/spear_detail.html"


@permission_required("core.view_capital")
def spear_download(request):
    items = Spear.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_spears_{current_datetime}.csv"
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
            "spear",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.spear,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def spear_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="spears.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of spears as a military technology used in warfare. Includes lances and pikes. A trident is a spear.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Handheld weapons",
    }
    my_meta_data_dic_inner_vars = {
        "spear": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of spear for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class PolearmCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polearm
    form_class = PolearmForm
    template_name = "wf/polearm/polearm_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polearm-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Polearm"
        context["my_exp"] = (
            "The absence or presence of polearms as a military technology used in warfare. This category includes halberds, naginatas, and morning stars"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "polearm": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of polearm for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class PolearmUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polearm
    form_class = PolearmForm
    template_name = "wf/polearm/polearm_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polearm"
        context["my_exp"] = (
            "The absence or presence of polearms as a military technology used in warfare. This category includes halberds, naginatas, and morning stars"
        )

        return context


class PolearmDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polearm
    success_url = reverse_lazy("polearms")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class PolearmListView(generic.ListView):
    """ """

    model = Polearm
    template_name = "wf/polearm/polearm_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polearms")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polearm"
        context["var_main_desc"] = (
            "The absence or presence of polearms as a military technology used in warfare. this category includes halberds, naginatas, and morning stars"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "polearm": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of polearm for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class PolearmListViewAll(generic.ListView):
    """ """

    model = Polearm
    template_name = "wf/polearm/polearm_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polearms_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Polearm.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polearm"
        context["var_main_desc"] = (
            "The absence or presence of polearms as a military technology used in warfare. this category includes halberds, naginatas, and morning stars"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Handheld weapons"
        context["inner_vars"] = {
            "polearm": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of polearm for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class PolearmDetailView(generic.DetailView):
    """ """

    model = Polearm
    template_name = "wf/polearm/polearm_detail.html"


@permission_required("core.view_capital")
def polearm_download(request):
    items = Polearm.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_polearms_{current_datetime}.csv"
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
            "polearm",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.polearm,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def polearm_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="polearms.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of polearms as a military technology used in warfare. This category includes halberds, naginatas, and morning stars",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Handheld weapons",
    }
    my_meta_data_dic_inner_vars = {
        "polearm": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of polearm for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class DogCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dog
    form_class = DogForm
    template_name = "wf/dog/dog_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("dog-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Dog"
        context["my_exp"] = (
            "The absence or presence of dogs as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "dog": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of dog for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class DogUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dog
    form_class = DogForm
    template_name = "wf/dog/dog_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Dog"
        context["my_exp"] = (
            "The absence or presence of dogs as a military technology used in warfare. "
        )

        return context


class DogDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dog
    success_url = reverse_lazy("dogs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class DogListView(generic.ListView):
    """ """

    model = Dog
    template_name = "wf/dog/dog_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("dogs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Dog"
        context["var_main_desc"] = (
            "The absence or presence of dogs as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "dog": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of dog for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class DogListViewAll(generic.ListView):
    """ """

    model = Dog
    template_name = "wf/dog/dog_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("dogs_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Dog.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Dog"
        context["var_main_desc"] = (
            "The absence or presence of dogs as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "dog": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of dog for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class DogDetailView(generic.DetailView):
    """ """

    model = Dog
    template_name = "wf/dog/dog_detail.html"


@permission_required("core.view_capital")
def dog_download(request):
    items = Dog.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_dogs_{current_datetime}.csv"
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
            "dog",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.dog,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def dog_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="dogs.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of dogs as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Animals used in warfare",
    }
    my_meta_data_dic_inner_vars = {
        "dog": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of dog for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class DonkeyCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Donkey
    form_class = DonkeyForm
    template_name = "wf/donkey/donkey_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("donkey-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Donkey"
        context["my_exp"] = (
            "The absence or presence of donkeys as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "donkey": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of donkey for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class DonkeyUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Donkey
    form_class = DonkeyForm
    template_name = "wf/donkey/donkey_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Donkey"
        context["my_exp"] = (
            "The absence or presence of donkeys as a military technology used in warfare. "
        )

        return context


class DonkeyDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Donkey
    success_url = reverse_lazy("donkeys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class DonkeyListView(generic.ListView):
    """ """

    model = Donkey
    template_name = "wf/donkey/donkey_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("donkeys")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Donkey"
        context["var_main_desc"] = (
            "The absence or presence of donkeys as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "donkey": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of donkey for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class DonkeyListViewAll(generic.ListView):
    """ """

    model = Donkey
    template_name = "wf/donkey/donkey_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("donkeys_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Donkey.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Donkey"
        context["var_main_desc"] = (
            "The absence or presence of donkeys as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "donkey": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of donkey for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class DonkeyDetailView(generic.DetailView):
    """ """

    model = Donkey
    template_name = "wf/donkey/donkey_detail.html"


@permission_required("core.view_capital")
def donkey_download(request):
    items = Donkey.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_donkeys_{current_datetime}.csv"
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
            "donkey",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.donkey,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def donkey_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="donkeys.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of donkeys as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Animals used in warfare",
    }
    my_meta_data_dic_inner_vars = {
        "donkey": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of donkey for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class HorseCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Horse
    form_class = HorseForm
    template_name = "wf/horse/horse_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("horse-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Horse"
        context["my_exp"] = (
            "The absence or presence of horses as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "horse": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of horse for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class HorseUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Horse
    form_class = HorseForm
    template_name = "wf/horse/horse_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Horse"
        context["my_exp"] = (
            "The absence or presence of horses as a military technology used in warfare. "
        )

        return context


class HorseDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Horse
    success_url = reverse_lazy("horses")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class HorseListView(generic.ListView):
    """ """

    model = Horse
    template_name = "wf/horse/horse_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("horses")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Horse"
        context["var_main_desc"] = (
            "The absence or presence of horses as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "horse": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of horse for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class HorseListViewAll(generic.ListView):
    """ """

    model = Horse
    template_name = "wf/horse/horse_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("horses_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Horse.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Horse"
        context["var_main_desc"] = (
            "The absence or presence of horses as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "horse": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of horse for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class HorseDetailView(generic.DetailView):
    """ """

    model = Horse
    template_name = "wf/horse/horse_detail.html"


@permission_required("core.view_capital")
def horse_download(request):
    items = Horse.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_horses_{current_datetime}.csv"
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
            "horse",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.horse,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def horse_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="horses.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of horses as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Animals used in warfare",
    }
    my_meta_data_dic_inner_vars = {
        "horse": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of horse for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class CamelCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Camel
    form_class = CamelForm
    template_name = "wf/camel/camel_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("camel-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Camel"
        context["my_exp"] = (
            "The absence or presence of camels as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "camel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of camel for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class CamelUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Camel
    form_class = CamelForm
    template_name = "wf/camel/camel_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Camel"
        context["my_exp"] = (
            "The absence or presence of camels as a military technology used in warfare. "
        )

        return context


class CamelDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Camel
    success_url = reverse_lazy("camels")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CamelListView(generic.ListView):
    """ """

    model = Camel
    template_name = "wf/camel/camel_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("camels")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Camel"
        context["var_main_desc"] = (
            "The absence or presence of camels as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "camel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of camel for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class CamelListViewAll(generic.ListView):
    """ """

    model = Camel
    template_name = "wf/camel/camel_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("camels_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Camel.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Camel"
        context["var_main_desc"] = (
            "The absence or presence of camels as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "camel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of camel for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class CamelDetailView(generic.DetailView):
    """ """

    model = Camel
    template_name = "wf/camel/camel_detail.html"


@permission_required("core.view_capital")
def camel_download(request):
    items = Camel.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_camels_{current_datetime}.csv"
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
            "camel",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.camel,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def camel_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="camels.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of camels as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Animals used in warfare",
    }
    my_meta_data_dic_inner_vars = {
        "camel": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of camel for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class ElephantCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Elephant
    form_class = ElephantForm
    template_name = "wf/elephant/elephant_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("elephant-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Elephant"
        context["my_exp"] = (
            "The absence or presence of elephants as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "elephant": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of elephant for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class ElephantUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Elephant
    form_class = ElephantForm
    template_name = "wf/elephant/elephant_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Elephant"
        context["my_exp"] = (
            "The absence or presence of elephants as a military technology used in warfare. "
        )

        return context


class ElephantDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Elephant
    success_url = reverse_lazy("elephants")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class ElephantListView(generic.ListView):
    """ """

    model = Elephant
    template_name = "wf/elephant/elephant_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("elephants")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Elephant"
        context["var_main_desc"] = (
            "The absence or presence of elephants as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "elephant": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of elephant for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class ElephantListViewAll(generic.ListView):
    """ """

    model = Elephant
    template_name = "wf/elephant/elephant_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("elephants_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Elephant.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Elephant"
        context["var_main_desc"] = (
            "The absence or presence of elephants as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Animals used in warfare"
        context["inner_vars"] = {
            "elephant": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of elephant for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class ElephantDetailView(generic.DetailView):
    """ """

    model = Elephant
    template_name = "wf/elephant/elephant_detail.html"


@permission_required("core.view_capital")
def elephant_download(request):
    items = Elephant.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_elephants_{current_datetime}.csv"
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
            "elephant",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.elephant,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def elephant_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="elephants.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of elephants as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Animals used in warfare",
    }
    my_meta_data_dic_inner_vars = {
        "elephant": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of elephant for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Wood_bark_etcCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wood_bark_etc
    form_class = Wood_bark_etcForm
    template_name = "wf/wood_bark_etc/wood_bark_etc_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wood_bark_etc-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Wood Bark Etc"
        context["my_exp"] = (
            "The absence or presence of wood, bark, etc. as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "wood_bark_etc": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of wood bark etc for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Wood_bark_etcUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wood_bark_etc
    form_class = Wood_bark_etcForm
    template_name = "wf/wood_bark_etc/wood_bark_etc_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Wood Bark Etc"
        context["my_exp"] = (
            "The absence or presence of wood, bark, etc. as a military technology used in warfare. "
        )

        return context


class Wood_bark_etcDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wood_bark_etc
    success_url = reverse_lazy("wood_bark_etcs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Wood_bark_etcListView(generic.ListView):
    """ """

    model = Wood_bark_etc
    template_name = "wf/wood_bark_etc/wood_bark_etc_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wood_bark_etcs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Wood Bark Etc"
        context["var_main_desc"] = (
            "The absence or presence of wood, bark, etc. as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "wood_bark_etc": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of wood bark etc for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Wood_bark_etcListViewAll(generic.ListView):
    """ """

    model = Wood_bark_etc
    template_name = "wf/wood_bark_etc/wood_bark_etc_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wood_bark_etcs_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Wood_bark_etc.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Wood Bark Etc"
        context["var_main_desc"] = (
            "The absence or presence of wood, bark, etc. as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "wood_bark_etc": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of wood bark etc for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Wood_bark_etcDetailView(generic.DetailView):
    """ """

    model = Wood_bark_etc
    template_name = "wf/wood_bark_etc/wood_bark_etc_detail.html"


@permission_required("core.view_capital")
def wood_bark_etc_download(request):
    items = Wood_bark_etc.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_wood_bark_etcs_{current_datetime}.csv"
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
            "wood_bark_etc",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.wood_bark_etc,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def wood_bark_etc_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="wood_bark_etcs.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of wood, bark, etc. as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "wood_bark_etc": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of wood bark etc for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Leather_clothCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Leather_cloth
    form_class = Leather_clothForm
    template_name = "wf/leather_cloth/leather_cloth_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("leather_cloth-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Leather Cloth"
        context["my_exp"] = (
            "The absence or presence of leather, cloth as a military technology used in warfare. For example, leather cuirass, quilted cotton armor"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "leather_cloth": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of leather cloth for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Leather_clothUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Leather_cloth
    form_class = Leather_clothForm
    template_name = "wf/leather_cloth/leather_cloth_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Leather Cloth"
        context["my_exp"] = (
            "The absence or presence of leather, cloth as a military technology used in warfare. For example, leather cuirass, quilted cotton armor"
        )

        return context


class Leather_clothDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Leather_cloth
    success_url = reverse_lazy("leather_cloths")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Leather_clothListView(generic.ListView):
    """ """

    model = Leather_cloth
    template_name = "wf/leather_cloth/leather_cloth_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("leather_cloths")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Leather Cloth"
        context["var_main_desc"] = (
            "The absence or presence of leather, cloth as a military technology used in warfare. for example, leather cuirass, quilted cotton armor"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "leather_cloth": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of leather cloth for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Leather_clothListViewAll(generic.ListView):
    """ """

    model = Leather_cloth
    template_name = "wf/leather_cloth/leather_cloth_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("leather_cloths_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Leather_cloth.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Leather Cloth"
        context["var_main_desc"] = (
            "The absence or presence of leather, cloth as a military technology used in warfare. for example, leather cuirass, quilted cotton armor"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "leather_cloth": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of leather cloth for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Leather_clothDetailView(generic.DetailView):
    """ """

    model = Leather_cloth
    template_name = "wf/leather_cloth/leather_cloth_detail.html"


@permission_required("core.view_capital")
def leather_cloth_download(request):
    items = Leather_cloth.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_leather_cloths_{current_datetime}.csv"
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
            "leather_cloth",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.leather_cloth,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def leather_cloth_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="leather_cloths.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of leather, cloth as a military technology used in warfare. For example, leather cuirass, quilted cotton armor",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "leather_cloth": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of leather cloth for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class ShieldCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Shield
    form_class = ShieldForm
    template_name = "wf/shield/shield_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("shield-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Shield"
        context["my_exp"] = (
            "The absence or presence of shields as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "shield": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of shield for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class ShieldUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Shield
    form_class = ShieldForm
    template_name = "wf/shield/shield_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Shield"
        context["my_exp"] = (
            "The absence or presence of shields as a military technology used in warfare. "
        )

        return context


class ShieldDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Shield
    success_url = reverse_lazy("shields")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class ShieldListView(generic.ListView):
    """ """

    model = Shield
    template_name = "wf/shield/shield_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("shields")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Shield"
        context["var_main_desc"] = (
            "The absence or presence of shields as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "shield": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of shield for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class ShieldListViewAll(generic.ListView):
    """ """

    model = Shield
    template_name = "wf/shield/shield_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("shields_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Shield.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Shield"
        context["var_main_desc"] = (
            "The absence or presence of shields as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "shield": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of shield for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class ShieldDetailView(generic.DetailView):
    """ """

    model = Shield
    template_name = "wf/shield/shield_detail.html"


@permission_required("core.view_capital")
def shield_download(request):
    items = Shield.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_shields_{current_datetime}.csv"
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
            "shield",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.shield,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def shield_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="shields.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of shields as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "shield": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of shield for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class HelmetCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Helmet
    form_class = HelmetForm
    template_name = "wf/helmet/helmet_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("helmet-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Helmet"
        context["my_exp"] = (
            "The absence or presence of helmets as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "helmet": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of helmet for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class HelmetUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Helmet
    form_class = HelmetForm
    template_name = "wf/helmet/helmet_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Helmet"
        context["my_exp"] = (
            "The absence or presence of helmets as a military technology used in warfare. "
        )

        return context


class HelmetDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Helmet
    success_url = reverse_lazy("helmets")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class HelmetListView(generic.ListView):
    """ """

    model = Helmet
    template_name = "wf/helmet/helmet_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("helmets")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Helmet"
        context["var_main_desc"] = (
            "The absence or presence of helmets as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "helmet": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of helmet for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class HelmetListViewAll(generic.ListView):
    """ """

    model = Helmet
    template_name = "wf/helmet/helmet_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("helmets_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Helmet.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Helmet"
        context["var_main_desc"] = (
            "The absence or presence of helmets as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "helmet": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of helmet for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class HelmetDetailView(generic.DetailView):
    """ """

    model = Helmet
    template_name = "wf/helmet/helmet_detail.html"


@permission_required("core.view_capital")
def helmet_download(request):
    items = Helmet.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_helmets_{current_datetime}.csv"
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
            "helmet",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.helmet,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def helmet_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="helmets.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of helmets as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "helmet": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of helmet for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class BreastplateCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Breastplate
    form_class = BreastplateForm
    template_name = "wf/breastplate/breastplate_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("breastplate-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Breastplate"
        context["my_exp"] = (
            "The absence or presence of breastplates as a military technology used in warfare. Armor made from wood, horn, or bone can be very important (as in the spread of the Asian War Complex into North America). Leather and cotton (in the Americas) armor was also effective against arrows and warclubs. Breastplate refers to any form of torso protection (in fact, we might rename this variable 'torso protection' at a later date). In the vast majority of cases you will probably find that if a culture has wooden armor, leather armor, chainmail armor, or scaled armor that breastplate should be coded as present because this is the most common location for armor. However, in theory, it is possible to have armor that doesn't protect the torso (for example, a culture might use armor that protects the limbs only)."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "breastplate": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of breastplate for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class BreastplateUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Breastplate
    form_class = BreastplateForm
    template_name = "wf/breastplate/breastplate_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Breastplate"
        context["my_exp"] = (
            "The absence or presence of breastplates as a military technology used in warfare. Armor made from wood, horn, or bone can be very important (as in the spread of the Asian War Complex into North America). Leather and cotton (in the Americas) armor was also effective against arrows and warclubs. Breastplate refers to any form of torso protection (in fact, we might rename this variable 'torso protection' at a later date). In the vast majority of cases you will probably find that if a culture has wooden armor, leather armor, chainmail armor, or scaled armor that breastplate should be coded as present because this is the most common location for armor. However, in theory, it is possible to have armor that doesn't protect the torso (for example, a culture might use armor that protects the limbs only)."
        )

        return context


class BreastplateDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Breastplate
    success_url = reverse_lazy("breastplates")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class BreastplateListView(generic.ListView):
    """ """

    model = Breastplate
    template_name = "wf/breastplate/breastplate_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("breastplates")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Breastplate"
        context["var_main_desc"] = (
            "The absence or presence of breastplates as a military technology used in warfare. armor made from wood, horn, or bone can be very important (as in the spread of the asian war complex into north america). leather and cotton (in the americas) armor was also effective against arrows and warclubs. breastplate refers to any form of torso protection (in fact, we might rename this variable 'torso protection' at a later date). in the vast majority of cases you will probably find that if a culture has wooden armor, leather armor, chainmail armor, or scaled armor that breastplate should be coded as present because this is the most common location for armor. however, in theory, it is possible to have armor that doesn't protect the torso (for example, a culture might use armor that protects the limbs only)."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "breastplate": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of breastplate for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class BreastplateListViewAll(generic.ListView):
    """ """

    model = Breastplate
    template_name = "wf/breastplate/breastplate_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("breastplates_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Breastplate.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Breastplate"
        context["var_main_desc"] = (
            "The absence or presence of breastplates as a military technology used in warfare. armor made from wood, horn, or bone can be very important (as in the spread of the asian war complex into north america). leather and cotton (in the americas) armor was also effective against arrows and warclubs. breastplate refers to any form of torso protection (in fact, we might rename this variable 'torso protection' at a later date). in the vast majority of cases you will probably find that if a culture has wooden armor, leather armor, chainmail armor, or scaled armor that breastplate should be coded as present because this is the most common location for armor. however, in theory, it is possible to have armor that doesn't protect the torso (for example, a culture might use armor that protects the limbs only)."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "breastplate": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of breastplate for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class BreastplateDetailView(generic.DetailView):
    """ """

    model = Breastplate
    template_name = "wf/breastplate/breastplate_detail.html"


@permission_required("core.view_capital")
def breastplate_download(request):
    items = Breastplate.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_breastplates_{current_datetime}.csv"
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
            "breastplate",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.breastplate,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def breastplate_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="breastplates.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of breastplates as a military technology used in warfare. Armor made from wood, horn, or bone can be very important (as in the spread of the Asian War Complex into North America). Leather and cotton (in the Americas) armor was also effective against arrows and warclubs. Breastplate refers to any form of torso protection (in fact, we might rename this variable 'torso protection' at a later date). In the vast majority of cases you will probably find that if a culture has wooden armor, leather armor, chainmail armor, or scaled armor that breastplate should be coded as present because this is the most common location for armor. However, in theory, it is possible to have armor that doesn't protect the torso (for example, a culture might use armor that protects the limbs only).",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "breastplate": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of breastplate for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Limb_protectionCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Limb_protection
    form_class = Limb_protectionForm
    template_name = "wf/limb_protection/limb_protection_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("limb_protection-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Limb Protection"
        context["my_exp"] = (
            "The absence or presence of limb protection as a military technology used in warfare. E.g., greaves. Covering arms, or legs, or both."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "limb_protection": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of limb protection for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Limb_protectionUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Limb_protection
    form_class = Limb_protectionForm
    template_name = "wf/limb_protection/limb_protection_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Limb Protection"
        context["my_exp"] = (
            "The absence or presence of limb protection as a military technology used in warfare. E.g., greaves. Covering arms, or legs, or both."
        )

        return context


class Limb_protectionDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Limb_protection
    success_url = reverse_lazy("limb_protections")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Limb_protectionListView(generic.ListView):
    """ """

    model = Limb_protection
    template_name = "wf/limb_protection/limb_protection_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("limb_protections")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Limb Protection"
        context["var_main_desc"] = (
            "The absence or presence of limb protection as a military technology used in warfare. e.g., greaves. covering arms, or legs, or both."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "limb_protection": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of limb protection for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Limb_protectionListViewAll(generic.ListView):
    """ """

    model = Limb_protection
    template_name = "wf/limb_protection/limb_protection_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("limb_protections_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Limb_protection.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Limb Protection"
        context["var_main_desc"] = (
            "The absence or presence of limb protection as a military technology used in warfare. e.g., greaves. covering arms, or legs, or both."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "limb_protection": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of limb protection for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Limb_protectionDetailView(generic.DetailView):
    """ """

    model = Limb_protection
    template_name = "wf/limb_protection/limb_protection_detail.html"


@permission_required("core.view_capital")
def limb_protection_download(request):
    items = Limb_protection.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_limb_protections_{current_datetime}.csv"
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
            "limb_protection",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.limb_protection,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def limb_protection_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="limb_protections.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of limb protection as a military technology used in warfare. E.g., greaves. Covering arms, or legs, or both.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "limb_protection": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of limb protection for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Scaled_armorCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Scaled_armor
    form_class = Scaled_armorForm
    template_name = "wf/scaled_armor/scaled_armor_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scaled_armor-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Scaled Armor"
        context["my_exp"] = (
            "The absence or presence of scaled armor as a military technology used in warfare. Armor consisting of many individual small armor scales (plates) attached to a backing of cloth or leather. The scaled don't need to be metal (i.e. they could be particularly rigid bits of leather, horn, bone, etc)."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "scaled_armor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of scaled armor for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Scaled_armorUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Scaled_armor
    form_class = Scaled_armorForm
    template_name = "wf/scaled_armor/scaled_armor_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Scaled Armor"
        context["my_exp"] = (
            "The absence or presence of scaled armor as a military technology used in warfare. Armor consisting of many individual small armor scales (plates) attached to a backing of cloth or leather. The scaled don't need to be metal (i.e. they could be particularly rigid bits of leather, horn, bone, etc)."
        )

        return context


class Scaled_armorDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Scaled_armor
    success_url = reverse_lazy("scaled_armors")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Scaled_armorListView(generic.ListView):
    """ """

    model = Scaled_armor
    template_name = "wf/scaled_armor/scaled_armor_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scaled_armors")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Scaled Armor"
        context["var_main_desc"] = (
            "The absence or presence of scaled armor as a military technology used in warfare. armor consisting of many individual small armor scales (plates) attached to a backing of cloth or leather. the scaled don't need to be metal (i.e. they could be particularly rigid bits of leather, horn, bone, etc)."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "scaled_armor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of scaled armor for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Scaled_armorListViewAll(generic.ListView):
    """ """

    model = Scaled_armor
    template_name = "wf/scaled_armor/scaled_armor_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scaled_armors_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Scaled_armor.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Scaled Armor"
        context["var_main_desc"] = (
            "The absence or presence of scaled armor as a military technology used in warfare. armor consisting of many individual small armor scales (plates) attached to a backing of cloth or leather. the scaled don't need to be metal (i.e. they could be particularly rigid bits of leather, horn, bone, etc)."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "scaled_armor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of scaled armor for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Scaled_armorDetailView(generic.DetailView):
    """ """

    model = Scaled_armor
    template_name = "wf/scaled_armor/scaled_armor_detail.html"


@permission_required("core.view_capital")
def scaled_armor_download(request):
    items = Scaled_armor.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_scaled_armors_{current_datetime}.csv"
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
            "scaled_armor",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.scaled_armor,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def scaled_armor_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="scaled_armors.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of scaled armor as a military technology used in warfare. Armor consisting of many individual small armor scales (plates) attached to a backing of cloth or leather. The scaled don't need to be metal (i.e. they could be particularly rigid bits of leather, horn, bone, etc).",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "scaled_armor": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of scaled armor for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Laminar_armorCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Laminar_armor
    form_class = Laminar_armorForm
    template_name = "wf/laminar_armor/laminar_armor_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("laminar_armor-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Laminar Armor"
        context["my_exp"] = (
            "The absence or presence of laminar armor as a military technology used in warfare. (also known as banded mail, example: lorica segmentata). Armor that is made from horizontal overlapping rows or bands of sold armor plates."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "laminar_armor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of laminar armor for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Laminar_armorUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Laminar_armor
    form_class = Laminar_armorForm
    template_name = "wf/laminar_armor/laminar_armor_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Laminar Armor"
        context["my_exp"] = (
            "The absence or presence of laminar armor as a military technology used in warfare. (also known as banded mail, example: lorica segmentata). Armor that is made from horizontal overlapping rows or bands of sold armor plates."
        )

        return context


class Laminar_armorDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Laminar_armor
    success_url = reverse_lazy("laminar_armors")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Laminar_armorListView(generic.ListView):
    """ """

    model = Laminar_armor
    template_name = "wf/laminar_armor/laminar_armor_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("laminar_armors")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Laminar Armor"
        context["var_main_desc"] = (
            "The absence or presence of laminar armor as a military technology used in warfare. (also known as banded mail, example: lorica segmentata). armor that is made from horizontal overlapping rows or bands of sold armor plates."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "laminar_armor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of laminar armor for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Laminar_armorListViewAll(generic.ListView):
    """ """

    model = Laminar_armor
    template_name = "wf/laminar_armor/laminar_armor_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("laminar_armors_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Laminar_armor.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Laminar Armor"
        context["var_main_desc"] = (
            "The absence or presence of laminar armor as a military technology used in warfare. (also known as banded mail, example: lorica segmentata). armor that is made from horizontal overlapping rows or bands of sold armor plates."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "laminar_armor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of laminar armor for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Laminar_armorDetailView(generic.DetailView):
    """ """

    model = Laminar_armor
    template_name = "wf/laminar_armor/laminar_armor_detail.html"


@permission_required("core.view_capital")
def laminar_armor_download(request):
    items = Laminar_armor.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_laminar_armors_{current_datetime}.csv"
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
            "laminar_armor",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.laminar_armor,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def laminar_armor_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="laminar_armors.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of laminar armor as a military technology used in warfare. (also known as banded mail, example: lorica segmentata). Armor that is made from horizontal overlapping rows or bands of sold armor plates.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "laminar_armor": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of laminar armor for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Plate_armorCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Plate_armor
    form_class = Plate_armorForm
    template_name = "wf/plate_armor/plate_armor_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("plate_armor-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Plate Armor"
        context["my_exp"] = (
            "The absence or presence of plate armor as a military technology used in warfare. Armor made of iron or steel plates."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "plate_armor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of plate armor for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Plate_armorUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Plate_armor
    form_class = Plate_armorForm
    template_name = "wf/plate_armor/plate_armor_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Plate Armor"
        context["my_exp"] = (
            "The absence or presence of plate armor as a military technology used in warfare. Armor made of iron or steel plates."
        )

        return context


class Plate_armorDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Plate_armor
    success_url = reverse_lazy("plate_armors")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Plate_armorListView(generic.ListView):
    """ """

    model = Plate_armor
    template_name = "wf/plate_armor/plate_armor_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("plate_armors")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Plate Armor"
        context["var_main_desc"] = (
            "The absence or presence of plate armor as a military technology used in warfare. armor made of iron or steel plates."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "plate_armor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of plate armor for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Plate_armorListViewAll(generic.ListView):
    """ """

    model = Plate_armor
    template_name = "wf/plate_armor/plate_armor_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("plate_armors_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Plate_armor.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Plate Armor"
        context["var_main_desc"] = (
            "The absence or presence of plate armor as a military technology used in warfare. armor made of iron or steel plates."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "plate_armor": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of plate armor for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Plate_armorDetailView(generic.DetailView):
    """ """

    model = Plate_armor
    template_name = "wf/plate_armor/plate_armor_detail.html"


@permission_required("core.view_capital")
def plate_armor_download(request):
    items = Plate_armor.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_plate_armors_{current_datetime}.csv"
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
            "plate_armor",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.plate_armor,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def plate_armor_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="plate_armors.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of plate armor as a military technology used in warfare. Armor made of iron or steel plates.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "plate_armor": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of plate armor for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Small_vessels_canoes_etcCreate(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Small_vessels_canoes_etc
    form_class = Small_vessels_canoes_etcForm
    template_name = "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("small_vessels_canoes_etc-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Small Vessels Canoes Etc"
        context["my_exp"] = (
            "The absence or presence of small vessels, canoes, etc. as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "small_vessels_canoes_etc": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of small vessels canoes etc for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Small_vessels_canoes_etcUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Small_vessels_canoes_etc
    form_class = Small_vessels_canoes_etcForm
    template_name = "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Small Vessels Canoes Etc"
        context["my_exp"] = (
            "The absence or presence of small vessels, canoes, etc. as a military technology used in warfare. "
        )

        return context


class Small_vessels_canoes_etcDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Small_vessels_canoes_etc
    success_url = reverse_lazy("small_vessels_canoes_etcs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Small_vessels_canoes_etcListView(generic.ListView):
    """ """

    model = Small_vessels_canoes_etc
    template_name = "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("small_vessels_canoes_etcs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Small Vessels Canoes Etc"
        context["var_main_desc"] = (
            "The absence or presence of small vessels, canoes, etc. as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Naval technology"
        context["inner_vars"] = {
            "small_vessels_canoes_etc": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of small vessels canoes etc for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Small_vessels_canoes_etcListViewAll(generic.ListView):
    """ """

    model = Small_vessels_canoes_etc
    template_name = "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("small_vessels_canoes_etcs_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Small_vessels_canoes_etc.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Small Vessels Canoes Etc"
        context["var_main_desc"] = (
            "The absence or presence of small vessels, canoes, etc. as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Naval technology"
        context["inner_vars"] = {
            "small_vessels_canoes_etc": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of small vessels canoes etc for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Small_vessels_canoes_etcDetailView(generic.DetailView):
    """ """

    model = Small_vessels_canoes_etc
    template_name = "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_detail.html"


@permission_required("core.view_capital")
def small_vessels_canoes_etc_download(request):
    items = Small_vessels_canoes_etc.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_small_vessels_canoes_etcs_{current_datetime}.csv"
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
            "small_vessels_canoes_etc",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.small_vessels_canoes_etc,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def small_vessels_canoes_etc_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="small_vessels_canoes_etcs.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of small vessels, canoes, etc. as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Naval technology",
    }
    my_meta_data_dic_inner_vars = {
        "small_vessels_canoes_etc": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of small vessels canoes etc for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Merchant_ships_pressed_into_serviceCreate(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Merchant_ships_pressed_into_service
    form_class = Merchant_ships_pressed_into_serviceForm
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("merchant_ships_pressed_into_service-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Merchant Ships Pressed Into Service"
        context["my_exp"] = (
            "The absence or presence of merchant ships pressed into service as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "merchant_ships_pressed_into_service": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of merchant ships pressed into service for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Merchant_ships_pressed_into_serviceUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Merchant_ships_pressed_into_service
    form_class = Merchant_ships_pressed_into_serviceForm
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Merchant Ships Pressed Into Service"
        context["my_exp"] = (
            "The absence or presence of merchant ships pressed into service as a military technology used in warfare. "
        )

        return context


class Merchant_ships_pressed_into_serviceDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Merchant_ships_pressed_into_service
    success_url = reverse_lazy("merchant_ships_pressed_into_services")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Merchant_ships_pressed_into_serviceListView(generic.ListView):
    """ """

    model = Merchant_ships_pressed_into_service
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("merchant_ships_pressed_into_services")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Merchant Ships Pressed Into Service"
        context["var_main_desc"] = (
            "The absence or presence of merchant ships pressed into service as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Naval technology"
        context["inner_vars"] = {
            "merchant_ships_pressed_into_service": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of merchant ships pressed into service for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Merchant_ships_pressed_into_serviceListViewAll(generic.ListView):
    """ """

    model = Merchant_ships_pressed_into_service
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("merchant_ships_pressed_into_services_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Merchant_ships_pressed_into_service.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Merchant Ships Pressed Into Service"
        context["var_main_desc"] = (
            "The absence or presence of merchant ships pressed into service as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Naval technology"
        context["inner_vars"] = {
            "merchant_ships_pressed_into_service": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of merchant ships pressed into service for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Merchant_ships_pressed_into_serviceDetailView(generic.DetailView):
    """ """

    model = Merchant_ships_pressed_into_service
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_detail.html"


@permission_required("core.view_capital")
def merchant_ships_pressed_into_service_download(request):
    items = Merchant_ships_pressed_into_service.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_merchant_ships_pressed_into_services_{current_datetime}.csv"
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
            "merchant_ships_pressed_into_service",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.merchant_ships_pressed_into_service,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def merchant_ships_pressed_into_service_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="merchant_ships_pressed_into_services.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of merchant ships pressed into service as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Naval technology",
    }
    my_meta_data_dic_inner_vars = {
        "merchant_ships_pressed_into_service": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of merchant ships pressed into service for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Specialized_military_vesselCreate(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Specialized_military_vessel
    form_class = Specialized_military_vesselForm
    template_name = (
        "wf/specialized_military_vessel/specialized_military_vessel_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("specialized_military_vessel-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Specialized Military Vessel"
        context["my_exp"] = (
            "The absence or presence of specialized military vessels as a military technology used in warfare. (such as galleys and sailing ships)"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "specialized_military_vessel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of specialized military vessel for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Specialized_military_vesselUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Specialized_military_vessel
    form_class = Specialized_military_vesselForm
    template_name = (
        "wf/specialized_military_vessel/specialized_military_vessel_update.html"
    )
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Specialized Military Vessel"
        context["my_exp"] = (
            "The absence or presence of specialized military vessels as a military technology used in warfare. (such as galleys and sailing ships)"
        )

        return context


class Specialized_military_vesselDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Specialized_military_vessel
    success_url = reverse_lazy("specialized_military_vessels")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Specialized_military_vesselListView(generic.ListView):
    """ """

    model = Specialized_military_vessel
    template_name = (
        "wf/specialized_military_vessel/specialized_military_vessel_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("specialized_military_vessels")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Specialized Military Vessel"
        context["var_main_desc"] = (
            "The absence or presence of specialized military vessels as a military technology used in warfare. (such as galleys and sailing ships)"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Naval technology"
        context["inner_vars"] = {
            "specialized_military_vessel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of specialized military vessel for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Specialized_military_vesselListViewAll(generic.ListView):
    """ """

    model = Specialized_military_vessel
    template_name = (
        "wf/specialized_military_vessel/specialized_military_vessel_list_all.html"
    )

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("specialized_military_vessels_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Specialized_military_vessel.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Specialized Military Vessel"
        context["var_main_desc"] = (
            "The absence or presence of specialized military vessels as a military technology used in warfare. (such as galleys and sailing ships)"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Naval technology"
        context["inner_vars"] = {
            "specialized_military_vessel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of specialized military vessel for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Specialized_military_vesselDetailView(generic.DetailView):
    """ """

    model = Specialized_military_vessel
    template_name = (
        "wf/specialized_military_vessel/specialized_military_vessel_detail.html"
    )


@permission_required("core.view_capital")
def specialized_military_vessel_download(request):
    items = Specialized_military_vessel.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_specialized_military_vessels_{current_datetime}.csv"
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
            "specialized_military_vessel",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.specialized_military_vessel,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def specialized_military_vessel_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="specialized_military_vessels.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of specialized military vessels as a military technology used in warfare. (such as galleys and sailing ships)",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Naval technology",
    }
    my_meta_data_dic_inner_vars = {
        "specialized_military_vessel": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of specialized military vessel for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Settlements_in_a_defensive_positionCreate(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Settlements_in_a_defensive_position
    form_class = Settlements_in_a_defensive_positionForm
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("settlements_in_a_defensive_position-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Settlements in a Defensive Position"
        context["my_exp"] = (
            "The absence or presence of settlements in a defensive position as a military technology used in warfare. Settlements in a location that was clearly chosen for defensive reasons. E.g. on a hill top, peninsula."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "settlements_in_a_defensive_position": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of settlements in a defensive position for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Settlements_in_a_defensive_positionUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Settlements_in_a_defensive_position
    form_class = Settlements_in_a_defensive_positionForm
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Settlements in a Defensive Position"
        context["my_exp"] = (
            "The absence or presence of settlements in a defensive position as a military technology used in warfare. Settlements in a location that was clearly chosen for defensive reasons. E.g. on a hill top, peninsula."
        )

        return context


class Settlements_in_a_defensive_positionDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Settlements_in_a_defensive_position
    success_url = reverse_lazy("settlements_in_a_defensive_positions")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Settlements_in_a_defensive_positionListView(generic.ListView):
    """ """

    model = Settlements_in_a_defensive_position
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("settlements_in_a_defensive_positions")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Settlements in a Defensive Position"
        context["var_main_desc"] = (
            "The absence or presence of settlements in a defensive position as a military technology used in warfare. settlements in a location that was clearly chosen for defensive reasons. e.g. on a hill top, peninsula."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "settlements_in_a_defensive_position": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of settlements in a defensive position for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Settlements_in_a_defensive_positionListViewAll(generic.ListView):
    """ """

    model = Settlements_in_a_defensive_position
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("settlements_in_a_defensive_positions_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Settlements_in_a_defensive_position.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Settlements in a Defensive Position"
        context["var_main_desc"] = (
            "The absence or presence of settlements in a defensive position as a military technology used in warfare. settlements in a location that was clearly chosen for defensive reasons. e.g. on a hill top, peninsula."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "settlements_in_a_defensive_position": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of settlements in a defensive position for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Settlements_in_a_defensive_positionDetailView(generic.DetailView):
    """ """

    model = Settlements_in_a_defensive_position
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_detail.html"


@permission_required("core.view_capital")
def settlements_in_a_defensive_position_download(request):
    items = Settlements_in_a_defensive_position.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_settlements_in_a_defensive_positions_{current_datetime}.csv"
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
            "settlements_in_a_defensive_position",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.settlements_in_a_defensive_position,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def settlements_in_a_defensive_position_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="settlements_in_a_defensive_positions.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of settlements in a defensive position as a military technology used in warfare. Settlements in a location that was clearly chosen for defensive reasons. E.g. on a hill top, peninsula.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "settlements_in_a_defensive_position": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of settlements in a defensive position for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Wooden_palisadeCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wooden_palisade
    form_class = Wooden_palisadeForm
    template_name = "wf/wooden_palisade/wooden_palisade_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wooden_palisade-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Wooden Palisade"
        context["my_exp"] = (
            "The absence or presence of wooden palisades as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "wooden_palisade": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of wooden palisade for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Wooden_palisadeUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wooden_palisade
    form_class = Wooden_palisadeForm
    template_name = "wf/wooden_palisade/wooden_palisade_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Wooden Palisade"
        context["my_exp"] = (
            "The absence or presence of wooden palisades as a military technology used in warfare. "
        )

        return context


class Wooden_palisadeDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wooden_palisade
    success_url = reverse_lazy("wooden_palisades")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Wooden_palisadeListView(generic.ListView):
    """ """

    model = Wooden_palisade
    template_name = "wf/wooden_palisade/wooden_palisade_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wooden_palisades")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Wooden Palisade"
        context["var_main_desc"] = (
            "The absence or presence of wooden palisades as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "wooden_palisade": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of wooden palisade for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Wooden_palisadeListViewAll(generic.ListView):
    """ """

    model = Wooden_palisade
    template_name = "wf/wooden_palisade/wooden_palisade_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wooden_palisades_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Wooden_palisade.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Wooden Palisade"
        context["var_main_desc"] = (
            "The absence or presence of wooden palisades as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "wooden_palisade": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of wooden palisade for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Wooden_palisadeDetailView(generic.DetailView):
    """ """

    model = Wooden_palisade
    template_name = "wf/wooden_palisade/wooden_palisade_detail.html"


@permission_required("core.view_capital")
def wooden_palisade_download(request):
    items = Wooden_palisade.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_wooden_palisades_{current_datetime}.csv"
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
            "wooden_palisade",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.wooden_palisade,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def wooden_palisade_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="wooden_palisades.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of wooden palisades as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "wooden_palisade": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of wooden palisade for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Earth_rampartCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Earth_rampart
    form_class = Earth_rampartForm
    template_name = "wf/earth_rampart/earth_rampart_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("earth_rampart-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Earth Rampart"
        context["my_exp"] = (
            "The absence or presence of earth ramparts as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "earth_rampart": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of earth rampart for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Earth_rampartUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Earth_rampart
    form_class = Earth_rampartForm
    template_name = "wf/earth_rampart/earth_rampart_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Earth Rampart"
        context["my_exp"] = (
            "The absence or presence of earth ramparts as a military technology used in warfare. "
        )

        return context


class Earth_rampartDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Earth_rampart
    success_url = reverse_lazy("earth_ramparts")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Earth_rampartListView(generic.ListView):
    """ """

    model = Earth_rampart
    template_name = "wf/earth_rampart/earth_rampart_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("earth_ramparts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Earth Rampart"
        context["var_main_desc"] = (
            "The absence or presence of earth ramparts as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "earth_rampart": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of earth rampart for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Earth_rampartListViewAll(generic.ListView):
    """ """

    model = Earth_rampart
    template_name = "wf/earth_rampart/earth_rampart_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("earth_ramparts_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Earth_rampart.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Earth Rampart"
        context["var_main_desc"] = (
            "The absence or presence of earth ramparts as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "earth_rampart": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of earth rampart for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Earth_rampartDetailView(generic.DetailView):
    """ """

    model = Earth_rampart
    template_name = "wf/earth_rampart/earth_rampart_detail.html"


@permission_required("core.view_capital")
def earth_rampart_download(request):
    items = Earth_rampart.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_earth_ramparts_{current_datetime}.csv"
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
            "earth_rampart",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.earth_rampart,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def earth_rampart_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="earth_ramparts.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of earth ramparts as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "earth_rampart": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of earth rampart for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class DitchCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Ditch
    form_class = DitchForm
    template_name = "wf/ditch/ditch_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("ditch-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Ditch"
        context["my_exp"] = (
            "The absence or presence of ditch as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "ditch": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of ditch for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class DitchUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Ditch
    form_class = DitchForm
    template_name = "wf/ditch/ditch_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Ditch"
        context["my_exp"] = (
            "The absence or presence of ditch as a military technology used in warfare. "
        )

        return context


class DitchDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Ditch
    success_url = reverse_lazy("ditchs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class DitchListView(generic.ListView):
    """ """

    model = Ditch
    template_name = "wf/ditch/ditch_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("ditchs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Ditch"
        context["var_main_desc"] = (
            "The absence or presence of ditch as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "ditch": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of ditch for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class DitchListViewAll(generic.ListView):
    """ """

    model = Ditch
    template_name = "wf/ditch/ditch_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("ditchs_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Ditch.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Ditch"
        context["var_main_desc"] = (
            "The absence or presence of ditch as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "ditch": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of ditch for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class DitchDetailView(generic.DetailView):
    """ """

    model = Ditch
    template_name = "wf/ditch/ditch_detail.html"


@permission_required("core.view_capital")
def ditch_download(request):
    items = Ditch.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_ditchs_{current_datetime}.csv"
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
            "ditch",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.ditch,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def ditch_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="ditchs.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of ditch as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "ditch": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of ditch for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class MoatCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Moat
    form_class = MoatForm
    template_name = "wf/moat/moat_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("moat-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Moat"
        context["my_exp"] = (
            "The absence or presence of moat as a military technology used in warfare. Differs from a ditch in that it has water"
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "moat": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of moat for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class MoatUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Moat
    form_class = MoatForm
    template_name = "wf/moat/moat_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Moat"
        context["my_exp"] = (
            "The absence or presence of moat as a military technology used in warfare. Differs from a ditch in that it has water"
        )

        return context


class MoatDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Moat
    success_url = reverse_lazy("moats")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class MoatListView(generic.ListView):
    """ """

    model = Moat
    template_name = "wf/moat/moat_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("moats")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Moat"
        context["var_main_desc"] = (
            "The absence or presence of moat as a military technology used in warfare. differs from a ditch in that it has water"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "moat": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of moat for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class MoatListViewAll(generic.ListView):
    """ """

    model = Moat
    template_name = "wf/moat/moat_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("moats_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Moat.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Moat"
        context["var_main_desc"] = (
            "The absence or presence of moat as a military technology used in warfare. differs from a ditch in that it has water"
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "moat": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of moat for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class MoatDetailView(generic.DetailView):
    """ """

    model = Moat
    template_name = "wf/moat/moat_detail.html"


@permission_required("core.view_capital")
def moat_download(request):
    items = Moat.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_moats_{current_datetime}.csv"
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
            "moat",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.moat,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def moat_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="moats.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of moat as a military technology used in warfare. Differs from a ditch in that it has water",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "moat": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of moat for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Stone_walls_non_mortaredCreate(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_non_mortared
    form_class = Stone_walls_non_mortaredForm
    template_name = "wf/stone_walls_non_mortared/stone_walls_non_mortared_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_non_mortared-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Stone Walls Non Mortared"
        context["my_exp"] = (
            "The absence or presence of stone walls (non-mortared) as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "stone_walls_non_mortared": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of stone walls non mortared for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Stone_walls_non_mortaredUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_non_mortared
    form_class = Stone_walls_non_mortaredForm
    template_name = "wf/stone_walls_non_mortared/stone_walls_non_mortared_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Stone Walls Non Mortared"
        context["my_exp"] = (
            "The absence or presence of stone walls (non-mortared) as a military technology used in warfare. "
        )

        return context


class Stone_walls_non_mortaredDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_non_mortared
    success_url = reverse_lazy("stone_walls_non_mortareds")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Stone_walls_non_mortaredListView(generic.ListView):
    """ """

    model = Stone_walls_non_mortared
    template_name = "wf/stone_walls_non_mortared/stone_walls_non_mortared_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_non_mortareds")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Stone Walls Non Mortared"
        context["var_main_desc"] = (
            "The absence or presence of stone walls (non-mortared) as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "stone_walls_non_mortared": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of stone walls non mortared for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Stone_walls_non_mortaredListViewAll(generic.ListView):
    """ """

    model = Stone_walls_non_mortared
    template_name = "wf/stone_walls_non_mortared/stone_walls_non_mortared_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_non_mortareds_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Stone_walls_non_mortared.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Stone Walls Non Mortared"
        context["var_main_desc"] = (
            "The absence or presence of stone walls (non-mortared) as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "stone_walls_non_mortared": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of stone walls non mortared for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Stone_walls_non_mortaredDetailView(generic.DetailView):
    """ """

    model = Stone_walls_non_mortared
    template_name = "wf/stone_walls_non_mortared/stone_walls_non_mortared_detail.html"


@permission_required("core.view_capital")
def stone_walls_non_mortared_download(request):
    items = Stone_walls_non_mortared.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_stone_walls_non_mortareds_{current_datetime}.csv"
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
            "stone_walls_non_mortared",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.stone_walls_non_mortared,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def stone_walls_non_mortared_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="stone_walls_non_mortareds.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of stone walls (non-mortared) as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "stone_walls_non_mortared": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of stone walls non mortared for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Stone_walls_mortaredCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_mortared
    form_class = Stone_walls_mortaredForm
    template_name = "wf/stone_walls_mortared/stone_walls_mortared_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_mortared-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Stone Walls Mortared"
        context["my_exp"] = (
            "The absence or presence of stone walls (mortared) as a military technology used in warfare. "
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "stone_walls_mortared": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of stone walls mortared for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Stone_walls_mortaredUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_mortared
    form_class = Stone_walls_mortaredForm
    template_name = "wf/stone_walls_mortared/stone_walls_mortared_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Stone Walls Mortared"
        context["my_exp"] = (
            "The absence or presence of stone walls (mortared) as a military technology used in warfare. "
        )

        return context


class Stone_walls_mortaredDelete(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_mortared
    success_url = reverse_lazy("stone_walls_mortareds")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Stone_walls_mortaredListView(generic.ListView):
    """ """

    model = Stone_walls_mortared
    template_name = "wf/stone_walls_mortared/stone_walls_mortared_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_mortareds")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Stone Walls Mortared"
        context["var_main_desc"] = (
            "The absence or presence of stone walls (mortared) as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "stone_walls_mortared": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of stone walls mortared for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Stone_walls_mortaredListViewAll(generic.ListView):
    """ """

    model = Stone_walls_mortared
    template_name = "wf/stone_walls_mortared/stone_walls_mortared_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_mortareds_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Stone_walls_mortared.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Stone Walls Mortared"
        context["var_main_desc"] = (
            "The absence or presence of stone walls (mortared) as a military technology used in warfare. "
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "stone_walls_mortared": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of stone walls mortared for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Stone_walls_mortaredDetailView(generic.DetailView):
    """ """

    model = Stone_walls_mortared
    template_name = "wf/stone_walls_mortared/stone_walls_mortared_detail.html"


@permission_required("core.view_capital")
def stone_walls_mortared_download(request):
    items = Stone_walls_mortared.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_stone_walls_mortareds_{current_datetime}.csv"
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
            "stone_walls_mortared",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.stone_walls_mortared,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def stone_walls_mortared_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="stone_walls_mortareds.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of stone walls (mortared) as a military technology used in warfare. ",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "stone_walls_mortared": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of stone walls mortared for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Fortified_campCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Fortified_camp
    form_class = Fortified_campForm
    template_name = "wf/fortified_camp/fortified_camp_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("fortified_camp-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Fortified Camp"
        context["my_exp"] = (
            "The absence or presence of fortified camps as a military technology used in warfare. Camps made by armies on the move (e.g. on a campaign) that which could be constructed on a hill top or in the middle of a plain or desert, usually out of local materials."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "fortified_camp": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of fortified camp for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Fortified_campUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Fortified_camp
    form_class = Fortified_campForm
    template_name = "wf/fortified_camp/fortified_camp_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Fortified Camp"
        context["my_exp"] = (
            "The absence or presence of fortified camps as a military technology used in warfare. Camps made by armies on the move (e.g. on a campaign) that which could be constructed on a hill top or in the middle of a plain or desert, usually out of local materials."
        )

        return context


class Fortified_campDelete(PermissionRequiredMixin, DeleteView):
    """ """

    model = Fortified_camp
    success_url = reverse_lazy("fortified_camps")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Fortified_campListView(generic.ListView):
    """ """

    model = Fortified_camp
    template_name = "wf/fortified_camp/fortified_camp_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("fortified_camps")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Fortified Camp"
        context["var_main_desc"] = (
            "The absence or presence of fortified camps as a military technology used in warfare. camps made by armies on the move (e.g. on a campaign) that which could be constructed on a hill top or in the middle of a plain or desert, usually out of local materials."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "fortified_camp": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of fortified camp for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Fortified_campListViewAll(generic.ListView):
    """ """

    model = Fortified_camp
    template_name = "wf/fortified_camp/fortified_camp_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("fortified_camps_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Fortified_camp.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Fortified Camp"
        context["var_main_desc"] = (
            "The absence or presence of fortified camps as a military technology used in warfare. camps made by armies on the move (e.g. on a campaign) that which could be constructed on a hill top or in the middle of a plain or desert, usually out of local materials."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "fortified_camp": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of fortified camp for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Fortified_campDetailView(generic.DetailView):
    """ """

    model = Fortified_camp
    template_name = "wf/fortified_camp/fortified_camp_detail.html"


@permission_required("core.view_capital")
def fortified_camp_download(request):
    items = Fortified_camp.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_fortified_camps_{current_datetime}.csv"
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
            "fortified_camp",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.fortified_camp,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def fortified_camp_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="fortified_camps.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of fortified camps as a military technology used in warfare. Camps made by armies on the move (e.g. on a campaign) that which could be constructed on a hill top or in the middle of a plain or desert, usually out of local materials.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "fortified_camp": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of fortified camp for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Complex_fortificationCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """ """

    model = Complex_fortification
    form_class = Complex_fortificationForm
    template_name = "wf/complex_fortification/complex_fortification_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("complex_fortification-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Complex Fortification"
        context["my_exp"] = (
            "The absence or presence of complex fortifications as a military technology used in warfare. When there are two or more concentric walls. So simply a wall and a donjon, for example, is not enough."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "complex_fortification": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of complex fortification for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Complex_fortificationUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Complex_fortification
    form_class = Complex_fortificationForm
    template_name = "wf/complex_fortification/complex_fortification_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Complex Fortification"
        context["my_exp"] = (
            "The absence or presence of complex fortifications as a military technology used in warfare. When there are two or more concentric walls. So simply a wall and a donjon, for example, is not enough."
        )

        return context


class Complex_fortificationDelete(PermissionRequiredMixin, DeleteView):
    """ """

    model = Complex_fortification
    success_url = reverse_lazy("complex_fortifications")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Complex_fortificationListView(generic.ListView):
    """ """

    model = Complex_fortification
    template_name = "wf/complex_fortification/complex_fortification_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("complex_fortifications")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Complex Fortification"
        context["var_main_desc"] = (
            "The absence or presence of complex fortifications as a military technology used in warfare. when there are two or more concentric walls. so simply a wall and a donjon, for example, is not enough."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "complex_fortification": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of complex fortification for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Complex_fortificationListViewAll(generic.ListView):
    """ """

    model = Complex_fortification
    template_name = "wf/complex_fortification/complex_fortification_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("complex_fortifications_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Complex_fortification.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Complex Fortification"
        context["var_main_desc"] = (
            "The absence or presence of complex fortifications as a military technology used in warfare. when there are two or more concentric walls. so simply a wall and a donjon, for example, is not enough."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "complex_fortification": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of complex fortification for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Complex_fortificationDetailView(generic.DetailView):
    """ """

    model = Complex_fortification
    template_name = "wf/complex_fortification/complex_fortification_detail.html"


@permission_required("core.view_capital")
def complex_fortification_download(request):
    items = Complex_fortification.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_complex_fortifications_{current_datetime}.csv"
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
            "complex_fortification",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.complex_fortification,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def complex_fortification_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        'attachment; filename="complex_fortifications.csv"'
    )

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of complex fortifications as a military technology used in warfare. When there are two or more concentric walls. So simply a wall and a donjon, for example, is not enough.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "complex_fortification": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of complex fortification for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class Modern_fortificationCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """ """

    model = Modern_fortification
    form_class = Modern_fortificationForm
    template_name = "wf/modern_fortification/modern_fortification_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("modern_fortification-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Modern Fortification"
        context["my_exp"] = (
            "The absence or presence of modern fortifications as a military technology used in warfare. used after the introduction of gunpowder, e.g., trace italienne/starfort."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "modern_fortification": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of modern fortification for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class Modern_fortificationUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Modern_fortification
    form_class = Modern_fortificationForm
    template_name = "wf/modern_fortification/modern_fortification_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Modern Fortification"
        context["my_exp"] = (
            "The absence or presence of modern fortifications as a military technology used in warfare. used after the introduction of gunpowder, e.g., trace italienne/starfort."
        )

        return context


class Modern_fortificationDelete(PermissionRequiredMixin, DeleteView):
    """ """

    model = Modern_fortification
    success_url = reverse_lazy("modern_fortifications")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Modern_fortificationListView(generic.ListView):
    """ """

    model = Modern_fortification
    template_name = "wf/modern_fortification/modern_fortification_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("modern_fortifications")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Modern Fortification"
        context["var_main_desc"] = (
            "The absence or presence of modern fortifications as a military technology used in warfare. used after the introduction of gunpowder, e.g., trace italienne/starfort."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "modern_fortification": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of modern fortification for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Modern_fortificationListViewAll(generic.ListView):
    """ """

    model = Modern_fortification
    template_name = "wf/modern_fortification/modern_fortification_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("modern_fortifications_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Modern_fortification.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Modern Fortification"
        context["var_main_desc"] = (
            "The absence or presence of modern fortifications as a military technology used in warfare. used after the introduction of gunpowder, e.g., trace italienne/starfort."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Fortifications"
        context["inner_vars"] = {
            "modern_fortification": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of modern fortification for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class Modern_fortificationDetailView(generic.DetailView):
    """ """

    model = Modern_fortification
    template_name = "wf/modern_fortification/modern_fortification_detail.html"


@permission_required("core.view_capital")
def modern_fortification_download(request):
    items = Modern_fortification.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_modern_fortifications_{current_datetime}.csv"
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
            "modern_fortification",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.modern_fortification,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def modern_fortification_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="modern_fortifications.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of modern fortifications as a military technology used in warfare. used after the introduction of gunpowder, e.g., trace italienne/starfort.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Fortifications",
    }
    my_meta_data_dic_inner_vars = {
        "modern_fortification": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of modern fortification for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


class ChainmailCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """ """

    model = Chainmail
    form_class = ChainmailForm
    template_name = "wf/chainmail/chainmail_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("chainmail-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "Warfare Variables"
        context["mysubsection"] = "Military Technologies"
        context["myvar"] = "Chainmail"
        context["my_exp"] = (
            "The absence or presence of chainmail as a military technology used in warfare. We’re using a broad definition of chainmail. Habergeon was the word used to describe the Chinese version and that would qualify as chainmail. Armor that is made of small metal rings linked together in a pattern to form a mesh."
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "chainmail": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of chainmail for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        return context


class ChainmailUpdate(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Chainmail
    form_class = ChainmailForm
    template_name = "wf/chainmail/chainmail_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Chainmail"
        context["my_exp"] = (
            "The absence or presence of chainmail as a military technology used in warfare. We’re using a broad definition of chainmail. Habergeon was the word used to describe the Chinese version and that would qualify as chainmail. Armor that is made of small metal rings linked together in a pattern to form a mesh."
        )

        return context


class ChainmailDelete(PermissionRequiredMixin, DeleteView):
    """ """

    model = Chainmail
    success_url = reverse_lazy("chainmails")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class ChainmailListView(generic.ListView):
    """ """

    model = Chainmail
    template_name = "wf/chainmail/chainmail_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("chainmails")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Chainmail"
        context["var_main_desc"] = (
            "The absence or presence of chainmail as a military technology used in warfare. we’re using a broad definition of chainmail. habergeon was the word used to describe the chinese version and that would qualify as chainmail. armor that is made of small metal rings linked together in a pattern to form a mesh."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "chainmail": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of chainmail for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class ChainmailListViewAll(generic.ListView):
    """ """

    model = Chainmail
    template_name = "wf/chainmail/chainmail_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("chainmails_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        new_context = (
            Chainmail.objects.all()
            .annotate(
                home_nga=ExpressionWrapper(
                    F("polity__home_nga__name"), output_field=CharField()
                ),
                year=Case(
                    When(year_from__isnull=False, then=F("year_from")),
                    default=F("polity__start_year"),
                    output_field=IntegerField(),
                ),
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Chainmail"
        context["var_main_desc"] = (
            "The absence or presence of chainmail as a military technology used in warfare. we’re using a broad definition of chainmail. habergeon was the word used to describe the chinese version and that would qualify as chainmail. armor that is made of small metal rings linked together in a pattern to form a mesh."
        )
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Warfare Variables"
        context["var_subsection"] = "Armor"
        context["inner_vars"] = {
            "chainmail": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of chainmail for a polity.",
                "units": None,
                "choices": [
                    "- present",
                    "- absent",
                    "- unknown",
                    "- Transitional (Absent -> Present)",
                    "- Transitional (Present -> Absent)",
                ],
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]
        context["orderby"] = self.request.GET.get("orderby", "year_from")

        return context


class ChainmailDetailView(generic.DetailView):
    """ """

    model = Chainmail
    template_name = "wf/chainmail/chainmail_detail.html"


@permission_required("core.view_capital")
def chainmail_download(request):
    items = Chainmail.objects.all()

    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"warfare_chainmails_{current_datetime}.csv"
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
            "chainmail",
            "confidence",
            "is_disputed",
            "is_uncertain",
            "expert_checked",
        ]
    )

    for obj in items:
        writer.writerow(
            [
                obj.name,
                obj.year_from,
                obj.year_to,
                obj.polity,
                obj.polity.new_name,
                obj.polity.name,
                obj.chainmail,
                obj.get_tag_display(),
                obj.is_disputed,
                obj.is_uncertain,
                obj.expert_reviewed,
            ]
        )

    return response


@permission_required("core.view_capital")
def chainmail_meta_download(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="chainmails.csv"'

    my_meta_data_dic = {
        "notes": "No_Actual_note",
        "main_desc": "The absence or presence of chainmail as a military technology used in warfare. We’re using a broad definition of chainmail. Habergeon was the word used to describe the Chinese version and that would qualify as chainmail. Armor that is made of small metal rings linked together in a pattern to form a mesh.",
        "main_desc_source": "NOTHING",
        "section": "Warfare Variables",
        "subsection": "Armor",
    }
    my_meta_data_dic_inner_vars = {
        "chainmail": {
            "min": None,
            "max": None,
            "scale": None,
            "var_exp_source": None,
            "var_exp": "The absence or presence of chainmail for a polity.",
            "units": None,
            "choices": [
                "- present",
                "- absent",
                "- unknown",
                "- Transitional (Absent -> Present)",
                "- Transitional (Present -> Absent)",
            ],
            "null_meaning": None,
        }
    }
    writer = csv.writer(response, delimiter="|")
    # bring in the meta data nedded
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


def wfvars(request):
    app_name = "wf"  # Replace with your app name
    models_1 = apps.get_app_config(app_name).get_models()

    unique_politys = set()
    number_of_all_rows = 0
    number_of_variables = 0

    all_vars_grouped = {}

    all_sect_download_links = {}

    for model in models_1:
        model_name = model.__name__
        if model_name == "Ra":
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
        subsection_value = str(model().subsection())
        sub_subsection_value = str(model().sub_subsection())
        count = model.objects.count()
        number_of_all_rows += count
        model_title = model_name.replace("_", " ").title()
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
    return render(request, "wf/wfvars.html", context=context)


@permission_required("core.view_capital")
def show_problematic_wf_data_table(request):
    # Fetch all models in the "socomp" app
    app_name = "wf"  # Replace with your app name
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
    return render(request, "wf/problematic_wf_data_table.html", {"data": data})


# @permission_required('core.view_capital')
# def show_problematic_wf_data_table(request):
#     # Fetch all models in the "socomp" app
#     app_name = 'wf'  # Replace with your app name
#     app_models = apps.get_app_config(app_name).get_models()

#     # Collect data from all models
#     data = []
#     for model in app_models:
#         items = model.objects.all()
#         for obj in items:
#             if obj.polity.start_year is not None and obj.year_from is not None and obj.polity.start_year > obj.year_from:
#                 data.append(obj)

#     # Render the template with the data
#     return render(request, 'wf/problematic_wf_data_table.html', {'data': data})


@permission_required("core.view_capital")
def download_csv_all_wf(request):
    # Fetch all models in the "socomp" app
    app_name = "wf"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_data_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    # type the headers
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
        ]
    )
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        items = model.objects.all()

        for obj in items:
            if obj.clean_name() == "long_wall":
                writer.writerow(
                    [
                        "Military Technologies",
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
                    ]
                )
            else:
                writer.writerow(
                    [
                        "Military Technologies",
                        obj.clean_name(),
                        obj.year_from,
                        obj.year_to,
                        obj.polity.long_name,
                        obj.polity.new_name,
                        obj.polity.name,
                        obj.show_value(),
                        None,
                        obj.get_tag_display(),
                        obj.is_disputed,
                        obj.is_uncertain,
                        obj.expert_reviewed,
                    ]
                )

    return response


@permission_required("core.view_capital")
def download_csv_fortifications(request):
    # Fetch all models in the "socomp" app
    app_name = "wf"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_fortifications_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    # type the headers
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
        if s_value == "Fortifications":
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
def download_csv_military_use_of_metals(request):
    # Fetch all models in the "socomp" app
    app_name = "wf"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_military_use_of_metals_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    # type the headers
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
        if s_value == "Military use of Metals":
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
def download_csv_projectiles(request):
    # Fetch all models in the "socomp" app
    app_name = "wf"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_projectiles_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    # type the headers
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
        if s_value == "Projectiles":
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
def download_csv_handheld_weapons(request):
    # Fetch all models in the "socomp" app
    app_name = "wf"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_handheld_weapons_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    # type the headers
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
        if s_value == "Handheld weapons":
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
def download_csv_animals_used_in_warfare(request):
    # Fetch all models in the "socomp" app
    app_name = "wf"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_animals_used_in_warfare_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    # type the headers
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
        if s_value == "Animals used in warfare":
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
def download_csv_armor(request):
    # Fetch all models in the "socomp" app
    app_name = "wf"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_armor_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    # type the headers
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
        if s_value == "Armor":
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
def download_csv_naval_technology(request):
    # Fetch all models in the "socomp" app
    app_name = "wf"  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"warfare_naval_technology_{current_datetime}.csv"

    response["Content-Disposition"] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter="|")

    # type the headers
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
        if s_value == "Naval technology":
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
