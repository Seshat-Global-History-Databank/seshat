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
from seshat.apps.core.models import Polity, Tags, Prec_met_instance

from seshat.apps.sc.models import ABSENT_PRESENT_CHOICES, clean_times, return_citations, call_my_name




def template_display_table_value(self) -> str:
    rows = []

    if self.place_of_provenance_pol:
        all_pols_connected =[]
        all_pols_connected_str=""
        for pol in self.place_of_provenance_pol.all():

            polity_url = reverse('polity-detail-main', args=[pol.id]) 
            a_str = f"""
<a href='{polity_url}'>{pol.long_name}</a>  
            """
            
            all_pols_connected.append(a_str)
            all_pols_connected_str =  '<span style="display: block; width: 5px;"></span>'.join(all_pols_connected)
    else:
        all_pols_connected_str=""

    if self.place_of_provenance_str:
        places_str = self.place_of_provenance_str.replace(';',  '<span style="display: block; width: 5px;"></span>')
    else:
        places_str = ""
    # Conditionally add rows if values are not None
    if self.coded_value:
        if self.coded_value in ['present']:
            my_color = 'teal'
        elif self.coded_value in ['absent']:
            my_color = 'maroon'
        elif self.tag in ['SSP']:
            my_color = 'hotpink'
        else:
            my_color = 'darkgray'

        if self.tag in ["TRS", "UND", None]:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-0 pe-4" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                        {self.clean_name_spaced()}
                    </td>
                    <td class="ps-1 align-right" style="padding-right: 8px; text-align: right; color: #555;">

        <span class="badge bg-success-light small-knopf text-dark" style="
        font-size: 16px;padding-left:5px;padding-right:5px;padding-top:3px;padding-bottom:3px;margin:0px; background: #fffdf2; color: {my_color}; border: 1px solid {my_color};">
        {self.get_coded_value_display()}</span> 
                        
                    </td>
                </tr>
            """)
        else:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-0 pe-4" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                        {self.clean_name_spaced()}
                    </td>
                    <td class="ps-1 align-right" style="padding-right: 8px; text-align: right; color: #555;">

        <span class="badge bg-success-light small-knopf text-dark" style="
        font-size: 16px;padding-left:5px;padding-right:5px;padding-top:3px;padding-bottom:3px;margin:0px;  background: #fffdf2; color: {my_color}; border: 1px solid {my_color};">
        
                    {self.get_tag_display()}
                    {self.get_coded_value_display()}
                    
                    </span> 

                    
                    </td>
                </tr>
            """)

    if self.place_of_provenance_str and all_pols_connected_str:
        rows.append(f"""
            <tr style="border-bottom:1px solid #FFFDF2;">
                <td class="ps-0 pe-4" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                    Place(s) of Provenance
                </td>
                <td class="ps-1 align-right fw-normal" style="padding-right: 8px; text-align: right; color: #555;">
                    <span>    
                   {all_pols_connected_str} <span style="display: block; width: 5px;"></span>{places_str} 
                   </span>
                </td>
            </tr>
        """)
    elif all_pols_connected_str:
        rows.append(f"""
            <tr style="border-bottom:1px solid #FFFDF2;">
                <td class="ps-0 pe-4" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                    Place(s) of Provenance
                </td>
                <td class="ps-1 align-right fw-normal" style="padding-right: 8px; text-align: right; color: #555;">
                <span>    
                   {all_pols_connected_str}
                </span>    

                </td>
            </tr>
        """)
    elif self.place_of_provenance_str:
        rows.append(f"""
            <tr style="border-bottom:1px solid #FFFDF2;">
                <td class="ps-0 pe-4" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                    Place(s) of Provenance
                </td>
                <td class="ps-1 align-right fw-normal" style="padding-right: 8px; text-align: right; color: #555;">
                    <span>    

                   {places_str}
                    </span>    
                </td>
            </tr>
        """)

    if self.ruler_consumption:
        if self.ruler_consumption in ['present']:
            my_cons_color = 'teal'
        elif self.ruler_consumption in ['absent']:
            my_cons_color = 'maroon'
        elif self.ruler_consumption_tag in ['SSP']:
            my_cons_color = 'hotpink'
        else:
            my_cons_color = 'darkgray'

        if self.ruler_consumption_tag in ["TRS", "UND", None]:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-0 pe-4 fw-normal" style="padding-right: 8px; text-align: left; color: #888;">
                        Consumption by <b> Ruler</b>
                    </td>
                    <td class="ps-1 align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        <span class="badge bg-success-light small-knopf text-dark" style="font-size: 16px;padding-left:5px;padding-right:5px;padding-top:3px;padding-bottom:3px;margin:0px; background: #fffdf2; color: {my_cons_color}; border: 1px solid {my_cons_color};">
                        {self.get_ruler_consumption_display()}
                        </span> 

                    </td>
                </tr>
            """)
        else:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-0 pe-4 fw-normal" style="padding-right: 8px; text-align: left; color: #888;">
                        Consumption by <b> Ruler</b>
                    </td>
                    <td class="ps-1 align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        <span class="badge bg-success-light small-knopf text-dark" style="font-size: 16px;padding-left:5px;padding-right:5px;padding-top:3px;padding-bottom:3px;margin:0px; background: #fffdf2; color: {my_cons_color}; border: 1px solid {my_cons_color};">
                        {self.get_ruler_consumption_tag_display()}
                        {self.get_ruler_consumption_display()}

                        </span> 

                    </td>
                </tr>
            """)

    if self.elite_consumption:
        if self.elite_consumption in ['present']:
            my_cons_color = 'teal'
        elif self.elite_consumption in ['absent']:
            my_cons_color = 'maroon'
        elif self.elite_consumption_tag in ['SSP']:
            my_cons_color = 'hotpink'
        else:
            my_cons_color = 'darkgray'

        if self.elite_consumption_tag in ["TRS", "UND", None]:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-0 pe-4 fw-normal" style="padding-right: 8px; text-align: left; color: #888;">
                        Consumption by <b> Elite</b>
                    </td>
                    <td class="ps-1 align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        <span class="badge bg-success-light small-knopf text-dark" style="font-size: 16px;padding-left:5px;padding-right:5px;padding-top:3px;padding-bottom:3px;margin:0px; background: #fffdf2; color: {my_cons_color}; border: 1px solid {my_cons_color};">
                        {self.get_elite_consumption_display()}
                        </span> 

                    </td>
                </tr>
            """)
        else:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-0 pe-4 fw-normal" style="padding-right: 8px; text-align: left; color: #888;">
                        Consumption by <b> Elite</b>
                    </td>
                    <td class="ps-1 align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        <span class="badge bg-success-light small-knopf text-dark" style="font-size: 16px;padding-left:5px;padding-right:5px;padding-top:3px;padding-bottom:3px;margin:0px; background: #fffdf2; color: {my_cons_color}; border: 1px solid {my_cons_color};">
                        {self.get_elite_consumption_tag_display()}
                        {self.get_elite_consumption_display()}

                        </span> 

                    </td>
                </tr>
            """)

    if self.common_people_consumption:
        if self.common_people_consumption in ['present']:
            my_cons_color = 'teal'
        elif self.common_people_consumption in ['absent']:
            my_cons_color = 'maroon'
        elif self.common_people_consumption_tag in ['SSP']:
            my_cons_color = 'hotpink'
        else:
            my_cons_color = 'darkgray'

        if self.common_people_consumption_tag in ["TRS", "UND", None]:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-0 pe-4 fw-normal" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                        Consumption by <b> Common People</b>
                    </td>
                    <td class="ps-1 align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        <span class="badge bg-success-light small-knopf text-dark" style="font-size: 16px;padding-left:5px;padding-right:5px;padding-top:3px;padding-bottom:3px;margin:0px; background: #fffdf2; color: {my_cons_color}; border: 1px solid {my_cons_color};">
                        {self.get_common_people_consumption_display()}
                        </span> 

                    </td>
                </tr>
            """)
        else:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-0 pe-4 fw-normal" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                        Consumption by <b> Common People</b>
                    </td>
                    <td class="ps-1 align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        <span class="badge bg-success-light small-knopf text-dark" style="font-size: 16px;padding-left:5px;padding-right:5px;padding-top:3px;padding-bottom:3px;margin:0px; background: #fffdf2; color: {my_cons_color}; border: 1px solid {my_cons_color};">
                        {self.get_common_people_consumption_tag_display()}
                        {self.get_common_people_consumption_display()}

                        </span> 

                    </td>
                </tr>
            """)

    # Combine rows into a table
    table_html = f"""
        <table class="table p-0" style="width: 100%; border-collapse: collapse; border: none; margin: 0px;">
        <tbody class="p-0">
            {''.join(rows)}
        </tbody>

        </table>
    """
    return table_html



