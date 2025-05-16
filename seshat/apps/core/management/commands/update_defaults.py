from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import transaction
from django.core.exceptions import FieldDoesNotExist

class Command(BaseCommand):
    help = "Update 'name' field to its default value for all models in the 'general' app, if the field exists."

    def handle(self, *args, **options):
        my_db_sections = ['general', 'sc', 'wf', 'ec', 'rt',]
        for my_section in my_db_sections:
            my_models = apps.get_app_config(my_section).get_models()

            for model in my_models:
                model_name = model.__name__
                try:
                    self.update_name_field(model)
                except FieldDoesNotExist:
                    self.stderr.write(f"❌ {model_name} has no 'name' field. Skipping.")
                except Exception as e:
                    self.stderr.write(f"❌ Error processing {model_name}: {e}")

    def update_name_field(self, model):
        model_name = model.__name__
        name_field = model._meta.get_field('name')
        default_value = name_field.get_default()
        if not default_value:
            print(f"❌❌❌❌❌❌ No Default Value for: {model_name}.")

        updated_count = 0
        with transaction.atomic():
            for instance in model.objects.all():
                if default_value and instance.name != default_value:
                    instance.name = default_value
                    instance.save()
                    updated_count += 1

        self.stdout.write(f"✅ {model_name}: Updated {updated_count} instances with default 'name' = '{default_value}'.")
