
########## Beginning of Model Imports
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

from ..core.models import SeshatCommon, Certainty, Tags, Section, Subsection
from seshat.apps.accounts.models import Seshat_Expert


########## End of Model Imports

########## Beginning of tuple choices for general Models
POLITY_DEGREE_OF_CENTRALIZATION_CHOICES = (
('loose', 'loose'),
('confederated state', 'confederated state'),
('unitary state', 'unitary state'),
('nominal', 'nominal'),
('confederate state', 'confederate state'),
('quasi-polity', 'quasi-polity'),
('suspected unknown', 'suspected unknown'),
('none', 'none'),
('unknown', 'unknown'),
('confederation', 'confederation'),
('polity', 'polity'),
('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'),
('nominal allegiance', 'nominal allegiance'),
('unitary', 'unitary'),
)

POLITY_SUPRAPOLITY_RELATIONS_CHOICES = (
('none', 'none'),
('vassalage', 'vassalage'),
('alliance', 'alliance'),
('nominal allegiance', 'nominal allegiance'),
('suspected unknown', 'suspected unknown'),
('nominal', 'nominal'),
('personal union', 'personal union'),
('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'),
('unknown', 'unknown'),
('Nominal', 'Nominal'),
('Alliance', 'Alliance'),
('uncoded', 'uncoded'),
)

