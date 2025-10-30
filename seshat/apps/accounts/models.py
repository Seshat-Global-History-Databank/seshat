from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.urls import reverse
from django.core.exceptions import ValidationError
from .custom_validators import validate_email_with_dots  # Import your custom validator
from django.core.validators import EmailValidator
from datetime import datetime


# class CustomUser(AbstractUser):
#     email = models.EmailField(
#         unique=True,  # Make sure emails are unique
#         validators=[validate_email_with_dots, EmailValidator(message="Enter a valid email address.")],
#     )

from django.conf import settings

class TermsVersion(models.Model):
    slug = models.SlugField(unique=True)              # e.g. "tos-2025-10-01"
    title = models.CharField(max_length=200)
    body_html = models.TextField()                    # paste rendered HTML (e.g., your terms.html body)
    is_active = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]

class TermsAcceptance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    terms = models.ForeignKey(TermsVersion, on_delete=models.PROTECT)
    accepted_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ("user", "terms")
        ordering = ["-accepted_at"]

class Profile(models.Model):
    """
    Model representing a user profile.
    """
    SESHATADMIN = 1
    RA = 2
    SESHATEXPERT = 3
    PUBLICUSER = 4
    ROLE_CHOICES = (
        (SESHATADMIN, 'Seshat Admin'),
        (RA, 'Research Assistant'),
        (SESHATEXPERT, 'Seshat Expert'),
        (PUBLICUSER, 'Public User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False, null=True, blank=True)
    # avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField( null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True)
    
    def get_initials(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name[0].upper()}{self.user.last_name[0].upper()}"
        return self.user.username[:2].upper() 
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('user-profile')

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@property
def full_name(self):
    if self.first_name and self.last_name:
        return f"{self.first_name} {self.last_name}".strip()
    elif self.first_name:
        return f"{self.first_name}".strip()
    else:
        return f"{self.user_name}".strip()

User.add_to_class("full_name", full_name)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler for creating or updating a user profile.
    """
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()




class Seshat_Expert(models.Model):
    """
    Model representing a Seshat Expert.
    """
    SESHATADMIN = 'Seshat Admin'
    RA = 'Researcher'
    SESHATEXPERT = 'Seshat Expert'
    LR = 'Lead Researcher'
    SD = 'Seshat Director'
    PM = 'Project Manager'

    ROLE_CHOICES = (
        (SESHATADMIN, 'Seshat Admin'),
        (RA, 'Researcher'),
        (SESHATEXPERT, 'Seshat Expert'),
        (LR, 'Lead Researcher'),
        (SD, 'Seshat Director'),
        (PM, 'Project Manager'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=60,
        choices=ROLE_CHOICES, null=True, blank=True)
    
    def get_initials(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name[0].upper()}{self.user.last_name[0].upper()}"
        return self.user.username[:2].upper() 

    def __str__(self):  # __unicode__ for Python 2
        if self.user.first_name and self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        else:
            return self.user.username + " (" + self.role + ")"

class Seshat_Task(models.Model):
    """
    Model representing a Seshat Task.
    """
    giver = models.ForeignKey(Seshat_Expert, on_delete=models.CASCADE)
    taker = models.ManyToManyField(Seshat_Expert, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)ss", blank=True,)
    task_description = models.TextField( null=True, blank=True)
    task_url = models.URLField(max_length=200, null=True, blank=True)


    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('seshat_task-detail', args=[str(self.id)])

    @property
    def display_takers(self):
        """
        Returns a string of all takers of the task.

        Returns:
            str: A string of all takers of the task, joined with a HTML tag ("<br />").
        """
        all_takers = []
        for taker in self.taker.all():
            all_takers.append(taker.__str__())
        return "<br>".join(all_takers)

    @property
    def clickable_url(self):
        """
        Returns a clickable URL.

        Returns:
            str: A string of a clickable URL.
        """
        return f'<a href="{self.task_url}">{self.task_url}</a>'

    def __str__(self):  # __unicode__ for Python 2
        return self.giver.user.username + " has a atsk for you: " +  self.task_description
