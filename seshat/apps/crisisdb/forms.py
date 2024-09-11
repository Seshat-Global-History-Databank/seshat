from django import forms


from ..global_constants import (
    COMMON_FIELDS,
    COMMON_LABELS,
    COMMON_WIDGETS,
    ATTRS,
)

from .models import (
    Us_location,
    Us_violence_subtype,
    Us_violence_data_source,
    Us_violence,
    Power_transition,
    Crisis_consequence,
    Human_sacrifice,
    External_conflict,
    Internal_conflict,
    External_conflict_side,
    Agricultural_population,
    Arable_land,
    Arable_land_per_farmer,
    Gross_grain_shared_per_agricultural_population,
    Net_grain_shared_per_agricultural_population,
    Surplus,
    Military_expense,
    Silver_inflow,
    Silver_stock,
    Total_population,
    Gdp_per_capita,
    Drought_event,
    Locust_event,
    Socioeconomic_turmoil_event,
    Crop_failure_event,
    Famine_event,
    Disease_outbreak,
)


class Us_locationForm(forms.ModelForm):
    """
    Form for creating and updating a US location.
    """

    class Meta:
        """
        :noindex:
        """

        model = Us_location
        fields = "__all__"


class Us_violence_subtypeForm(forms.ModelForm):
    """
    Form for creating and updating a US violence subtype.
    """

    class Meta:
        """
        :noindex:
        """

        model = Us_violence_subtype
        fields = "__all__"


class Us_violence_data_sourceForm(forms.ModelForm):
    """
    Form for creating and updating a US violence data source.
    """

    class Meta:
        """
        :noindex:
        """

        model = Us_violence_data_source
        fields = "__all__"


class Us_violenceForm(forms.ModelForm):
    """
    Form for creating and updating a US violence.
    """

    class Meta:
        """
        :noindex:
        """

        model = Us_violence
        fields = [
            "violence_date",
            "violence_type",
            "violence_subtype",
            "fatalities",
            "location",
            "url_address",
            "short_data_source",
            "source_details",
            "narrative",
        ]
        widgets = {
            "violence_date": forms.DateInput(
                attrs=dict(ATTRS.MB3_ATTRS, **{"placeholder": "Ex: 2022-12-14"})
            ),
            "violence_type": forms.Select(attrs=ATTRS.MB3_ATTRS),
            "violence_subtype": forms.SelectMultiple(
                attrs={
                    "class": "form-control mb-3 js-states js-example-basic-multiple-violence-subtype",
                    "text": "violence_subtypes[]",
                    "style": "height: 340px",
                    "multiple": "multiple",
                }
            ),
            "fatalities": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            "location": forms.SelectMultiple(
                attrs={
                    "class": "form-control mb-3 js-states js-example-basic-multiple-location",
                    "text": "locations[]",
                    "style": "height: 340px",
                    "multiple": "multiple",
                }
            ),
            "url_address": forms.TextInput(
                attrs=dict(ATTRS.MB3_ATTRS, **{"placeholder": "Enter a URL"})
            ),
            "short_data_source": forms.SelectMultiple(
                attrs={
                    "class": "form-control mb-3 js-states js-example-basic-multiple-short-data-source",
                    "text": "short_data_sources[]",
                    "style": "height: 340px",
                    "multiple": "multiple",
                }
            ),
            "source_details": forms.Textarea(
                attrs=dict(
                    ATTRS.MB3_ATTRS,
                    **{
                        "placeholder": "Add source details (optional)",
                        "style": "height: 250px",
                    },
                )
            ),
            "narrative": forms.Textarea(
                attrs=dict(
                    ATTRS.MB3_ATTRS,
                    **{
                        "placeholder": "Add a narrative (optional)",
                        "style": "height: 250px",
                    },
                )
            ),
        }


