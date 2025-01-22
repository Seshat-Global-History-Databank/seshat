import os
import json
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from django.db import connection
from seshat.apps.core.models import Cliopatria


class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('geojson_file', type=str, help='Path to the geojson file')

    def handle(self, *args, **options):

        # Ensure the file exists and has the suffix "_seshat_processed.geojson"
        cliopatria_geojson_path = options['geojson_file']
        if not os.path.exists(cliopatria_geojson_path):
            self.stdout.write(self.style.ERROR(f"File {cliopatria_geojson_path} does not exist"))
            return
        if not cliopatria_geojson_path.endswith('_seshat_processed.geojson'):
            self.stdout.write(self.style.ERROR(f"File {cliopatria_geojson_path} should have the suffix '_seshat_processed.geojson'"))
            self.stdout.write(self.style.ERROR(f"Please run the cliopatria/convert_data.py script first"))
            return

        # Load the Cliopatria shape dataset with JSON
        self.stdout.write(self.style.SUCCESS(f"Loading Cliopatria shape dataset from {cliopatria_geojson_path}..."))
        with open(cliopatria_geojson_path) as f:
            cliopatria_data = json.load(f)
        self.stdout.write(self.style.SUCCESS(f"Successfully loaded Cliopatria shape dataset from {cliopatria_geojson_path}"))

        # Clear the Cliopatria table
        self.stdout.write(self.style.SUCCESS('Clearing Cliopatria table...'))
        Cliopatria.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cliopatria table cleared'))

        # Iterate through the data and create Cliopatria instances
        self.stdout.write(self.style.SUCCESS('Adding data to the database...'))
        for feature in cliopatria_data['features']:
            properties = feature['properties']
            self.stdout.write(self.style.SUCCESS(f"Creating Cliopatria instance for {properties['DisplayName']} ({properties['FromYear']} - {properties['ToYear']})"))
            
            # Save geom and convert Polygon to MultiPolygon if necessary
            geom = GEOSGeometry(json.dumps(feature['geometry']))
            if geom.geom_type == 'Polygon':
                geom = MultiPolygon(geom)

            Cliopatria.objects.create(
                geom=geom,
                name=properties['DisplayName'],
                wikipedia_name=properties['Wikipedia'],
                seshat_id=properties['SeshatID'],
                area=properties['Area'],
                start_year=properties['FromYear'],
                end_year=properties['ToYear'],
                polity_start_year=properties['PolityStartYear'],
                polity_end_year=properties['PolityEndYear'],
                colour=properties['Color'],
                components=properties['Components'],
                member_of=properties['MemberOf']
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully imported all data from {cliopatria_geojson_path}"))

        ###########################################################
        ### Adjust the tolerance param of ST_Simplify as needed ###
        ###########################################################

        self.stdout.write(self.style.SUCCESS('Adding simplified geometries for faster loading...'))

        ## Use this code if you want to simplify the geometries
        # with connection.cursor() as cursor:
        #     cursor.execute("""
        #         UPDATE core_cliopatria 
        #         SET simplified_geom = ST_Simplify(geom, 0.07);
        #     """)

        ## Use this code if you don't need to simplify the geometries
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE core_cliopatria
                SET simplified_geom = geom;
            """)
        self.stdout.write(self.style.SUCCESS('Simplified geometries added'))

