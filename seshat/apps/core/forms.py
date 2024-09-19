from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.formsets import BaseFormSet
from django.core.exceptions import ValidationError
from django_recaptcha.fields import ReCaptchaField

from ..global_constants import _wrap, ATTRS
from ..global_utils import clean_email
from ..core.models import (
    Reference,
    Citation,
    SeshatComment,
    SeshatCommentPart,
    Polity,
    Capital,
    Nga,
    SeshatPrivateCommentPart,
    SeshatPrivateComment,
    Religion,
)


class ReligionForm(forms.ModelForm):
    """
    Form for adding or updating a new religion in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = Religion
        fields = [
            "religion_name",
        ]
        widgets = {"religion_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS)}


class ReferenceForm(forms.ModelForm):
    """
    Form for adding or updating a new reference in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = Reference
        fields = ("title", "year", "creator", "zotero_link", "long_name")
        labels = {
            "title": _wrap("Title"),
            "year": _wrap("Year"),
            "creator": _wrap("Creator"),
            "zotero_link": _wrap("Zotero Link"),
            "long_name": _wrap("Long Name"),
        }
        widgets = {
            "title": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "year": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "creator": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "zotero_link": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "long_name": forms.Textarea(
                attrs=dict(ATTRS.MB3_ATTRS, **{"style": "height: 100px"})
            ),
        }


class CitationForm(forms.ModelForm):
    """
    Form for adding or updating a new citation in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = Citation
        fields = (
            "ref",
            "page_from",
            "page_to",
        )
        labels = {
            "page_from": _wrap("Start Page"),
            "page_to": _wrap("End Page"),
            "ref": _wrap("Select Your Reference"),
        }
        widgets = {
            "ref": forms.Select(
                attrs={
                    "class": "form-control mb-3 form-select js-states js-example-basic-single",  # noqa: E501 pylint: disable=C0301
                    "text": "ref",
                }
            ),
            "page_from": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "page_to": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
        }

    def clean(self) -> dict:
        """
        Check if the citation is a duplicate.

        Returns:
            dict: The cleaned data.

        Raises:
            ValidationError: If the citation is a duplicate.
        """
        cleaned_data = super(CitationForm, self).clean()

        ref = cleaned_data.get("ref")
        page_from = cleaned_data.get("page_from")
        page_to = cleaned_data.get("page_to")

        try:
            ref_id = ref.id
        except AttributeError:
            ref_id = None  # TODO: Should we handle this differently

        if Citation.objects.filter(ref__id=ref_id, page_from=page_from, page_to=page_to):
            raise ValidationError(
                "There is already a citation with the given information. We cannot create a duplicate."  # noqa: E501 pylint: disable=C0301
            )

        return cleaned_data


class PolityForm(forms.ModelForm):
    """
    Form for adding or updating a new polity in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity
        fields = (
            "name",
            "new_name",
            "long_name",
            "start_year",
            "end_year",
            "home_seshat_region",
            "polity_tag",
            "shapefile_name",
            "private_comment",
            "general_description",
        )
        labels = {
            "name": "Polity ID (Old)",
            "new_name": "Polity ID (New)",
            "long_name": "Long Name",
            "start_year": "Start Year",
            "end_year": "End Year",
            "home_seshat_region": "Home Seshat Region",
            "polity_tag": "Polity Tag",
            "shapefile_name": "Shapefile name",
            "private_comment": "Private Comment (optional)",
            "general_description": "General Description of the Polity",
        }
        widgets = {
            "name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "new_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "long_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "start_year": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "end_year": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "home_seshat_region": forms.Select(
                attrs={
                    "class": "form-control mb-3 form-select js-example-basic-single",
                }
            ),
            "polity_tag": forms.Select(
                attrs={
                    "class": "form-control mb-3 form-select",
                }
            ),
            "shapefile_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "private_comment": forms.Textarea(
                attrs=dict(
                    ATTRS.MB3_ATTRS,
                    **{
                        "style": "height: 100px",
                        "placeholder": "Add a private comment that will only be visible to Seshat experts and RAs.\nUse this box to request edits to the polity map data.",  # noqa: E501 pylint: disable=C0301
                    }
                )
            ),
            "general_description": forms.Textarea(
                attrs=dict(
                    ATTRS.MB3_ATTRS,
                    **{
                        "style": "height: 265px",
                        "placeholder": "Add a general description (optional)",
                    }
                )
            ),
        }