class Crisis_consequenceForm(forms.ModelForm):
    """
    Form for creating and updating a crisis consequence.
    """

    class Meta:
        """
        :noindex:
        """

        model = Crisis_consequence

        fields = COMMON_FIELDS + [
            "crisis_case_id",
            "name",
            "other_polity",
            "is_first_100",
            "decline",
            "collapse",
            "epidemic",
            "downward_mobility",
            "extermination",
            "uprising",
            "revolution",
            "successful_revolution",
            "civil_war",
            "century_plus",
            "fragmentation",
            "fragmentation",
            "capital",
            "conquest",
            "assassination",
            "depose",
            "constitution",
            "labor",
            "unfree_labor",
            "suffrage",
            "public_goods",
            "religion",
        ]

        _class = "class='h5 text-teal'"
        _text = "class='text-primary text-decoration-underline'"
        labels = dict(
            COMMON_LABELS,
            **{
                "is_first_100": f"<span class='h5'> Is it a <span {_text}> first 100 </span> case? </span>",
                "polity": f"<span {_class}> Polity: </span>",
                "name": f"<span {_class}> Crisis Period Name: </span>",
                "other_polity": f"<span {_class}> Other Polity: </span>",
                "crisis_case_id": f"<span {_class}> Crisis Case Name (ID): </span>",
                "year_from": f"<span {_class}> Crisis Start Year: </span>",
                "year_to": f"<span {_class}> Crisis End Year: </span>",
                "decline": f"<span {_class}> Decline: </span>",
                "collapse": f"<span {_class}> Collapse: </span>",
                "epidemic": f"<span {_class}> Epidemic: </span>",
                "downward_mobility": f"<span {_class}> Downward mobility: </span>",
                "extermination": f"<span {_class}> Extermination: </span>",
                "uprising": f"<span {_class}> Uprising: </span>",
                "revolution": f"<span {_class}> Revolution: </span>",
                "successful_revolution": f"<span {_class}> Successful revolution: </span>",
                "civil_war": f"<span {_class}> Civil war: </span>",
                "century_plus": f"<span {_class}> Century plus: </span>",
                "fragmentation": f"<span {_class}> Fragmentation: </span>",
                "capital": f"<span {_class}> Capital: </span>",
                "conquest": f"<span {_class}> Conquest: </span>",
                "assassination": f"<span {_class}> Assassination: </span>",
                "depose": f"<span {_class}> Depose: </span>",
                "constitution": f"<span {_class}> Constitution: </span>",
                "labor": f"<span {_class}> Labor: </span>",
                "unfree_labor": f"<span {_class}> Unfree labor: </span>",
                "suffrage": f"<span {_class}> Suffrage: </span>",
                "public_goods": f"<span {_class}> Public goods: </span>",
                "religion": f"<span {_class}> Religion: </span>",
                "description": f"<span {_class}> Note: </span>",
            },
        )

        widgets = dict(
            COMMON_WIDGETS,
            **{
                "crisis_case_id": forms.TextInput(attrs=ATTRS.MB1_ATTRS),
                "name": forms.TextInput(attrs=ATTRS.MB1_ATTRS),
                "other_polity": forms.Select(
                    attrs={
                        "class": "form-control mb-1 js-example-basic-single2",
                        "id": "id_polity_other",
                    }
                ),
                "is_first_100": forms.CheckboxInput(attrs=ATTRS.MB3_SIMPLE_ATTRS),
                "decline": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "collapse": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "epidemic": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "downward_mobility": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "extermination": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "uprising": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "revolution": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "successful_revolution": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "civil_war": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "century_plus": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "fragmentation": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "capital": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "conquest": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "assassination": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "depose": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "constitution": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "labor": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "unfree_labor": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "suffrage": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "public_goods": forms.Select(attrs=ATTRS.MB1_ATTRS),
                "religion": forms.Select(attrs=ATTRS.MB1_ATTRS),
            },
        )


