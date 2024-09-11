from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from ..global_constants import ATTRS

from .models import Seshat_Task, Profile


class Seshat_TaskForm(forms.ModelForm):
    """
    Form for adding or updating a task.
    """

    class Meta:
        """
        :noindex:
        """

        model = Seshat_Task
        fields = ["giver", "taker", "task_description", "task_url"]
        labels = {
            "giver": "Who are You? ",
            "taker": '<h5>Who needs to take the task?</h5><h6 class="text-secondary mt-1">Hold <kbd class="bg-success">Ctrl</kbd> to select multiple task-takers.</h6>',
            "task_description": "<h6>What is the task?</h6>",
            "task_url": "Task URL",
        }

        widgets = {
            "giver": forms.Select(attrs=ATTRS.MB3_ATTRS),
            "taker": forms.SelectMultiple(
                attrs={
                    "class": "form-group mt-3 px-2",
                }
            ),
            "task_description": forms.Textarea(attrs=ATTRS.MB3_ATTRS),
            "task_url": forms.TextInput(attrs=ATTRS.MB3_ATTRS),
        }


class ProfileForm(forms.ModelForm):
    """
    Form for adding or updating a profile.
    """

    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)

    class Meta:
        """
        :noindex:
        """

        model = Profile
        fields = [
            "first_name",
            "last_name",
            "role",
            "location",
            "bio",
        ]
        labels = {
            "first_name": "first_name",
            "last_name": "last_name",
            "role": "role",
            "location": "location",
            "bio": "Bio",
        }

        widgets = {
            "bio": forms.Textarea(attrs=ATTRS.MB3_ATTRS),
        }


class CustomSignUpForm(UserCreationForm):
    """
    Form for signing up a user.
    """

    def clean_email(self):
        """
        A method to clean the email field and check if it contains too many
        dots in the username part.

        Returns:
            str: The email address if it is valid.

        Raises:
            ValidationError: If the email address contains too many dots in the
                username part.
        """
        email = self.cleaned_data.get("email")

        if email:
            username, domain = email.split("@")
            username_parts = username.split(".")
            if len(username_parts) > 5:
                raise ValidationError(
                    "Email address contains too many dots in the username part."
                )

        return email
