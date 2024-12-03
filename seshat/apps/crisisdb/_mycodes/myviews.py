"""
Note: This file is currently not in use.
"""

# Generated Imports
from ..models import Population, Land_taxes_collected, Land_yield, Total_tax, Total_economic_output, Total_revenue, Diding_taxes, Salt_tax, Tariff_and_transit, Misc_incomes, Total_expenditure, Balance, Lijin, Maritime_custom, Other_incomes, Revenue_official, Revenue_real

from ..forms import PopulationForm, Land_taxes_collectedForm, Land_yieldForm, Total_taxForm, Total_economic_outputForm, Total_revenueForm, Diding_taxesForm, Salt_taxForm, Tariff_and_transitForm, Misc_incomesForm, Total_expenditureForm, BalanceForm, LijinForm, Maritime_customForm, Other_incomesForm, Revenue_officialForm, Revenue_realForm

# END OF Generated Imports


# Here is where we add all the generated views:


class PopulationCreate(PermissionRequiredMixin, CreateView):
    model = Population
    form_class = PopulationForm
    template_name = "crisisdb/population/population_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('population-create')

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
        context["mysection"] = "No Section Provided"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Total Population"

        return context


class PopulationUpdate(PermissionRequiredMixin, UpdateView):
    model = Population
    form_class = PopulationForm
    template_name = "crisisdb/population/population.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["mysection"] = "No Section Provided"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Total Population"

        return context


class PopulationDelete(PermissionRequiredMixin, DeleteView):
    model = Population
    success_url = reverse_lazy('populations')
    permission_required = 'catalog.can_mark_returned'


class PopulationListView(generic.ListView):
    model = Population
    template_name = "crisisdb/population/population_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        return reverse('populations')

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
        context["mysection"] = "No Section Provided"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Total Population"

        return context


class PopulationDetailView(generic.DetailView):
    model = Population
    template_name = "crisisdb/population/population_detail.html"


@permission_required('admin.can_add_log_entry')
def population_download(request):
    items = Population.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="populations.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_population', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_population, ])

    return response


class Land_taxes_collectedCreate(PermissionRequiredMixin, CreateView):
    model = Land_taxes_collected
    form_class = Land_taxes_collectedForm
    template_name = "crisisdb/land_taxes_collected/land_taxes_collected_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('land_taxes_collected-create')

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
        context["myvar"] = "Land Taxes Collected"

        return context


class Land_taxes_collectedUpdate(PermissionRequiredMixin, UpdateView):
    model = Land_taxes_collected
    form_class = Land_taxes_collectedForm
    template_name = "crisisdb/land_taxes_collected/land_taxes_collected.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Land Taxes Collected"

        return context


class Land_taxes_collectedDelete(PermissionRequiredMixin, DeleteView):
    model = Land_taxes_collected
    success_url = reverse_lazy('land_taxes_collecteds')
    permission_required = 'catalog.can_mark_returned'


class Land_taxes_collectedListView(generic.ListView):
    model = Land_taxes_collected
    template_name = "crisisdb/land_taxes_collected/land_taxes_collected_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('land_taxes_collecteds')

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
        context["myvar"] = "Land Taxes Collected"

        return context


class Land_taxes_collectedDetailView(generic.DetailView):
    model = Land_taxes_collected
    template_name = "crisisdb/land_taxes_collected/land_taxes_collected_detail.html"


@permission_required('admin.can_add_log_entry')
def land_taxes_collected_download(request):
    items = Land_taxes_collected.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="land_taxes_collecteds.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'land_taxes_collected', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.land_taxes_collected, ])

    return response


class Land_yieldCreate(PermissionRequiredMixin, CreateView):
    model = Land_yield
    form_class = Land_yieldForm
    template_name = "crisisdb/land_yield/land_yield_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('land_yield-create')

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
        context["myvar"] = "Land Yield"

        return context


class Land_yieldUpdate(PermissionRequiredMixin, UpdateView):
    model = Land_yield
    form_class = Land_yieldForm
    template_name = "crisisdb/land_yield/land_yield.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Land Yield"

        return context


class Land_yieldDelete(PermissionRequiredMixin, DeleteView):
    model = Land_yield
    success_url = reverse_lazy('land_yields')
    permission_required = 'catalog.can_mark_returned'


