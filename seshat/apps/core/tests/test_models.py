from django.test import TestCase
from models import Polity, Nga, Seshat_region, Macro_region
from django.core.exceptions import ValidationError
import decimal
from datetime import datetime


class PolityModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods

        mac_region = Macro_region.objects.create(name="Southwest Asia")

        home_seshat_region = Seshat_region.objects.create(
            name="Mesopotamia", subregions_list="Iraq, Kuwait", mac_region=mac_region
        )

        home_nga = Nga.objects.create(
            name="Southern Mesopotamia",
            subregion="Levant-Mesopotamia",
            longitude=decimal.Decimal("44.420000000000"),
            latitude=decimal.Decimal("32.470000000000"),
            capital_city="Babylon (Hillah)",
            nga_code="IQ",
            fao_country="Iraq",
            world_region="Southwest Asia",
        )


        cls.polity = Polity.objects.create(
                name="IqAbbs1",
                start_year=750,
                end_year=946,
                long_name="Abbasid Caliphate I",
                new_name="iq_abbasid_cal_1",
                polity_tag="LEGACY",
                general_description="Abbasid Caliphate in Mesopotamia.",
                shapefile_name="",
                home_nga=home_nga,
                home_seshat_region=home_seshat_region,
            )

        def test_name_max_length(self):
            polity = PolityModelTest.polity
            max_length = polity._meta.get_field('name').max_length
            self.assertEqual(max_length, 100)

        def test_long_name_max_length(self):
            polity = PolityModelTest.polity
            max_length = polity._meta.get_field('long_name').max_length
            self.assertEqual(max_length, 200)

        def test_new_name_max_length(self):
            polity = PolityModelTest.polity
            max_length = polity._meta.get_field('new_name').max_length
            self.assertEqual(max_length, 100)

        def test_shapefile_name_max_length(self):
            polity = PolityModelTest.polity
            max_length = polity._meta.get_field('shapefile_name').max_length
            self.assertEqual(max_length, 300)

        def test_polity_tag_default(self):
            polity = PolityModelTest.polity
            default_tag = polity._meta.get_field('polity_tag').default
            self.assertEqual(default_tag, "OTHER_TAG")

        def test_polity_str_method(self):
            polity = PolityModelTest.polity
            expected_str = "Abbasid Caliphate I (iq_abbasid_cal_1)"
            self.assertEqual(str(polity), expected_str)

        def test_polity_clean_validation(self):
            polity = PolityModelTest.polity

            # Valid case
            polity.start_year = 800
            polity.end_year = 900
            try:
                polity.clean()  # Should not raise any exceptions
            except ValidationError:
                self.fail("Polity.clean() raised ValidationError unexpectedly!")

            # Invalid case: start_year > end_year
            polity.start_year = 950
            polity.end_year = 900
            with self.assertRaises(ValidationError):
                polity.clean()

            # Invalid case: end_year > current year
            current_year = int(datetime.now().strftime("%Y"))
            polity.start_year = 800
            polity.end_year = current_year + 1
            with self.assertRaises(ValidationError):
                polity.clean()

            # Invalid case: start_year > current year
            polity.start_year = current_year + 1
            polity.end_year = current_year + 2
            with self.assertRaises(ValidationError):
                polity.clean()

        def test_unique_together_constraint(self):
            # Attempting to create a Polity with the same name should raise an IntegrityError
            with self.assertRaises(Exception):  # Replace with the specific IntegrityError exception if needed
                Polity.objects.create(
                    name="IqAbbs1",
                    start_year=800,
                    end_year=900,
                    long_name="Abbasid Caliphate II",
                    new_name="iq_abbasid_cal_2",
                    polity_tag="LEGACY",
                    general_description="A second Abbasid polity.",
                    home_nga=self.polity.home_nga,
                    home_seshat_region=self.polity.home_seshat_region,
                )