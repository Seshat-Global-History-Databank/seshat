from django import forms

from ..constants import (
    COMMON_FIELDS,
    COMMON_LABELS,
    COMMON_WIDGETS,
    ATTRS,
)

from .models import (
    Polity_research_assistant,
    Polity_utm_zone,
    Polity_original_name,
    Polity_alternative_name,
    Polity_peak_years,
    Polity_duration,
    Polity_degree_of_centralization,
    Polity_suprapolity_relations,
    Polity_capital,
    Polity_language,
    Polity_linguistic_family,
    Polity_language_genus,
    Polity_religion_genus,
    Polity_religion_family,
    Polity_religion,
    Polity_relationship_to_preceding_entity,
    Polity_preceding_entity,
    Polity_succeeding_entity,
    Polity_supracultural_entity,
    Polity_scale_of_supracultural_interaction,
    Polity_alternate_religion_genus,
    Polity_alternate_religion_family,
    Polity_alternate_religion,
    Polity_expert,
    Polity_editor,
    Polity_religious_tradition,
)


class Polity_research_assistantForm(forms.ModelForm):
    """
    Form for creating and updating Polity_research_assistant model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_research_assistant
        fields = COMMON_FIELDS + ["polity_ra"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"polity_ra": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_utm_zoneForm(forms.ModelForm):
    """
    Form for creating and updating Polity_utm_zone model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_utm_zone
        fields = COMMON_FIELDS + ["utm_zone"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"utm_zone": forms.TextInput(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_original_nameForm(forms.ModelForm):
    """
    Form for creating and updating Polity_original_name model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_original_name
        fields = COMMON_FIELDS + ["original_name"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"original_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_alternative_nameForm(forms.ModelForm):
    """
    Form for creating and updating Polity_alternative_name model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_alternative_name
        fields = COMMON_FIELDS + ["alternative_name"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"alternative_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_peak_yearsForm(forms.ModelForm):
    """
    Form for creating and updating Polity_peak_years model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_peak_years
        fields = COMMON_FIELDS + ["peak_year_from", "peak_year_to"]
        labels = dict(
            COMMON_LABELS,
            **{
                "peak_year_from": "Peak Year (Start)",
                "peak_year_to": "Peak Year (End)",
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "peak_year_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "peak_year_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Polity_durationForm(forms.ModelForm):
    """
    Form for creating and updating Polity_duration model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_duration
        fields = COMMON_FIELDS + ["polity_year_from", "polity_year_to"]
        labels = dict(
            COMMON_LABELS,
            **{
                "polity_year_from": "Polity Start Year",
                "polity_year_to": "Polity End Year",
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "polity_year_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "polity_year_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Polity_degree_of_centralizationForm(forms.ModelForm):
    """
    Form for creating and updating Polity_degree_of_centralization model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_degree_of_centralization
        fields = COMMON_FIELDS + ["degree_of_centralization"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"degree_of_centralization": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_suprapolity_relationsForm(forms.ModelForm):
    """
    Form for creating and updating Polity_suprapolity_relations model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_suprapolity_relations
        fields = COMMON_FIELDS + ["supra_polity_relations", "other_polity"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "supra_polity_relations": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "other_polity": forms.Select(
                    attrs={
                        "class": "form-control mb-4 pb-4 js-example-basic-single",
                        "id": "id_other_polity",
                        "name": "other_polity",
                    }
                ),
            }
        )


class Polity_capitalForm(forms.ModelForm):
    """
    Form for creating and updating Polity_capital model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_capital
        fields = COMMON_FIELDS + ["capital", "polity_cap"]
        labels = dict(
            COMMON_LABELS,
            **{
                "capital": "Coded Capital (Obsolete)",
                "polity_cap": "Polity Capital",
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "capital": forms.TextInput(
                    attrs=dict(
                        ATTRS.MB3_ATTRS,
                        **{
                            "readonly": "True",
                        }
                    )
                ),
                "polity_cap": forms.Select(
                    attrs={
                        "class": "form-control mb-1 js-example-basic-single",
                        "id": "id_polity_cap",
                        "name": "polity_cap",
                    }
                ),
            }
        )


class Polity_languageForm(forms.ModelForm):
    """
    Form for creating and updating Polity_language model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_language
        fields = COMMON_FIELDS + ["language"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"language": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_linguistic_familyForm(forms.ModelForm):
    """
    Form for creating and updating Polity_linguistic_family model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_linguistic_family
        fields = COMMON_FIELDS + ["linguistic_family"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"linguistic_family": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_language_genusForm(forms.ModelForm):
    """
    Form for creating and updating Polity_language_genus model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_language_genus
        fields = COMMON_FIELDS + ["language_genus"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"language_genus": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_religion_genusForm(forms.ModelForm):
    """
    Form for creating and updating Polity_religion_genus model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_religion_genus
        fields = COMMON_FIELDS + ["religion_genus"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"religion_genus": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_religion_familyForm(forms.ModelForm):
    """
    Form for creating and updating Polity_religion_family model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_religion_family
        fields = COMMON_FIELDS + ["religion_family"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"religion_family": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_religionForm(forms.ModelForm):
    """
    Form for creating and updating Polity_religion model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_religion
        fields = COMMON_FIELDS + ["religion"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"religion": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_relationship_to_preceding_entityForm(forms.ModelForm):
    """
    Form for creating and updating Polity_relationship_to_preceding_entity model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_relationship_to_preceding_entity
        fields = COMMON_FIELDS + ["relationship_to_preceding_entity"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"relationship_to_preceding_entity": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_preceding_entityForm(forms.ModelForm):
    """
    Form for creating and updating Polity_preceding_entity model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_preceding_entity
        fields = COMMON_FIELDS + [
            "merged_old_data",
            "relationship_to_preceding_entity",
            "other_polity",
        ]
        labels = dict(
            COMMON_LABELS,
            **{
                "other_polity": "Entity (A): Prior",
                "polity": "Entity (B): Subsequent",
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "merged_old_data": forms.TextInput(
                    attrs=dict(
                        ATTRS.MB3_ATTRS,
                        **{
                            "readonly": "True",
                        }
                    )
                ),
                "relationship_to_preceding_entity": forms.Select(attrs=ATTRS.MB3_ATTRS),
                "other_polity": forms.Select(
                    attrs={
                        "class": "form-control mb-4 pb-4 js-example-basic-single",
                        "id": "id_other_polity",
                        "name": "other_polity",
                    }
                ),
            }
        )


class Polity_succeeding_entityForm(forms.ModelForm):
    """
    Form for creating and updating Polity_succeeding_entity model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_succeeding_entity
        fields = COMMON_FIELDS + ["succeeding_entity"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"succeeding_entity": forms.TextInput(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_supracultural_entityForm(forms.ModelForm):
    """
    Form for creating and updating Polity_supracultural_entity model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_supracultural_entity
        fields = COMMON_FIELDS + ["supracultural_entity"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"supracultural_entity": forms.TextInput(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_scale_of_supracultural_interactionForm(forms.ModelForm):
    """
    Form for creating and updating Polity_scale_of_supracultural_interaction model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_scale_of_supracultural_interaction
        fields = COMMON_FIELDS + ["scale_from", "scale_to"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "scale_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "scale_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Polity_alternate_religion_genusForm(forms.ModelForm):
    """
    Form for creating and updating Polity_alternate_religion_genus model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_alternate_religion_genus
        fields = COMMON_FIELDS + ["alternate_religion_genus"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"alternate_religion_genus": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_alternate_religion_familyForm(forms.ModelForm):
    """
    Form for creating and updating Polity_alternate_religion_family model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_alternate_religion_family
        fields = COMMON_FIELDS + ["alternate_religion_family"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"alternate_religion_family": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_alternate_religionForm(forms.ModelForm):
    """
    Form for creating and updating Polity_alternate_religion model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_alternate_religion
        fields = COMMON_FIELDS + ["alternate_religion"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"alternate_religion": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_expertForm(forms.ModelForm):
    """
    Form for creating and updating Polity_expert model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_expert
        fields = COMMON_FIELDS + ["expert"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"expert": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_editorForm(forms.ModelForm):
    """
    Form for creating and updating Polity_editor model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_editor
        fields = COMMON_FIELDS + ["editor"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS, **{"editor": forms.Select(attrs=ATTRS.MB3_ATTRS)}
        )


class Polity_religious_traditionForm(forms.ModelForm):
    """
    Form for creating and updating Polity_religious_tradition model.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_religious_tradition
        fields = COMMON_FIELDS + ["religious_tradition"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{"religious_tradition": forms.TextInput(attrs=ATTRS.MB3_ATTRS)}
        )
