from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

import csv

from ....utils import (
    get_date,
    get_api_results,
)

from ...constants import (
    TAGS_DIC,
)
from ...utils import get_vars_with_hierarchy, get_all_polity_names


class Playground(View):
    # TODO: Do we not want this view to be restricted access?

    def get(self, request):
        context = self.get_context_data()

        return render(request, "crisisdb/playground.html", context)

    def get_context_data(self):
        context = {
            "allpols": get_all_polity_names(),
            "all_var_hiers": get_vars_with_hierarchy(),
        }

        return context


# TODO: rewrite as a class-based view (RedirectView)
def download_view(request):
    """
    Download the data from the playground.

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse: HTTP response with CSV file
    """
    # Read the data from the previous from
    # Make sure you collect all the data from seshat_api
    # Sort it out and spit it out
    # Small task: download what we have on seshat_api

    # Extract POST data
    checked_pols = request.POST.getlist("selected_pols")
    checked_vars = request.POST.getlist("selected_vars")
    delimiter = request.POST.get("SeparatorRadioOptions")

    # Call utility functions
    date = get_date()
    all_my_data = get_api_results()

    new_checked_vars = [
        f"crisisdb_{item.lower()}_related" for item in checked_vars
    ]

    if delimiter == "comma":
        delimiter = ","
    elif delimiter == "bar":
        delimiter = "|"
    else:
        # Bad selection of Separator
        delimiter = ","  # Set default
        pass

    # Create a response object with CSV content type
    response = HttpResponse(content_type="text/csv")

    filename = f"CrisisDB_data_{request.user}_{date}.csv"
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    writer = csv.writer(response, delimiter=delimiter)

    # The top row is the same as Equinox, so no need to read data from user
    # input for that
    writer.writerow(
        [
            "polity",
            "variable_name",
            "variable_sub_name",
            "value",
            "year_from",
            "year_to",
            "certainty",
            "references",
            "notes",
        ]
    )

    for polity_with_everything in all_my_data:
        if polity_with_everything["name"] not in checked_pols:
            continue

        for variable in new_checked_vars:
            if variable not in polity_with_everything.keys():
                continue

            # We can get into a list of dictionaries
            for var_instance in polity_with_everything[variable]:
                all_used_keys = []
                for active_key in var_instance.keys():
                    if (
                        active_key
                        not in ["year_from", "year_to", "tag"] + all_used_keys
                    ):
                        equinox_rows = [
                            polity_with_everything["name"],
                            variable[:-8],
                            active_key,
                            var_instance[active_key],
                            var_instance["year_from"],
                            var_instance["year_to"],
                            TAGS_DIC[var_instance["tag"]],
                        ]

                        writer.writerow(equinox_rows)

    return response