class LuxAttributes(models.Model):
    """
    Abstract base class for consumption-related attributes.
    """
    coded_value = models.CharField(max_length=50, choices=ABSENT_PRESENT_CHOICES)
    #which_metals = models.ManyToManyField(Prec_met_instance, related_name="%(app_label)s_%(class)s_related_metals", related_query_name="%(app_label)s_%(class)ss", blank=True)
    place_of_provenance_pol = models.ManyToManyField(Polity, related_name="%(app_label)s_%(class)s_related_places", related_query_name="%(app_label)s_%(class)ss", blank=True)
    place_of_provenance_str = models.CharField(max_length=500, blank=True, null=True)
    ruler_consumption = models.CharField(max_length=50, choices=ABSENT_PRESENT_CHOICES, blank=True, null=True)
    ruler_consumption_tag = models.CharField(max_length=50, choices=Tags, blank=True, null=True)
    elite_consumption = models.CharField(max_length=50, choices=ABSENT_PRESENT_CHOICES, blank=True, null=True)
    elite_consumption_tag = models.CharField(max_length=50, choices=Tags, blank=True, null=True)
    common_people_consumption = models.CharField(max_length=50, choices=ABSENT_PRESENT_CHOICES, blank=True, null=True)
    common_people_consumption_tag = models.CharField(max_length=50, choices=Tags, blank=True, null=True)

    class Meta:
        abstract = True

    
    def all_places(self):
        return ', '.join([str(place) for place in self.place_of_provenance_pol.all()])
    
    def show_value(self) -> str:
        return template_display_table_value(self)
    
    def display_table_value(self) -> str:
        return template_display_table_value(self)
    
    def __str__(self) -> str:
        return f'{self.coded_value} in {self.all_places()} and {self.place_of_provenance_str}.'