POLITY_LANGUAGE_CHOICES = (
('Pashto', 'Pashto'),
('Persian', 'Persian'),
('Greek', 'Greek'),
('Bactrian', 'Bactrian'),
('Sogdian', 'Sogdian'),
('Pahlavi', 'Pahlavi'),
('Brahmi', 'Brahmi'),
('Kharoshthi', 'Kharoshthi'),
('Tocharian', 'Tocharian'),
('Chinese', 'Chinese'),
('archaic Chinese', 'archaic Chinese'),
('Xiangxi', 'Xiangxi'),
('Qiandong', 'Qiandong'),
('Chuanqiandian', 'Chuanqiandian'),
('Hmong-Mien', 'Hmong-Mien'),
('Hmongic', 'Hmongic'),
('Middle Chinese', 'Middle Chinese'),
('Jurchen', 'Jurchen'),
('Khitan', 'Khitan'),
('Xianbei', 'Xianbei'),
('Manchu language', 'Manchu language'),
('Mongolian language', 'Mongolian language'),
('Atanque', 'Atanque'),
('Shuar', 'Shuar'),
('Arabic', 'Arabic'),
('suspected unknown', 'suspected unknown'),
('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'),
('Demotic', 'Demotic'),
('Ancient Egyptian', 'Ancient Egyptian'),
('Late Egyptian', 'Late Egyptian'),
('demotic Egyptian', 'demotic Egyptian'),
('Castilian Spanish', 'Castilian Spanish'),
('Chuukese', 'Chuukese'),
('French', 'French'),
('Langues dOil', 'Langues dOil'),
('Occitan', 'Occitan'),
('Latin', 'Latin'),
('Old Frankish', 'Old Frankish'),
('Germanic', 'Germanic'),
('Gallic', 'Gallic'),
('Gaulish', 'Gaulish'),
('English', 'English'),
('Akan', 'Akan'),
('Twi', 'Twi'),
('Doric Greek', 'Doric Greek'),
('Minoan', 'Minoan'),
('Early Greek', 'Early Greek'),
('Eteocretan', 'Eteocretan'),
('Old Hawaiian', 'Old Hawaiian'),
('Hawaiian', 'Hawaiian'),
('Iban', 'Iban'),
('Sanskrit', 'Sanskrit'),
('Old Javanese', 'Old Javanese'),
('Middle Javanese', 'Middle Javanese'),
('Javanese', 'Javanese'),
('Canaanite', 'Canaanite'),
('Aramaic', 'Aramaic'),
('Hebrew', 'Hebrew'),
('Kannada', 'Kannada'),
('Urdu', 'Urdu'),
('A’chik', 'A’chik'),
('Prakrit', 'Prakrit'),
('Telugu', 'Telugu'),
('Tamil', 'Tamil'),
('Akkadian', 'Akkadian'),
('Sumerian', 'Sumerian'),
('Amorite', 'Amorite'),
('Old Babylonian', 'Old Babylonian'),
('Mesopotamian Religions', 'Mesopotamian Religions'),
('Old Persian', 'Old Persian'),
('Elamite', 'Elamite'),
('Egyptian', 'Egyptian'),
('Old Elamite', 'Old Elamite'),
('Mongolian', 'Mongolian'),
('native Iranian languages', 'native Iranian languages'),
('Turkic', 'Turkic'),
('Turkish', 'Turkish'),
('Babylonian', 'Babylonian'),
('Hurrian', 'Hurrian'),
('Proto-Elamite', 'Proto-Elamite'),
('Old Norse', 'Old Norse'),
('Italian', 'Italian'),
('Middle Japanese', 'Middle Japanese'),
('Old Japanese', 'Old Japanese'),
('Late Old Japanese', 'Late Old Japanese'),
('Japanese', 'Japanese'),
('Early Modern Japanese', 'Early Modern Japanese'),
('Old Turkic', 'Old Turkic'),
('Iranian', 'Iranian'),
('Old Khmer', 'Old Khmer'),
('Mon', 'Mon'),
('Tai', 'Tai'),
('Khmer', 'Khmer'),
('Pali', 'Pali'),
('Phoenician', 'Phoenician'),
('Berber', 'Berber'),
('Spanish', 'Spanish'),
('Portuguese', 'Portuguese'),
('Bambara', 'Bambara'),
('Mande', 'Mande'),
('Songhay', 'Songhay'),
('Russian', 'Russian'),
('Georgian', 'Georgian'),
('Armenian', 'Armenian'),
('Kereid', 'Kereid'),
('Tatar', 'Tatar'),
('Naimans', 'Naimans'),
('Khalkha', 'Khalkha'),
('Rouran', 'Rouran'),
('Xiongnu', 'Xiongnu'),
('Oirat', 'Oirat'),
('Zapotec', 'Zapotec'),
('Icelandic', 'Icelandic'),
('Aymara', 'Aymara'),
('Puquina', 'Puquina'),
('Quechua', 'Quechua'),
('Orokaiva', 'Orokaiva'),
('unknown', 'unknown'),
('Sindhi', 'Sindhi'),
('Punjabi', 'Punjabi'),
('Sakha (Yakut)', 'Sakha (Yakut)'),
('Merotic', 'Merotic'),
('Coptic', 'Coptic'),
('Thai', 'Thai'),
('Proto-Indo-European language', 'Proto-Indo-European language'),
('Nesite', 'Nesite'),
('Luwian', 'Luwian'),
('Hattic', 'Hattic'),
('Hittite', 'Hittite'),
('Old Assyrian dialect of Akkadian', 'Old Assyrian dialect of Akkadian'),
('Indo-European language', 'Indo-European language'),
('Lydian', 'Lydian'),
('Ottoman Turkish', 'Ottoman Turkish'),
('Phrygian', 'Phrygian'),
('Miami Illinois', 'Miami Illinois'),
('Cayuga', 'Cayuga'),
('Mohawk', 'Mohawk'),
('Oneida', 'Oneida'),
('Onondaga', 'Onondaga'),
('Seneca', 'Seneca'),
('Tuscarora', 'Tuscarora'),
('Middle Mongolian', 'Middle Mongolian'),
('Ancient Iranian', 'Ancient Iranian'),
('Chagatai Turkish', 'Chagatai Turkish'),
('Sabaic', 'Sabaic'),
('Mainic', 'Mainic'),
('Qatabanic', 'Qatabanic'),
('Hadramawtic', 'Hadramawtic'),
('Old Arabic', 'Old Arabic'),
)