class Land_yieldListView(generic.ListView):
    model = Land_yield
    template_name = "crisisdb/land_yield/land_yield_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('land_yields')

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
        context["myvar"] = "Land Yield"

        return context


class Land_yieldDetailView(generic.DetailView):
    model = Land_yield
    template_name = "crisisdb/land_yield/land_yield_detail.html"


@permission_required('admin.can_add_log_entry')
def land_yield_download(request):
    items = Land_yield.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="land_yields.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'land_yield', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.land_yield, ])

    return response


class Total_taxCreate(PermissionRequiredMixin, CreateView):
    model = Total_tax
    form_class = Total_taxForm
    template_name = "crisisdb/total_tax/total_tax_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('total_tax-create')

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
        context["myvar"] = "Total Amount of Taxes Collected"

        return context


class Total_taxUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_tax
    form_class = Total_taxForm
    template_name = "crisisdb/total_tax/total_tax.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Total Amount of Taxes Collected"

        return context


class Total_taxDelete(PermissionRequiredMixin, DeleteView):
    model = Total_tax
    success_url = reverse_lazy('total_taxs')
    permission_required = 'catalog.can_mark_returned'


class Total_taxListView(generic.ListView):
    model = Total_tax
    template_name = "crisisdb/total_tax/total_tax_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('total_taxs')

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
        context["myvar"] = "Total Amount of Taxes Collected"

        return context


class Total_taxDetailView(generic.DetailView):
    model = Total_tax
    template_name = "crisisdb/total_tax/total_tax_detail.html"


@permission_required('admin.can_add_log_entry')
def total_tax_download(request):
    items = Total_tax.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_taxs.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_amount_of_taxes_collected', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_amount_of_taxes_collected, ])

    return response


class Total_economic_outputCreate(PermissionRequiredMixin, CreateView):
    model = Total_economic_output
    form_class = Total_economic_outputForm
    template_name = "crisisdb/total_economic_output/total_economic_output_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('total_economic_output-create')

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
        context["myvar"] = "Total Economic Output"

        return context


class Total_economic_outputUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_economic_output
    form_class = Total_economic_outputForm
    template_name = "crisisdb/total_economic_output/total_economic_output.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Total Economic Output"

        return context


class Total_economic_outputDelete(PermissionRequiredMixin, DeleteView):
    model = Total_economic_output
    success_url = reverse_lazy('total_economic_outputs')
    permission_required = 'catalog.can_mark_returned'


class Total_economic_outputListView(generic.ListView):
    model = Total_economic_output
    template_name = "crisisdb/total_economic_output/total_economic_output_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('total_economic_outputs')

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
        context["myvar"] = "Total Economic Output"

        return context


class Total_economic_outputDetailView(generic.DetailView):
    model = Total_economic_output
    template_name = "crisisdb/total_economic_output/total_economic_output_detail.html"


@permission_required('admin.can_add_log_entry')
def total_economic_output_download(request):
    items = Total_economic_output.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_economic_outputs.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_economic_output', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_economic_output, ])

    return response


class Total_revenueCreate(PermissionRequiredMixin, CreateView):
    model = Total_revenue
    form_class = Total_revenueForm
    template_name = "crisisdb/total_revenue/total_revenue_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('total_revenue-create')

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
        context["mysection"] = "No Section Provided"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Total Revenue"

        return context


class Total_revenueUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_revenue
    form_class = Total_revenueForm
    template_name = "crisisdb/total_revenue/total_revenue.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["mysection"] = "No Section Provided"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Total Revenue"

        return context


class Total_revenueDelete(PermissionRequiredMixin, DeleteView):
    model = Total_revenue
    success_url = reverse_lazy('total_revenues')
    permission_required = 'catalog.can_mark_returned'


class Total_revenueListView(generic.ListView):
    model = Total_revenue
    template_name = "crisisdb/total_revenue/total_revenue_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('total_revenues')

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
        context["mysection"] = "No Section Provided"
        context["mysubsection"] = "No Subsection Provided"
        context["myvar"] = "Total Revenue"

        return context


class Total_revenueDetailView(generic.DetailView):
    model = Total_revenue
    template_name = "crisisdb/total_revenue/total_revenue_detail.html"


