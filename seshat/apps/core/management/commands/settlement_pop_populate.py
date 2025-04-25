from django.core.management.base import BaseCommand
from seshat.apps.core.models import HabitationSite, CurrentCountry, ScientificResource
from seshat.apps.stlm.models import Settlement_population

# Replace 'your_app' with the name of the app where your models are defined
from seshat.apps.stlm.settlements_population_1 import ultimate_dics_list

ultimate_dics_list_2 = [
    {
        'city': 'A Coruna', 'alt_name': 'Coruna, A Coruña', 'country_name': 'Spain', 'my_file': 'chandler.csv',
        'lat': '43.362344', 'lon': '-8.41154', 'certainty': 1, 'pop': {1900: 43000}
    },
    {
        'city': 'Aachen', 'alt_name': 'Aix-la-Chapelle', 'country_name': 'Germany',
        'lat': '50.77664', 'lon': '6.08342', 'certainty': 1, 'my_file': 'chandler66666.csv',
        'pop': {1300: 32000, 1500: 38000, 1600: 36000, 1700: 35000, 1750: 39000,
                2799: 33699, 1800: 33000, 1849: 50533, 1850: 49000, 1852: 48688, 1900: 335000}
    },
    {
        'city': 'Aalborg', 'alt_name': 'No_alt_name', 'country_name': 'Denmark',
        'lat': '57.048', 'lon': '9.9187', 'my_file': 'chandler.csv', 'certainty': 1, 'pop': {1900: 34000}
    }
]

class Command(BaseCommand):
    help = "Import habitation site data with population history"

    def handle(self, *args, **kwargs):
        for entry in ultimate_dics_list:
            city = entry['city']
            alt_name = entry['alt_name'] if entry['alt_name'] != 'No_alt_name' else None

            my_resource, rs_created = ScientificResource.objects.get_or_create(title=entry['my_file'][:-4], file_name=entry['my_file'])
            country = entry['country_name'].strip()

            print(f'----{entry["country_name"]}-----')
            try:
                my_country_obj = CurrentCountry.objects.get(name=country)
            except:
                print(f'------------------------{entry["country_name"]}---------------------------------')
                my_country_obj = CurrentCountry.objects.get(name='Iran')
                
            lat = entry['lat']
            lon = entry['lon']
            populations = entry.get('pop', {})

            # Create or get the HabitationSite
            settlement, already_created = HabitationSite.objects.get_or_create(
                name=city,
                current_country_obj_id=my_country_obj.id,
                defaults={
                    'alternative_names': alt_name,
                    'latitude': lat,
                    'longitude': lon
                }
            )

            if not already_created:
                # Update fields if needed
                print("OLD CITY: ",city )
                if alt_name and settlement.alternative_names and  alt_name == settlement.alternative_names:
                    settlement.alternative_names = settlement.alternative_names
                elif alt_name and settlement.alternative_names:
                    settlement.alternative_names = settlement.alternative_names +', ' + alt_name
                elif alt_name:
                    settlement.alternative_names = alt_name
                elif settlement.alternative_names:
                    settlement.alternative_names = settlement.alternative_names
                else:
                    settlement.alternative_names = None
                settlement.current_country_obj_id = my_country_obj.id
                settlement.latitude = lat
                settlement.longitude = lon
                settlement.save()
            else:
                print("NEEEEEEEEEEEEEEW CITY: ",city )

            # Populate Settlement_population
            for year, pop in populations.items():
                Settlement_population.objects.get_or_create(
                    settlement=settlement,  # Assumes a ForeignKey from Settlement_population to HabitationSite
                    year_from=year,
                    year_to=year,
                    population_from=pop,
                    population_to=pop,
                    general_ref_id=my_resource.id,
                    tag=entry['certainty'],
                )
            self.stdout.write(self.style.SUCCESS(f"Added: {city}"))

        self.stdout.write(self.style.SUCCESS('Successfully imported habitation and population data.'))