POLITY_LINGUISTIC_FAMILY_CHOICES = (
('Indo-European', 'Indo-European'),
('Sino-Tibetan', 'Sino-Tibetan'),
('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'),
('Tungusic', 'Tungusic'),
('Altaic', 'Altaic'),
('Mongolic', 'Mongolic'),
('Chibcha', 'Chibcha'),
('Chicham', 'Chicham'),
('Afro-Asiatic', 'Afro-Asiatic'),
('Oceanic-Austronesian', 'Oceanic-Austronesian'),
('Celtic', 'Celtic'),
('Niger-Congo', 'Niger-Congo'),
('Kwa', 'Kwa'),
('Hamito-Semitic', 'Hamito-Semitic'),
('Austronesian', 'Austronesian'),
('Malayo-Polynesian', 'Malayo-Polynesian'),
('Semitic', 'Semitic'),
('Indo-Iranian', 'Indo-Iranian'),
('Dravidian', 'Dravidian'),
('isolate language', 'isolate language'),
('West Semetic', 'West Semetic'),
('isolate', 'isolate'),
('suspected unknown', 'suspected unknown'),
('language isolate', 'language isolate'),
('none', 'none'),
('Germanic', 'Germanic'),
('Japonic', 'Japonic'),
('Turkic', 'Turkic'),
('Austro-Asiatic, Mon-Khmer', 'Austro-Asiatic, Mon-Khmer'),
('Austro-Asiatic', 'Austro-Asiatic'),
('unknown', 'unknown'),
('Mande', 'Mande'),
('Songhay', 'Songhay'),
('Oghuz', 'Oghuz'),
('Kartvelian', 'Kartvelian'),
('Manchu-Tungusic', 'Manchu-Tungusic'),
('Proto-Mongolic', 'Proto-Mongolic'),
('Otomanguean', 'Otomanguean'),
('Proto-Otomanguean', 'Proto-Otomanguean'),
('Mixe-Zoquean', 'Mixe-Zoquean'),
('Aymaran', 'Aymaran'),
('Quechuan', 'Quechuan'),
('Papuan Languages', 'Papuan Languages'),
('Tai-Kadai', 'Tai-Kadai'),
('Algonquian', 'Algonquian'),
('Iroquois', 'Iroquois'),
('Iranian', 'Iranian'),
)

POLITY_LANGUAGE_GENUS_CHOICES = (
('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'),
('Afro-Asiatic', 'Afro-Asiatic'),
('Indo-European', 'Indo-European'),
('suspected unknown', 'suspected unknown'),
)

POLITY_RELIGION_GENUS_CHOICES = (
('Zoroastrianism', 'Zoroastrianism'),
('Graeco-Bactrian Religions', 'Graeco-Bactrian Religions'),
('Buddhism', 'Buddhism'),
('Christianity', 'Christianity'),
('Islam', 'Islam'),
('Mongolian Shamanism', 'Mongolian Shamanism'),
('Hittite Religions', 'Hittite Religions'),
('Ismaili', 'Ismaili'),
('Lydian Religions', 'Lydian Religions'),
('Chinese State Religion', 'Chinese State Religion'),
('Egyptian Religions', 'Egyptian Religions'),
('Ancient Iranian Religions', 'Ancient Iranian Religions'),
('Hellenistic Religions', 'Hellenistic Religions'),
('Hephthalite Religions', 'Hephthalite Religions'),
('Manichaeism', 'Manichaeism'),
('Ancient East Asian Religion', 'Ancient East Asian Religion'),
('Jain Traditions', 'Jain Traditions'),
('Xiongnu Religions', 'Xiongnu Religions'),
('Roman State Religions', 'Roman State Religions'),
('Shinto', 'Shinto'),
('Phrygian Religions', 'Phrygian Religions'),
('Mesopotamian Religions', 'Mesopotamian Religions'),
('Hinduism', 'Hinduism'),
('Ancient Javanese Religions', 'Ancient Javanese Religions'),
('Confucianism', 'Confucianism'),
)

