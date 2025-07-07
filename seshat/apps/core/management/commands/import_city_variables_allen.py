from django.core.management.base import BaseCommand
from seshat.apps.core.models import HabitationSite
from seshat.apps.stlm.models import (
    Number_of_ziggurats, Number_of_palaces, Number_of_temples,
    Defensive_wall, Tablet, Seal_indicator
)

from seshat.apps.stlm.allen_data_sample import full_dic

MODEL_MAP = {
    "number_of_ziggurats": Number_of_ziggurats,
    "number_of_palaces": Number_of_palaces,
    "number_of_temples": Number_of_temples,
    "defensive_wall": Defensive_wall,
    "tablet": Tablet,
    "seal_indicator": Seal_indicator,
}


class Command(BaseCommand):
    help = "Import city variable data into the database"

    def handle(self, *args, **options):
        for var_name, records in full_dic.items():
            Model = MODEL_MAP.get(var_name)
            if not Model:
                self.stdout.write(self.style.WARNING(f"Model not found for var_name: {var_name}"))
                continue

            for entry in records:
                try:
                    city = HabitationSite.objects.get(name=entry["name"])
                except HabitationSite.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"City not found: {entry['name']}"))
                    continue

                obj = Model.objects.create(
                    settlement=city,
                    year_from=entry["period_start"],
                    year_to=entry["period_end"],
                    general_ref_id = 4,
                )

                # Set coded value
                if hasattr(obj, "count"):
                    obj.count = entry["coded_val"]
                elif hasattr(obj, "present"):
                    obj.present = bool(entry["coded_val"])
                
                obj.save()
                self.stdout.write(self.style.SUCCESS(f"Created {var_name} for {city.name} ({entry['period_start']}–{entry['period_end']})"))

        self.stdout.write(self.style.SUCCESS("Import completed."))