@permission_required('admin.can_add_log_entry')
def total_revenue_download(request):
    items = Total_revenue.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_revenues.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_revenue', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_revenue, ])

    return response


class Diding_taxesCreate(PermissionRequiredMixin, CreateView):
    model = Diding_taxes
    form_class = Diding_taxesForm
    template_name = "crisisdb/diding_taxes/diding_taxes_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('diding_taxes-create')

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
        context["myvar"] = "Total Revenue"

        return context


class Diding_taxesUpdate(PermissionRequiredMixin, UpdateView):
    model = Diding_taxes
    form_class = Diding_taxesForm
    template_name = "crisisdb/diding_taxes/diding_taxes.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Total Revenue"

        return context


class Diding_taxesDelete(PermissionRequiredMixin, DeleteView):
    model = Diding_taxes
    success_url = reverse_lazy('diding_taxess')
    permission_required = 'catalog.can_mark_returned'


class Diding_taxesListView(generic.ListView):
    model = Diding_taxes
    template_name = "crisisdb/diding_taxes/diding_taxes_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('diding_taxess')

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
        context["myvar"] = "Total Revenue"

        return context


class Diding_taxesDetailView(generic.DetailView):
    model = Diding_taxes
    template_name = "crisisdb/diding_taxes/diding_taxes_detail.html"


@permission_required('admin.can_add_log_entry')
def diding_taxes_download(request):
    items = Diding_taxes.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="diding_taxess.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_revenue', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_revenue, ])

    return response


class Salt_taxCreate(PermissionRequiredMixin, CreateView):
    model = Salt_tax
    form_class = Salt_taxForm
    template_name = "crisisdb/salt_tax/salt_tax_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('salt_tax-create')

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
        context["myvar"] = "Salt Tax"

        return context


class Salt_taxUpdate(PermissionRequiredMixin, UpdateView):
    model = Salt_tax
    form_class = Salt_taxForm
    template_name = "crisisdb/salt_tax/salt_tax.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Salt Tax"

        return context


class Salt_taxDelete(PermissionRequiredMixin, DeleteView):
    model = Salt_tax
    success_url = reverse_lazy('salt_taxs')
    permission_required = 'catalog.can_mark_returned'


class Salt_taxListView(generic.ListView):
    model = Salt_tax
    template_name = "crisisdb/salt_tax/salt_tax_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('salt_taxs')

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
        context["myvar"] = "Salt Tax"

        return context


class Salt_taxDetailView(generic.DetailView):
    model = Salt_tax
    template_name = "crisisdb/salt_tax/salt_tax_detail.html"


@permission_required('admin.can_add_log_entry')
def salt_tax_download(request):
    items = Salt_tax.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="salt_taxs.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'salt_tax', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.salt_tax, ])

    return response


class Tariff_and_transitCreate(PermissionRequiredMixin, CreateView):
    model = Tariff_and_transit
    form_class = Tariff_and_transitForm
    template_name = "crisisdb/tariff_and_transit/tariff_and_transit_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('tariff_and_transit-create')

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
        context["myvar"] = "Tariff and Transit"

        return context


class Tariff_and_transitUpdate(PermissionRequiredMixin, UpdateView):
    model = Tariff_and_transit
    form_class = Tariff_and_transitForm
    template_name = "crisisdb/tariff_and_transit/tariff_and_transit.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Tariff and Transit"

        return context


class Tariff_and_transitDelete(PermissionRequiredMixin, DeleteView):
    model = Tariff_and_transit
    success_url = reverse_lazy('tariff_and_transits')
    permission_required = 'catalog.can_mark_returned'


class Tariff_and_transitListView(generic.ListView):
    model = Tariff_and_transit
    template_name = "crisisdb/tariff_and_transit/tariff_and_transit_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('tariff_and_transits')

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
        context["myvar"] = "Tariff and Transit"

        return context


class Tariff_and_transitDetailView(generic.DetailView):
    model = Tariff_and_transit
    template_name = "crisisdb/tariff_and_transit/tariff_and_transit_detail.html"


@permission_required('admin.can_add_log_entry')
def tariff_and_transit_download(request):
    items = Tariff_and_transit.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tariff_and_transits.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'tariff_and_transit', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.tariff_and_ransit, ])

    return response