POLITY_RELIGION_FAMILY_CHOICES = (
('Saivist Traditions', 'Saivist Traditions'),
('Assyrian Religions', 'Assyrian Religions'),
('Republican Religions', 'Republican Religions'),
('Imperial Confucian Traditions', 'Imperial Confucian Traditions'),
('Shii', 'Shii'),
('Bhagavatist Traditions', 'Bhagavatist Traditions'),
('Sunni', 'Sunni'),
('Vedist Traditions', 'Vedist Traditions'),
('Saivist', 'Saivist'),
('Islam', 'Islam'),
('Chinese Folk Religion', 'Chinese Folk Religion'),
('Semitic', 'Semitic'),
('Vaisnava Traditions', 'Vaisnava Traditions'),
('Ptolemaic Religion', 'Ptolemaic Religion'),
('Vedic Traditions', 'Vedic Traditions'),
('Japanese Buddhism', 'Japanese Buddhism'),
('Orthodox', 'Orthodox'),
('Vaishnava Traditions', 'Vaishnava Traditions'),
('Shang Religion', 'Shang Religion'),
('Atenism', 'Atenism'),
('Mahayana', 'Mahayana'),
('suspected unknown', 'suspected unknown'),
('Japanese State Shinto', 'Japanese State Shinto'),
('Saiva Traditions', 'Saiva Traditions'),
('Sufi', 'Sufi'),
('Chinese Buddhist Traditions', 'Chinese Buddhist Traditions'),
('Arian', 'Arian'),
('Shia', 'Shia'),
('Catholic', 'Catholic'),
('Western Zhou Religion', 'Western Zhou Religion'),
('Imperial Cult', 'Imperial Cult'),
('Theravada', 'Theravada'),
('Seleucid Religion', 'Seleucid Religion'),
)

POLITY_RELIGION_CHOICES = (
('Islam', 'Islam'),
('Shadhil', 'Shadhil'),
('Karrami', 'Karrami'),
('Hanafi', 'Hanafi'),
('Mevlevi', 'Mevlevi'),
('Ismaili', 'Ismaili'),
('Shafii', 'Shafii'),
('Shia', 'Shia'),
('Twelver', 'Twelver'),
('Byzantine Orthodox', 'Byzantine Orthodox'),
('Bektasi', 'Bektasi'),
('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'),
('Sunni', 'Sunni'),
('Roman Catholic', 'Roman Catholic'),
)

POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES = (
('continuity', 'continuity'),
('elite migration', 'elite migration'),
('cultural assimilation', 'cultural assimilation'),
('continuation', 'continuation'),
('indigenous revolt', 'indigenous revolt'),
('replacement', 'replacement'),
('population migration', 'population migration'),
('hostile', 'hostile'),
('disruption/continuity', 'disruption/continuity'),
('continuity/discontinuity', 'continuity/discontinuity'),
('NO_VALUE_ON_WIKI', 'NO_VALUE_ON_WIKI'),
('suspected unknown', 'suspected unknown'),
('vassalage', 'vassalage'),
('not applicable', 'not applicable'),
)


########## TUPLE CHOICES THAT ARE THE SAME 
POLITY_ALTERNATE_RELIGION_GENUS_CHOICES = POLITY_RELIGION_GENUS_CHOICES  
POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES = POLITY_RELIGION_FAMILY_CHOICES  
POLITY_ALTERNATE_RELIGION_CHOICES = POLITY_RELIGION_CHOICES  

########## END of tuple choices for general Models

########## Beginning of Function Definitions for General (Vars) Models

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
            'year_from': 'The start year is bigger than the end year!',
        })
    if self.year_from and (self.year_from < -10000 or self.year_from > date.today().year):
        raise ValidationError({
            'year_from': 'The start year is out of range!',
        })
    if self.year_from and (self.year_from < self.polity.start_year):
        raise ValidationError({
            'year_from': 'The start year is earlier than the start year of the corresponding polity!',
        })
    if self.year_to and (self.year_to > self.polity.end_year):
        raise ValidationError({
            'year_to': 'The end year is later than the end year of the corresponding polity!',
        })
    if self.year_to and (self.year_to < -10000 or self.year_to > date.today().year):
        raise ValidationError({
            'year_to': 'The end year is out of range!',
        })
    if not self.year_to and not self.year_from:
        raise ValidationError({
            'year_from': 'You need to enter at least one year (From or To)',
        })

########## End of Function Definitions for General (Vars) Models

########## Beginning of class Definitions for general Models

