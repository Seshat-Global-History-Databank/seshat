from django.contrib.gis.geos import MultiPolygon, Polygon, GEOSGeometry
from django.test import TestCase, Client
from django.urls import reverse

import json

from ...general.models import Polity_capital, Polity_peak_years, Polity_language
from ...rt.models import Gov_res_pub_pros
from ...sc.models import Judge

from ..models import VideoShapefile, GADMShapefile, GADMCountries, GADMProvinces, Polity, Capital
from ..templatetags.core_tags import get_polity_capitals, polity_map
from ..views import get_provinces, get_polity_shape_content, get_all_polity_capitals, assign_variables_to_shapes, assign_categorical_variables_to_shapes


class ShapesTest(TestCase):
    """Test case for the shape models and views."""

    def setUp(self):
        """Set up the test client and Polity entry for the view functions."""
        self.maxDiff = None
        self.client = Client()
        self.pk = 1
        # Simple square polygon to use in geospatial data table tests
        self.square = MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))
        self.geo_square = '{"type":"MultiPolygon","coordinates":[[[[0,0],[0,1],[1,1],[0,0]]]]}'
        self.geo_square_for_gadm = GEOSGeometry(self.square).geojson
        self.polity = Polity.objects.create(
            name='TestPolity',
            id=self.pk,
            long_name='TestPolity',
            new_name='Test seshat_id'
        )
        Polity.objects.create(
            name='TestPolity2',
            id=2,
            long_name='TestPolity2',
            new_name='Test seshat_id 2',
            start_year=-100,
            end_year=1100
        )
        Polity.objects.create(
            name='TestPolity3',
            id=3,
            long_name='TestPolity3',
            new_name='Test seshat_id 3',
            start_year=-100,
            end_year=1100
        )
        self.video_shapefile = VideoShapefile.objects.create(
            id=1,
            geom=self.square,
            simplified_geom=self.square,
            name="Test shape",
            polity="Testpolityname",
            seshat_id="Test seshat_id",
            area=100.0,
            start_year=2000,
            end_year=2020,
            polity_start_year=2000,
            polity_end_year=2020,
            colour="#FFFFFF"
        )
        VideoShapefile.objects.create(
            id=2,
            geom=self.square,
            simplified_geom=self.square,
            name="Test shape 2",
            polity="Testpolityname2",
            seshat_id="Test seshat_id 2",
            area=100.0,
            start_year=0,
            end_year=1000,
            polity_start_year=0,
            polity_end_year=1000,
            colour="#FFFFFF"
        )
        self.gadm_shapefile = GADMShapefile.objects.create(
            geom=self.square,
            UID=123456789,
            NAME_0="Test shape"
        )
        self.province = GADMProvinces.objects.create(
            geom=self.square,
            COUNTRY="Test Country",
            NAME_1="Test Province",
            ENGTYPE_1="Test Type"
        )
        self.country = GADMCountries.objects.create(
            geom=self.square,
            COUNTRY="Test Country"
        )
        self.capital = Capital.objects.create(
            name="Test Capital",
            latitude=51.567522,
            longitude=-0.1294531
        )
        Capital.objects.create(
            name="Test Capital 2",
            latitude=51.567523,
            longitude=-0.1294532
        )
        Capital.objects.create(
            name="Test Capital 2A",
            latitude=51.567523,
            longitude=-0.1294532
        )
        self.polity_capital = Polity_capital.objects.create(
            name="TestPolity",
            capital="Test Capital",
            year_from=2000,
            year_to=2020,
            polity_id = self.pk
        )
        Polity_capital.objects.create(
            name="TestPolity2",
            capital="Test Capital 2",
            polity_id=2
        )
        Polity_capital.objects.create(
            name="TestPolity2",
            capital="Test Capital 2A",
            year_from=0,
            year_to=100,
            polity_id=2
        )
        Polity_peak_years.objects.create(
            polity_id=self.pk,
            peak_year_from=2001,
            peak_year_to=2002
        )
        Judge.objects.create(
            name='judge',
            judge='present',
            year_from=2003,
            year_to=2004,
            polity_id=2
        )
        Gov_res_pub_pros.objects.create(
            name='gov_res_pub_pros',
            coded_value='absent',
            year_from=2002,
            year_to=2003,
            polity_id=2
        )
        Polity_language.objects.create(
            name='language',
            language='English',
            polity_id=2,
            year_from=1998,
            year_to=2000
        )
        Polity_language.objects.create(
            name='language',
            language='French',
            year_from=1999,
            year_to=2007,
            polity_id=2
        )

    # Model tests

    def test_video_shapefile_creation(self):
        """Test the creation of a VideoShapefile instance."""
        self.assertIsInstance(self.video_shapefile, VideoShapefile)
        self.assertEqual(self.video_shapefile.name, "Test shape")

    def test_gadm_shapefile_creation(self):
        """Test the creation of a GADMShapefile instance."""
        self.assertIsInstance(self.gadm_shapefile, GADMShapefile)
        self.assertEqual(self.gadm_shapefile.NAME_0, "Test shape")

    def test_gadm_countries_creation(self):
        """Test the creation of a GADMCountries instance."""
        self.assertIsInstance(self.country, GADMCountries)
        self.assertEqual(self.country.COUNTRY, "Test Country")

    def test_gadm_provinces_creation(self):
        """Test the creation of a GADMProvinces instance."""
        self.assertIsInstance(self.province, GADMProvinces)
        self.assertEqual(self.province.NAME_1, "Test Province")

    # View function tests

    def test_get_provinces(self):
        """Test the get_provinces function."""
        province_result = get_provinces(selected_base_map_gadm='province')
        country_result = get_provinces(selected_base_map_gadm='country')
        
        province_expected_result = [{'aggregated_geometry': self.geo_square_for_gadm,
                                     'country': 'Test Country',
                                     'province': 'Test Province',
                                     'province_type': 'Test Type'}]
        country_expected_result = [{'aggregated_geometry': self.geo_square_for_gadm,
                                    'country': 'Test Country'}]
        
        self.assertEqual(province_result, province_expected_result)
        self.assertEqual(country_result, country_expected_result)

    def test_get_polity_shape_content(self):
        """Test the get_polity_shape_content function."""
        expected_result = {
            'shapes': [
                {
                    'seshat_id': 'Test seshat_id',
                    'name': 'Test shape',
                    'polity': 'Testpolityname',
                    'start_year': 2000,
                    'end_year': 2020,
                    'polity_start_year': 2000,
                    'polity_end_year': 2020,
                    'colour': "#FFFFFF",
                    'area': 100.0,
                    'geom_json': self.geo_square,
                    'id': 1
                },
                {
                    'seshat_id': 'Test seshat_id 2',
                    'name': 'Test shape 2',
                    'polity': 'Testpolityname2',
                    'start_year': 0,
                    'end_year': 1000,
                    'polity_start_year': 0,
                    'polity_end_year': 1000,
                    'colour': "#FFFFFF",
                    'area': 100.0,
                    'geom_json': self.geo_square,
                    'id': 2
                }
            ],
            'earliest_year': 0,
            'display_year': 0,
            'tick_years': json.dumps([0, 1010, 2020]),
            'latest_year': 2020,
            'seshat_id_page_id': {
                'Test seshat_id': {'id': 1, 'long_name': 'TestPolity'},
                'Test seshat_id 2': {'id': 2, 'long_name': 'TestPolity2'}
            }
        }
        result = get_polity_shape_content(tick_number=3)

        self.assertEqual(result, expected_result)

    def test_get_polity_shape_content_single_year(self):
        """
            Test the get_polity_shape_content function for a single year.
            This gets run when loading one year of the world map whilst waiting for the rest of the data to load.
        """
        expected_result = {
            'shapes': [
                {
                    'seshat_id': 'Test seshat_id',
                    'name': 'Test shape',
                    'polity': 'Testpolityname',
                    'start_year': 2000,
                    'end_year': 2020,
                    'polity_start_year': 2000,
                    'polity_end_year': 2020,
                    'colour': "#FFFFFF",
                    'area': 100.0,
                    'geom_json': self.geo_square,
                    'id': 1
                }
            ],
            'earliest_year': 0,  # This is the earliest year in the database, not the earliest year of the polity
            'display_year': 2000,
            'tick_years': json.dumps([0, 1010, 2020]),
            'latest_year': 2020,
            'seshat_id_page_id': {
                'Test seshat_id': {'id': 1, 'long_name': 'TestPolity'}
            }
        }
        result = get_polity_shape_content(displayed_year=2000, tick_number=3)

        self.assertEqual(result, expected_result)

    def test_get_polity_shape_content_single_seshat_id(self):
        """
            Test the get_polity_shape_content function for a single polity.
            This gets run for the polity_map view.
        """
        expected_result = {
            'shapes': [
                {
                    'seshat_id': 'Test seshat_id',
                    'name': 'Test shape',
                    'polity': 'Testpolityname',
                    'start_year': 2000,
                    'end_year': 2020,
                    'polity_start_year': 2000,
                    'polity_end_year': 2020,
                    'colour': "#FFFFFF",
                    'area': 100.0,
                    'geom_json': self.geo_square,
                    'id': 1
                }
            ],
            'earliest_year': 2000,  # This is the earliest year of the polity
            'display_year': 2000,
            'tick_years': json.dumps([2000, 2010, 2020]),
            'latest_year': 2020,
            'seshat_id_page_id': {
                'Test seshat_id': {'id': 1, 'long_name': 'TestPolity'}
            }
        }
        result = get_polity_shape_content(seshat_id='Test seshat_id', tick_number=3)

        self.assertEqual(result, expected_result)

    def test_get_polity_shape_content_displayed_year_and_seshat_id_both_set(self):
        """Test that a ValueError is raised if both displayed_year and seshat_id are set."""
        self.assertRaises(ValueError, get_polity_shape_content, displayed_year=2000, seshat_id='Test seshat_id', tick_number=3)

    def test_get_polity_capitals(self):
        """Test the get_polity_capitals function."""
        result = get_polity_capitals(self.pk)
        self.assertEqual(result,
                        [{'capital': 'Test Capital', 'latitude': 51.567522, 'longitude': -0.1294531, 'year_from': 2000, 'year_to': 2020}]
                        )
        
    def test_get_all_polity_capitals(self):
        """Test the get_all_polity_capitals function."""
        result = get_all_polity_capitals()
        self.assertEqual(result,
                        {'Test seshat_id': [
                                {'capital': 'Test Capital', 'latitude': 51.567522, 'longitude': -0.1294531, 'year_from': 2000, 'year_to': 2020}
                            ],
                        'Test seshat_id 2': [
                                {'capital': 'Test Capital 2A', 'latitude': 51.567523, 'longitude': -0.1294532, 'year_from': 0, 'year_to': 100},
                                {'capital': 'Test Capital 2', 'latitude': 51.567523, 'longitude': -0.1294532, 'year_from': -100, 'year_to': 1100}
                            ]
                        }
        )

    def test_polity_map(self):
        """Test the polity_map template tag."""
        expected_result = {
            'content': {
                'shapes': [
                    {
                        'seshat_id': 'Test seshat_id',
                        'name': 'Test shape',
                        'polity': 'Testpolityname',
                        'start_year': 2000,
                        'end_year': 2020,
                        'polity_start_year': 2000,
                        'polity_end_year': 2020,
                        'colour': "#FFFFFF",
                        'area': 100.0,
                        'geom_json': self.geo_square,
                        'id': 1
                    }
                ],
                'earliest_year': 2000,
                'display_year': 2001,  # This is the peak year of the polity
                'latest_year': 2020,
                'tick_years': json.dumps([2000, 2010, 2020]),
                'seshat_id_page_id': {
                    'Test seshat_id': {'id': 1, 'long_name': 'TestPolity'}
                },
                'include_polity_map': True,
                'capitals_info': [
                    {'capital': 'Test Capital', 'latitude': 51.567522, 'longitude': -0.1294531, 'year_from': 2000, 'year_to': 2020}
                ]
            }
        }
        result = polity_map(self.pk, test=True)
    
        self.assertEqual(result, expected_result)

    def test_polity_map_no_peak_year_set(self):
        """Test the polity_map template tag for a polity that has no peak year set."""
        expected_result = {
            'content': {
                'shapes': [
                    {
                        'seshat_id': 'Test seshat_id 2',
                        'name': 'Test shape 2',
                        'polity': 'Testpolityname2',
                        'start_year': 0,
                        'end_year': 1000,
                        'polity_start_year': 0,  # Note: this is taken from the shape objectm, not the polity object (they don't match in this test case)
                        'polity_end_year': 1000,
                        'colour': "#FFFFFF",
                        'area': 100.0,
                        'geom_json': self.geo_square,
                        'id': 2
                    }
                ],
                'earliest_year': 0,
                'display_year': 0,
                'latest_year': 1000,
                'tick_years': json.dumps([0, 500, 1000]),
                'seshat_id_page_id': {
                    'Test seshat_id 2': {'id': 2, 'long_name': 'TestPolity2'}
                },
                'include_polity_map': True,
                'capitals_info': [
                    {'capital': 'Test Capital 2A', 'latitude': 51.567523, 'longitude': -0.1294532, 'year_from': 0, 'year_to': 100},
                    {'capital': 'Test Capital 2', 'latitude': 51.567523, 'longitude': -0.1294532, 'year_from': -100, 'year_to': 1100}
                ]
            }
        }
        result = polity_map(2, test=True)

        self.assertEqual(result, expected_result)

    def test_polity_map_no_content(self):
        """Test the polity_map func when polity has no shapes associated."""
        expected_result = {
            'content': {
                'include_polity_map': False
            }
        }
        result = polity_map(3, test=True)
        self.assertEqual(result, expected_result)

    def test_map_view_initial(self):
        """Test the initial map view which whould redirect to a specific year."""
        response = self.client.get(reverse('world_map'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/core/world_map/?year='))

    def test_map_view_all(self):
        """Test the map view with all data."""
        response = self.client.get(reverse('world_map_all'))
        self.assertEqual(response.status_code, 200)

    def test_provinces_and_countries_view(self):
        """Test the provinces and countries view."""
        response = self.client.get(reverse('provinces_and_countries'))
        self.assertEqual(response.status_code, 200)

    def test_assign_variables_to_shapes(self):
        """Test the assign_variables_to_shapes function."""
        shapes = [
                    {
                        'seshat_id': 'Test seshat_id 2',
                        'name': 'Test shape 2',
                        'polity': 'Testpolityname2',
                        'start_year': 0,
                        'end_year': 1000,
                        'polity_start_year': 0,
                        'polity_end_year': 1000,
                        'colour': "#FFFFFF",
                        'area': 100.0,
                        'geom_json': self.geo_square,
                        'id': 2
                    }
                ]
        app_map = {
            'sc': 'Social Complexity Variables',
            'wf': 'Warfare Variables (Military Technologies)',
            'rt': 'Religion Tolerance'
        }
        result_shapes, result_variables = assign_variables_to_shapes(shapes, app_map)
        # Choose some example variables to test
        expected_result_variables_judge = {
            'formatted': 'Judge',
            'full_name': 'Law: Judge'
        }
        expected_result_variables_gov_res_pub_pros = {
            'formatted': 'Government Restrictions on Public Proselytizings',
            'full_name': 'Government Restrictions: Government Restrictions on Public Proselytizings'
        }
        self.assertEqual(result_variables['Social Complexity Variables']['judge'], expected_result_variables_judge)
        self.assertEqual(result_variables['Religion Tolerance']['gov_res_pub_pros'], expected_result_variables_gov_res_pub_pros)
        # Test that the shapes have been updated with the variables
        self.assertEqual(result_shapes[0]['Judge'], 'present')
        self.assertEqual(result_shapes[0]['Judge_dict'], {'present': [2003, 2004]})
        self.assertEqual(result_shapes[0]['Government Restrictions on Public Proselytizings'], 'absent')
        self.assertEqual(result_shapes[0]['Government Restrictions on Public Proselytizings_dict'], {'absent': [2002, 2003]})

    def test_assign_categorical_variables_to_shapes(self):
        """Test the assign_categorical_variables_to_shapes function."""
        shapes = [
                    {
                        'seshat_id': 'Test seshat_id 2',
                        'name': 'Test shape 2',
                        'polity': 'Testpolityname2',
                        'start_year': 0,
                        'end_year': 1000,
                        'polity_start_year': 0,
                        'polity_end_year': 1000,
                        'colour': "#FFFFFF",
                        'area': 100.0,
                        'geom_json': self.geo_square,
                        'id': 2
                    }
                ]
        result_shapes, result_variables = assign_categorical_variables_to_shapes(shapes, {})
        expected_result_variables_language = {
            'formatted': 'language',
            'full_name': 'Language'
        }
        self.assertEqual(result_variables['General Variables']['polity_language'], expected_result_variables_language)
        self.assertEqual(result_shapes[0]['language'], ['English', 'French'])
        self.assertEqual(result_shapes[0]['language_dict']['English'], [1998, 2000])
        self.assertEqual(result_shapes[0]['language_dict']['French'], [1999, 2007])