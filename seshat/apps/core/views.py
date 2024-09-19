import sys
import importlib
import random
import numpy as np

from collections import defaultdict
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections

from django.contrib.sites.shortcuts import get_current_site
from seshat.apps.core.forms import SignUpForm, VariablehierarchyFormNew, CitationForm, ReferenceForm, SeshatCommentForm, SeshatCommentPartForm, PolityForm, PolityUpdateForm, CapitalForm, NgaForm, SeshatCommentPartForm2, SeshatCommentPartForm5,  SeshatCommentPartForm10, SeshatPrivateCommentPartForm, ReferenceFormSet2, ReferenceFormSet5, ReferenceFormSet10, CommentPartFormSet, ReferenceWithPageForm, SeshatPrivateCommentForm, ReligionForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.db import IntegrityError, connection
from django.db.models import Prefetch, F, Value, Q, Min, Max, Count
from django.db.models.functions import Replace

from django.views.decorators.http import require_GET

from django.contrib.auth.decorators import login_required, permission_required
from seshat.apps.accounts.models import Seshat_Expert
from seshat.apps.general.models import Polity_preceding_entity

from django.core.paginator import Paginator

from django.http import FileResponse
from django.shortcuts import get_object_or_404, render, redirect
import os

from django.apps import apps

from decouple import config


from markupsafe import Markup, escape
from django.http import JsonResponse

from django.core.mail import EmailMessage, send_mail
import html
import datetime
import csv

import json
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.contrib.messages.views import SuccessMessageMixin

from ..general.models import Polity_research_assistant, Polity_duration, Polity_linguistic_family, Polity_language_genus, Polity_language, POLITY_LINGUISTIC_FAMILY_CHOICES, POLITY_LANGUAGE_GENUS_CHOICES, POLITY_LANGUAGE_CHOICES, Polity_religious_tradition, Polity_religion_genus, Polity_religion_family, Polity_religion, Polity_alternate_religion_genus, Polity_alternate_religion_family, Polity_alternate_religion, POLITY_RELIGION_GENUS_CHOICES, POLITY_RELIGION_FAMILY_CHOICES, POLITY_RELIGION_CHOICES

from ..crisisdb.models import Power_transition

from .models import Citation, Polity, Section, Subsection, Variablehierarchy, Reference, SeshatComment, SeshatCommentPart, Nga, Ngapolityrel, Capital, Seshat_region, Macro_region, Cliopatria, GADMCountries, GADMProvinces, SeshatCommon, ScpThroughCtn, SeshatPrivateComment, SeshatPrivateCommentPart, Religion
import pprint
import requests
from requests.structures import CaseInsensitiveDict
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier, get_all_data_for_a_polity, polity_detail_data_collector, get_all_general_data_for_a_polity, get_all_sc_data_for_a_polity, get_all_wf_data_for_a_polity, get_all_rt_data_for_a_polity, get_all_crisis_cases_data_for_a_polity, get_all_power_transitions_data_for_a_polity, give_polity_app_data


from django.shortcuts import HttpResponse

from math import floor, ceil
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.views.generic import ListView

@login_required
@permission_required('core.add_seshatprivatecommentpart')
def religion_create(request):
    """
    Create a new religion.

    Note:
        This view is only accessible to users with the 'add_seshatprivatecommentpart' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == 'POST':
        form = ReligionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('religion_list')
    else:
        form = ReligionForm()
    return render(request, 'core/religion_create.html', {'form': form})

@login_required
@permission_required('core.add_seshatprivatecommentpart')
def religion_update(request, pk):
    """
    Update an existing religion.

    Note:
        This view is only accessible to users with the 'add_seshatprivatecommentpart' permission.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the religion.

    Returns:
        HttpResponse: The response object.
    """
    religion = get_object_or_404(Religion, pk=pk)
    if request.method == 'POST':
        form = ReligionForm(request.POST, instance=religion)
        if form.is_valid():
            form.save()
            return redirect('religion_list')
    else:
        form = ReligionForm(instance=religion)
    return render(request, 'core/religion_update.html', {'form': form})

class ReligionListView(ListView):
    """
    List all religions.
    """
    model = Religion
    template_name = 'core/religion_list.html'
    context_object_name = 'religions'
    ordering = ['religion_name']
    permission_required = 'core.add_seshatprivatecommentpart'



######
def is_ajax(request):
    """
    Return True if the request is an AJAX request, False otherwise.

    Args:
        request (HttpRequest): The request object.

    Returns:
        bool: True if the request is an AJAX request, False otherwise.
    """
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def ajax_test(request):
    """
    Test if the request is an AJAX request.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    if is_ajax(request=request):
        message = "This is ajax"
    else:
        message = "Not ajax"
    return HttpResponse(message)

# importing formset_factory
from django.forms import formset_factory, modelformset_factory, inlineformset_factory


def index(request):
    """
    Returns a simple "Hello World" response.

    Note:
        This is a simple view to test the server. It is not part of the
        application.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return HttpResponse('<h1>Hello World.</h1>')

def four_o_four(request):
    """
    Return a 404 error page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return render(request, 'core/not_found_404.html')

def seshatindex2(request):
    """
    Return the Seshat landing page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    context = {
        'insta': "Instabilities All Over the Place..",
        'trans': "Transitions All Over the Place",
    }
    #print('static_root:', settings.STATIC_ROOT)
    #print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)
    return render(request, 'core/seshat-index.html', context=context)

def seshatmethods(request):
    """
    Return the Seshat "Methods" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    context = {
        'insta': "Instabilities All Over the Place..",
        'trans': "Transitions All Over the Place",
    }
    #print('static_root:', settings.STATIC_ROOT)
    #print('STATICFILES_DIRS:', settings.STATICFILES_DIRS)
    return render(request, 'core/seshat-methods.html', context=context)

def seshatwhoweare(request):
    """
    Return the Seshat "Who We are" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    #json_url_inners = "https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_500k.json"
    #json_url_outline = "https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_outline_500k.json"
    json_file_path = "/home/majid/dev/seshat/seshat/seshat/apps/core/static/geojson/us_states_geojson.json"

    try:
        #response_inners = requests.get(json_url_inners)
        #response_outline = requests.get(json_url_outline)
        with open(json_file_path, "r") as json_file:
            json_data = json.load(json_file)
        #with open(json_file_path, "r") as json_file:
        #    json_data = json.load(json_file)
        # Check if the request was successful (status code 200)
        #if response_inners.status_code == 200 and response_outline.status_code == 200:
        #    # Parse the JSON data from the response_inners
        #    json_inners = response_inners.json()
        #    json_outline = response_outline.json()

        context = {
                'insta': "Instabilities All Over the Place..",
                'json_data': json_data,  # Add this line to your context
        }
        print(len(json_data))
        return render(request, 'core/seshat-whoweare.html', context=context)
    except FileNotFoundError:
        # Handle the case when the file is not found
        context = {
            'insta': "Instabilities All Over the Place..",
            'json_error': "JSON file not found",
        }
        return render(request, 'core/seshat-whoweare.html', context=context)
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors if the file is not valid JSON
        context = {
            'insta': "Instabilities All Over the Place..",
            'json_error': f"JSON decoding error: {str(e)}",
        }
        return render(request, 'core/seshat-whoweare.html', context=context)

def seshatolddownloads(request):
    """
    Return the Seshat "Downloads" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    context = {
        'insta': "Instabilities All Over the Place..",
    }
    return render(request, 'core/old_downloads.html', context=context)

def seshatcodebookold(request):
    """
    Return the Seshat "Codebook" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    context = {
        'insta': "Instabilities All Over the Place..",
    }
    return render(request, 'core/old_codebook.html', context=context)

def seshatcodebooknew1(request):
    context = {
        'insta': "Instabilities All Over the Place..",
    }
    return render(request, 'core/code_book_1.html', context=context)

# def seshatcodebooknew2(request):
#     context = {
#         'insta': "Instabilities All Over the Place..",
#     }
#     return render(request, 'core/new_codebook_2.html', context=context)

def seshatacknowledgements(request):
    """
    Return the Seshat "Acknowledgements" page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    context = {
        'insta': "Instabilities All Over the Place..",
    }
    return render(request, 'core/seshat-acknowledgements.html', context=context)

class ReferenceListView(generic.ListView):
    """
    List all references.
    """
    model = Reference
    template_name = "core/references/reference_list.html"
    paginate_by = 100

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('references')

    def get_queryset(self):
        """
        Get the queryset of references.

        Returns:
            QuerySet: The queryset of references.
        """
        queryset = Reference.objects.exclude(creator='MAJIDBENAM').all()
        return queryset
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     selected_only_zotero_refs = Reference.objects.exclude(creator='MAJIDBENAM')
    #     context['object_list'] = selected_only_zotero_refs

    #     return context


class NlpReferenceListView(generic.ListView):
    """
    List all NLP references.
    """
    model = Reference
    template_name = "core/references/nlp_reference_list.html"
    paginate_by = 50

    def get_absolute_url(self):
        """
        Return the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('nlp-references')

    def get_queryset(self):
        """
        Return the queryset of NLP references.

        Returns:
            QuerySet: The queryset of NLP references.
        """
        # Import the list of Zotero links inside the method
        from .nlp_zotero_links import NLP_ZOTERO_LINKS_TO_FILTER

        # Use the imported list of Zotero links to filter references
        queryset = Reference.objects.filter(zotero_link__in=NLP_ZOTERO_LINKS_TO_FILTER)

        queryset = queryset.filter(year__gt=0)

        # Replace underscores in 'creator' with spaces
        queryset = queryset.annotate(
            creator_with_spaces=Replace('creator', Value('_'), Value(' '))
        )

        # Replace "_et_al" at the end of 'creator' with ", ..."
        queryset = queryset.annotate(
            creator_cleaned=Replace(F('creator_with_spaces'), Value(' et al'), Value(', ...'))
        )

        queryset = queryset.order_by('-year', 'title')

        # Create a list of Zotero links from the queryset
        #matched_zotero_links = list(queryset.values_list('zotero_link', flat=True))

        # Find the missing Zotero links
        #missing_zotero_links = [link for link in NLP_ZOTERO_LINKS_TO_FILTER if link not in matched_zotero_links]

        #print(missing_zotero_links)

        return queryset

# references without a Zotero link:
def no_zotero_refs_list(request):
    """
    List all references without a Zotero link.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    selected_no_zotero_refs = Reference.objects.filter(zotero_link__startswith='NOZOTERO_')
    #all_refs = Reference.objects.all()
    #selected_no_zotero_refs = []
    #for ref in all_refs:
    #    if "NOZOTERO_" in ref.zotero_link:
    #        selected_no_zotero_refs.append(ref)

    paginator = Paginator(selected_no_zotero_refs, 10) # Show 25 refs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {}
    context['object_list'] = selected_no_zotero_refs
    context['page_obj'] = page_obj
    context['is_paginated'] = False


    # Citation.objects.bulk_create(all_citations)
    return render (request, 'core/references/reference_list_nozotero.html', context)

def reference_update_modal(request, pk):
    """
    Update a reference using a modal or a standalone page depending on the
    request.

    Args:
        request (HttpRequest): The request object.
        pk (int): The primary key of the reference.

    Returns:
        HttpResponse: The response object.
    """
    # Either render only the modal content, or a full standalone page
    if is_ajax(request=request):
        template_name = 'core/references/reference_update_modal.html'
    else:
        template_name = 'core/references/reference_update.html'

    object = Reference.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReferenceForm(instance=object, data=request.POST)
        if form.is_valid():
            form.save()
            if not is_ajax(request=request):
                # reload the page
                next = request.META['PATH_INFO']
                return HttpResponseRedirect(next)
            # if is_ajax(), we just return the validated form, so the modal will close
    else:
        form = ReferenceForm(instance=object)

    return render(request, template_name, {
        'object': object,
        'form': form,
    })

###########


class ReferenceCreate(PermissionRequiredMixin, CreateView):
    """
    Create a new reference.
    """
    model = Reference
    form_class = ReferenceForm
    template_name = "core/references/reference_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('reference-create')

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
        context["mysection"] = "xyz"
        context["mysubsection"] = "abc"
        context["myvar"] = "def reference"
        context["errors"] = "Halooooooooo"
        #print(context)

        return context

    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse('seshat-index'))


class ReferenceUpdate(PermissionRequiredMixin, UpdateView):
    """
    Update a reference.
    """
    model = Reference
    form_class = ReferenceForm
    template_name = "core/references/reference_update.html"
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
        context["mysection"] = "Fiscal Heeeelath"
        context["mysubsection"] = "No Subsection Proeeeevided"
        context["myvar"] = "Reference Daeeeeta"

        return context

class ReferenceDelete(PermissionRequiredMixin, DeleteView):
    """
    Delete a reference.
    """
    model = Reference
    success_url = reverse_lazy('references')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class ReferenceDetailView(generic.DetailView):
    """
    Display the details of a reference.
    """
    model = Reference
    template_name = "core/references/reference_detail.html"



@permission_required('core.view_capital')
def references_download(request):
    """
    Download all references as a CSV file.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    items = Reference.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="referencess.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['zotero_link', 'creator'])

    for obj in items:
        writer.writerow([obj.zotero_link, obj.creator])

    return response


# Citations
class CitationListView(generic.ListView):
    """
    List all citations.
    """
    model = Citation
    template_name = "core/references/citation_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('citations')

class CitationCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create a new citation.
    """
    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_form.html"
    permission_required = 'core.add_capital'
    success_message = "Yoohoooo..."

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        context = self.get_context_data(form=form)
        context.update({"my_message": "Soemthign went wrong"})
        return self.render_to_response(context)

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('citation-create')

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
        context["mysection"] = "xyz"
        context["mysubsection"] = "abc"
        context["myvar"] = "def citation"
        context["errors"] = "Halooooooooo"
        #print(context)

        return context

    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     return HttpResponseRedirect(reverse('seshat-index'))


class CitationUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update a citation.
    """
    model = Citation
    form_class = CitationForm
    template_name = "core/references/citation_update.html"
    permission_required = 'core.add_capital'
    success_message = "Yoohoooo..."

    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        context = self.get_context_data(form=form)
        context.update({"my_message": "Soemthign went wrong"})
        return self.render_to_response(context)

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
        context["mysection"] = "Fiscal Helath"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Citation Data xyz"

        return context

class CitationDelete(PermissionRequiredMixin, DeleteView):
    """
    Delete a citation.
    """
    model = Citation
    success_url = reverse_lazy('citations')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class CitationDetailView(generic.DetailView):
    """
    Display the details of a citation.
    """
    model = Citation
    template_name = "core/references/citation_detail.html"

# SeshatComment
class SeshatCommentListView(generic.ListView):
    """
    List all comments.
    """
    model = SeshatComment
    template_name = "core/seshatcomments/seshatcomment_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('seshatcomments')

class SeshatCommentCreate(PermissionRequiredMixin, CreateView):
    """
    Create a new comment.
    """
    model = SeshatComment
    form_class = SeshatCommentForm
    template_name = "core/seshatcomments/seshatcomment_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('seshatcomment-create')


    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form (Form): The form object.
        Returns:
            HttpResponse: The response object.
        """
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse('seshat-index'))


class SeshatCommentUpdate(PermissionRequiredMixin, UpdateView):
    """
    Update a comment.
    """
    model = SeshatComment
    form_class = SeshatCommentForm
    template_name = "core/seshatcomments/seshatcomment_update.html"
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
        my_apps=['rt', 'general', 'sc', 'wf', 'crisisdb']
        my_app_models = {name: apps.all_models[name] for name in my_apps}

        #context['my_app_models'] = my_app_models
        abc = []

        for myapp, mymodels in my_app_models.items():
            for mm, mymodel in mymodels.items():
                if '_citations' not in mm and '_curator' not in mm and not mm.startswith('us_') and mymodel.objects.filter(comment=self.object.id):
                    my_instance = mymodel.objects.get(comment=self.object.id)
                    my_polity = my_instance.polity
                    my_polity_id = my_instance.polity.id
                    try:
                        my_var_name = my_instance.clean_name_spaced()
                    except:
                        my_var_name = my_instance.name

                    my_value = my_instance.show_value
                    my_year_from = my_instance.year_from
                    my_year_to = my_instance.year_to
                    my_tag = my_instance.get_tag_display()


                    abc.append({
                        'my_polity': my_polity,
                        'my_value': my_value,
                        'my_year_from': my_year_from,
                        'my_year_to': my_year_to,
                        'my_tag': my_tag,
                        'my_var_name': my_var_name,
                        'my_polity_id': my_polity_id,
                    })

        # for model_name in related_models:
        #     print(model_name)
        #     related_objects = getattr(self.object, model_name)
        #     if related_objects:
        #         context['related_objects'] = related_objects
        #         break
        
        context['my_app_models'] = abc


        return context


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #an_instance = SeshatComment.objects.first()
    #     #related_fact = 
    #     #print("Haloooooo_________ooooooooooo", self.kwargs['com_id'])
    #     #print("Halooooooooooooooooo", self.kwargs['subcom_order'])
    #     #related_fact = self.        context["com_id"] = self.kwargs['com_id']
    #     #context["subcom_order"] = self.kwargs['subcom_order']
    #     #context["subcom_order"] = self.comment_order

    #     print("HEre we gooooooooooo: ", dir(self.object))
    #     #for potential_attr in dir(isinstance):
            
    #     #if an_instance

    #     return context

class SeshatCommentDelete(PermissionRequiredMixin, DeleteView):
    """
    Delete a comment.
    """
    model = SeshatComment
    success_url = reverse_lazy('seshatcomments')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'


class SeshatCommentDetailView(generic.DetailView):
    """
    Display the details of a comment.
    """
    model = SeshatComment
    template_name = "core/seshatcomments/seshatcomment_detail.html"


# SeshatCommentPart
class SeshatCommentPartListView(generic.ListView):
    """
    List all comment parts.
    """
    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_list.html"
    paginate_by = 20

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('seshatcommentparts')

# SeshatCommentPart
class SeshatCommentPartListView3(generic.ListView):
    """
    List all comment parts.
    """
    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_list3.html"
    paginate_by = 20

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('seshatcommentparts3')
    
class SeshatCommentPartCreate(PermissionRequiredMixin, CreateView):
    """
    Create a new comment part.
    """
    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_form.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('seshatcommentpart-create')


    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse('seshat-index'))

class SeshatCommentPartCreate2(PermissionRequiredMixin, CreateView):
    """
    Create a new comment part.
    """
    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_form_prefilled.html"
    permission_required = 'core.add_capital'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('seshatcommentpart-create2')

    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse('seshat-index'))
    
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
        logged_in_user = self.request.user
        logged_in_expert = Seshat_Expert.objects.get(user=logged_in_user)
        #print("Haloooooo_________ooooooooooo", self.kwargs['com_id'])
        #print("Halooooooooooooooooo", self.kwargs['subcom_order'])
        context["com_id"] = self.kwargs['com_id']
        context["subcom_order"] = self.kwargs['subcom_order']
        context["comment_curator"] = logged_in_expert
        context["comment_curator_id"] = logged_in_expert.id
        context["comment_curator_name"] = "Selected USER"

        #context["subcom_order"] = self.comment_order
        #print(context)

        return context
    

