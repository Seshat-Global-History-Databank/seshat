from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.template.loader import render_to_string
from django.urls import reverse

from seshat.apps.accounts.models import Seshat_Expert
from seshat.apps.core.models import Polity, SeshatComment
from seshat.apps.crisisdb.models import (
    Check_choice,
    Instability_event,
    Instability_ref,
    Instability_type,
)


class InstabilityCreateViewTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="instability_creator",
            email="instability_creator@example.com",
            password="testpass123",
            is_staff=True,
            first_name="Instability",
            last_name="Creator",
        )
        user.user_permissions.add(Permission.objects.get(codename="add_capital"))
        user.user_permissions.add(
            Permission.objects.get(codename="add_seshatprivatecommentpart")
        )
        Seshat_Expert.objects.create(user=user, role=Seshat_Expert.RA)
        self.user = user
        self.client.force_login(user)

    def test_instability_create_page_renders_for_permitted_user(self):

        response = self.client.get(reverse("instability_event-create"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Instability Event")
        self.assertEqual(response.context["create_layout_mode"], "instability_event_manual")
        self.assertEqual(response.context["extra_var"].name, "name")
        self.assertEqual(response.context["extra_var2"].name, "inst_intensity")
        self.assertEqual(response.context["extra_var3"].name, "inst_extent")
        self.assertEqual(response.context["extra_var4"].name, "inst_type")

    def test_instability_list_page_shows_create_button_for_editors(self):
        response = self.client.get(reverse("instability_events_all"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse("instability_event-create"))

    def test_instability_row_actions_include_inline_create_button(self):
        polity = Polity.objects.create(
            name="test_polity",
            new_name="test_polity",
            long_name="Test Polity",
            start_year=100,
            end_year=200,
        )
        event = Instability_event.objects.create(
            polity=polity,
            name="Test Instability",
            year_from=150,
            year_to=151,
        )

        rendered = render_to_string(
            "core/partials/_abc_obj_instability.html",
            {
                "user": self.user,
                "obj": event,
                "object": polity,
                "key": "instability_event",
                "my_app_name": "crisisdb",
            },
        )

        self.assertIn(f'{reverse("instability_event-create")}?polity_id_x={polity.id}', rendered)

    def test_manual_instability_update_uses_standard_update_template(self):
        polity = Polity.objects.create(
            name="manual_polity",
            new_name="manual_polity",
            long_name="Manual Polity",
            start_year=100,
            end_year=200,
        )
        event = Instability_event.objects.create(
            polity=polity,
            name="Manual Instability",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
            llm_description="Old generated note that should not drive the UI",
        )

        response = self.client.get(reverse("instability_event-updatenew", args=[event.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/generic_templates/generic_update.html")
        self.assertEqual(response.context["extra_var"].name, "name")
        self.assertEqual(response.context["extra_var2"].name, "inst_intensity")
        self.assertEqual(response.context["extra_var3"].name, "inst_extent")
        self.assertEqual(response.context["extra_var4"].name, "inst_type")

    def test_llm_instability_update_keeps_llm_template(self):
        polity = Polity.objects.create(
            name="llm_polity",
            new_name="llm_polity",
            long_name="LLM Polity",
            start_year=100,
            end_year=200,
        )
        event = Instability_event.objects.create(
            polity=polity,
            name="LLM Instability",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )

        response = self.client.get(reverse("instability_event-updatenew", args=[event.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/generic_templates/generic_update_llm.html")

    def test_manual_instability_badges_show_only_manual_marker(self):
        polity = Polity.objects.create(
            name="manual_badge_polity",
            new_name="manual_badge_polity",
            long_name="Manual Badge Polity",
            start_year=100,
            end_year=200,
        )
        event = Instability_event.objects.create(
            polity=polity,
            name="Manual Badge Event",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
        )

        rendered = render_to_string(
            "core/partials/_instability_event_badges.html",
            {"event": event},
        )

        self.assertIn("Manual", rendered)
        self.assertNotIn(">AI<", rendered)
        self.assertNotIn("Batch", rendered)
        self.assertNotIn("fa-user-tie", rendered)
        self.assertNotIn("fa-user-graduate", rendered)
        self.assertNotIn(">D<", rendered)

    def test_manual_instability_badges_stay_manual_only_even_with_comment_and_curators(self):
        polity = Polity.objects.create(
            name="manual_review_polity",
            new_name="manual_review_polity",
            long_name="Manual Review Polity",
            start_year=100,
            end_year=200,
        )
        event = Instability_event.objects.create(
            polity=polity,
            name="Manual Reviewed Event",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
            comment=SeshatComment.objects.create(text="Manual description"),
        )
        event.curator.add(Seshat_Expert.objects.get(user=self.user))

        rendered = render_to_string(
            "core/partials/_instability_event_badges.html",
            {"event": event},
        )

        self.assertIn("Manual", rendered)
        self.assertNotIn("fa-user-tie", rendered)
        self.assertNotIn("fa-user-graduate", rendered)
        self.assertNotIn(">D<", rendered)

    def test_llm_instability_badges_show_ai_and_batch(self):
        polity = Polity.objects.create(
            name="llm_badge_polity",
            new_name="llm_badge_polity",
            long_name="LLM Badge Polity",
            start_year=100,
            end_year=200,
        )
        event = Instability_event.objects.create(
            polity=polity,
            name="LLM Badge Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )

        rendered = render_to_string(
            "core/partials/_instability_event_badges.html",
            {"event": event},
        )

        self.assertIn(">AI<", rendered)
        self.assertIn(event.batch_number, rendered)

    def test_instability_list_can_filter_manual_source(self):
        polity = Polity.objects.create(
            name="source_filter_polity",
            new_name="source_filter_polity",
            long_name="Source Filter Polity",
            start_year=100,
            end_year=200,
        )
        manual_event = Instability_event.objects.create(
            polity=polity,
            name="Manual Source Event",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
        )
        Instability_event.objects.create(
            polity=polity,
            name="LLM Source Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )

        response = self.client.get(reverse("instability_events_all"), {"source": "manual"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [manual_event])

    def test_batch_filter_is_ignored_for_manual_source(self):
        polity = Polity.objects.create(
            name="manual_batch_polity",
            new_name="manual_batch_polity",
            long_name="Manual Batch Polity",
            start_year=100,
            end_year=200,
        )
        manual_event = Instability_event.objects.create(
            polity=polity,
            name="Manual Batch Event",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {"source": "manual", "selected_batch": "Batch 1"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [manual_event])

    def test_source_filter_scopes_filter_options_and_chip(self):
        manual_polity = Polity.objects.create(
            name="manual_filter_polity",
            new_name="manual_filter_polity",
            long_name="Manual Filter Polity",
            start_year=100,
            end_year=200,
        )
        llm_polity = Polity.objects.create(
            name="llm_filter_polity",
            new_name="llm_filter_polity",
            long_name="LLM Filter Polity",
            start_year=100,
            end_year=200,
        )
        Instability_event.objects.create(
            polity=manual_polity,
            name="Manual Event (Macro Event: Manual Macro)",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
        )
        Instability_event.objects.create(
            polity=llm_polity,
            name="LLM Event",
            llm_name="LLM Event (Macro Event: LLM Macro)",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )

        response = self.client.get(reverse("instability_events_all"), {"source": "manual"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [polity.id for polity in response.context["polities"]],
            [manual_polity.id],
        )
        self.assertEqual(response.context["macro_events_with_counts"], [("Manual Macro", 1)])
        self.assertContains(response, "Source:")

    def test_instability_analytics_only_includes_llm_events(self):
        polity = Polity.objects.create(
            name="analytics_polity",
            new_name="analytics_polity",
            long_name="Analytics Polity",
            start_year=100,
            end_year=200,
        )
        llm_event = Instability_event.objects.create(
            polity=polity,
            name="Analytics LLM Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
            llm_year_from=150,
            llm_year_to=151,
        )
        Instability_event.objects.create(
            polity=polity,
            name="Analytics Manual Event",
            source=Instability_event.Source.MANUAL,
            year_from=152,
            year_to=153,
        )

        response = self.client.get(reverse("instability-analytics"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["events"]), [llm_event])
        self.assertEqual(response.context["all_events_count"], 1)

    def test_instability_json_download_uses_source_aware_schema(self):
        polity = Polity.objects.create(
            name="json_polity",
            new_name="json_polity",
            long_name="JSON Polity",
            start_year=100,
            end_year=200,
        )
        inst_type = Instability_type.objects.create(
            name="Urban Riot",
            description="Urban unrest event",
        )
        check_choice = Check_choice.objects.create(
            name="Needs Review",
            check_description="Reviewer flagged this event.",
            color="Blue",
        )
        llm_ref = Instability_ref.objects.create(name="LLM Ref 1")

        manual_event = Instability_event.objects.create(
            polity=polity,
            name="Manual JSON Event (Macro Event: Manual JSON Macro)",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
        )
        manual_event.inst_type.add(inst_type)

        llm_comment = SeshatComment.objects.create(text="Approved LLM summary")
        llm_event = Instability_event.objects.create(
            polity=polity,
            name="LLM JSON Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
            real_event_check="Real",
            sorokin_rationale="Model rationale",
            llm_description="Generated description",
            llm_name="LLM JSON Event (Macro Event: LLM JSON Macro)",
            llm_year_from=152,
            llm_year_to=153,
            llm_inst_type="Urban Riot",
            llm_inst_extent="4",
            llm_inst_intensity="3",
            llm_real_event_check="Real",
            comment=llm_comment,
        )
        llm_event.inst_type.add(inst_type)
        llm_event.ra_check.add(check_choice)
        llm_event.inst_llm_ref.add(llm_ref)

        response = self.client.get(reverse("instability_event-json-download"))

        self.assertEqual(response.status_code, 200)

        payload = response.json()
        self.assertEqual(len(payload), 2)

        entries_by_source = {
            entry["coded_values"]["source"]: entry
            for entry in payload
        }

        manual_entry = entries_by_source["manual"]
        self.assertEqual(
            manual_entry["coded_values"]["name"],
            "Manual JSON Event (Macro Event: Manual JSON Macro)",
        )
        self.assertEqual(manual_entry["coded_values"]["macro_event"], "Manual JSON Macro")
        self.assertEqual(manual_entry["coded_values"]["inst_types"], "Urban Riot")
        self.assertEqual(manual_entry["coded_values"]["checking_status"], "")
        self.assertIsNone(manual_entry["coded_values"]["batch_number"])
        self.assertIsNone(manual_entry["coded_values"]["llm_description"])

        llm_entry = entries_by_source["llm"]
        self.assertEqual(llm_entry["coded_values"]["name"], "LLM JSON Event")
        self.assertEqual(llm_entry["coded_values"]["macro_event"], "LLM JSON Macro")
        self.assertEqual(llm_entry["coded_values"]["inst_types"], "Urban Riot")
        self.assertEqual(llm_entry["coded_values"]["ra_checks"], "Needs Review")
        self.assertEqual(llm_entry["coded_values"]["checking_status"], "RA Checked")
        self.assertEqual(llm_entry["coded_values"]["llm_description"], "Generated description")
        self.assertEqual(llm_entry["coded_values"]["llm_references"], "LLM Ref 1")
        self.assertEqual(
            llm_entry["coded_values"]["ra_approved_description"],
            "Approved LLM summary",
        )
        self.assertEqual(llm_entry["coded_values"]["llm_name"], "LLM JSON Event (Macro Event: LLM JSON Macro)")