class Precious_metal(SeshatCommon):
    name = models.CharField(max_length=100, default="precious_metal")
    # this will use the normal tag for confidence
    coded_value = models.CharField(max_length=50, choices=ABSENT_PRESENT_CHOICES)
    #which_metals = models.ManyToManyField(Prec_met_instance, related_name="%(app_label)s_%(class)s_related_metals", related_query_name="%(app_label)s_%(class)ss", blank=True)
    place_of_provenance_pol = models.ManyToManyField(Polity, related_name="%(app_label)s_%(class)s_related_places", related_query_name="%(app_label)s_%(class)ss", blank=True)
    place_of_provenance_str = models.CharField(max_length=500, blank=True, null=True)
    ruler_consumption = models.CharField(max_length=50, choices=ABSENT_PRESENT_CHOICES, blank=True)
    ruler_consumption_tag = models.CharField(max_length=50, choices=Tags, blank=True)
    elite_consumption = models.CharField(max_length=50, choices=ABSENT_PRESENT_CHOICES, blank=True)
    elite_consumption_tag = models.CharField(max_length=50, choices=Tags, blank=True)
    common_people_consumption = models.CharField(max_length=50, choices=ABSENT_PRESENT_CHOICES, blank=True)
    common_people_consumption_tag = models.CharField(max_length=50, choices=Tags, blank=True)


    def get_absolute_url(self):
        return reverse('precious_metal-detail', args=[str(self.id)])
    
    def all_places(self):
        return ', '.join([str(place) for place in self.place_of_provenance_pol.all()])
    
    def clean_name(self):
        """
        Return the name of the model instance.
        """
        return "precious_metal"

    def show_value(self) -> str:
        # Generate a meaningful string representation based on the coded_value and place_of_provenance_pol
        return self.coded_value
        
    def display_table_value(self) -> str:
        rows = []

        # Conditionally add rows if values are not None
        if self.coded_value:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-1 fw-normal" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                        Precious Metal
                    </td>
                    <td class="align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        {self.coded_value}
                    </td>
                </tr>
            """)

        if self.place_of_provenance_str:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-1 fw-normal" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                        Place of Provenance
                    </td>
                    <td class="align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        {self.place_of_provenance_str}
                    </td>
                </tr>
            """)

        if self.ruler_consumption:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-1 fw-normal" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                        Consumption by Ruler
                    </td>
                    <td class="align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        {self.ruler_consumption}
                    </td>
                </tr>
            """)

        if self.elite_consumption:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-1 fw-normal" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                        Consumption by Elites
                    </td>
                    <td class="align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        {self.elite_consumption}
                    </td>
                </tr>
            """)

        if self.common_people_consumption:
            rows.append(f"""
                <tr style="border-bottom:1px solid #FFFDF2;">
                    <td class="ps-1 fw-normal" style="padding-right: 8px; text-align: left; font-weight: bold; color: #888;">
                        Consumption by Common People
                    </td>
                    <td class="align-right" style="padding-right: 8px; text-align: right; color: #555;">
                        {self.common_people_consumption}
                    </td>
                </tr>
            """)

        # Combine rows into a table
        table_html = f"""
            <table class="table" style="width: 100%; border-collapse: collapse; border: none; margin: 0px;">
                {''.join(rows)}
            </table>
        """
        return table_html



    def __str__(self) -> str:
        # Generate a meaningful string representation based on the coded_value and place_of_provenance_pol
        return f'{self.coded_value} in {self.all_places()} and {self.place_of_provenance_str}.'
    