class SeshatPrivateCommentPartCreate2(PermissionRequiredMixin, CreateView):
    """
    Create a new private comment part.
    """
    model = SeshatPrivateCommentPart
    form_class = SeshatPrivateCommentPartForm
    template_name = "core/seshatcomments/seshatprivatecommentpart_form_prefilled.html"
    permission_required = 'core.add_seshatprivatecommentpart'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('seshatprivatecommentpart-create2')

    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse('seshat-index'))
    
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
        logged_in_user = self.request.user
        logged_in_expert = Seshat_Expert.objects.get(user=logged_in_user)
        #readers_experts = SeshatPrivateCommentPart.get()
        #print("Haloooooo_________ooooooooooo", self.kwargs['com_id'])
        #print("Halooooooooooooooooo", self.kwargs['subcom_order'])
        context["private_com_id"] = self.kwargs['private_com_id']
        context["private_comment_owner"] = logged_in_expert
        #context["private_comment_reader"] = readers_experts

        #context["subcom_order"] = self.comment_order
        #print(context)
        #print("2222222222222222222222222222222")

        return context

  
# Function based:
@permission_required('core.add_capital')
def seshat_comment_part_create_from_null_view_OLD(request, com_id, subcom_order):
    """
    Create a new comment part.

    Note:
        This function is not used in the current implementation.
        This view is only accessible to users with the 'add_capital' permission.

    Args:
        request (HttpRequest): The request object.
        com_id (int): The primary key of the comment.
        subcom_order (int): The order of the comment part.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == 'POST':
        form = SeshatCommentPartForm2(request.POST)
        big_father = SeshatComment.objects.get(id=com_id)

        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            comment_order = form.cleaned_data['comment_order']
            user_logged_in = request.user

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except:
                seshat_expert_instance = None

            seshat_comment_part = SeshatCommentPart(comment_part_text=comment_text, comment_order=subcom_order, comment_curator=seshat_expert_instance, comment= big_father)

            seshat_comment_part.save()

            # Process the formset
            reference_formset = ReferenceFormSet2(request.POST, prefix='refs')
            if reference_formset.is_valid():
                to_be_added = []
                to_be_deleted_later = []
                for reference_form in reference_formset:
                    if reference_form.is_valid():
                        try:
                            reference = reference_form.cleaned_data['ref']
                            page_from = reference_form.cleaned_data['page_from']
                            page_to = reference_form.cleaned_data['page_to']
                            to_be_deleted = reference_form.cleaned_data['DELETE']

                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to)
                                )
                            elif page_from:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_from)
                                )
                            elif page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_to),
                                    page_to=int(page_to)
                                )
                                #print(page_from, "AAAAAAAAAAAAAAAAAAAAND ", page_to)
                            else:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=None,
                                    page_to=None
                                )

                            # Associate the Citation with the SeshatCommentPart
                            if to_be_deleted:
                                #comment_part.comment_citations.remove(citation)
                                to_be_deleted_later.append(citation)
                            else:
                                #comment_part.comment_citations.add(citation)
                                to_be_added.append(citation)
                        except:
                            pass  # Handle the exception as per your requirement
                seshat_comment_part.comment_citations.clear()
                seshat_comment_part.comment_citations.add(*to_be_added)
            return redirect(reverse('seshatcomment-update', kwargs={'pk': com_id}))

    else:
        init_data = ReferenceFormSet2(prefix='refs')
        form = SeshatCommentPartForm2()

    context = {
        'form': form,
        'com_id': com_id,  # Include com_id in the context
        'subcom_order': subcom_order,  # Include subcom_order in the context
        'formset': init_data, 
        #'comm_num': com_id,
        #'comm_part_display': comment_part,
    }
    return render(request, 'core/seshatcomments/seshatcommentpart_create2.html', context)

    
# Function based NEW:
@permission_required('core.add_capital')
def seshat_comment_part_create_from_null_view(request, com_id, subcom_order):
    """
    Create a new comment part.

    Note:
        This view is only accessible to users with the 'add_capital' permission.

    Args:
        request (HttpRequest): The request object.
        com_id (int): The primary key of the comment.
        subcom_order (int): The order of the comment part.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == 'POST':
        form = SeshatCommentPartForm2(request.POST)
        big_father = SeshatComment.objects.get(id=com_id)

        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            comment_order = form.cleaned_data['comment_order']
            user_logged_in = request.user

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except:
                seshat_expert_instance = None

            seshat_comment_part = SeshatCommentPart(comment_part_text=comment_text, comment_order=subcom_order, comment_curator=seshat_expert_instance, comment= big_father)

            seshat_comment_part.save()

            # Process the formset
            reference_formset = ReferenceFormSet2(request.POST, prefix='refs')
            if reference_formset.is_valid():
                #print("ALOOOOOOOOOOOOOOOOOOO: ", len(reference_formset))
                to_be_added = []
                to_be_deleted_later = []
                for reference_form in reference_formset:
                    if reference_form.is_valid():
                        try:
                            reference = reference_form.cleaned_data['ref']
                            page_from = reference_form.cleaned_data['page_from']
                            page_to = reference_form.cleaned_data['page_to']
                            to_be_deleted = reference_form.cleaned_data['DELETE']
                            parent_pars_inserted = reference_form.cleaned_data['parent_pars']


                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to)
                                )
                            elif page_from:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_from)
                                )
                            elif page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_to),
                                    page_to=int(page_to)
                                )
                                #print(page_from, "AAAAAAAAAAAAAAAAAAAAND ", page_to)
                            else:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=None,
                                    page_to=None
                                )

                            # Associate the Citation with the SeshatCommentPart
                            if to_be_deleted:
                                #comment_part.comment_citations.remove(citation)
                                to_be_deleted_later.append((citation, parent_pars_inserted))
                            else:
                                #comment_part.comment_citations.add((citation, parent_pars_inserted))
                                to_be_added.append((citation, parent_pars_inserted))
                        except:
                            pass  # Handle the exception as per your requirement
                # seshat_comment_part.comment_citations.clear()
                # seshat_comment_part.comment_citations.add(*to_be_added)
                seshat_comment_part.comment_citations_plus.clear()
                #seshat_comment_part.comment_citations_plus.add(*to_be_added)

                for item in to_be_added:
                    # Query for an existing row based on citation and SeshatCommentPart
                    scp_through_ctn, created = ScpThroughCtn.objects.get_or_create(
                        seshatcommentpart=seshat_comment_part,
                        citation=item[0],
                        defaults={'parent_paragraphs': item[1]}  # Set defaults including parent_paragraphs
                    )

                    # If the row already exists, update its parent_paragraphs
                    if not created:
                        scp_through_ctn.parent_paragraphs = item[1]
                        scp_through_ctn.save()
            return redirect(reverse('seshatcomment-update', kwargs={'pk': com_id}))

    else:
        init_data = ReferenceFormSet2(prefix='refs')
        form = SeshatCommentPartForm2()
        big_father = SeshatComment.objects.get(id=com_id)

    context = {
        'form': form,
        'com_id': com_id,  # Include com_id in the context
        'subcom_order': subcom_order,  # Include subcom_order in the context
        'formset': init_data, 
        'parent_par': big_father, 

        #'comm_num': com_id,
        #'comm_part_display': comment_part,
    }
    return render(request, 'core/seshatcomments/seshatcommentpart_create2.html', context)



# Function based NEW:
@permission_required('core.add_capital')
def seshat_comment_part_create_from_null_view_inline(request, app_name, model_name, instance_id):
    if request.method == 'POST':
        form = SeshatCommentPartForm2(request.POST)
        big_father = SeshatComment.objects.create(text='a new_comment_text')
        #big_father = SeshatComment.objects.get(id=com_id)
        com_id = big_father.pk
        model_class = apps.get_model(app_label=app_name, model_name= model_name)

        model_instance = get_object_or_404(model_class, id=instance_id)
        model_instance.comment = big_father

        model_instance.save()
        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            comment_order = form.cleaned_data['comment_order']
            user_logged_in = request.user

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except:
                seshat_expert_instance = None

            seshat_comment_part = SeshatCommentPart(comment_part_text=comment_text, comment_order=1, comment_curator=seshat_expert_instance, comment= big_father)

            seshat_comment_part.save()

            # Process the formset
            reference_formset = ReferenceFormSet2(request.POST, prefix='refs')
            if reference_formset.is_valid():
                #print("ALOOOOOOOOOOOOOOOOOOO: ", len(reference_formset))
                to_be_added = []
                to_be_deleted_later = []
                for reference_form in reference_formset:
                    if reference_form.is_valid():
                        try:
                            reference = reference_form.cleaned_data['ref']
                            page_from = reference_form.cleaned_data['page_from']
                            page_to = reference_form.cleaned_data['page_to']
                            to_be_deleted = reference_form.cleaned_data['DELETE']
                            parent_pars_inserted = reference_form.cleaned_data['parent_pars']


                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to)
                                )
                            elif page_from:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_from)
                                )
                            elif page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_to),
                                    page_to=int(page_to)
                                )
                                #print(page_from, "AAAAAAAAAAAAAAAAAAAAND ", page_to)
                            else:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=None,
                                    page_to=None
                                )

                            # Associate the Citation with the SeshatCommentPart
                            if to_be_deleted:
                                #comment_part.comment_citations.remove(citation)
                                to_be_deleted_later.append((citation, parent_pars_inserted))
                            else:
                                #comment_part.comment_citations.add((citation, parent_pars_inserted))
                                to_be_added.append((citation, parent_pars_inserted))
                        except:
                            pass  # Handle the exception as per your requirement
                # seshat_comment_part.comment_citations.clear()
                # seshat_comment_part.comment_citations.add(*to_be_added)
                seshat_comment_part.comment_citations_plus.clear()
                #seshat_comment_part.comment_citations_plus.add(*to_be_added)

                for item in to_be_added:
                    # Query for an existing row based on citation and SeshatCommentPart
                    scp_through_ctn, created = ScpThroughCtn.objects.get_or_create(
                        seshatcommentpart=seshat_comment_part,
                        citation=item[0],
                        defaults={'parent_paragraphs': item[1]}  # Set defaults including parent_paragraphs
                    )

                    # If the row already exists, update its parent_paragraphs
                    if not created:
                        scp_through_ctn.parent_paragraphs = item[1]
                        scp_through_ctn.save()
            return redirect(reverse('seshatcomment-update', kwargs={'pk': com_id}))

    else:
        init_data = ReferenceFormSet2(prefix='refs')
        form = SeshatCommentPartForm2()

    context = {
        'form': form,
        'com_id': com_id,  # Include com_id in the context
        'subcom_order': subcom_order,  # Include subcom_order in the context
        'formset': init_data, 
        #'comm_num': com_id,
        #'comm_part_display': comment_part,
    }
    return render(request, 'core/seshatcomments/seshatcommentpart_create2.html', context)


# Function based NEW:
@permission_required('core.add_seshatprivatecommentpart')
def seshat_private_comment_part_create_from_null_view(request, private_com_id):
    """
    Create a new private comment part.

    Note:
        This view is only accessible to users with the 'add_seshatprivatecommentpart' permission.

    Args:
        request (HttpRequest): The request object.
        private_com_id (int): The primary key of the private comment.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == 'POST':
        form = SeshatPrivateCommentPartForm(request.POST)
        oopsi = request.POST.getlist('selected_items')
        print("ooopsiiiiiiiiiiiiiiii,", oopsi)
        big_father = SeshatPrivateComment.objects.get(id=private_com_id)

        if form.is_valid():
            private_comment_part_text = form.cleaned_data['private_comment_part_text']
            my_private_comment_readers = form.cleaned_data['private_comment_reader']
            user_logged_in = request.user

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except:
                seshat_expert_instance = None

            seshat_private_comment_part = SeshatPrivateCommentPart(private_comment_part_text=private_comment_part_text, private_comment_owner=seshat_expert_instance, private_comment= big_father)

            seshat_private_comment_part.save()

            seshat_private_comment_part.private_comment_reader.add(*my_private_comment_readers) 

            #print("4444444444444444444444444444444444444")

            return redirect(reverse('seshatprivatecomment-update', kwargs={'pk': private_com_id}))

    else:
        form = SeshatPrivateCommentPartForm()
        #print('5555555555555555555555555555555')

    context = {
        'form': form,
        'private_com_id': private_com_id,
    }

    #print("333333333333333333333333333333")
    return render(request, 'core/seshatcomments/seshatprivatecommentpart_create2.html', context)

    # return render(request, 'core/seshatcomments/seshatcommentpart_update2.html', {'form': form, 'formset': init_data, 'comm_num':pk, 'comm_part_display': comment_part})

class SeshatCommentPartUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update a comment part.
    """
    model = SeshatCommentPart
    form_class = SeshatCommentPartForm
    template_name = "core/seshatcomments/seshatcommentpart_update.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the subdescription."


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
        logged_in_user = self.request.user
        logged_in_expert = Seshat_Expert.objects.get(user=logged_in_user)
        #context["com_id"] = self.kwargs['com_id']
        #context["subcom_order"] = self.kwargs['subcom_order']
        context["comment_curator"] = logged_in_expert
        context["comment_curator_id"] = logged_in_expert.id
        context["comment_curator_name"] = "Selected USER"

        #context["subcom_order"] = self.comment_order

        #print(context)

        return context
    
class SeshatPrivateCommentPartUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update a private comment part.
    """
    model = SeshatPrivateCommentPart
    form_class = SeshatPrivateCommentPartForm
    template_name = "core/seshatcomments/seshatprivatecommentpart_update2.html"
    permission_required = 'core.add_seshatprivatecommentpart'
    success_message = "You successfully updated the Private comment."


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
        logged_in_user = self.request.user
        logged_in_expert = Seshat_Expert.objects.get(user=logged_in_user)
        context["private_com_id"] = self.kwargs['private_com_id']
        context["pk"] = self.kwargs['pk']
        #context["subcom_order"] = self.kwargs['subcom_order']
        context["private_comment_owner"] = logged_in_expert

        #666666666666666666666666666")

        return context


class SeshatCommentPartDelete(PermissionRequiredMixin, DeleteView):
    """
    Delete a comment part.
    """
    model = SeshatCommentPart
    #success_url = reverse_lazy('seshatcommentparts')
    #success_url = reverse_lazy('seshatcommentparts')

    #('seshatcomment-update', self.pk)
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'
    
    # def get_success_url(self):
    #     return redirect(reverse('seshatcomment-update', kwargs={'pk': self.object.comment.pk}))
    def get_success_url(self):
        return reverse_lazy('seshatcomment-update', kwargs={'pk': self.object.comment.pk})


class SeshatCommentPartDetailView(generic.DetailView):
    model = SeshatCommentPart
    template_name = "core/seshatcomments/seshatcommentpart_detail.html"




##### Extra function for seshat comments


# POLITY

class PolityCreate(PermissionRequiredMixin, CreateView):
    """
    Create a new Polity.
    """
    model = Polity
    form_class = PolityForm
    template_name = "core/polity/polity_form.html"
    permission_required = 'core.add_capital'
    success_url = reverse_lazy('polities')

    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        # Custom validation to check if a Polity with the same new_name already exists
        new_name = form.cleaned_data['new_name']
        existing_polity = Polity.objects.filter(new_name=new_name)

        if existing_polity.exists():
            messages.error(self.request, "A Polity with this new_name already exists.")
            return self.form_invalid(form)

        # Continue with the default behavior if validation passes
        return super().form_valid(form)
    
    def form_invalid(self, form):
        #return HttpResponseRedirect(reverse('seshat-index'))
        messages.error(self.request, "Form submission failed. Please check the form.")
        # Redirect to the 'polities' page
        return self.render_to_response(self.get_context_data(form=form))


class PolityUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update a Polity.
    """
    model = Polity
    form_class = PolityUpdateForm
    template_name = "core/polity/polity_form.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the Polity."

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
        context['pk'] = self.object.pk
        return context
    
    def get_success_url(self):
        return reverse_lazy('polity-detail-main', kwargs={'pk': self.object.pk})
    #success_url = reverse_lazy('polity-detail-main')



# class PolityListView(PermissionRequiredMixin, SuccessMessageMixin, generic.ListView):
#     model = Polity
#     template_name = "core/polity/polity_list.html"
#     permission_required = 'core.add_capital'

#     def get_absolute_url(self):
#         return reverse('polities')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         all_ngas = Nga.objects.all()
#         all_pols = Polity.objects.select_related('ngapolityrel__polity_party', 'ngapolityrel__nga_party').order_by('start_year').all()
#         all_nga_pol_rels = Ngapolityrel.objects.all()

#         all_world_regions = {a_nga.world_region: [a_nga.subregion] for a_nga in all_ngas}

#         ultimate_wregion_dic = {}

#         for a_world_region, all_its_sub_regions in all_world_regions.items():
#             ultimate_wregion_dic[a_world_region] = {}

#             for a_subregion in all_its_sub_regions:
#                 all_politys_on_the_polity_list_page = Polity.objects.filter(
#                     ngapolityrel__polity_party__name=F('name'),
#                     ngapolityrel__nga_party__world_region=a_world_region,
#                     ngapolityrel__nga_party__subregion=a_subregion
#                 ).distinct()

#                 ultimate_wregion_dic[a_world_region][a_subregion] = list(all_politys_on_the_polity_list_page)

#         context["all_ngas"] = all_ngas
#         context["all_nga_pol_rels"] = all_nga_pol_rels
#         context["all_world_regions"] = all_world_regions
#         context["ultimate_wregion_dic"] = ultimate_wregion_dic

#         return context


