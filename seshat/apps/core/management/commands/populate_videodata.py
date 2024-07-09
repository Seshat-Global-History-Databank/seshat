import os
import json
import fnmatch
from distinctipy import get_colors, get_hex
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from django.db import connection
from seshat.apps.core.models import VideoShapefile

class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Directory containing geojson files')

    def handle(self, *args, **options):
        dir = options['dir']

        # Clear the VideoShapefile table
        self.stdout.write(self.style.SUCCESS('Clearing VideoShapefile table...'))
        VideoShapefile.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('VideoShapefile table cleared'))

        # Set of all polities, for generating colour mapping
        all_polities = set()
        # Dict of all the polities found and the shapes they include
        polity_shapes = {}
        # Iterate over files in the directory
        for filename in os.listdir(dir):
            if filename.endswith('.geojson'):
                file_path = os.path.join(dir, filename)

                # Read and parse the GeoJSON file
                with open(file_path, 'r') as geojson_file:
                    geojson_data = json.load(geojson_file)

                # Extract data and create VideoShapefile instances
                for feature in geojson_data['features']:
                    properties = feature['properties']
                    polity_name = properties['Name'].replace('(', '').replace(')', '')  # Remove spaces and brackets from name
                    polity_colour_key = polity_name
                    try:
                        # If a shape has components we'll load the components instead
                        # ... unless the components have their own components, then load the top level shape
                        # ... or the shape is a personal union, then load the personal union shape
                        if properties['Components']:
                            if ';' not in properties['SeshatID']:
                                if len(properties['Components']) > 0 and '(' not in properties['Components']:
                                    polity_name = None
                    except KeyError:
                        pass
                    try:
                        if properties['Member_of']:
                            # If a shape is a component, get the parent polity to use as the polity_colour_key
                            if len(properties['Member_of']) > 0:
                                polity_colour_key = properties['Member_of'].replace('(', '').replace(')', '')
                    except KeyError:
                        pass
                    if polity_name:
                        if properties['Type'] != 'POLITY':
                            polity_name = properties['Type'] + ': ' + polity_name
                        if polity_colour_key not in polity_shapes:
                            polity_shapes[polity_colour_key] = []
                        polity_shapes[polity_colour_key].append(feature)

                        all_polities.add(polity_colour_key)

                        self.stdout.write(self.style.SUCCESS(f'Found shape for {polity_name} ({properties['FromYear']})'))

        # Sort the polities and generate a colour mapping
        unique_polities = sorted(all_polities)
        self.stdout.write(self.style.SUCCESS(f'Generating colour mapping for {len(unique_polities)} polities'))
        pol_col_map = polity_colour_mapping(unique_polities)
        self.stdout.write(self.style.SUCCESS(f'Colour mapping generated'))

        # Iterate through polity_shapes and create VideoShapefile instances
        for polity_colour_key, features in polity_shapes.items():
            for feature in features:
                properties = feature['properties']
                polity_name = properties["Name"].replace('(', '').replace(')', '')
                if properties['Type'] != 'POLITY':
                    polity_name = properties['Type'] + ': ' + polity_name
                self.stdout.write(self.style.SUCCESS(f'Importing shape for {polity_name} ({properties['FromYear']})'))
                
                # Save geom and convert Polygon to MultiPolygon if necessary
                geom = GEOSGeometry(json.dumps(feature['geometry']))
                if geom.geom_type == 'Polygon':
                    geom = MultiPolygon(geom)

                self.stdout.write(self.style.SUCCESS(f'Creating VideoShapefile instance for {polity_name} ({properties['FromYear']} - {properties['ToYear']})'))

                VideoShapefile.objects.create(
                    geom=geom,
                    name=polity_name,
                    polity=polity_colour_key,
                    wikipedia_name=properties['Wikipedia'],
                    seshat_id=properties['SeshatID'],
                    area=properties['Area'],
                    start_year=properties['FromYear'],
                    end_year=properties['ToYear'],
                    polity_start_year=polity_start_year,
                    polity_end_year=polity_end_year,
                    colour=pol_col_map[polity_colour_key]
                )

                self.stdout.write(self.style.SUCCESS(f'Successfully imported shape for {polity_name} ({properties['FromYear']})'))

            self.stdout.write(self.style.SUCCESS(f'Successfully imported all shapes for {polity_name}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully imported all data from {filename}'))

        ###########################################################
        ### Adjust the tolerance param of ST_Simplify as needed ###
        ###########################################################

        self.stdout.write(self.style.SUCCESS('Adding simplified geometries for faster loading...'))

        ## Use this code if you want to simplify the geometries
        # with connection.cursor() as cursor:
        #     cursor.execute("""
        #         UPDATE core_videoshapefile 
        #         SET simplified_geom = ST_Simplify(geom, 0.07);
        #     """)

        ## Use this code if you don't need to simplify the geometries
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE core_videoshapefile
                SET simplified_geom = geom;
            """)
        self.stdout.write(self.style.SUCCESS('Simplified geometries added'))


def polity_colour_mapping(polities):
    """Use DistinctiPy package to assign a colour to each polity"""
    colours = []
    for col in get_colors(len(polities)):
        colours.append(get_hex(col))
    return dict(zip(polities, colours))