class Power_transitionForm(forms.ModelForm):
    """
    Form for creating and updating a power transition.
    """

    class Meta:
        """
        :noindex:
        """

        model = Power_transition

        fields = COMMON_FIELDS + [
            "predecessor",
            "successor",
            "name",
            "culture_group",
            "reign_number_predecessor",
            "contested",
            "overturn",
            "predecessor_assassination",
            "intra_elite",
            "military_revolt",
            "popular_uprising",
            "separatist_rebellion",
            "external_invasion",
            "external_interference",
        ]

        _class = "class='h6 text-teal'"
        labels = dict(
            COMMON_LABELS,
            **{
                "polity": f"<span {_class}> Polity: </span>",
                "name": f"<span {_class}> Conflict Name: </span>",
                "predecessor": f"<span {_class}> Predecessor: </span>",
                "successor": f"<span {_class}> Successor: </span>",
                "reign_number_predecessor": f"<span {_class}> Reign Number (predecessor): </span>",
                "culture_group": f"<span {_class}> Culture Group: </span>",
                "year_from": f"<span {_class}> Start Year (of Predecessor): </span>",
                "year_to": f"<span {_class}> End Year (Transition): </span>",
                "contested": f"<span {_class}> Contested: </span>",
                "overturn": f"<span {_class}> Overturn: </span>",
                "predecessor_assassination": f"<span {_class}> Predecessor_Assassination: </span>",
                "intra_elite": f"<span {_class}> Intra_Elite: </span>",
                "military_revolt": f"<span {_class}> Military_Revolt: </span>",
                "popular_uprising": f"<span {_class}> Popular_Uprising: </span>",
                "separatist_rebellion": f"<span {_class}> Separatist_Rebellion: </span>",
                "external_invasion": f"<span {_class}> External_Invasion: </span>",
                "external_interference": f"<span {_class}> External_Interference: </span>",
                "description": f"<span {_class}> Note: </span>",
            },
        )

        widgets = dict(
            COMMON_WIDGETS,
            **{
                "predecessor": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
                "successor": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
                "reign_number_predecessor": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "culture_group": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
                "name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
                "contested": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "overturn": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "predecessor_assassination": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "intra_elite": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "military_revolt": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "popular_uprising": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "separatist_rebellion": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "external_invasion": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "external_interference": forms.Select(attrs=ATTRS.MB3_ATTRS),
            },
        )


class Human_sacrificeForm(forms.ModelForm):
    """
    Form for creating and updating a human sacrifice.
    """

    class Meta:
        """
        :noindex:
        """

        model = Human_sacrifice

        fields = COMMON_FIELDS + ["human_sacrifice"]

        labels = COMMON_LABELS.copy()

        widgets = dict(
            COMMON_WIDGETS,
            **{
                "sub_category": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "human_sacrifice": forms.Select(attrs=ATTRS.MB3_ATTRS),
            },
        )


class External_conflictForm(forms.ModelForm):
    """
    Form for creating and updating an external conflict.
    """

    class Meta:
        """
        :noindex:
        """

        model = External_conflict

        fields = COMMON_FIELDS + ["conflict_name"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"conflict_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Internal_conflictForm(forms.ModelForm):
    """
    Form for creating and updating an internal conflict.
    """

    class Meta:
        """
        :noindex:
        """

        model = Internal_conflict

        fields = COMMON_FIELDS + [
            "conflict",
            "expenditure",
            "leader",
            "casualty",
        ]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{
                "conflict": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
                "expenditure": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "leader": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
                "casualty": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            },
        )


class External_conflict_sideForm(forms.ModelForm):
    """
    Side form for creating and updating an external conflict.
    """

    class Meta:
        """
        :noindex:
        """

        model = External_conflict_side

        fields = COMMON_FIELDS + [
            "conflict_id",
            "expenditure",
            "leader",
            "casualty",
        ]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{
                "conflict_id": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "expenditure": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "leader": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
                "casualty": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            },
        )


