from django.contrib.gis.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
#from model_utils.models import StatusModel
from django.core.exceptions import ValidationError
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import date
from django.db.models import Q
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

import uuid

from seshat.apps.accounts.models import Seshat_Expert


from django.utils import translation
from django.contrib import messages
from django.core.validators import URLValidator

def give_me_a_color_for_expert(value):
    """
    Returns a color for a given expert.

    Args:
        value (int): The id of the expert.

    Returns:
        str: A color for the expert.
    """
    light_colors = [
    '#b86354',  # Darker red tone of #e6b8af
    '#cc6666',  # Darker red tone of #f4cccc
    '#d9a065',  # Darker orange tone of #fce5cd
    '#d6b656',  # Darker yellow tone of #fff2cc
    '#94b373',  # Darker green tone of #d9ead3
    '#6c8488',  # Darker blue-gray tone of #d0e0e3
    '#6a92d1',  # Darker blue tone of #c9daf8
    '#7292a6',  # Darker gray-blue tone of #cfe2f3
    '#8f78c3',  # Darker purple tone of #d9d2e9
    '#c35b7f',  # Darker pink-purple tone of #ead1dc
    '#a93d2b',  # Darker orange-red tone of #dd7e6b
    '#b85454',  # Darker red tone of #ea9999
    '#e09957',  # Darker orange tone of #f9cb9c
    '#d7b942',  # Darker yellow tone of #ffe599
    '#79a659',  # Darker green tone of #b6d7a8
    '#4e7476',  # Darker teal tone of #a2c4c9
    '#4a7bbf',  # Darker blue tone of #a4c2f4
    '#4e92b8',  # Darker blue tone of #9fc5e8
    '#6c5ba3',  # Darker purple tone of #b4a7d6
    '#a35f88',  # Darker pink-purple tone of #d5a6bd
    '#892f15',  # Darker red tone of #cc4125
    '#a73f3f',  # Darker red tone of #e06666
    '#b86b35',  # Darker orange tone of #f6b26b
    '#d6ac34',  # Darker yellow tone of #ffd966
    '#5d8e52',  # Darker green tone of #93c47d
    '#43696d',  # Darker teal tone of #76a5af
    '#3d64b3',  # Darker blue tone of #6d9eeb
    '#4176a5',  # Darker blue tone of #6fa8dc
    '#654da6',  # Darker purple tone of #8e7cc3
    '#8f5477',  # Darker pink tone of #c27ba0
    ]
    # light_colors = [
    # '#e6b8af',
    # '#f4cccc',
    # '#fce5cd',
    # '#fff2cc',
    # '#d9ead3',
    # '#d0e0e3',
    # '#c9daf8',
    # '#cfe2f3',
    # '#d9d2e9',
    # '#ead1dc',
    # '#dd7e6b',
    # '#ea9999',
    # '#f9cb9c',
    # '#ffe599',
    # '#b6d7a8',
    # '#a2c4c9',
    # '#a4c2f4',
    # '#9fc5e8',
    # '#b4a7d6',
    # '#d5a6bd',
    # '#cc4125',
    # '#e06666',
    # '#f6b26b',
    # '#ffd966',
    # '#93c47d',
    # '#76a5af',
    # '#6d9eeb',
    # '#6fa8dc',
    # '#8e7cc3',
    # '#c27ba0',
    # ]

    index = int(value) % 30
    return light_colors[index]
# APS = 'A;P*'
# AP = 'A;P'
# NFY = 'NFY'
# UU = 'U*'
# AA = 'A'
# PP = 'P'
# PS = 'P*'
# AS = 'A*'
# Certainty = (
#     (APS, 'Absent Present Suspected'),
#     (AP, 'Absent Present'),
#     (UU, 'Unknown'),
#     (AA, 'Absent'),
#     (PP, 'Present'),
#     (AS, 'Absent Suspected'),
#     (PS, 'Present Suspected'),
#     (NFY, 'Not Filled Yet'),
# )

# Tags = (
#     ('TRS', 'Evidenced'),
#     ('DSP', 'Disputed'),
#     ('SSP', 'Suspected'),
#     ('IFR', 'Inferred'),
#     ('UNK', 'Unknown'),
# )



Tags = (
    ('TRS', 'Confident'),
    ('SSP', 'Suspected'),
    ('IFR', 'Inferred'),
    ('UND', 'Undecided'),
)

DataTypes = (
    ('A/P/U/~', 'A/P/U/~'),
    ('RANGE', 'RANGE'),
    ('TEXT', 'TEXT'),
    ('CHOICES', 'CHOICES'),
    ('COMPLEX', 'COMPLEX'),
)

CityTags = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

APS = 'A;P*'
AP = 'A;P'
NFY = 'NFY'
UU = 'U*'
AA = 'A'
U = "U"
PP = 'P'
PS = 'P*'
AS = 'A*'
P_TO_A = "P~A" 
A_TO_P = "A~P" 

POLITY_TAG_CHOICES = (('LEGACY', 'Equinox 2020 Polities'),
        ('POL_AFR_EAST', 'NEW East African Polities'),   # Africa ----> East Africa*
        ('POL_AFR_WEST', 'NEW West African Polities'), # Africa ---->  West Africa
        ('POL_AFR_SA', 'NEW Southern African Polities'),    # Africa ----> Southern Africa*
        ('POL_SA_SI', 'NEW South East Indian Polities'),    # South Asia ----> Southern India*
        ('CRISISDB_POLITIES', 'CrisisDB-specific Polities'),
        ('OTHER_TAG', 'Other Polities'),

        )

WORLD_REGION_CHOICES = (('Europe', 'Europe'),
        ('Southwest Asia', 'Southwest Asia'),
        ('Africa', 'Africa'),
        ('Central Eurasia', 'Central Eurasia'),
        ('South Asia', 'South Asia'),
        ('Southeast Asia', 'Southeast Asia'),
        ('East Asia', 'East Asia'),
        ('Oceania-Australia', 'Oceania-Australia'),
        ('North America', 'North America'),
        ('South America', 'South America'))

Certainty = (
    (AP, 'scholarly disagreement or uncertainty'),
    (UU, 'Suspected Unknown'),
    (AA, 'Absent'),
    (PP, 'Present'),
    (AS, 'Inferred Absent'),
    (PS, 'Inferred Present'),
    (NFY, 'not applicable; no other code is appropriate'),
    (U, 'Unknown'),
    (P_TO_A, 'uncertainty about when a given trait disappears'),
    (A_TO_P, 'uncertainty about when a given trait appears'),
)

def return_citations_for_comments(self):
    """
    This function is used to return the citations of the model instance
    (returning the value used in the display_citations method of the model
    instance).

    Note:
        The model instance must have the following attribute:
        - citations

        The model instance must have the following methods:
        - zoteroer

    Args:
        self (model instance): The model instance.

    Returns:
        str: The citations of the model instance, separated by comma.
    """
    if self.comment_citations.all():
        return ', '.join([' <a class="fw-bold" href="' + citation.zoteroer() + '">' + citation.citation_short_title + '</a>' for citation in self.comment_citations.all()])
    
