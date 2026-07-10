import csv
import os
import tempfile
from collections import defaultdict
from unittest.mock import patch

from django.core.management import call_command
from django.test import SimpleTestCase, TestCase

from seshat.apps.core.management.commands.map_coinhoards_to_polities import (
    map_coinhoard_to_polities,
)
from seshat.apps.core.views_coinhoards import (
    _external_dataset_id_label,
    _format_deposit_date,
    _source_record_url,
)
from seshat.apps.core.models import Cliopatria, CoinHoard, Polity


class FakeShapeQuerySet(list):
    def only(self, *args):
        return self

    def order_by(self, *args):
        return self


class CoinHoardImportTests(TestCase):
    def test_model_ready_csv_import_keeps_terminal_and_deposit_dates_separate(self):
        handle = tempfile.NamedTemporaryFile("w", newline="", suffix=".csv", delete=False)
        try:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
                    "external_dataset_id",
                    "raw_external_id",
                    "data_source",
                    "hoard_name",
                    "number_of_coins",
                    "year_from",
                    "year_to",
                    "deposit_year_from",
                    "deposit_year_to",
                    "deposit_display",
                    "latitude",
                    "longitude",
                    "external_url",
                ],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "external_dataset_id": "TEST001",
                    "raw_external_id": "raw-1",
                    "data_source": "Test dataset",
                    "hoard_name": "Test hoard",
                    "number_of_coins": "12",
                    "year_from": "400",
                    "year_to": "410",
                    "deposit_year_from": "425",
                    "deposit_year_to": "430",
                    "deposit_display": "425-430 CE",
                    "latitude": "51.5",
                    "longitude": "-0.1",
                    "external_url": "https://example.test/hoard/1",
                }
            )
            handle.close()

            call_command("import_coinhoards", csv=handle.name, verbosity=0)
        finally:
            handle.close()
            os.unlink(handle.name)

        hoard = CoinHoard.objects.get(external_dataset_id="TEST001")
        self.assertEqual(hoard.year_from, 400)
        self.assertEqual(hoard.year_to, 410)
        self.assertEqual(hoard.deposit_year_from, 425)
        self.assertEqual(hoard.deposit_year_to, 430)
        self.assertEqual(hoard.deposit_display, "425-430 CE")


class CoinHoardViewHelperTests(SimpleTestCase):
    def test_deposit_date_prefers_normalized_range_over_duplicate_display(self):
        hoard = CoinHoard(
            deposit_year_from=931,
            deposit_year_to=945,
            deposit_display="931–945",
        )

        self.assertEqual(_format_deposit_date(hoard), "931 CE to 945 CE")

    def test_coupland_id_label_removes_internal_separator(self):
        self.assertEqual(_external_dataset_id_label("COUPLAND_0253"), "COUPLAND0253")

    def test_non_coupland_id_label_is_unchanged(self):
        self.assertEqual(_external_dataset_id_label("CHRE00253"), "CHRE00253")

    def test_source_record_url_is_blank_for_dataset_only_coupland_row(self):
        hoard = CoinHoard(
            external_dataset_id="COUPLAND_0253",
            raw_external_id="253",
            data_source="Coupland Carolingian Hoards",
            external_url="https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/23984&version=1.0",
        )

        self.assertEqual(_source_record_url(hoard), "")

    def test_source_record_url_is_built_for_chre_rows(self):
        hoard = CoinHoard(
            external_dataset_id="CHRE00253",
            raw_external_id="253",
            data_source="Coin Hoards of the Roman Empire",
        )

        self.assertEqual(
            _source_record_url(hoard),
            "https://chre.ashmus.ox.ac.uk/hoard/253",
        )

    def test_source_record_url_uses_bns_per_hoard_url(self):
        hoard = CoinHoard(
            external_dataset_id="ENG0735",
            raw_external_id="ENG0735",
            data_source="British Numismatic Society",
            external_url="https://www.britnumsoc.uk/hoard/ENG0735",
        )

        self.assertEqual(
            _source_record_url(hoard),
            "https://www.britnumsoc.uk/hoard/ENG0735",
        )

    def test_source_record_url_uses_coinhoards_org_per_hoard_url(self):
        hoard = CoinHoard(
            external_dataset_id="IGCH0091",
            raw_external_id="igch0091",
            data_source="CoinHoards.org",
            external_url="http://coinhoards.org/id/igch0091",
        )

        self.assertEqual(
            _source_record_url(hoard),
            "http://coinhoards.org/id/igch0091",
        )


class CoinHoardPolityMappingTests(SimpleTestCase):
    def setUp(self):
        self.polity = Polity(
            id=1,
            name="Test polity",
            long_name="Test polity",
            new_name="test_polity",
            start_year=400,
            end_year=700,
        )
        self.shape = Cliopatria(
            id=1,
            name="Test shape",
            seshat_id="test_polity",
            area=1.0,
            start_year=400,
            end_year=700,
            polity_start_year=400,
            polity_end_year=700,
            colour="#FFFFFF",
            components="",
            member_of="",
            wikipedia_name="",
        )

    def test_mapping_uses_deposit_date(self):
        hoard = CoinHoard(
            id=1,
            seshat_id="900001",
            external_dataset_id="TEST002",
            data_source="Test dataset",
            hoard_name="Deposit-only hoard",
            latitude=0.5,
            longitude=0.5,
            deposit_year_from=550,
            deposit_year_to=560,
        )

        with patch(
            "seshat.apps.core.management.commands.map_coinhoards_to_polities.Cliopatria.objects.filter",
            return_value=FakeShapeQuerySet([self.shape]),
        ):
            mappings = map_coinhoard_to_polities(
                hoard,
                defaultdict(list, {"test_polity": [self.polity]}),
            )

        self.assertEqual(len(mappings), 1)
        self.assertEqual(mappings[0].overlap_year_from, 550)
        self.assertEqual(mappings[0].temporal_match_basis, "deposit")

    def test_mapping_prefers_deposit_date_when_both_dates_exist(self):
        hoard = CoinHoard(
            id=2,
            seshat_id="900002",
            external_dataset_id="TEST003",
            data_source="Test dataset",
            hoard_name="Terminal hoard",
            latitude=0.5,
            longitude=0.5,
            year_from=450,
            deposit_year_from=550,
        )

        with patch(
            "seshat.apps.core.management.commands.map_coinhoards_to_polities.Cliopatria.objects.filter",
            return_value=FakeShapeQuerySet([self.shape]),
        ):
            mappings = map_coinhoard_to_polities(
                hoard,
                defaultdict(list, {"test_polity": [self.polity]}),
            )

        self.assertEqual(len(mappings), 1)
        self.assertEqual(mappings[0].overlap_year_from, 550)
        self.assertEqual(mappings[0].temporal_match_basis, "deposit")

    def test_mapping_falls_back_to_terminal_date_when_deposit_date_missing(self):
        hoard = CoinHoard(
            id=3,
            seshat_id="900003",
            external_dataset_id="TEST004",
            data_source="Test dataset",
            hoard_name="Terminal-only hoard",
            latitude=0.5,
            longitude=0.5,
            year_from=450,
        )

        with patch(
            "seshat.apps.core.management.commands.map_coinhoards_to_polities.Cliopatria.objects.filter",
            return_value=FakeShapeQuerySet([self.shape]),
        ):
            mappings = map_coinhoard_to_polities(
                hoard,
                defaultdict(list, {"test_polity": [self.polity]}),
            )

        self.assertEqual(len(mappings), 1)
        self.assertEqual(mappings[0].overlap_year_from, 450)
        self.assertEqual(mappings[0].temporal_match_basis, "terminal_fallback")
