from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.widgets import Textarea

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.template.defaulttags import register
from .models import Seshat_Task, Seshat_Expert, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



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
            'giver': 'Who are You? ',
            'taker': '<h5>Who needs to take the task?</h5><h6 class="text-secondary mt-1">Hold <kbd class="bg-success">Ctrl</kbd> to select multiple task-takers.</h6>',
            'task_description': '<h6>What is the task?</h6>',
            "task_url" : "Task URL"
        }
                
        widgets = {
        'giver': forms.Select(attrs={'class': 'form-control  mb-3', }),
        'taker': forms.SelectMultiple(attrs={'class': 'form-group mt-3 px-2', }),
        'task_description': forms.Textarea(attrs={'class': 'form-control  mb-3', }),
        'task_url': forms.TextInput(attrs={'class': 'form-control  mb-3', })
}

        
# class EditProfileForm(ModelForm):
#     class Meta:
#         model = User
#         fields = (
#                  'email',
#                  'first_name',
#                  'last_name'
#                 )
        
#         widgets = {
#         'email': forms.Textarea(attrs={'class': 'form-control  mb-3', }),
#         'first_name': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
#         'last_name': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
# }

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
        fields = ["first_name", "last_name", "role", "location", "bio", ]
        labels = {
            'first_name': "first_name",
            'last_name': "last_name",
            'role': 'role',
            'location': 'location',
            'bio': 'Bio',
        }
                
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control  mb-3', }),
#            'role': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
#            'location': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
#            'last_name': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
#            'first_name': forms.TextInput(attrs={'class': 'form-control  mb-3', }),
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
        email = self.cleaned_data.get('email')
        if email:
            username, domain = email.split('@')
            username_parts = username.split('.')
            if len(username_parts) > 5:
                raise ValidationError("Email address contains too many dots in the username part.")
        return email