class PolityUpdateForm(forms.ModelForm):
    """
    Form for adding or updating an existing polity in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity
        fields = (
            "name",
            "new_name",
            "long_name",
            "start_year",
            "end_year",
            "home_seshat_region",
            "polity_tag",
            "shapefile_name",
            "private_comment",
            "general_description",
        )
        labels = {
            "name": "Polity ID (Old)",
            "new_name": "Polity ID (New)",
            "long_name": "Long Name",
            "start_year": "Start Year",
            "end_year": "End Year",
            "home_seshat_region": "Home Seshat Region",
            "shapefile_name": "Shapefile name",
            "polity_tag": "Polity Tag",
            "private_comment": "Private Comment (optional)",
            "general_description": "General Description of the Polity",
        }
        widgets = {
            "name": forms.TextInput(
                attrs=dict(ATTRS.MB3_ATTRS, **{"readonly": "True"})
            ),
            "new_name": forms.TextInput(
                attrs=dict(ATTRS.MB3_ATTRS, **{"readonly": "True"})
            ),
            "long_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "start_year": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "end_year": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "home_seshat_region": forms.Select(
                attrs={
                    "class": "form-control mb-3 form-select js-example-basic-single",
                }
            ),
            "polity_tag": forms.Select(
                attrs={
                    "class": "form-control mb-3 form-select",
                }
            ),
            "shapefile_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "private_comment": forms.Textarea(
                attrs=dict(
                    ATTRS.MB3_ATTRS,
                    **{
                        "style": "height: 100px",
                        "placeholder": "Add a private comment that will only be visible to Seshat experts and RAs.\nUse this box to request edits to the polity map data.",  # noqa: E501 pylint: disable=C0301
                    }
                )
            ),
            "general_description": forms.Textarea(
                attrs=dict(
                    ATTRS.MB3_ATTRS,
                    **{
                        "style": "height: 265px",
                        "placeholder": "Add a general description (optional)",
                    }
                )
            ),
        }


class NgaForm(forms.ModelForm):
    """
    Form for adding or updating a new NGA in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = Nga
        fields = ("name", "world_region", "subregion", "fao_country")
        labels = {
            "name": _wrap("NGA"),
            "world_region": _wrap("World Region"),
            "subregion": _wrap("Subregion"),
            "fao_country": _wrap("Current Country"),
        }
        widgets = {
            "name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "world_region": forms.Select(
                attrs={
                    "class": "form-control mb-3 form-select",
                }
            ),
            "subregion": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "fao_country": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
        }


class CapitalForm(forms.ModelForm):
    """
    Form for adding or updating a new capital in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = Capital
        fields = (
            "name",
            "latitude",
            "longitude",
            "current_country",
            "alternative_names",
            "is_verified",
            "url_on_the_map",
            "note",
        )
        labels = {
            "name": "City Name",
            "latitude": "Latitude",
            "longitude": "Longitude",
            "alternative_names": "Alternative Names",
            "current_country": "Current Country",
            "is_verified": "Verified?",
            "url_on_the_map": "Link on Google Maps",
            "note": "Add an optional Note",
        }
        widgets = {
            "name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "current_country": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "alternative_names": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "url_on_the_map": forms.Textarea(
                attrs=dict(
                    ATTRS.MB3_ATTRS,
                    **{
                        "style": "height: 120px",
                        "placeholder": "Add the full URL from Google Maps (optional)",
                    }
                )
            ),
            "note": forms.Textarea(
                attrs=dict(
                    ATTRS.MB3_ATTRS,
                    **{
                        "style": "height: 120px",
                        "placeholder": "Add a note (optional)",
                    }
                )
            ),
            "latitude": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "longitude": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "is_verified": forms.CheckboxInput(attrs=ATTRS.MB3_SIMPLE_ATTRS),
        }


class SeshatCommentForm(forms.ModelForm):
    """
    Form for adding or updating a new comment in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = SeshatComment
        fields = ("text",)
        labels = {
            "text": _wrap("Description"),
        }
        widgets = {
            "text": forms.Textarea(
                attrs=dict(ATTRS.MB3_ATTRS, **{"style": "height: 100px"})
            ),
        }


