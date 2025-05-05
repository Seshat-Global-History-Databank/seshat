from django.core.management.base import BaseCommand
from django.db import connection
from django.apps import apps

from seshat.apps.core.models import Seshat_Expert


from seshat.apps.general.models import Polity_expert, Polity_original_name, Polity_alternative_name


# GENERAL_TABLES = [
#     'general_polity_research_assistant', 
#     'general_polity_original_name', 
#     'general_polity_alternative_name', 
#     'general_polity_duration', 
#     'general_polity_peak_years', 
#     'general_polity_degree_of_centralization', 
#     'general_polity_suprapolity_relations', 
#     'general_polity_utm_zone', 
#     'general_polity_capital', 
#     'general_polity_language', 
#     'general_polity_linguistic_family', 
#     'general_polity_language_genus', 
#     'general_polity_religion_genus', 
#     'general_polity_religion_family', 
#     'general_polity_religion', 
#     'general_polity_relationship_to_preceding_entity', 
#     'general_polity_preceding_entity', 
#     'general_polity_succeeding_entity', 
#     'general_polity_supracultural_entity', 
#     'general_polity_scale_of_supracultural_interaction', 
#     'general_polity_alternate_religion_genus', 
#     'general_polity_alternate_religion_family', 
#     'general_polity_alternate_religion', 
#     'general_polity_expert', 
#     'general_polity_editor', 
#     'general_polity_religious_tradition', 
# ]
class Command(BaseCommand):
    help = "Update curators table with coded records based on polity experts"

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching polities and experts...")

        # Fetch polity_id and expert mapping
        polity_experts = Polity_expert.objects.all().values_list('polity_id', 'expert_id')
        print(polity_experts)
        for item in polity_experts:
            try:
                main_objects = Polity_alternative_name.objects.filter(polity_id=item[0])  # Replace with your filter criteria
            
            except:
                print("BAD item: ", item)
                continue
            if main_objects:
                new_curator = Seshat_Expert.objects.get(id=item[1])  # Replace with your filter criteria

                # Add the new curator to the ManyToManyField for all cases
                for main_object in main_objects:
                    main_object.curator.add(new_curator)

                    # Save the main object (optional since ManyToManyField updates are saved immediately)
                    main_object.save()
                    print("Yes")


        self.stdout.write("Update completed.")


class Command(BaseCommand):
    help = "Update curators table with coded records based on polity experts for all general app models"

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching polities and experts...")
        
        # Fetch polity_id and expert mapping
        polity_experts = Polity_expert.objects.all().values_list('polity_id', 'expert_id')
        print("Polity Experts Mapping: ", polity_experts)

        # Get all models in the 'general' app
        general_models = apps.get_app_config('general').get_models()

        for model in general_models:
            if hasattr(model, 'curator') and hasattr(model, 'polity_id'):  # Ensure the model has required fields
                self.stdout.write(f"Processing model: {model.__name__}")

                for item in polity_experts:
                    try:
                        # Filter by polity_id
                        main_objects = model.objects.filter(polity_id=item[0])

                    except model.DoesNotExist:
                        self.stdout.write(f"No matching object found in {model.__name__} for polity_id {item[0]}")
                        continue

                    # Get the expert
                    try:
                        new_curator = Seshat_Expert.objects.get(id=item[1])
                    except Seshat_Expert.DoesNotExist:
                        self.stdout.write(f"No expert found with ID {item[1]}")
                        continue
                    # Add the new curator to the ManyToManyField for all cases

                    for main_object in main_objects:
                        main_object.curator.add(new_curator)

                        # Save the main object (optional since ManyToManyField updates are saved immediately)
                        main_object.save()
                        print("Yes")
                    self.stdout.write(f"Added curator {new_curator} to {model.__name__} with polity_id {item[0]}")

        self.stdout.write("Update completed.")
        