class Misc_incomesCreate(PermissionRequiredMixin, CreateView):
    model = Misc_incomes
    form_class = Misc_incomesForm
    template_name = "crisisdb/misc_incomes/misc_incomes_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('misc_incomes-create')

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
        context["myvar"] = "Misc Incomes"

        return context


class Misc_incomesUpdate(PermissionRequiredMixin, UpdateView):
    model = Misc_incomes
    form_class = Misc_incomesForm
    template_name = "crisisdb/misc_incomes/misc_incomes.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Misc Incomes"

        return context


class Misc_incomesDelete(PermissionRequiredMixin, DeleteView):
    model = Misc_incomes
    success_url = reverse_lazy('misc_incomess')
    permission_required = 'catalog.can_mark_returned'


class Misc_incomesListView(generic.ListView):
    model = Misc_incomes
    template_name = "crisisdb/misc_incomes/misc_incomes_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('misc_incomess')

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
        context["myvar"] = "Misc Incomes"

        return context


class Misc_incomesDetailView(generic.DetailView):
    model = Misc_incomes
    template_name = "crisisdb/misc_incomes/misc_incomes_detail.html"


@permission_required('admin.can_add_log_entry')
def misc_incomes_download(request):
    items = Misc_incomes.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="misc_incomess.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'misc_incomes', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.misc_incomes, ])

    return response


class Total_expenditureCreate(PermissionRequiredMixin, CreateView):
    model = Total_expenditure
    form_class = Total_expenditureForm
    template_name = "crisisdb/total_expenditure/total_expenditure_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('total_expenditure-create')

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
        context["myvar"] = "Total Expenditure"

        return context


class Total_expenditureUpdate(PermissionRequiredMixin, UpdateView):
    model = Total_expenditure
    form_class = Total_expenditureForm
    template_name = "crisisdb/total_expenditure/total_expenditure.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Total Expenditure"

        return context


class Total_expenditureDelete(PermissionRequiredMixin, DeleteView):
    model = Total_expenditure
    success_url = reverse_lazy('total_expenditures')
    permission_required = 'catalog.can_mark_returned'


class Total_expenditureListView(generic.ListView):
    model = Total_expenditure
    template_name = "crisisdb/total_expenditure/total_expenditure_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('total_expenditures')

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
        context["myvar"] = "Total Expenditure"

        return context


class Total_expenditureDetailView(generic.DetailView):
    model = Total_expenditure
    template_name = "crisisdb/total_expenditure/total_expenditure_detail.html"


@permission_required('admin.can_add_log_entry')
def total_expenditure_download(request):
    items = Total_expenditure.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="total_expenditures.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'total_expenditure', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.total_expenditure, ])

    return response


class BalanceCreate(PermissionRequiredMixin, CreateView):
    model = Balance
    form_class = BalanceForm
    template_name = "crisisdb/balance/balance_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('balance-create')

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
        context["myvar"] = "Balance"

        return context


class BalanceUpdate(PermissionRequiredMixin, UpdateView):
    model = Balance
    form_class = BalanceForm
    template_name = "crisisdb/balance/balance.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Balance"

        return context


class BalanceDelete(PermissionRequiredMixin, DeleteView):
    model = Balance
    success_url = reverse_lazy('balances')
    permission_required = 'catalog.can_mark_returned'


class BalanceListView(generic.ListView):
    model = Balance
    template_name = "crisisdb/balance/balance_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('balances')

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
        context["myvar"] = "Balance"

        return context


class BalanceDetailView(generic.DetailView):
    model = Balance
    template_name = "crisisdb/balance/balance_detail.html"


@permission_required('admin.can_add_log_entry')
def balance_download(request):
    items = Balance.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="balances.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'balance', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.balance, ])

    return response


class LijinCreate(PermissionRequiredMixin, CreateView):
    model = Lijin
    form_class = LijinForm
    template_name = "crisisdb/lijin/lijin_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('lijin-create')

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
        context["myvar"] = "Lijin"

        return context


class LijinUpdate(PermissionRequiredMixin, UpdateView):
    model = Lijin
    form_class = LijinForm
    template_name = "crisisdb/lijin/lijin.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Lijin"

        return context