class SeshatCommentPartForm(forms.ModelForm):
    """
    Form for adding or updating a new comment part in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = SeshatCommentPart
        fields = (
            "comment",
            "comment_part_text",
            "comment_citations",
            "comment_order",
            "comment_curator",
        )
        labels = {
            "comment": _wrap("Description ID"),
            "comment_part_text": _wrap("Subdescription Text"),
            "comment_citations": _wrap("Subdescription Citations"),
            "comment_order": _wrap("Subdescription Order in the Description"),
            "comment_curator": _wrap("Curator"),
        }
        widgets = {
            "comment": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "comment_order": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "comment_part_text": forms.Textarea(
                attrs=dict(ATTRS.MB3_ATTRS, **{"style": "height: 300px"})
            ),
            "comment_citations": forms.SelectMultiple(
                attrs={
                    "class": "form-control mb-3 js-states js-example-basic-multiple",
                    "text": "citations[]",
                    "style": "height: 340px",
                    "multiple": "multiple",
                }
            ),
            "comment_curator": forms.Select(
                attrs={
                    "class": "form-control mb-3 form-select",
                }
            ),
        }


class SeshatPrivateCommentPartForm(forms.ModelForm):
    """
    Form for adding or updating a new private comment part in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = SeshatPrivateCommentPart
        fields = (
            "private_comment",
            "private_comment_part_text",
            "private_comment_owner",
            "private_comment_reader",
        )
        labels = {
            "private_comment": _wrap("PrivateDescription ID"),
            "private_comment_part_text": _wrap("Private Comment Text"),
            "private_comment_owner": _wrap("Owner"),
            "private_comment_reader": _wrap("Target"),
        }
        widgets = {
            "private_comment": forms.NumberInput(attrs=ATTRS.MB3_BOLD_ATTRS),
            "private_comment_part_text": forms.Textarea(
                attrs=dict(ATTRS.MB3_ATTRS, **{"style": "height: 150px"})
            ),
            "private_comment_owner": forms.Select(
                attrs={
                    "class": "form-control mb-3 form-select",
                }
            ),
            "private_comment_reader": forms.SelectMultiple(
                attrs={
                    "class": "form-control mb-3 js-states js-example-basic-multiple",
                    "text": "private_comment_readers[]",
                    "style": "height: 340px",
                    "multiple": "multiple",
                }
            ),
        }


class SeshatPrivateCommentForm(forms.ModelForm):
    """
    Form for adding or updating a new private comment in the database.
    """

    class Meta:
        """
        :noindex:
        """

        model = SeshatPrivateComment
        fields = ("text",)
        labels = {
            "text": _wrap("Private Comment"),
        }
        widgets = {
            "text": forms.Textarea(
                attrs=dict(ATTRS.MB3_ATTRS, **{"style": "height: 100px"})
            ),
        }


class ReferenceWithPageForm(forms.Form):
    """
    Form for adding or updating a new reference with page numbers in the database.
    """

    ref = forms.ModelChoiceField(
        queryset=Reference.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control mb-1 form-select js-example-basic-single",
                "text": "ref",
            }
        ),
        label="",
        empty_label="Please choose a Reference ...",
    )

    page_from = forms.IntegerField(label="", required=False)
    page_to = forms.IntegerField(label="", required=False)
    parent_pars = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "style": "height: 60px;",
                "placeholder": "Consulted Paragraphs (Private, for NLP project)",
            }
        ),
        label="",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-exampleForm"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"

        self.helper.add_input(Submit("submit", "Submit"))


class BaseReferenceFormSet(BaseFormSet):
    """
    Base formset for adding or updating multiple references to a comment.
    """

    def add_fields(self, form, index):
        """
        Add fields to the form.

        Args:
            form (Form): The form to add fields to.
            index (int): The index of the form.

        Returns:
            None
        """
        super().add_fields(form, index)
        form.fields["ref"].widget.attrs[
            "class"
        ] = "form-control mb-1 form-select p-1 js-example-basic-single"
        form.fields["page_from"].widget.attrs["class"] = "form-control mb-1 p-1"
        form.fields["page_from"].widget.attrs["placeholder"] = "p_from"
        form.fields["page_to"].widget.attrs["placeholder"] = "p_to"

        form.fields["page_to"].widget.attrs["class"] = "form-control mb-1 p-1"
        form.fields["parent_pars"].widget.attrs["class"] = "form-control mb-1 p-1"


ReferenceFormSet2 = forms.formset_factory(
    ReferenceWithPageForm,
    formset=BaseReferenceFormSet,
    extra=3,
    max_num=3,
    can_delete=True,
    can_order=True,
)


ReferenceFormSet5 = forms.formset_factory(
    ReferenceWithPageForm,
    formset=BaseReferenceFormSet,
    extra=5,
    max_num=5,
    can_delete=True,
    can_order=True,
)

