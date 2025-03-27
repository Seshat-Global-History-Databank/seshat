import os
from django.core.management.base import BaseCommand
import pandas as pd
from seshat.apps.core.models import Capital
from seshat.apps.general.models import City_duration

class Command(BaseCommand):
    help = 'Populates the database with Cities'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the csv file')

    def handle(self, *args, **options):

        # Ensure the file exists and has the suffix "_seshat_processed.geojson"
        chandlerV2_path = options['csv_file']
        if not os.path.exists(chandlerV2_path):
            self.stdout.write(self.style.ERROR(f"File {chandlerV2_path} does not exist"))
            return

        # Load the chandlerV2 cities dataset with csv
        self.stdout.write(self.style.SUCCESS(f"Loading chandlerV2 dataset from {chandlerV2_path}..."))
        chandlerV2_data = pd.read_csv(chandlerV2_path)
        self.stdout.write(self.style.SUCCESS(f"Successfully loaded chandlerV2 dataset from {chandlerV2_path}"))

        # Process the chandlerV2 cities to be ready for the City model
        self.stdout.write(self.style.SUCCESS('Processing chandlerV2 cities dataset...'))

        # Get the data from CSV
        chandlerV2_data = pd.read_csv(chandlerV2_path, encoding='Windows-1252')

        # Select the columns we need to use directly
        chandlerV2_seshat_ready = chandlerV2_data[['City', 'OtherName', 'Country', 'Latitude', 'Longitude']]

        # Create the 'url_on_the_map' column
        chandlerV2_seshat_ready['url_on_the_map'] = 'https://www.google.com/maps/search/?api=1&query=' + chandlerV2_seshat_ready['Latitude'].astype(str) + ',' + chandlerV2_seshat_ready['Longitude'].astype(str)

        # Get the year_from based on the earliest record of a population estimate in the dataset
        # TODO: Update the code to populate the City_population table, which does not exist yet. Column values are population estimates for particular years.
        def extract_year_from(row):
            for column in row.index:
                if 'BC' in column or 'AD' in column:
                    if not pd.isna(row[column]):
                        col_sign, col_val = column.split('_')
                        return 0 - int(col_val) if col_sign == 'BC' else int(col_val)
            return None  # Default if no valid year is found
        # Apply the function to each row
        chandlerV2_seshat_ready['year_from'] = chandlerV2_data.apply(extract_year_from, axis=1)

        # Iterate through the data and create City and City_duration instances (City model currently named Capital for legacy reasons)
        self.stdout.write(self.style.SUCCESS('Adding chandlerV2_data to the database...'))
        for index, row in chandlerV2_seshat_ready.iterrows():
            # Check there isn't already a City instance with the same name
            if Capital.objects.filter(name=row['City']).exists():
                self.stdout.write(self.style.WARNING(f"City instance for {row['City']} already exists"))
            else:
                # Create the City instance
                Capital.objects.create(
                    name=row['City'],
                    alternative_names=row['OtherName'],
                    current_country=row['Country'],
                    latitude=row['Latitude'],
                    longitude=row['Longitude'],
                    url_on_the_map=row['url_on_the_map']
                )
                self.stdout.write(self.style.SUCCESS(f"Created City instance for {row['City']}"))

                # Create the City_duration instance
                City_duration.objects.create(
                    city=Capital.objects.get(name=row['City']),
                    year_from=row['year_from']
                )
                self.stdout.write(self.style.SUCCESS(f"Created City_duration instance for {row['City']}"))