class PolityListView_old(PermissionRequiredMixin, SuccessMessageMixin, generic.ListView):
    """
    List all polities.

    Note:
        This class is not used in the current implementation.
    """
    model = Polity
    template_name = "core/polity/polity_list.html"
    permission_required = 'core.add_capital'

    #paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polities')

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
        all_ngas = Nga.objects.all()
        all_pols = Polity.objects.all().order_by('start_year')
        all_nga_pol_rels  = Ngapolityrel.objects.all()
        all_world_regions = {}
        for a_nga in all_ngas:
            if a_nga.world_region not in all_world_regions.keys():
                all_world_regions[a_nga.world_region] = [a_nga.subregion]
            else:
                if a_nga.subregion not in all_world_regions[a_nga.world_region]:
                    all_world_regions[a_nga.world_region].append(a_nga.subregion)
        
        ultimate_wregion_dic = {'Europe': {},
        'Southwest Asia': {},
        'Africa':  {},
        'Central Eurasia': {},
        'South Asia':  {},
        'Southeast Asia': {},
        'East Asia':  {},
        'Oceania-Australia':  {},
        'North America':  {},
        'South America':  {},
        }
        all_politys_on_the_polity_list_page = []
        for a_world_region, all_its_sub_regions in all_world_regions.items():
            for a_subregion in all_its_sub_regions:
                list_for_a_subregion = []
                for a_polity in all_pols:
                    for a_rel in all_nga_pol_rels:
                        if a_rel.polity_party.name == a_polity.name and a_world_region == a_rel.nga_party.world_region and a_subregion == a_rel.nga_party.subregion and a_polity not in list_for_a_subregion:
                            list_for_a_subregion.append(a_polity)
                            if a_polity not in all_politys_on_the_polity_list_page:
                                all_politys_on_the_polity_list_page.append(a_polity)
                        
                ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion
        context["all_ngas"] = all_ngas
        context["all_nga_pol_rels"] = all_nga_pol_rels
        context["all_world_regions"] = all_world_regions
        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        #print(ultimate_wregion_dic)

        #print(f"out of {len(all_pols)}: {len(all_politys_on_the_polity_list_page)} were taken care of.")
        

        return context

class PolityListView1(SuccessMessageMixin, generic.ListView):
    """
    List all polities.

    Note:
        This class is not used in the current implementation.
    """
    model = Polity
    template_name = "core/polity/polity_list.html"

    #paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polities')

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
        all_ngas = Nga.objects.all()
        all_pols = Polity.objects.all().order_by('start_year')
        all_nga_pol_rels  = Ngapolityrel.objects.all()
        all_world_regions = {}
        for a_nga in all_ngas:
            if a_nga.world_region not in all_world_regions.keys():
                all_world_regions[a_nga.world_region] = [a_nga.subregion]
            else:
                if a_nga.subregion not in all_world_regions[a_nga.world_region]:
                    all_world_regions[a_nga.world_region].append(a_nga.subregion)
        
        ultimate_wregion_dic = {'Europe': {},
        'Southwest Asia': {},
        'Africa':  {},
        'Central Eurasia': {},
        'South Asia':  {},
        'Southeast Asia': {},
        'East Asia':  {},
        'Oceania-Australia':  {},
        'North America':  {},
        'South America':  {},
        'Nomad Polities': {
            "Nomad Land": []
        },
        }
        all_politys_on_the_polity_list_page = []
        nomad_polities = []
        for a_world_region, all_its_sub_regions in all_world_regions.items():
            for a_subregion in all_its_sub_regions:
                list_for_a_subregion = []
                for a_polity in all_pols:
                    for a_rel in all_nga_pol_rels:
                        if a_rel.polity_party.name == a_polity.name and a_world_region == a_rel.nga_party.world_region and a_subregion == a_rel.nga_party.subregion and a_polity not in list_for_a_subregion:
                            list_for_a_subregion.append(a_polity)
                            if a_polity not in all_politys_on_the_polity_list_page:
                                all_politys_on_the_polity_list_page.append(a_polity)
                        
                ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion
        # nomads
        for a_polity in all_pols:
            if a_polity not in nomad_polities and a_polity not in all_politys_on_the_polity_list_page:
                nomad_polities.append(a_polity)
        ultimate_wregion_dic['Nomad Polities'][ "Nomad Land"] = nomad_polities
        context["all_ngas"] = all_ngas
        context["all_nga_pol_rels"] = all_nga_pol_rels
        context["all_world_regions"] = all_world_regions
        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        #print(ultimate_wregion_dic)

        #print(f"out of {len(all_pols)}: {len(all_politys_on_the_polity_list_page)} were taken care of.")
        

        return context
    

class PolityListViewX(SuccessMessageMixin, generic.ListView):
    """
    List all polities.

    Note:
        This class is not used in the current implementation.
    """
    model = Polity
    template_name = "core/polity/polity_list.html"

    #paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polities')

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
        all_ngas = Nga.objects.all()
        all_pols = Polity.objects.all().order_by('start_year')
        pol_count = len(all_pols)
        #import time
        #start_time = time.time()

        all_polities_g_sc_wf = give_polity_app_data()


        #all_nga_pol_rels  = Ngapolityrel.objects.all()
        all_world_regions = {}
        for a_nga in all_ngas:
            if a_nga.world_region not in all_world_regions.keys():
                all_world_regions[a_nga.world_region] = [a_nga.subregion]
            else:
                if a_nga.subregion not in all_world_regions[a_nga.world_region]:
                    all_world_regions[a_nga.world_region].append(a_nga.subregion)
        
        ultimate_wregion_dic = {'Europe': {},
        'Southwest Asia': {},
        'Africa':  {},
        'Central Eurasia': {},
        'South Asia':  {},
        'Southeast Asia': {},
        'East Asia':  {},
        'Oceania-Australia':  {},
        'North America':  {},
        'South America':  {},
        'Nomad Polities': {
            "Nomad Land": []
        },
        }

        sub_regions_details = {'Western Europe': 'British Isles, France, Low Countries, Switzerland', 'Southern Europe': 'Iberia, Italy, Sicily, Sardinia, Corsica, Balearics', 'Northern Europe': 'Iceland, Scandinavia, Finland, Baltics, Karelia, Kola Peninsula', 'Central Europe': 'Germany, Poland, Austria, Hungary, Czechia, Slovakia', 'Southeastern Europe': 'Yugoslavia, Romania-Moldova, Bulgaria, Albania, Greece', 'Eastern Europe': 'Belarus, non-Steppe Russia and Ukraine', 'Maghreb': 'From Morocco to Libya', 'Northeastern Africa': 'Egypt and Sudan (the Nile Basin)', 'Sahel': 'Mauritania, Mali, Burkina Faso, Niger, Chad (Arid)', 'West Africa': 'From Senegal to Gabon (Tropical)', 'Central Africa': 'Angola and DRC', 'East Africa': 'Tanzania, Burundi, Uganda, So Sudan, Somalia, Ethiopia, Eritrea', 'Southern Africa': 'Namibia, Zambia, Malawi, Mozambique and south', 'Anatolia-Caucasus': 'Turkey, Armenia, Georgia, Azerbaijan', 'Levant-Mesopotamia': 'Israel, Jordan, Lebanon, Syria, Iraq, Kuwait, Khuzestan (Susiana)', 'Arabia': 'Arabian Peninsula', 'Iran': 'Persia, most of Afghanistan, (western Pakistan?)', 'Pontic-Caspian ': 'The steppe belt of Ukraine and Russia', 'Turkestan': 'Turkmenistan, Uzbekistan, Tajikistan, Kyrgyzstan, Kazakstan, Xinjiang', 'Afghanistan': 'Afghanistan', 'Mongolia': 'Mongolia, Inner Mongolia, the steppe part of Manchuria', 'Siberia': 'Urals, West Siberia, Central Siberia, Yakutia', 'Arctic Asia': 'The tundra and arctic regions of Eurasia sans Scandinavia', 'Tibet': 'Tibet', 'Northeast Asia': 'Korea, Japan, forest part of Manchuria, Russian Far East', 'China': 'China without Tibet, Inner Mongolia, and Xinjiang', 'Indo-Gangetic Plain': 'Pakistan, Punjab, upper and middle Ganges', 'Eastern India': 'Lower Ganges (Bangladesh) and eastern India (Assam)', 'Central India': 'Deccan, etc', 'Southern India': 'Southern India and Sri Lanka', 'Mainland': 'Myanmar, Thailand, Cambodia, Laos, south Vietnam', 'Archipelago': 'Malaysia, Indonesia, Philippines', 'Australia': 'Australia', 'New Guinea': 'New Guinea', 'Polynesia': 'Polynesia', 'Arctic America': 'Alaska, Arctic Canada, Greenland', 'Western NA': 'West Coast, the Rockies, and the American SouthWest', 'Great Plains': 'American Great Plains', 'Mississippi Basin': 'From the Great Lakes to Louisiana', 'East Coast': 'East Coast of US', 'Mexico': 'Mexico and Central America (without Panama)', 'Caribbean': 'Caribbean islands, Panama, coastal Columbia-Venezuela', 'Andes': 'From Ecuador to Chile', 'Amazonia': 'Brazil, Guyanas, plus Amazonian parts of bordering states', 'Southern Cone': 'Parguay, Uruguay, Argentina'}
        all_politys_on_the_polity_list_page = []
        nomad_polities = []

        # modify the world regions:
        all_world_regions["Africa"].append("East Africa")
        all_world_regions["Africa"].append("Southern Africa")
        all_world_regions["South Asia"].append("Southern India")

        for a_polity in all_pols:
            try:
                #a_polity.has_general = has_general_data_for_polity(a_polity.id)
                #a_polity.has_sc = has_sc_data_for_polity(a_polity.id)
                #a_polity.has_wf = has_wf_data_for_polity(a_polity.id)
                #a_polity.has_cc = has_crisis_cases_data_for_polity(a_polity.id)
                #a_polity.has_pt = has_power_transition_data_for_polity(a_polity.id)
                a_polity.has_g_sc_wf = all_polities_g_sc_wf[a_polity.id]
                
            except:
                #a_polity.has_general = None
                #a_polity.has_sc = None
                #a_polity.has_wf = None
                #a_polity.has_cc = None
                #a_polity.has_pt = None
                a_polity.has_g_sc_wf = None

        #end_time = time.time()
        #print('elapsed_time ', end_time-start_time)

        for a_world_region, all_its_sub_regions in all_world_regions.items():
            for a_subregion in all_its_sub_regions:
                list_for_a_subregion = []
                extras_for_AFR_WEST = []
                extras_for_AFR_EAST = []
                extras_for_AFR_SA = []
                extras_for_SA_SI = []

                for a_polity in all_pols:
                    if a_polity.home_nga and a_world_region == a_polity.home_nga.world_region and a_subregion == a_polity.home_nga.subregion and a_polity not in list_for_a_subregion:
                        list_for_a_subregion.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_AFR_WEST":
                        extras_for_AFR_WEST.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_AFR_EAST":
                        extras_for_AFR_EAST.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_AFR_SA":
                        extras_for_AFR_SA.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)
                    elif a_polity.polity_tag == "POL_SA_SI":
                        extras_for_SA_SI.append(a_polity)
                        if a_polity not in all_politys_on_the_polity_list_page:
                            all_politys_on_the_polity_list_page.append(a_polity)

                if a_world_region == "Africa" and a_subregion == "West Africa":
                    ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_AFR_WEST
                elif a_world_region == "Africa" and a_subregion == "East Africa":
                    ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_AFR_EAST
                elif a_world_region == "Africa" and a_subregion == "Southern Africa":
                   ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_AFR_SA
                elif a_world_region == "South Asia" and a_subregion == "Southern India":
                   ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion + extras_for_SA_SI
                else:
                    ultimate_wregion_dic[a_world_region][a_subregion] = list_for_a_subregion

                        
        # nomads
        for a_polity in all_pols:
            if a_polity not in nomad_polities and a_polity not in all_politys_on_the_polity_list_page:
                nomad_polities.append(a_polity)

        ultimate_wregion_dic['Nomad Polities'][ "Nomad Land"] = nomad_polities
        context["sub_regions_details"] = sub_regions_details
        #context["all_nga_pol_rels"] = all_nga_pol_rels
        context["all_world_regions"] = all_world_regions
        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        #print(ultimate_wregion_dic)
        context['all_pols'] = all_pols
        context["pol_count"] = pol_count

        #print(f"out of {len(all_pols)}: {len(all_politys_on_the_polity_list_page)} were taken care of.")
        

        return context
    
class PolityListViewLight(SuccessMessageMixin, generic.ListView):
    """
    List all polities.
    """
    model = Polity
    template_name = "core/polity/polity_list_light.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polities-light')

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
        #import time
        #start_time = time.time()
        all_srs_unsorted = Seshat_region.objects.all()
        all_mrs_unsorted = Macro_region.objects.all()


        custom_order = [5, 2, 11, 3, 4, 9, 10, 8, 7, 6, 1, 23, 24, 27, 26,25, 29,28, 31,33,32,30, ]  

        custom_order_sr = [20, 18, 17, 15, 19, 16, 3, 4, 5, 7, 1, 2, 6, 43, 61, 62, 44, 45, 10, 13, 8, 9, 11, 12, 14, 58, 59, 38, 39, 37, 36, 40, 41, 42, 28, 29, 30, 26,25, 27,24, 22, 23, 21, 32, 31, 33, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57 ]

        all_mrs = sorted(all_mrs_unsorted, key=lambda item: custom_order.index(item.id))
        all_srs = sorted(all_srs_unsorted, key=lambda item: custom_order_sr.index(item.id))

        all_pols = Polity.objects.all().order_by('start_year')
        pol_count = len(all_pols)

        ultimate_wregion_dic = {}
        ultimate_wregion_dic_top = {}
        for a_mr in all_mrs:
            if a_mr not in ultimate_wregion_dic:
                ultimate_wregion_dic[a_mr.name] = {}
            if a_mr not in ultimate_wregion_dic_top:
                ultimate_wregion_dic_top[a_mr.name] = {}
            for a_sr in all_srs:
                if a_sr.mac_region_id == a_mr.id:
                    if a_sr.name not in ultimate_wregion_dic[a_mr.name]:
                        ultimate_wregion_dic[a_mr.name][a_sr.name] = []
                    if a_sr.name not in ultimate_wregion_dic_top[a_mr.name]:
                        ultimate_wregion_dic_top[a_mr.name][a_sr.name] = [a_sr.subregions_list, 0]

        #all_polities_g_sc_wf, freq_dic = give_polity_app_data()
        #all_polities_g_sc_wf = give_polity_app_data()
        freq_dic = {}
        freq_dic["d"] = 0

        for a_polity in all_pols:
            if a_polity.home_seshat_region:
                ultimate_wregion_dic[a_polity.home_seshat_region.mac_region.name][a_polity.home_seshat_region.name].append(a_polity)
                ultimate_wregion_dic_top[a_polity.home_seshat_region.mac_region.name][a_polity.home_seshat_region.name][1] += 1
            if a_polity.general_description:
                freq_dic["d"] += 1

        for a_polity in all_pols:
            a_polity.has_g_sc_wf = None

        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        context["ultimate_wregion_dic_top"] = ultimate_wregion_dic_top
        context['all_pols'] = all_pols
        context['all_srs'] = all_srs
        context["pol_count"] = pol_count
        freq_dic['pol_count'] = pol_count
        context["freq_data"] = freq_dic

        #end_time = time.time()
        #print('elapsed_time ', end_time-start_time)

        return context

class PolityListView(SuccessMessageMixin, generic.ListView):
    """
    List all polities.
    """
    model = Polity
    template_name = "core/polity/polity_list.html"

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polities')

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
        #import time
        #start_time = time.time()
        all_srs_unsorted = Seshat_region.objects.all()
        all_mrs_unsorted = Macro_region.objects.all()

        # 1 | World
        # 2 | Africa
        # 3 | Central and Northern Eurasia
        # 4 | East Asia
        # 5 | Europe
        # 6 | South America
        # 7 | North America
        # 8 | Oceania-Australia
        # 9 | South Asia
        # 10 | Southeast Asia
        # 11 | Southwest Asia

        custom_order = [5, 2, 11, 3, 4, 9, 10, 8, 7, 6, 1, 23, 24, 27, 26,25, 29,28, 31,33,32,30, ]  

        custom_order_sr = [20, 18, 17, 15, 19, 16, 3, 4, 5, 7, 1, 2, 6, 43, 61, 62, 44, 45, 10, 13, 8, 9, 11, 12, 14, 58, 59, 38, 39, 37, 36, 40, 41, 42, 28, 29, 30, 26,25, 27,24, 22, 23, 21, 32, 31, 33, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57 ]

        all_mrs = sorted(all_mrs_unsorted, key=lambda item: custom_order.index(item.id))
        all_srs = sorted(all_srs_unsorted, key=lambda item: custom_order_sr.index(item.id))

        all_pols = Polity.objects.all().order_by('start_year')
        pol_count = len(all_pols)

        ultimate_wregion_dic = {}
        ultimate_wregion_dic_top = {}
        for a_mr in all_mrs:
            if a_mr not in ultimate_wregion_dic:
                ultimate_wregion_dic[a_mr.name] = {}
            if a_mr not in ultimate_wregion_dic_top:
                ultimate_wregion_dic_top[a_mr.name] = {}
            for a_sr in all_srs:
                if a_sr.mac_region_id == a_mr.id:
                    if a_sr.name not in ultimate_wregion_dic[a_mr.name]:
                        ultimate_wregion_dic[a_mr.name][a_sr.name] = []
                    if a_sr.name not in ultimate_wregion_dic_top[a_mr.name]:
                        ultimate_wregion_dic_top[a_mr.name][a_sr.name] = [a_sr.subregions_list, 0]

        all_polities_g_sc_wf, freq_dic = give_polity_app_data()
        #all_polities_g_sc_wf = give_polity_app_data()
        #freq_dic = {}
        freq_dic["d"] = 0

        for a_polity in all_pols:
            if a_polity.home_seshat_region:
                ultimate_wregion_dic[a_polity.home_seshat_region.mac_region.name][a_polity.home_seshat_region.name].append(a_polity)
                ultimate_wregion_dic_top[a_polity.home_seshat_region.mac_region.name][a_polity.home_seshat_region.name][1] += 1
            if a_polity.general_description:
                freq_dic["d"] += 1

        for a_polity in all_pols:
            try:
                a_polity.has_g_sc_wf = all_polities_g_sc_wf[a_polity.id]
            except:
                a_polity.has_g_sc_wf = None

            all_durations = {
                "intr": [],
                "gv": [],
                "pt": [],
                "color": "xyz",
            }
            all_durations["intr"] = [a_polity.start_year, a_polity.end_year]
            # Pol_dur object
            try:
                Polity_duration_object = Polity_duration.objects.get(polity_id=a_polity.id)

                polity_duration_coded = []
                polity_duration_coded.extend([f'{Polity_duration_object.polity_year_from}, {Polity_duration_object.polity_year_to}'])
                all_durations["gv"] = [Polity_duration_object.polity_year_from, Polity_duration_object.polity_year_to]
            except:
                polity_duration_coded = [-10000, 2000]

            # Pow Trans Data
            try:
                Polity_pt_objects = Power_transition.objects.filter(polity_id=a_polity.id)

                polity_duration_implied = []
                pol_dur_min_list = []
                pol_dur_max_list = []

                for a_pt in Polity_pt_objects:
                    if a_pt.year_from is not None:
                        pol_dur_min_list.append(a_pt.year_from)
                    if a_pt.year_to is not None:
                        pol_dur_max_list.append(a_pt.year_to)

                polity_duration_implied = [min(pol_dur_min_list), max(pol_dur_max_list)]
                all_durations["pt"] = polity_duration_implied
            except:
                polity_duration_implied = [-10000, 2000]

            a_polity.all_durations = all_durations
            if all_durations["intr"] and all_durations["gv"] and all_durations["pt"]:
                if (all_durations["intr"] == all_durations["gv"] == all_durations["pt"]):
                    a_polity.color = "ggg"
                elif (all_durations["intr"] == all_durations["gv"]):
                    a_polity.color = "ggr"
                elif (all_durations["intr"] == all_durations["pt"]):
                    a_polity.color = "grg"
                elif (all_durations["gv"] == all_durations["pt"]):
                    a_polity.color = "rgg"
            elif all_durations["intr"] and all_durations["gv"]:
                if (all_durations["intr"] == all_durations["gv"]):
                    a_polity.color = "ggm"
                else:
                    a_polity.color = "grm"
            elif all_durations["intr"] and all_durations["pt"]:
                if (all_durations["intr"] == all_durations["pt"]):
                    a_polity.color = "gmg"
                elif all_durations["intr"][0] == -10000:
                    a_polity.color = "rmr"
                else:
                    a_polity.color = "gmr"
            elif all_durations["intr"] and all_durations["intr"][0] == -10000:
                a_polity.color = "rmm"
            elif all_durations["intr"]:
                a_polity.color = "gmm"
                




        context["ultimate_wregion_dic"] = ultimate_wregion_dic
        context["ultimate_wregion_dic_top"] = ultimate_wregion_dic_top
        context['all_pols'] = all_pols
        context['all_srs'] = all_srs
        context["pol_count"] = pol_count
        freq_dic['pol_count'] = pol_count
        context["freq_data"] = freq_dic

        #end_time = time.time()
        #print('elapsed_time ', end_time-start_time)

        return context
    

