import csv
import os
import tempfile
from collections import defaultdict
from io import StringIO
from types import SimpleNamespace
from unittest.mock import patch

from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import RequestFactory, SimpleTestCase, TestCase

from seshat.apps.core.management.commands.import_coinhoards import (
    MODEL_READY_REQUIRED_COLUMNS,
)
from seshat.apps.core.management.commands.map_coinhoards_to_polities import (
    map_coinhoard_to_polities,
)
from seshat.apps.core.views_coinhoards import (
    _coinhoard_dataset_choices,
    _filtered_coinhoard_queryset,
    _format_deposit_date,
    _source_record_url,
    coinhoard_polity_context,
    hoard_export_csv,
)
from seshat.apps.core.models import (
    Cliopatria,
    CoinHoard,
    CoinHoardPolityMapping,
    Polity,
)


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
                fieldnames=MODEL_READY_REQUIRED_COLUMNS,
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

    def test_incomplete_model_ready_csv_is_rejected_without_erasing_existing_data(self):
        hoard = CoinHoard.objects.create(
            seshat_id="900001",
            external_dataset_id="TEST_EXISTING",
            data_source="Test dataset",
            hoard_name="Original name",
            year_from=400,
            deposit_year_from=425,
            latitude="51.5000000",
            longitude="-0.1000000",
            summary="Original summary",
        )
        handle = tempfile.NamedTemporaryFile("w", newline="", suffix=".csv", delete=False)
        try:
            writer = csv.DictWriter(
                handle,
                fieldnames=["external_dataset_id", "hoard_name"],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "external_dataset_id": "TEST_EXISTING",
                    "hoard_name": "Replacement name",
                }
            )
            handle.close()

            with self.assertRaisesMessage(CommandError, "Model-ready CSV is incomplete"):
                call_command("import_coinhoards", csv=handle.name, verbosity=0)
        finally:
            handle.close()
            os.unlink(handle.name)

        hoard.refresh_from_db()
        self.assertEqual(hoard.hoard_name, "Original name")
        self.assertEqual(hoard.year_from, 400)
        self.assertEqual(hoard.deposit_year_from, 425)
        self.assertEqual(hoard.summary, "Original summary")

    def test_legacy_chre_csv_remains_supported(self):
        handle = tempfile.NamedTemporaryFile("w", newline="", suffix=".csv", delete=False)
        try:
            writer = csv.DictWriter(
                handle,
                fieldnames=["id", "hoardName", "terminalYear1", "terminalYear2"],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "id": "7",
                    "hoardName": "Legacy CHRE hoard",
                    "terminalYear1": "410",
                    "terminalYear2": "420",
                }
            )
            handle.close()

            call_command("import_coinhoards", csv=handle.name, verbosity=0)
        finally:
            handle.close()
            os.unlink(handle.name)

        hoard = CoinHoard.objects.get(external_dataset_id="CHRE00007")
        self.assertEqual(hoard.hoard_name, "Legacy CHRE hoard")
        self.assertEqual(hoard.year_from, 410)
        self.assertEqual(hoard.year_to, 420)
        self.assertIsNone(hoard.deposit_year_from)

    def test_duplicate_model_ready_ids_are_rejected(self):
        handle = tempfile.NamedTemporaryFile("w", newline="", suffix=".csv", delete=False)
        try:
            writer = csv.DictWriter(handle, fieldnames=MODEL_READY_REQUIRED_COLUMNS)
            writer.writeheader()
            writer.writerow(
                {
                    "external_dataset_id": "TEST_DUPLICATE",
                    "data_source": "Test dataset",
                    "hoard_name": "First row",
                }
            )
            writer.writerow(
                {
                    "external_dataset_id": "TEST_DUPLICATE",
                    "data_source": "Test dataset",
                    "hoard_name": "Second row",
                }
            )
            handle.close()

            with self.assertRaisesMessage(CommandError, "Duplicate external_dataset_id"):
                call_command("import_coinhoards", csv=handle.name, verbosity=0)
        finally:
            handle.close()
            os.unlink(handle.name)

        self.assertFalse(
            CoinHoard.objects.filter(external_dataset_id="TEST_DUPLICATE").exists()
        )


class CoinHoardViewHelperTests(SimpleTestCase):
    def test_deposit_date_prefers_normalized_range_over_duplicate_display(self):
        hoard = CoinHoard(
            deposit_year_from=931,
            deposit_year_to=945,
            deposit_display="931–945",
        )

        self.assertEqual(_format_deposit_date(hoard), "931 CE to 945 CE")

    def test_source_record_url_is_blank_for_dataset_only_coupland_row(self):
        hoard = CoinHoard(
            external_dataset_id="COUPLAND0253",
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
            external_dataset_id="BNSENG0735",
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
            external_dataset_id="CHORGigch0091",
            raw_external_id="igch0091",
            data_source="CoinHoards.org",
            external_url="http://coinhoards.org/id/igch0091",
        )

        self.assertEqual(
            _source_record_url(hoard),
            "http://coinhoards.org/id/igch0091",
        )


class CoinHoardDatasetFilterTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        coupland_hoard = CoinHoard.objects.create(
            seshat_id="990001",
            external_dataset_id="COUPLAND0253",
            raw_external_id="253",
            data_source="Coupland Carolingian Hoards",
            hoard_name="Coupland test hoard",
            number_of_coins=70,
            deposit_year_from=425,
            deposit_year_to=430,
            city="Zillis",
            country="Switzerland",
        )
        CoinHoard.objects.create(
            seshat_id="990002",
            external_dataset_id="COUPLAND0254",
            raw_external_id="254",
            data_source="Coupland Carolingian Hoards",
            hoard_name="Second Coupland test hoard",
        )
        chre_hoard = CoinHoard.objects.create(
            seshat_id="990003",
            external_dataset_id="CHRE00253",
            raw_external_id="253",
            data_source="Coin Hoards of the Roman Empire",
            hoard_name="CHRE test hoard",
            number_of_coins=5,
            year_from=400,
            year_to=410,
            city="Rome",
            country="Italy",
        )
        CoinHoard.objects.create(
            seshat_id="990004",
            external_dataset_id="UNSOURCED001",
            data_source="",
            hoard_name="Unclassified test hoard",
        )
        cls.polity = Polity.objects.create(
            name="Coin hoard filter test polity",
            long_name="Coin hoard filter test polity",
            new_name="coinhoard_filter_test_polity",
            start_year=350,
            end_year=500,
        )
        CoinHoardPolityMapping.objects.create(
            coin_hoard=coupland_hoard,
            polity=cls.polity,
            overlap_year_from=425,
            overlap_year_to=430,
            temporal_match_basis="deposit",
        )
        CoinHoardPolityMapping.objects.create(
            coin_hoard=chre_hoard,
            polity=cls.polity,
            overlap_year_from=400,
            overlap_year_to=410,
            temporal_match_basis="terminal",
        )

    def test_dataset_choices_are_dynamic_and_include_record_counts(self):
        self.assertEqual(
            _coinhoard_dataset_choices(),
            [
                {
                    "data_source": "Coin Hoards of the Roman Empire",
                    "count": 1,
                },
                {
                    "data_source": "Coupland Carolingian Hoards",
                    "count": 2,
                },
            ],
        )

    def test_dataset_filter_selects_exact_source_and_combines_with_search(self):
        request = RequestFactory().get(
            "/core/coinhoards/",
            {
                "dataset": "Coupland Carolingian Hoards",
                "q": "0253",
            },
        )

        queryset, q, dataset, start, end, polity_ids = _filtered_coinhoard_queryset(
            request
        )

        self.assertEqual(
            list(queryset.values_list("external_dataset_id", flat=True)),
            ["COUPLAND0253"],
        )
        self.assertEqual(q, "0253")
        self.assertEqual(dataset, "Coupland Carolingian Hoards")
        self.assertEqual(start, "")
        self.assertEqual(end, "")
        self.assertEqual(polity_ids, [])

    def test_polity_context_summarizes_and_caps_associated_hoards(self):
        context = coinhoard_polity_context(self.polity.id, preview_limit=1)

        self.assertEqual(context["coinhoard_count"], 2)
        self.assertTrue(context["coinhoard_has_more"])
        self.assertEqual(
            context["coinhoard_dataset_counts"],
            [
                {
                    "data_source": "Coin Hoards of the Roman Empire",
                    "count": 1,
                },
                {
                    "data_source": "Coupland Carolingian Hoards",
                    "count": 1,
                },
            ],
        )
        self.assertEqual(len(context["associated_coinhoards"]), 1)
        hoard = context["associated_coinhoards"][0]
        self.assertEqual(hoard.external_dataset_id, "CHRE00253")
        self.assertEqual(hoard.location_label, "Rome, Italy")
        self.assertEqual(hoard.terminal_year_label, "400 CE to 410 CE")
        self.assertEqual(hoard.deposit_year_label, "")

    def test_csv_export_applies_dataset_and_polity_filters(self):
        request = RequestFactory().get(
            "/core/coinhoards/export/",
            {
                "dataset": "Coupland Carolingian Hoards",
                "polity": str(self.polity.id),
                "col": ["external_dataset_id", "number_of_coins", "data_source"],
                "delimiter": "comma",
            },
        )
        request.user = SimpleNamespace(is_authenticated=True)

        response = hoard_export_csv(request)
        rows = list(csv.reader(StringIO(response.content.decode("utf-8-sig"))))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response["Content-Type"].startswith("text/csv"))
        self.assertIn("coinhoards_export_", response["Content-Disposition"])
        self.assertEqual(
            rows,
            [
                ["External dataset ID", "Number of coins", "Data source"],
                ["COUPLAND0253", "70", "Coupland Carolingian Hoards"],
            ],
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
