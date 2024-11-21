from django.db import models
########## Beginning of Model Imports
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
#from model_utils.models import StatusModel
from django.core.exceptions import ValidationError
from django.urls import reverse

from datetime import date

import uuid

from django.utils import translation

from ..core.models import SeshatCommon, Certainty, Tags, Section, Subsection, Religion
from seshat.apps.accounts.models import Seshat_Expert



########## Beginning of tuple choices for general Models
ABSENT_PRESENT_CHOICES = (
('present', 'present'),
('absent', 'absent'),
('unknown', 'unknown'),
('A~P', 'Transitional (Absent -> Present)'),
('P~A', 'Transitional (Present -> Absent)'),
)

FREQUENCY_CHOICES = (
('never', 'never (absent)'),
('vr', 'very rarely'),
('mftvr', 'more frequently than very rarely'),
('unknown', 'unknown'),
)

PREVALENCE_CHOICES = (
('v_m', 'Vast majority'),
('o_h_p', 'Over half of the population'),
('sz_m', 'Sizeable minority'),
('a_m', 'Minority'),
('sm_m', 'Small minority'),
('vs_m',  'Very small minority'),
('unk', 'unknown'),   # suspected goes into the tag
('unc', 'uncoded'),
('n_d', 'no_data'),   # none
)

ORDER_CHOICES = (
('1', '1. Most widespread'),
('2', '2. Second most widespread'),
('3', '3. Third most widespread'),
('4', '4. Fourth most widespread'),
('9', 'Other'),
)

###################
def call_my_name(self):
    """
    This function is used to return the name of the model instance (in lieu of
    the __str__ representation of the model instance).

    Note:
        The model instance must have the following attributes:
        - name
        - polity (and polity.name)
        - year_from
        - year_to

    Args:
        self (model instance): The model instance.

    Returns:
        str: The name of the model instance.
    """
    if self.year_from == self.year_to or ((not self.year_to) and self.year_from):
        return self.name + " [for " + self.polity.name + " in " + str(self.year_from) + "]"
    else:
        return self.name + " [for " + self.polity.name + " from " + str(self.year_from) + " to " + str(self.year_to) + "]"


def return_citations(self):
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
    return ', '.join(['<a href="' + citation.zoteroer() + '">' + citation.__str__() + ' </a>' for citation in self.citations.all()[:2]])

def clean_times(self):
    """
    This function is used to validate the year_from and year_to fields of the
    model instance (called from each model's clean method).

    Note:
        The model instance must have the following attributes:
        - year_from
        - year_to
        - polity (and polity.start_year and polity.end_year)

    Args:
        self (model instance): The model instance.

    Returns:
        None

    Raises:
        ValidationError: If the year_from is greater than the year_to.
        ValidationError: If the year_from is out of range.
        ValidationError: If the year_from is earlier than the start year of the corresponding polity.
        ValidationError: If the year_to is later than the end year of the corresponding polity.
        ValidationError: If the year_to is out of range.
    """
    if (self.year_from and self.year_to) and self.year_from > self.year_to:
        raise ValidationError({
            'year_from':  mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i> The start year is bigger than the end year!</span>'),
        })
    if self.year_from and (self.year_from > date.today().year):
        raise ValidationError({
            'year_from':  mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i> The start year is out of range!</span>'),
        })
    if self.year_from and (self.year_from < self.polity.start_year):
        raise ValidationError({
            'year_from': mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i> The start year is earlier than the start year of the corresponding polity!</span>'),
        })
    if self.year_to and (self.year_to > self.polity.end_year):
        raise ValidationError({
            'year_to':  mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i>The end year is later than the end year of the corresponding polity!</span>'),
        })
    if self.year_to and (self.year_to > date.today().year):
        raise ValidationError({
            'year_to': mark_safe('<span class="text-danger"> <i class="fa-solid fa-triangle-exclamation"></i>The end year is out of range!</span>'),
        })

#########################