def return_number_of_citations_for_comments(self):
    """
    Returns the number of citations for a comment.

    Returns:
        int: The number of citations for a comment.
    """
    if self.comment_citations.all():
        return len(self.comment_citations.all())
    return 0
    
def return_citations_plus_for_comments(self):
    """
    Returns a string of all the citations for a comment.

    Returns:
        str: A string of all the citations for a comment.
    """
    get_scp_tr = ScpThroughCtn.objects.filter(seshatcommentpart=self.id)
    if get_scp_tr:
        return ', '.join([' <a class="fw-bold" href="' + x.citation.zoteroer() + '">' + x.citation.citation_short_title + '</a>' for x in get_scp_tr])
    
def return_number_of_citations_plus_for_comments(self):
    """
    Returns the number of citations for a comment.

    Returns:
        int: The number of citations for a comment.
    """
    get_scp_tr = ScpThroughCtn.objects.filter(seshatcommentpart=self.id)
    if get_scp_tr:
        return len(get_scp_tr)
    return 0




class Prec_met_instance(models.Model):
    name = models.CharField(max_length=100, default="precious_metal_instance")
    metal = models.CharField(max_length=100,)

    def __str__(self) -> str:
        return self.metal

class SeshatPrivateComment(models.Model):
    """
    Model representing a private comment.
    """
    text = models.TextField(blank=True, null=True,)

    def __str__(self) -> str:
        all_private_comment_parts = self.inner_private_comments_related.all().order_by('created_date')
        if all_private_comment_parts:
            private_comment_parts = []
            for private_comment_part in all_private_comment_parts:
                my_color = give_me_a_color_for_expert(private_comment_part.private_comment_owner.id)
                private_comment_full_text = f'<span class="badge text-dark fs-6" style="border: 2px solid {my_color};">' + str(private_comment_part.private_comment_owner) + "</span> " + private_comment_part.private_comment_part_text + "<br>"
                private_comment_parts.append(private_comment_full_text)
            if not private_comment_parts or private_comment_parts == [None]:
                to_be_shown = " Nothing "
            else:
                to_be_shown = " ".join(private_comment_parts)
        elif self.text and not all_private_comment_parts:
            to_be_shown = "No Private Comments."
        else:
            to_be_shown = "EMPTY_PRIVATE_COMMENT"
        return f'{to_be_shown}'
    
    def show_inline(self) -> str:
        all_private_comment_parts = self.inner_private_comments_related.all().order_by('created_date')
        if all_private_comment_parts:
            private_comment_parts = []
            for private_comment_part in all_private_comment_parts:
                # Assign a color for the owner
                owner_color = give_me_a_color_for_expert(private_comment_part.private_comment_owner.id)

                # Create the owner badge
                owner_badge = (
                    f'<span class="text-dark px-1 fs-6" '
                    f'style="border: 2px solid {owner_color}; border-left: 10px solid {owner_color}; border-radius:5px;">'
                    f'{private_comment_part.private_comment_owner}</span>'
                )

                # Assign colors to each reader and create reader badges
                reader_badges = []
                for reader in private_comment_part.private_comment_reader.all():
                    reader_color = give_me_a_color_for_expert(reader.id)  # Use the same function for readers
                    reader_badge = (
                        f'<span class="text-dark px-1" '
                        f'style="border: 2px solid {reader_color}; border-left: 10px solid {reader_color}; border-radius:5px;">'
                        f'{reader}</span>'
                    )
                    reader_badges.append(reader_badge)

                # Combine the owner badge, reader badges, and comment text
                readers_html = "<i class='fa-solid fa-at text-secondary'></i>&nbsp;" + " ".join(reader_badges) if reader_badges else " "
                private_comment_full_text = (
                    f"<div class='pb-3'> {owner_badge} {readers_html} "
                    f"<span class='text-secondary'> {private_comment_part.private_comment_part_text}</span></div>"
                    
                )
                private_comment_parts.append(private_comment_full_text)

            if not private_comment_parts or private_comment_parts == [None]:
                to_be_shown = " Nothing "
            else:
                to_be_shown = " ".join(private_comment_parts)
        elif self.text and not all_private_comment_parts:
            to_be_shown = "No Private Comments."
        else:
            to_be_shown = "EMPTY_PRIVATE_COMMENT"
        return f'{to_be_shown}'
    
    def show_inline_short(self) -> str:
        all_private_comment_parts = self.inner_private_comments_related.all().order_by('created_date')
        if all_private_comment_parts:
            private_comment_parts = []
            for private_comment_part in all_private_comment_parts:
                # Assign a color for the owner
                owner_color = give_me_a_color_for_expert(private_comment_part.private_comment_owner.id)

                # Create the owner badge
                owner_badge = (
                    f'<span class="text-dark px-1 fs-6" '
                    f'style="border: 2px solid {owner_color}; border-left: 10px solid {owner_color}; border-radius:5px;">'
                    f'{private_comment_part.private_comment_owner}</span>'
                )

                # Assign colors to each reader and create reader badges
                reader_badges = []
                for reader in private_comment_part.private_comment_reader.all():
                    reader_color = give_me_a_color_for_expert(reader.id)  # Use the same function for readers
                    reader_badge = (
                        f'<span class="text-dark px-1" '
                        f'style="border: 2px solid {reader_color}; border-left: 10px solid {reader_color}; border-radius:5px;">'
                        f'{reader}</span>'
                    )
                    reader_badges.append(reader_badge)

                # Combine the owner badge, reader badges, and comment text
                readers_html = "<i class='fa-solid fa-at text-secondary'></i>&nbsp;" + " ".join(reader_badges) if reader_badges else " "

                if private_comment_part.private_comment_part_text.endswith("I would appreciate it if you could review it."):
                    private_comment_full_text = (
                        f"<div class='pb-3'><span class='text-secondary badge fs-6'> <i class='fa-solid fa-check-to-slot fs-6'></i> Review Request Sent By:</span> {owner_badge} {readers_html} </div>"
                    )
                else:
                    private_comment_full_text = (
                        f"<div class='pb-3'> {owner_badge} {readers_html} "
                        f"<span class='text-secondary'> {private_comment_part.private_comment_part_text}</span></div>"
                    )

                private_comment_parts.append(private_comment_full_text)

            if not private_comment_parts or private_comment_parts == [None]:
                to_be_shown = " Nothing "
            else:
                to_be_shown = " ".join(private_comment_parts)
        elif self.text and not all_private_comment_parts:
            to_be_shown = "No Private Comments."
        else:
            to_be_shown = "EMPTY_PRIVATE_COMMENT"
        return f'{to_be_shown}'
    

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('seshatprivatecomments')
        