class Agricultural_populationForm(forms.ModelForm):
    """
    Form for creating and updating an agricultural population.
    """

    class Meta:
        """
        :noindex:
        """

        model = Agricultural_population

        fields = COMMON_FIELDS + ["agricultural_population"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"agricultural_population": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Arable_landForm(forms.ModelForm):
    """
    Form for creating and updating an arable land.
    """

    class Meta:
        """
        :noindex:
        """

        model = Arable_land

        fields = COMMON_FIELDS + ["arable_land"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"arable_land": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Arable_land_per_farmerForm(forms.ModelForm):
    """
    Form for creating and updating an arable land per farmer.
    """

    class Meta:
        """
        :noindex:
        """

        model = Arable_land_per_farmer

        fields = COMMON_FIELDS + ["arable_land_per_farmer"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"arable_land_per_farmer": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Gross_grain_shared_per_agricultural_populationForm(forms.ModelForm):
    """
    Form for creating and updating a gross grain shared per agricultural population.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gross_grain_shared_per_agricultural_population

        fields = COMMON_FIELDS + ["gross_grain_shared_per_agricultural_population"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{
                "gross_grain_shared_per_agricultural_population": (
                    forms.NumberInput(attrs=ATTRS.MB3_ATTRS)
                )
            },
        )


class Net_grain_shared_per_agricultural_populationForm(forms.ModelForm):
    """
    Form for creating and updating a net grain shared per agricultural population.
    """

    class Meta:
        """
        :noindex:
        """

        model = Net_grain_shared_per_agricultural_population

        fields = COMMON_FIELDS + ["net_grain_shared_per_agricultural_population"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{
                "net_grain_shared_per_agricultural_population": (
                    forms.NumberInput(attrs=ATTRS.MB3_ATTRS)
                )
            },
        )


class SurplusForm(forms.ModelForm):
    """
    Form for creating and updating a surplus.
    """

    class Meta:
        """
        :noindex:
        """

        model = Surplus

        fields = COMMON_FIELDS + ["surplus"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"surplus": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Military_expenseForm(forms.ModelForm):
    """
    Form for creating and updating a military expense.
    """

    class Meta:
        """
        :noindex:
        """

        model = Military_expense

        fields = COMMON_FIELDS + ["conflict", "expenditure"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{
                "conflict": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
                "expenditure": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            },
        )


class Silver_inflowForm(forms.ModelForm):
    """
    Form for creating and updating a silver inflow.
    """

    class Meta:
        """
        :noindex:
        """

        model = Silver_inflow

        fields = COMMON_FIELDS + ["silver_inflow"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"silver_inflow": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Silver_stockForm(forms.ModelForm):
    """
    Form for creating and updating a silver stock.
    """

    class Meta:
        """
        :noindex:
        """

        model = Silver_stock

        fields = COMMON_FIELDS + ["silver_stock"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"silver_stock": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Total_populationForm(forms.ModelForm):
    """
    Form for creating and updating a total population.
    """

    class Meta:
        """
        :noindex:
        """

        model = Total_population

        fields = COMMON_FIELDS + ["total_population"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"total_population": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Gdp_per_capitaForm(forms.ModelForm):
    """
    Form for creating and updating a GDP per capita.
    """

    class Meta:
        """
        :noindex:
        """

        model = Gdp_per_capita

        fields = COMMON_FIELDS + ["gdp_per_capita"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"gdp_per_capita": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Drought_eventForm(forms.ModelForm):
    """
    Form for creating and updating a drought event.
    """

    class Meta:
        """
        :noindex:
        """

        model = Drought_event

        fields = COMMON_FIELDS + ["drought_event"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"drought_event": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Locust_eventForm(forms.ModelForm):
    """
    Form for creating and updating a locust event.
    """

    class Meta:
        """
        :noindex:
        """

        model = Locust_event

        fields = COMMON_FIELDS + ["locust_event"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"locust_event": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Socioeconomic_turmoil_eventForm(forms.ModelForm):
    """
    Form for creating and updating a socioeconomic turmoil event.
    """

    class Meta:
        """
        :noindex:
        """

        model = Socioeconomic_turmoil_event

        fields = COMMON_FIELDS + ["socioeconomic_turmoil_event"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"socioeconomic_turmoil_event": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Crop_failure_eventForm(forms.ModelForm):
    """
    Form for creating and updating a crop failure event.
    """

    class Meta:
        """
        :noindex:
        """

        model = Crop_failure_event

        fields = COMMON_FIELDS + ["crop_failure_event"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"crop_failure_event": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Famine_eventForm(forms.ModelForm):
    """
    Form for creating and updating a famine event.
    """

    class Meta:
        """
        :noindex:
        """

        model = Famine_event

        fields = COMMON_FIELDS + ["famine_event"]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{"famine_event": forms.NumberInput(attrs=ATTRS.MB3_ATTRS)},
        )


class Disease_outbreakForm(forms.ModelForm):
    """
    Form for creating and updating a disease outbreak.
    """

    class Meta:
        """
        :noindex:
        """

        model = Disease_outbreak

        fields = COMMON_FIELDS + [
            "longitude",
            "latitude",
            "elevation",
            "sub_category",
            "magnitude",
            "duration",
        ]

        labels = COMMON_LABELS

        widgets = dict(
            COMMON_WIDGETS,
            **{
                "longitude": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "latitude": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "elevation": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "sub_category": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "magnitude": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "duration": forms.Select(attrs=ATTRS.MB3_ATTRS),
            },
        )
