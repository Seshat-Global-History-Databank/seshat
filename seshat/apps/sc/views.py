
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier
from django.db.models.base import Model
# from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.utils.safestring import mark_safe
from django.views.generic.list import ListView

from django.contrib.contenttypes.models import ContentType

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect, response, JsonResponse, HttpResponseForbidden
from ..core.models import Citation, Reference, Polity, Section, Subsection, Country, Variablehierarchy

# from .mycodes import *
from django.conf import settings

from django.urls import reverse, reverse_lazy

from django.views import generic
import csv
import datetime

from django.core.paginator import Paginator

from django.http import HttpResponse

from ..general.mixins import PolityIdMixin

import requests
from requests.structures import CaseInsensitiveDict
from django.apps import apps

from django.contrib import messages

#from easyaudit.models import CRUDEvent

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test


from .models import Ra, Polity_territory, Polity_population, Population_of_the_largest_settlement, Settlement_hierarchy, Administrative_level, Religious_level, Military_level, Professional_military_officer, Professional_soldier, Professional_priesthood, Full_time_bureaucrat, Examination_system, Merit_promotion, Specialized_government_building, Formal_legal_code, Judge, Court, Professional_lawyer, Irrigation_system, Drinking_water_supply_system, Market, Food_storage_site, Road, Bridge, Canal, Port, Mines_or_quarry, Mnemonic_device, Nonwritten_record, Written_record, Script, Non_phonetic_writing, Phonetic_alphabetic_writing, Lists_tables_and_classification, Calendar, Sacred_text, Religious_literature, Practical_literature, History, Philosophy, Scientific_literature, Fiction, Article, Token, Precious_metal, Foreign_coin, Indigenous_coin, Paper_currency, Courier, Postal_station, General_postal_service


from .forms import RaForm, Polity_territoryForm, Polity_populationForm, Population_of_the_largest_settlementForm, Settlement_hierarchyForm, Administrative_levelForm, Religious_levelForm, Military_levelForm, Professional_military_officerForm, Professional_soldierForm, Professional_priesthoodForm, Full_time_bureaucratForm, Examination_systemForm, Merit_promotionForm, Specialized_government_buildingForm, Formal_legal_codeForm, JudgeForm, CourtForm, Professional_lawyerForm, Irrigation_systemForm, Drinking_water_supply_systemForm, MarketForm, Food_storage_siteForm, RoadForm, BridgeForm, CanalForm, PortForm, Mines_or_quarryForm, Mnemonic_deviceForm, Nonwritten_recordForm, Written_recordForm, ScriptForm, Non_phonetic_writingForm, Phonetic_alphabetic_writingForm, Lists_tables_and_classificationForm, CalendarForm, Sacred_textForm, Religious_literatureForm, Practical_literatureForm, HistoryForm, PhilosophyForm, Scientific_literatureForm, FictionForm, ArticleForm, TokenForm, Precious_metalForm, Foreign_coinForm, Indigenous_coinForm, Paper_currencyForm, CourierForm, Postal_stationForm, General_postal_serviceForm

class RaCreate(PermissionRequiredMixin, CreateView):
    """
    View for creating a new Ra object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Ra
    form_class = RaForm
    template_name = "sc/ra/ra_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('ra-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "ra"
        context["my_exp"] = "The name of the research assistant or associate who coded the data. If more than one RA made a substantial contribution, list all via separate entries."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'sc_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of Social Complexity Variables', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class RaUpdate(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Ra object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Ra
    form_class = RaForm
    template_name = "sc/ra/ra_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "ra"

        return context

class RaDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Ra object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Ra
    success_url = reverse_lazy('ras')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class RaListView(generic.ListView):
    """
    Paginated view for listing all the Ra objects.
    """
    model = Ra
    template_name = "sc/ra/ra_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('ras')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "ra"
        context["var_main_desc"] = "The name of the research assistant or associate who coded the data. if more than one ra made a substantial contribution, list all via separate entries."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "staff"
        context["inner_vars"] = {'sc_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of Social Complexity Variables', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class RaListViewAll(generic.ListView):
    """
    View for listing all the Ra objects.
    """
    model = Ra
    template_name = "sc/ra/ra_list_all.html"

    def get_absolute_url(self):
        return reverse('ras_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Ra.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "ra"
        context["var_main_desc"] = "The name of the research assistant or associate who coded the data. if more than one ra made a substantial contribution, list all via separate entries."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "staff"
        context["inner_vars"] = {'sc_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of Social Complexity Variables', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class RaDetailView(generic.DetailView):
    """
    View for displaying the details of a Ra object.
    """
    model = Ra
    template_name = "sc/ra/ra_detail.html"


@permission_required('core.view_capital')
def ra_download(request):
    """
    Download all the data in the Ra model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    items = Ra.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_ra_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'sc_ra', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.sc_ra, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def ra_meta_download(request):
    """
    Download the metadata of the Ra model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_ras.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'The name of the research assistant or associate who coded the data. If more than one RA made a substantial contribution, list all via separate entries.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'staff'}
    my_meta_data_dic_inner_vars = {'sc_ra': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The RA of Social Complexity Variables', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_territoryCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    View for creating a new Polity_territory object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Polity_territory
    form_class = Polity_territoryForm
    template_name = "sc/polity_territory/polity_territory_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polity_territory-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Territory"
        context["my_exp"] = "Talking about Social Scale, Polity territory is coded in squared kilometers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'polity_territory_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}, 'polity_territory_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Polity_territoryUpdate(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_territory object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Polity_territory
    form_class = Polity_territoryForm
    template_name = "sc/polity_territory/polity_territory_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Territory"

        return context

class Polity_territoryDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_territory object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Polity_territory
    success_url = reverse_lazy('polity_territorys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_territoryListView(generic.ListView):
    """
    Paginated view for listing all the Polity_territory objects.
    """
    model = Polity_territory
    template_name = "sc/polity_territory/polity_territory_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polity_territorys')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Territory"
        context["var_main_desc"] = "Talking about social scale, polity territory is coded in squared kilometers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'polity_territory_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}, 'polity_territory_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = ['Units']

        return context


class Polity_territoryListViewAll(generic.ListView):
    """
    View for listing all the Polity_territory objects.
    """
    model = Polity_territory
    template_name = "sc/polity_territory/polity_territory_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polity_territorys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_territory.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Territory"
        context["var_main_desc"] = "Talking about social scale, polity territory is coded in squared kilometers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'polity_territory_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}, 'polity_territory_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = ['Units']
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_territoryDetailView(generic.DetailView):
    """
    View for displaying the details of a Polity_territory object.
    """
    model = Polity_territory
    template_name = "sc/polity_territory/polity_territory_detail.html"


@permission_required('core.view_capital')
def polity_territory_download(request):
    """
    Download all the data in the Polity_territory model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    items = Polity_territory.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_polity_territory_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'polity_territory_from', 'polity_territory_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.polity_territory_from, obj.polity_territory_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_territory_meta_download(request):
    """
    Download the metadata of the Polity_territory model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_polity_territorys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Social Scale, Polity territory is coded in squared kilometers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Social Scale'}
    my_meta_data_dic_inner_vars = {'polity_territory_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}, 'polity_territory_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of polity territory for a polity.', 'units': 'km squared', 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Polity_populationCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    View for creating a new Polity_population object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Polity_population
    form_class = Polity_populationForm
    template_name = "sc/polity_population/polity_population_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polity_population-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Polity Population"
        context["my_exp"] = "Talking about Social Scale, Polity Population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'polity_population_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'polity_population_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Polity_populationUpdate(PermissionRequiredMixin, UpdateView):
    """
    View for updating an existing Polity_population object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Polity_population
    form_class = Polity_populationForm
    template_name = "sc/polity_population/polity_population_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Population"

        return context

