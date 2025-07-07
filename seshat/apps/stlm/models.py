######### Beginning of Model Imports
from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
#from model_utils.models import StatusModel
from django.core.exceptions import ValidationError
from django.urls import reverse

from datetime import date

import uuid

from django.utils import translation

from ..core.models import SeshatCityCommon, Certainty, Tags, Section, Subsection
from seshat.apps.accounts.models import Seshat_Expert



def call_my_name(self):
    """
    This function is used to return the name of the model instance (in lieu of
    the __str__ representation of the model instance).

    Note:
        The model instance must have the following attributes:
        - name
        - settlement (and settlement.name)
        - year_from
        - year_to

    Args:
        self (model instance): The model instance.

    Returns:
        str: The name of the model instance.
    """
    if self.year_from == self.year_to or ((not self.year_to) and self.year_from):
        return self.name + " [for " + self.settlement.name + " in " + str(self.year_from) + "]"
    else:
        return self.name + " [for " + self.settlement.name + " from " + str(self.year_from) + " to " + str(self.year_to) + "]"
    

class Settlement_population(SeshatCityCommon):
    name = models.CharField(max_length=100, default="settlement_population")
    population_from = models.IntegerField(blank=True, null=True)
    population_to = models.IntegerField(blank=True, null=True)

    def show_value(self):
        if self.population_from is not None and self.population_to is not None and self.population_to == self.population_from:
            return mark_safe(f"{self.population_from:,}<span class='fw-light fs-6 text-secondary'> people </span>")
        elif self.population_from is not None and self.population_to is not None:
            return  mark_safe(f"<span class='fw-light text-secondary'> [</span>{self.population_from:,} <span class='fw-light text-secondary'> to </span> {self.population_to:,}<span class='fw-light text-secondary'>] </span> <span class='fw-light fs-6 text-secondary'> people </span>")
        elif self.population_from is not None:
            return f"[{self.population_from:,}, ...]"
        elif self.population_to is not None:
            return f"[..., {self.population_to:,}]"
        else:
            return " - "
        
    def __str__(self) -> str:
        return call_my_name(self)
    
class Number_of_ziggurats(SeshatCityCommon):
    name = models.CharField(max_length=100, default="number_of_ziggurats")
    count = models.IntegerField(blank=True, null=True)

    def show_value(self):
        if self.count is not None:
            return f"{self.count}"
        else:
            return " - "

    def __str__(self) -> str:
        return call_my_name(self)

class Number_of_palaces(SeshatCityCommon):
    name = models.CharField(max_length=100, default="number_of_palaces")
    count = models.IntegerField(blank=True, null=True)

    def show_value(self):
        if self.count is not None:
            return f"{self.count}"
        else:
            return " - "

    def __str__(self) -> str:
        return call_my_name(self)

class Number_of_temples(SeshatCityCommon):
    name = models.CharField(max_length=100, default="number_of_temples")
    count = models.IntegerField(blank=True, null=True)

    def show_value(self):
        if self.count is not None:
            return f"{self.count}"
        else:
            return " - "

    def __str__(self) -> str:
        return call_my_name(self)

class Defensive_wall(SeshatCityCommon):
    name = models.CharField(max_length=100, default="defensive_wall")
    present = models.BooleanField(null=True, blank=True)

    def show_value(self):
        if self.present:
            return "Present"
        else:
            return "Absent"

    def __str__(self) -> str:
        return call_my_name(self)

class Tablet(SeshatCityCommon):
    name = models.CharField(max_length=100, default="tablet")
    present = models.BooleanField(null=True, blank=True)

    def show_value(self):
        if self.present:
            return "Present"
        else:
            return "Absent"


    def __str__(self) -> str:
        return call_my_name(self)

class Seal_indicator(SeshatCityCommon):
    name = models.CharField(max_length=100, default="seal_indicator")
    present = models.BooleanField(null=True, blank=True)


    def show_value(self):
        if self.present:
            return "Present"
        else:
            return "Absent"


    def __str__(self) -> str:
        return call_my_name(self)