class PolityListViewCommented(PermissionRequiredMixin, SuccessMessageMixin, generic.ListView):
    """
    List all polities with comments.
    """
    model = Polity
    template_name = "core/polity/polity_list_commented.html"
    permission_required = 'core.add_seshatprivatecommentpart'


    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('polities')

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

        #all_pols = Polity.objects.filter(private_comment__isnull=False).order_by('start_year')
        #all_pols = Polity.objects.exclude(Q(private_comment__isnull=True) | Q(private_comment=''))
        all_pols = Polity.objects.exclude(Q(private_comment_n__isnull=True) | Q(private_comment_n=1))

        pol_count = len(all_pols)

        all_polities_g_sc_wf, freq_dic = give_polity_app_data()

        for a_polity in all_pols:
            try:
                a_polity.has_g_sc_wf = all_polities_g_sc_wf[a_polity.id]
            except:
                a_polity.has_g_sc_wf = None

        context['all_pols'] = all_pols
        context["pol_count"] = pol_count

        return context
    



class PolityDetailView(SuccessMessageMixin, generic.DetailView):
    """
    Show details of a polity.
    """
    model = Polity
    template_name = "core/polity/polity_detail.html"

    def get_object(self, queryset=None):
        """
        Get the object of the view.

        Args:
            queryset: The queryset to use.

        Returns:
            Polity: The object of the view.

        Raises:
            Http404: If no polity matches the given name.
            Http404: If multiple polities are found with the same name.
        """
        if 'pk' in self.kwargs:
            return get_object_or_404(Polity, pk=self.kwargs['pk'])
        elif 'new_name' in self.kwargs:
            new_name = self.kwargs['new_name']
            try:
                # Attempt to get the object by new_name, handle multiple objects returned
                return Polity.objects.get(new_name=new_name)
            except Polity.MultipleObjectsReturned:
                # Handle the case of multiple objects with the same new_name
                raise Http404("Multiple objects with the same new_name")
            except Polity.DoesNotExist:
                # Handle the case where no object with the given new_name is found
                raise Http404("No Polity matches the given new_name")
        else:
            # Handle the case where neither pk nor new_name is provided
            return None

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
        context['pk'] = self.kwargs['pk']
        try:
            context["all_data"] = get_all_data_for_a_polity(self.object.pk, "crisisdb") 
            context["all_general_data"], context["has_any_general_data"] = get_all_general_data_for_a_polity(self.object.pk)
            context["all_sc_data"], context["has_any_sc_data"] = get_all_sc_data_for_a_polity(self.object.pk)
            context["all_wf_data"], context["has_any_wf_data"] = get_all_wf_data_for_a_polity(self.object.pk)
            context["all_rt_data"], context["has_any_rt_data"] = get_all_rt_data_for_a_polity(self.object.pk)
            context["all_crisis_cases_data"] = get_all_crisis_cases_data_for_a_polity(self.object.pk)
            context["all_power_transitions_data"] = get_all_power_transitions_data_for_a_polity(self.object.pk)
            all_Ras = Polity_research_assistant.objects.filter(polity_id=self.object.pk)
            all_Ras_ids = all_Ras.values_list('polity_ra_id', flat=True)
            experts = Seshat_Expert.objects.filter(id__in=all_Ras_ids)
            
            all_general_ras = []
            for xx in experts:
                an_ra = xx.user.first_name + " " + xx.user.last_name
                if an_ra not in all_general_ras:
                    all_general_ras.append(an_ra)

            all_general_ras_string = ", ".join(all_general_ras)

            

            #my_users_general = [User.objects.get(pk=aa.polity_ra_id) for aa in all_Ras]
            context["majid"] = {"utm_zone": "benam"}
            context["all_Ras"] = all_general_ras_string

        except:
            context["all_data"] = None
            context["all_general_data"] = None
            context["all_sc_data"] = None
            context["all_wf_data"] = None
            context["all_rt_data"] = None
        ################# NEW
        Polity_object = Polity.objects.get(id=self.object.pk)

        # Get the related data
        all_durations = {
            "intr": [],
            "gv": [],
            "pt": [],
            "color": "xyz",
        }
        try:
            intrinsic_duration = f'Polity Intrinsic Duration: {Polity_object.start_year}, {Polity_object.end_year}'
            all_durations["intr"] = [Polity_object.start_year, Polity_object.end_year]
        except:
            intrinsic_duration = [-10000, 2000]
        # Pol_dur object
        try:
            Polity_duration_object = Polity_duration.objects.get(polity_id=self.object.pk)

            polity_duration_coded = []
            polity_duration_coded.extend([f'{Polity_duration_object.polity_year_from}, {Polity_duration_object.polity_year_to}'])
            all_durations["gv"] = [Polity_duration_object.polity_year_from, Polity_duration_object.polity_year_to]
        except:
            polity_duration_coded = [-10000, 2000]

        # Pow Trans Data
        try:
            Polity_pt_objects = Power_transition.objects.filter(polity_id=self.object.pk)

            polity_duration_implied = []
            pol_dur_min_list = []
            pol_dur_max_list = []

            for a_pt in Polity_pt_objects:
                if a_pt.year_from is not None:
                    pol_dur_min_list.append(a_pt.year_from)
                if a_pt.year_to is not None:
                    pol_dur_max_list.append(a_pt.year_to)

            polity_duration_implied = [min(pol_dur_min_list), max(pol_dur_max_list)]
            all_durations["pt"] = polity_duration_implied
        except:
            polity_duration_implied = [-10000, 2000]

        if all_durations["intr"] and all_durations["gv"] and all_durations["pt"]:
            if (all_durations["intr"] == all_durations["gv"] == all_durations["pt"]):
               all_durations['color'] = "ggg"
            elif (all_durations["intr"] == all_durations["gv"]):
               all_durations['color'] = "ggr"
            elif (all_durations["intr"] == all_durations["pt"]):
               all_durations['color'] = "grg"
            elif (all_durations["gv"] == all_durations["pt"]):
               all_durations['color'] = "rgg"
        elif all_durations["intr"] and all_durations["gv"]:
            if (all_durations["intr"] == all_durations["gv"]):
               all_durations['color'] = "ggm"
            else:
               all_durations['color'] = "grm"
        elif all_durations["intr"] and all_durations["pt"]:
            if (all_durations["intr"] == all_durations["pt"]):
               all_durations['color'] = "gmg"
            elif all_durations["intr"][0] == -10000:
               all_durations['color'] = "rmr"
            else:
               all_durations['color'] = "gmr"
        elif all_durations["intr"] and all_durations["intr"][0] == -10000:
           all_durations['color'] = "rmm"
        elif all_durations["intr"]:
           all_durations['color'] = "gmm"

        context["all_durations"] = all_durations
        #####################


        #x = polity_detail_data_collector(self.object.pk)
        #context["all_data"] = dict(x)
        #print(self.object.pk)
        context["all_vars"] = {
            "arable_land": "arable_land",
            "agricultural_population": "agricultural_population",
        }
        try:
            my_pol = Polity.objects.get(pk=self.object.pk)
            nga_pol_rels = my_pol.polity_sides.all()
            time_deltas = []
            for nga_pol_rel in nga_pol_rels:
                if (nga_pol_rel.year_from, nga_pol_rel.year_to) not in time_deltas:
                    time_deltas.append((nga_pol_rel.year_from, nga_pol_rel.year_to))

            concise_rels = {}
            for time_delta in time_deltas:
                nga_list = []
                for nga_pol_rel in nga_pol_rels:
                    if time_delta[0] == nga_pol_rel.year_from and time_delta[1] == nga_pol_rel.year_to:
                        nga_list.append(nga_pol_rel.nga_party)
                
                concise_rels[time_delta] = nga_list # "  ~~~   ".join(nga_list)
            context["nga_pol_rel"] = concise_rels
            #print("__________________________")
        except:
            context["nga_pol_rel"] = None
            #print("*************")
        #import django
        #print(django.get_version())

        preceding_data = []
        succeeding_data = []

        prec_data = Polity_preceding_entity.objects.filter(
                    Q(polity_id=self.object.pk) | Q(other_polity_id=self.object.pk))
        for vv in prec_data:
            if vv.polity and vv.polity.id == self.object.pk:
                preceding_data.append(vv)
            elif vv.other_polity and vv.other_polity.id == self.object.pk:
                succeeding_data.append(vv)

        # Pass the data to the template
        context['preceding_data'] = preceding_data
        context['succeeding_data'] = succeeding_data

        return context


    
# NGA

class NgaCreate(PermissionRequiredMixin, CreateView):
    """
    Create a new NGA.
    """
    model = Nga
    form_class = NgaForm
    template_name = "core/nga/nga_form.html"
    permission_required = 'core.add_capital'
    success_url = reverse_lazy('ngas')

    def form_valid(self, form):
        """
        Validate the form.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """
        Handle invalid form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponse: The response object.
        """
        return HttpResponseRedirect(reverse('seshat-index'))


class NgaUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update an NGA.
    """
    model = Nga
    form_class = NgaForm
    template_name = "core/nga/nga_update.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the Nga."
    success_url = reverse_lazy('ngas')


class NgaListView(generic.ListView):
    """
    List all NGAs.
    """
    model = Nga
    template_name = "core/nga/nga_list.html"
    #paginate_by = 10

class NgaDetailView(generic.DetailView):
    """
    Show details of an NGA.
    """
    model = Nga
    template_name = "core/nga/nga_detail.html"


# Capital

class CapitalCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Create a new Capital.
    """
    model = Capital
    form_class = CapitalForm
    template_name = "core/capital/capital_form_create.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully created a new Capital."
    success_url = reverse_lazy('capitals')

    # def form_valid(self, form):
    #     return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     return HttpResponseRedirect(reverse('capital-create'))


class CapitalUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Update a Capital.
    """
    model = Capital
    form_class = CapitalForm
    template_name = "core/capital/capital_form.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully updated the Capital."
    success_url = reverse_lazy('capitals')


class CapitalListView(generic.ListView):
    """
    List all Capitals.
    """
    model = Capital
    template_name = "core/capital/capital_list.html"
    #paginate_by = 10

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('capitals')
    

class CapitalDelete(PermissionRequiredMixin, DeleteView):
    """
    Delete a Capital.
    """
    model = Capital
    success_url = reverse_lazy('capitals')
    template_name = "core/delete_general.html"
    permission_required = 'core.add_capital'
    success_message = "You successfully deleted one Capital."

    

@permission_required('core.view_capital')
def capital_download(request):
    """
    Download all Capitals as CSV.

    Note:
        This view is only accessible to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    items = Capital.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="capitals.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['capital', 
                     'current_country', 'longitude', 'latitude','is_verified', 'note'])

    for obj in items:
        writer.writerow([obj.name, obj.current_country, obj.longitude, obj.latitude, obj.is_verified, obj.note])

    return response


def signup_traditional(request):
    """
    Handle user signup.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            #current_site = get_current_site(request)
            #subject = 'Activate Your Seshat Account'
            message = render_to_string('core/account_activation_email.html', {
                'user': user,
                'domain': 'seshat-db.com',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })

            send_mail(
                'Seshat-DB Email Verification',
                message,
                'seshatdb@gmail.com',  # Replace with your sender email
                [user.email],  # Replace with recipient email(s)
                fail_silently=False,
            )
            #user.email_user(subject, message)
            # to_be_sent_email = EmailMessage(subject=subject, body=message,
            #                                 from_email=settings.EMAIL_FROM_USER, to=[user.email])

            # #print(settings.EMAIL_HOST_USER)
            # to_be_sent_email.send()
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'core/signup_traditional.html', {'form': form})


def signupfollowup(request):
    """
    Handle user signup follow-up.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    print(settings.EMAIL_HOST_USER)
    return render(request, 'core/signup-followup.html')


def activate(request, uidb64, token):
    """
    Activate user account.

    Args:
        request: The request object.
        uidb64: The user ID encoded in base64.
        token: The token.

    Returns:
        HttpResponse: The HTTP response.
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        #uid = str(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.save()
        login(request, user)
        return redirect('signup-followup')
    else:
        return render(request, 'core/account_activation_invalid.html')


# Discussion Room
def discussion_room(request):
    """
    Render the discussion room page.
    """
    return render(request, 'core/discussion_room.html')

# NLP Room 1
def nlp_datapoints(request):
    """
    Render the NLP data points page.
    """
    return render(request, 'core/nlp_datapoints.html')

# NLP Room 2
def nlp_datapoints_2(request):
    """
    Render the NLP data points page.
    """
    return render(request, 'core/nlp_datapoints_2.html')

def account_activation_sent(request):
    """
    Render the account activation sent page.
    """
    return render(request, 'core/account_activation_sent.html')