class SeshatPrivateCommentPart(models.Model):
    """
    Model representing a part of a private comment.
    """
    private_comment = models.ForeignKey(SeshatPrivateComment, on_delete=models.SET_NULL, related_name="inner_private_comments_related",
                               related_query_name="inner_private_comments_related", null=True, blank=True)
    private_comment_part_text = models.TextField(blank=True, null=True,)

    private_comment_owner = models.ForeignKey(Seshat_Expert, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    private_comment_reader = models.ManyToManyField(Seshat_Expert,  related_name="%(app_label)s_%(class)s_readers_related",
                               related_query_name="%(app_label)s_%(class)ss_readers", blank=True,)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('seshatprivatecomment-update',  args=[str(self.private_comment.id)])

    class Meta:
        """
        :noindex:
        """
        ordering = ["created_date", "last_modified_date"]

    def __str__(self) -> str:
        if self.private_comment_part_text:
            return self.private_comment_part_text
        else:
            return "NO_Private_COMMENTS_TO_SHOW"
        

class Macro_region(models.Model):
    """
    Model representing a macro region.
    """
    name = models.CharField(max_length=100)

    class Meta:
        """
        :noindex:
        """
        ordering = ['name',]

    def __str__(self):
        return self.name

class Seshat_region(models.Model):
    """
    Model representing a Seshat region.
    """
    name = models.CharField(max_length=100)
    mac_region = models.ForeignKey(Macro_region, on_delete=models.SET_NULL, null=True, blank=True, related_name="mac_region")
    subregions_list = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        ordering = ['mac_region__name', 'name']

    def __str__(self):
        if self.mac_region:
            return f"{self.name} ({self.mac_region.name})"
        return self.name


class Nga(models.Model):
    """
    Model representing a NGA.
    """
    name = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.DecimalField(max_digits= 16, decimal_places = 12, blank=True, null=True)
    latitude = models.DecimalField(max_digits= 16, decimal_places = 12, blank=True, null=True)
    capital_city =  models.CharField(max_length=100, blank=True, null=True)
    nga_code = models.CharField(max_length=20, blank=True, null=True)
    fao_country = models.CharField(max_length=100, blank=True, null=True)
    world_region = models.CharField(max_length=100, choices=WORLD_REGION_CHOICES, default="Europe", null=True, blank=True)

    class Meta:
        """
        :noindex:
        """
        ordering = ['name']

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('ngas')

    def __str__(self) -> str:
        return self.name




class Continent(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class CurrentCountry(models.Model):
    flag_code = models.CharField(max_length=2, help_text="ISO 3166-1 alpha-2 country code (e.g., 'AF')", blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    continent = models.ForeignKey(Continent, on_delete=models.PROTECT, related_name='countries')

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']

    def __str__(self):
        return self.name


class Polity(models.Model):
    """
    Model representing a polity.
    """
    name = models.CharField(max_length=100)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    long_name = models.CharField(max_length=200, blank=True, null=True)
    new_name = models.CharField(max_length=100, blank=True, null=True)
    home_nga = models.ForeignKey(Nga, on_delete=models.SET_NULL, null=True, blank=True, related_name="home_nga")
    home_seshat_region = models.ForeignKey(Seshat_region, on_delete=models.SET_NULL, null=True, blank=True, related_name="home_seshat_region")
    polity_tag = models.CharField(max_length=100, choices=POLITY_TAG_CHOICES, default="OTHER_TAG", null=True, blank=True)
    general_description = models.TextField(blank=True, null=True,)
    shapefile_name = models.CharField(max_length=300, blank=True, null=True)
    private_comment = models.TextField(blank=True, null=True,)
    private_comment_n = models.ForeignKey(SeshatPrivateComment, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s", null=True, blank=True)

    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'polity'
        verbose_name_plural = 'polities'
        unique_together = ("name",)
        ordering = ['long_name']

    def clean(self):
        """
        Verifies a number of conditions on the start and end years of the polity.

        Raises:
            ValidationError: If the start year is greater than the end year.
            ValidationError: If the end year is greater than the current year.
            ValidationError: If the start year is greater than the current year.

        Returns:
            None
        """
        current_year = date.today().year
        if self.start_year is not None and self.end_year is not None and self.start_year > self.end_year:
            raise ValidationError("Start year cannot be greater than end year.")
        if self.end_year is not None and self.end_year > current_year:
            raise ValidationError("End year cannot be greater than the current year")
        if self.start_year is not None and self.start_year > current_year:
            raise ValidationError("Start year cannot be greater than the current year")
        
    @property
    def formatted_years(self):
        if self.start_year == self.end_year:
            if self.start_year is None:
                return '<i class="fa-solid fa-minus"></i>'
            if self.start_year < 0:
                return f'{abs(self.start_year)} <small class="text-secondary fw-normal bce-color">BCE</small>'
            else:
                return f'{self.start_year} <small class="text-secondary fw-normal ce-color">CE</small>'
        elif self.end_year is None:
            if self.start_year is None:
                return '<i class="fa-solid fa-minus"></i>'
            if self.start_year < 0:
                return f'{abs(self.start_year)} <small class="text-secondary fw-normal bce-color">BCE</small>'
            else:
                return f'{self.start_year} <small class="text-secondary fw-normal ce-color">CE</small>'
        else:
            if self.start_year < 0 and self.end_year < 0:
                return f'{abs(self.start_year)} <small class="text-secondary fw-normal bce-color">BCE</small> <i class="fa-solid fa-arrow-right-long fa-2xs" style="color:rgb(151, 151, 151)"></i> {abs(self.end_year)} <small class="text-secondary fw-normal bce-color">BCE</small>'
            elif self.start_year < 0 and self.end_year >= 0:
                return f'{abs(self.start_year)} <small class="text-secondary fw-normal bce-color">BCE</small> <i class="fa-solid fa-arrow-right-long fa-2xs" style="color:rgb(151, 151, 151)"></i> {self.end_year} <small class="text-secondary fw-normal ce-color">CE</small>'
            else:
                return f'{self.start_year} <small class="text-secondary fw-normal ce-color">CE</small> <i class="fa-solid fa-arrow-right-long fa-2xs" style="color:rgb(151, 151, 151)"></i> {self.end_year} <small class="text-secondary fw-normal ce-color">CE</small>'
            
    @property
    def formatted_years_text(self):
        if self.start_year == self.end_year:
            if self.start_year is None:
                return '-'
            if self.start_year < 0:
                return f'{abs(self.start_year)} BCE'
            else:
                return f'{self.start_year} CE'
        elif self.end_year is None:
            if self.start_year is None:
                return '-'
            if self.start_year < 0:
                return f'{abs(self.start_year)} BCE'
            else:
                return f'{self.start_year} CE'
        else:
            if self.start_year < 0 and self.end_year < 0:
                return f'{abs(self.start_year)} BCE to {abs(self.end_year)} BCE'
            elif self.start_year < 0 and self.end_year >= 0:
                return f'{abs(self.start_year)} BCE to {self.end_year} CE'
            else:
                return f'{self.start_year} CE to {self.end_year} CE'

    def __str__(self) -> str:
        if self.long_name and self.new_name:
            return f"{self.long_name} ({self.new_name})"
        else:
            return self.name

class Country(models.Model):
    """
    Model representing a country.
    """
    name = models.CharField(max_length=200)
    polity = models.ForeignKey(
        Polity, on_delete=models.SET_NULL, null=True, related_name="countries")

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'country'
        verbose_name_plural = 'countries'
        unique_together = ("name",)

    def __str__(self) -> str:
        return self.name
    

class Capital(models.Model):
    """
    Model representing a capital.
    """
    name = models.CharField(max_length=100)
    alternative_names =  models.CharField(max_length=300, blank=True, null=True)
    current_country = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(max_digits= 11, decimal_places = 8, blank=True, null=True)
    longitude = models.DecimalField(max_digits= 11, decimal_places = 8, blank=True, null=True)
    #polity_cap = models.ForeignKey(Polity, on_delete=models.SET_NULL, null=True, related_name="polity_caps")  
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True,) 
    url_on_the_map =  models.URLField(max_length=200, blank=True, null=True)
    is_verified = models.BooleanField(default=False, blank=True, null=True)

    note = models.TextField(
        blank=True, null=True,)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('capitals')

    def __str__(self) -> str:
        if self.name and self.alternative_names:
            return str(self.name) + " [" + str(self.alternative_names) + "]"
        return self.name
    class Meta:
        """
        :noindex:
        """

        #ordering = ['-year']
        ordering = ['is_verified']

class HabitationSite(models.Model):
    """
    Model representing a habitation site. Can be capital, major, or regular habitation site depending on its relation to a polity.
    """
    name = models.CharField(max_length=100)
    alternative_names = models.CharField(max_length=300, blank=True, null=True)
    current_country = models.CharField(max_length=100, blank=True, null=True)
    current_country_obj = models.ForeignKey(CurrentCountry, on_delete=models.PROTECT, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s",  null=True, blank=True)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    url_on_the_map = models.URLField(max_length=200, blank=True, null=True)

    is_verified = models.BooleanField(default=False, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    private_comment_n = models.ForeignKey(SeshatPrivateComment, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s", null=True, blank=True)


    def __str__(self):
        if self.name and self.alternative_names:
            return f"{self.name} [{self.alternative_names}]"
        return self.name

    class Meta:
        ordering = ['is_verified']




class CityPolityRelation(models.Model):
    """
    Relationship between a City and a Polity over time.
    """
    CITY_ROLE_CHOICES = [
        ("CAPITAL", "Capital"),
        ("MAJOR", "Major Settlement"),
        ("NORMAL", "Normal Settlement"),
    ]

    settlement = models.ForeignKey(HabitationSite, on_delete=models.CASCADE)
    polity = models.ForeignKey(Polity, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=CITY_ROLE_CHOICES)

    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True)

    is_verified = models.BooleanField(default=False, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.city.name} ({self.role}) in {self.polity.name}"

    class Meta:
        verbose_name = "Settlement-Polity Relation"
        verbose_name_plural = "Settlement-Polity Relations"

    @property
    def formatted_years(self):
        if self.year_from is None and self.year_to is None:
            return '<i class="fa-solid fa-minus"></i>'
        if self.year_from == self.year_to:
            if self.year_from is None:
                return '&nbsp;'
            elif self.year_from < 0:
                return f'{abs(self.year_from)} <small class="text-secondary fw-light">BCE</small>'
            else:
                return f'{self.year_from} <small class="text-secondary fw-light">CE</small>'
        elif self.year_to is None:
            if self.year_from < 0:
                return f'{abs(self.year_from)} <small class="text-secondary fw-light">BCE</small>'
            else:
                return f'{self.year_from} <small class="text-secondary fw-light">CE</small>'
        else:
            arrow = '<i class="fa-solid fa-arrow-right-long fa-2xs" style="color:rgb(151, 151, 151)"></i>'
            if self.year_from < 0 and self.year_to < 0:
                return f'{abs(self.year_from)} <small class="text-secondary fw-light">BCE</small> {arrow} {abs(self.year_to)} <small class="text-secondary fw-light">BCE</small>'
            elif self.year_from < 0 and self.year_to >= 0:
                return f'{abs(self.year_from)} <small class="text-secondary fw-light">BCE</small> {arrow} {self.year_to} <small class="text-secondary fw-light">CE</small>'
            else:
                return f'{self.year_from} <small class="text-secondary fw-light">CE</small> {arrow} {self.year_to} <small class="text-secondary fw-light">CE</small>'
            

    
class Ngapolityrel(models.Model):
    """
    Model representing a relationship between a NGA and a polity.
    """
    name = models.CharField(max_length=200, blank=True, null=True)
    polity_party = models.ForeignKey(Polity, on_delete=models.SET_NULL, null=True, related_name="polity_sides")
    nga_party = models.ForeignKey(Nga, on_delete=models.SET_NULL, null=True, related_name="nga_sides")
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True,) 
    is_home_nga = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        if self.name:
            return self.name
        elif self.polity_party and self.nga_party:
            return f"{self.polity_party.name}'s settlement in {self.nga_party.name}"
        else:
            return str(self.id)




class Section(models.Model):
    """
    Model representing a section.
    """
    name = models.CharField(max_length=200)
    seshat_db_section = models.CharField(max_length=200, null=True, blank=True,)
    db_table_name = models.CharField(max_length=100, null=True, blank=True,)
    sort_order = models.PositiveIntegerField(default=0)



    def __str__(self) -> str:
        return self.name

    def augmented_str(self) -> str:
        if self.seshat_db_section and self.name:
            return self.seshat_db_section + '_' + self.name
        else:
            return self.name

    
    class Meta:
        """
        :noindex:
        """
        unique_together = ("name", 'seshat_db_section')
        ordering = ['sort_order']



class Subsection(models.Model):
    """
    Model representing a subsection.
    """
    name = models.CharField(max_length=200)
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL, null=True, related_name="subsections")
    sort_order = models.PositiveIntegerField(default=0)


    def __str__(self) -> str:
        return self.name

    class Meta:
        """
        :noindex:
        """
        unique_together = ("name", "section")
        ordering = ['sort_order']



class Variablehierarchy(models.Model):
    """
    Model representing a variable hierarchy.
    """
    ACCESS_TYPES = [
        ('public', 'public'),
        ('private', 'private'),
        ('some_polities_are_public', 'some_polities_are_public'),
    ]
    name = models.CharField(
        max_length=200)
    canonical_name = models.CharField(
        max_length=200, null=True, blank=True,)
    section = models.ForeignKey(
        Section, on_delete=models.SET_NULL, null=True, blank=True,)
    subsection = models.ForeignKey(
        Subsection, on_delete=models.SET_NULL, null=True, blank=True,)
    is_verified = models.BooleanField(default=False)
    explanation = models.TextField(blank=True, null=True,)
    data_unit = models.TextField(blank=True, null=True,)
    data_type =models.CharField(max_length=50, choices=DataTypes, default="A/P/U/~", blank=True, null=True,)
    data_type_definition = models.TextField(blank=True, null=True,)
    api_endpoint = models.TextField(blank=True, null=True,)
    who_can_access = models.CharField(max_length=50, choices=ACCESS_TYPES, default='private')
    private_comment = models.ForeignKey(SeshatPrivateComment, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    sort_order = models.PositiveIntegerField(default=0)


    def __str__(self) -> str:
        return self.name

    class Meta:
        """
        :noindex:
        """
        unique_together = ("name", "section", "subsection")
        ordering = ['sort_order']


class Reference(models.Model):
    """
    Model Representing a reference.
    """
    title = models.CharField(max_length=500,)
    year = models.IntegerField(blank=True, null=True, )
    creator = models.CharField(max_length=500, )
    zotero_link = models.CharField(max_length=500, blank=True, null=True)
    long_name = models.CharField(max_length=500, blank=True, null=True)
    item_type = models.CharField(max_length=100, blank=True, null=True)
    url_link = models.TextField(max_length=500, validators=[URLValidator()], blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        original_title = self.title
        if self.item_type:
            my_item = self.item_type
        else:
            my_item = 'No_Item_Type'
        if len(original_title) > 60:
            shorter_title = original_title[0:60] + original_title[60:].split(" ")[0] + " ..."
        else:
            shorter_title = original_title
        if self.year and self.year > 1:
            return "%s: (%s_%s) %s" % (my_item, self.creator, self.year, shorter_title,)
        else:
            return "%s: (%s) %s" % (my_item, self.creator, shorter_title,)



    @property
    def reference_short_title(self):
        """
        Returns a short title for the reference. If the title is longer than
        60 characters, it is truncated. If the title is not provided, a default
        title is returned.

        Returns:
            str: A short title for the reference.
        """

        original_long_name = self.long_name
        if original_long_name and len(original_long_name) > 60:
           shorter_name = original_long_name[0:60] + original_long_name[60:].split(" ")[0] + "..."
        elif original_long_name:
           shorter_name = original_long_name
        else:
            shorter_name = "BlaBla"

        if self.zotero_link and "NOZOTERO_LINK" in self.zotero_link:
            return f'(NOZOTERO_REF: {shorter_name})'
        elif self.title:
            return self.title
        else:
            return "NO_TITLES_PROVIDED"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('references')

    class Meta:
        """
        :noindex:
        """
        # ordering = ['-year']
        unique_together = ("zotero_link",)
        ordering = ['-created_date', 'title']


class Citation(models.Model):
    """
    Model representing a specific citation.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique Id for this particular citation")
    ref = models.ForeignKey(
        Reference, on_delete=models.SET_NULL, null=True, related_name="citation")
    page_from = models.IntegerField(null=True, blank=True)
    page_to = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    # class Meta:
    #     permissions = (("can_mark_returned", "Set book as returned"),
    #                    ("can_renew", "Can Renew A Book"),)

    def zoteroer(self):
        """
        Returns the Zotero link for the citation.

        Returns:
            str: The Zotero link for the citation.
        """
        if self.ref.zotero_link and "NOZOTERO_LINK" not in self.ref.zotero_link:
            my_zotero_link = "https://www.zotero.org/groups/1051264/seshat_databank/items/" + \
                str(self.ref.zotero_link)
        else:
            my_zotero_link = reverse('citation-update', args=[str(self.id)])
        return my_zotero_link

    # def page_from_maker(self):
    #     return(str(self.page_from))
    # def page_to_maker(self):
    #     return(str(self.page_to))

    def __str__(self) -> str:
        if self.ref and self.ref.title:
            original_title = self.ref.title
        else:
            original_title = "REFERENCE_WITH_NO_TITLE"
        if original_title and len(original_title) > 50:
            shorter_title = original_title[0:50] + original_title[50:].split(" ")[0] + "..."
        elif original_title:
            shorter_title = original_title
        else:
            shorter_title = "BlaBlaBla"

        if self.ref and self.ref.long_name:
            original_long_name = self.ref.long_name
        else:
            original_long_name = "REFERENCE_WITH_NO_LONG_NAME"
        if original_long_name and len(original_long_name) > 50:
            shorter_name = original_long_name[0:50] + original_long_name[50:].split(" ")[0] + "..."
        elif original_long_name:
            shorter_name = original_long_name
        else:
            shorter_name = "BlaBla"

        if self.ref and self.ref.zotero_link and "NOZOTERO_LINK" in self.ref.zotero_link:
            return f'(NOZOTERO: {shorter_name})'
        if self.ref and self.ref.creator and self.ref.item_type and self.ref.creator == 'NO_CREATOR':
            return f'{self.ref.item_type}_{shorter_name}'
        if self.ref and self.ref.creator:
            if self.page_from == None and self.page_to == None:
                return '({0} {1}): {2}'.format(self.ref.creator, self.ref.year, shorter_title)
            elif self.page_from == self.page_to or ((not self.page_to) and self.page_from):
                return '({0} {1}, p. {2}): {3}'.format(self.ref.creator, self.ref.year, self.page_from, shorter_title)
            elif self.page_from == self.page_to or ((not self.page_from) and self.page_to):
                return '({0} {1}, p. {2}): {3}'.format(self.ref.creator, self.ref.year, self.page_to, shorter_title)
            elif self.page_from and self.page_to:
                return '({0} {1}, pp. {2}-{3}): {4}'.format(self.ref.creator, self.ref.year, self.page_from, self.page_to, shorter_title)
            else:
                return '({0} {1}): {2}'.format(self.ref.creator, self.ref.year, shorter_title)
        else:
            print("BADREF::::")
            print(self.id)
            print(self.modified_date)

            return "BADBADREFERENCE"

    def full_citation_display(self) -> str:
        """
        Returns a string of the full citation. If the citation has a title, it
        is included in the string. If the citation has a creator, it is
        included in the string. If the citation has a year, it is included in
        the string. If the citation has a page_from, it is included in the
        string. If the citation has a page_to, it is included in the string.

        Returns:
            str: A string of the full citation.
        """
        if self.ref and self.ref.title:
            original_title = self.ref.title
        else:
            original_title = "REFERENCE_WITH_NO_TITLE"
        if original_title:
            shorter_title = original_title
        else:
            shorter_title = "BlaBlaBla"

        if self.ref and self.ref.long_name:
            original_long_name = self.ref.long_name
        else:
            original_long_name = "REFERENCE_WITH_NO_LONG_NAME"
        if original_long_name:
            shorter_name = original_long_name
        else:
            shorter_name = "BlaBla"

        if self.ref and self.ref.zotero_link and "NOZOTERO_LINK" in self.ref.zotero_link:
            return f'(NOZOTERO: {shorter_name})'
        if self.ref and self.ref.creator:
            if self.page_from == None and self.page_to == None:
                return '<b class="fw-bold">({0} {1})</b>: {2}'.format(self.ref.creator, self.ref.year, shorter_title)
            elif self.page_from == self.page_to or ((not self.page_to) and self.page_from):
                return '<b class="fw-bold">({0} {1}, p. {2})</b>: {3}'.format(self.ref.creator, self.ref.year, self.page_from, shorter_title)
            elif self.page_from == self.page_to or ((not self.page_from) and self.page_to):
                return '<b class="fw-bold">({0} {1}, p. {2})</b>: {3}'.format(self.ref.creator, self.ref.year, self.page_to, shorter_title)
            elif self.page_from and self.page_to:
                return '<b class="fw-bold">({0} {1}, pp. {2}-{3})</b>: {4}'.format(self.ref.creator, self.ref.year, self.page_from, self.page_to, shorter_title)
            else:
                return '<b class="fw-bold">({0} {1})</b>: {2}'.format(self.ref.creator, self.ref.year, shorter_title)
        else:
            print("BADREF::::")
            print(self.id)
            print(self.modified_date)

            return "BADBADREFERENCE"

    class Meta:
        """
        :noindex:
        """
        #ordering = ['-year']
        ordering = ['-modified_date']
        constraints = [
        models.UniqueConstraint(
            name="No_PAGE_TO_AND_FROM",
            fields=("ref",),
            condition=(Q(page_to__isnull=True) & Q(page_from__isnull=True)) 
        ),
        models.UniqueConstraint(
            name="No_PAGE_TO",
            fields=("ref", "page_from"),
            condition=Q(page_to__isnull=True)
        ),
        models.UniqueConstraint(
            name="No_PAGE_FROM",
            fields=("ref", "page_to"),
            condition=Q(page_from__isnull=True)
        ),
        ]
        #unique_together = ["ref", "page_from", "page_to"]

    @property
    def citation_short_title(self):
        """
        Returns a short title for the citation. If the title is longer than
        40 characters, it is truncated. If the title is not provided, a default
        title is returned.

        Returns:
            str: A short title for the citation.
        """

        original_long_name = self.ref.long_name
        if original_long_name and len(original_long_name) > 40:
            shorter_name = original_long_name[0:40] + original_long_name[40:].split(" ")[0] + "..."
        elif original_long_name:
            shorter_name = original_long_name
        else:
            shorter_name = "BlaBla"

        original_title = self.ref.title
        if original_title and len(original_title) > 30:
           shorter_title = original_title[0:30] + original_title[30:].split(" ")[0] + "..."
        elif original_title:
            shorter_title = original_title
        else:
            shorter_title = "BlaBla"

        if "NOZOTERO_LINK" in self.ref.zotero_link:
            return f'(NOZOTERO: {shorter_name})'
        
        if self.ref and self.ref.creator and self.ref.item_type and self.ref.creator == 'NO_CREATOR' and self.ref.title:
            return f'[{self.ref.item_type}_{shorter_title}]'

        if self.page_from == None and self.page_to == None:
            return '[{0} {1}]'.format(self.ref.creator, self.ref.year)
        elif self.page_from == self.page_to or ((not self.page_to) and self.page_from):
            return '[{0} {1}, p. {2}]'.format(self.ref.creator, self.ref.year, self.page_from)
        elif self.page_from == self.page_to or ((not self.page_from) and self.page_to):
            return '[{0} {1}, p. {2}]'.format(self.ref.creator, self.ref.year, self.page_to)
        elif self.page_from and self.page_to:
            return '[{0} {1}, pp. {2}-{3}]'.format(self.ref.creator, self.ref.year, self.page_from, self.page_to)
        else:
            return '[{0} {1}]'.format(self.ref.creator, self.ref.year)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('citations')
    
    def save(self, *args, **kwargs):
        """
        Saves the citation to the database.

        Args:
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Raises:
            IntegrityError: If the citation cannot be saved to the database.

        Returns:
            None
        """
        try:
            super(Citation, self).save(*args, **kwargs)
        except IntegrityError as e:
            print(e)

class SeshatComment(models.Model):
    """
    Model representing a comment.
    """
    text = models.TextField(blank=True, null=True,)

    def zoteroer(self):
        """
        Returns the Zotero link for the comment.

        Returns:
            str: The Zotero link for the comment.
        """
        if self.ref.zotero_link and "NOZOTERO_LINK" not in self.ref.zotero_link:
            my_zotero_link = "https://www.zotero.org/groups/1051264/seshat_databank/items/" + \
                str(self.ref.zotero_link)
        else:
            my_zotero_link = "#"
        return my_zotero_link

    def __str__(self) -> str:
        all_comment_parts = self.inner_comments_related.all().order_by('comment_order')

        if all_comment_parts:
            comment_parts = []
            for comment_part in all_comment_parts:
                if comment_part.citation_index:
                    separation_point = comment_part.citation_index
                    comment_full_text = comment_part.comment_part_text[0:separation_point] + str(comment_part.display_citations_plus) + " " + comment_part.comment_part_text[separation_point:]
                else:
                    if comment_part.comment_part_text and comment_part.comment_part_text.startswith("<br>"):
                        if comment_part.display_citations_plus:
                            comment_full_text = comment_part.comment_part_text[4:] + str(comment_part.display_citations_plus)
                        else:
                            comment_full_text = comment_part.comment_part_text[4:]
                    else:
                        if comment_part.display_citations_plus:
                            comment_full_text = comment_part.comment_part_text + ' ' + str(comment_part.display_citations_plus)
                        else:
                            comment_full_text = comment_part.comment_part_text

                comment_parts.append(comment_full_text)
            #comment_parts = ["<b>" + str(comment_part.comment_curator)+ "</b>: " + str(comment_part.comment_part_text) + str(comment_part.display_citations) for comment_part in all_comment_parts]
            #ref_parts = ['<a href="#">' + str(comment_part.comment_order) + ' </a>' for comment_part in all_comment_parts]
            if not comment_parts or comment_parts == [None]:
                to_be_shown = " Nothing "
            else:
                to_be_shown = " ".join(comment_parts)
                
        elif self.text and not all_comment_parts:
            to_be_shown = "No descriptions."
        else:
            to_be_shown = "EMPTY_COMMENT"
        return f'{to_be_shown}'
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('seshatcomments')


class SeshatCommentPart(models.Model):
    """
    Model representing a part of a comment.
    """
    comment = models.ForeignKey(SeshatComment, on_delete=models.SET_NULL, related_name="inner_comments_related",
                               related_query_name="inner_comments_related", null=True, blank=True)
    comment_part_text = models.TextField(blank=True, null=True,)
    comment_citations_plus = models.ManyToManyField(Citation, through='ScpThroughCtn', related_name="%(app_label)s_%(class)s_related_through",
                               related_query_name="%(app_label)s_%(class)ss", blank=True,)
    comment_curator = models.ForeignKey(Seshat_Expert, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    comment_order = models.IntegerField(blank=True, null=True,)
    comment_citations = ManyToManyField(
        Citation, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", blank=True,)
    citation_index = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the
            return_citations_for_comments function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations_for_comments(self)

    @property
    def citations_count(self):
        """
        Returns the number of citations for a comment.

        Returns:
            int: The number of citations for a comment.
        """
        return return_number_of_citations_for_comments(self)
    
    @property
    def display_citations_plus(self):
        """
        Returns a string of all the citations for a comment.

        :noindex:

        Note:
            The method is a property, and an alias for the
            return_citations_for_comments function.

        Returns:
            str: A string of all the citations for a comment.
        """
        if return_citations_plus_for_comments(self) and return_citations_for_comments(self):
            return return_citations_plus_for_comments(self) + return_citations_for_comments(self)
        elif return_citations_plus_for_comments(self):
            return return_citations_plus_for_comments(self)
        else:
            return return_citations_for_comments(self)
    
    @property
    def citations_count_plus(self):
        """
        Returns the number of citations for a comment.

        Returns:
            int: The number of citations for a comment.
        """
        return return_number_of_citations_plus_for_comments(self)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('seshatcomment-update',  args=[str(self.comment.id)])

    class Meta:
        """
        :noindex:
        """
        ordering = ['comment_order', "modified_date"]
        #ordering = ["modified_date"]

    def __str__(self) -> str:
        if self.comment_part_text and self.display_citations_plus:
            return self.comment_part_text + ' ' + self.display_citations_plus
        elif self.comment_part_text and self.display_citations:
            return self.comment_part_text + ' ' + self.display_citations
        elif self.comment_part_text:
            return self.comment_part_text
        else:
            return "NO_SUB_COMMENTS_TO_SHOW"
        

class ScpThroughCtn(models.Model):
    """
    Model representing a through model for the many-to-many relationship between
    a comment part and a citation.
    """
    seshatcommentpart = models.ForeignKey(SeshatCommentPart, on_delete=models.CASCADE,  related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    citation = models.ForeignKey(Citation, on_delete=models.CASCADE,  related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    parent_paragraphs = models.TextField(blank=True, null=True,)


class SeshatCommon(models.Model):
    """
    Model representing a common Seshat model.
    """
    polity = models.ForeignKey(Polity, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True,)
    name = models.CharField(
        max_length=200,)
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True,)
    # exra vars will be added in between
    description = models.TextField(
        blank=True, null=True,)
    note = models.TextField(
        blank=True, null=True,)
    citations = ManyToManyField(
        Citation, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", blank=True,)
    finalized = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    tag = models.CharField(max_length=5, choices=Tags, default="TRS")
    is_disputed = models.BooleanField(default=False, blank=True, null=True)
    is_uncertain = models.BooleanField(default=False, blank=True, null=True)
    expert_reviewed = models.BooleanField(null=True, blank=True, default=True)
    drb_reviewed = models.BooleanField(null=True, blank=True, default=False)
    curator = models.ManyToManyField(Seshat_Expert,  related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", blank=True,)
    comment = models.ForeignKey(SeshatComment, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    private_comment = models.ForeignKey(SeshatPrivateComment, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s", null=True, blank=True)

    class Meta:
        """
        :noindex:
        """
        abstract = True
        ordering = ['polity']

    def curators_list(self):
        my_list = [f'{curator.user.full_name} ({curator.role})' for curator in self.curator.all()]
        return ", ".join(my_list) if my_list else None

        
    def curators_list_ids(self):
        my_list = [curator.id for curator in self.curator.all()]
        return my_list if my_list else None

        
    def researchers_list(self):
        researchers = self.curator.filter(role__in=['Researcher', 'Seshat Admin', 'Lead Researcher'])  
        my_list = [f'{curator.user.full_name} ({curator.role})' for curator in researchers]
        return ", ".join(my_list) if my_list else None
    
        
    def researchers_list_ids(self):
        researchers = self.curator.filter(role__in=['Researcher', 'Seshat Admin', 'Lead Researcher'])  
        my_list = [curator.id for curator in researchers]
        return my_list if my_list else None
    
        
    def seshat_experts_list(self):
        seshat_experts = self.curator.filter(role__in=['Seshat Expert',])  
        my_list = [f'{curator.user.full_name} ({curator.role})' for curator in seshat_experts]
        return ", ".join(my_list) if my_list else None
    
        
    def seshat_experts_list_ids(self):
        seshat_experts = self.curator.filter(role__in=['Seshat Expert',])  
        my_list = [curator.id for curator in seshat_experts]
        return my_list if my_list else None
    
    @property
    def formatted_years(self):
        if self.year_from is None and self.year_to is None:
            return '<i class="fa-solid fa-minus"></i>'

        if self.year_to is None:
            if self.year_from < 0:
                return f'{abs(self.year_from)} <small class="text-secondary fw-light">BCE</small>'
            else:
                return f'{self.year_from} <small class="text-secondary fw-light">CE</small>'
        elif self.year_from is None:
            if self.year_to < 0:
                return f'{abs(self.year_to)} <small class="text-secondary fw-light">BCE</small>'
            else:
                return f'{self.year_to} <small class="text-secondary fw-light">CE</small>'
        elif self.year_from == self.year_to:
            if self.year_from is None:
                return '&nbsp;'
            elif self.year_from < 0:
                return f'{abs(self.year_from)} <small class="text-secondary fw-light">BCE</small>'
            else:
                return f'{self.year_from} <small class="text-secondary fw-light">CE</small>'
        else:
            arrow = '<i class="fa-solid fa-arrow-right-long fa-2xs" style="color:rgb(151, 151, 151)"></i>'
            if self.year_from < 0 and self.year_to < 0:
                return f'{abs(self.year_from)} <small class="text-secondary fw-light">BCE</small> {arrow} {abs(self.year_to)} <small class="text-secondary fw-light">BCE</small>'
            elif self.year_from < 0 and self.year_to >= 0:
                return f'{abs(self.year_from)} <small class="text-secondary fw-light">BCE</small> {arrow} {self.year_to} <small class="text-secondary fw-light">CE</small>'
            else:
                return f'{self.year_from} <small class="text-secondary fw-light">CE</small> {arrow} {self.year_to} <small class="text-secondary fw-light">CE</small>'
            
    @property
    def formatted_years_text(self):
        if self.year_from is None and self.year_to is None:
            return '-'

        if self.year_to is None:
            if self.year_from < 0:
                return f'{abs(self.year_from)}  BCE'
            else:
                return f'{self.year_from}  CE'
        elif self.year_from is None:
            if self.year_to < 0:
                return f'{abs(self.year_to)}  BCE'
            else:
                return f'{self.year_to}  CE'
        elif self.year_from == self.year_to:
            if self.year_from is None:
                return ' '
            elif self.year_from < 0:
                return f'{abs(self.year_from)}  BCE'
            else:
                return f'{self.year_from}  CE'
        else:
            arrow = 'to'
            if self.year_from < 0 and self.year_to < 0:
                return f'{abs(self.year_from)}  BCE {arrow} {abs(self.year_to)}  BCE'
            elif self.year_from < 0 and self.year_to >= 0:
                return f'{abs(self.year_from)}  BCE {arrow} {self.year_to}  CE'
            else:
                return f'{self.year_from}  CE {arrow} {self.year_to}  CE'



class ScientificResource(models.Model):
    RESOURCE_TYPES = [
        ('article', 'Article'),
        ('dataset', 'Dataset'),
        ('book', 'Book'),
        ('report', 'Report'),
        ('thesis', 'Thesis'),
        ('code', 'Code Repository'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    authors = models.CharField(max_length=500, help_text="List of authors, separated by commas", blank=True, null=True)
    publication_year = models.PositiveIntegerField(blank=True, null=True)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES, default='article')
    url = models.URLField(blank=True, null=True)
    doi = models.CharField(max_length=100, blank=True, null=True, help_text="Digital Object Identifier if available")
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    last_updated = models.DateTimeField(auto_now=True, blank=True, null=True,)
    is_peer_reviewed = models.BooleanField(default=False, blank=True, null=True,)
    file_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['-publication_year', 'title']

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    

class SeshatCityCommon(models.Model):
    """
    Model representing a common Seshat model.
    """
    settlement = models.ForeignKey(HabitationSite, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True,)
    name = models.CharField(
        max_length=200,)
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(blank=True, null=True,)
    # exra vars will be added in between
    description = models.TextField(
        blank=True, null=True,)
    note = models.TextField(
        blank=True, null=True,)
    general_ref = models.ForeignKey(ScientificResource, on_delete=models.SET_NULL,  related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    finalized = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    tag = models.CharField(max_length=5, choices=CityTags, default="1")
    is_disputed = models.BooleanField(default=False, blank=True, null=True)
    is_uncertain = models.BooleanField(default=False, blank=True, null=True)
    expert_reviewed = models.BooleanField(null=True, blank=True, default=True)
    curator = models.ManyToManyField(Seshat_Expert,  related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)ss", blank=True,)
    comment = models.ForeignKey(SeshatComment, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s", null=True, blank=True)
    private_comment = models.ForeignKey(SeshatPrivateComment, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s", null=True, blank=True)

    class Meta:
        """
        :noindex:
        """
        abstract = True
        ordering = ['settlement']

    def curators_list(self):
        my_list = [f'{curator.user.full_name} ({curator.role})' for curator in self.curator.all()]
        return ", ".join(my_list) if my_list else None

        
    def curators_list_ids(self):
        my_list = [curator.id for curator in self.curator.all()]
        return my_list if my_list else None

        
    def researchers_list(self):
        researchers = self.curator.filter(role__in=['Researcher', 'Seshat Admin', 'Lead Researcher'])  
        my_list = [f'{curator.user.full_name} ({curator.role})' for curator in researchers]
        return ", ".join(my_list) if my_list else None
    
        
    def researchers_list_ids(self):
        researchers = self.curator.filter(role__in=['Researcher', 'Seshat Admin', 'Lead Researcher'])  
        my_list = [curator.id for curator in researchers]
        return my_list if my_list else None
    
        
    def seshat_experts_list(self):
        seshat_experts = self.curator.filter(role__in=['Seshat Expert',])  
        my_list = [f'{curator.user.full_name} ({curator.role})' for curator in seshat_experts]
        return ", ".join(my_list) if my_list else None
    
        
    def seshat_experts_list_ids(self):
        seshat_experts = self.curator.filter(role__in=['Seshat Expert',])  
        my_list = [curator.id for curator in seshat_experts]
        return my_list if my_list else None


# class Annual_wages(SeshatCommon):
#     name = models.CharField(max_length=100, default="Annual_wages")
#     annual_wages = models.IntegerField(blank=True, null=True)
#     job_category = models.CharField(choices=job_category_annual_wages_choices)
#     job_description = models.CharField(
#         choices=job_description_annual_wages_choices)
        
class Religion(models.Model):
    """
    Model representing a religion.
    """
    name = models.CharField(max_length=100, default="Religion")
    religion_name = models.CharField(max_length=100, null=True, blank=True)
    religion_family = models.CharField(max_length=100, blank=True, null=True)
    religion_genus = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        ordering = ['name']

    def __str__(self) -> str:
        if self.religion_name:
            return self.religion_name
        return self.name

# Shapefile models

class Cliopatria(models.Model):
    """
    Model representing Cliopatria polity borders dataset.
    """
    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField()
    simplified_geom = models.MultiPolygonField(null=True)
    name=models.CharField(max_length=100)
    wikipedia_name=models.CharField(max_length=100, null=True)
    seshat_id=models.CharField(max_length=100)
    area=models.FloatField()
    start_year=models.IntegerField()
    end_year=models.IntegerField()
    polity_start_year=models.IntegerField()
    polity_end_year=models.IntegerField()
    colour=models.CharField(max_length=7)
    components=models.CharField(max_length=500, null=True)
    member_of=models.CharField(max_length=500, null=True)

    def __str__(self):
        return "Name: %s" % self.name

class GADMShapefile(models.Model):
    """
    
    """
    geom = models.MultiPolygonField()
    UID=models.BigIntegerField()
    GID_0=models.CharField(max_length=100, null=True)
    NAME_0=models.CharField(max_length=100, null=True)
    VARNAME_0=models.CharField(max_length=100, null=True)
    GID_1=models.CharField(max_length=100, null=True)
    NAME_1=models.CharField(max_length=100, null=True)
    VARNAME_1=models.CharField(max_length=100, null=True)
    NL_NAME_1=models.CharField(max_length=100, null=True)
    ISO_1=models.CharField(max_length=100, null=True)
    HASC_1=models.CharField(max_length=100, null=True)
    CC_1=models.CharField(max_length=100, null=True)
    TYPE_1=models.CharField(max_length=100, null=True)
    ENGTYPE_1=models.CharField(max_length=100, null=True)
    VALIDFR_1=models.CharField(max_length=100, null=True)
    GID_2=models.CharField(max_length=100, null=True)
    NAME_2=models.CharField(max_length=100, null=True)
    VARNAME_2=models.CharField(max_length=100, null=True)
    NL_NAME_2=models.CharField(max_length=100, null=True)
    HASC_2=models.CharField(max_length=100, null=True)
    CC_2=models.CharField(max_length=100, null=True)
    TYPE_2=models.CharField(max_length=100, null=True)
    ENGTYPE_2=models.CharField(max_length=100, null=True)
    VALIDFR_2=models.CharField(max_length=100, null=True)
    GID_3=models.CharField(max_length=100, null=True)
    NAME_3=models.CharField(max_length=100, null=True)
    VARNAME_3=models.CharField(max_length=100, null=True)
    NL_NAME_3=models.CharField(max_length=100, null=True)
    HASC_3=models.CharField(max_length=100, null=True)
    CC_3=models.CharField(max_length=100, null=True)
    TYPE_3=models.CharField(max_length=100, null=True)
    ENGTYPE_3=models.CharField(max_length=100, null=True)
    VALIDFR_3=models.CharField(max_length=100, null=True)
    GID_4=models.CharField(max_length=100, null=True)
    NAME_4=models.CharField(max_length=100, null=True)
    VARNAME_4=models.CharField(max_length=100, null=True)
    CC_4=models.CharField(max_length=100, null=True)
    TYPE_4=models.CharField(max_length=100, null=True)
    ENGTYPE_4=models.CharField(max_length=100, null=True)
    VALIDFR_4=models.CharField(max_length=100, null=True)
    GID_5=models.CharField(max_length=100, null=True)
    NAME_5=models.CharField(max_length=100, null=True)
    CC_5=models.CharField(max_length=100, null=True)
    TYPE_5=models.CharField(max_length=100, null=True)
    ENGTYPE_5=models.CharField(max_length=100, null=True)
    GOVERNEDBY=models.CharField(max_length=100, null=True)
    SOVEREIGN=models.CharField(max_length=100, null=True)
    DISPUTEDBY=models.CharField(max_length=100, null=True)
    REGION=models.CharField(max_length=100, null=True)
    VARREGION=models.CharField(max_length=100, null=True)
    COUNTRY=models.CharField(max_length=100, null=True)
    CONTINENT=models.CharField(max_length=100, null=True)
    SUBCONT=models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Name: %s" % self.name
    
class GADMCountries(models.Model):
    """
    Model representing a country (GADM).
    """
    geom = models.MultiPolygonField()
    COUNTRY=models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Name: %s" % self.name
    
class GADMProvinces(models.Model):
    """
    Model representing a province (GADM).
    """
    geom = models.MultiPolygonField()
    COUNTRY=models.CharField(max_length=100, null=True)
    NAME_1=models.CharField(max_length=100, null=True)
    ENGTYPE_1=models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Name: %s" % self.name