class LijinDelete(PermissionRequiredMixin, DeleteView):
    model = Lijin
    success_url = reverse_lazy('lijins')
    permission_required = 'catalog.can_mark_returned'


class LijinListView(generic.ListView):
    model = Lijin
    template_name = "crisisdb/lijin/lijin_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('lijins')

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
        context["myvar"] = "Lijin"

        return context


class LijinDetailView(generic.DetailView):
    model = Lijin
    template_name = "crisisdb/lijin/lijin_detail.html"


@permission_required('admin.can_add_log_entry')
def lijin_download(request):
    items = Lijin.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lijins.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'lijin', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.lijin, ])

    return response


class Maritime_customCreate(PermissionRequiredMixin, CreateView):
    model = Maritime_custom
    form_class = Maritime_customForm
    template_name = "crisisdb/maritime_custom/maritime_custom_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('maritime_custom-create')

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
        context["myvar"] = "Maritime Custom"

        return context


class Maritime_customUpdate(PermissionRequiredMixin, UpdateView):
    model = Maritime_custom
    form_class = Maritime_customForm
    template_name = "crisisdb/maritime_custom/maritime_custom.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Maritime Custom"

        return context


class Maritime_customDelete(PermissionRequiredMixin, DeleteView):
    model = Maritime_custom
    success_url = reverse_lazy('maritime_customs')
    permission_required = 'catalog.can_mark_returned'


class Maritime_customListView(generic.ListView):
    model = Maritime_custom
    template_name = "crisisdb/maritime_custom/maritime_custom_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('maritime_customs')

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
        context["myvar"] = "Maritime Custom"

        return context


class Maritime_customDetailView(generic.DetailView):
    model = Maritime_custom
    template_name = "crisisdb/maritime_custom/maritime_custom_detail.html"


@permission_required('admin.can_add_log_entry')
def maritime_custom_download(request):
    items = Maritime_custom.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="maritime_customs.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'maritime_custom', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.maritime_custom, ])

    return response


class Other_incomesCreate(PermissionRequiredMixin, CreateView):
    model = Other_incomes
    form_class = Other_incomesForm
    template_name = "crisisdb/other_incomes/other_incomes_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('other_incomes-create')

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
        context["myvar"] = "Other Incomes"

        return context


class Other_incomesUpdate(PermissionRequiredMixin, UpdateView):
    model = Other_incomes
    form_class = Other_incomesForm
    template_name = "crisisdb/other_incomes/other_incomes.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Other Incomes"

        return context


class Other_incomesDelete(PermissionRequiredMixin, DeleteView):
    model = Other_incomes
    success_url = reverse_lazy('other_incomess')
    permission_required = 'catalog.can_mark_returned'


class Other_incomesListView(generic.ListView):
    model = Other_incomes
    template_name = "crisisdb/other_incomes/other_incomes_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('other_incomess')

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
        context["myvar"] = "Other Incomes"

        return context


class Other_incomesDetailView(generic.DetailView):
    model = Other_incomes
    template_name = "crisisdb/other_incomes/other_incomes_detail.html"


@permission_required('admin.can_add_log_entry')
def other_incomes_download(request):
    items = Other_incomes.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="other_incomess.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'other_incomes', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.other_incomes, ])

    return response


class Revenue_officialCreate(PermissionRequiredMixin, CreateView):
    model = Revenue_official
    form_class = Revenue_officialForm
    template_name = "crisisdb/revenue_official/revenue_official_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('revenue_official-create')

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
        context["myvar"] = "Revenue Official"

        return context


class Revenue_officialUpdate(PermissionRequiredMixin, UpdateView):
    model = Revenue_official
    form_class = Revenue_officialForm
    template_name = "crisisdb/revenue_official/revenue_official.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Revenue Official"

        return context


class Revenue_officialDelete(PermissionRequiredMixin, DeleteView):
    model = Revenue_official
    success_url = reverse_lazy('revenue_officials')
    permission_required = 'catalog.can_mark_returned'


class Revenue_officialListView(generic.ListView):
    model = Revenue_official
    template_name = "crisisdb/revenue_official/revenue_official_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('revenue_officials')

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
        context["myvar"] = "Revenue Official"

        return context