ReferenceFormSet10 = forms.formset_factory(
    ReferenceWithPageForm,
    formset=BaseReferenceFormSet,
    extra=10,
    max_num=10,
    can_delete=True,
    can_order=True,
)


class SeshatCommentPartForm2(forms.Form):
    comment_text = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-1 p-1",
                "style": "height: 300px",
                "placeholder": "SubDescription Text (Public)",
            }
        ),
    )

    formset = ReferenceFormSet2(prefix="refs")
    comment_order = forms.IntegerField(
        label="Do NOT Change This Number: ",
        required=False,
    )
    formset.management_form  # Include the management form


class SeshatCommentPartForm5(forms.Form):
    comment_text = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-1 p-0",
                "style": "height: 200px",
            }
        ),
    )

    formset = ReferenceFormSet5(prefix="refs")
    comment_order = forms.IntegerField(
        label="Do NOT Change This Number: ",
        required=False,
    )
    formset.management_form  # Include the management form


class SeshatCommentPartForm10(forms.Form):
    comment_text = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-1 p-0",
                "style": "height: 200px",
            }
        ),
    )

    formset = ReferenceFormSet10(prefix="refs")
    comment_order = forms.IntegerField(
        label="Do NOT Change This Number: ",
        required=False,
    )
    formset.management_form  # Include the management form


CommentPartFormSet = forms.formset_factory(SeshatCommentPartForm2, extra=2)


class SeshatCommentForm2(forms.Form):
    formset = CommentPartFormSet(prefix="commentpart")
    formset.management_form  # Include the management form


class SignUpForm(UserCreationForm):
    captcha = ReCaptchaField()

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs=dict(
                ATTRS.MB3_ATTRS,
                **{
                    "placeholder": "password",
                    "type": "password",
                    "align": "center",
                }
            )
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs=dict(
                ATTRS.MB3_ATTRS,
                **{"placeholder": "password", "type": "password", "align": "center"}
            )
        ),
    )

    def clean_email(self) -> str:
        email = self.cleaned_data.get("email")
        return clean_email(email)

    class Meta:
        """
        :noindex:
        """

        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "captcha",
        )
        widgets = {
            "first_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "last_name": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "username": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
            "email": forms.EmailInput(attrs=ATTRS.MB3_ATTRS),
        }


class VariablehierarchyFormNew(forms.Form):
    my_vars = {}
    my_vars_tuple = [("", " -- Select Variable -- ")]
    variable_name = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-control mb-3 form-select",
                "name": "variable_name",
                "id": "variable_name",
            }
        )
    )

    section_name = forms.ChoiceField(
        label="Section",
        widget=forms.Select(
            attrs={
                "class": "form-control mb-3 form-select required-entry",
                "name": "section",
                "id": "section",
                "onchange": "javascript:dynamicdropdown(this.options[this.selectedIndex].value);",  # noqa: E501 pylint: disable=C0301
            }
        ),
    )

    subsection_name = forms.ChoiceField(
        label="Subsection",
        widget=forms.Select(
            attrs={
                "class": "form-control mb-3 form-select",
                "name": "subsection",
                "id": "subsection",
            }
        ),
    )

    is_verified = forms.BooleanField(
        label=" Verified?",
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "type": "checkbox",
                "class": "form-control form-check-input align-middle",
            }
        ),
    )

    class Meta:
        """
        :noindex:
        """

        unique_together = ("variable_name", "section_name", "subsection_name")


class ReferenceWithPageForm_UPGRADE(forms.Form):
    ref = forms.ModelChoiceField(
        queryset=Reference.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-control mb-1 form-select js-example-basic-single"}
        ),
        label="",
    )
    page_from = forms.IntegerField(label="", required=False)
    page_to = forms.IntegerField(label="", required=False)
    parent_pars = forms.CharField(
        widget=forms.Textarea(attrs={"style": "height: 140px;"}),
        label="Consulted Paragraphs (UPGRADED) (Private, for NLP project)",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Submit"))


ReferenceFormSet2_UPGRADE = formset_factory(ReferenceWithPageForm_UPGRADE, extra=1)


class SeshatCommentPartForm2_UPGRADE(forms.Form):
    comment_text = forms.CharField(
        label="SubComment Text (Public)",
        widget=forms.Textarea(
            attrs={"class": "form-control mb-1", "style": "height: 200px"}
        ),
    )
    references_formset = ReferenceFormSet2_UPGRADE(prefix="refs")
    comment_order = forms.IntegerField(
        label="Do NOT Change This Number:", required=False
    )
    references_formset.management_form  # Include the management form