class Polity_research_assistant(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_research_assistant")
    polity_ra = models.ForeignKey(Seshat_Expert, on_delete=models.SET_NULL, null=True, related_name="seshat_research_assistant")

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_research_assistant'
        verbose_name_plural = 'Polity_research_assistants'
        ordering = ['polity_ra', 'year_from', 'year_to']

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
        return "polity_research_assistant"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Research Assistant"
    
    def show_value(self):
        if self.polity_ra:
            return self.polity_ra
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_research_assistant-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_utm_zone(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_utm_zone")
    utm_zone = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_utm_zone'
        verbose_name_plural = 'Polity_utm_zones'
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
        return "polity_utm_zone"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Utm Zone"
    
    def show_value(self):
        if self.utm_zone:
            return self.utm_zone
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_utm_zone-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_original_name(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_original_name")
    original_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_original_name'
        verbose_name_plural = 'Polity_original_names'
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
        return "polity_original_name"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Original Name"
    
    def show_value(self):
        if self.original_name:
            return self.original_name
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_original_name-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_alternative_name(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_alternative_name")
    alternative_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_alternative_name'
        verbose_name_plural = 'Polity_alternative_names'
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
        return "polity_alternative_name"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Alternative Name"
    
    def show_value(self):
        if self.alternative_name:
            return self.alternative_name
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_alternative_name-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_peak_years(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_peak_years")
    peak_year_from = models.IntegerField(blank=True, null=True)
    peak_year_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_peak_years'
        verbose_name_plural = 'Polity_peak_years'
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
        return "polity_peak_years"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Peak Years"
    
    def show_value(self):
        if self.peak_year_from == self.peak_year_to:
            if self.peak_year_from < 0:
                return f'{abs(self.peak_year_from):,}' + " BCE" 
            else:
                return f'{abs(self.peak_year_from):,}' + " CE" 
        elif self.peak_year_to == None:
            if self.peak_year_from < 0:
                return f'{abs(self.peak_year_from):,}' + " BCE" 
            else:
                return f'{abs(self.peak_year_from):,}' + " CE" 
        elif self.peak_year_to == None and  self.peak_year_from == None:
            return " - " 
        else:
            if self.peak_year_from < 0 and self.peak_year_to < 0:
                return "[" + f'{abs(self.peak_year_from):,}' + " BCE"  + " ➜ " + f'{abs(self.peak_year_to):,}' + " BCE"  + "]"
            elif  self.peak_year_from < 0 and self.peak_year_to >= 0:
                return "[" + f'{abs(self.peak_year_from):,}' + " BCE"  + " ➜ " + f'{abs(self.peak_year_to):,}' + " CE"  + "]"
            else:
                return "[" + f'{abs(self.peak_year_from):,}' + " CE"  + " ➜ " + f'{abs(self.peak_year_to):,}' + " CE" + "]"
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_peak_years-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_duration(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_duration")
    polity_year_from = models.IntegerField(blank=True, null=True)
    polity_year_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_duration'
        verbose_name_plural = 'Polity_durations'
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
        return "polity_duration"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Duration"
    
    def show_value(self):
        if self.polity_year_from == self.polity_year_to:
            if self.polity_year_from < 0:
                return f'{abs(self.polity_year_from):,}' + " BCE" 
            else:
                return f'{abs(self.polity_year_from):,}' + " CE" 
        elif self.polity_year_to == None:
            if self.polity_year_from < 0:
                return f'{abs(self.polity_year_from):,}' + " BCE" 
            else:
                return f'{abs(self.polity_year_from):,}' + " CE" 
        elif self.polity_year_to == None and  self.polity_year_from == None:
            return " - " 
        else:
            if self.polity_year_from < 0 and self.polity_year_to < 0:
                return "[" + f'{abs(self.polity_year_from):,}' + " BCE"  + " ➜ " + f'{abs(self.polity_year_to):,}' + " BCE"  + "]"
            elif  self.polity_year_from < 0 and self.polity_year_to >= 0:
                return "[" + f'{abs(self.polity_year_from):,}' + " BCE"  + " ➜ " + f'{abs(self.polity_year_to):,}' + " CE"  + "]"
            else:
                return "[" + f'{abs(self.polity_year_from):,}' + " CE"  + " ➜ " + f'{abs(self.polity_year_to):,}' + " CE" + "]"
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_duration-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_degree_of_centralization(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_degree_of_centralization")
    degree_of_centralization = models.CharField(max_length=500, choices=POLITY_DEGREE_OF_CENTRALIZATION_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_degree_of_centralization'
        verbose_name_plural = 'Polity_degree_of_centralizations'
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
        return "polity_degree_of_centralization"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Degree of Centralization"
    
    def show_value(self):
        if self.degree_of_centralization:
            return self.get_degree_of_centralization_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_degree_of_centralization-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_suprapolity_relations(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_suprapolity_relations")
    supra_polity_relations = models.CharField(max_length=500, choices=POLITY_SUPRAPOLITY_RELATIONS_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_suprapolity_relations'
        verbose_name_plural = 'Polity_suprapolity_relations'
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
        return "polity_suprapolity_relations"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Suprapolity Relations"
    
    def show_value(self):
        if self.supra_polity_relations:
            return self.get_supra_polity_relations_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_suprapolity_relations-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_capital(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_capital")
    capital = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_capital'
        verbose_name_plural = 'Polity_capitals'
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
        return "polity_capital"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Capital"
    
    def show_value(self):
        if self.capital:
            return self.capital
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_capital-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_language(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_language")
    language = models.CharField(max_length=500, choices=POLITY_LANGUAGE_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_language'
        verbose_name_plural = 'Polity_languages'
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
        return "polity_language"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Language"
    
    def show_value(self):
        if self.language:
            return self.get_language_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_language-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_linguistic_family(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_linguistic_family")
    linguistic_family = models.CharField(max_length=500, choices=POLITY_LINGUISTIC_FAMILY_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_linguistic_family'
        verbose_name_plural = 'Polity_linguistic_families'
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
        return "polity_linguistic_family"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Linguistic Family"
    
    def show_value(self):
        if self.linguistic_family:
            return self.get_linguistic_family_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_linguistic_family-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_language_genus(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_language_genus")
    language_genus = models.CharField(max_length=500, choices=POLITY_LANGUAGE_GENUS_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_language_genus'
        verbose_name_plural = 'Polity_language_genus'
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
        return "polity_language_genus"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Language Genus"
    
    def show_value(self):
        if self.language_genus:
            return self.get_language_genus_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_language_genus-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_religion_genus(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_religion_genus")
    religion_genus = models.CharField(max_length=500, choices=POLITY_RELIGION_GENUS_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_religion_genus'
        verbose_name_plural = 'Polity_religion_genus'
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
        return "polity_religion_genus"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Religion Genus"
    
    def show_value(self):
        if self.religion_genus:
            return self.get_religion_genus_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_religion_genus-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_religion_family(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_religion_family")
    religion_family = models.CharField(max_length=500, choices=POLITY_RELIGION_FAMILY_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_religion_family'
        verbose_name_plural = 'Polity_religion_families'
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
        return "polity_religion_family"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Religion Family"
    
    def show_value(self):
        if self.religion_family:
            return self.get_religion_family_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_religion_family-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_religion(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_religion")
    religion = models.CharField(max_length=500, choices=POLITY_RELIGION_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_religion'
        verbose_name_plural = 'Polity_religions'
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
        return "polity_religion"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Religion"
    
    def show_value(self):
        if self.religion:
            return self.get_religion_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_religion-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_relationship_to_preceding_entity(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_relationship_to_preceding_entity")
    relationship_to_preceding_entity = models.CharField(max_length=500, choices=POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_relationship_to_preceding_entity'
        verbose_name_plural = 'Polity_relationship_to_preceding_entities'
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
        return "polity_relationship_to_preceding_entity"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Relationship to Preceding Entity"
    
    def show_value(self):
        if self.relationship_to_preceding_entity:
            return self.get_relationship_to_preceding_entity_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_relationship_to_preceding_entity-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_preceding_entity(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_preceding_entity")
    preceding_entity = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_preceding_entity'
        verbose_name_plural = 'Polity_preceding_entities'
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
        return "polity_preceding_entity"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Preceding Entity"
    
    def show_value(self):
        if self.preceding_entity:
            return self.preceding_entity
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_preceding_entity-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_succeeding_entity(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_succeeding_entity")
    succeeding_entity = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_succeeding_entity'
        verbose_name_plural = 'Polity_succeeding_entities'
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
        return "polity_succeeding_entity"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Succeeding Entity"
    
    def show_value(self):
        if self.succeeding_entity:
            return self.succeeding_entity
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_succeeding_entity-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_supracultural_entity(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_supracultural_entity")
    supracultural_entity = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_supracultural_entity'
        verbose_name_plural = 'Polity_supracultural_entities'
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
        return "polity_supracultural_entity"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Supracultural Entity"
    
    def show_value(self):
        if self.supracultural_entity:
            return self.supracultural_entity
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_supracultural_entity-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_scale_of_supracultural_interaction(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_scale_of_supracultural_interaction")
    scale_from = models.IntegerField(blank=True, null=True)
    scale_to = models.IntegerField(blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_scale_of_supracultural_interaction'
        verbose_name_plural = 'Polity_scale_of_supracultural_interactions'
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
        return "polity_scale_of_supracultural_interaction"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Scale of Supracultural Interaction"
    
    def show_value(self):
        if self.scale_from and self.scale_to and self.scale_to == self.scale_from:
            return self.scale_from
        elif self.scale_from and self.scale_to:
            return f"[{self.scale_from:,} to {self.scale_to:,}]"
        elif self.scale_from:
            return f"[{self.scale_from:,}"
        elif self.scale_to:
            return f"[{self.scale_to:,}"
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_scale_of_supracultural_interaction-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_alternate_religion_genus(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_alternate_religion_genus")
    alternate_religion_genus = models.CharField(max_length=500, choices=POLITY_ALTERNATE_RELIGION_GENUS_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_alternate_religion_genus'
        verbose_name_plural = 'Polity_alternate_religion_genus'
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
        return "polity_alternate_religion_genus"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Alternate Religion Genus"
    
    def show_value(self):
        if self.alternate_religion_genus:
            return self.get_alternate_religion_genus_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_alternate_religion_genus-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_alternate_religion_family(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_alternate_religion_family")
    alternate_religion_family = models.CharField(max_length=500, choices=POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_alternate_religion_family'
        verbose_name_plural = 'Polity_alternate_religion_families'
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
        return "polity_alternate_religion_family"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Alternate Religion Family"
    
    def show_value(self):
        if self.alternate_religion_family:
            return self.get_alternate_religion_family_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_alternate_religion_family-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_alternate_religion(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_alternate_religion")
    alternate_religion = models.CharField(max_length=500, choices=POLITY_ALTERNATE_RELIGION_CHOICES)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_alternate_religion'
        verbose_name_plural = 'Polity_alternate_religions'
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
        return "polity_alternate_religion"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Alternate Religion"
    
    def show_value(self):
        if self.alternate_religion:
            return self.get_alternate_religion_display()
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_alternate_religion-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_expert(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_expert")
    expert = models.ForeignKey(Seshat_Expert, on_delete=models.SET_NULL, null=True, related_name="seshat_expert")

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_expert'
        verbose_name_plural = 'Polity_experts'
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
        return "polity_expert"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Expert"
    
    def show_value(self):
        if self.expert:
            return self.expert
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_expert-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_editor(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_editor")
    editor = models.ForeignKey(Seshat_Expert, on_delete=models.SET_NULL, null=True, related_name="seshat_editor")

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_editor'
        verbose_name_plural = 'Polity_editors'
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
        return "polity_editor"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Editor"
    
    def show_value(self):
        if self.editor:
            return self.editor
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_editor-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
class Polity_religious_tradition(SeshatCommon):
    name = models.CharField(max_length=100, default="Polity_religious_tradition")
    religious_tradition = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """
        verbose_name = 'Polity_religious_tradition'
        verbose_name_plural = 'Polity_religious_traditions'
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
        return "polity_religious_tradition"

    def clean_name_spaced(self):
        """
        Return the name of the model instance with spaces.

        Note:
            TODO This method should probably just be an attribute set on the
            model instead.
        """
        return "Polity Religious Tradition"
    
    def show_value(self):
        if self.religious_tradition:
            return self.religious_tradition
        else:
            return " - "
        
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse('polity_religious_tradition-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return call_my_name(self)
             
        
########## END of class Definitions for general Models