def variablehierarchysetting(request):
    """
    Handle variable hierarchy setting. This is a view for the admin to set the
    variable hierarchy.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    my_vars = dic_of_all_vars()
    my_vars_keys = list(my_vars.keys())
    my_vars_good_keys = []
    for item in my_vars_keys:
        good_key = item[0:9] + item[9].lower() + item[10:]
        good_key = good_key.replace('gdp', 'GDP')
        good_key = good_key.replace('gDP', 'GDP')
        my_vars_good_keys.append(good_key)
    all_var_hiers_to_be_hidden = Variablehierarchy.objects.filter(is_verified=True)
    all_var_hiers_to_be_hidden_names = []
    for var in all_var_hiers_to_be_hidden:
        with_crisisdb_name = "crisisdb_" + var.name
        var_name = with_crisisdb_name[0:9] + with_crisisdb_name[9].lower() + with_crisisdb_name[10:]
        var_name = var_name.replace('gdp', 'GDP')
        var_name = var_name.replace('gDP', 'GDP')

        if with_crisisdb_name in my_vars_good_keys:
            var_name = with_crisisdb_name[0:9] + with_crisisdb_name[9].lower() + with_crisisdb_name[10:]
            var_name = var_name.replace('gdp', 'GDP')
            var_name = var_name.replace('gDP', 'GDP')

            all_var_hiers_to_be_hidden_names.append(var_name)
    print('I am here...\n\n')
    #print(all_var_hiers_to_be_hidden_names)
    my_vars_tuple = [('', ' -- Select a CrisisDB Variable -- ')]
    for var in my_vars_good_keys:
        if var not in all_var_hiers_to_be_hidden_names:
            without_crisisdb_var = var[9:]
            var_name = without_crisisdb_var[0].lower() + without_crisisdb_var[1:]
            var_name = var_name.replace('gdp', 'GDP')
            var_name = var_name.replace('gDP', 'GDP')

            my_var_tuple = (var_name, var_name)
            my_vars_tuple.append(my_var_tuple)

    all_sections = Section.objects.all()
    all_sections_tuple = [('', ' -- Select Section -- ')]
    for section in all_sections:
        my_section = section.name
        my_section_tuple = (my_section, my_section)
        all_sections_tuple.append(my_section_tuple)
    # subsections
    all_subsections = Subsection.objects.all()
    all_subsections_tuple = [('', ' -- Select Section First -- ')]
    for subsection in all_subsections:
        my_subsection = subsection.name
        my_subsection_tuple = (my_subsection, my_subsection)
        all_subsections_tuple.append(my_subsection_tuple)
    # Let's create an API serializer for section and subsection heierarchy
    url = "http://127.0.0.1:8000/api/sections/"
    #url = "https://www.majidbenam.com/api/sections/"
    #url = settings.MY_CURRENT_SERVER + "/api/sections/"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    all_my_data = resp.json()['results']
    sections_tree = {}
    sections_options_for_JS = {}
    for list_item in all_my_data:
        subsect_dic = {}
        subsects_only_list = []
        for subsec in list_item['subsections']:
            list_to_be = []
            subsects_only_list.append(subsec)
            sel_sect = Section.objects.get(name=list_item['name'])
            sel_subsect = Subsection.objects.get(name=subsec)
            my_selected_vars_objects = Variablehierarchy.objects.filter( section=sel_sect, subsection=sel_subsect,)
            for var_obj in my_selected_vars_objects:
                #print(var_obj)
                list_to_be.append(var_obj.name)
            subsect_dic[subsec] = list_to_be
        sections_tree[list_item['name']] = subsect_dic
        sections_options_for_JS[list_item['name']] = subsects_only_list
    context = {
        'sectionOptions': sections_options_for_JS, 
        'section_tree_data': sections_tree,
    }
    #print(context['sectionOptions'])
    #print(context['section_tree_data'])


    if request.method == 'POST':
        form = VariablehierarchyFormNew(request.POST)
        if True:
            data = request.POST
            variable_name = data["variable_name"]
            #is_verified_str = data["is_verified"]
            is_verified_str = data.get("is_verified", False)
            if is_verified_str == 'on':
                is_verified = True
            elif is_verified_str == 'off':
                is_verified = False
            else:
                is_verified = False
            section_name = Section.objects.get(name=data["section_name"])
            subsection_name = Subsection.objects.get(
                name=data["subsection_name"])
            # check to see if subsection and section match
            if data["subsection_name"] in sections_tree[data["section_name"]]:
                new_var_hierarchy = Variablehierarchy(
                    name=variable_name, section=section_name, subsection=subsection_name,  is_verified=is_verified)
                new_var_hierarchy.save()
                #print('Valid Foooooooooooorm: \n\n',)
                # print(data)
                my_message = f'''You have successfully submitted {variable_name} to: {section_name} >  {subsection_name}'''
                messages.success(request, my_message)
                return HttpResponseRedirect(reverse('variablehierarchysetting'))
            else:
                messages.warning(request, 'Form submission unssuccessful, section and subsection do not match.')
                #return render(request, 'core/Variablehierarchy.html', {'form': VariablehierarchyFormNew()})

        else:
            data = request.POST
            #print('halllooooooooo:', data["variable_name"])
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

    else:
        form = VariablehierarchyFormNew()
    context['form'] = form
    context['variable_list'] = list(my_vars_tuple)
    context['section_list'] = list(all_sections_tuple)
    context['subsection_list'] = list(all_subsections_tuple)

    #context['SuccessMessage'] = "Done Perfectly."
    return render(request, 'core/variablehierarchy.html', context)



###############
def do_zotero(results):
    """
    Process the results from the Zotero API.

    Args:
        results: The results from the Zotero API.

    Returns:
        list: A list of dictionaries containing the processed data.
    """
    import re
    mother_ref_dic = []
    for i, item in enumerate(results):
        #print(i, ": ", item['data']['key'], item['data']['date'])
        #if item['data']['key'] in ["MJT9UJE4", "NIKCMK5L", "QTI79LX9"]:
        #    print("______________")
        #    print(item)
        a_key = item['data']['key']
        if a_key == "3BQQ8WN8":
            print("I skipped over  youuuuu: 3BQQ8WN8 because you are not in the database!")
            continue
        if a_key == 'RR6R3383':
            print("I skipped over  youuuuu: RR6R3383 because your title is too big")
            continue
            
            #print(pprint.pprint(item))
        try:
            # we need to make sure that all the changes in Zotero will be reflected here.
            potential_new_ref = Reference.objects.get(zotero_link=a_key)
            # full_date = item['data'].get('date')
            # if full_date:
            #     year = re.search(r'[12]\d{3}', full_date)
            #     if year:
            #         year_int = int(year[0])
            #         if potential_new_ref.year != year_int:
            #             print(f"Item Changed On Zotero: {a_key}")
            continue
        except:          
            my_dic = {}
            try:
                if item['data']['key']:
                    tuple_key = item['data']['key']
                    my_dic['key'] = tuple_key
                else:
                    pass #print("key is empty for index: ", i, item['data']['itemType'])
            except:
                pass #print("No key for item with index: ", i)
            try:
                if item['data']['itemType']:
                    tuple_item = item['data']['itemType']
                    my_dic['itemType'] = tuple_item
                else:
                    pass #print("itemType is empty for index: ", i, item['data']['itemType'])
            except:
                pass #print("No itemType for item with index: ", i)
            try:
                num_of_creators = len(item['data']['creators'])
                if num_of_creators < 4 and num_of_creators > 0:
                    all_creators_list = []  
                    for j in range(num_of_creators):
                        if a_key == "MM6AEU7H":
                            print("I saw youuuuuuuuuuuuuuu more probably because you have contributors instead of authors")
                        try:
                            try:
                                good_name = item['data']['creators'][j]['lastName']
                            except:
                                good_name = item['data']['creators'][j]['name']
                        except:
                            good_name = ("NO_NAMES",)
                        all_creators_list.append(good_name)
                    good_name_with_space = "_".join(all_creators_list)
                    good_name_with_underscore = good_name_with_space.replace(' ', '_')
                    my_dic['mainCreator'] = good_name_with_underscore
                elif num_of_creators > 3:
                    try:
                        try:
                            good_name = item['data']['creators'][0]['lastName']
                        except:
                            good_name = item['data']['creators'][0]['name']
                    except:
                        good_name = ("NO_NAME",)
                    good_name_with_space = good_name + '_et_al'
                    good_name_with_underscore = good_name_with_space.replace(' ', '_')
                    my_dic['mainCreator'] = good_name_with_underscore
                else:
                    my_dic['mainCreator'] = "NO_CREATOR" 
                #pass #print(my_dic['mainCreator'])
            except:
                my_dic['mainCreator'] = "NO_CREATORS"
                pass #print("No mainCreator for item with index: ", i, item['data']['itemType'])
            try:
                if item['data']['date']:
                    full_date = item['data']['date']
                    year = re.search(r'[12]\d{3}', full_date)
                    year_int = int(year[0])
                    my_dic['year'] = year_int
                else:
                    my_dic['year'] = 0
                    #pass #print("year is empty for index: ", i, item['data']['itemType'])
                #pass #print(my_dic['year'])
            except:
                my_dic['year'] = -1
                #pass #print("No year for item with index: ", i, item['data']['itemType'])
            try:
                try:
                    if item['data']['bookTitle']:
                        if a_key == "MM6AEU7H":
                            print("I saw youuuuuuuuuuuuuuu more")
                        if item['data']['itemType'] == 'bookSection':
                            good_title = item['data']['title'] + " (IN) " + item['data']['bookTitle']
                            pass #print (i, ": ", a_key, "    ", good_title)
                        else:
                            good_title = item['data']['title']
                            pass #print (i, ": ", a_key, "    ", good_title)
                        counter_bookTitle = counter_bookTitle + 1
                        my_dic['title'] = good_title
                    else:
                        good_title = item['data']['title']
                        my_dic['title'] = good_title
                        if a_key == "MM6AEU7H":
                            print("I saw youuuuuuuuuuuuuuu more")
                        #pass #print (i, ": ", a_key, "    ", good_title)
                except:
                    my_dic['title'] = item['data']['title']
                    #pass #print (i, ": ", a_key, "    ", item['data']['title'])
            except:
                pass #print("No title for item with index: ", i)
            
            pot_title = my_dic.get('title')
            if not pot_title:
                pot_title = "NO_TITLE_PROVIDED_IN_ZOTERO"
            #print("Years: ", my_dic.get('year'))
            #print("****************")

            try:
                if item['data']['dateAdded']:
                    full_date = item['data']['dateAdded']
                    my_dic['created_date'] = full_date
                    #print(f'Full Date caught is: {full_date}')
                else:
                    my_dic['created_date'] = None
                    #pass #print("year is empty for index: ", i, item['data']['itemType'])
                #pass #print(my_dic['year'])
            except:
                my_dic['created_date'] = None
            # item_type
            try:
                if item['data']['itemType']:
                    full_item = item['data']['itemType']
                    my_dic['item_type'] = full_item
                else:
                    my_dic['item_type'] = 'No_Item_Type'
                    #pass #print("year is empty for index: ", i, item['data']['itemType'])
                #pass #print(my_dic['year'])
            except:
                my_dic['item_type'] = 'No_Item_Type'
            newref = Reference(title=pot_title, year=my_dic.get('year'), creator=my_dic.get('mainCreator'), zotero_link=my_dic.get('key'), item_type=my_dic.get('item_type'), created_date=my_dic.get('created_date'))
            #newref = Reference(title=my_dic['title'], year=my_dic['year'], creator=my_dic['mainCreator'], zotero_link=my_dic['key'])

            if my_dic.get('year') < 2040:
                #print("Here we Goooooooooo:", newref.created_date)
                newref.save()
                #print("Here we Goooooooooo 2:", newref.created_date)
                mother_ref_dic.append(my_dic)

    #print(len(mother_ref_dic))
    #print(counter_bookTitle)
    print("Bye Zotero")
    return mother_ref_dic

def do_zotero_manually(results):
    """
    Process the results from the Zotero API.

    Args:
        results: The results from the Zotero API.

    Returns:
        list: A list of dictionaries containing the processed data.
    """
    mother_ref_dic = []
    for i, item in enumerate(results):

        a_key = item['key']
        if a_key == "3BQQ8WN8":
            print("I skipped over  youuuuu: 3BQQ8WN8 because you are not in the database!")
            continue
        if a_key == 'RR6R3383':
            print("I skipped over  youuuuu: RR6R3383 because your title is too big")
            continue
            
        try:
            potential_new_ref = Reference.objects.get(zotero_link=a_key)
            continue
        except:          
            my_dic = {}
            my_dic['key'] = a_key
            my_dic['mainCreator'] = item['mainCreator']
            my_dic['year'] = item['year']
            my_dic['title'] = item['title']

            newref = Reference(title=my_dic.get('title'), year=my_dic.get('year'), creator=my_dic.get('mainCreator'), zotero_link=my_dic.get('key'))

            if my_dic.get('year') < 2040:
                newref.save()
                mother_ref_dic.append(my_dic)


    print("Bye Zotero Manually")
    return mother_ref_dic


##########

def update_citations_from_inside_zotero_update():
    """
    This function takes all the references and build a citation for them.

    Args:
        None

    Returns:
        None
    """
    from datetime import datetime
    all_refs = Reference.objects.all()
    for ref in all_refs:
        a_citation = Citation.objects.get_or_create(ref=ref, page_from=None, page_to=None)
        a_citation[0].save()
    print("Halllooooo")
    # Citation.objects.bulk_create(all_citations)
    #return render (request, 'core/references/reference_list.html')

###########


def synczoteromanually(request):
    """
    This function is used to manually input the references from the Zotero data
    available in the manual_input_refs.py file into the database.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    print("Hallo Zotero Manually")
    from .manual_input_refs import manual_input_refs 

    new_refs = do_zotero_manually(manual_input_refs)
    context = {}
    context["newly_adds"] = new_refs
    update_citations_from_inside_zotero_update()
    return render (request, 'core/references/synczotero.html', context)

def synczotero(request):
    """
    This function is used to sync the Zotero data with the database.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    print("Hallo Zotero")

    from pyzotero import zotero
    zot = zotero.Zotero(1051264, 'group', config('ZOTERO_API_KEY'))
    results = zot.everything(zot.top())
    #results = zot.top(limit=100)

    print(len(results))
    counter_bookTitle = 0
    new_refs = do_zotero(results[0:300])
    context = {}
    context["newly_adds"] = new_refs
    update_citations_from_inside_zotero_update()
    #num_1_ref = Reference.objects.get(zotero_link ="FGFSZUNB")
    #num_1_ref.year = 2014
    #num_1_ref.save()
    return render (request, 'core/references/synczotero.html', context)

def synczotero100(request):
    """
    This function is used to sync the Zotero data with the database.

    Note:
        This function syncs only 100 references.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    print("Hallo Zotero")

    from pyzotero import zotero
    zot = zotero.Zotero(1051264, 'group', config('ZOTERO_API_KEY'))
    #results = zot.everything(zot.top())
    results = zot.top(limit=100)

    print(len(results))
    counter_bookTitle = 0
    new_refs = do_zotero(results)
    context = {}
    context["newly_adds"] = new_refs
    # Seemingly problematic call from Zotero to Nginx
    #update_citations_from_inside_zotero_update()
    #num_1_ref = Reference.objects.get(zotero_link ="FGFSZUNB")
    #num_1_ref.year = 2014
    #num_1_ref.save()
    return render (request, 'core/references/synczotero.html', context)



def update_citations(request):
    """
    This function takes all the references and build a citation for them.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    all_refs = Reference.objects.all()
    for ref in all_refs:
        a_citation = Citation.objects.get_or_create(ref=ref, page_from=None, page_to=None)
        a_citation[0].save()
    # Citation.objects.bulk_create(all_citations)
    return render (request, 'core/references/reference_list.html')


@require_GET
def polity_filter_options_view(request):
    """
    This view returns the options for the polity filter.

    Note:
        The view is decorated with the `require_GET` decorator to ensure that
        only GET requests are allowed.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The JSON response.
    """
    search_text = request.GET.get('search_text', '')

    # Filter the options based on the search text
    options = Polity.objects.filter(name__icontains=search_text).values('id', 'name')

    response = {
        'options': list(options)
    }
    return JsonResponse(response)


def download_oldcsv(request, file_name):
    """
    Download a CSV file.

    Args:
        request: The request object.
        file_name (str): The name of the file to download.

    Returns:
        FileResponse: The file response.
    """
    file_path = os.path.join(settings.STATIC_ROOT, 'csvfiles', file_name)
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response



def seshatindex(request):
    """
    Render the Seshat landing page.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    app_names = ['general','sc', 'wf', 'crisisdb']  # Replace with your app name
    context = {
        'pols_data': [],
        'general_data': [],
        'sc_data': [], 
        'wf_data': [],
        'crisisdb': [],
        'pt_data': [],
        'cc_data': [],
        'hs_data': [],
        'sr_data': [],
        'general_examples': [('Alternative Name', 'polity_alternative_names_all', 'Identity and Location'),
                            ('Polity Peak Years', 'polity_peak_yearss_all', 'Temporal Bounds'), 
                            ('Polity Capital', 'polity_capitals_all', 'Identity and Location'), 
                            ('Polity Language', 'polity_languages_all', 'Language'),
                            ('Polity Religion', 'polity_religions_all', 'Religion'),
                            ('Degree of Centralization', 'polity_degree_of_centralizations_all', 'Temporal Bounds'),
                            ('Succeeding Entity', 'polity_succeeding_entitys_all', 'Supra-cultural relations'),
                            ('Relationship to Preceding Entity', 'polity_relationship_to_preceding_entitys_all', 'Supra-cultural relations'),
                            ],

        'sc_examples': [('Polity Territory', 'polity_territorys_all', 'Social Scale'), 
                        ('Polity Population', 'polity_populations_all', 'Social Scale'), 
                        ('Settlement Hierarchy', 'settlement_hierarchys_all', 'Hierarchical Complexity'), 
                        ('Irrigation System', 'irrigation_systems_all', 'Specialized Buildings: polity owned'), 
                        ('Merit Promotion', 'merit_promotions_all', 'Bureaucracy Characteristics'), 
                        ('Formal Legal Code', 'formal_legal_codes_all', 'Law'), 
                        ('Road', 'roads_all', 'Transport Infrastructure'), 
                        ('Postal Station', 'postal_stations_all', 'Information / Postal System')],
        'wf_examples': [('Bronze', 'bronzes_all', 'Military use of Metals'),
                        ('Javelin', 'javelins_all', 'Projectiles'),
                        ('Battle Axe', 'battle_axes_all', 'Handheld Weapons'),
                        ('Sword', 'swords_all', 'Handheld Weapons'),
                        ('Horse', 'horses_all', 'Animals used in warfare'),
                        ('Small Vessels (canoes, etc)', 'small_vessels_canoes_etcs_all', 'Naval technology'),
                        ('Shield', 'shields_all', 'Armor'),
                        ('Wooden Palisade', 'small_vessels_canoes_etcs_all', 'Fortifications'),
                        ]
        #'crisisdb_examples': [],
        #'pt_examples': [],
        #'cc_examples': [],
        #'sr_examples': [],

        }
    all_srs_unsorted = Seshat_region.objects.exclude(name="Somewhere")
    all_mrs_unsorted = Macro_region.objects.exclude(name="World")
    to_be_appended_y = [len(all_srs_unsorted), len(all_mrs_unsorted)] 
    context['sr_data'] = to_be_appended_y

    all_pols_count = Polity.objects.count()
    to_be_appended_y = [all_pols_count, len(all_srs_unsorted)] 
    context['pols_data'] = to_be_appended_y

    eight_pols = Polity.objects.order_by('?')[:8]
    context['eight_pols'] = eight_pols

    #eight_srs = Seshat_region.objects.exclude(name="Somewhere").order_by('?')[:8]
    eight_srs_0 = Seshat_region.objects.exclude(name="Somewhere").annotate(
    num_polities=Count('home_seshat_region'))
    eight_srs = eight_srs_0.order_by('-num_polities')[:8]


    context['eight_srs'] = eight_srs

    for app_name in app_names:
        models = apps.get_app_config(app_name).get_models()
        unique_politys = set()
        number_of_variables = 0
        number_of_rows_in_app = 0
        app_key = app_name + "_data"
        for model in models:
            model_name = model.__name__
            if model_name == "Ra":
                continue
            if  model_name.startswith("Us_violence"):
                queryset_count = model.objects.count()

                queryset = model.objects.all()

                to_be_appended_xxxx = [queryset_count, 1,]
                context['us_data'] = to_be_appended_xxxx
                eight_uss = queryset.order_by('?')[:8]
                context['eight_uss'] = eight_uss
                continue
            if  model_name.startswith("Us_"):
                continue
            if  model_name.startswith("Power_transition"):
                queryset_count = model.objects.count()

                queryset = model.objects.all()
                politys = queryset.values_list('polity', flat=True).distinct()

                to_be_appended_x = [queryset_count, 1, len(set(politys)),]
                context['pt_data'] = to_be_appended_x
                eight_pts = queryset.order_by('?')[:8]
                context['eight_pts'] = eight_pts
                continue
            if  model_name.startswith("Crisis_consequence"):
                queryset_count = model.objects.count()

                queryset = model.objects.all()
                politys = queryset.values_list('polity', flat=True).distinct()

                to_be_appended_xx = [queryset_count, 1, len(set(politys)),]
                context['cc_data'] = to_be_appended_xx
                eight_ccs = queryset.order_by('?')[:8]
                context['eight_ccs'] = eight_ccs
                continue
            if  model_name.startswith("Human_sacrifice"):
                queryset_count = model.objects.count()

                queryset = model.objects.all()
                politys = queryset.values_list('polity', flat=True).distinct()

                to_be_appended_xxx = [queryset_count, 1, len(set(politys)),]
                context['hs_data'] = to_be_appended_xxx
                eight_hss = queryset.order_by('?')[:8]
                context['eight_hss'] = eight_hss
                continue

            queryset_count = model.objects.count()

            queryset = model.objects.all()
            politys = queryset.values_list('polity', flat=True).distinct()
            unique_politys.update(politys)
            number_of_variables += 1

            number_of_rows_in_app += queryset_count

        to_be_appended = [number_of_rows_in_app, number_of_variables, len(unique_politys),]

        context[app_key] = to_be_appended

    return render(request, 'core/seshat-index.html', context=context)


def get_polity_data_single(polity_id):
    """
    Get the data for a single polity. The returned data includes the number of
    records for each app (general, sc, wf, hs, cc, pt).

    Args:
        polity_id: The ID of the polity.

    Returns:
        dict: The data for the polity.
    """
    from seshat.apps.crisisdb.models import Crisis_consequence, Power_transition, Human_sacrifice
    from django.apps import apps

    app_models_general = apps.get_app_config('general').get_models()
    app_models_sc = apps.get_app_config('sc').get_models()
    app_models_wf = apps.get_app_config('wf').get_models()

    data = {
        'g': 0,
        'sc': 0,
        'wf': 0,
        'hs': 0,
        'cc': 0,
        'pt': 0,
    }

    for model in app_models_general:
        if hasattr(model, 'polity_id') and model.objects.filter(polity_id=polity_id).exists():
            data['g'] += model.objects.filter(polity_id=polity_id).count()

    for model in app_models_sc:
        if hasattr(model, 'polity_id') and model.objects.filter(polity_id=polity_id).exists():
            data['sc'] += model.objects.filter(polity_id=polity_id).count()

    for model in app_models_wf:
        if hasattr(model, 'polity_id') and model.objects.filter(polity_id=polity_id).exists():
            data['wf'] += model.objects.filter(polity_id=polity_id).count()

    data['hs'] = Human_sacrifice.objects.filter(polity=polity_id).count()
    data['cc'] = Crisis_consequence.objects.filter(polity=polity_id).count()
    data['pt'] = Power_transition.objects.filter(polity=polity_id).count()

    return data