class Lux_precious_metal(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="lux_precious_metal")
    which_metals = models.ManyToManyField(Prec_met_instance, related_name="%(app_label)s_%(class)s_related_metals", related_query_name="%(app_label)s_%(class)ss", blank=True)

    def get_absolute_url(self):
        return reverse('lux_precious_metal-detail', args=[str(self.id)])
    
    def clean_name(self):
        return "lux_precious_metal"
    
    def clean_name_spaced(self):
        return "Luxury Precious Metal"
        


class Luxury_fabrics(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="luxury_fabrics")

    def get_absolute_url(self):
        return reverse('luxury_fabrics-detail', args=[str(self.id)])

    def clean_name(self):
        return "luxury_fabrics"

    def clean_name_spaced(self):
        return "Luxury Fabrics"


class Luxury_manufactured_goods(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="luxury_manufactured_goods")

    def get_absolute_url(self):
        return reverse('luxury_manufactured_goods-detail', args=[str(self.id)])

    def clean_name(self):
        return "luxury_manufactured_goods"

    def clean_name_spaced(self):
        return "Luxury Manufactured Goods"


class Luxury_spices_incense_and_dyes(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="luxury_spices_incense_and_dyes")

    def get_absolute_url(self):
        return reverse('luxury_spices_incense_and_dyes-detail', args=[str(self.id)])

    def clean_name(self):
        return "luxury_spices_incense_and_dyes"

    def clean_name_spaced(self):
        return "Luxury Spices Incense And Dyes"


class Luxury_drink_alcohol(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="luxury_drink_alcohol")

    def get_absolute_url(self):
        return reverse('luxury_drink_alcohol-detail', args=[str(self.id)])

    def clean_name(self):
        return "luxury_drink_alcohol"

    def clean_name_spaced(self):
        return "Luxury Drink/Alcohol"


class Luxury_glass_goods(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="luxury_glass_goods")

    def get_absolute_url(self):
        return reverse('luxury_glass_goods-detail', args=[str(self.id)])

    def clean_name(self):
        return "luxury_glass_goods"

    def clean_name_spaced(self):
        return "Luxury Glass Goods"


class Lux_fine_ceramic_wares(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="lux_fine_ceramic_wares")

    def get_absolute_url(self):
        return reverse('lux_fine_ceramic_wares-detail', args=[str(self.id)])

    def clean_name(self):
        return "lux_fine_ceramic_wares"

    def clean_name_spaced(self):
        return "Luxury Fine Ceramic Wares"


class Lux_precious_stone(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="lux_precious_stone")

    def get_absolute_url(self):
        return reverse('lux_precious_stone-detail', args=[str(self.id)])

    def clean_name(self):
        return "lux_precious_stone"

    def clean_name_spaced(self):
        return "Luxury Precious Stone"


class Lux_statuary(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="lux_statuary")

    def get_absolute_url(self):
        return reverse('lux_statuary-detail', args=[str(self.id)])

    def clean_name(self):
        return "lux_statuary"

    def clean_name_spaced(self):
        return "Luxury Statuary"


class Luxury_food(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="luxury_food")

    def get_absolute_url(self):
        return reverse('luxury_food-detail', args=[str(self.id)])

    def clean_name(self):
        return "luxury_food"

    def clean_name_spaced(self):
        return "Luxury Food"


class Other_luxury_personal_items(SeshatCommon, LuxAttributes):
    name = models.CharField(max_length=100, default="other_luxury_personal_items")

    def get_absolute_url(self):
        return reverse('other_luxury_personal_items-detail', args=[str(self.id)])

    def clean_name(self):
        return "other_luxury_personal_items"

    def clean_name_spaced(self):
        return "Other Luxury Personal Items"