class Polity_populationDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Polity_population object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Polity_population
    success_url = reverse_lazy('polity_populations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Polity_populationListView(generic.ListView):
    """
    Paginated view for listing all the Polity_population objects.
    """
    model = Polity_population
    template_name = "sc/polity_population/polity_population_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polity_populations')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Population"
        context["var_main_desc"] = "Talking about social scale, polity population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'polity_population_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'polity_population_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Polity_populationListViewAll(generic.ListView):
    """
    View for listing all the Polity_population objects.
    """
    model = Polity_population
    template_name = "sc/polity_population/polity_population_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polity_populations_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Polity_population.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Polity Population"
        context["var_main_desc"] = "Talking about social scale, polity population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'polity_population_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'polity_population_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Polity_populationDetailView(generic.DetailView):
    """
    View for displaying the details of a Polity_population object.
    """
    model = Polity_population
    template_name = "sc/polity_population/polity_population_detail.html"


@permission_required('core.view_capital')
def polity_population_download(request):
    """
    Download all the data of the Polity_population model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    items = Polity_population.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_polity_population_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'polity_population_from', 'polity_population_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.polity_population_from, obj.polity_population_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def polity_population_meta_download(request):
    """
    Download the metadata of the Polity_population model as a CSV file.

    Note:
        The access to this view is restricted to users with the 'core.view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_polity_populations.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Social Scale, Polity Population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Social Scale'}
    my_meta_data_dic_inner_vars = {'polity_population_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'polity_population_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of polity population for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Population_of_the_largest_settlementCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    View for creating a new Population_of_the_largest_settlement object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Population_of_the_largest_settlement
    form_class = Population_of_the_largest_settlementForm
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('population_of_the_largest_settlement-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Population of the Largest Settlement"
        context["my_exp"] = "Talking about Social Scale, Population of the largest settlement is the estimated population of the largest settlement of the polity. Note that the largest settlement could be different from the capital (coded under General Variables). If possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). Note that we are also building a city database - you should consult it as it may already have the needed data."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'population_of_the_largest_settlement_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'population_of_the_largest_settlement_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Population_of_the_largest_settlementUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Population_of_the_largest_settlement
    form_class = Population_of_the_largest_settlementForm
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Population of the Largest Settlement"

        return context

class Population_of_the_largest_settlementDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Population_of_the_largest_settlement object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Population_of_the_largest_settlement
    success_url = reverse_lazy('population_of_the_largest_settlements')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Population_of_the_largest_settlementListView(generic.ListView):
    """
    Paginated view for listing all the Population_of_the_largest_settlement objects.
    """
    model = Population_of_the_largest_settlement
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('population_of_the_largest_settlements')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Population of the Largest Settlement"
        context["var_main_desc"] = "Talking about social scale, population of the largest settlement is the estimated population of the largest settlement of the polity. note that the largest settlement could be different from the capital (coded under general variables). if possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). note that we are also building a city database - you should consult it as it may already have the needed data."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'population_of_the_largest_settlement_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'population_of_the_largest_settlement_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Population_of_the_largest_settlementListViewAll(generic.ListView):
    """
    
    """
    model = Population_of_the_largest_settlement
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('population_of_the_largest_settlements_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Population_of_the_largest_settlement.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Population of the Largest Settlement"
        context["var_main_desc"] = "Talking about social scale, population of the largest settlement is the estimated population of the largest settlement of the polity. note that the largest settlement could be different from the capital (coded under general variables). if possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). note that we are also building a city database - you should consult it as it may already have the needed data."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Social Scale"
        context["inner_vars"] = {'population_of_the_largest_settlement_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'population_of_the_largest_settlement_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Population_of_the_largest_settlementDetailView(generic.DetailView):
    """
    
    """
    model = Population_of_the_largest_settlement
    template_name = "sc/population_of_the_largest_settlement/population_of_the_largest_settlement_detail.html"


@permission_required('core.view_capital')
def population_of_the_largest_settlement_download(request):
    items = Population_of_the_largest_settlement.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_population_of_the_largest_settlement_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'population_of_the_largest_settlement_from', 'population_of_the_largest_settlement_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.population_of_the_largest_settlement_from, obj.population_of_the_largest_settlement_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def population_of_the_largest_settlement_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_population_of_the_largest_settlements.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Social Scale, Population of the largest settlement is the estimated population of the largest settlement of the polity. Note that the largest settlement could be different from the capital (coded under General Variables). If possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). Note that we are also building a city database - you should consult it as it may already have the needed data.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Social Scale'}
    my_meta_data_dic_inner_vars = {'population_of_the_largest_settlement_from': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'population_of_the_largest_settlement_to': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of population of the largest settlement for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Settlement_hierarchyCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Settlement_hierarchy
    form_class = Settlement_hierarchyForm
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('settlement_hierarchy-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Settlement Hierarchy"
        context["my_exp"] = "Talking about Hierarchical Complexity, Settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. As settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). Example: (1) Large City (monumental structures, theatre, market, hospital, central government buildings) (2) City (market, theatre, regional government buildings) (3) Large Town (market, administrative buildings) (4) Town (administrative buildings, storehouse)) (5) Village (shrine) (6) Hamlet (residential only). In the narrative paragraph explain the different levels and list their functions. Provide a (crude) estimate of population sizes. For example, Large Town (market, temple, administrative buildings): 2,000-5,000 inhabitants."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'settlement_hierarchy_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'settlement_hierarchy_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Settlement_hierarchyUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Settlement_hierarchy
    form_class = Settlement_hierarchyForm
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Settlement Hierarchy"

        return context

class Settlement_hierarchyDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Settlement_hierarchy object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Settlement_hierarchy
    success_url = reverse_lazy('settlement_hierarchys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Settlement_hierarchyListView(generic.ListView):
    """
    Paginated view for listing all the Settlement_hierarchy objects.
    """
    model = Settlement_hierarchy
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('settlement_hierarchys')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Settlement Hierarchy"
        context["var_main_desc"] = "Talking about hierarchical complexity, settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. as settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). example: (1) large city (monumental structures, theatre, market, hospital, central government buildings) (2) city (market, theatre, regional government buildings) (3) large town (market, administrative buildings) (4) town (administrative buildings, storehouse)) (5) village (shrine) (6) hamlet (residential only). in the narrative paragraph explain the different levels and list their functions. provide a (crude) estimate of population sizes. for example, large town (market, temple, administrative buildings): 2,000-5,000 inhabitants."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'settlement_hierarchy_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'settlement_hierarchy_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Settlement_hierarchyListViewAll(generic.ListView):
    """
    
    """
    model = Settlement_hierarchy
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('settlement_hierarchys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Settlement_hierarchy.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Settlement Hierarchy"
        context["var_main_desc"] = "Talking about hierarchical complexity, settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. as settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). example: (1) large city (monumental structures, theatre, market, hospital, central government buildings) (2) city (market, theatre, regional government buildings) (3) large town (market, administrative buildings) (4) town (administrative buildings, storehouse)) (5) village (shrine) (6) hamlet (residential only). in the narrative paragraph explain the different levels and list their functions. provide a (crude) estimate of population sizes. for example, large town (market, temple, administrative buildings): 2,000-5,000 inhabitants."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'settlement_hierarchy_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'settlement_hierarchy_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Settlement_hierarchyDetailView(generic.DetailView):
    """
    
    """
    model = Settlement_hierarchy
    template_name = "sc/settlement_hierarchy/settlement_hierarchy_detail.html"


@permission_required('core.view_capital')
def settlement_hierarchy_download(request):
    items = Settlement_hierarchy.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_settlement_hierarchy_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'settlement_hierarchy_from', 'settlement_hierarchy_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.settlement_hierarchy_from, obj.settlement_hierarchy_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def settlement_hierarchy_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_settlement_hierarchys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Hierarchical Complexity, Settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. As settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). Example: (1) Large City (monumental structures, theatre, market, hospital, central government buildings) (2) City (market, theatre, regional government buildings) (3) Large Town (market, administrative buildings) (4) Town (administrative buildings, storehouse)) (5) Village (shrine) (6) Hamlet (residential only). In the narrative paragraph explain the different levels and list their functions. Provide a (crude) estimate of population sizes. For example, Large Town (market, temple, administrative buildings): 2,000-5,000 inhabitants.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Hierarchical Complexity'}
    my_meta_data_dic_inner_vars = {'settlement_hierarchy_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'settlement_hierarchy_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of settlement hierarchy for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Administrative_levelCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Administrative_level
    form_class = Administrative_levelForm
    template_name = "sc/administrative_level/administrative_level_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('administrative_level-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Administrative Level"
        context["my_exp"] = "Talking about Hierarchical Complexity, Administrative levels records the administrative levels of a polity. An example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. Note that unlike in settlement hierarchy, here you code people hierarchy. Do not simply copy settlement hierarchy data here. For archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. Note: Often there are more than one concurrent administrative hierarchy. In the example above the hierarchy refers to the territorial government. In addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. For example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. In the narrative paragraph detail what is known about both hierarchies. The machine-readable code should reflect the largest number (the longer chain of command)."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'administrative_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'administrative_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Administrative_levelUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Administrative_level
    form_class = Administrative_levelForm
    template_name = "sc/administrative_level/administrative_level_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Administrative Level"

        return context

class Administrative_levelDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Administrative_level object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Administrative_level
    success_url = reverse_lazy('administrative_levels')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Administrative_levelListView(generic.ListView):
    """
    Paginated view for listing all the Administrative_level objects.
    """
    model = Administrative_level
    template_name = "sc/administrative_level/administrative_level_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('administrative_levels')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Administrative Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, administrative levels records the administrative levels of a polity. an example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. note that unlike in settlement hierarchy, here you code people hierarchy. do not simply copy settlement hierarchy data here. for archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. note: often there are more than one concurrent administrative hierarchy. in the example above the hierarchy refers to the territorial government. in addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. for example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. in the narrative paragraph detail what is known about both hierarchies. the machine-readable code should reflect the largest number (the longer chain of command)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'administrative_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'administrative_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Administrative_levelListViewAll(generic.ListView):
    """
    
    """
    model = Administrative_level
    template_name = "sc/administrative_level/administrative_level_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('administrative_levels_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Administrative_level.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Administrative Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, administrative levels records the administrative levels of a polity. an example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. note that unlike in settlement hierarchy, here you code people hierarchy. do not simply copy settlement hierarchy data here. for archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. note: often there are more than one concurrent administrative hierarchy. in the example above the hierarchy refers to the territorial government. in addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. for example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. in the narrative paragraph detail what is known about both hierarchies. the machine-readable code should reflect the largest number (the longer chain of command)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'administrative_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'administrative_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Administrative_levelDetailView(generic.DetailView):
    """
    
    """
    model = Administrative_level
    template_name = "sc/administrative_level/administrative_level_detail.html"


@permission_required('core.view_capital')
def administrative_level_download(request):
    items = Administrative_level.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_administrative_level_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'administrative_level_from', 'administrative_level_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.administrative_level_from, obj.administrative_level_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def administrative_level_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_administrative_levels.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Hierarchical Complexity, Administrative levels records the administrative levels of a polity. An example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. Note that unlike in settlement hierarchy, here you code people hierarchy. Do not simply copy settlement hierarchy data here. For archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. Note: Often there are more than one concurrent administrative hierarchy. In the example above the hierarchy refers to the territorial government. In addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. For example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. In the narrative paragraph detail what is known about both hierarchies. The machine-readable code should reflect the largest number (the longer chain of command).", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Hierarchical Complexity'}
    my_meta_data_dic_inner_vars = {'administrative_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'administrative_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of administrative level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Religious_levelCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Religious_level
    form_class = Religious_levelForm
    template_name = "sc/religious_level/religious_level_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('religious_level-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Religious Level"
        context["my_exp"] = "Talking about Hierarchical Complexity, Religious levels records the Religious levels of a polity. Same principle as with Administrative levels. Start with the head of the official cult (if present) coded as: level 1, and work down to the local priest."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'religious_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'religious_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Religious_levelUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Religious_level
    form_class = Religious_levelForm
    template_name = "sc/religious_level/religious_level_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Level"

        return context

class Religious_levelDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Religious_level object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Religious_level
    success_url = reverse_lazy('religious_levels')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Religious_levelListView(generic.ListView):
    """
    Paginated view for listing all the Religious_level objects.
    """
    model = Religious_level
    template_name = "sc/religious_level/religious_level_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('religious_levels')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, religious levels records the religious levels of a polity. same principle as with administrative levels. start with the head of the official cult (if present) coded as: level 1, and work down to the local priest."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'religious_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'religious_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Religious_levelListViewAll(generic.ListView):
    """
    
    """
    model = Religious_level
    template_name = "sc/religious_level/religious_level_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('religious_levels_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Religious_level.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, religious levels records the religious levels of a polity. same principle as with administrative levels. start with the head of the official cult (if present) coded as: level 1, and work down to the local priest."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'religious_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'religious_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Religious_levelDetailView(generic.DetailView):
    """
    
    """
    model = Religious_level
    template_name = "sc/religious_level/religious_level_detail.html"


@permission_required('core.view_capital')
def religious_level_download(request):
    items = Religious_level.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_religious_level_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'religious_level_from', 'religious_level_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.religious_level_from, obj.religious_level_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def religious_level_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_religious_levels.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Hierarchical Complexity, Religious levels records the Religious levels of a polity. Same principle as with Administrative levels. Start with the head of the official cult (if present) coded as: level 1, and work down to the local priest.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Hierarchical Complexity'}
    my_meta_data_dic_inner_vars = {'religious_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'religious_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of religious level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Military_levelCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Military_level
    form_class = Military_levelForm
    template_name = "sc/military_level/military_level_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('military_level-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Military Level"
        context["my_exp"] = "Talking about Hierarchical Complexity, Military levels records the Military levels of a polity. Same principle as with Administrative levels. Start with the commander-in-chief coded as: level 1, and work down to the private. Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier)."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'military_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'military_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Military_levelUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Military_level
    form_class = Military_levelForm
    template_name = "sc/military_level/military_level_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Military Level"

        return context

class Military_levelDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Military_level object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Military_level
    success_url = reverse_lazy('military_levels')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Military_levelListView(generic.ListView):
    """
    Paginated view for listing all the Military_level objects.
    """
    model = Military_level
    template_name = "sc/military_level/military_level_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('military_levels')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Military Level"
        context["var_main_desc"] = "Talking about hierarchical complexity, military levels records the military levels of a polity. same principle as with administrative levels. start with the commander-in-chief coded as: level 1, and work down to the private. even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. a complex chiefdom would be coded three levels. the presence of warrior burials might be the basis for inferring the existence of a military organization. (the lowest military level is always the individual soldier)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Hierarchical Complexity"
        context["inner_vars"] = {'military_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'military_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
        context["potential_cols"] = []

        return context


# class Military_levelListViewAll(generic.ListView):
#    model = Military_level
#     template_name = "sc/military_level/military_level_list_all.html"

#     def get_absolute_url(self):
#         return reverse('military_levels_all')

#     def get_queryset(self):
#         order = self.request.GET.get('orderby', 'year_from')
#         order2 = self.request.GET.get('orderby2', 'year_to')
#         #orders = [order, order2]
#         new_context = Military_level.objects.all().order_by(order, order2)
#         return new_context
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["myvar"] = "Military Level"
#         context["var_main_desc"] = "Talking about hierarchical complexity, military levels records the military levels of a polity. same principle as with administrative levels. start with the commander-in-chief coded as: level 1, and work down to the private. even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. a complex chiefdom would be coded three levels. the presence of warrior burials might be the basis for inferring the existence of a military organization. (the lowest military level is always the individual soldier)."
#         context["var_main_desc_source"] = "NOTHING"
#         context["var_section"] = "Social Complexity"
#         context["var_subsection"] = "Hierarchical Complexity"
#         context["inner_vars"] = {'military_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'military_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
#         context["potential_cols"] = []
#         context['orderby'] = self.request.GET.get('orderby', 'year_from')

#         return context
        
class Military_levelDetailView(generic.DetailView):
    """
    
    """
    model = Military_level
    template_name = "sc/military_level/military_level_detail.html"


@permission_required('core.view_capital')
def military_level_download(request):
    items = Military_level.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_military_level_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'military_level_from', 'military_level_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.military_level_from, obj.military_level_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def military_level_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_military_levels.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Hierarchical Complexity, Military levels records the Military levels of a polity. Same principle as with Administrative levels. Start with the commander-in-chief coded as: level 1, and work down to the private. Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier).', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Hierarchical Complexity'}
    my_meta_data_dic_inner_vars = {'military_level_from': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The lower range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}, 'military_level_to': {'min': 0, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The upper range of military level for a polity.', 'units': None, 'choices': None, 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Professional_military_officerCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_military_officer
    form_class = Professional_military_officerForm
    template_name = "sc/professional_military_officer/professional_military_officer_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_military_officer-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Professional Military Officer"
        context["my_exp"] = "Talking about Professions, Professional military officers refer to Full-time Professional military officers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'professional_military_officer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional military officer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Professional_military_officerUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_military_officer
    form_class = Professional_military_officerForm
    template_name = "sc/professional_military_officer/professional_military_officer_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Military Officer"

        return context

class Professional_military_officerDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Professional_military_officer object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_military_officer
    success_url = reverse_lazy('professional_military_officers')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Professional_military_officerListView(generic.ListView):
    """
    Paginated view for listing all the Professional_military_officer objects.
    """
    model = Professional_military_officer
    template_name = "sc/professional_military_officer/professional_military_officer_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_military_officers')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Military Officer"
        context["var_main_desc"] = "Talking about professions, professional military officers refer to full-time professional military officers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_military_officer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional military officer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Professional_military_officerListViewAll(generic.ListView):
    """
    
    """
    model = Professional_military_officer
    template_name = "sc/professional_military_officer/professional_military_officer_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_military_officers_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Professional_military_officer.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Military Officer"
        context["var_main_desc"] = "Talking about professions, professional military officers refer to full-time professional military officers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_military_officer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional military officer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Professional_military_officerDetailView(generic.DetailView):
    """
    
    """
    model = Professional_military_officer
    template_name = "sc/professional_military_officer/professional_military_officer_detail.html"


@permission_required('core.view_capital')
def professional_military_officer_download(request):
    items = Professional_military_officer.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_professional_military_officer_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'professional_military_officer', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.professional_military_officer, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def professional_military_officer_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_professional_military_officers.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Professions, Professional military officers refer to Full-time Professional military officers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Professions'}
    my_meta_data_dic_inner_vars = {'professional_military_officer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional military officer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Professional_soldierCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_soldier
    form_class = Professional_soldierForm
    template_name = "sc/professional_soldier/professional_soldier_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_soldier-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Professional Soldier"
        context["my_exp"] = "Talking about Professions, Professional soldiers refer to Full-time Professional soldiers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'professional_soldier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional soldier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Professional_soldierUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_soldier
    form_class = Professional_soldierForm
    template_name = "sc/professional_soldier/professional_soldier_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Soldier"

        return context

class Professional_soldierDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Professional_soldier object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_soldier
    success_url = reverse_lazy('professional_soldiers')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Professional_soldierListView(generic.ListView):
    """
    Paginated view for listing all the Professional_soldier objects.
    """
    model = Professional_soldier
    template_name = "sc/professional_soldier/professional_soldier_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_soldiers')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Soldier"
        context["var_main_desc"] = "Talking about professions, professional soldiers refer to full-time professional soldiers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_soldier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional soldier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Professional_soldierListViewAll(generic.ListView):
    """
    
    """
    model = Professional_soldier
    template_name = "sc/professional_soldier/professional_soldier_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_soldiers_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Professional_soldier.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Soldier"
        context["var_main_desc"] = "Talking about professions, professional soldiers refer to full-time professional soldiers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_soldier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional soldier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Professional_soldierDetailView(generic.DetailView):
    """
    
    """
    model = Professional_soldier
    template_name = "sc/professional_soldier/professional_soldier_detail.html"


@permission_required('core.view_capital')
def professional_soldier_download(request):
    items = Professional_soldier.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_professional_soldier_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'professional_soldier', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.professional_soldier, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def professional_soldier_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_professional_soldiers.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Professions, Professional soldiers refer to Full-time Professional soldiers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Professions'}
    my_meta_data_dic_inner_vars = {'professional_soldier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional soldier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Professional_priesthoodCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_priesthood
    form_class = Professional_priesthoodForm
    template_name = "sc/professional_priesthood/professional_priesthood_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_priesthood-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Professional Priesthood"
        context["my_exp"] = "Talking about Professions, Professional priesthood refers to Full-time Professional priesthood."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'professional_priesthood': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional priesthood for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Professional_priesthoodUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_priesthood
    form_class = Professional_priesthoodForm
    template_name = "sc/professional_priesthood/professional_priesthood_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Priesthood"

        return context

class Professional_priesthoodDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Professional_priesthood object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_priesthood
    success_url = reverse_lazy('professional_priesthoods')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Professional_priesthoodListView(generic.ListView):
    """
    Paginated view for listing all the Professional_priesthood objects.
    """
    model = Professional_priesthood
    template_name = "sc/professional_priesthood/professional_priesthood_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_priesthoods')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Priesthood"
        context["var_main_desc"] = "Talking about professions, professional priesthood refers to full-time professional priesthood."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_priesthood': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional priesthood for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Professional_priesthoodListViewAll(generic.ListView):
    """
    
    """
    model = Professional_priesthood
    template_name = "sc/professional_priesthood/professional_priesthood_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_priesthoods_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Professional_priesthood.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Priesthood"
        context["var_main_desc"] = "Talking about professions, professional priesthood refers to full-time professional priesthood."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Professions"
        context["inner_vars"] = {'professional_priesthood': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional priesthood for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Professional_priesthoodDetailView(generic.DetailView):
    """
    
    """
    model = Professional_priesthood
    template_name = "sc/professional_priesthood/professional_priesthood_detail.html"


@permission_required('core.view_capital')
def professional_priesthood_download(request):
    items = Professional_priesthood.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_professional_priesthood_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'professional_priesthood', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.professional_priesthood, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def professional_priesthood_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_professional_priesthoods.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Professions, Professional priesthood refers to Full-time Professional priesthood.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Professions'}
    my_meta_data_dic_inner_vars = {'professional_priesthood': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional priesthood for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Full_time_bureaucratCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Full_time_bureaucrat
    form_class = Full_time_bureaucratForm
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('full_time_bureaucrat-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Full Time Bureaucrat"
        context["my_exp"] = "Talking about Bureaucracy characteristics, Full-time bureaucrats refer to Full-time administrative specialists. Code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. Also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. Note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'full_time_bureaucrat': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of full time bureaucrat for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Full_time_bureaucratUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Full_time_bureaucrat
    form_class = Full_time_bureaucratForm
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Full Time Bureaucrat"

        return context

class Full_time_bureaucratDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Full_time_bureaucrat object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Full_time_bureaucrat
    success_url = reverse_lazy('full_time_bureaucrats')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Full_time_bureaucratListView(generic.ListView):
    """
    Paginated view for listing all the Full_time_bureaucrat objects.
    """
    model = Full_time_bureaucrat
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('full_time_bureaucrats')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Full Time Bureaucrat"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, full-time bureaucrats refer to full-time administrative specialists. code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'full_time_bureaucrat': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of full time bureaucrat for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Full_time_bureaucratListViewAll(generic.ListView):
    """
    
    """
    model = Full_time_bureaucrat
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('full_time_bureaucrats_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Full_time_bureaucrat.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Full Time Bureaucrat"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, full-time bureaucrats refer to full-time administrative specialists. code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'full_time_bureaucrat': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of full time bureaucrat for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Full_time_bureaucratDetailView(generic.DetailView):
    """
    
    """
    model = Full_time_bureaucrat
    template_name = "sc/full_time_bureaucrat/full_time_bureaucrat_detail.html"


@permission_required('core.view_capital')
def full_time_bureaucrat_download(request):
    items = Full_time_bureaucrat.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_full_time_bureaucrat_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'full_time_bureaucrat', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.full_time_bureaucrat, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def full_time_bureaucrat_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_full_time_bureaucrats.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Bureaucracy characteristics, Full-time bureaucrats refer to Full-time administrative specialists. Code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. Also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. Note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government.", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Bureaucracy characteristics'}
    my_meta_data_dic_inner_vars = {'full_time_bureaucrat': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of full time bureaucrat for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Examination_systemCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Examination_system
    form_class = Examination_systemForm
    template_name = "sc/examination_system/examination_system_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('examination_system-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Examination System"
        context["my_exp"] = "Talking about Bureaucracy characteristics, The paradigmatic example of an Examination system is the Chinese imperial system."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'examination_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of examination system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Examination_systemUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Examination_system
    form_class = Examination_systemForm
    template_name = "sc/examination_system/examination_system_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Examination System"

        return context

class Examination_systemDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Examination_system object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Examination_system
    success_url = reverse_lazy('examination_systems')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Examination_systemListView(generic.ListView):
    """
    Paginated view for listing all the Examination_system objects.
    """
    model = Examination_system
    template_name = "sc/examination_system/examination_system_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('examination_systems')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Examination System"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, the paradigmatic example of an examination system is the chinese imperial system."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'examination_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of examination system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Examination_systemListViewAll(generic.ListView):
    """
    
    """
    model = Examination_system
    template_name = "sc/examination_system/examination_system_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('examination_systems_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Examination_system.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Examination System"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, the paradigmatic example of an examination system is the chinese imperial system."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'examination_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of examination system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Examination_systemDetailView(generic.DetailView):
    """
    
    """
    model = Examination_system
    template_name = "sc/examination_system/examination_system_detail.html"


@permission_required('core.view_capital')
def examination_system_download(request):
    items = Examination_system.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_examination_system_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'examination_system', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.examination_system, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def examination_system_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_examination_systems.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Bureaucracy characteristics, The paradigmatic example of an Examination system is the Chinese imperial system.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Bureaucracy characteristics'}
    my_meta_data_dic_inner_vars = {'examination_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of examination system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Merit_promotionCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Merit_promotion
    form_class = Merit_promotionForm
    template_name = "sc/merit_promotion/merit_promotion_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('merit_promotion-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Merit Promotion"
        context["my_exp"] = "Talking about Bureaucracy characteristics, Merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. When exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'merit_promotion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of merit promotion for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Merit_promotionUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Merit_promotion
    form_class = Merit_promotionForm
    template_name = "sc/merit_promotion/merit_promotion_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Merit Promotion"

        return context

class Merit_promotionDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Merit_promotion object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Merit_promotion
    success_url = reverse_lazy('merit_promotions')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Merit_promotionListView(generic.ListView):
    """
    Paginated view for listing all the Merit_promotion objects.
    """
    model = Merit_promotion
    template_name = "sc/merit_promotion/merit_promotion_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('merit_promotions')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Merit Promotion"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. when exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'merit_promotion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of merit promotion for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Merit_promotionListViewAll(generic.ListView):
    """
    
    """
    model = Merit_promotion
    template_name = "sc/merit_promotion/merit_promotion_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('merit_promotions_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Merit_promotion.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Merit Promotion"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. when exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'merit_promotion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of merit promotion for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Merit_promotionDetailView(generic.DetailView):
    """
    
    """
    model = Merit_promotion
    template_name = "sc/merit_promotion/merit_promotion_detail.html"


@permission_required('core.view_capital')
def merit_promotion_download(request):
    items = Merit_promotion.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_merit_promotion_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'merit_promotion', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.merit_promotion, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def merit_promotion_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_merit_promotions.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Bureaucracy characteristics, Merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. When exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Bureaucracy characteristics'}
    my_meta_data_dic_inner_vars = {'merit_promotion': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of merit promotion for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Specialized_government_buildingCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Specialized_government_building
    form_class = Specialized_government_buildingForm
    template_name = "sc/specialized_government_building/specialized_government_building_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('specialized_government_building-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Specialized Government Building"
        context["my_exp"] = "Talking about Bureaucracy characteristics, These buildings are where administrative officials are located, and must be distinct from the ruler's palace. They may be used for document storage, registration offices, minting money, etc. Defense structures also are not coded here (see Military). State-owned/operated workshop should also not be coded here."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'specialized_government_building': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of specialized government building for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Specialized_government_buildingUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Specialized_government_building
    form_class = Specialized_government_buildingForm
    template_name = "sc/specialized_government_building/specialized_government_building_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Specialized Government Building"

        return context

class Specialized_government_buildingDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Specialized_government_building object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Specialized_government_building
    success_url = reverse_lazy('specialized_government_buildings')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Specialized_government_buildingListView(generic.ListView):
    """
    Paginated view for listing all the Specialized_government_building objects.
    """
    model = Specialized_government_building
    template_name = "sc/specialized_government_building/specialized_government_building_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('specialized_government_buildings')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Specialized Government Building"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, these buildings are where administrative officials are located, and must be distinct from the ruler's palace. they may be used for document storage, registration offices, minting money, etc. defense structures also are not coded here (see military). state-owned/operated workshop should also not be coded here."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'specialized_government_building': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of specialized government building for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Specialized_government_buildingListViewAll(generic.ListView):
    """
    
    """
    model = Specialized_government_building
    template_name = "sc/specialized_government_building/specialized_government_building_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('specialized_government_buildings_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Specialized_government_building.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Specialized Government Building"
        context["var_main_desc"] = "Talking about bureaucracy characteristics, these buildings are where administrative officials are located, and must be distinct from the ruler's palace. they may be used for document storage, registration offices, minting money, etc. defense structures also are not coded here (see military). state-owned/operated workshop should also not be coded here."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Bureaucracy characteristics"
        context["inner_vars"] = {'specialized_government_building': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of specialized government building for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Specialized_government_buildingDetailView(generic.DetailView):
    """
    
    """
    model = Specialized_government_building
    template_name = "sc/specialized_government_building/specialized_government_building_detail.html"


@permission_required('core.view_capital')
def specialized_government_building_download(request):
    items = Specialized_government_building.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_specialized_government_building_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'specialized_government_building', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.specialized_government_building, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def specialized_government_building_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_specialized_government_buildings.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Bureaucracy characteristics, These buildings are where administrative officials are located, and must be distinct from the ruler's palace. They may be used for document storage, registration offices, minting money, etc. Defense structures also are not coded here (see Military). State-owned/operated workshop should also not be coded here.", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Bureaucracy characteristics'}
    my_meta_data_dic_inner_vars = {'specialized_government_building': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of specialized government building for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Formal_legal_codeCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Formal_legal_code
    form_class = Formal_legal_codeForm
    template_name = "sc/formal_legal_code/formal_legal_code_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('formal_legal_code-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Formal Legal Code"
        context["my_exp"] = "Talking about Law, Formal legal code refers to legal code usually, but not always written down. If not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). Provide a short description"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'formal_legal_code': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of formal legal code for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Formal_legal_codeUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Formal_legal_code
    form_class = Formal_legal_codeForm
    template_name = "sc/formal_legal_code/formal_legal_code_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Formal Legal Code"

        return context

class Formal_legal_codeDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Formal_legal_code object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Formal_legal_code
    success_url = reverse_lazy('formal_legal_codes')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Formal_legal_codeListView(generic.ListView):
    """
    Paginated view for listing all the Formal_legal_code objects.
    """
    model = Formal_legal_code
    template_name = "sc/formal_legal_code/formal_legal_code_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('formal_legal_codes')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Formal Legal Code"
        context["var_main_desc"] = "Talking about law, formal legal code refers to legal code usually, but not always written down. if not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). provide a short description"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'formal_legal_code': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of formal legal code for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Formal_legal_codeListViewAll(generic.ListView):
    """
    
    """
    model = Formal_legal_code
    template_name = "sc/formal_legal_code/formal_legal_code_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('formal_legal_codes_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Formal_legal_code.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Formal Legal Code"
        context["var_main_desc"] = "Talking about law, formal legal code refers to legal code usually, but not always written down. if not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). provide a short description"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'formal_legal_code': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of formal legal code for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Formal_legal_codeDetailView(generic.DetailView):
    """
    
    """
    model = Formal_legal_code
    template_name = "sc/formal_legal_code/formal_legal_code_detail.html"


@permission_required('core.view_capital')
def formal_legal_code_download(request):
    items = Formal_legal_code.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_formal_legal_code_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'formal_legal_code', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.formal_legal_code, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def formal_legal_code_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_formal_legal_codes.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Law, Formal legal code refers to legal code usually, but not always written down. If not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). Provide a short description", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Law'}
    my_meta_data_dic_inner_vars = {'formal_legal_code': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of formal legal code for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class JudgeCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Judge
    form_class = JudgeForm
    template_name = "sc/judge/judge_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('judge-create')

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Judge"
        context["my_exp"] = "Talking about Law, judges refers only to full-time professional judges"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'judge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of judge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class JudgeUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Judge
    form_class = JudgeForm
    template_name = "sc/judge/judge_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Judge"

        return context

class JudgeDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Judge object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Judge
    success_url = reverse_lazy('judges')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class JudgeListView(generic.ListView):
    """
    Paginated view for listing all the Judge objects.
    """
    model = Judge
    template_name = "sc/judge/judge_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('judges')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Judge"
        context["var_main_desc"] = "Talking about law, judges refers only to full-time professional judges"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'judge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of judge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class JudgeListViewAll(generic.ListView):
    """
    
    """
    model = Judge
    template_name = "sc/judge/judge_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('judges_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Judge.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Judge"
        context["var_main_desc"] = "Talking about law, judges refers only to full-time professional judges"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'judge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of judge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class JudgeDetailView(generic.DetailView):
    """
    
    """
    model = Judge
    template_name = "sc/judge/judge_detail.html"


@permission_required('core.view_capital')
def judge_download(request):
    items = Judge.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_judge_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'judge', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.judge, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def judge_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_judges.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Law, judges refers only to full-time professional judges', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Law'}
    my_meta_data_dic_inner_vars = {'judge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of judge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class CourtCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Court
    form_class = CourtForm
    template_name = "sc/court/court_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('court-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Court"
        context["my_exp"] = "Talking about Law, courts are buildings specialized for legal proceedings only."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'court': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of court for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class CourtUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Court
    form_class = CourtForm
    template_name = "sc/court/court_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Court"

        return context

class CourtDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Court object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Court
    success_url = reverse_lazy('courts')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class CourtListView(generic.ListView):
    """
    Paginated view for listing all the Court objects.
    """
    model = Court
    template_name = "sc/court/court_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('courts')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Court"
        context["var_main_desc"] = "Talking about law, courts are buildings specialized for legal proceedings only."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'court': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of court for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class CourtListViewAll(generic.ListView):
    """
    
    """
    model = Court
    template_name = "sc/court/court_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('courts_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Court.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Court"
        context["var_main_desc"] = "Talking about law, courts are buildings specialized for legal proceedings only."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'court': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of court for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class CourtDetailView(generic.DetailView):
    """
    
    """
    model = Court
    template_name = "sc/court/court_detail.html"


@permission_required('core.view_capital')
def court_download(request):
    items = Court.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_court_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'court', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.court, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def court_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_courts.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Law, courts are buildings specialized for legal proceedings only.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Law'}
    my_meta_data_dic_inner_vars = {'court': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of court for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Professional_lawyerCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_lawyer
    form_class = Professional_lawyerForm
    template_name = "sc/professional_lawyer/professional_lawyer_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_lawyer-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Professional Lawyer"
        context["my_exp"] = "Talking about Law, NO_DESCRIPTIONS_IN_CODEBOOK."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'professional_lawyer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional lawyer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Professional_lawyerUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_lawyer
    form_class = Professional_lawyerForm
    template_name = "sc/professional_lawyer/professional_lawyer_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Lawyer"

        return context

class Professional_lawyerDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Professional_lawyer object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Professional_lawyer
    success_url = reverse_lazy('professional_lawyers')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Professional_lawyerListView(generic.ListView):
    """
    Paginated view for listing all the Professional_lawyer objects.
    """
    model = Professional_lawyer
    template_name = "sc/professional_lawyer/professional_lawyer_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_lawyers')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Lawyer"
        context["var_main_desc"] = "Talking about law, no Descriptions IN Codebook."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'professional_lawyer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional lawyer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Professional_lawyerListViewAll(generic.ListView):
    """
    
    """
    model = Professional_lawyer
    template_name = "sc/professional_lawyer/professional_lawyer_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('professional_lawyers_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Professional_lawyer.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Professional Lawyer"
        context["var_main_desc"] = "Talking about law, no Descriptions IN Codebook."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Law"
        context["inner_vars"] = {'professional_lawyer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional lawyer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Professional_lawyerDetailView(generic.DetailView):
    """
    
    """
    model = Professional_lawyer
    template_name = "sc/professional_lawyer/professional_lawyer_detail.html"


@permission_required('core.view_capital')
def professional_lawyer_download(request):
    items = Professional_lawyer.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_professional_lawyer_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'professional_lawyer', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.professional_lawyer, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def professional_lawyer_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_professional_lawyers.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Law, NO_DESCRIPTIONS_IN_CODEBOOK.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Law'}
    my_meta_data_dic_inner_vars = {'professional_lawyer': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of professional lawyer for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Irrigation_systemCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Irrigation_system
    form_class = Irrigation_systemForm
    template_name = "sc/irrigation_system/irrigation_system_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('irrigation_system-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Irrigation System"
        context["my_exp"] = "Talking about Specialized Buildings, irrigation systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'irrigation_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of irrigation system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Irrigation_systemUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Irrigation_system
    form_class = Irrigation_systemForm
    template_name = "sc/irrigation_system/irrigation_system_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Irrigation System"

        return context

class Irrigation_systemDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Irrigation_system object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Irrigation_system
    success_url = reverse_lazy('irrigation_systems')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Irrigation_systemListView(generic.ListView):
    """
    Paginated view for listing all the Irrigation_system objects.
    """
    model = Irrigation_system
    template_name = "sc/irrigation_system/irrigation_system_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('irrigation_systems')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Irrigation System"
        context["var_main_desc"] = "Talking about specialized buildings, irrigation systems are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'irrigation_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of irrigation system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Irrigation_systemListViewAll(generic.ListView):
    """
    
    """
    model = Irrigation_system
    template_name = "sc/irrigation_system/irrigation_system_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('irrigation_systems_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Irrigation_system.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Irrigation System"
        context["var_main_desc"] = "Talking about specialized buildings, irrigation systems are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'irrigation_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of irrigation system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Irrigation_systemDetailView(generic.DetailView):
    """
    
    """
    model = Irrigation_system
    template_name = "sc/irrigation_system/irrigation_system_detail.html"


@permission_required('core.view_capital')
def irrigation_system_download(request):
    items = Irrigation_system.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_irrigation_system_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'irrigation_system', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.irrigation_system, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def irrigation_system_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_irrigation_systems.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Specialized Buildings, irrigation systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Specialized Buildings'}
    my_meta_data_dic_inner_vars = {'irrigation_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of irrigation system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Drinking_water_supply_systemCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Drinking_water_supply_system
    form_class = Drinking_water_supply_systemForm
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('drinking_water_supply_system-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Drinking Water Supply System"
        context["my_exp"] = "Talking about Specialized Buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'drinking_water_supply_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of drinking water supply system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Drinking_water_supply_systemUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Drinking_water_supply_system
    form_class = Drinking_water_supply_systemForm
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drinking Water Supply System"

        return context

class Drinking_water_supply_systemDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Drinking_water_supply_system object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Drinking_water_supply_system
    success_url = reverse_lazy('drinking_water_supply_systems')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Drinking_water_supply_systemListView(generic.ListView):
    """
    Paginated view for listing all the Drinking_water_supply_system objects.
    """
    model = Drinking_water_supply_system
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('drinking_water_supply_systems')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drinking Water Supply System"
        context["var_main_desc"] = "Talking about specialized buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'drinking_water_supply_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of drinking water supply system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Drinking_water_supply_systemListViewAll(generic.ListView):
    """
    
    """
    model = Drinking_water_supply_system
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('drinking_water_supply_systems_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Drinking_water_supply_system.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Drinking Water Supply System"
        context["var_main_desc"] = "Talking about specialized buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'drinking_water_supply_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of drinking water supply system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Drinking_water_supply_systemDetailView(generic.DetailView):
    """
    
    """
    model = Drinking_water_supply_system
    template_name = "sc/drinking_water_supply_system/drinking_water_supply_system_detail.html"


@permission_required('core.view_capital')
def drinking_water_supply_system_download(request):
    items = Drinking_water_supply_system.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_drinking_water_supply_system_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'drinking_water_supply_system', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.drinking_water_supply_system, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def drinking_water_supply_system_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_drinking_water_supply_systems.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Specialized Buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Specialized Buildings'}
    my_meta_data_dic_inner_vars = {'drinking_water_supply_system': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of drinking water supply system for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class MarketCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Market
    form_class = MarketForm
    template_name = "sc/market/market_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('market-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Market"
        context["my_exp"] = "Talking about Specialized Buildings, markets are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'market': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of market for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class MarketUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Market
    form_class = MarketForm
    template_name = "sc/market/market_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Market"

        return context

class MarketDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Market object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Market
    success_url = reverse_lazy('markets')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class MarketListView(generic.ListView):
    """
    Paginated view for listing all the Market objects.
    """
    model = Market
    template_name = "sc/market/market_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('markets')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Market"
        context["var_main_desc"] = "Talking about specialized buildings, markets are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'market': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of market for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class MarketListViewAll(generic.ListView):
    """
    
    """
    model = Market
    template_name = "sc/market/market_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('markets_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Market.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Market"
        context["var_main_desc"] = "Talking about specialized buildings, markets are polity owned (which includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'market': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of market for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class MarketDetailView(generic.DetailView):
    """
    
    """
    model = Market
    template_name = "sc/market/market_detail.html"


@permission_required('core.view_capital')
def market_download(request):
    items = Market.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_market_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'market', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.market, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def market_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_markets.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Specialized Buildings, markets are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Specialized Buildings'}
    my_meta_data_dic_inner_vars = {'market': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of market for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Food_storage_siteCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Food_storage_site
    form_class = Food_storage_siteForm
    template_name = "sc/food_storage_site/food_storage_site_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('food_storage_site-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Food Storage Site"
        context["my_exp"] = "Talking about Specialized Buildings, food storage sites are polity owned (which  includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'food_storage_site': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of food storage site for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Food_storage_siteUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Food_storage_site
    form_class = Food_storage_siteForm
    template_name = "sc/food_storage_site/food_storage_site_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Food Storage Site"

        return context

class Food_storage_siteDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Food_storage_site object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Food_storage_site
    success_url = reverse_lazy('food_storage_sites')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Food_storage_siteListView(generic.ListView):
    """
    Paginated view for listing all the Food_storage_site objects.
    """
    model = Food_storage_site
    template_name = "sc/food_storage_site/food_storage_site_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('food_storage_sites')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Food Storage Site"
        context["var_main_desc"] = "Talking about specialized buildings, food storage sites are polity owned (which  includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'food_storage_site': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of food storage site for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Food_storage_siteListViewAll(generic.ListView):
    """
    
    """
    model = Food_storage_site
    template_name = "sc/food_storage_site/food_storage_site_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('food_storage_sites_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Food_storage_site.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Food Storage Site"
        context["var_main_desc"] = "Talking about specialized buildings, food storage sites are polity owned (which  includes owned by the community, or the state), no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Specialized Buildings"
        context["inner_vars"] = {'food_storage_site': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of food storage site for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Food_storage_siteDetailView(generic.DetailView):
    """
    
    """
    model = Food_storage_site
    template_name = "sc/food_storage_site/food_storage_site_detail.html"


@permission_required('core.view_capital')
def food_storage_site_download(request):
    items = Food_storage_site.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_food_storage_site_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'food_storage_site', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.food_storage_site, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def food_storage_site_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_food_storage_sites.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Specialized Buildings, food storage sites are polity owned (which  includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Specialized Buildings'}
    my_meta_data_dic_inner_vars = {'food_storage_site': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of food storage site for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class RoadCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Road
    form_class = RoadForm
    template_name = "sc/road/road_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('road-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Road"
        context["my_exp"] = "Talking about Transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. It excludes streets/accessways within settlements and paths between settlements that develop through repeated use."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'road': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of road for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class RoadUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Road
    form_class = RoadForm
    template_name = "sc/road/road_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Road"

        return context

class RoadDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Road object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Road
    success_url = reverse_lazy('roads')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class RoadListView(generic.ListView):
    """
    Paginated view for listing all the Road objects.
    """
    model = Road
    template_name = "sc/road/road_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('roads')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Road"
        context["var_main_desc"] = "Talking about transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. it excludes streets/accessways within settlements and paths between settlements that develop through repeated use."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'road': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of road for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class RoadListViewAll(generic.ListView):
    """
    
    """
    model = Road
    template_name = "sc/road/road_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('roads_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Road.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Road"
        context["var_main_desc"] = "Talking about transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. it excludes streets/accessways within settlements and paths between settlements that develop through repeated use."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'road': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of road for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class RoadDetailView(generic.DetailView):
    """
    
    """
    model = Road
    template_name = "sc/road/road_detail.html"


@permission_required('core.view_capital')
def road_download(request):
    items = Road.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_road_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'road', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.road, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def road_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_roads.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. It excludes streets/accessways within settlements and paths between settlements that develop through repeated use.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Transport infrastructure'}
    my_meta_data_dic_inner_vars = {'road': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of road for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class BridgeCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Bridge
    form_class = BridgeForm
    template_name = "sc/bridge/bridge_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('bridge-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Bridge"
        context["my_exp"] = "Talking about Transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it)."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'bridge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of bridge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class BridgeUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Bridge
    form_class = BridgeForm
    template_name = "sc/bridge/bridge_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Bridge"

        return context

class BridgeDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Bridge object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Bridge
    success_url = reverse_lazy('bridges')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class BridgeListView(generic.ListView):
    """
    Paginated view for listing all the Bridge objects.
    """
    model = Bridge
    template_name = "sc/bridge/bridge_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('bridges')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Bridge"
        context["var_main_desc"] = "Talking about transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'bridge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of bridge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class BridgeListViewAll(generic.ListView):
    """
    
    """
    model = Bridge
    template_name = "sc/bridge/bridge_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('bridges_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Bridge.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Bridge"
        context["var_main_desc"] = "Talking about transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'bridge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of bridge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class BridgeDetailView(generic.DetailView):
    """
    
    """
    model = Bridge
    template_name = "sc/bridge/bridge_detail.html"


@permission_required('core.view_capital')
def bridge_download(request):
    items = Bridge.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_bridge_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'bridge', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.bridge, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def bridge_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_bridges.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it).", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Transport infrastructure'}
    my_meta_data_dic_inner_vars = {'bridge': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of bridge for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class CanalCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Canal
    form_class = CanalForm
    template_name = "sc/canal/canal_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('canal-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Canal"
        context["my_exp"] = "Talking about Transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it)."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'canal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of canal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class CanalUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Canal
    form_class = CanalForm
    template_name = "sc/canal/canal_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Canal"

        return context

class CanalDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Canal object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Canal
    success_url = reverse_lazy('canals')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class CanalListView(generic.ListView):
    """
    Paginated view for listing all the Canal objects.
    """
    model = Canal
    template_name = "sc/canal/canal_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('canals')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Canal"
        context["var_main_desc"] = "Talking about transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'canal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of canal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class CanalListViewAll(generic.ListView):
    """
    
    """
    model = Canal
    template_name = "sc/canal/canal_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('canals_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Canal.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Canal"
        context["var_main_desc"] = "Talking about transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it)."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'canal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of canal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class CanalDetailView(generic.DetailView):
    """
    
    """
    model = Canal
    template_name = "sc/canal/canal_detail.html"


@permission_required('core.view_capital')
def canal_download(request):
    items = Canal.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_canal_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'canal', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.canal, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def canal_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_canals.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it).", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Transport infrastructure'}
    my_meta_data_dic_inner_vars = {'canal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of canal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class PortCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Port
    form_class = PortForm
    template_name = "sc/port/port_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('port-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Port"
        context["my_exp"] = "Talking about Transport infrastructure, Ports include river ports. Direct historical or archaeological evidence of Ports is absent when no port has been excavated or all evidence of such has been obliterated. Indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta Egypt at a time we know there was a timber trade with the Levant). When evidence for the variable itself is available the code is 'present.' When other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). When indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'port': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of port for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class PortUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Port
    form_class = PortForm
    template_name = "sc/port/port_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Port"

        return context

class PortDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Port object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Port
    success_url = reverse_lazy('ports')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class PortListView(generic.ListView):
    """
    Paginated view for listing all the Port objects.
    """
    model = Port
    template_name = "sc/port/port_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('ports')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Port"
        context["var_main_desc"] = "Talking about transport infrastructure, ports include river ports. direct historical or archaeological evidence of ports is absent when no port has been excavated or all evidence of such has been obliterated. indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta egypt at a time we know there was a timber trade with the levant). when evidence for the variable itself is available the code is 'present.' when other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). when indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'port': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of port for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class PortListViewAll(generic.ListView):
    """
    
    """
    model = Port
    template_name = "sc/port/port_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('ports_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Port.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Port"
        context["var_main_desc"] = "Talking about transport infrastructure, ports include river ports. direct historical or archaeological evidence of ports is absent when no port has been excavated or all evidence of such has been obliterated. indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta egypt at a time we know there was a timber trade with the levant). when evidence for the variable itself is available the code is 'present.' when other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). when indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Transport infrastructure"
        context["inner_vars"] = {'port': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of port for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class PortDetailView(generic.DetailView):
    """
    
    """
    model = Port
    template_name = "sc/port/port_detail.html"


@permission_required('core.view_capital')
def port_download(request):
    items = Port.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_port_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'port', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.port, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def port_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_ports.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Transport infrastructure, Ports include river ports. Direct historical or archaeological evidence of Ports is absent when no port has been excavated or all evidence of such has been obliterated. Indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta Egypt at a time we know there was a timber trade with the Levant). When evidence for the variable itself is available the code is 'present.' When other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). When indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown.", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Transport infrastructure'}
    my_meta_data_dic_inner_vars = {'port': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of port for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Mines_or_quarryCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Mines_or_quarry
    form_class = Mines_or_quarryForm
    template_name = "sc/mines_or_quarry/mines_or_quarry_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('mines_or_quarry-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Mines or Quarry"
        context["my_exp"] = "Talking about Special purpose sites, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'mines_or_quarry': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mines or quarry for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Mines_or_quarryUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Mines_or_quarry
    form_class = Mines_or_quarryForm
    template_name = "sc/mines_or_quarry/mines_or_quarry_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mines or Quarry"

        return context

class Mines_or_quarryDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Mines_or_quarry object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Mines_or_quarry
    success_url = reverse_lazy('mines_or_quarrys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Mines_or_quarryListView(generic.ListView):
    """
    Paginated view for listing all the Mines_or_quarry objects.
    """
    model = Mines_or_quarry
    template_name = "sc/mines_or_quarry/mines_or_quarry_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('mines_or_quarrys')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mines or Quarry"
        context["var_main_desc"] = "Talking about special purpose sites, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Special purpose sites"
        context["inner_vars"] = {'mines_or_quarry': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mines or quarry for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Mines_or_quarryListViewAll(generic.ListView):
    """
    
    """
    model = Mines_or_quarry
    template_name = "sc/mines_or_quarry/mines_or_quarry_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('mines_or_quarrys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Mines_or_quarry.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mines or Quarry"
        context["var_main_desc"] = "Talking about special purpose sites, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Special purpose sites"
        context["inner_vars"] = {'mines_or_quarry': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mines or quarry for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Mines_or_quarryDetailView(generic.DetailView):
    """
    
    """
    model = Mines_or_quarry
    template_name = "sc/mines_or_quarry/mines_or_quarry_detail.html"


@permission_required('core.view_capital')
def mines_or_quarry_download(request):
    items = Mines_or_quarry.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_mine_or_quarry_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'mines_or_quarry', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.mines_or_quarry, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def mines_or_quarry_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_mines_or_quarrys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Special purpose sites, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Special purpose sites'}
    my_meta_data_dic_inner_vars = {'mines_or_quarry': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mines or quarry for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Mnemonic_deviceCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Mnemonic_device
    form_class = Mnemonic_deviceForm
    template_name = "sc/mnemonic_device/mnemonic_device_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('mnemonic_device-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Mnemonic Device"
        context["my_exp"] = "Talking about Writing Systems, Mnemonic devices are: For example, tallies"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'mnemonic_device': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mnemonic device for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Mnemonic_deviceUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Mnemonic_device
    form_class = Mnemonic_deviceForm
    template_name = "sc/mnemonic_device/mnemonic_device_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mnemonic Device"

        return context

class Mnemonic_deviceDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Mnemonic_device object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Mnemonic_device
    success_url = reverse_lazy('mnemonic_devices')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Mnemonic_deviceListView(generic.ListView):
    """
    Paginated view for listing all the Mnemonic_device objects.
    """
    model = Mnemonic_device
    template_name = "sc/mnemonic_device/mnemonic_device_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('mnemonic_devices')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mnemonic Device"
        context["var_main_desc"] = "Talking about writing systems, mnemonic devices are: for example, tallies"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'mnemonic_device': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mnemonic device for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Mnemonic_deviceListViewAll(generic.ListView):
    """
    
    """
    model = Mnemonic_device
    template_name = "sc/mnemonic_device/mnemonic_device_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('mnemonic_devices_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Mnemonic_device.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Mnemonic Device"
        context["var_main_desc"] = "Talking about writing systems, mnemonic devices are: for example, tallies"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'mnemonic_device': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mnemonic device for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Mnemonic_deviceDetailView(generic.DetailView):
    """
    
    """
    model = Mnemonic_device
    template_name = "sc/mnemonic_device/mnemonic_device_detail.html"


@permission_required('core.view_capital')
def mnemonic_device_download(request):
    items = Mnemonic_device.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_mnemonic_device_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'mnemonic_device', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.mnemonic_device, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def mnemonic_device_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_mnemonic_devices.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, Mnemonic devices are: For example, tallies', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'mnemonic_device': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of mnemonic device for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Nonwritten_recordCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Nonwritten_record
    form_class = Nonwritten_recordForm
    template_name = "sc/nonwritten_record/nonwritten_record_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('nonwritten_record-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Nonwritten Record"
        context["my_exp"] = "Talking about Writing Systems, Nonwritten Records are more extensive than mnemonics, but don't utilize script. Example: quipu; seals and stamps"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'nonwritten_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of nonwritten record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Nonwritten_recordUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Nonwritten_record
    form_class = Nonwritten_recordForm
    template_name = "sc/nonwritten_record/nonwritten_record_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Nonwritten Record"

        return context

class Nonwritten_recordDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Nonwritten_record object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Nonwritten_record
    success_url = reverse_lazy('nonwritten_records')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Nonwritten_recordListView(generic.ListView):
    """
    Paginated view for listing all the Nonwritten_record objects.
    """
    model = Nonwritten_record
    template_name = "sc/nonwritten_record/nonwritten_record_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('nonwritten_records')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Nonwritten Record"
        context["var_main_desc"] = "Talking about writing systems, nonwritten records are more extensive than mnemonics, but don't utilize script. example: quipu; seals and stamps"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'nonwritten_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of nonwritten record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Nonwritten_recordListViewAll(generic.ListView):
    """
    
    """
    model = Nonwritten_record
    template_name = "sc/nonwritten_record/nonwritten_record_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('nonwritten_records_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Nonwritten_record.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Nonwritten Record"
        context["var_main_desc"] = "Talking about writing systems, nonwritten records are more extensive than mnemonics, but don't utilize script. example: quipu; seals and stamps"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'nonwritten_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of nonwritten record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Nonwritten_recordDetailView(generic.DetailView):
    """
    
    """
    model = Nonwritten_record
    template_name = "sc/nonwritten_record/nonwritten_record_detail.html"


@permission_required('core.view_capital')
def nonwritten_record_download(request):
    items = Nonwritten_record.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_nonwritten_record_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'nonwritten_record', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.nonwritten_record, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def nonwritten_record_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_nonwritten_records.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about Writing Systems, Nonwritten Records are more extensive than mnemonics, but don't utilize script. Example: quipu; seals and stamps", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'nonwritten_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of nonwritten record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Written_recordCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Written_record
    form_class = Written_recordForm
    template_name = "sc/written_record/written_record_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('written_record-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Written Record"
        context["my_exp"] = "Talking about Writing Systems, Written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. There must be several sentences strung together, at the very minimum. For example, royal proclamations from Mesopotamia and Egypt qualify as written records"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'written_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of written record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Written_recordUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Written_record
    form_class = Written_recordForm
    template_name = "sc/written_record/written_record_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Written Record"

        return context

class Written_recordDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Written_record object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Written_record
    success_url = reverse_lazy('written_records')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Written_recordListView(generic.ListView):
    """
    Paginated view for listing all the Written_record objects.
    """
    model = Written_record
    template_name = "sc/written_record/written_record_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('written_records')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Written Record"
        context["var_main_desc"] = "Talking about writing systems, written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. there must be several sentences strung together, at the very minimum. for example, royal proclamations from mesopotamia and egypt qualify as written records"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'written_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of written record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Written_recordListViewAll(generic.ListView):
    """
    
    """
    model = Written_record
    template_name = "sc/written_record/written_record_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('written_records_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Written_record.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Written Record"
        context["var_main_desc"] = "Talking about writing systems, written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. there must be several sentences strung together, at the very minimum. for example, royal proclamations from mesopotamia and egypt qualify as written records"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'written_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of written record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Written_recordDetailView(generic.DetailView):
    """
    
    """
    model = Written_record
    template_name = "sc/written_record/written_record_detail.html"


@permission_required('core.view_capital')
def written_record_download(request):
    items = Written_record.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_written_records_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'written_record', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.written_record, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def written_record_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_written_records.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, Written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. There must be several sentences strung together, at the very minimum. For example, royal proclamations from Mesopotamia and Egypt qualify as written records', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'written_record': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of written record for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class ScriptCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Script
    form_class = ScriptForm
    template_name = "sc/script/script_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('script-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Script"
        context["my_exp"] = "Talking about Writing Systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'script': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of script for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class ScriptUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Script
    form_class = ScriptForm
    template_name = "sc/script/script_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Script"

        return context

class ScriptDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Script object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Script
    success_url = reverse_lazy('scripts')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class ScriptListView(generic.ListView):
    """
    Paginated view for listing all the Script objects.
    """
    model = Script
    template_name = "sc/script/script_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('scripts')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Script"
        context["var_main_desc"] = "Talking about writing systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'script': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of script for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class ScriptListViewAll(generic.ListView):
    """
    
    """
    model = Script
    template_name = "sc/script/script_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('scripts_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Script.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Script"
        context["var_main_desc"] = "Talking about writing systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'script': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of script for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class ScriptDetailView(generic.DetailView):
    """
    
    """
    model = Script
    template_name = "sc/script/script_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     my_instance_id = self.object.pk
    #     context["myvar"] = "Script"
    #     content_type = ContentType.objects.get_for_model(self.model)
    #     print(f'content_type:             {content_type}')
    #     print(f'my_instance_id:             {my_instance_id}')
    #     crud_events = CRUDEvent.objects.filter(
    #         content_type_id=content_type,
    #         object_id=445
    #     )

    #     context['cruds'] = crud_events

    #     print(context)

    #     return context



@permission_required('core.view_capital')
def script_download(request):
    items = Script.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_script_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'script', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.script, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def script_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_scripts.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'script': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of script for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Non_phonetic_writingCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Non_phonetic_writing
    form_class = Non_phonetic_writingForm
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('non_phonetic_writing-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Non Phonetic Writing"
        context["my_exp"] = "Talking about Writing Systems, this refers to the kind of script"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'non_phonetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of non phonetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Non_phonetic_writingUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Non_phonetic_writing
    form_class = Non_phonetic_writingForm
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Non Phonetic Writing"

        return context

class Non_phonetic_writingDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Non_phonetic_writing object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Non_phonetic_writing
    success_url = reverse_lazy('non_phonetic_writings')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Non_phonetic_writingListView(generic.ListView):
    """
    Paginated view for listing all the Non_phonetic_writing objects.
    """
    model = Non_phonetic_writing
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('non_phonetic_writings')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Non Phonetic Writing"
        context["var_main_desc"] = "Talking about writing systems, this refers to the kind of script"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'non_phonetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of non phonetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Non_phonetic_writingListViewAll(generic.ListView):
    """
    
    """
    model = Non_phonetic_writing
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('non_phonetic_writings_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Non_phonetic_writing.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Non Phonetic Writing"
        context["var_main_desc"] = "Talking about writing systems, this refers to the kind of script"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'non_phonetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of non phonetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Non_phonetic_writingDetailView(generic.DetailView):
    """
    
    """
    model = Non_phonetic_writing
    template_name = "sc/non_phonetic_writing/non_phonetic_writing_detail.html"


@permission_required('core.view_capital')
def non_phonetic_writing_download(request):
    items = Non_phonetic_writing.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_non_phonetic_writing_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'non_phonetic_writing', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.non_phonetic_writing, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def non_phonetic_writing_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_non_phonetic_writings.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, this refers to the kind of script', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'non_phonetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of non phonetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Phonetic_alphabetic_writingCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Phonetic_alphabetic_writing
    form_class = Phonetic_alphabetic_writingForm
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('phonetic_alphabetic_writing-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Phonetic Alphabetic Writing"
        context["my_exp"] = "Talking about Writing Systems, this refers to the kind of script"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'phonetic_alphabetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of phonetic alphabetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Phonetic_alphabetic_writingUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Phonetic_alphabetic_writing
    form_class = Phonetic_alphabetic_writingForm
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Phonetic Alphabetic Writing"

        return context

class Phonetic_alphabetic_writingDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Phonetic_alphabetic_writing object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Phonetic_alphabetic_writing
    success_url = reverse_lazy('phonetic_alphabetic_writings')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Phonetic_alphabetic_writingListView(generic.ListView):
    """
    Paginated view for listing all the Phonetic_alphabetic_writing objects.
    """
    model = Phonetic_alphabetic_writing
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('phonetic_alphabetic_writings')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Phonetic Alphabetic Writing"
        context["var_main_desc"] = "Talking about writing systems, this refers to the kind of script"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'phonetic_alphabetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of phonetic alphabetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Phonetic_alphabetic_writingListViewAll(generic.ListView):
    """
    
    """
    model = Phonetic_alphabetic_writing
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('phonetic_alphabetic_writings_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Phonetic_alphabetic_writing.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Phonetic Alphabetic Writing"
        context["var_main_desc"] = "Talking about writing systems, this refers to the kind of script"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Writing Systems"
        context["inner_vars"] = {'phonetic_alphabetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of phonetic alphabetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Phonetic_alphabetic_writingDetailView(generic.DetailView):
    """
    
    """
    model = Phonetic_alphabetic_writing
    template_name = "sc/phonetic_alphabetic_writing/phonetic_alphabetic_writing_detail.html"


@permission_required('core.view_capital')
def phonetic_alphabetic_writing_download(request):
    items = Phonetic_alphabetic_writing.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_phonetic_alphabetic_writing_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'phonetic_alphabetic_writing', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.phonetic_alphabetic_writing, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def phonetic_alphabetic_writing_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_phonetic_alphabetic_writings.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Writing Systems, this refers to the kind of script', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Writing Systems'}
    my_meta_data_dic_inner_vars = {'phonetic_alphabetic_writing': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of phonetic alphabetic writing for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Lists_tables_and_classificationCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Lists_tables_and_classification
    form_class = Lists_tables_and_classificationForm
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('lists_tables_and_classification-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Lists Tables and Classification"
        context["my_exp"] = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'lists_tables_and_classification': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of lists tables and classification for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Lists_tables_and_classificationUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Lists_tables_and_classification
    form_class = Lists_tables_and_classificationForm
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Lists Tables and Classification"

        return context

class Lists_tables_and_classificationDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Lists_tables_and_classification object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Lists_tables_and_classification
    success_url = reverse_lazy('lists_tables_and_classifications')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Lists_tables_and_classificationListView(generic.ListView):
    """
    Paginated view for listing all the Lists_tables_and_classification objects.
    """
    model = Lists_tables_and_classification
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('lists_tables_and_classifications')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Lists Tables and Classification"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'lists_tables_and_classification': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of lists tables and classification for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Lists_tables_and_classificationListViewAll(generic.ListView):
    """
    
    """
    model = Lists_tables_and_classification
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('lists_tables_and_classifications_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Lists_tables_and_classification.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Lists Tables and Classification"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'lists_tables_and_classification': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of lists tables and classification for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Lists_tables_and_classificationDetailView(generic.DetailView):
    """
    
    """
    model = Lists_tables_and_classification
    template_name = "sc/lists_tables_and_classification/lists_tables_and_classification_detail.html"


@permission_required('core.view_capital')
def lists_tables_and_classification_download(request):
    items = Lists_tables_and_classification.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_list_table_and_classification_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'lists_tables_and_classification', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.lists_tables_and_classification, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def lists_tables_and_classification_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_lists_tables_and_classifications.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'lists_tables_and_classification': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of lists tables and classification for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class CalendarCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Calendar
    form_class = CalendarForm
    template_name = "sc/calendar/calendar_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('calendar-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Calendar"
        context["my_exp"] = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'calendar': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of calendar for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class CalendarUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Calendar
    form_class = CalendarForm
    template_name = "sc/calendar/calendar_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Calendar"

        return context

class CalendarDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Calendar object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Calendar
    success_url = reverse_lazy('calendars')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class CalendarListView(generic.ListView):
    """
    Paginated view for listing all the Calendar objects.
    """
    model = Calendar
    template_name = "sc/calendar/calendar_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('calendars')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Calendar"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'calendar': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of calendar for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class CalendarListViewAll(generic.ListView):
    """
    
    """
    model = Calendar
    template_name = "sc/calendar/calendar_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('calendars_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Calendar.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Calendar"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'calendar': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of calendar for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class CalendarDetailView(generic.DetailView):
    """
    
    """
    model = Calendar
    template_name = "sc/calendar/calendar_detail.html"


@permission_required('core.view_capital')
def calendar_download(request):
    items = Calendar.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_calendar_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'calendar', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.calendar, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def calendar_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_calendars.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'calendar': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of calendar for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Sacred_textCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Sacred_text
    form_class = Sacred_textForm
    template_name = "sc/sacred_text/sacred_text_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('sacred_text-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Sacred Text"
        context["my_exp"] = "Talking about Kinds of Written Documents, Sacred Texts originate from supernatural agents (deities), or are directly inspired by them."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'sacred_text': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of sacred text for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Sacred_textUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Sacred_text
    form_class = Sacred_textForm
    template_name = "sc/sacred_text/sacred_text_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sacred Text"

        return context

class Sacred_textDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Sacred_text object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Sacred_text
    success_url = reverse_lazy('sacred_texts')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Sacred_textListView(generic.ListView):
    """
    Paginated view for listing all the Sacred_text objects.
    """
    model = Sacred_text
    template_name = "sc/sacred_text/sacred_text_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('sacred_texts')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sacred Text"
        context["var_main_desc"] = "Talking about kinds of written documents, sacred texts originate from supernatural agents (deities), or are directly inspired by them."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'sacred_text': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of sacred text for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Sacred_textListViewAll(generic.ListView):
    """
    
    """
    model = Sacred_text
    template_name = "sc/sacred_text/sacred_text_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('sacred_texts_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Sacred_text.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Sacred Text"
        context["var_main_desc"] = "Talking about kinds of written documents, sacred texts originate from supernatural agents (deities), or are directly inspired by them."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'sacred_text': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of sacred text for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Sacred_textDetailView(generic.DetailView):
    """
    
    """
    model = Sacred_text
    template_name = "sc/sacred_text/sacred_text_detail.html"


@permission_required('core.view_capital')
def sacred_text_download(request):
    items = Sacred_text.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_sacred_text_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'sacred_text', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.sacred_text, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def sacred_text_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_sacred_texts.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, Sacred Texts originate from supernatural agents (deities), or are directly inspired by them.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'sacred_text': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of sacred text for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Religious_literatureCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Religious_literature
    form_class = Religious_literatureForm
    template_name = "sc/religious_literature/religious_literature_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('religious_literature-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Religious Literature"
        context["my_exp"] = "Talking about Kinds of Written Documents, Religious literature differs from the sacred texts. For example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'religious_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of religious literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Religious_literatureUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Religious_literature
    form_class = Religious_literatureForm
    template_name = "sc/religious_literature/religious_literature_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Literature"

        return context

class Religious_literatureDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Religious_literature object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Religious_literature
    success_url = reverse_lazy('religious_literatures')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Religious_literatureListView(generic.ListView):
    """
    Paginated view for listing all the Religious_literature objects.
    """
    model = Religious_literature
    template_name = "sc/religious_literature/religious_literature_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('religious_literatures')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, religious literature differs from the sacred texts. for example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'religious_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of religious literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Religious_literatureListViewAll(generic.ListView):
    """
    
    """
    model = Religious_literature
    template_name = "sc/religious_literature/religious_literature_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('religious_literatures_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Religious_literature.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Religious Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, religious literature differs from the sacred texts. for example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'religious_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of religious literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Religious_literatureDetailView(generic.DetailView):
    """
    
    """
    model = Religious_literature
    template_name = "sc/religious_literature/religious_literature_detail.html"


@permission_required('core.view_capital')
def religious_literature_download(request):
    items = Religious_literature.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_religious_literature_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'religious_literature', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.religious_literature, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def religious_literature_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_religious_literatures.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, Religious literature differs from the sacred texts. For example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'religious_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of religious literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Practical_literatureCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Practical_literature
    form_class = Practical_literatureForm
    template_name = "sc/practical_literature/practical_literature_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('practical_literature-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Practical Literature"
        context["my_exp"] = "Talking about Kinds of Written Documents, Practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. Letters do not count as practical literature."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'practical_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of practical literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Practical_literatureUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Practical_literature
    form_class = Practical_literatureForm
    template_name = "sc/practical_literature/practical_literature_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Practical Literature"

        return context

class Practical_literatureDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Practical_literature object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Practical_literature
    success_url = reverse_lazy('practical_literatures')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Practical_literatureListView(generic.ListView):
    """
    Paginated view for listing all the Practical_literature objects.
    """
    model = Practical_literature
    template_name = "sc/practical_literature/practical_literature_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('practical_literatures')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Practical Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. letters do not count as practical literature."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'practical_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of practical literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Practical_literatureListViewAll(generic.ListView):
    """
    
    """
    model = Practical_literature
    template_name = "sc/practical_literature/practical_literature_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('practical_literatures_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Practical_literature.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Practical Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. letters do not count as practical literature."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'practical_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of practical literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Practical_literatureDetailView(generic.DetailView):
    """
    
    """
    model = Practical_literature
    template_name = "sc/practical_literature/practical_literature_detail.html"


@permission_required('core.view_capital')
def practical_literature_download(request):
    items = Practical_literature.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_practical_literature_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'practical_literature', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.practical_literature, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def practical_literature_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_practical_literatures.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, Practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. Letters do not count as practical literature.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'practical_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of practical literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class HistoryCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = History
    form_class = HistoryForm
    template_name = "sc/history/history_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('history-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "History"
        context["my_exp"] = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'history': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of history for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class HistoryUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = History
    form_class = HistoryForm
    template_name = "sc/history/history_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "History"

        return context

class HistoryDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing History object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = History
    success_url = reverse_lazy('historys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class HistoryListView(generic.ListView):
    """
    Paginated view for listing all the History objects.
    """
    model = History
    template_name = "sc/history/history_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('historys')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "History"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'history': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of history for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class HistoryListViewAll(generic.ListView):
    """
    
    """
    model = History
    template_name = "sc/history/history_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('historys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = History.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "History"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'history': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of history for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class HistoryDetailView(generic.DetailView):
    """
    
    """
    model = History
    template_name = "sc/history/history_detail.html"


@permission_required('core.view_capital')
def history_download(request):
    items = History.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_history_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'history', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.history, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def history_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_historys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'history': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of history for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class PhilosophyCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Philosophy
    form_class = PhilosophyForm
    template_name = "sc/philosophy/philosophy_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('philosophy-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Philosophy"
        context["my_exp"] = "Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'philosophy': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of philosophy for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class PhilosophyUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Philosophy
    form_class = PhilosophyForm
    template_name = "sc/philosophy/philosophy_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Philosophy"

        return context

class PhilosophyDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Philosophy object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Philosophy
    success_url = reverse_lazy('philosophys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class PhilosophyListView(generic.ListView):
    """
    Paginated view for listing all the Philosophy objects.
    """
    model = Philosophy
    template_name = "sc/philosophy/philosophy_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('philosophys')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Philosophy"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'philosophy': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of philosophy for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class PhilosophyListViewAll(generic.ListView):
    """
    
    """
    model = Philosophy
    template_name = "sc/philosophy/philosophy_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('philosophys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Philosophy.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Philosophy"
        context["var_main_desc"] = "Talking about kinds of written documents, no Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'philosophy': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of philosophy for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class PhilosophyDetailView(generic.DetailView):
    """
    
    """
    model = Philosophy
    template_name = "sc/philosophy/philosophy_detail.html"


@permission_required('core.view_capital')
def philosophy_download(request):
    items = Philosophy.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_philosophy_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'philosophy', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.philosophy, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def philosophy_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_philosophys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'philosophy': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of philosophy for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Scientific_literatureCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Scientific_literature
    form_class = Scientific_literatureForm
    template_name = "sc/scientific_literature/scientific_literature_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('scientific_literature-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Scientific Literature"
        context["my_exp"] = "Talking about Kinds of Written Documents, Scientific literature includes mathematics, natural sciences, social sciences"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'scientific_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of scientific literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Scientific_literatureUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Scientific_literature
    form_class = Scientific_literatureForm
    template_name = "sc/scientific_literature/scientific_literature_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Scientific Literature"

        return context

class Scientific_literatureDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Scientific_literature object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Scientific_literature
    success_url = reverse_lazy('scientific_literatures')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Scientific_literatureListView(generic.ListView):
    """
    Paginated view for listing all the Scientific_literature objects.
    """
    model = Scientific_literature
    template_name = "sc/scientific_literature/scientific_literature_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('scientific_literatures')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Scientific Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, scientific literature includes mathematics, natural sciences, social sciences"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'scientific_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of scientific literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Scientific_literatureListViewAll(generic.ListView):
    """
    
    """
    model = Scientific_literature
    template_name = "sc/scientific_literature/scientific_literature_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('scientific_literatures_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Scientific_literature.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Scientific Literature"
        context["var_main_desc"] = "Talking about kinds of written documents, scientific literature includes mathematics, natural sciences, social sciences"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'scientific_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of scientific literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Scientific_literatureDetailView(generic.DetailView):
    """
    
    """
    model = Scientific_literature
    template_name = "sc/scientific_literature/scientific_literature_detail.html"


@permission_required('core.view_capital')
def scientific_literature_download(request):
    items = Scientific_literature.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_scientific_literature_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'scientific_literature', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.scientific_literature, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def scientific_literature_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_scientific_literatures.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, Scientific literature includes mathematics, natural sciences, social sciences', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'scientific_literature': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of scientific literature for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class FictionCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Fiction
    form_class = FictionForm
    template_name = "sc/fiction/fiction_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('fiction-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Fiction"
        context["my_exp"] = "Talking about Kinds of Written Documents, fiction includes poetry."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'fiction': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of fiction for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class FictionUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Fiction
    form_class = FictionForm
    template_name = "sc/fiction/fiction_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Fiction"

        return context

class FictionDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Fiction object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Fiction
    success_url = reverse_lazy('fictions')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class FictionListView(generic.ListView):
    """
    Paginated view for listing all the Fiction objects.
    """
    model = Fiction
    template_name = "sc/fiction/fiction_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('fictions')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Fiction"
        context["var_main_desc"] = "Talking about kinds of written documents, fiction includes poetry."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'fiction': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of fiction for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class FictionListViewAll(generic.ListView):
    """
    
    """
    model = Fiction
    template_name = "sc/fiction/fiction_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('fictions_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Fiction.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Fiction"
        context["var_main_desc"] = "Talking about kinds of written documents, fiction includes poetry."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Kinds of Written Documents"
        context["inner_vars"] = {'fiction': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of fiction for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class FictionDetailView(generic.DetailView):
    """
    
    """
    model = Fiction
    template_name = "sc/fiction/fiction_detail.html"


@permission_required('core.view_capital')
def fiction_download(request):
    items = Fiction.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_fiction_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'fiction', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.fiction, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def fiction_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_fictions.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about Kinds of Written Documents, fiction includes poetry.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Kinds of Written Documents'}
    my_meta_data_dic_inner_vars = {'fiction': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of fiction for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class ArticleCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Article
    form_class = ArticleForm
    template_name = "sc/article/article_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('article-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Article"
        context["my_exp"] = "Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'article': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of article for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Article
    form_class = ArticleForm
    template_name = "sc/article/article_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Article"
        context["testvar"] = ["a", "bb", "ccc"]
        context["citations_list"] = Reference.objects.all()

        return context

class ArticleDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Article object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Article
    success_url = reverse_lazy('articles')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class ArticleListView(generic.ListView):
    """
    Paginated view for listing all the Article objects.
    """
    model = Article
    template_name = "sc/article/article_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('articles')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Article"
        context["var_main_desc"] = "Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'article': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of article for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class ArticleListViewAll(generic.ListView):
    """
    
    """
    model = Article
    template_name = "sc/article/article_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('articles_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Article.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Article"
        context["var_main_desc"] = "Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'article': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of article for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class ArticleDetailView(generic.DetailView):
    """
    
    """
    model = Article
    template_name = "sc/article/article_detail.html"


@permission_required('core.view_capital')
def article_download(request):
    items = Article.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_article_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'article', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.article, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def article_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_articles.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'article': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of article for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class TokenCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Token
    form_class = TokenForm
    template_name = "sc/token/token_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('token-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Token"
        context["my_exp"] = "Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'token': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of token for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class TokenUpdate(PermissionRequiredMixin, UpdateView):
    """
    
    """
    model = Token
    form_class = TokenForm
    template_name = "sc/token/token_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Token"

        return context

class TokenDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Token object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Token
    success_url = reverse_lazy('tokens')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class TokenListView(generic.ListView):
    """
    Paginated view for listing all the Token objects.
    """
    model = Token
    template_name = "sc/token/token_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('tokens')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Token"
        context["var_main_desc"] = "Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'token': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of token for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class TokenListViewAll(generic.ListView):
    """
    
    """
    model = Token
    template_name = "sc/token/token_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('tokens_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Token.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Token"
        context["var_main_desc"] = "Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'token': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of token for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class TokenDetailView(generic.DetailView):
    """
    
    """
    model = Token
    template_name = "sc/token/token_detail.html"


@permission_required('core.view_capital')
def token_download(request):
    items = Token.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_token_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'token', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.token, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def token_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_tokens.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'token': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of token for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Precious_metalCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Precious_metal
    form_class = Precious_metalForm
    template_name = "sc/precious_metal/precious_metal_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('precious_metal-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Precious Metal"
        context["my_exp"] = "Talking about forms of money, Precious metals are non-coined silver, gold, platinum"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'precious_metal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of precious metal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Precious_metalUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Precious_metal
    form_class = Precious_metalForm
    template_name = "sc/precious_metal/precious_metal_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Precious Metal"

        return context

class Precious_metalDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Precious_metal object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Precious_metal
    success_url = reverse_lazy('precious_metals')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Precious_metalListView(generic.ListView):
    """
    Paginated view for listing all the Precious_metal objects.
    """
    model = Precious_metal
    template_name = "sc/precious_metal/precious_metal_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('precious_metals')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Precious Metal"
        context["var_main_desc"] = "Talking about forms of money, precious metals are non-coined silver, gold, platinum"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'precious_metal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of precious metal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Precious_metalListViewAll(generic.ListView):
    """
    
    """
    model = Precious_metal
    template_name = "sc/precious_metal/precious_metal_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('precious_metals_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Precious_metal.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Precious Metal"
        context["var_main_desc"] = "Talking about forms of money, precious metals are non-coined silver, gold, platinum"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'precious_metal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of precious metal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Precious_metalDetailView(generic.DetailView):
    """
    
    """
    model = Precious_metal
    template_name = "sc/precious_metal/precious_metal_detail.html"


@permission_required('core.view_capital')
def precious_metal_download(request):
    items = Precious_metal.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_precious_metal_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'precious_metal', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.precious_metal, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def precious_metal_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_precious_metals.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about forms of money, Precious metals are non-coined silver, gold, platinum', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'precious_metal': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of precious metal for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Foreign_coinCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Foreign_coin
    form_class = Foreign_coinForm
    template_name = "sc/foreign_coin/foreign_coin_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('foreign_coin-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Foreign Coin"
        context["my_exp"] = "NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'foreign_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of foreign coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Foreign_coinUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Foreign_coin
    form_class = Foreign_coinForm
    template_name = "sc/foreign_coin/foreign_coin_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Foreign Coin"

        return context

class Foreign_coinDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Foreign_coin object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Foreign_coin
    success_url = reverse_lazy('foreign_coins')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Foreign_coinListView(generic.ListView):
    """
    Paginated view for listing all the Foreign_coin objects.
    """
    model = Foreign_coin
    template_name = "sc/foreign_coin/foreign_coin_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('foreign_coins')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Foreign Coin"
        context["var_main_desc"] = "NO Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'foreign_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of foreign coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Foreign_coinListViewAll(generic.ListView):
    """
    
    """
    model = Foreign_coin
    template_name = "sc/foreign_coin/foreign_coin_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('foreign_coins_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Foreign_coin.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Foreign Coin"
        context["var_main_desc"] = "NO Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'foreign_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of foreign coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Foreign_coinDetailView(generic.DetailView):
    """
    
    """
    model = Foreign_coin
    template_name = "sc/foreign_coin/foreign_coin_detail.html"


@permission_required('core.view_capital')
def foreign_coin_download(request):
    items = Foreign_coin.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_foreign_coin_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'foreign_coin', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.foreign_coin, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def foreign_coin_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_foreign_coins.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'foreign_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of foreign coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Indigenous_coinCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Indigenous_coin
    form_class = Indigenous_coinForm
    template_name = "sc/indigenous_coin/indigenous_coin_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('indigenous_coin-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Indigenous Coin"
        context["my_exp"] = "NO_DESCRIPTIONS_IN_CODEBOOK"
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'indigenous_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of indigenous coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Indigenous_coinUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Indigenous_coin
    form_class = Indigenous_coinForm
    template_name = "sc/indigenous_coin/indigenous_coin_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Indigenous Coin"

        return context

class Indigenous_coinDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Indigenous_coin object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Indigenous_coin
    success_url = reverse_lazy('indigenous_coins')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Indigenous_coinListView(generic.ListView):
    """
    Paginated view for listing all the Indigenous_coin objects.
    """
    model = Indigenous_coin
    template_name = "sc/indigenous_coin/indigenous_coin_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('indigenous_coins')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Indigenous Coin"
        context["var_main_desc"] = "NO Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'indigenous_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of indigenous coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Indigenous_coinListViewAll(generic.ListView):
    """
    
    """
    model = Indigenous_coin
    template_name = "sc/indigenous_coin/indigenous_coin_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('indigenous_coins_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Indigenous_coin.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Indigenous Coin"
        context["var_main_desc"] = "NO Descriptions IN Codebook"
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'indigenous_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of indigenous coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Indigenous_coinDetailView(generic.DetailView):
    """
    
    """
    model = Indigenous_coin
    template_name = "sc/indigenous_coin/indigenous_coin_detail.html"


@permission_required('core.view_capital')
def indigenous_coin_download(request):
    items = Indigenous_coin.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_indigenous_coin_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'indigenous_coin', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.indigenous_coin, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response


@permission_required('core.view_capital')
def indigenous_coin_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_indigenous_coins.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'NO_DESCRIPTIONS_IN_CODEBOOK', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'indigenous_coin': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of indigenous coin for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Paper_currencyCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Paper_currency
    form_class = Paper_currencyForm
    template_name = "sc/paper_currency/paper_currency_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('paper_currency-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Paper Currency"
        context["my_exp"] = "Paper currency or another kind of fiat money. Note that this only refers to indigenously produced paper currency. Code absent if colonial money is used."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'paper_currency': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of paper currency for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Paper_currencyUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Paper_currency
    form_class = Paper_currencyForm
    template_name = "sc/paper_currency/paper_currency_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Paper Currency"

        return context

class Paper_currencyDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Paper_currency object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Paper_currency
    success_url = reverse_lazy('paper_currencys')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Paper_currencyListView(generic.ListView):
    """
    Paginated view for listing all the Paper_currency objects.
    """
    model = Paper_currency
    template_name = "sc/paper_currency/paper_currency_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('paper_currencys')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Paper Currency"
        context["var_main_desc"] = "Paper currency or another kind of fiat money. note that this only refers to indigenously produced paper currency. code absent if colonial money is used."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'paper_currency': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of paper currency for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Paper_currencyListViewAll(generic.ListView):
    """
    
    """
    model = Paper_currency
    template_name = "sc/paper_currency/paper_currency_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('paper_currencys_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Paper_currency.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Paper Currency"
        context["var_main_desc"] = "Paper currency or another kind of fiat money. note that this only refers to indigenously produced paper currency. code absent if colonial money is used."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Forms of money"
        context["inner_vars"] = {'paper_currency': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of paper currency for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Paper_currencyDetailView(generic.DetailView):
    """
    
    """
    model = Paper_currency
    template_name = "sc/paper_currency/paper_currency_detail.html"


@permission_required('core.view_capital')
def paper_currency_download(request):
    items = Paper_currency.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_paper_currency_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'paper_currency', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.paper_currency, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def paper_currency_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_paper_currencys.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Paper currency or another kind of fiat money. Note that this only refers to indigenously produced paper currency. Code absent if colonial money is used.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Forms of money'}
    my_meta_data_dic_inner_vars = {'paper_currency': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of paper currency for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class CourierCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Courier
    form_class = CourierForm
    template_name = "sc/courier/courier_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('courier-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Courier"
        context["my_exp"] = "Full-time professional couriers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'courier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of courier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class CourierUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Courier
    form_class = CourierForm
    template_name = "sc/courier/courier_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Courier"

        return context

class CourierDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Courier object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Courier
    success_url = reverse_lazy('couriers')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class CourierListView(generic.ListView):
    """
    Paginated view for listing all the Courier objects.
    """
    model = Courier
    template_name = "sc/courier/courier_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('couriers')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Courier"
        context["var_main_desc"] = "Full-time professional couriers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'courier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of courier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class CourierListViewAll(generic.ListView):
    """
    
    """
    model = Courier
    template_name = "sc/courier/courier_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('couriers_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Courier.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Courier"
        context["var_main_desc"] = "Full-time professional couriers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'courier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of courier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class CourierDetailView(generic.DetailView):
    """
    
    """
    model = Courier
    template_name = "sc/courier/courier_detail.html"


@permission_required('core.view_capital')
def courier_download(request):
    items = Courier.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_courier_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'courier', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.courier, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def courier_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_couriers.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Full-time professional couriers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Postal sytems'}
    my_meta_data_dic_inner_vars = {'courier': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of courier for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class Postal_stationCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Postal_station
    form_class = Postal_stationForm
    template_name = "sc/postal_station/postal_station_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('postal_station-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "Postal Station"
        context["my_exp"] = "Talking about postal sytems, Postal stations are specialized buildings exclusively devoted to the postal service. If there is a special building that has other functions than a postal station, we still code postal station as present. The intent is to capture additional infrastructure beyond having a corps of messengers."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'postal_station': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of postal station for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class Postal_stationUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Postal_station
    form_class = Postal_stationForm
    template_name = "sc/postal_station/postal_station_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Postal Station"

        return context

class Postal_stationDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing Postal_station object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = Postal_station
    success_url = reverse_lazy('postal_stations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class Postal_stationListView(generic.ListView):
    """
    Paginated view for listing all the Postal_station objects.
    """
    model = Postal_station
    template_name = "sc/postal_station/postal_station_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('postal_stations')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Postal Station"
        context["var_main_desc"] = "Talking about postal sytems, postal stations are specialized buildings exclusively devoted to the postal service. if there is a special building that has other functions than a postal station, we still code postal station as present. the intent is to capture additional infrastructure beyond having a corps of messengers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'postal_station': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of postal station for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class Postal_stationListViewAll(generic.ListView):
    """
    
    """
    model = Postal_station
    template_name = "sc/postal_station/postal_station_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('postal_stations_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = Postal_station.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "Postal Station"
        context["var_main_desc"] = "Talking about postal sytems, postal stations are specialized buildings exclusively devoted to the postal service. if there is a special building that has other functions than a postal station, we still code postal station as present. the intent is to capture additional infrastructure beyond having a corps of messengers."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'postal_station': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of postal station for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class Postal_stationDetailView(generic.DetailView):
    """
    
    """
    model = Postal_station
    template_name = "sc/postal_station/postal_station_detail.html"


@permission_required('core.view_capital')
def postal_station_download(request):
    items = Postal_station.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_postal_station_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'postal_station', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.postal_station, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def postal_station_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_postal_stations.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': 'Talking about postal sytems, Postal stations are specialized buildings exclusively devoted to the postal service. If there is a special building that has other functions than a postal station, we still code postal station as present. The intent is to capture additional infrastructure beyond having a corps of messengers.', 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Postal sytems'}
    my_meta_data_dic_inner_vars = {'postal_station': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of postal station for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

class General_postal_serviceCreate(PermissionRequiredMixin, PolityIdMixin, CreateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = General_postal_service
    form_class = General_postal_serviceForm
    template_name = "sc/general_postal_service/general_postal_service_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('general_postal_service-create')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        # get the explanattion:
        context["mysection"] = "General Variables"
        context["mysubsection"] = "General Variables"
        context["myvar"] = "General Postal Service"
        context["my_exp"] = "Talking about postal sytems, 'General postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens."
        context["var_null_meaning"] = "The value is not available."
        context["inner_vars"] = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of general postal service for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        return context


class General_postal_serviceUpdate(PermissionRequiredMixin, UpdateView):
    """
    

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = General_postal_service
    form_class = General_postal_serviceForm
    template_name = "sc/general_postal_service/general_postal_service_update.html"
    permission_required = 'core.add_capital'

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "General Postal Service"

        return context

class General_postal_serviceDelete(PermissionRequiredMixin, DeleteView):
    """
    View for deleting an existing General_postal_service object.

    Note:
        This view is restricted to users with the 'add_capital' permission.
    """
    model = General_postal_service
    success_url = reverse_lazy('general_postal_services')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class General_postal_serviceListView(generic.ListView):
    """
    Paginated view for listing all the General_postal_service objects.
    """
    model = General_postal_service
    template_name = "sc/general_postal_service/general_postal_service_list.html"
    paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('general_postal_services')
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "General Postal Service"
        context["var_main_desc"] = "Talking about postal sytems, 'general postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of general postal service for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []

        return context


class General_postal_serviceListViewAll(generic.ListView):
    """
    
    """
    model = General_postal_service
    template_name = "sc/general_postal_service/general_postal_service_list_all.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('general_postal_services_all')

    def get_queryset(self):
        order = self.request.GET.get('orderby', 'year_from')
        order2 = self.request.GET.get('orderby2', 'year_to')
        #orders = [order, order2]
        new_context = General_postal_service.objects.all().order_by(order, order2)
        return new_context
    
    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super().get_context_data(**kwargs)
        context["myvar"] = "General Postal Service"
        context["var_main_desc"] = "Talking about postal sytems, 'general postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens."
        context["var_main_desc_source"] = "NOTHING"
        context["var_section"] = "Social Complexity"
        context["var_subsection"] = "Postal sytems"
        context["inner_vars"] = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of general postal service for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
        context["potential_cols"] = []
        context['orderby'] = self.request.GET.get('orderby', 'year_from')

        return context
        
class General_postal_serviceDetailView(generic.DetailView):
    """
    
    """
    model = General_postal_service
    template_name = "sc/general_postal_service/general_postal_service_detail.html"


@permission_required('core.view_capital')
def general_postal_service_download(request):
    items = General_postal_service.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_general_postal_service_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'general_postal_service', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])

    for obj in items:
        writer.writerow([obj.name, obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.general_postal_service, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def general_postal_service_meta_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="metadata_general_postal_services.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': "Talking about postal sytems, 'General postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens.", 'main_desc_source': 'NOTHING', 'section': 'Social Complexity', 'subsection': 'Postal sytems'}
    my_meta_data_dic_inner_vars = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': 'The absence or presence of general postal service for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}
    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response

        

def scvars(request):

    app_name = 'sc'  # Replace with your app name
    models_1 = apps.get_app_config(app_name).get_models()

    unique_politys = set()
    number_of_all_rows = 0
    number_of_variables = 0
    all_vars_grouped = {}

    all_sect_download_links = {}

    for model in models_1:
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        ss_value = str(model().sub_subsection())

        better_name = "download_csv_" + s_value.replace("-", "_").replace(" ", "_").replace(":", "").lower()
        all_sect_download_links[s_value] = better_name
        if s_value not in all_vars_grouped:
            all_vars_grouped[s_value] = {}
            if ss_value:
                all_vars_grouped[s_value][ss_value] = []
            else:
                all_vars_grouped[s_value]["None"] = []
        else:
            if ss_value:
                all_vars_grouped[s_value][ss_value] = []
            else:
                all_vars_grouped[s_value]["None"] = []

    models = apps.get_app_config(app_name).get_models()

    for model in models:
        model_name = model.__name__
        if model_name == "Ra":
            continue
        subsection_value = str(model().subsection())
        sub_subsection_value = str(model().sub_subsection())
        count = model.objects.count()
        number_of_all_rows += count
        model_title = model_name.replace("_", " ").title()
        model_create = model_name.lower() + "-create"
        model_download = model_name.lower() + "-download"
        model_metadownload = model_name.lower() + "-metadownload"
        model_all = model_name.lower() + "s_all"
        model_s = model_name.lower() + "s"

        queryset = model.objects.all()
        politys = queryset.values_list('polity', flat=True).distinct()
        unique_politys.update(politys)
        number_of_variables += 1

        to_be_appended = [model_title, model_s, model_create, model_download, model_metadownload, model_all, count]

        if sub_subsection_value:
            all_vars_grouped[subsection_value][sub_subsection_value].append(to_be_appended)
        else:
            all_vars_grouped[subsection_value]["None"].append(to_be_appended)


    context = {}
    context["all_vars_grouped"] = all_vars_grouped
    context["all_sect_download_links"] = all_sect_download_links
    context["all_polities"] = len(unique_politys)
    context["number_of_all_rows"] = number_of_all_rows

    context["number_of_variables"] = number_of_variables

    return render(request, 'sc/scvars.html', context=context)


# new

@permission_required('core.view_capital')
def show_problematic_sc_data_table(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Collect data from all models
    data = []
    for model in app_models:
        items = model.objects.all()
        for obj in items:
            if obj.polity.start_year is not None and obj.year_from is not None and obj.polity.start_year > obj.year_from:
                data.append(obj)

    # Render the template with the data
    return render(request, 'sc/problematic_sc_data_table.html', {'data': data})


@permission_required('core.view_capital')
def download_csv_all_sc(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_data_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        items = model.objects.all()


        for obj in items:
            writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                         obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                         obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def download_csv_social_scale(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')

    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_social_scale_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Social Scale":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def download_csv_professions(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_professions_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Professions":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def download_csv_bureaucracy_characteristics(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_bureaucracy_characteristics_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Bureaucracy Characteristics":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def download_csv_hierarchical_complexity(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_hierarchical_complexity_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Hierarchical Complexity":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def download_csv_law(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_law_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Law":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def download_csv_specialized_buildings_polity_owned(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_specialized_buildings_polity_owned_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Specialized Buildings: polity owned":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def download_csv_transport_infrastructure(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_transport_infrastructure_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Transport Infrastructure":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def download_csv_special_purpose_sites(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_special_purpose_sites_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Special-purpose Sites":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response

@permission_required('core.view_capital')
def download_csv_information(request):
    # Fetch all models in the "socomp" app
    app_name = 'sc'  # Replace with your app name
    app_models = apps.get_app_config(app_name).get_models()

    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_information_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['subsection', 'variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    'value_from', 'value_to', 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    # Iterate over each model
    for model in app_models:
        # Get all rows of data from the model
        model_name = model.__name__
        if model_name == "Ra":
            continue
        s_value = str(model().subsection())
        if s_value == "Information":
            items = model.objects.all()
            for obj in items:
                writer.writerow([obj.subsection(), obj.clean_name(), obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, obj.show_value_from(), obj.show_value_to(), obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response





from seshat.apps.core.forms import  SeshatCommentPartForm2


# Define a custom test function to check for the 'core.add_capital' permission
def has_add_capital_permission(user):
    return user.has_perm('core.add_capital')


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def dynamic_detail_view(request, pk, model_class, myvar, var_name_display):
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)
    form_inline_new = SeshatCommentPartForm2(request.POST)

    context = {
        'object': obj,
        "myvar": myvar,
        "var_name_display": var_name_display,
        'create_new_url': myvar+"-create",
        'see_all_url': myvar+"s_all",
        'letsdo': 'Let us do it!!!',
        'form': form_inline_new,
        'db_section': 'rt',
    }

    return render(request, 'sc/sc_detail.html', context)



# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def dynamic_create_view(request, form_class, x_name, myvar, my_exp, var_section, var_subsection):
    # Retrieve the object based on the object_id

    if x_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
        x_name_with_from = x_name + "_from"
        x_name_with_to = x_name + "_to"
    else:
        x_name_with_from = x_name
        x_name_with_to = None


    if request.method == 'POST':
        # If the request method is POST, it means the form has been submitted
        my_form = form_class(request.POST)
        
        if my_form.is_valid():
            # Save the new object to the database
            new_object = my_form.save()
            return redirect(f"{x_name}-detail", pk=new_object.id)  # Replace 'success_url_name' with your success URL
    else:
        polity_id_x = request.GET.get('polity_id_x')
        my_form = form_class(initial= {'polity': polity_id_x,})

    # Define the context with the variables you want to pass to the template
    if x_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
        context = {
            'form': my_form,
            'object': object,
            'extra_var': my_form[x_name_with_from], 
            'extra_var2': my_form[x_name_with_to], 
            "myvar": myvar,
            "my_exp": my_exp,
            'var_section': var_section,
            'var_subsection': var_subsection,
            }
    else:
        context = {
            'form': my_form,
            'object': object,
            'extra_var': my_form[x_name], 
            "myvar": myvar,
            "my_exp": my_exp,
            'var_section': var_section,
            'var_subsection': var_subsection,
        }

    return render(request, 'sc/sc_create.html', context)


# Use the login_required, permission_required, and user_passes_test decorators
@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def dynamic_update_view(request, object_id, form_class, model_class, x_name, myvar, my_exp, var_section, var_subsection, delete_url_name):
    # Retrieve the object based on the object_id
    my_object = model_class.objects.get(id=object_id)


    if x_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
        x_name_with_from = x_name + "_from"
        x_name_with_to = x_name + "_to"
    else:
        x_name_with_from = x_name
        x_name_with_to = None

    #return_url = f"{x_name}s_all"
    if request.method == 'POST':
        # Bind the form to the POST data
        my_form = form_class(request.POST, instance=my_object)
        
        if my_form.is_valid():
            # Save the changes to the object
            my_form.save()   
            #return redirect(return_url) 
            return redirect(f"{x_name}-detail", pk=my_object.id) 

    else:
        # Create an instance of the form and populate it with the object's data
        my_form = form_class(instance=my_object)

        # Define the context with the variables you want to pass to the template
        if x_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
            context = {
                'form': my_form,
                'object': my_object,
                'delete_url': delete_url_name,
                'extra_var': my_form[x_name_with_from], 
                'extra_var2': my_form[x_name_with_to], 
                "myvar": myvar,
                'var_section': var_section,
                'var_subsection': var_subsection,
                "my_exp": my_exp,
            }
        else:
            context = {
                'form': my_form,
                'object': my_object,
                'delete_url': delete_url_name,
                'extra_var': my_form[x_name], 
                "myvar": myvar,
                'var_section': var_section,
                'var_subsection': var_subsection,
                "my_exp": my_exp,
            }

    return render(request, 'sc/sc_update.html', context)



def generic_list_view(request, model_class, var_name, var_name_display, var_section, var_subsection, var_main_desc):
    # Retrieve a list of objects from the database (you can customize this query)
    object_list = model_class.objects.all()
    #extra_var_dict = {obj.id: obj.__dict__.get(var_name) for obj in object_list}
    extra_var_dict = {obj.id: obj.show_value() for obj in object_list}

    orderby = request.GET.get('orderby', None)

    # Apply sorting if orderby is provided and is a valid field name
    if orderby and hasattr(model_class, orderby):
        object_list = object_list.order_by(orderby)

    if var_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
        var_name_with_from = var_name + "_from"
        var_exp_new = f'The range of "{var_name_display}" for a polity.'
    else:
        var_name_with_from = var_name
        var_exp_new = f'The absence or presence of "{var_name_display}" for a polity.'


    # Define any additional context variables you want to pass to the template
    context = {
        'object_list': object_list,
        'var_name': var_name,
        'create_url': f'{var_name}-create',
        'update_url': f'{var_name}-update',
        'download_url': f'{var_name}-download',
        'pagination_url': f'{var_name}s',
        'metadownload_url':  f'{var_name}-metadownload',
        'list_all_url':  f'{var_name}s_all',
        'var_name_display': var_name_display,
        'ordering_tag': f"?orderby={var_name_with_from}",
        'var_section': var_section,
        'var_subsection': var_subsection,
        'var_main_desc': var_main_desc,
        'myvar': var_name_display,
        'extra_var_dict': extra_var_dict,  # Add the dictionary to the context
        #'extra_var': obj[var_name],

        #'obj_var': my_form[x_name], 
        #"myvar": myvar,
        #"my_exp": my_exp,
    }


    context["inner_vars"] = {
        var_name_display: {
            'min': None,
            'max': None,
            'scale': None, 
            'var_exp_source': None, 
            'var_exp': var_exp_new,
            'units': None, 
            'choices': 'ABSENT_PRESENT_CHOICES', 
            'null_meaning': None}}

    return render(request, 'sc/sc_list_all.html', context)




@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def generic_download(request, model_class, var_name):
    # Fetch all objects for the specified model
    items = model_class.objects.all()

    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"social_complexity_{var_name}_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    if var_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
        var_name_with_from = var_name + "_from"
        var_name_with_to = var_name + "_to"
    else:
        var_name_with_from = var_name
        var_name_with_to = None

    writer = csv.writer(response, delimiter='|')
    if var_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
        writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    var_name_with_from, var_name_with_to, 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    else:
        writer.writerow(['variable_name', 'year_from', 'year_to', 'polity_name', 'polity_new_ID', 'polity_old_ID',
                    var_name, 'confidence', 'is_disputed', 'is_uncertain', 'expert_checked', 'DRB_reviewed'])
    for obj in items:
        if var_name in ["largest_communication_distance", "fastest_individual_communication", "military_level"]:
            dynamic_value_from = getattr(obj, var_name_with_from, '')
            dynamic_value_to = getattr(obj, var_name_with_to, '')
            writer.writerow([obj.name, obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, dynamic_value_from, dynamic_value_to, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])
        else:
            dynamic_value = getattr(obj, var_name, '')
            writer.writerow([obj.name, obj.year_from, obj.year_to,
                            obj.polity.long_name, obj.polity.new_name, obj.polity.name, dynamic_value, obj.get_tag_display(), obj.is_disputed, obj.is_uncertain,
                            obj.expert_reviewed, obj.drb_reviewed,])

    return response

@login_required
@permission_required('core.add_capital', raise_exception=True)
@user_passes_test(has_add_capital_permission, login_url='permission_denied')
def generic_metadata_download(request, var_name, var_name_display, var_section, var_subsection, var_main_desc):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="metadata_{var_name}s.csv"'
    
    my_meta_data_dic = {'notes': 'No_Actual_note', 'main_desc': var_main_desc, 'main_desc_source': 'NOTHING', 'section': var_section, 'subsection': var_subsection}
    my_meta_data_dic_inner_vars = {'general_postal_service': {'min': None, 'max': None, 'scale': None, 'var_exp_source': None, 'var_exp': f'The {var_name_display} for a polity.', 'units': None, 'choices': 'ABSENT_PRESENT_CHOICES', 'null_meaning': None}}

    writer = csv.writer(response, delimiter='|')
    # bring in the meta data nedded
    for k, v in my_meta_data_dic.items():
        writer.writerow([k, v])

    for k_in, v_in in my_meta_data_dic_inner_vars.items():
        writer.writerow([k_in,])
        for inner_key, inner_value in v_in.items():
            if inner_value:
                writer.writerow([inner_key, inner_value])

    return response



# def generic_delete_view(request, model_class, pk, var_name):
#     permission_required = 'core.add_capital'
    
#     # Retrieve the object for the given model class
#     #obj = get_object_or_404(model_class, pk=request.POST.get(pk))
#     obj = get_object_or_404(model_class, pk=pk)

#     # Check if the user has the required permission
#     if not request.user.has_perm(permission_required):
#         return HttpResponseForbidden("You don't have permission to delete this object.")

#     # Delete the object
#     #obj.delete()

#     # Redirect to the success URL
#     success_url_name = var_name + "s_all"
#     success_url = reverse(success_url_name)

#     template_name = "core/delete_general.html"
    
#     #return HttpResponseRedirect(success_url)
#     # Display a success message
#     messages.success(request, f"{var_name} has been deleted successfully.")

#     # Redirect or render a template
#     return render(request, template_name, {})


def confirm_delete_view(request, model_class, pk, var_name):
    permission_required = 'core.add_capital'
    
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    # Check if the user has the required permission
    if not request.user.has_perm(permission_required):
        return HttpResponseForbidden("You don't have permission to delete this object.")

    template_name = "core/confirm_delete.html"
    
    context = {
        'var_name': var_name,
        'obj': obj,
        'delete_object': f'{var_name}-delete',
    }

    return render(request, template_name, context)

def delete_object_view(request, model_class, pk, var_name):
    permission_required = 'core.add_capital'
    # Retrieve the object for the given model class
    obj = get_object_or_404(model_class, pk=pk)

    if not request.user.has_perm(permission_required):
        return HttpResponseForbidden("You don't have permission to delete this object.")
    
    # Delete the object
    obj.delete()
    
    # Redirect to the success URL
    success_url_name = f'{var_name}s_all'  # Adjust the success URL as needed
    success_url = reverse(success_url_name)
    
    # Display a success message
    messages.success(request, f"{var_name} has been deleted successfully.")
    
    return redirect(success_url)