@permission_required('core.view_capital')
def download_csv_all_polities(request):
    """
    Download a CSV file containing all polities.

    Note:
        This view is restricted to users with the 'view_capital' permission.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    # Create a response object with CSV content type
    response = HttpResponse(content_type='text/csv')
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    file_name = f"polities_{current_datetime}.csv"

    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    # Create a CSV writer
    writer = csv.writer(response, delimiter='|')

    # type the headers
    writer.writerow(['macro_region', 'home_seshat_region',  'polity_new_ID', 'polity_old_ID', 'polity_long_name', 'start_year', 'end_year', 'home_nga', 'G', "SC", "WF", "RT", "HS", "CC", "PT", 'polity_tag', 'shapefile_name'])

    items = Polity.objects.all()
    coded_value_data, freq_data = give_polity_app_data()

    for obj in items:
        #coded_values_data = get_polity_data_single(obj.id)
        #print(obj.id)
        #print(type(obj))
        if obj.home_seshat_region:
            writer.writerow([obj.home_seshat_region.mac_region.name, obj.home_seshat_region.name, obj.new_name, obj.name, obj.long_name, obj.start_year, obj.end_year, obj.home_nga,  coded_value_data[obj.id]['g'], coded_value_data[obj.id]['sc'], coded_value_data[obj.id]['wf'], coded_value_data[obj.id]['rt'], coded_value_data[obj.id]['hs'], coded_value_data[obj.id]['cc'], coded_value_data[obj.id]['pt'], obj.get_polity_tag_display(), obj.shapefile_name])
        else:
            writer.writerow(["None", "None", obj.new_name, obj.name, obj.long_name, obj.start_year, obj.end_year, obj.home_nga,  coded_value_data[obj.id]['g'], coded_value_data[obj.id]['sc'], coded_value_data[obj.id]['wf'], coded_value_data[obj.id]['rt'], coded_value_data[obj.id]['hs'], coded_value_data[obj.id]['cc'], coded_value_data[obj.id]['pt'], obj.get_polity_tag_display(), obj.shapefile_name])

    return response

##### additions for the seshatcommentpart enhancement
# views.py


def get_or_create_citation(reference, page_from, page_to):
    """
    Get or create a Citation instance. If a matching citation already exists, it
    is returned; otherwise, a new one is created.

    Args:
        reference (Reference): The reference.
        page_from (int): The starting page number.
        page_to (int): The ending page number.

    Returns:
        Citation: The Citation instance.
    """
    # Check if a matching citation already exists
    existing_citation = Citation.objects.filter(
        ref=reference,
        page_from=page_from,
        page_to=page_to
    ).first()

    # If a matching citation exists, return it; otherwise, create a new one
    return existing_citation or Citation.objects.create(
        ref=reference,
        page_from=page_from,
        page_to=page_to
    )
from django.shortcuts import render, redirect
from .forms import SeshatCommentPartForm, SeshatCommentForm2


from .models import SeshatCommentPart, Citation

def seshatcommentpart_create_view_old(request):
    """
    Create a new SeshatCommentPart instance.

    Note:
        The old view of the SeshatCommentPart creation is not currently used in
        the application.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    if request.method == 'POST':
        form = SeshatCommentPartForm2(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            reference = form.cleaned_data['reference']
            page_from = form.cleaned_data['page_from']
            page_to = form.cleaned_data['page_to']
            comment_order = form.cleaned_data['comment_order']

            # Get or create the Citation instance
            citation = get_or_create_citation(reference, page_from, page_to)
            user_logged_in = request.user

            comment_instance = SeshatComment.objects.create(text='a new_comment_text')

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except Seshat_Expert.DoesNotExist:
                seshat_expert_instance = None

            # Create the SeshatCommentPart instance and associate the Citation
            comment_part = SeshatCommentPart.objects.create(
                comment=comment_instance,
                comment_part_text=comment_text,
                comment_order=comment_order,
                comment_curator=seshat_expert_instance 
            )
            comment_part.comment_citations.add(citation)

            return redirect('seshat-index')  # Redirect to a success page

    else:
        form = SeshatCommentPartForm2()

    return render(request, 'core/seshatcomments/seshatcommentpart_create.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from .models import SeshatCommentPart, Citation, SeshatComment

def seshatcommentpart_create_view(request):
    """
    Create a new SeshatCommentPart instance.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    if request.method == 'POST':
        form = SeshatCommentPartForm2(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            comment_order = form.cleaned_data['comment_order']
            user_logged_in = request.user

            comment_instance = SeshatComment.objects.create(text='a new_comment_text')

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except Seshat_Expert.DoesNotExist:
                seshat_expert_instance = None

            # Create the SeshatCommentPart instance
            comment_part = SeshatCommentPart.objects.create(
                comment=comment_instance,
                comment_part_text=comment_text,
                comment_order=comment_order,
                comment_curator=seshat_expert_instance 
            )

            # Process the formset
            reference_formset = ReferenceFormSet(request.POST, prefix='refs')
            print("++++++ffffffff++++++++")
            if reference_formset.is_valid():
                print("Ahsaaaaant")
            else:
                print(f'Formset errors: {reference_formset.errors}, {reference_formset.non_form_errors()}')

            if reference_formset.has_changed():
                print("Ahsaaaaaaaaaaaaaaaaaant")
            else:
                print(f'Formset errors: {reference_formset.errors}, {reference_formset.non_form_errors()}')
            print("++++++ffffffff++++++++")
            for i, reference_form in enumerate(reference_formset):
                if reference_form.is_valid():
                    print("+++++++xxaaaaaaaaaxx+++++++")
                    try:
                        reference = reference_form.cleaned_data['ref']
                        page_from = reference_form.cleaned_data['page_from']
                        page_to = reference_form.cleaned_data['page_to']

                        # Get or create the Citation instance
                        #citation = get_or_create_citation(reference, page_from, page_to)
                        citation, created = Citation.objects.get_or_create(
                            ref=reference,
                            page_from=int(page_from),
                            page_to=int(page_to)
                        )


                        # Associate the Citation with the SeshatCommentPart
                        comment_part.comment_citations.add(citation)
                        print("+++++++xxxx+++++++")
                        print("I am here::::::", citation)
                    except:
                        print("OOOPsi")
                else:
                    print(f'Form errors: {reference_form.errors}')

            return redirect('seshat-index')  # Redirect to a success page

    else:
        form = SeshatCommentPartForm2()

    return render(request, 'core/seshatcomments/seshatcommentpart_create.html', {'form': form})


def get_provinces(selected_base_map_gadm='province'):
    """
    Get all the province or country shapes for the map base layer.

    Args:
        selected_base_map_gadm (str): The selected base map GADM level.

    Returns:
        list: A list of dictionaries containing the province or country shapes.
    """

    # Use the appropriate Django ORM query based on the selected baseMapGADM value
    if selected_base_map_gadm == 'country':
        rows = GADMCountries.objects.values_list('geom', 'COUNTRY')
        provinces = [
            {
                'aggregated_geometry': GEOSGeometry(geom).geojson,
                'country': country
            }
            for geom, country in rows if geom is not None
        ]
    elif selected_base_map_gadm == 'province':
        rows = GADMProvinces.objects.values_list('geom', 'COUNTRY', 'NAME_1', 'ENGTYPE_1')
        provinces = [
            {
                'aggregated_geometry': GEOSGeometry(geom).geojson,
                'country': country,
                'province': name,
                'province_type': engtype
            }
            for geom, country, name, engtype in rows if geom is not None
        ]

    return provinces

def get_polity_shape_content(displayed_year="all", seshat_id="all", tick_number=80, override_earliest_year=None, override_latest_year=None, geometries=True):
    """
    This function returns the polity shapes and other content for the map.
    Only one of displayed_year or seshat_id should be set; not both.

    Note:
        seshat_id in Cliopatria is new_name in Polity.

    Args:
        displayed_year (str): The year to display the polities for. "all" will return all polities. Any given year will return polities that were active in that year.
        seshat_id (str): The seshat_id of the polity to display. If a value is provided, only the shapes for that polity being returned.

    Returns:
        dict: The content for the polity shapes.
    """

    if displayed_year != "all" and seshat_id != "all":
        raise ValueError("Only one of displayed_year or seshat_id should be set not both.")

    if displayed_year != "all":
        rows = Cliopatria.objects.filter(polity_start_year__lte=displayed_year, polity_end_year__gte=displayed_year)
    elif seshat_id != "all":
        # Note: this query assumes that some polities have multiple seshat_ids separated by a semicolon, but none are included inside a different longer seshat_id
        rows = Cliopatria.objects.filter(seshat_id__contains=seshat_id)
    else:
        rows = Cliopatria.objects.all()

    if geometries:
        # Convert 'geom' to GeoJSON in the database query
        rows = rows.annotate(geom_json=AsGeoJSON('geom'))
        # Filter the rows to return
        rows = rows.values('id', 'seshat_id', 'name', 'start_year', 'end_year', 'polity_start_year', 'polity_end_year', 'colour', 'area', 'geom_json', 'components', 'member_of', 'wikipedia_name') 
    else:
        rows = rows.values('id', 'seshat_id', 'name', 'start_year', 'end_year', 'polity_start_year', 'polity_end_year', 'colour', 'area', 'components', 'member_of', 'wikipedia_name')
    shapes = list(rows)

    seshat_ids = [shape['seshat_id'] for shape in shapes if shape['seshat_id']]

    polities = Polity.objects.filter(new_name__in=seshat_ids).values('new_name', 'id', 'long_name')

    polity_info = [(polity['new_name'], polity['id'], polity['long_name']) for polity in polities]

    seshat_id_page_id = {new_name: {'id': id, 'long_name': long_name or ""} for new_name, id, long_name in polity_info}

    if 'migrate' not in sys.argv:
        result = Cliopatria.objects.aggregate(
            min_year=Min('polity_start_year'), 
            max_year=Max('polity_end_year')
        )
        earliest_year = result['min_year']
        latest_year = result['max_year']
        initial_displayed_year = earliest_year
    else:
        earliest_year, latest_year = 2024, 2024  # These are not used in the web app, but are set to avoid errors when running migrations
        initial_displayed_year = -3400

    # Overrides can be set to restrict the years shown on the map
    if override_earliest_year is not None:
        earliest_year = override_earliest_year
    if override_latest_year is not None:
        latest_year = override_latest_year

    if displayed_year == "all":
        displayed_year = initial_displayed_year 

    if seshat_id != "all":  # Used in the polity pages
        earliest_year = min([shape['start_year'] for shape in shapes])
        displayed_year = earliest_year
        latest_year = max([shape['end_year'] for shape in shapes])

    # Get the years for the tick marks on the year slider
    tick_years = [round(year) for year in np.linspace(earliest_year, latest_year, num=tick_number)]

    content = {
        'shapes': shapes,
        'earliest_year': earliest_year,
        'display_year': displayed_year,
        'tick_years': json.dumps(tick_years),
        'latest_year': latest_year,
        'seshat_id_page_id': seshat_id_page_id
    }
    if hasattr(settings, 'CESIUM_ION_ACCESS_TOKEN'):
        content['CESIUM_ION_ACCESS_TOKEN'] = settings.CESIUM_ION_ACCESS_TOKEN  # This is used in the template to access Cesium Ion

    return content

def get_all_polity_capitals():
    """
    Get capital cities for polities that have them.

    Returns:
        dict: A dictionary containing the capital cities for polities.
    """
    from seshat.apps.core.templatetags.core_tags import get_polity_capitals

    # Try to get the capitals from the cache
    all_capitals_info = cache.get('all_capitals_info')

    if all_capitals_info is None:
        all_capitals_info = {}
        for polity in Polity.objects.all():
            caps = get_polity_capitals(polity.id)

            if caps:
                # Set the start and end years to be the same as the polity where missing
                modified_caps = caps
                i = 0
                for capital_info in caps:
                    if capital_info['year_from'] == None:
                        modified_caps[i]['year_from'] = polity.start_year
                    if capital_info['year_to'] == None:
                        modified_caps[i]['year_to'] = polity.end_year
                    i+=1
                all_capitals_info[polity.new_name] = modified_caps
        # Store the capitals in the cache for 1 hour
        cache.set('all_capitals_info', all_capitals_info, 3600)

    return all_capitals_info

def assign_variables_to_shapes(shapes, app_map):
    """
    Assign the absent/present variables to the shapes.

    Args:
        shapes (list): The shapes to assign the variables to.
        app_map (dict): A dictionary mapping app names to their long names.

    Returns:
        tuple: A tuple containing the shapes and the variables.
    """
    from seshat.apps.sc.models import ABSENT_PRESENT_CHOICES  # These should be the same in the other apps
    # Try to get the variables from the cache
    variables = cache.get('variables')
    if variables is None:
        variables = {}
        for app_name, app_name_long in app_map.items():
            module = apps.get_app_config(app_name)
            variables[app_name_long] = {}
            models = list(module.get_models())
            for model in models:
                fields = list(model._meta.get_fields())
                for field in fields:
                    if hasattr(field, 'choices') and field.choices == ABSENT_PRESENT_CHOICES:
                        # Get the variable name and formatted name
                        if field.name == 'coded_value':  # Use the class name lower case for rt models where coded_value is used
                            var_name = model.__name__.lower()
                            var_long = getattr(model._meta, 'verbose_name_plural', model.__name__.lower())
                            if var_name == var_long:
                                variable_formatted = var_name.capitalize().replace('_', ' ')
                            else:
                                variable_formatted = var_long
                        else:  # Use the field name for other models
                            var_name = field.name
                            variable_formatted = field.name.capitalize().replace('_', ' ')
                        variables[app_name_long][var_name] = {}
                        variables[app_name_long][var_name]['formatted'] = variable_formatted
                        # Get the variable subsection and subsubsection if they exist
                        variable_full_name = variable_formatted
                        instance = model()
                        if hasattr(instance, 'subsubsection'):
                            variable_full_name = instance.subsubsection() + ': ' + variable_full_name
                        if hasattr(instance, 'subsection'):
                            variable_full_name = instance.subsection() + ': ' + variable_full_name 
                        variables[app_name_long][var_name]['full_name'] = variable_full_name

        # Store the variables in the cache for 1 hour
        cache.set('variables', variables, 3600)

    for app_name, app_name_long in app_map.items():

        app_variables_list = list(variables[app_name_long].keys())
        module_path = 'seshat.apps.' + app_name + '.models'
        module = __import__(module_path, fromlist=[variable.capitalize() for variable in app_variables_list])
        variable_classes = {variable: getattr(module, variable.capitalize()) for variable in app_variables_list}

        seshat_ids = [shape['seshat_id'] for shape in shapes if shape['seshat_id'] != 'none']
        polities = {polity.new_name: polity for polity in Polity.objects.filter(new_name__in=seshat_ids)}

        for variable, class_ in variable_classes.items():
            variable_formatted = variables[app_name_long][variable]['formatted']
            variable_objs = {obj.polity_id: obj for obj in class_.objects.filter(polity_id__in=polities.values())}

            all_variable_objs = {}
            for obj in class_.objects.filter(polity_id__in=polities.values()):
                try:
                    variable_value = getattr(obj, variable)
                except AttributeError:  # For rt models where coded_value is used
                    variable_value = getattr(obj, 'coded_value')
                if obj.polity_id not in all_variable_objs:
                    all_variable_objs[obj.polity_id] = {}
                all_variable_objs[obj.polity_id][variable_value] = [obj.year_from, obj.year_to]

            for shape in shapes:
                shape[variable_formatted] = 'uncoded'  # Default value
                polity = polities.get(shape['seshat_id'])
                if polity:
                    variable_obj = variable_objs.get(polity.id)
                    try:
                        variable_obj_dict = all_variable_objs[polity.id]
                    except KeyError:
                        pass
                    if variable_obj:
                        try:
                            shape[variable_formatted] = getattr(variable_obj, variable)  # absent/present choice         
                            shape[variable_formatted + '_dict'] = variable_obj_dict
                        except AttributeError:  # For rt models where coded_value is used
                            shape[variable_formatted] = getattr(variable_obj, 'coded_value')
                            shape[variable_formatted + '_dict'] = variable_obj_dict
                else:
                    shape[variable_formatted] = 'no seshat page'

    return shapes, variables

def assign_categorical_variables_to_shapes(shapes, variables):
    """
    Assign the categorical variables to the shapes.

    Note:
        Currently only language and religion variables are implemented.

    Args:
        shapes (list): The shapes to assign the variables to.
        variables (dict): The variables to assign to the shapes.

    Returns:
        tuple: A tuple containing the shapes and the variables.
    """
    # Add categorical variables to the variables dictionary
    variables['General Variables'] = {
        'polity_linguistic_family': {'formatted': 'linguistic_family', 'full_name': 'Linguistic Family'},
        'polity_language_genus': {'formatted': 'language_genus', 'full_name': 'Language Genus'},
        'polity_language': {'formatted': 'language', 'full_name': 'Language'},
        'polity_religious_tradition': {'formatted': 'religious_tradition', 'full_name': 'Religious Tradition'},
        'polity_religion_genus': {'formatted': 'religion_genus', 'full_name': 'Religion Genus'},
        'polity_religion_family': {'formatted': 'religion_family', 'full_name': 'Religion Family'},
        'polity_religion': {'formatted': 'religion', 'full_name': 'Religion'},
        'polity_alternate_religion_genus': {'formatted': 'alternate_religion_genus', 'full_name': 'Alternate Religion Genus'},
        'polity_alternate_religion_family': {'formatted': 'alternate_religion_family', 'full_name': 'Alternate Religion Family'},
        'polity_alternate_religion': {'formatted': 'alternate_religion', 'full_name': 'Alternate Religion'},
    }

    # Fetch all polities and store them in a dictionary for quick access
    polities = {polity.new_name: polity for polity in Polity.objects.all()}

    # Fetch all linguistic families, language genuses, and languages and store them in dictionaries for quick access
    linguistic_families = {}
    for lf in Polity_linguistic_family.objects.all():
        if lf.polity_id not in linguistic_families:
            linguistic_families[lf.polity_id] = []
        linguistic_families[lf.polity_id].append(lf)

    language_genuses = {}
    for lg in Polity_language_genus.objects.all():
        if lg.polity_id not in language_genuses:
            language_genuses[lg.polity_id] = []
        language_genuses[lg.polity_id].append(lg)

    languages = {}
    for l in Polity_language.objects.all():
        if l.polity_id not in languages:
            languages[l.polity_id] = []
        languages[l.polity_id].append(l)

    religious_traditions = {}
    for rt in Polity_religious_tradition.objects.all():
        if rt.polity_id not in religious_traditions:
            religious_traditions[rt.polity_id] = []
        religious_traditions[rt.polity_id].append(rt)

    religion_genuses = {}
    for rg in Polity_religion_genus.objects.all():
        if rg.polity_id not in religion_genuses:
            religion_genuses[rg.polity_id] = []
        religion_genuses[rg.polity_id].append(rg)

    religion_families = {}
    for rf in Polity_religion_family.objects.all():
        if rf.polity_id not in religion_families:
            religion_families[rf.polity_id] = []
        religion_families[rf.polity_id].append(rf)

    religions = {}
    for r in Polity_religion.objects.all():
        if r.polity_id not in religions:
            religions[r.polity_id] = []
        religions[r.polity_id].append(r)

    alternate_religion_genuses = {}
    for arg in Polity_alternate_religion_genus.objects.all():
        if arg.polity_id not in alternate_religion_genuses:
            alternate_religion_genuses[arg.polity_id] = []
        alternate_religion_genuses[arg.polity_id].append(arg)

    alternate_religion_families = {}
    for arf in Polity_alternate_religion_family.objects.all():
        if arf.polity_id not in alternate_religion_families:
            alternate_religion_families[arf.polity_id] = []
        alternate_religion_families[arf.polity_id].append(arf)

    alternate_religions = {}
    for ar in Polity_alternate_religion.objects.all():
        if ar.polity_id not in alternate_religions:
            alternate_religions[ar.polity_id] = []
        alternate_religions[ar.polity_id].append(ar)

    # Add language variable info to polity shapes
    for shape in shapes:
        shape['linguistic_family'] = []
        shape['linguistic_family_dict'] = {}
        shape['language_genus'] = []
        shape['language_genus_dict'] = {}
        shape['language'] = []
        shape['language_dict'] = {}
        shape['religious_tradition'] = []
        shape['religious_tradition_dict'] = {}
        shape['religion_genus'] = []
        shape['religion_genus_dict'] = {}
        shape['religion_family'] = []
        shape['religion_family_dict'] = {}
        shape['religion'] = []
        shape['religion_dict'] = {}
        shape['alternate_religion_genus'] = []
        shape['alternate_religion_genus_dict'] = {}
        shape['alternate_religion_family'] = []
        shape['alternate_religion_family_dict'] = {}
        shape['alternate_religion'] = []
        shape['alternate_religion_dict'] = {}
        if shape['seshat_id'] != 'none':  # Skip shapes with no seshat_id
            polity = polities.get(shape['seshat_id'])
            if polity:
                # Get the variables for the polity
                shape['linguistic_family'].extend([lf.linguistic_family for lf in linguistic_families.get(polity.id, [])])
                shape['language_genus'].extend([lg.language_genus for lg in language_genuses.get(polity.id, [])])
                shape['language'].extend([l.language for l in languages.get(polity.id, [])])
                shape['religious_tradition'].extend([rt.religious_tradition for rt in religious_traditions.get(polity.id, [])])
                shape['religion_genus'].extend([rg.religion_genus for rg in religion_genuses.get(polity.id, [])])
                shape['religion_family'].extend([rf.religion_family for rf in religion_families.get(polity.id, [])])
                shape['religion'].extend([r.religion for r in religions.get(polity.id, [])])
                shape['alternate_religion_genus'].extend([arg.alternate_religion_genus for arg in alternate_religion_genuses.get(polity.id, [])])
                shape['alternate_religion_family'].extend([arf.alternate_religion_family for arf in alternate_religion_families.get(polity.id, [])])
                shape['alternate_religion'].extend([ar.alternate_religion for ar in alternate_religions.get(polity.id, [])])

                # Get the years for the variables for the polity
                shape['linguistic_family_dict'].update({lf.linguistic_family: [lf.year_from, lf.year_to] for lf in linguistic_families.get(polity.id, [])})
                shape['language_genus_dict'].update({lg.language_genus: [lg.year_from, lg.year_to] for lg in language_genuses.get(polity.id, [])})
                shape['language_dict'].update({l.language: [l.year_from, l.year_to] for l in languages.get(polity.id, [])})
                shape['religious_tradition_dict'].update({rt.religious_tradition: [rt.year_from, rt.year_to] for rt in religious_traditions.get(polity.id, [])})
                shape['religion_genus_dict'].update({rg.religion_genus: [rg.year_from, rg.year_to] for rg in religion_genuses.get(polity.id, [])})
                shape['religion_family_dict'].update({rf.religion_family: [rf.year_from, rf.year_to] for rf in religion_families.get(polity.id, [])})
                shape['religion_dict'].update({r.religion: [r.year_from, r.year_to] for r in religions.get(polity.id, [])})
                shape['alternate_religion_genus_dict'].update({arg.alternate_religion_genus: [arg.year_from, arg.year_to] for arg in alternate_religion_genuses.get(polity.id, [])})
                shape['alternate_religion_family_dict'].update({arf.alternate_religion_family: [arf.year_from, arf.year_to] for arf in alternate_religion_families.get(polity.id, [])})
                shape['alternate_religion_dict'].update({ar.alternate_religion: [ar.year_from, ar.year_to] for ar in alternate_religions.get(polity.id, [])})

        # If no linguistic family, language genus, or language was found, append 'Uncoded'
        polity = polities.get(shape['seshat_id'])
        if polity:
            if not shape['linguistic_family']:
                shape['linguistic_family'].append('Uncoded')
            if not shape['language_genus']:
                shape['language_genus'].append('Uncoded')
            if not shape['language']:
                shape['language'].append('Uncoded')
            if not shape['religious_tradition']:
                shape['religious_tradition'].append('Uncoded')
            if not shape['religion_genus']:
                shape['religion_genus'].append('Uncoded')
            if not shape['religion_family']:
                shape['religion_family'].append('Uncoded')
            if not shape['religion']:
                shape['religion'].append('Uncoded')
            if not shape['alternate_religion_genus']:
                shape['alternate_religion_genus'].append('Uncoded')
            if not shape['alternate_religion_family']:
                shape['alternate_religion_family'].append('Uncoded')
            if not shape['alternate_religion']:
                shape['alternate_religion'].append('Uncoded')
        else:
            if not shape['linguistic_family']:
                shape['linguistic_family'].append('No Seshat page')
            if not shape['language_genus']:
                shape['language_genus'].append('No Seshat page')
            if not shape['language']:
                shape['language'].append('No Seshat page') 
            if not shape['religious_tradition']:
                shape['religious_tradition'].append('No Seshat page')
            if not shape['religion_genus']:
                shape['religion_genus'].append('No Seshat page')
            if not shape['religion_family']:
                shape['religion_family'].append('No Seshat page')
            if not shape['religion']:
                shape['religion'].append('No Seshat page')
            if not shape['alternate_religion_genus']:
                shape['alternate_religion_genus'].append('No Seshat page')
            if not shape['alternate_religion_family']:
                shape['alternate_religion_family'].append('No Seshat page')
            if not shape['alternate_religion']:
                shape['alternate_religion'].append('No Seshat page') 

    return shapes, variables

# Get all the variables used in the map view
app_map = {
    'sc': 'Social Complexity Variables',
    'wf': 'Warfare Variables (Military Technologies)',
    # 'rt': 'Religion Tolerance',     # TODO: Implemented but temporarily restricted. Uncomment when ready.
    # 'general': 'General Variables', # TODO: Partially implmented and hardcoded in assign_categorical_variables_to_shapes.
}

# Get sorted lists of choices for each categorical variable
if 'test' not in sys.argv:  # Skip this if running tests as it breaks GitHub actions
    POLITY_RELIGIOUS_TRADITION_CHOICES = list(set(Polity_religious_tradition.objects.values_list('religious_tradition', flat=True).distinct()))
else:
    POLITY_RELIGIOUS_TRADITION_CHOICES = ['test', 'choices']
categorical_variables = {
    'linguistic_family': sorted([x[0] for x in POLITY_LINGUISTIC_FAMILY_CHOICES]),
    'language_genus': sorted([x[0] for x in POLITY_LANGUAGE_GENUS_CHOICES]),
    'language': sorted([x[0] for x in POLITY_LANGUAGE_CHOICES]),
    'religious_tradition': sorted([x for x in POLITY_RELIGIOUS_TRADITION_CHOICES]),
    'religion_genus': sorted([x[0] for x in POLITY_RELIGION_GENUS_CHOICES]),
    'religion_family': sorted([x[0] for x in POLITY_RELIGION_FAMILY_CHOICES]),
    'religion': sorted([x[0] for x in POLITY_RELIGION_CHOICES]),
    'alternate_religion_genus': sorted([x[0] for x in POLITY_RELIGION_GENUS_CHOICES]),
    'alternate_religion_family': sorted([x[0] for x in POLITY_RELIGION_FAMILY_CHOICES]),
    'alternate_religion': sorted([x[0] for x in POLITY_RELIGION_CHOICES]),
}

def random_polity_shape(from_selection=True):
    """
    This function is used to get a pseudo-random polity for the map_view_initial and map_view_initial views to display.
    It selects a polity with a large area and which has a seshat_id.

    If from_selection is true, choose a polity from a pre-approved list.
    TODO: if the loading time of map_view_initial becomes sufficiently fast, we could set from_selection to False.

    Returns:
        tuple: A tuple containing the start year and seshat_id.
    """
    if from_selection:  # These are polities where loading all the shapes for their start year is fast
        selected_polities = [
            'sy_umayyad_cal',
            'it_roman_principate',
            'de_empire_3',
            'tr_east_roman_emp',
            'ir_seleucid_emp',
            'iq_abbasid_cal_1',
            'ir_seljuk_sultanate',
            'cn_five_dyn',
            'fr_carolingian_emp_1',
            'cn_tang_dyn_1',
            'ir_sassanid_emp_2',
        ]
        # Select a random polity from the list
        seshat_id = random.choice(selected_polities)
        shape = Cliopatria.objects.filter(seshat_id=seshat_id).first()
    else:
        max_id = Cliopatria.objects.filter(seshat_id__isnull=False).aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            shape = Cliopatria.objects.filter(seshat_id__isnull=False, id=pk).first()
            if shape:
                if shape.seshat_id and shape.area > 600000:  # Big empires only
                    break
    return shape.start_year, shape.seshat_id

def common_map_view_content(content):
    """
    Set of functions that update content and run in each map view function.

    Args:
        content (dict): The content for the polity shapes.

    Returns:
        dict: The updated content for the polity shapes.
    """

    # Add in the present/absent variables to view for the shapes
    content['shapes'], content['variables'] = assign_variables_to_shapes(content['shapes'], app_map)

    # Add in the categorical variables to view for the shapes
    content['shapes'], content['variables'] = assign_categorical_variables_to_shapes(content['shapes'], content['variables'])

    # Load the capital cities for polities that have them
    content['all_capitals_info'] = get_all_polity_capitals()
    
    # Add categorical variable choices to content for dropdown selection
    content['categorical_variables'] = categorical_variables

    # Set the initial polity to highlight
    content['world_map_initial_polity'] = world_map_initial_polity

    # Set the last year in history we ever want to display, which will be used to determine when we should say "present"
    content['last_history_year'] = content['latest_year']  # Set this to the latest year in the data or a value of choice

    return content

def dummy_map_view_content(content):
    """
    Dummy version of common_map_view_content that adds blank dicts.

    Args:
        content (dict): The content for the polity shapes.

    Returns:
        dict: The updated content for the polity shapes.
    """
    content['all_capitals_info'] = {}
    content['categorical_variables'] = {}
    content['variables'] = {}

    # Set the initial polity to highlight
    content['world_map_initial_polity'] = world_map_initial_polity

    # Set the last year in history we ever want to display, which will be used to determine when we should say "present"
    content['last_history_year'] = content['latest_year']  # Set this to the latest year in the data or a value of choice
    return content

# World map default settings
world_map_initial_displayed_year = 117
world_map_initial_polity = 'it_roman_principate'

import time

def map_view_initial(request):
    global world_map_initial_displayed_year, world_map_initial_polity
    """
    This view is used to display a map with polities plotted on it. The initial
    view just loads a polity with a seshat_id picked at random and sets the
    display year to that polity start year.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    
    # Start a timer to measure the time taken to load the page
    start_time = time.time()

    # Check if 'year' parameter is different from the world_map_initial_displayed_year or not present then redirect
    if 'year' in request.GET:
        if request.GET['year'] != str(world_map_initial_displayed_year):
            return redirect('{}?year={}'.format(request.path, world_map_initial_displayed_year))
    else:
        # Select a random polity for the initial view
        if 'test' not in sys.argv:
            world_map_initial_displayed_year, world_map_initial_polity = random_polity_shape()
        return redirect('{}?year={}'.format(request.path, world_map_initial_displayed_year))

    content = get_polity_shape_content(displayed_year=world_map_initial_displayed_year)

    content = dummy_map_view_content(content)

    # Print the time taken to load the page
    print(f"Time taken to load the initial view: {time.time() - start_time} seconds")

    return render(request,
                  'core/world_map.html',
                  content
                  )

def map_view_all(request):
    """
    This view is used to display a map with polities plotted on it. The view
    loads all polities for the range of years.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The HTTP response with serialized JSON.
    """

    # Start a timer to measure the time taken to load the page
    start_time = time.time()

    content = get_polity_shape_content()

    content = dummy_map_view_content(content)

    # Print the time taken to load the page
    print(f"Time taken to load the all view: {time.time() - start_time} seconds")

    return JsonResponse(content)

def map_view_all_with_vars(request):
    """
    This view is used to display a map with polities plotted on it. The view
    loads all polities for the range of years with added variables for each polity shape.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The HTTP response with serialized JSON.
    """

    # Start a timer to measure the time taken to load the page
    start_time = time.time()

    content = get_polity_shape_content(geometries=False)

    content = common_map_view_content(content)

    # Print the time taken to load the page
    print(f"Time taken to load the vars view: {time.time() - start_time} seconds")

    return JsonResponse(content)

def provinces_and_countries_view(request):
    """
    This view is used to get the provinces and countries for the map.

    Args:
        request: The request object.

    Returns:
        JsonResponse: The HTTP response with serialized JSON.
    """
    provinces = get_provinces()
    countries = get_provinces(selected_base_map_gadm='country')

    content = {
        'provinces': provinces,
        'countries': countries,
    }

    return JsonResponse(content)
######################

def update_seshat_comment_part_view(request, pk):
    """
    View to update a SeshatCommentPart instance.

    Note:
        This view can handle POST and GET requests.

    Args:
        request: The request object.
        pk: The primary key of the SeshatCommentPart instance.

    Returns:
        HttpResponse: The HTTP response.
    """
    comment_part = SeshatCommentPart.objects.get(id=pk)
    parent_comment_id = comment_part.comment.id
    subcomment_order = comment_part.comment_order

    parent_comment_part = SeshatComment.objects.get(id=parent_comment_id)

    init_data={}
    if request.method == 'POST':
        form = SeshatCommentPartForm2(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            comment_order = form.cleaned_data['comment_order']
            user_logged_in = request.user

            # Update the SeshatCommentPart instance
            comment_part.comment_part_text = comment_text
            comment_part.comment_order = comment_order
            comment_part.save()

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except Seshat_Expert.DoesNotExist:
                seshat_expert_instance = None

            comment_part.comment_curator = seshat_expert_instance 
            comment_part.save()
            # Process the formset
            # comment_part.comment_citations_plus
            #print("YOOOOOOOOOOO", comment_part.comment_citations_plus.count())
            if comment_part.citations_count <= 2:
                reference_formset = ReferenceFormSet2(request.POST, prefix='refs')
            elif comment_part.citations_count <= 4:
                reference_formset = ReferenceFormSet5(request.POST, prefix='refs')
            else:
                reference_formset = ReferenceFormSet10(request.POST, prefix='refs')

            if reference_formset.is_valid():
                #print("ALOOOOOOOOOOOOOOOOOOO: ", len(reference_formset))
                to_be_added = []
                to_be_deleted_later = []
                for reference_form in reference_formset:
                    if reference_form.is_valid():
                        try:
                            reference = reference_form.cleaned_data['ref']
                            #print(f"aaaaaaaaaaaaaaaaaa: {reference}")
                            page_from = reference_form.cleaned_data['page_from']
                            page_to = reference_form.cleaned_data['page_to']
                            to_be_deleted = reference_form.cleaned_data['DELETE']
                            parent_pars_inserted = reference_form.cleaned_data['parent_pars']

                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to)
                                )
                            elif page_from:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_from)
                                )
                            elif page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_to),
                                    page_to=int(page_to)
                                )
                            else:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=None,
                                    page_to=None
                                )

                            # Associate the Citation with the SeshatCommentPart
                            if to_be_deleted:
                                #comment_part.comment_citations.remove(citation)
                                to_be_deleted_later.append((citation, parent_pars_inserted))
                            else:
                                #comment_part.comment_citations.add(citation)
                                to_be_added.append((citation, parent_pars_inserted))
                        except:
                            #print("OOOPSI", reference_form)
                            pass  # Handle the exception as per your requirement
                        #print("OOzzzzzzzzzzzzzzOPSI", reference_form)
                #comment_part.comment_citations.clear()
                #comment_part.comment_citations.add(*to_be_added)

                comment_part.comment_citations_plus.clear()
                #comment_part.comment_citations_plus.add(*to_be_added)

                for item in to_be_added:
                    # Query for an existing row based on citation and SeshatCommentPart
                    scp_through_ctn, created = ScpThroughCtn.objects.get_or_create(
                        seshatcommentpart=comment_part,
                        citation=item[0],
                        defaults={'parent_paragraphs': item[1]}  # Set defaults including parent_paragraphs
                    )

                    # If the row already exists, update its parent_paragraphs
                    if not created:
                        scp_through_ctn.parent_paragraphs = item[1]
                        scp_through_ctn.save()
                    # ScpThroughCtn.objects.get_or_create(
                    #     seshatcommentpart = comment_part,
                    #     citation=item[0],
                    #     parent_paragraphs=item[1],
                    # )

            #return redirect('seshat-index')  # Redirect to a success page
            #return reverse('seshatcomment-update', args=209)  
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            return redirect(reverse('seshatcomment-update', kwargs={'pk': parent_comment_id}))

            #return render(request('seshatcomment-update', kwargs={'pk': pk})# Redirect to a success page

    else:
        # form = SeshatCommentPartForm2(instance=comment_part)
        # ReferenceFormSet = inlineformset_factory(SeshatCommentPart, Reference, form=ReferenceWithPageForm, extra=1, can_delete=True)
        # reference_formset = ReferenceFormSet(instance=comment_part, prefix='refs')
        
        all_present_citations = comment_part.comment_citations_plus.all()
        all_present_citations_plus = ScpThroughCtn.objects.filter(seshatcommentpart_id= comment_part.id)

        initial_data= []
        if all_present_citations_plus:
            for a_cit_through in all_present_citations_plus:
                my_id = a_cit_through.citation.ref.id
                my_pf = a_cit_through.citation.page_from
                my_pt = a_cit_through.citation.page_to
                my_pp = a_cit_through.parent_paragraphs
                initial_data.append(
                    {'ref': Reference.objects.get(id=my_id), 'page_from': my_pf, 'page_to': my_pt, 'parent_pars': my_pp},
                )
        if all_present_citations:
            for a_cit in all_present_citations:
                my_id = a_cit.ref.id
                my_pf = a_cit.page_from
                my_pt = a_cit.page_to
                my_pp = ""
                initial_data.append(
                    {'ref': Reference.objects.get(id=my_id), 'page_from': my_pf, 'page_to': my_pt, 'parent_pars': my_pp},
                )

        #my_reference = Reference.objects.get(id=32734)
        # initial_data = [
        #     {'ref': my_reference, 'page_from': 1, 'page_to': 10},
        #     {'ref': my_reference, 'page_from': 11, 'page_to': 20},
        # ]
        if len(initial_data) <= 2:
            init_data = ReferenceFormSet2(prefix='refs', initial=initial_data)
            form = SeshatCommentPartForm2(initial={
            'comment_text': comment_part.comment_part_text,
            'comment_order': comment_part.comment_order,})
        elif len(initial_data) <= 4:
            init_data = ReferenceFormSet5(prefix='refs', initial=initial_data)
            form = SeshatCommentPartForm5(initial={
            'comment_text': comment_part.comment_part_text,
            'comment_order': comment_part.comment_order,})
        else:
            init_data = ReferenceFormSet10(prefix='refs', initial=initial_data)
            form = SeshatCommentPartForm10(initial={
            'comment_text': comment_part.comment_part_text,
            'comment_order': comment_part.comment_order,})


    #print(formset)
    return render(request, 'core/seshatcomments/seshatcommentpart_update2.html', {'form': form, 'formset': init_data, 'comm_num':pk, 'comm_part_display': comment_part, 'parent_comment': parent_comment_part, 'subcom_order': subcomment_order,})


