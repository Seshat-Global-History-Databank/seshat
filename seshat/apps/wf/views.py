from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from ..general.mixins import PolityIdMixin
from ..constants import (
    ABSENT_PRESENT_STRING_LIST,
    CORRECT_YEAR,
    POLITY_NGA_NAME,
)

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


class Long_wallCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    Create a new Long_wall instance.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Long_wall
    form_class = Long_wallForm
    template_name = "wf/long_wall/long_wall_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("long_wall-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Long Wall"
        context["my_exp"] = (
            "The absence or presence or height of long walls. (code absent as number zero on the long_wall_from / and for coding  'unknown', keep the long_wall_from and long_wall_to empty and only select the confidence etc.)"  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Long_wallUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Update an existing Long_wall instance.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Long_wall
    form_class = Long_wallForm
    template_name = "wf/long_wall/long_wall_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Long Wall",
                "my_exp": "The absence or presence or height of long walls. (code absent as number zero on the long_wall_from / and for coding  'unknown', keep the long_wall_from and long_wall_to empty and only select the confidence etc.)",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Long_wallDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Delete an existing Long_wall instance.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Long_wall
    success_url = reverse_lazy("long_walls")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Long_wallListView(ListView):
    """
    Display a list of Long_wall instances.
    """

    model = Long_wall
    template_name = "wf/long_wall/long_wall_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("long_walls")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Long Wall",
                "var_main_desc": "The absence or presence or height of long walls.",
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military Technologies",
                "inner_vars": {
                    "long_wall": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence or height of long walls for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": "km",
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Long_wallListAllView(ListView):
    """ """

    model = Long_wall
    template_name = "wf/long_wall/long_wall_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Long Wall",
                "var_main_desc": "The absence or presence or height of long walls.",
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military Technologies",
                "inner_vars": {
                    "long_wall": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence or height of long walls for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": "km",
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Long_wallDetailView(DetailView):
    """ """

    model = Long_wall
    template_name = "wf/long_wall/long_wall_detail.html"


class CopperCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Copper
    form_class = CopperForm
    template_name = "wf/copper/copper_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("copper-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class CopperUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Copper",
                "my_exp": "The absence or presence of copper as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class CopperDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Copper
    success_url = reverse_lazy("coppers")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CopperListView(ListView):
    """ """

    model = Copper
    template_name = "wf/copper/copper_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("coppers")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Copper",
                "var_main_desc": "The absence or presence of copper as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military use of Metals",
                "inner_vars": {
                    "copper": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of copper for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class CopperListAllView(ListView):
    """ """

    model = Copper
    template_name = "wf/copper/copper_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Copper",
                "var_main_desc": "The absence or presence of copper as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military use of Metals",
                "inner_vars": {
                    "copper": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of copper for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class CopperDetailView(DetailView):
    """ """

    model = Copper
    template_name = "wf/copper/copper_detail.html"


class BronzeCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Bronze
    form_class = BronzeForm
    template_name = "wf/bronze/bronze_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("bronze-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Bronze"
        context["my_exp"] = (
            "The absence or presence of bronze as a military technology used in warfare. Bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class BronzeUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Bronze",
                "my_exp": "The absence or presence of bronze as a military technology used in warfare. Bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class BronzeDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Bronze
    success_url = reverse_lazy("bronzes")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class BronzeListView(ListView):
    """ """

    model = Bronze
    template_name = "wf/bronze/bronze_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("bronzes")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Bronze",
                "var_main_desc": "The absence or presence of bronze as a military technology used in warfare. bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military use of Metals",
                "inner_vars": {
                    "bronze": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of bronze for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class BronzeListAllView(ListView):
    """ """

    model = Bronze
    template_name = "wf/bronze/bronze_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Bronze",
                "var_main_desc": "The absence or presence of bronze as a military technology used in warfare. bronze is an alloy that includes copper, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. consequently, if a culture uses bronze in warfare and there is no mention of using copper then 'inferred present' is probably best.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military use of Metals",
                "inner_vars": {
                    "bronze": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of bronze for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class BronzeDetailView(DetailView):
    """ """

    model = Bronze
    template_name = "wf/bronze/bronze_detail.html"


class IronCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Iron
    form_class = IronForm
    template_name = "wf/iron/iron_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("iron-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class IronUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Iron",
                "my_exp": "The absence or presence of iron as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class IronDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Iron
    success_url = reverse_lazy("irons")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class IronListView(ListView):
    """ """

    model = Iron
    template_name = "wf/iron/iron_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("irons")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Iron",
                "var_main_desc": "The absence or presence of iron as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military use of Metals",
                "inner_vars": {
                    "iron": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of iron for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class IronListAllView(ListView):
    """ """

    model = Iron
    template_name = "wf/iron/iron_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Iron",
                "var_main_desc": "The absence or presence of iron as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military use of Metals",
                "inner_vars": {
                    "iron": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of iron for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class IronDetailView(DetailView):
    """ """

    model = Iron
    template_name = "wf/iron/iron_detail.html"


class SteelCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Steel
    form_class = SteelForm
    template_name = "wf/steel/steel_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("steel-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Steel"
        context["my_exp"] = (
            "The absence or presence of steel as a military technology used in warfare. Steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class SteelUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Steel",
                "my_exp": "The absence or presence of steel as a military technology used in warfare. Steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. Consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class SteelDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Steel
    success_url = reverse_lazy("steels")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SteelListView(ListView):
    """ """

    model = Steel
    template_name = "wf/steel/steel_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("steels")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Steel",
                "var_main_desc": "The absence or presence of steel as a military technology used in warfare. steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military use of Metals",
                "inner_vars": {
                    "steel": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of steel for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class SteelListAllView(ListView):
    """ """

    model = Steel
    template_name = "wf/steel/steel_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Steel",
                "var_main_desc": "The absence or presence of steel as a military technology used in warfare. steel is an alloy that includes iron, so a polity that uses bronze in warfare is familiar with copper technology and probably uses it to at least a limited extent. consequently, if a culture uses steel in warfare and there is no mention of using iron then 'inferred present' is probably best.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Military use of Metals",
                "inner_vars": {
                    "steel": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of steel for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class SteelDetailView(DetailView):
    """ """

    model = Steel
    template_name = "wf/steel/steel_detail.html"


class JavelinCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Javelin
    form_class = JavelinForm
    template_name = "wf/javelin/javelin_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("javelin-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Javelin"
        context["my_exp"] = (
            "The absence or presence of javelins as a military technology used in warfare. Includes thrown spears"  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class JavelinUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Javelin",
                "my_exp": "The absence or presence of javelins as a military technology used in warfare. Includes thrown spears",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class JavelinDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Javelin
    success_url = reverse_lazy("javelins")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class JavelinListView(ListView):
    """ """

    model = Javelin
    template_name = "wf/javelin/javelin_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("javelins")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Javelin",
                "var_main_desc": "The absence or presence of javelins as a military technology used in warfare. includes thrown spears",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "javelin": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of javelin for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class JavelinListAllView(ListView):
    """ """

    model = Javelin
    template_name = "wf/javelin/javelin_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Javelin",
                "var_main_desc": "The absence or presence of javelins as a military technology used in warfare. includes thrown spears",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "javelin": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of javelin for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class JavelinDetailView(DetailView):
    """ """

    model = Javelin
    template_name = "wf/javelin/javelin_detail.html"


class AtlatlCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Atlatl
    form_class = AtlatlForm
    template_name = "wf/atlatl/atlatl_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("atlatl-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class AtlatlUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Atlatl",
                "my_exp": "The absence or presence of atlatl as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class AtlatlDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Atlatl
    success_url = reverse_lazy("atlatls")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class AtlatlListView(ListView):
    """ """

    model = Atlatl
    template_name = "wf/atlatl/atlatl_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("atlatls")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Atlatl",
                "var_main_desc": "The absence or presence of atlatl as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "atlatl": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of atlatl for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class AtlatlListAllView(ListView):
    """ """

    model = Atlatl
    template_name = "wf/atlatl/atlatl_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Atlatl",
                "var_main_desc": "The absence or presence of atlatl as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "atlatl": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of atlatl for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class AtlatlDetailView(DetailView):
    """ """

    model = Atlatl
    template_name = "wf/atlatl/atlatl_detail.html"


class SlingCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling
    form_class = SlingForm
    template_name = "wf/sling/sling_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sling-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class SlingUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Sling",
                "my_exp": "The absence or presence of slings as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class SlingDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling
    success_url = reverse_lazy("slings")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SlingListView(ListView):
    """ """

    model = Sling
    template_name = "wf/sling/sling_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("slings")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Sling",
                "var_main_desc": "The absence or presence of slings as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "sling": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of sling for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class SlingListAllView(ListView):
    """ """

    model = Sling
    template_name = "wf/sling/sling_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Sling",
                "var_main_desc": "The absence or presence of slings as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "sling": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of sling for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class SlingDetailView(DetailView):
    """ """

    model = Sling
    template_name = "wf/sling/sling_detail.html"


class Self_bowCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Self_bow
    form_class = Self_bowForm
    template_name = "wf/self_bow/self_bow_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("self_bow-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Self Bow"
        context["my_exp"] = (
            "The absence or presence of self bow as a military technology used in warfare. This is a bow made from a single piece of wood (example: the English/Welsh longbow)"  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Self_bowUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Self Bow",
                "my_exp": "The absence or presence of self bow as a military technology used in warfare. This is a bow made from a single piece of wood (example: the English/Welsh longbow)",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Self_bowDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Self_bow
    success_url = reverse_lazy("self_bows")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Self_bowListView(ListView):
    """ """

    model = Self_bow
    template_name = "wf/self_bow/self_bow_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("self_bows")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Self Bow",
                "var_main_desc": "The absence or presence of self bow as a military technology used in warfare. this is a bow made from a single piece of wood (example: the english/welsh longbow)",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "self_bow": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of self bow for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Self_bowListAllView(ListView):
    """ """

    model = Self_bow
    template_name = "wf/self_bow/self_bow_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Self Bow",
                "var_main_desc": "The absence or presence of self bow as a military technology used in warfare. this is a bow made from a single piece of wood (example: the english/welsh longbow)",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "self_bow": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of self bow for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Self_bowDetailView(DetailView):
    """ """

    model = Self_bow
    template_name = "wf/self_bow/self_bow_detail.html"


class Composite_bowCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Composite_bow
    form_class = Composite_bowForm
    template_name = "wf/composite_bow/composite_bow_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("composite_bow-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Composite Bow"
        context["my_exp"] = (
            "The absence or presence of composite bow as a military technology used in warfare. This is a bow made from several different materials, usually wood, horn, and sinew. Also known as laminated bow. Recurved bows should be coded here as well, because usually they are composite bows. When there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present)."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Composite_bowUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Composite Bow",
                "my_exp": "The absence or presence of composite bow as a military technology used in warfare. This is a bow made from several different materials, usually wood, horn, and sinew. Also known as laminated bow. Recurved bows should be coded here as well, because usually they are composite bows. When there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present).",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Composite_bowDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Composite_bow
    success_url = reverse_lazy("composite_bows")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Composite_bowListView(ListView):
    """ """

    model = Composite_bow
    template_name = "wf/composite_bow/composite_bow_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("composite_bows")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Composite Bow",
                "var_main_desc": "The absence or presence of composite bow as a military technology used in warfare. this is a bow made from several different materials, usually wood, horn, and sinew. also known as laminated bow. recurved bows should be coded here as well, because usually they are composite bows. when there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present).",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "composite_bow": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of composite bow for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Composite_bowListAllView(ListView):
    """ """

    model = Composite_bow
    template_name = "wf/composite_bow/composite_bow_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Composite Bow",
                "var_main_desc": "The absence or presence of composite bow as a military technology used in warfare. this is a bow made from several different materials, usually wood, horn, and sinew. also known as laminated bow. recurved bows should be coded here as well, because usually they are composite bows. when there is evidence for bows (or arrows) and no specific comment about how sophisticated the bows are then 'inferred present' for self bows and 'inferred absent' for composite bows is generally best (along with brief notes indicating that it is best to assume the less sophisticated rather than the more sophisticated technology is present).",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "composite_bow": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of composite bow for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Composite_bowDetailView(DetailView):
    """ """

    model = Composite_bow
    template_name = "wf/composite_bow/composite_bow_detail.html"


class CrossbowCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Crossbow
    form_class = CrossbowForm
    template_name = "wf/crossbow/crossbow_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("crossbow-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class CrossbowUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Crossbow",
                "my_exp": "The absence or presence of crossbow as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class CrossbowDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Crossbow
    success_url = reverse_lazy("crossbows")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CrossbowListView(ListView):
    """ """

    model = Crossbow
    template_name = "wf/crossbow/crossbow_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("crossbows")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Crossbow",
                "var_main_desc": "The absence or presence of crossbow as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "crossbow": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of crossbow for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class CrossbowListAllView(ListView):
    """ """

    model = Crossbow
    template_name = "wf/crossbow/crossbow_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Crossbow",
                "var_main_desc": "The absence or presence of crossbow as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "crossbow": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of crossbow for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class CrossbowDetailView(DetailView):
    """ """

    model = Crossbow
    template_name = "wf/crossbow/crossbow_detail.html"


class Tension_siege_engineCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Tension_siege_engine
    form_class = Tension_siege_engineForm
    template_name = "wf/tension_siege_engine/tension_siege_engine_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("tension_siege_engine-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Tension Siege Engine"
        context["my_exp"] = (
            "The absence or presence of tension siege engines as a military technology used in warfare. For example, catapult, onager"  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Tension_siege_engineUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Tension Siege Engine",
                "my_exp": "The absence or presence of tension siege engines as a military technology used in warfare. For example, catapult, onager",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Tension_siege_engineDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Tension_siege_engine
    success_url = reverse_lazy("tension_siege_engines")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Tension_siege_engineListView(ListView):
    """ """

    model = Tension_siege_engine
    template_name = "wf/tension_siege_engine/tension_siege_engine_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("tension_siege_engines")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Tension Siege Engine",
                "var_main_desc": "The absence or presence of tension siege engines as a military technology used in warfare. for example, catapult, onager",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "tension_siege_engine": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of tension siege engine for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Tension_siege_engineListAllView(ListView):
    """ """

    model = Tension_siege_engine
    template_name = (
        "wf/tension_siege_engine/tension_siege_engine_list_all.html"
    )

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Tension Siege Engine",
                "var_main_desc": "The absence or presence of tension siege engines as a military technology used in warfare. for example, catapult, onager",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "tension_siege_engine": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of tension siege engine for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Tension_siege_engineDetailView(DetailView):
    """ """

    model = Tension_siege_engine
    template_name = "wf/tension_siege_engine/tension_siege_engine_detail.html"


class Sling_siege_engineCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling_siege_engine
    form_class = Sling_siege_engineForm
    template_name = "wf/sling_siege_engine/sling_siege_engine_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sling_siege_engine-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Sling Siege Engine"
        context["my_exp"] = (
            "The absence or presence of sling siege engines as a military technology used in warfare. E.g., trebuchet, innclude mangonels here"  # noqa: E501 pylint: disable=C0301
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "sling_siege_engine": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of sling siege engine for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Sling_siege_engineUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Sling Siege Engine",
                "my_exp": "The absence or presence of sling siege engines as a military technology used in warfare. E.g., trebuchet, innclude mangonels here",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Sling_siege_engineDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sling_siege_engine
    success_url = reverse_lazy("sling_siege_engines")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Sling_siege_engineListView(ListView):
    """ """

    model = Sling_siege_engine
    template_name = "wf/sling_siege_engine/sling_siege_engine_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sling_siege_engines")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Sling Siege Engine",
                "var_main_desc": "The absence or presence of sling siege engines as a military technology used in warfare. e.g., trebuchet, innclude mangonels here",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "sling_siege_engine": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of sling siege engine for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Sling_siege_engineListAllView(ListView):
    """ """

    model = Sling_siege_engine
    template_name = "wf/sling_siege_engine/sling_siege_engine_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Sling Siege Engine",
                "var_main_desc": "The absence or presence of sling siege engines as a military technology used in warfare. e.g., trebuchet, innclude mangonels here",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "sling_siege_engine": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of sling siege engine for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Sling_siege_engineDetailView(DetailView):
    """ """

    model = Sling_siege_engine
    template_name = "wf/sling_siege_engine/sling_siege_engine_detail.html"


class Gunpowder_siege_artilleryCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Gunpowder_siege_artillery
    form_class = Gunpowder_siege_artilleryForm
    template_name = (
        "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("gunpowder_siege_artillery-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Gunpowder Siege Artillery"
        context["my_exp"] = (
            "The absence or presence of gunpowder siege artillery as a military technology used in warfare. For example, cannon, mortars."  # noqa: E501 pylint: disable=C0301
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "gunpowder_siege_artillery": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of gunpowder siege artillery for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Gunpowder_siege_artilleryUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Gunpowder_siege_artillery
    form_class = Gunpowder_siege_artilleryForm
    template_name = (
        "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_update.html"
    )
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Gunpowder Siege Artillery",
                "my_exp": "The absence or presence of gunpowder siege artillery as a military technology used in warfare. For example, cannon, mortars.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Gunpowder_siege_artilleryDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Gunpowder_siege_artillery
    success_url = reverse_lazy("gunpowder_siege_artillerys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Gunpowder_siege_artilleryListView(ListView):
    """ """

    model = Gunpowder_siege_artillery
    template_name = (
        "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("gunpowder_siege_artillerys")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Gunpowder Siege Artillery",
                "var_main_desc": "The absence or presence of gunpowder siege artillery as a military technology used in warfare. for example, cannon, mortars.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "gunpowder_siege_artillery": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of gunpowder siege artillery for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Gunpowder_siege_artilleryListAllView(ListView):
    """ """

    model = Gunpowder_siege_artillery
    template_name = (
        "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_list_all.html"
    )

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Gunpowder Siege Artillery",
                "var_main_desc": "The absence or presence of gunpowder siege artillery as a military technology used in warfare. for example, cannon, mortars.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "gunpowder_siege_artillery": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of gunpowder siege artillery for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Gunpowder_siege_artilleryDetailView(DetailView):
    """ """

    model = Gunpowder_siege_artillery
    template_name = (
        "wf/gunpowder_siege_artillery/gunpowder_siege_artillery_detail.html"
    )


class Handheld_firearmCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Handheld_firearm
    form_class = Handheld_firearmForm
    template_name = "wf/handheld_firearm/handheld_firearm_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("handheld_firearm-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Handheld Firearm"
        context["my_exp"] = (
            "The absence or presence of handheld firearms as a military technology used in warfare. E.g., muskets, pistols, and rifles"  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Handheld_firearmUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Handheld Firearm",
                "my_exp": "The absence or presence of handheld firearms as a military technology used in warfare. E.g., muskets, pistols, and rifles",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Handheld_firearmDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Handheld_firearm
    success_url = reverse_lazy("handheld_firearms")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Handheld_firearmListView(ListView):
    """ """

    model = Handheld_firearm
    template_name = "wf/handheld_firearm/handheld_firearm_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("handheld_firearms")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Handheld Firearm",
                "var_main_desc": "The absence or presence of handheld firearms as a military technology used in warfare. e.g., muskets, pistols, and rifles",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "handheld_firearm": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of handheld firearm for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Handheld_firearmListAllView(ListView):
    """ """

    model = Handheld_firearm
    template_name = "wf/handheld_firearm/handheld_firearm_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Handheld Firearm",
                "var_main_desc": "The absence or presence of handheld firearms as a military technology used in warfare. e.g., muskets, pistols, and rifles",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Projectiles",
                "inner_vars": {
                    "handheld_firearm": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of handheld firearm for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Handheld_firearmDetailView(DetailView):
    """ """

    model = Handheld_firearm
    template_name = "wf/handheld_firearm/handheld_firearm_detail.html"


class War_clubCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = War_club
    form_class = War_clubForm
    template_name = "wf/war_club/war_club_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("war_club-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "War Club"
        context["my_exp"] = (
            "The absence or presence of war clubs as a military technology used in warfare. Includes maces"  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class War_clubUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "War Club",
                "my_exp": "The absence or presence of war clubs as a military technology used in warfare. Includes maces",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class War_clubDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = War_club
    success_url = reverse_lazy("war_clubs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class War_clubListView(ListView):
    """ """

    model = War_club
    template_name = "wf/war_club/war_club_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("war_clubs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "War Club",
                "var_main_desc": "The absence or presence of war clubs as a military technology used in warfare. includes maces",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "war_club": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of war club for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class War_clubListAllView(ListView):
    """ """

    model = War_club
    template_name = "wf/war_club/war_club_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "War Club",
                "var_main_desc": "The absence or presence of war clubs as a military technology used in warfare. includes maces",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "war_club": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of war club for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class War_clubDetailView(DetailView):
    """ """

    model = War_club
    template_name = "wf/war_club/war_club_detail.html"


class Battle_axeCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Battle_axe
    form_class = Battle_axeForm
    template_name = "wf/battle_axe/battle_axe_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("battle_axe-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Battle Axe"
        context["my_exp"] = (
            "The absence or presence of battle axes as a military technology used in warfare. Axes designed for military use."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Battle_axeUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Battle Axe",
                "my_exp": "The absence or presence of battle axes as a military technology used in warfare. Axes designed for military use.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Battle_axeDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Battle_axe
    success_url = reverse_lazy("battle_axes")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Battle_axeListView(ListView):
    """ """

    model = Battle_axe
    template_name = "wf/battle_axe/battle_axe_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("battle_axes")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Battle Axe",
                "var_main_desc": "The absence or presence of battle axes as a military technology used in warfare. axes designed for military use.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "battle_axe": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of battle axe for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Battle_axeListAllView(ListView):
    """ """

    model = Battle_axe
    template_name = "wf/battle_axe/battle_axe_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Battle Axe",
                "var_main_desc": "The absence or presence of battle axes as a military technology used in warfare. axes designed for military use.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "battle_axe": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of battle axe for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Battle_axeDetailView(DetailView):
    """ """

    model = Battle_axe
    template_name = "wf/battle_axe/battle_axe_detail.html"


class DaggerCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dagger
    form_class = DaggerForm
    template_name = "wf/dagger/dagger_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("dagger-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Dagger"
        context["my_exp"] = (
            "The absence or presence of daggers as a military technology used in warfare. Bladed weapons shorter than 50 cm. Includes knives. Material is not important (coded elsewhere), thus flint daggers should be coded as present."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class DaggerUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Dagger",
                "my_exp": "The absence or presence of daggers as a military technology used in warfare. Bladed weapons shorter than 50 cm. Includes knives. Material is not important (coded elsewhere), thus flint daggers should be coded as present.",  # noqa: E501 pylint: disable=C0301
            },
        )
        context["myvar"] = "Dagger"
        context["my_exp"] = (
            "The absence or presence of daggers as a military technology used in warfare. Bladed weapons shorter than 50 cm. Includes knives. Material is not important (coded elsewhere), thus flint daggers should be coded as present."  # noqa: E501 pylint: disable=C0301
        )

        return context


class DaggerDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dagger
    success_url = reverse_lazy("daggers")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class DaggerListView(ListView):
    """ """

    model = Dagger
    template_name = "wf/dagger/dagger_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("daggers")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Dagger",
                "var_main_desc": "The absence or presence of daggers as a military technology used in warfare. bladed weapons shorter than 50 cm. includes knives. material is not important (coded elsewhere), thus flint daggers should be coded as present.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "dagger": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of dagger for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class DaggerListAllView(ListView):
    """ """

    model = Dagger
    template_name = "wf/dagger/dagger_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Dagger",
                "var_main_desc": "The absence or presence of daggers as a military technology used in warfare. bladed weapons shorter than 50 cm. includes knives. material is not important (coded elsewhere), thus flint daggers should be coded as present.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "dagger": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of dagger for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class DaggerDetailView(DetailView):
    """ """

    model = Dagger
    template_name = "wf/dagger/dagger_detail.html"


class SwordCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sword
    form_class = SwordForm
    template_name = "wf/sword/sword_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("sword-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Sword"
        context["my_exp"] = (
            "The absence or presence of swords as a military technology used in warfare. Bladed weapons longer than 50 cm. A machete is a sword (assuming the blade is probably longer than 50 cm). Material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class SwordUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Sword",
                "my_exp": "The absence or presence of swords as a military technology used in warfare. Bladed weapons longer than 50 cm. A machete is a sword (assuming the blade is probably longer than 50 cm). Material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class SwordDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Sword
    success_url = reverse_lazy("swords")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SwordListView(ListView):
    """ """

    model = Sword
    template_name = "wf/sword/sword_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("swords")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Sword",
                "var_main_desc": "The absence or presence of swords as a military technology used in warfare. bladed weapons longer than 50 cm. a machete is a sword (assuming the blade is probably longer than 50 cm). material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "sword": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of sword for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class SwordListAllView(ListView):
    """ """

    model = Sword
    template_name = "wf/sword/sword_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Sword",
                "var_main_desc": "The absence or presence of swords as a military technology used in warfare. bladed weapons longer than 50 cm. a machete is a sword (assuming the blade is probably longer than 50 cm). material is not important (coded elsewhere), thus swords made from hard wood, or those edged with stones or bone should be coded as present.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "sword": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of sword for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class SwordDetailView(DetailView):
    """ """

    model = Sword
    template_name = "wf/sword/sword_detail.html"


class SpearCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Spear
    form_class = SpearForm
    template_name = "wf/spear/spear_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("spear-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Spear"
        context["my_exp"] = (
            "The absence or presence of spears as a military technology used in warfare. Includes lances and pikes. A trident is a spear."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class SpearUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Spear",
                "my_exp": "The absence or presence of spears as a military technology used in warfare. Includes lances and pikes. A trident is a spear.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class SpearDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Spear
    success_url = reverse_lazy("spears")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class SpearListView(ListView):
    """ """

    model = Spear
    template_name = "wf/spear/spear_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("spears")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Spear",
                "var_main_desc": "The absence or presence of spears as a military technology used in warfare. includes lances and pikes. a trident is a spear.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "spear": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of spear for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class SpearListAllView(ListView):
    """ """

    model = Spear
    template_name = "wf/spear/spear_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Spear",
                "var_main_desc": "The absence or presence of spears as a military technology used in warfare. includes lances and pikes. a trident is a spear.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "spear": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of spear for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class SpearDetailView(DetailView):
    """ """

    model = Spear
    template_name = "wf/spear/spear_detail.html"


class PolearmCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polearm
    form_class = PolearmForm
    template_name = "wf/polearm/polearm_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polearm-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Polearm"
        context["my_exp"] = (
            "The absence or presence of polearms as a military technology used in warfare. This category includes halberds, naginatas, and morning stars"  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class PolearmUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Polearm",
                "my_exp": "The absence or presence of polearms as a military technology used in warfare. This category includes halberds, naginatas, and morning stars",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class PolearmDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Polearm
    success_url = reverse_lazy("polearms")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class PolearmListView(ListView):
    """ """

    model = Polearm
    template_name = "wf/polearm/polearm_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("polearms")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Polearm",
                "var_main_desc": "The absence or presence of polearms as a military technology used in warfare. this category includes halberds, naginatas, and morning stars",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "polearm": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of polearm for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class PolearmListAllView(ListView):
    """ """

    model = Polearm
    template_name = "wf/polearm/polearm_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Polearm",
                "var_main_desc": "The absence or presence of polearms as a military technology used in warfare. this category includes halberds, naginatas, and morning stars",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Handheld weapons",
                "inner_vars": {
                    "polearm": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of polearm for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class PolearmDetailView(DetailView):
    """ """

    model = Polearm
    template_name = "wf/polearm/polearm_detail.html"


class DogCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dog
    form_class = DogForm
    template_name = "wf/dog/dog_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("dog-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class DogUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Dog",
                "my_exp": "The absence or presence of dogs as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class DogDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Dog
    success_url = reverse_lazy("dogs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class DogListView(ListView):
    """ """

    model = Dog
    template_name = "wf/dog/dog_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("dogs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Dog",
                "var_main_desc": "The absence or presence of dogs as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "dog": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of dog for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class DogListAllView(ListView):
    """ """

    model = Dog
    template_name = "wf/dog/dog_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Dog",
                "var_main_desc": "The absence or presence of dogs as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "dog": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of dog for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class DogDetailView(DetailView):
    """ """

    model = Dog
    template_name = "wf/dog/dog_detail.html"


class DonkeyCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Donkey
    form_class = DonkeyForm
    template_name = "wf/donkey/donkey_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("donkey-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class DonkeyUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Donkey",
                "my_exp": "The absence or presence of donkeys as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class DonkeyDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Donkey
    success_url = reverse_lazy("donkeys")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class DonkeyListView(ListView):
    """ """

    model = Donkey
    template_name = "wf/donkey/donkey_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("donkeys")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Donkey",
                "var_main_desc": "The absence or presence of donkeys as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "donkey": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of donkey for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class DonkeyListAllView(ListView):
    """ """

    model = Donkey
    template_name = "wf/donkey/donkey_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Donkey",
                "var_main_desc": "The absence or presence of donkeys as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "donkey": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of donkey for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class DonkeyDetailView(DetailView):
    """ """

    model = Donkey
    template_name = "wf/donkey/donkey_detail.html"


class HorseCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Horse
    form_class = HorseForm
    template_name = "wf/horse/horse_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("horse-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class HorseUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Horse",
                "my_exp": "The absence or presence of horses as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class HorseDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Horse
    success_url = reverse_lazy("horses")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class HorseListView(ListView):
    """ """

    model = Horse
    template_name = "wf/horse/horse_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("horses")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Horse",
                "var_main_desc": "The absence or presence of horses as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "horse": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of horse for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class HorseListAllView(ListView):
    """ """

    model = Horse
    template_name = "wf/horse/horse_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Horse",
                "var_main_desc": "The absence or presence of horses as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "horse": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of horse for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class HorseDetailView(DetailView):
    """ """

    model = Horse
    template_name = "wf/horse/horse_detail.html"


class CamelCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Camel
    form_class = CamelForm
    template_name = "wf/camel/camel_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("camel-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class CamelUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Camel",
                "my_exp": "The absence or presence of camels as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class CamelDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Camel
    success_url = reverse_lazy("camels")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class CamelListView(ListView):
    """ """

    model = Camel
    template_name = "wf/camel/camel_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("camels")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Camel",
                "var_main_desc": "The absence or presence of camels as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "camel": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of camel for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class CamelListAllView(ListView):
    """ """

    model = Camel
    template_name = "wf/camel/camel_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Camel",
                "var_main_desc": "The absence or presence of camels as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "camel": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of camel for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class CamelDetailView(DetailView):
    """ """

    model = Camel
    template_name = "wf/camel/camel_detail.html"


class ElephantCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Elephant
    form_class = ElephantForm
    template_name = "wf/elephant/elephant_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("elephant-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Elephant"
        context["my_exp"] = (
            "The absence or presence of elephants as a military technology used in warfare. "  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class ElephantUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Elephant",
                "my_exp": "The absence or presence of elephants as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class ElephantDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Elephant
    success_url = reverse_lazy("elephants")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class ElephantListView(ListView):
    """ """

    model = Elephant
    template_name = "wf/elephant/elephant_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("elephants")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Elephant",
                "var_main_desc": "The absence or presence of elephants as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "elephant": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of elephant for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class ElephantListAllView(ListView):
    """ """

    model = Elephant
    template_name = "wf/elephant/elephant_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Elephant",
                "var_main_desc": "The absence or presence of elephants as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Animals used in warfare",
                "inner_vars": {
                    "elephant": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of elephant for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class ElephantDetailView(DetailView):
    """ """

    model = Elephant
    template_name = "wf/elephant/elephant_detail.html"


class Wood_bark_etcCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wood_bark_etc
    form_class = Wood_bark_etcForm
    template_name = "wf/wood_bark_etc/wood_bark_etc_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wood_bark_etc-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Wood Bark Etc"
        context["my_exp"] = (
            "The absence or presence of wood, bark, etc. as a military technology used in warfare. "  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Wood_bark_etcUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Wood Bark Etc",
                "my_exp": "The absence or presence of wood, bark, etc. as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Wood_bark_etcDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wood_bark_etc
    success_url = reverse_lazy("wood_bark_etcs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Wood_bark_etcListView(ListView):
    """ """

    model = Wood_bark_etc
    template_name = "wf/wood_bark_etc/wood_bark_etc_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wood_bark_etcs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Wood Bark Etc",
                "var_main_desc": "The absence or presence of wood, bark, etc. as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "wood_bark_etc": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of wood bark etc for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Wood_bark_etcListAllView(ListView):
    """ """

    model = Wood_bark_etc
    template_name = "wf/wood_bark_etc/wood_bark_etc_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Wood Bark Etc",
                "var_main_desc": "The absence or presence of wood, bark, etc. as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "wood_bark_etc": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of wood bark etc for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Wood_bark_etcDetailView(DetailView):
    """ """

    model = Wood_bark_etc
    template_name = "wf/wood_bark_etc/wood_bark_etc_detail.html"


class Leather_clothCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Leather_cloth
    form_class = Leather_clothForm
    template_name = "wf/leather_cloth/leather_cloth_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("leather_cloth-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Leather Cloth"
        context["my_exp"] = (
            "The absence or presence of leather, cloth as a military technology used in warfare. For example, leather cuirass, quilted cotton armor"  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Leather_clothUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Leather Cloth",
                "my_exp": "The absence or presence of leather, cloth as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Leather_clothDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Leather_cloth
    success_url = reverse_lazy("leather_cloths")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Leather_clothListView(ListView):
    """ """

    model = Leather_cloth
    template_name = "wf/leather_cloth/leather_cloth_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("leather_cloths")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Leather Cloth",
                "var_main_desc": "The absence or presence of leather, cloth as a military technology used in warfare. for example, leather cuirass, quilted cotton armor",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "leather_cloth": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of leather cloth for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Leather_clothListAllView(ListView):
    """ """

    model = Leather_cloth
    template_name = "wf/leather_cloth/leather_cloth_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Leather Cloth",
                "var_main_desc": "The absence or presence of leather, cloth as a military technology used in warfare. for example, leather cuirass, quilted cotton armor",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "leather_cloth": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of leather cloth for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Leather_clothDetailView(DetailView):
    """ """

    model = Leather_cloth
    template_name = "wf/leather_cloth/leather_cloth_detail.html"


class ShieldCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Shield
    form_class = ShieldForm
    template_name = "wf/shield/shield_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("shield-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class ShieldUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Shield",
                "my_exp": "The absence or presence of shields as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class ShieldDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Shield
    success_url = reverse_lazy("shields")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class ShieldListView(ListView):
    """ """

    model = Shield
    template_name = "wf/shield/shield_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("shields")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Shield",
                "var_main_desc": "The absence or presence of shields as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "shield": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of shield for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class ShieldListAllView(ListView):
    """ """

    model = Shield
    template_name = "wf/shield/shield_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Shield",
                "var_main_desc": "The absence or presence of shields as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "shield": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of shield for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class ShieldDetailView(DetailView):
    """ """

    model = Shield
    template_name = "wf/shield/shield_detail.html"


class HelmetCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Helmet
    form_class = HelmetForm
    template_name = "wf/helmet/helmet_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("helmet-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class HelmetUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Helmet",
                "my_exp": "The absence or presence of helmets as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class HelmetDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Helmet
    success_url = reverse_lazy("helmets")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class HelmetListView(ListView):
    """ """

    model = Helmet
    template_name = "wf/helmet/helmet_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("helmets")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Helmet",
                "var_main_desc": "The absence or presence of helmets as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "helmet": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of helmet for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class HelmetListAllView(ListView):
    """ """

    model = Helmet
    template_name = "wf/helmet/helmet_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Helmet",
                "var_main_desc": "The absence or presence of helmets as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "helmet": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of helmet for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class HelmetDetailView(DetailView):
    """ """

    model = Helmet
    template_name = "wf/helmet/helmet_detail.html"


class BreastplateCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Breastplate
    form_class = BreastplateForm
    template_name = "wf/breastplate/breastplate_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("breastplate-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Breastplate"
        context["my_exp"] = (
            "The absence or presence of breastplates as a military technology used in warfare. Armor made from wood, horn, or bone can be very important (as in the spread of the Asian War Complex into North America). Leather and cotton (in the Americas) armor was also effective against arrows and warclubs. Breastplate refers to any form of torso protection (in fact, we might rename this variable 'torso protection' at a later date). In the vast majority of cases you will probably find that if a culture has wooden armor, leather armor, chainmail armor, or scaled armor that breastplate should be coded as present because this is the most common location for armor. However, in theory, it is possible to have armor that doesn't protect the torso (for example, a culture might use armor that protects the limbs only)."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class BreastplateUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Breastplate",
                "my_exp": "The absence or presence of breastplates as a military technology used in warfare. Armor made from wood, horn, or bone can be very important (as in the spread of the Asian War Complex into North America). Leather and cotton (in the Americas) armor was also effective against arrows and warclubs. Breastplate refers to any form of torso protection (in fact, we might rename this variable 'torso protection' at a later date). In the vast majority of cases you will probably find that if a culture has wooden armor, leather armor, chainmail armor, or scaled armor that breastplate should be coded as present because this is the most common location for armor. However, in theory, it is possible to have armor that doesn't protect the torso (for example, a culture might use armor that protects the limbs only).",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class BreastplateDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Breastplate
    success_url = reverse_lazy("breastplates")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class BreastplateListView(ListView):
    """ """

    model = Breastplate
    template_name = "wf/breastplate/breastplate_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("breastplates")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Breastplate",
                "var_main_desc": "The absence or presence of breastplates as a military technology used in warfare. armor made from wood, horn, or bone can be very important (as in the spread of the asian war complex into north america). leather and cotton (in the americas) armor was also effective against arrows and warclubs. breastplate refers to any form of torso protection (in fact, we might rename this variable 'torso protection' at a later date). in the vast majority of cases you will probably find that if a culture has wooden armor, leather armor, chainmail armor, or scaled armor that breastplate should be coded as present because this is the most common location for armor. however, in theory, it is possible to have armor that doesn't protect the torso (for example, a culture might use armor that protects the limbs only).",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "breastplate": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of breastplate for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class BreastplateListAllView(ListView):
    """ """

    model = Breastplate
    template_name = "wf/breastplate/breastplate_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Breastplate",
                "var_main_desc": "The absence or presence of breastplates as a military technology used in warfare. armor made from wood, horn, or bone can be very important (as in the spread of the asian war complex into north america). leather and cotton (in the americas) armor was also effective against arrows and warclubs. breastplate refers to any form of torso protection (in fact, we might rename this variable 'torso protection' at a later date). in the vast majority of cases you will probably find that if a culture has wooden armor, leather armor, chainmail armor, or scaled armor that breastplate should be coded as present because this is the most common location for armor. however, in theory, it is possible to have armor that doesn't protect the torso (for example, a culture might use armor that protects the limbs only).",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "breastplate": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of breastplate for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class BreastplateDetailView(DetailView):
    """ """

    model = Breastplate
    template_name = "wf/breastplate/breastplate_detail.html"


class Limb_protectionCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Limb_protection
    form_class = Limb_protectionForm
    template_name = "wf/limb_protection/limb_protection_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("limb_protection-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Limb Protection"
        context["my_exp"] = (
            "The absence or presence of limb protection as a military technology used in warfare. E.g., greaves. Covering arms, or legs, or both."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Limb_protectionUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Limb Protection",
                "my_exp": "The absence or presence of limb protection as a military technology used in warfare. E.g., greaves. Covering arms, or legs, or both.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Limb_protectionDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Limb_protection
    success_url = reverse_lazy("limb_protections")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Limb_protectionListView(ListView):
    """ """

    model = Limb_protection
    template_name = "wf/limb_protection/limb_protection_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("limb_protections")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Limb Protection",
                "var_main_desc": "The absence or presence of limb protection as a military technology used in warfare. e.g., greaves. covering arms, or legs, or both.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "limb_protection": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of limb protection for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Limb_protectionListAllView(ListView):
    """ """

    model = Limb_protection
    template_name = "wf/limb_protection/limb_protection_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Limb Protection",
                "var_main_desc": "The absence or presence of limb protection as a military technology used in warfare. e.g., greaves. covering arms, or legs, or both.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "limb_protection": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of limb protection for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Limb_protectionDetailView(DetailView):
    """ """

    model = Limb_protection
    template_name = "wf/limb_protection/limb_protection_detail.html"


class Scaled_armorCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Scaled_armor
    form_class = Scaled_armorForm
    template_name = "wf/scaled_armor/scaled_armor_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scaled_armor-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Scaled Armor"
        context["my_exp"] = (
            "The absence or presence of scaled armor as a military technology used in warfare. Armor consisting of many individual small armor scales (plates) attached to a backing of cloth or leather. The scaled don't need to be metal (i.e. they could be particularly rigid bits of leather, horn, bone, etc)."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Scaled_armorUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Scaled Armor",
                "my_exp": "The absence or presence of scaled armor as a military technology used in warfare. Armor consisting of many individual small armor scales (plates) attached to a backing of cloth or leather. The scaled don't need to be metal (i.e. they could be particularly rigid bits of leather, horn, bone, etc).",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Scaled_armorDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Scaled_armor
    success_url = reverse_lazy("scaled_armors")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Scaled_armorListView(ListView):
    """ """

    model = Scaled_armor
    template_name = "wf/scaled_armor/scaled_armor_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("scaled_armors")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Scaled Armor",
                "var_main_desc": "The absence or presence of scaled armor as a military technology used in warfare. armor consisting of many individual small armor scales (plates) attached to a backing of cloth or leather. the scaled don't need to be metal (i.e. they could be particularly rigid bits of leather, horn, bone, etc).",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "scaled_armor": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of scaled armor for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Scaled_armorListAllView(ListView):
    """ """

    model = Scaled_armor
    template_name = "wf/scaled_armor/scaled_armor_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Scaled Armor",
                "var_main_desc": "The absence or presence of scaled armor as a military technology used in warfare. armor consisting of many individual small armor scales (plates) attached to a backing of cloth or leather. the scaled don't need to be metal (i.e. they could be particularly rigid bits of leather, horn, bone, etc).",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "scaled_armor": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of scaled armor for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Scaled_armorDetailView(DetailView):
    """ """

    model = Scaled_armor
    template_name = "wf/scaled_armor/scaled_armor_detail.html"


class Laminar_armorCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Laminar_armor
    form_class = Laminar_armorForm
    template_name = "wf/laminar_armor/laminar_armor_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("laminar_armor-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Laminar Armor"
        context["my_exp"] = (
            "The absence or presence of laminar armor as a military technology used in warfare. (also known as banded mail, example: lorica segmentata). Armor that is made from horizontal overlapping rows or bands of sold armor plates."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Laminar_armorUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Laminar Armor",
                "my_exp": "The absence or presence of laminar armor as a military technology used in warfare. (also known as banded mail, example: lorica segmentata). Armor that is made from horizontal overlapping rows or bands of sold armor plates.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Laminar_armorDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Laminar_armor
    success_url = reverse_lazy("laminar_armors")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Laminar_armorListView(ListView):
    """ """

    model = Laminar_armor
    template_name = "wf/laminar_armor/laminar_armor_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("laminar_armors")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Laminar Armor",
                "var_main_desc": "The absence or presence of laminar armor as a military technology used in warfare. (also known as banded mail, example: lorica segmentata). armor that is made from horizontal overlapping rows or bands of sold armor plates.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "laminar_armor": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of laminar armor for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Laminar_armorListAllView(ListView):
    """ """

    model = Laminar_armor
    template_name = "wf/laminar_armor/laminar_armor_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Laminar Armor",
                "var_main_desc": "The absence or presence of laminar armor as a military technology used in warfare. (also known as banded mail, example: lorica segmentata). armor that is made from horizontal overlapping rows or bands of sold armor plates.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "laminar_armor": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of laminar armor for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Laminar_armorDetailView(DetailView):
    """ """

    model = Laminar_armor
    template_name = "wf/laminar_armor/laminar_armor_detail.html"


class Plate_armorCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Plate_armor
    form_class = Plate_armorForm
    template_name = "wf/plate_armor/plate_armor_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("plate_armor-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Plate Armor"
        context["my_exp"] = (
            "The absence or presence of plate armor as a military technology used in warfare. Armor made of iron or steel plates."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Plate_armorUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Plate Armor",
                "my_exp": "The absence or presence of plate armor as a military technology used in warfare. Armor made of iron or steel plates.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Plate_armorDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Plate_armor
    success_url = reverse_lazy("plate_armors")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Plate_armorListView(ListView):
    """ """

    model = Plate_armor
    template_name = "wf/plate_armor/plate_armor_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("plate_armors")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Plate Armor",
                "var_main_desc": "The absence or presence of plate armor as a military technology used in warfare. armor made of iron or steel plates.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "plate_armor": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of plate armor for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Plate_armorListAllView(ListView):
    """ """

    model = Plate_armor
    template_name = "wf/plate_armor/plate_armor_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Plate Armor",
                "var_main_desc": "The absence or presence of plate armor as a military technology used in warfare. armor made of iron or steel plates.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "plate_armor": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of plate armor for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Plate_armorDetailView(DetailView):
    """ """

    model = Plate_armor
    template_name = "wf/plate_armor/plate_armor_detail.html"


class Small_vessels_canoes_etcCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Small_vessels_canoes_etc
    form_class = Small_vessels_canoes_etcForm
    template_name = (
        "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("small_vessels_canoes_etc-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Small Vessels Canoes Etc"
        context["my_exp"] = (
            "The absence or presence of small vessels, canoes, etc. as a military technology used in warfare. "  # noqa: E501 pylint: disable=C0301
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "small_vessels_canoes_etc": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of small vessels canoes etc for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Small_vessels_canoes_etcUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Small_vessels_canoes_etc
    form_class = Small_vessels_canoes_etcForm
    template_name = (
        "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_update.html"
    )
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Small Vessels Canoes Etc",
                "my_exp": "The absence or presence of small vessels, canoes, etc. as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Small_vessels_canoes_etcDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Small_vessels_canoes_etc
    success_url = reverse_lazy("small_vessels_canoes_etcs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Small_vessels_canoes_etcListView(ListView):
    """ """

    model = Small_vessels_canoes_etc
    template_name = (
        "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("small_vessels_canoes_etcs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Small Vessels Canoes Etc",
                "var_main_desc": "The absence or presence of small vessels, canoes, etc. as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Naval technology",
                "inner_vars": {
                    "small_vessels_canoes_etc": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of small vessels canoes etc for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Small_vessels_canoes_etcListAllView(ListView):
    """ """

    model = Small_vessels_canoes_etc
    template_name = (
        "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_list_all.html"
    )

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Small Vessels Canoes Etc",
                "var_main_desc": "The absence or presence of small vessels, canoes, etc. as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Naval technology",
                "inner_vars": {
                    "small_vessels_canoes_etc": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of small vessels canoes etc for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Small_vessels_canoes_etcDetailView(DetailView):
    """ """

    model = Small_vessels_canoes_etc
    template_name = (
        "wf/small_vessels_canoes_etc/small_vessels_canoes_etc_detail.html"
    )


class Merchant_ships_pressed_into_serviceCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Merchant_ships_pressed_into_service
    form_class = Merchant_ships_pressed_into_serviceForm
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("merchant_ships_pressed_into_service-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Merchant Ships Pressed Into Service"
        context["my_exp"] = (
            "The absence or presence of merchant ships pressed into service as a military technology used in warfare."  # noqa: E501 pylint: disable=C0301
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "merchant_ships_pressed_into_service": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of merchant ships pressed into service for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Merchant_ships_pressed_into_serviceUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Merchant_ships_pressed_into_service
    form_class = Merchant_ships_pressed_into_serviceForm
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Merchant Ships Pressed Into Service",
                "my_exp": "The absence or presence of merchant ships pressed into service as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Merchant_ships_pressed_into_serviceDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Merchant_ships_pressed_into_service
    success_url = reverse_lazy("merchant_ships_pressed_into_services")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Merchant_ships_pressed_into_serviceListView(ListView):
    """ """

    model = Merchant_ships_pressed_into_service
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("merchant_ships_pressed_into_services")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Merchant Ships Pressed Into Service",
                "var_main_desc": "The absence or presence of merchant ships pressed into service as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Naval technology",
                "inner_vars": {
                    "merchant_ships_pressed_into_service": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of merchant ships pressed into service for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Merchant_ships_pressed_into_serviceListAllView(ListView):
    """ """

    model = Merchant_ships_pressed_into_service
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Merchant Ships Pressed Into Service",
                "var_main_desc": "The absence or presence of merchant ships pressed into service as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Naval technology",
                "inner_vars": {
                    "merchant_ships_pressed_into_service": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of merchant ships pressed into service for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Merchant_ships_pressed_into_serviceDetailView(DetailView):
    """ """

    model = Merchant_ships_pressed_into_service
    template_name = "wf/merchant_ships_pressed_into_service/merchant_ships_pressed_into_service_detail.html"  # noqa: E501 pylint: disable=C0301


class Specialized_military_vesselCreateView(
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

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("specialized_military_vessel-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Specialized Military Vessel"
        context["my_exp"] = (
            "The absence or presence of specialized military vessels as a military technology used in warfare. (such as galleys and sailing ships)"  # noqa: E501 pylint: disable=C0301
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "specialized_military_vessel": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of specialized military vessel for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Specialized_military_vesselUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Specialized_military_vessel
    form_class = Specialized_military_vesselForm
    template_name = "wf/specialized_military_vessel/specialized_military_vessel_update.html"
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Specialized Military Vessel",
                "my_exp": "The absence or presence of specialized military vessels as a military technology used in warfare. (such as galleys and sailing ships)",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Specialized_military_vesselDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Specialized_military_vessel
    success_url = reverse_lazy("specialized_military_vessels")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Specialized_military_vesselListView(ListView):
    """ """

    model = Specialized_military_vessel
    template_name = (
        "wf/specialized_military_vessel/specialized_military_vessel_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("specialized_military_vessels")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Specialized Military Vessel",
                "var_main_desc": "The absence or presence of specialized military vessels as a military technology used in warfare. (such as galleys and sailing ships)",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Naval technology",
                "inner_vars": {
                    "specialized_military_vessel": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of specialized military vessel for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Specialized_military_vesselListAllView(ListView):
    """ """

    model = Specialized_military_vessel
    template_name = "wf/specialized_military_vessel/specialized_military_vessel_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Specialized Military Vessel",
                "var_main_desc": "The absence or presence of specialized military vessels as a military technology used in warfare. (such as galleys and sailing ships)",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Naval technology",
                "inner_vars": {
                    "specialized_military_vessel": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of specialized military vessel for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Specialized_military_vesselDetailView(DetailView):
    """ """

    model = Specialized_military_vessel
    template_name = "wf/specialized_military_vessel/specialized_military_vessel_detail.html"


class Settlements_in_a_defensive_positionCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Settlements_in_a_defensive_position
    form_class = Settlements_in_a_defensive_positionForm
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_form.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("settlements_in_a_defensive_position-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Settlements in a Defensive Position"
        context["my_exp"] = (
            "The absence or presence of settlements in a defensive position as a military technology used in warfare. Settlements in a location that was clearly chosen for defensive reasons. E.g. on a hill top, peninsula."  # noqa: E501 pylint: disable=C0301
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "settlements_in_a_defensive_position": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of settlements in a defensive position for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Settlements_in_a_defensive_positionUpdateView(
    PermissionRequiredMixin, UpdateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Settlements_in_a_defensive_position
    form_class = Settlements_in_a_defensive_positionForm
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_update.html"  # noqa: E501 pylint: disable=C0301
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Settlements in a Defensive Position",
                "my_exp": "The absence or presence of settlements in a defensive position as a military technology used in warfare. Settlements in a location that was clearly chosen for defensive reasons. E.g. on a hill top, peninsula.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Settlements_in_a_defensive_positionDeleteView(
    PermissionRequiredMixin, DeleteView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Settlements_in_a_defensive_position
    success_url = reverse_lazy("settlements_in_a_defensive_positions")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Settlements_in_a_defensive_positionListView(ListView):
    """ """

    model = Settlements_in_a_defensive_position
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_list.html"  # noqa: E501 pylint: disable=C0301
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("settlements_in_a_defensive_positions")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Settlements in a Defensive Position",
                "var_main_desc": "The absence or presence of settlements in a defensive position as a military technology used in warfare. settlements in a location that was clearly chosen for defensive reasons. e.g. on a hill top, peninsula.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "settlements_in_a_defensive_position": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of settlements in a defensive position for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Settlements_in_a_defensive_positionListAllView(ListView):
    """ """

    model = Settlements_in_a_defensive_position
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_list_all.html"  # noqa: E501 pylint: disable=C0301

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Settlements in a Defensive Position",
                "var_main_desc": "The absence or presence of settlements in a defensive position as a military technology used in warfare. settlements in a location that was clearly chosen for defensive reasons. e.g. on a hill top, peninsula.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "settlements_in_a_defensive_position": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of settlements in a defensive position for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Settlements_in_a_defensive_positionDetailView(DetailView):
    """ """

    model = Settlements_in_a_defensive_position
    template_name = "wf/settlements_in_a_defensive_position/settlements_in_a_defensive_position_detail.html"  # noqa: E501 pylint: disable=C0301


class Wooden_palisadeCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wooden_palisade
    form_class = Wooden_palisadeForm
    template_name = "wf/wooden_palisade/wooden_palisade_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wooden_palisade-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Wooden Palisade"
        context["my_exp"] = (
            "The absence or presence of wooden palisades as a military technology used in warfare."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Wooden_palisadeUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Wooden Palisade",
                "my_exp": "The absence or presence of wooden palisades as a military technology used in warfare. ",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Wooden_palisadeDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Wooden_palisade
    success_url = reverse_lazy("wooden_palisades")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Wooden_palisadeListView(ListView):
    """ """

    model = Wooden_palisade
    template_name = "wf/wooden_palisade/wooden_palisade_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("wooden_palisades")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Wooden Palisade",
                "var_main_desc": "The absence or presence of wooden palisades as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "wooden_palisade": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of wooden palisade for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Wooden_palisadeListAllView(ListView):
    """ """

    model = Wooden_palisade
    template_name = "wf/wooden_palisade/wooden_palisade_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Wooden Palisade",
                "var_main_desc": "The absence or presence of wooden palisades as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "wooden_palisade": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of wooden palisade for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Wooden_palisadeDetailView(DetailView):
    """ """

    model = Wooden_palisade
    template_name = "wf/wooden_palisade/wooden_palisade_detail.html"


class Earth_rampartCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Earth_rampart
    form_class = Earth_rampartForm
    template_name = "wf/earth_rampart/earth_rampart_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("earth_rampart-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Earth Rampart"
        context["my_exp"] = (
            "The absence or presence of earth ramparts as a military technology used in warfare. "  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Earth_rampartUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Earth Rampart",
                "my_exp": "The absence or presence of earth ramparts as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Earth_rampartDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Earth_rampart
    success_url = reverse_lazy("earth_ramparts")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Earth_rampartListView(ListView):
    """ """

    model = Earth_rampart
    template_name = "wf/earth_rampart/earth_rampart_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("earth_ramparts")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Earth Rampart",
                "var_main_desc": "The absence or presence of earth ramparts as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "earth_rampart": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of earth rampart for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Earth_rampartListAllView(ListView):
    """ """

    model = Earth_rampart
    template_name = "wf/earth_rampart/earth_rampart_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Earth Rampart",
                "var_main_desc": "The absence or presence of earth ramparts as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "earth_rampart": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of earth rampart for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Earth_rampartDetailView(DetailView):
    """ """

    model = Earth_rampart
    template_name = "wf/earth_rampart/earth_rampart_detail.html"


class DitchCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Ditch
    form_class = DitchForm
    template_name = "wf/ditch/ditch_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("ditch-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class DitchUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Ditch",
                "my_exp": "The absence or presence of ditch as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class DitchDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Ditch
    success_url = reverse_lazy("ditchs")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class DitchListView(ListView):
    """ """

    model = Ditch
    template_name = "wf/ditch/ditch_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("ditchs")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Ditch",
                "var_main_desc": "The absence or presence of ditch as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "ditch": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of ditch for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class DitchListAllView(ListView):
    """ """

    model = Ditch
    template_name = "wf/ditch/ditch_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Ditch",
                "var_main_desc": "The absence or presence of ditch as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "ditch": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of ditch for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class DitchDetailView(DetailView):
    """ """

    model = Ditch
    template_name = "wf/ditch/ditch_detail.html"


class MoatCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Moat
    form_class = MoatForm
    template_name = "wf/moat/moat_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("moat-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Moat"
        context["my_exp"] = (
            "The absence or presence of moat as a military technology used in warfare. Differs from a ditch in that it has water"  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class MoatUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Moat",
                "my_exp": "The absence or presence of moat as a military technology used in warfare. Differs from a ditch in that it has water",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class MoatDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Moat
    success_url = reverse_lazy("moats")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class MoatListView(ListView):
    """ """

    model = Moat
    template_name = "wf/moat/moat_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("moats")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Moat",
                "var_main_desc": "The absence or presence of moat as a military technology used in warfare. differs from a ditch in that it has water",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "moat": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of moat for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class MoatListAllView(ListView):
    """ """

    model = Moat
    template_name = "wf/moat/moat_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Moat",
                "var_main_desc": "The absence or presence of moat as a military technology used in warfare. differs from a ditch in that it has water",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "moat": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of moat for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class MoatDetailView(DetailView):
    """ """

    model = Moat
    template_name = "wf/moat/moat_detail.html"


class Stone_walls_non_mortaredCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_non_mortared
    form_class = Stone_walls_non_mortaredForm
    template_name = (
        "wf/stone_walls_non_mortared/stone_walls_non_mortared_form.html"
    )
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_non_mortared-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Stone Walls Non Mortared"
        context["my_exp"] = (
            "The absence or presence of stone walls (non-mortared) as a military technology used in warfare. "  # noqa: E501 pylint: disable=C0301
        )
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {
            "stone_walls_non_mortared": {
                "min": None,
                "max": None,
                "scale": None,
                "var_exp_source": None,
                "var_exp": "The absence or presence of stone walls non mortared for a polity.",  # noqa: E501 pylint: disable=C0301
                "units": None,
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Stone_walls_non_mortaredUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_non_mortared
    form_class = Stone_walls_non_mortaredForm
    template_name = (
        "wf/stone_walls_non_mortared/stone_walls_non_mortared_update.html"
    )
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Stone Walls Non Mortared",
                "my_exp": "The absence or presence of stone walls (non-mortared) as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Stone_walls_non_mortaredDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_non_mortared
    success_url = reverse_lazy("stone_walls_non_mortareds")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Stone_walls_non_mortaredListView(ListView):
    """ """

    model = Stone_walls_non_mortared
    template_name = (
        "wf/stone_walls_non_mortared/stone_walls_non_mortared_list.html"
    )
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_non_mortareds")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Stone Walls Non Mortared",
                "var_main_desc": "The absence or presence of stone walls (non-mortared) as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "stone_walls_non_mortared": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of stone walls non mortared for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Stone_walls_non_mortaredListAllView(ListView):
    """ """

    model = Stone_walls_non_mortared
    template_name = (
        "wf/stone_walls_non_mortared/stone_walls_non_mortared_list_all.html"
    )

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Stone Walls Non Mortared",
                "var_main_desc": "The absence or presence of stone walls (non-mortared) as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "stone_walls_non_mortared": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of stone walls non mortared for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Stone_walls_non_mortaredDetailView(DetailView):
    """ """

    model = Stone_walls_non_mortared
    template_name = (
        "wf/stone_walls_non_mortared/stone_walls_non_mortared_detail.html"
    )


class Stone_walls_mortaredCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_mortared
    form_class = Stone_walls_mortaredForm
    template_name = "wf/stone_walls_mortared/stone_walls_mortared_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_mortared-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Stone Walls Mortared"
        context["my_exp"] = (
            "The absence or presence of stone walls (mortared) as a military technology used in warfare. "  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Stone_walls_mortaredUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Stone Walls Mortared",
                "my_exp": "The absence or presence of stone walls (mortared) as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Stone_walls_mortaredDeleteView(PermissionRequiredMixin, DeleteView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Stone_walls_mortared
    success_url = reverse_lazy("stone_walls_mortareds")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Stone_walls_mortaredListView(ListView):
    """ """

    model = Stone_walls_mortared
    template_name = "wf/stone_walls_mortared/stone_walls_mortared_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("stone_walls_mortareds")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Stone Walls Mortared",
                "var_main_desc": "The absence or presence of stone walls (mortared) as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "stone_walls_mortared": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of stone walls mortared for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Stone_walls_mortaredListAllView(ListView):
    """ """

    model = Stone_walls_mortared
    template_name = (
        "wf/stone_walls_mortared/stone_walls_mortared_list_all.html"
    )

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Stone Walls Mortared",
                "var_main_desc": "The absence or presence of stone walls (mortared) as a military technology used in warfare.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "stone_walls_mortared": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of stone walls mortared for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Stone_walls_mortaredDetailView(DetailView):
    """ """

    model = Stone_walls_mortared
    template_name = "wf/stone_walls_mortared/stone_walls_mortared_detail.html"


class Fortified_campCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Fortified_camp
    form_class = Fortified_campForm
    template_name = "wf/fortified_camp/fortified_camp_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("fortified_camp-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Fortified Camp"
        context["my_exp"] = (
            "The absence or presence of fortified camps as a military technology used in warfare. Camps made by armies on the move (e.g. on a campaign) that which could be constructed on a hill top or in the middle of a plain or desert, usually out of local materials."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Fortified_campUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Fortified Camp",
                "my_exp": "The absence or presence of fortified camps as a military technology used in warfare. Camps made by armies on the move (e.g. on a campaign) that which could be constructed on a hill top or in the middle of a plain or desert, usually out of local materials.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Fortified_campDeleteView(PermissionRequiredMixin, DeleteView):
    """ """

    model = Fortified_camp
    success_url = reverse_lazy("fortified_camps")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Fortified_campListView(ListView):
    """ """

    model = Fortified_camp
    template_name = "wf/fortified_camp/fortified_camp_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("fortified_camps")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Fortified Camp",
                "var_main_desc": "The absence or presence of fortified camps as a military technology used in warfare. camps made by armies on the move (e.g. on a campaign) that which could be constructed on a hill top or in the middle of a plain or desert, usually out of local materials.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "fortified_camp": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of fortified camp for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Fortified_campListAllView(ListView):
    """ """

    model = Fortified_camp
    template_name = "wf/fortified_camp/fortified_camp_list_all.html"

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Fortified Camp",
                "var_main_desc": "The absence or presence of fortified camps as a military technology used in warfare. camps made by armies on the move (e.g. on a campaign) that which could be constructed on a hill top or in the middle of a plain or desert, usually out of local materials.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "fortified_camp": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of fortified camp for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Fortified_campDetailView(DetailView):
    """ """

    model = Fortified_camp
    template_name = "wf/fortified_camp/fortified_camp_detail.html"


class Complex_fortificationCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """ """

    model = Complex_fortification
    form_class = Complex_fortificationForm
    template_name = "wf/complex_fortification/complex_fortification_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("complex_fortification-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Complex Fortification"
        context["my_exp"] = (
            "The absence or presence of complex fortifications as a military technology used in warfare. When there are two or more concentric walls. So simply a wall and a donjon, for example, is not enough."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Complex_fortificationUpdateView(PermissionRequiredMixin, UpdateView):
    """


    Note:
        This view is restricted to users with the 'add_capital' permission.
    """

    model = Complex_fortification
    form_class = Complex_fortificationForm
    template_name = (
        "wf/complex_fortification/complex_fortification_update.html"
    )
    permission_required = "core.add_capital"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Complex Fortification",
                "my_exp": "The absence or presence of complex fortifications as a military technology used in warfare. When there are two or more concentric walls. So simply a wall and a donjon, for example, is not enough.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Complex_fortificationDeleteView(PermissionRequiredMixin, DeleteView):
    """ """

    model = Complex_fortification
    success_url = reverse_lazy("complex_fortifications")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Complex_fortificationListView(ListView):
    """ """

    model = Complex_fortification
    template_name = "wf/complex_fortification/complex_fortification_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("complex_fortifications")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Complex Fortification",
                "var_main_desc": "The absence or presence of complex fortifications as a military technology used in warfare. when there are two or more concentric walls. so simply a wall and a donjon, for example, is not enough.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "complex_fortification": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of complex fortification for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Complex_fortificationListAllView(ListView):
    """ """

    model = Complex_fortification
    template_name = (
        "wf/complex_fortification/complex_fortification_list_all.html"
    )

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Complex Fortification",
                "var_main_desc": "The absence or presence of complex fortifications as a military technology used in warfare. when there are two or more concentric walls. so simply a wall and a donjon, for example, is not enough.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "complex_fortification": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of complex fortification for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Complex_fortificationDetailView(DetailView):
    """ """

    model = Complex_fortification
    template_name = (
        "wf/complex_fortification/complex_fortification_detail.html"
    )


class Modern_fortificationCreateView(
    PermissionRequiredMixin, PolityIdMixin, CreateView
):
    """ """

    model = Modern_fortification
    form_class = Modern_fortificationForm
    template_name = "wf/modern_fortification/modern_fortification_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("modern_fortification-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Modern Fortification"
        context["my_exp"] = (
            "The absence or presence of modern fortifications as a military technology used in warfare. used after the introduction of gunpowder, e.g., trace italienne/starfort."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class Modern_fortificationUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Modern Fortification",
                "my_exp": "The absence or presence of modern fortifications as a military technology used in warfare. used after the introduction of gunpowder, e.g., trace italienne/starfort.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class Modern_fortificationDeleteView(PermissionRequiredMixin, DeleteView):
    """ """

    model = Modern_fortification
    success_url = reverse_lazy("modern_fortifications")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class Modern_fortificationListView(ListView):
    """ """

    model = Modern_fortification
    template_name = "wf/modern_fortification/modern_fortification_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("modern_fortifications")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Modern Fortification",
                "var_main_desc": "The absence or presence of modern fortifications as a military technology used in warfare. used after the introduction of gunpowder, e.g., trace italienne/starfort.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "modern_fortification": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of modern fortification for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class Modern_fortificationListAllView(ListView):
    """ """

    model = Modern_fortification
    template_name = (
        "wf/modern_fortification/modern_fortification_list_all.html"
    )

    def get_absolute_url(self) -> str:
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
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return new_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Modern Fortification",
                "var_main_desc": "The absence or presence of modern fortifications as a military technology used in warfare. used after the introduction of gunpowder, e.g., trace italienne/starfort.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Fortifications",
                "inner_vars": {
                    "modern_fortification": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of modern fortification for a polity.",  # noqa: E501 pylint: disable=C0301
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class Modern_fortificationDetailView(DetailView):
    """ """

    model = Modern_fortification
    template_name = "wf/modern_fortification/modern_fortification_detail.html"


class ChainmailCreateView(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """ """

    model = Chainmail
    form_class = ChainmailForm
    template_name = "wf/chainmail/chainmail_form.html"
    permission_required = "core.add_capital"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("chainmail-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["myvar"] = "Chainmail"
        context["my_exp"] = (
            "The absence or presence of chainmail as a military technology used in warfare. We’re using a broad definition of chainmail. Habergeon was the word used to describe the Chinese version and that would qualify as chainmail. Armor that is made of small metal rings linked together in a pattern to form a mesh."  # noqa: E501 pylint: disable=C0301
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
                "choices": ABSENT_PRESENT_STRING_LIST,
                "null_meaning": None,
            }
        }
        context["potential_cols"] = ["Choices"]

        return context


class ChainmailUpdateView(PermissionRequiredMixin, UpdateView):
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

        context = dict(
            context,
            **{
                "myvar": "Chainmail",
                "my_exp": "The absence or presence of chainmail as a military technology used in warfare. We’re using a broad definition of chainmail. Habergeon was the word used to describe the Chinese version and that would qualify as chainmail. Armor that is made of small metal rings linked together in a pattern to form a mesh.",  # noqa: E501 pylint: disable=C0301
            },
        )

        return context


class ChainmailDeleteView(PermissionRequiredMixin, DeleteView):
    """ """

    model = Chainmail
    success_url = reverse_lazy("chainmails")
    template_name = "core/delete_general.html"
    permission_required = "core.add_capital"


class ChainmailListView(ListView):
    """ """

    model = Chainmail
    template_name = "wf/chainmail/chainmail_list.html"
    paginate_by = 10

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("chainmails")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Chainmail",
                "var_main_desc": "The absence or presence of chainmail as a military technology used in warfare. we’re using a broad definition of chainmail. habergeon was the word used to describe the chinese version and that would qualify as chainmail. armor that is made of small metal rings linked together in a pattern to form a mesh.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "chainmail": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of chainmail for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
            },
        )

        return context


class ChainmailListAllView(ListView):
    """ """

    model = Chainmail
    template_name = "wf/chainmail/chainmail_list_all.html"

    def get_absolute_url(self) -> str:
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse("chainmails_all")

    def get_queryset(self):
        order = self.request.GET.get("orderby", "home_nga")
        order2 = self.request.GET.get("orderby2", "year")

        queryset = (
            Chainmail.objects.all()
            .annotate(
                home_nga=POLITY_NGA_NAME,
                year=CORRECT_YEAR,
            )
            .order_by(order, order2)
        )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(
            context,
            **{
                "myvar": "Chainmail",
                "var_main_desc": "The absence or presence of chainmail as a military technology used in warfare. we’re using a broad definition of chainmail. habergeon was the word used to describe the chinese version and that would qualify as chainmail. armor that is made of small metal rings linked together in a pattern to form a mesh.",  # noqa: E501 pylint: disable=C0301
                "var_main_desc_source": "NOTHING",
                "var_section": "Warfare Variables",
                "var_subsection": "Armor",
                "inner_vars": {
                    "chainmail": {
                        "min": None,
                        "max": None,
                        "scale": None,
                        "var_exp_source": None,
                        "var_exp": "The absence or presence of chainmail for a polity.",
                        "units": None,
                        "choices": ABSENT_PRESENT_STRING_LIST,
                        "null_meaning": None,
                    }
                },
                "potential_cols": ["Choices"],
                "orderby": self.request.GET.get("orderby", "year_from"),
            },
        )

        return context


class ChainmailDetailView(DetailView):
    """ """

    model = Chainmail
    template_name = "wf/chainmail/chainmail_detail.html"
