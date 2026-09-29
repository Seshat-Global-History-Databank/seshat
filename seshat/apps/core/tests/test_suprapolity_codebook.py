import importlib

from django.test import SimpleTestCase

from seshat.apps.general.models import POLITY_SUPRAPOLITY_RELATIONS_CHOICES


codebook_migration = importlib.import_module(
    "seshat.apps.core.migrations.0091_update_suprapolity_codebook"
)


class SuprapolityCodebookTests(SimpleTestCase):
    def test_renames_codes_without_changing_stored_values(self):
        labels = dict(POLITY_SUPRAPOLITY_RELATIONS_CHOICES)
        self.assertEqual(labels["vassalage"], "subject to")
        self.assertEqual(labels["nominal allegiance"], "nominally subject to")

    def test_updates_html_explanation_and_preserves_other_entries(self):
        original = (
            "<ul><li><strong>alliance with:</strong> existing alliance text</li>"
            "<li><strong>personal union with:</strong> existing union text</li>"
            "<li><strong>nominal allegiance to:</strong> old nominal text</li>"
            "<li><strong>vassal state of:</strong> old vassal text</li>"
            "<li><strong>none:</strong> existing none text</li></ul>"
        )

        updated = codebook_migration.revised_explanation(original)

        self.assertIn("<strong>alliance with:</strong> existing alliance text", updated)
        self.assertIn("<strong>personal union with:</strong> existing union text", updated)
        self.assertIn("<strong>none:</strong> existing none text", updated)
        self.assertIn("<strong>subject to:</strong>", updated)
        self.assertIn("<strong>nominally subject to:</strong>", updated)
        self.assertNotIn("<strong>vassal state of:</strong>", updated)
        self.assertNotIn("<strong>nominal allegiance to:</strong>", updated)
        self.assertLess(updated.index("<strong>subject to:</strong>"),
                        updated.index("<strong>nominally subject to:</strong>"))

    def test_unrecognized_explanation_is_not_overwritten(self):
        with self.assertRaisesRegex(ValueError, "Unrecognized supra-polity"):
            codebook_migration.revised_explanation("custom editorial content")