#########################

@login_required
def create_a_comment_with_a_subcomment_new(request, app_name, model_name, instance_id):
    """
    Create a Comment and assign it to a model instance.

    Note:
        This view has the login_required decorator to ensure that only
        logged-in users can access it.

    Args:
        request: The request object.
        app_name: The name of the app containing the model.
        model_name: The name of the model.
        instance_id: The id of the model instance.

    Returns:
        HttpResponse: The HTTP response.
    """
    # Get the model class dynamically using the provided model_name
    #model_class = globals()[model_name]
    if model_name == 'general':
        model_class = apps.get_model(app_label=app_name, model_name='polity_' + model_name)
    else:
        model_class = apps.get_model(app_label=app_name, model_name= model_name)
    
    # Check if the model class exists
    if model_class is None:
        # Handle the case where the model class does not exist
        return HttpResponse("Model not found", status=404)

    # Get the instance of the model using the provided instance_id
    model_instance = get_object_or_404(model_class, id=instance_id)

    # Create a new comment instance and save it to the database
    if model_instance.comment and model_instance.comment.id > 1:
        comment_instance = model_instance.comment
    else:
        comment_instance = SeshatComment.objects.create(text='a new_comment_text new approach')
    user_logged_in = request.user
    
    # Get the Seshat_Expert instance associated with the user
    try:
        seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
    except Seshat_Expert.DoesNotExist:
        seshat_expert_instance = None

    # Create the subcomment instance and save it to the database
    subcomment_instance = SeshatCommentPart.objects.create(
        comment_part_text='A subdescription text placeholder (to be edited) using the new approach',
        comment=comment_instance,
        comment_curator=seshat_expert_instance,
        comment_order=1
    )

    # Assign the comment to the model instance
    model_instance.comment = comment_instance
    model_instance.save()

    # Redirect to the appropriate page
    # You may need to define the URL pattern for the model detail view
    # and replace 'model-detail' with the actual name of your detail view
    #return redirect('model-detail', pk=model_instance.id)
    return redirect('seshatcomment-update', pk=comment_instance.id)