class Widespread_religion(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Widespread_religion")
    order = models.CharField(max_length=10, choices=ORDER_CHOICES)
    widespread_religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related",
                               related_query_name="%(app_label)s_%(class)s",null=True, blank=True)
    degree_of_prevalence = models.CharField(max_length=500, choices=PREVALENCE_CHOICES, null=True, blank=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Widespread_religion'
        verbose_name_plural = 'Widespread_religions'
        ordering = ['order']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "widespread_religion"
    

    def clean_name_dynamic(self):
        if self.order == "1":
            return "Most widespread religion"
        elif self.order == "2":
            return "Second most widespread religion"
        elif self.order == "3":
            return "Third most widespread religion"
        elif self.order == "4":
            return "Fourth most widespread religion"
        elif self.order == "9":
            return "Other minority religion"
        else:
            return "Widespread religion"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Widespread Religion"

    def show_value(self):
        if self.widespread_religion:
            if not self.get_degree_of_prevalence_display():
                return self.get_order_display() + ": " + self.widespread_religion.religion_name
            elif self.get_degree_of_prevalence_display() in ['uncoded', 'unknown']:
                return self.get_order_display() + ": " + self.widespread_religion.religion_name
            else:
                return self.get_order_display() + ": " + self.widespread_religion.religion_name + " (" + self.get_degree_of_prevalence_display()  + ")" 
        else:
            return " - "

    def show_value_from(self):
        if self.widespread_religion:
            return self.widespread_religion
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Religious Landscape"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('widespread_religion-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
    

class Official_religion(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Official_religion")
    coded_value = models.ForeignKey(Religion, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s",null=True, blank=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Official_religion'
        verbose_name_plural = 'Official_religions'

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "official_religion"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Official Religion"

    def show_value(self):
        if self.coded_value:
            return self.coded_value
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Religious Landscape"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('official_religion-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
    

class Elites_religion(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Elites_religion")
    coded_value = models.ForeignKey(Religion, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)s", null=True, blank=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Elites_religion'
        verbose_name_plural = 'Elites_religions'

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "elites_religion"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Elites Religion"

    def show_value(self):
        if self.coded_value:
            return self.coded_value
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Religious Landscape"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('elites_religion-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


############################
class Theo_sync_dif_rel(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Theo_sync_dif_rel")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Theo_sync_dif_rel'
        verbose_name_plural = 'Theological Syncretism of Different Religionss'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "theo_sync_dif_rel"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Theological Syncretism of Different Religions"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Religious Landscape"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('theo_sync_dif_rel-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Sync_rel_pra_ind_beli(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Sync_rel_pra_ind_beli")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Sync_rel_pra_ind_beli'
        verbose_name_plural = 'Syncretism of Religious Practices at the Level of Individual Believerss'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "sync_rel_pra_ind_beli"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Syncretism of Religious Practices at the Level of Individual Believers"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Religious Landscape"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('sync_rel_pra_ind_beli-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Religious_fragmentation(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Religious_fragmentation")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Religious_fragmentation'
        verbose_name_plural = 'Religious Fragmentations'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "religious_fragmentation"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Religious Fragmentation"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Religious Landscape"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('religious_fragmentation-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_vio_freq_rel_grp(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_vio_freq_rel_grp")
    coded_value = models.CharField(max_length=500, choices=FREQUENCY_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_vio_freq_rel_grp'
        verbose_name_plural = 'Frequency of Governmental Violence Against Religious Groupss'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_vio_freq_rel_grp"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Frequency of Governmental Violence Against Religious Groups"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_vio_freq_rel_grp-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_res_pub_wor(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_res_pub_wor")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_res_pub_wor'
        verbose_name_plural = 'Government Restrictions on Public Worships'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_res_pub_wor"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Government Restrictions on Public Worship"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_res_pub_wor-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_res_pub_pros(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_res_pub_pros")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_res_pub_pros'
        verbose_name_plural = 'Government Restrictions on Public Proselytizings'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_res_pub_pros"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Government Restrictions on Public Proselytizing"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_res_pub_pros-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_res_conv(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_res_conv")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_res_conv'
        verbose_name_plural = 'Government Restrictions on Conversions'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_res_conv"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Government Restrictions on Conversion"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_res_conv-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_press_conv(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_press_conv")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_press_conv'
        verbose_name_plural = 'Government Pressure to Converts'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_press_conv"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Government Pressure to Convert"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_press_conv-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_res_prop_own_for_rel_grp(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_res_prop_own_for_rel_grp")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_res_prop_own_for_rel_grp'
        verbose_name_plural = 'Government Restrictions on Property Ownership for Adherents of Any Religious Groups'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_res_prop_own_for_rel_grp"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Government Restrictions on Property Ownership for Adherents of Any Religious Group"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_res_prop_own_for_rel_grp-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Tax_rel_adh_act_ins(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Tax_rel_adh_act_ins")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Tax_rel_adh_act_ins'
        verbose_name_plural = 'Taxes Based on Religious Adherence or on Religious Activities and Institutionss'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "tax_rel_adh_act_ins"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Taxes Based on Religious Adherence or on Religious Activities and Institutions"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('tax_rel_adh_act_ins-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_obl_rel_grp_ofc_reco(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_obl_rel_grp_ofc_reco")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_obl_rel_grp_ofc_reco'
        verbose_name_plural = 'Governmental Obligations for Religious Groups to Apply for Official Recognitions'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_obl_rel_grp_ofc_reco"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Governmental Obligations for Religious Groups to Apply for Official Recognition"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_obl_rel_grp_ofc_reco-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_res_cons_rel_buil(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_res_cons_rel_buil")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_res_cons_rel_buil'
        verbose_name_plural = 'Government Restrictions on Construction of Religious Buildingss'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_res_cons_rel_buil"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Government Restrictions on Construction of Religious Buildings"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_res_cons_rel_buil-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_res_rel_edu(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_res_rel_edu")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_res_rel_edu'
        verbose_name_plural = 'Government Restrictions on Religious Educations'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_res_rel_edu"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Government Restrictions on Religious Education"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_res_rel_edu-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_res_cir_rel_lit(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_res_cir_rel_lit")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_res_cir_rel_lit'
        verbose_name_plural = 'Government Restrictions on Circulation of Religious Literatures'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_res_cir_rel_lit"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Government Restrictions on Circulation of Religious Literature"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_res_cir_rel_lit-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_dis_rel_grp_occ_fun(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_dis_rel_grp_occ_fun")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_dis_rel_grp_occ_fun'
        verbose_name_plural = 'Government Discrimination Against Religious Groups Taking up Certain Occupations or Functionss'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_dis_rel_grp_occ_fun"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Government Discrimination Against Religious Groups Taking up Certain Occupations or Functions"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Government Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_dis_rel_grp_occ_fun-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Soc_vio_freq_rel_grp(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Soc_vio_freq_rel_grp")
    coded_value = models.CharField(max_length=500, choices=FREQUENCY_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Soc_vio_freq_rel_grp'
        verbose_name_plural = 'Frequency of Societal Violence Against Religious Groupss'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "soc_vio_freq_rel_grp"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Frequency of Societal Violence Against Religious Groups"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Societal Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('soc_vio_freq_rel_grp-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Soc_dis_rel_grp_occ_fun(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Soc_dis_rel_grp_occ_fun")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Soc_dis_rel_grp_occ_fun'
        verbose_name_plural = 'Societal Discrimination Against Religious Groups Taking up Certain Occupations or Functionss'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "soc_dis_rel_grp_occ_fun"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Societal Discrimination Against Religious Groups Taking up Certain Occupations or Functions"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Societal Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('soc_dis_rel_grp_occ_fun-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)


class Gov_press_conv_for_aga(SeshatCommon):
    """
    
    """
    name = models.CharField(max_length=100, default="Gov_press_conv_for_aga")
    coded_value = models.CharField(max_length=500, choices=ABSENT_PRESENT_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Gov_press_conv_for_aga'
        verbose_name_plural = 'Societal Pressure to Convert or Against Conversions'
        ordering = ['year_from', 'year_to']

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property, and an alias for the return_citations
            function.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        return return_citations(self)

    def clean(self):
        """
        Validate the year_from and year_to fields of the model instance.

        :noindex:

        Note:
            The method an alias for the clean_times function.

        Returns:
            None

        Raises:
            ValidationError: If the year_from is greater than the year_to.
            ValidationError: If the year_from is out of range.
            ValidationError: If the year_from is earlier than the start year of the corresponding polity.
            ValidationError: If the year_to is later than the end year of the corresponding polity.
            ValidationError: If the year_to is out of range.
        """
        clean_times(self)

    def clean_name(self):
        """
        Return the name of the model instance.

        :noindex:

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.

        Returns:
            str: The name of the model instance.
        """
        return "gov_press_conv_for_aga"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Societal Pressure to Convert or Against Conversion"

    def show_value(self):
        if self.coded_value:
            return self.get_coded_value_display()
        else:
            return " - "

    def show_value_from(self):
        if self.coded_value:
            return self.coded_value
        else:
            return None

    def show_value_to(self):
        return None  

    def subsection(self):
        return "Societal Restrictions"

    def sub_subsection(self):
        return None

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('gov_press_conv_for_aga-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)