class Revenue_officialDetailView(generic.DetailView):
    model = Revenue_official
    template_name = "crisisdb/revenue_official/revenue_official_detail.html"


@permission_required('admin.can_add_log_entry')
def revenue_official_download(request):
    items = Revenue_official.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="revenue_officials.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'revenue_official', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.revenue_official, ])

    return response


class Revenue_realCreate(PermissionRequiredMixin, CreateView):
    model = Revenue_real
    form_class = Revenue_realForm
    template_name = "crisisdb/revenue_real/revenue_real_form.html"
    permission_required = 'catalog.can_mark_returned'

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('revenue_real-create')

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
        context["myvar"] = "Revenue Real"

        return context


class Revenue_realUpdate(PermissionRequiredMixin, UpdateView):
    model = Revenue_real
    form_class = Revenue_realForm
    template_name = "crisisdb/revenue_real/revenue_real.html"
    permission_required = 'catalog.can_mark_returned'

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
        context["myvar"] = "Revenue Real"

        return context


class Revenue_realDelete(PermissionRequiredMixin, DeleteView):
    model = Revenue_real
    success_url = reverse_lazy('revenue_reals')
    permission_required = 'catalog.can_mark_returned'


class Revenue_realListView(generic.ListView):
    model = Revenue_real
    template_name = "crisisdb/revenue_real/revenue_real_list.html"
    paginate_by = 5

    def get_absolute_url(self):
        """
        Get the absolute URL of the view.

        Returns:
            str: The absolute URL of the view.
        """
        return reverse('revenue_reals')

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
        context["myvar"] = "Revenue Real"

        return context


class Revenue_realDetailView(generic.DetailView):
    model = Revenue_real
    template_name = "crisisdb/revenue_real/revenue_real_detail.html"


@permission_required('admin.can_add_log_entry')
def revenue_real_download(request):
    items = Revenue_real.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="revenue_reals.csv"'

    writer = csv.writer(response, delimiter='|')
    writer.writerow(['year_from', 'year_to',
                     'polity', 'revenue_real', ])

    for obj in items:
        writer.writerow([obj.year_from, obj.year_to,
                         obj.polity, obj.revenue_real, ])

    return response


vars_dic = {
    'Population': {'model': Population, 'list': PopulationListView, 'create': PopulationCreate}, 'Land_taxes_collected': {'model': Land_taxes_collected, 'list': Land_taxes_collectedListView, 'create': Land_taxes_collectedCreate},
    'Land_yield': {'model': Land_yield, 'list': Land_yieldListView, 'create': Land_yieldCreate},
    'Total_tax': {'model': Total_tax, 'list': Total_taxListView, 'create': Total_taxCreate}, 'Total_economic_output': {'model': Total_economic_output, 'list': Total_economic_outputListView, 'create': Total_economic_outputCreate}, 'Total_revenue': {'model': Total_revenue, 'list': Total_revenueListView, 'create': Total_revenueCreate}, 'Diding_taxes': {'model': Diding_taxes, 'list': Diding_taxesListView, 'create': Diding_taxesCreate}, 'Salt_tax': {'model': Salt_tax, 'list': Salt_taxListView, 'create': Salt_taxCreate}, 'Tariff_and_transit': {'model': Tariff_and_transit, 'list': Tariff_and_transitListView, 'create': Tariff_and_transitCreate}, 'Misc_incomes': {'model': Misc_incomes, 'list': Misc_incomesListView, 'create': Misc_incomesCreate}, 'Total_expenditure': {'model': Total_expenditure, 'list': Total_expenditureListView, 'create': Total_expenditureCreate}, 'Balance': {'model': Balance, 'list': BalanceListView, 'create': BalanceCreate}, 'Lijin': {'model': Lijin, 'list': LijinListView, 'create': LijinCreate}, 'Maritime_custom': {'model': Maritime_custom, 'list': Maritime_customListView, 'create': Maritime_customCreate}, 'Other_incomes': {'model': Other_incomes, 'list': Other_incomesListView, 'create': Other_incomesCreate}, 'Revenue_official': {'model': Revenue_official, 'list': Revenue_officialListView, 'create': Revenue_officialCreate}, 'Revenue_real': {'model': Revenue_real, 'list': Revenue_realListView, 'create': Revenue_realCreate}
}
