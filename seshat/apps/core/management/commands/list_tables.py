from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = "List all database tables associated with the 'general' app models."

    def handle(self, *args, **kwargs):
        # Get all models in the 'general' app
        general_models = apps.get_app_config('general').get_models()

        # Extract table names from models
        general_tables = [model._meta.db_table for model in general_models]

        # Print the tables
        self.stdout.write("Tables for models in 'general' app:")
        for table in general_tables:
            self.stdout.write(f"'{table}', ")