from .forms import SeshatCommentPartForm2_UPGRADE, ReferenceFormSet2_UPGRADE

@login_required
def create_a_comment_with_a_subcomment_newer(request, app_name, model_name, instance_id):
    """
    Create the first chunk of a new comment and assign it to a model instance and a seshat comment.
    Get the data on citations and do the appropriate assignments there as well. 
    """
    if model_name == 'general':
        model_class = apps.get_model(app_label=app_name, model_name='polity_' + model_name)
    else:
        model_class = apps.get_model(app_label=app_name, model_name=model_name)
    
    if model_class is None:
        return HttpResponse("Model not found", status=404)

    model_instance = get_object_or_404(model_class, id=instance_id)

    if request.method == 'POST':
        form = SeshatCommentPartForm2_UPGRADE(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            comment_order = form.cleaned_data['comment_order']
            references_formset = form.cleaned_data['references_formset']

            ######################## Process the formset
            references_formset = ReferenceFormSet2_UPGRADE(request.POST, prefix='refs')
            if references_formset.is_valid():
                #print("ALOOOOOOOOOOOOOOOOOOO: ", len(references_formset))
                to_be_added = []
                to_be_deleted_later = []
                for reference_form in references_formset:
                    if reference_form.is_valid():
                        try:
                            reference = reference_form.cleaned_data['ref']
                            page_from = reference_form.cleaned_data['page_from']
                            page_to = reference_form.cleaned_data['page_to']
                            to_be_deleted = reference_form.cleaned_data['DELETE']
                            parent_pars_inserted = reference_form.cleaned_data['parent_pars']


                            # Get or create the Citation instance
                            if page_from and page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to)
                                )
                            elif page_from:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_from)
                                )
                            elif page_to:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_to),
                                    page_to=int(page_to)
                                )
                                #print(page_from, "AAAAAAAAAAAAAAAAAAAAND ", page_to)
                            else:
                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=None,
                                    page_to=None
                                )

                            # Associate the Citation with the SeshatCommentPart
                            if to_be_deleted:
                                #comment_part.comment_citations.remove(citation)
                                to_be_deleted_later.append((citation, parent_pars_inserted))
                            else:
                                #comment_part.comment_citations.add((citation, parent_pars_inserted))
                                to_be_added.append((citation, parent_pars_inserted))
                        except:
                            pass  # Handle the exception as per your requirement
                # seshat_comment_part.comment_citations.clear()
                # seshat_comment_part.comment_citations.add(*to_be_added)
                seshat_comment_part.comment_citations_plus.clear()
                #seshat_comment_part.comment_citations_plus.add(*to_be_added)

                for item in to_be_added:
                    # Query for an existing row based on citation and SeshatCommentPart
                    scp_through_ctn, created = ScpThroughCtn.objects.get_or_create(
                        seshatcommentpart=seshat_comment_part,
                        citation=item[0],
                        defaults={'parent_paragraphs': item[1]}  # Set defaults including parent_paragraphs
                    )

                    # If the row already exists, update its parent_paragraphs
                    if not created:
                        scp_through_ctn.parent_paragraphs = item[1]
                        scp_through_ctn.save()
            return redirect(reverse('seshatcomment-update', kwargs={'pk': com_id}))
        #########################################







            if model_instance.comment and model_instance.comment.id > 1:
                comment_instance = model_instance.comment
            else:
                comment_instance = SeshatComment.objects.create(text='New comment')

            user_logged_in = request.user
            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except Seshat_Expert.DoesNotExist:
                seshat_expert_instance = None

            subcomment_instance = SeshatCommentPart.objects.create(
                comment_part_text=comment_text,
                comment=comment_instance,
                comment_curator=seshat_expert_instance,
                comment_order=comment_order
            )

            for reference_form in references_formset:
                ref = reference_form.cleaned_data['ref']
                page_from = reference_form.cleaned_data['page_from']
                page_to = reference_form.cleaned_data['page_to']
                parent_pars = reference_form.cleaned_data['parent_pars']
                # Process and save each reference

            model_instance.comment = comment_instance
            model_instance.save()

            return redirect('seshatcomment-update', pk=comment_instance.id)
    else:
        form = SeshatCommentPartForm2_UPGRADE()

    #return redirect('seshatcomment-update', pk=comment_instance.id)
    return render(request, 'core/seshatcomments/your_template.html', {'form': form})


@login_required
@permission_required('core.add_seshatprivatecommentpart')
def create_a_private_comment_with_a_private_subcomment_new(request, app_name, model_name, instance_id):
    """
    Create a PrivateComment and assign it to a model instance.

    Note:
        This view is only accessible to users with the 'add_seshatprivatecommentpart' permission.

    Args:
        request: The request object.
        app_name: The name of the app containing the model.
        model_name: The name of the model.
        instance_id: The id of the model instance.

    Returns:
        HttpResponse: The HTTP response.
    """
    # Get the model class dynamically using the provided model_name
    #model_class = globals()[model_name]
    #if app_name == 'general':
    #    model_class = apps.get_model(app_label=app_name, model_name='polity_' + #model_name)
    #else:
    model_class = apps.get_model(app_label=app_name, model_name= model_name)
    
    # Check if the model class exists
    if model_class is None:
        # Handle the case where the model class does not exist
        return HttpResponse("Model not found", status=404)

    # Get the instance of the model using the provided instance_id
    model_instance = get_object_or_404(model_class, id=instance_id)

    # Create a new comment instance and save it to the database
    if str(app_name) == 'core':
        if model_instance.private_comment_n and model_instance.private_comment_n.id > 1:
            private_comment_instance = model_instance.private_comment_n
        else:
            private_comment_instance = SeshatPrivateComment.objects.create(text='a new_private_comment_text new approach for polity')
    else:
        if model_instance.private_comment and model_instance.private_comment.id > 1:
            private_comment_instance = model_instance.private_comment
        else:
            private_comment_instance = SeshatPrivateComment.objects.create(text='a new_private_comment_text new approach')
    user_logged_in = request.user
    
    # Get the Seshat_Expert instance associated with the user
    # try:
    #     seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
    # except Seshat_Expert.DoesNotExist:
    #     seshat_expert_instance = None

    # Create the subcomment instance and save it to the database
    # subprivatecomment_instance = SeshatPrivateCommentPart.objects.create(
    #     private_comment_part_text='A subdescription text placeholder (to be edited) using the new approach',
    #     private_comment=private_comment_instance,
    #     private_comment_owner=seshat_expert_instance,
    #     created_date=datetime.datetime.now()
    # )

    # Assign the comment to the model instance
    if app_name == 'core':
        model_instance.private_comment_n = private_comment_instance
    else:
        model_instance.private_comment = private_comment_instance

    model_instance.save()

    # Redirect to the appropriate page
    # You may need to define the URL pattern for the model detail view
    # and replace 'model-detail' with the actual name of your detail view
    #return redirect('model-detail', pk=model_instance.id)
    return redirect('seshatprivatecomment-update', pk=private_comment_instance.id)

class SeshatPrivateCommentUpdate(PermissionRequiredMixin, UpdateView, FormMixin):
    """
    View to update a SeshatPrivateComment instance.
    """
    model = SeshatPrivateComment
    form_class = SeshatPrivateCommentForm
    template_name = "core/seshatcomments/seshatprivatecomment_update.html"
    permission_required = 'core.add_seshatprivatecommentpart'


    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.

        Args:
            request: The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponse: The HTTP response.
        """
        form = self.form()
        if form.is_valid():
            #print('hereeeeeeeeeeeee')
            self.object = self.get_object()  # Assuming you have this method to get the object
            new_experts = form.cleaned_data['private_comment_reader']
            self.object.private_comment_reader.add(*new_experts)  # Add the new experts to the ManyToMany field
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    #def get_queryset(self):
        
    def get_another_form(self, request, *args, **kwargs):
        """
        Return the data from another form in the SeshatPrivateCommentPartForm.

        Args:
            request: The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            SeshatPrivateCommentPartForm: The form instance.
        """
        # Implement this method to return the specific instance of another_form
        # For example:
        #return self.kwargs['another_form']
        #print("7777777777777777777")
        return SeshatPrivateCommentPartForm(request.POST, request.another_form)

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
        my_apps=['core', 'rt', 'general', 'sc', 'wf', 'crisisdb']
        my_app_models = {name: apps.all_models[name] for name in my_apps}

        #context['my_app_models'] = my_app_models
        abc = []

        for myapp, mymodels in my_app_models.items():
            if myapp != 'core':
                for mm, mymodel in mymodels.items():
                    if '_citations' not in mm and '_curator' not in mm and not mm.startswith('us_') and mymodel.objects.filter(private_comment=self.object.id):
                        my_instance = mymodel.objects.get(private_comment=self.object.id)
                        my_polity = my_instance.polity
                        my_polity_id = my_instance.polity.id
                        try:
                            my_var_name = my_instance.clean_name_spaced()
                        except:
                            my_var_name = my_instance.name

                        my_value = my_instance.show_value
                        my_desc = my_instance.description
                        my_year_from = my_instance.year_from
                        my_year_to = my_instance.year_to
                        my_tag = my_instance.get_tag_display()


                        abc.append({
                            'my_polity': my_polity,
                            'my_value': my_value,
                            'my_year_from': my_year_from,
                            'my_year_to': my_year_to,
                            'my_tag': my_tag,
                            'my_var_name': my_var_name,
                            'my_polity_id': my_polity_id,
                            'my_description': my_desc,
                        })
            else:
                for mm, mymodel in mymodels.items():
                    if mm == 'polity' and mymodel.objects.filter(private_comment_n=self.object.id):
                        my_instance = mymodel.objects.get(private_comment_n=self.object.id)
                        my_polity = my_instance
                        my_polity_id = my_instance.id
                        my_start_year = my_instance.start_year
                        my_end_year = my_instance.end_year

                        abc.append({
                            'my_polity': my_polity,
                            'my_polity_id': my_polity_id,
                            'commented_pols_link': True,
                            'start_year': my_start_year,
                            'end_year': my_end_year,

                        })

        # for model_name in related_models:
        #     print(model_name)
        #     related_objects = getattr(self.object, model_name)
        #     if related_objects:
        #         context['related_objects'] = related_objects
        #         break
        
        context['my_app_models'] = abc

        context['another_form'] = SeshatPrivateCommentPartForm()

        #print("111111111111111111111111111")

        return context

#############################
def seshatcomment_create_view(request):
    """
    View to create a SeshatComment instance.

    Note:
        This view can handle POST and GET requests.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    if request.method == 'POST':
        form = SeshatCommentForm2(request.POST)
        if form.is_valid():
            user_logged_in = request.user

            comment_instance = SeshatComment.objects.create(text='a new_comment_text')

            try:
                seshat_expert_instance = Seshat_Expert.objects.get(user=user_logged_in)
            except Seshat_Expert.DoesNotExist:
                seshat_expert_instance = None

            # Create the SeshatCommentPart instance
            comment_part = SeshatComment.objects.create(
                text='initial text',
            )

            # Process the formset
            comment_formset = CommentPartFormSet(request.POST, prefix='commentpart')

            for i, subcomment_form in enumerate(comment_formset):
                if subcomment_form.is_valid():
                    comment_text = subcomment_form.cleaned_data['comment_text']
                    comment_order = subcomment_form.cleaned_data['comment_order']
                    user_logged_in = request.user

                    # Create the SeshatCommentPart instance
                    comment_part = SeshatCommentPart.objects.create(
                        comment=comment_instance,
                        comment_part_text=comment_text,
                        comment_order=comment_order,
                        comment_curator=seshat_expert_instance 
                    )

                    # Process the formset
                    reference_formset = ReferenceFormSet(request.POST, prefix='refs')

                    for i, reference_form in enumerate(reference_formset):
                        if reference_form.is_valid():
                            #print("+++++++xxaaaaaaaaaxx+++++++")
                            try:
                                reference = reference_form.cleaned_data['ref']
                                page_from = reference_form.cleaned_data['page_from']
                                page_to = reference_form.cleaned_data['page_to']

                                citation, created = Citation.objects.get_or_create(
                                    ref=reference,
                                    page_from=int(page_from),
                                    page_to=int(page_to)
                                )


                                # Associate the Citation with the SeshatCommentPart
                                comment_part.comment_citations.add(citation)
                                #print("+++++++xxxx+++++++")
                                #print("I am here::::::", citation)
                            except:
                                print("OOOPsi")
                        else:
                            print(f'Form errors: {reference_form.errors}')


            return redirect('seshat-index')  # Redirect to a success page

    else:
        form = SeshatCommentForm2()

    return render(request, 'core/seshatcomments/seshatcomment_create.html', {'form': form})



def search_view(request):
    """
    View to search for a polity.

    Note:
        This view can handle GET requests.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    search_term = request.GET.get('search', '')
    if search_term:
        try:
            polity = Polity.objects.filter(name__icontains=search_term).first()
            if polity:
                return redirect('polity-detail-main', pk=polity.pk)
            else:
                # No polity found
                return redirect('seshat-index')  # Redirect to home or any other page
        except Polity.DoesNotExist:
            # Handle the case where no polity matches the search term
            pass
    return redirect('seshat-index')  # Redirect to home or any other page if no search term is provided or no match is found

def search_suggestions(request):
    """
    View to get search suggestions for a polity.

    Note:
        This view can handle GET requests.

    Args:
        request: The request object.

    Returns:
        HttpResponse: The HTTP response.
    """
    search_term = request.GET.get('search', '')
    polities = Polity.objects.filter(
        Q(name__icontains=search_term) | 
        Q(long_name__icontains=search_term) |
        Q(new_name__icontains=search_term)
    ).order_by('start_year')  # Limit to 5 suggestions [:5]
    return render(request, 'core/partials/_search_suggestions.html', {'polities': polities})


def xxyyzz(request, com_id):
    if request.method == 'POST':
        my_items = request.POST.getlist('selected_items')
        for item in my_items:
            my_sp = SeshatPrivateCommentPart.objects.get(id=int(item))
            my_sp.is_done= True
            my_sp.save()
        return redirect(reverse('seshatprivatecomment-update', kwargs={'pk': com_id}))

    return redirect(reverse('seshatprivatecomment-update', kwargs={'pk': com_id}))

def cliopatria(request):
    return render(request, 'core/cliopatria.html')