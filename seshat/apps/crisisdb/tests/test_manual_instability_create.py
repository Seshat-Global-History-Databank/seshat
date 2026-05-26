import datetime

from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

from seshat.apps.accounts.models import Seshat_Expert
from seshat.apps.core.models import Polity, SeshatComment
from seshat.apps.crisisdb.instability_filters import (
    GOOD_ROW_FILTER,
    get_polity_instability_queryset,
)
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
        self.assertEqual(response.context["extra_var5"].name, "is_macro_event")

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
        self.assertEqual(response.context["extra_var5"].name, "is_macro_event")

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
        self.assertEqual(response.context["extra_var11"].name, "is_macro_event")

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

    def test_instability_list_can_filter_multiple_polities(self):
        first_polity = Polity.objects.create(
            name="multi_polity_one",
            new_name="multi_polity_one",
            long_name="Multi Polity One",
            start_year=100,
            end_year=200,
        )
        second_polity = Polity.objects.create(
            name="multi_polity_two",
            new_name="multi_polity_two",
            long_name="Multi Polity Two",
            start_year=100,
            end_year=200,
        )
        third_polity = Polity.objects.create(
            name="multi_polity_three",
            new_name="multi_polity_three",
            long_name="Multi Polity Three",
            start_year=100,
            end_year=200,
        )
        first_event = Instability_event.objects.create(
            polity=first_polity,
            name="First Multi Polity Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        second_event = Instability_event.objects.create(
            polity=second_polity,
            name="Second Multi Polity Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        Instability_event.objects.create(
            polity=third_polity,
            name="Third Multi Polity Event",
            source=Instability_event.Source.LLM,
            year_from=154,
            year_to=155,
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {"polity": [str(first_polity.id), str(second_polity.id)]},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [first_event, second_event])
        self.assertEqual(
            response.context["selected_polity_ids"],
            [str(first_polity.id), str(second_polity.id)],
        )

    def test_good_row_filter_excludes_only_disqualifying_checks(self):
        polity = Polity.objects.create(
            name="good_row_polity",
            new_name="good_row_polity",
            long_name="Good Row Polity",
            start_year=100,
            end_year=200,
        )
        bad_row_check = Check_choice.objects.create(
            name="Bad Row",
            check_description="Entire row is invalid.",
            color="Red",
        )
        external_event_check = Check_choice.objects.create(
            name="External Event",
            check_description="External event should be excluded.",
            color="Blue",
        )
        corrected_check = Check_choice.objects.create(
            name="Intensity",
            check_description="Intensity was corrected.",
            color="Red",
        )

        clean_event = Instability_event.objects.create(
            polity=polity,
            name="Clean Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        corrected_event = Instability_event.objects.create(
            polity=polity,
            name="Corrected Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        corrected_event.ra_check.add(corrected_check)

        excluded_bad_row_event = Instability_event.objects.create(
            polity=polity,
            name="Bad Row Event",
            source=Instability_event.Source.LLM,
            year_from=154,
            year_to=155,
        )
        excluded_bad_row_event.ra_check.add(bad_row_check)

        excluded_external_event = Instability_event.objects.create(
            polity=polity,
            name="External Event Row",
            source=Instability_event.Source.LLM,
            year_from=156,
            year_to=157,
        )
        excluded_external_event.ra_check.add(external_event_check)

        mixed_event = Instability_event.objects.create(
            polity=polity,
            name="Mixed Check Event",
            source=Instability_event.Source.LLM,
            year_from=158,
            year_to=159,
        )
        mixed_event.ra_check.add(corrected_check, bad_row_check)

        response = self.client.get(
            reverse("instability_events_all"),
            {"row_quality": GOOD_ROW_FILTER},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["object_list"]),
            [clean_event, corrected_event],
        )
        self.assertEqual(response.context["selected_row_quality"], GOOD_ROW_FILTER)

    def test_polity_instability_queryset_filters_by_batch(self):
        polity = Polity.objects.create(
            name="polity_batch_filter",
            new_name="polity_batch_filter",
            long_name="Polity Batch Filter",
            start_year=100,
            end_year=200,
        )
        batch_one_event = Instability_event.objects.create(
            polity=polity,
            name="Batch One Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        batch_four_event = Instability_event.objects.create(
            polity=polity,
            name="Batch Four Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        manual_event = Instability_event.objects.create(
            polity=polity,
            name="Manual Event",
            source=Instability_event.Source.MANUAL,
            year_from=154,
            year_to=155,
        )
        batch_one_date = timezone.make_aware(datetime.datetime(2025, 3, 1))
        batch_four_date = timezone.make_aware(datetime.datetime(2026, 3, 2))
        Instability_event.objects.filter(pk=batch_one_event.pk).update(created_date=batch_one_date)
        Instability_event.objects.filter(pk=manual_event.pk).update(created_date=batch_one_date)
        Instability_event.objects.filter(pk=batch_four_event.pk).update(created_date=batch_four_date)

        unfiltered_events = list(get_polity_instability_queryset(polity.id))
        batch_one_events = list(
            get_polity_instability_queryset(polity.id, selected_batch="Batch 1")
        )
        manual_events = list(
            get_polity_instability_queryset(
                polity.id,
                selected_source=Instability_event.Source.MANUAL,
                selected_batch="Batch 1",
            )
        )
        llm_batch_one_events = list(
            get_polity_instability_queryset(
                polity.id,
                selected_source=Instability_event.Source.LLM,
                selected_batch="Batch 1",
            )
        )

        self.assertEqual(unfiltered_events, [batch_one_event, batch_four_event, manual_event])
        self.assertEqual(batch_one_events, [batch_one_event])
        self.assertEqual(manual_events, [manual_event])
        self.assertEqual(llm_batch_one_events, [batch_one_event])

    def test_polity_detail_instability_batch_filter_renders(self):
        polity = Polity.objects.create(
            name="polity_detail_batch_filter",
            new_name="polity_detail_batch_filter",
            long_name="Polity Detail Batch Filter",
            start_year=100,
            end_year=200,
        )
        batch_one_event = Instability_event.objects.create(
            polity=polity,
            name="Polity Detail Batch One Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        batch_four_event = Instability_event.objects.create(
            polity=polity,
            name="Polity Detail Batch Four Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        manual_event = Instability_event.objects.create(
            polity=polity,
            name="Polity Detail Manual Event",
            source=Instability_event.Source.MANUAL,
            year_from=154,
            year_to=155,
        )
        Instability_event.objects.filter(pk=batch_one_event.pk).update(
            created_date=timezone.make_aware(datetime.datetime(2025, 3, 1))
        )
        Instability_event.objects.filter(pk=batch_four_event.pk).update(
            created_date=timezone.make_aware(datetime.datetime(2026, 3, 2))
        )
        Instability_event.objects.filter(pk=manual_event.pk).update(
            created_date=timezone.make_aware(datetime.datetime(2025, 3, 1))
        )

        response = self.client.get(
            reverse("polity-detail-main", args=[polity.id]),
            {"selected_batch": "Batch 1"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Source")
        self.assertContains(response, "LLM Batch")
        self.assertContains(response, "Polity Detail Batch One Event")
        self.assertNotContains(response, "Polity Detail Batch Four Event")
        self.assertNotContains(response, "Polity Detail Manual Event")

        manual_response = self.client.get(
            reverse("polity-detail-main", args=[polity.id]),
            {"source": "manual", "selected_batch": "Batch 1"},
        )

        self.assertEqual(manual_response.status_code, 200)
        self.assertContains(manual_response, "Polity Detail Manual Event")
        self.assertNotContains(manual_response, "Polity Detail Batch One Event")
        self.assertNotContains(manual_response, "LLM Batch")

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

    def test_is_macro_event_filter_returns_only_matching_events(self):
        polity = Polity.objects.create(
            name="macro_filter_polity",
            new_name="macro_filter_polity",
            long_name="Macro Filter Polity",
            start_year=100,
            end_year=200,
        )
        macro_event = Instability_event.objects.create(
            polity=polity,
            name="Macro Event",
            source=Instability_event.Source.MANUAL,
            is_macro_event=True,
            year_from=150,
            year_to=151,
        )
        Instability_event.objects.create(
            polity=polity,
            name="Non Macro Event",
            source=Instability_event.Source.MANUAL,
            is_macro_event=False,
            year_from=152,
            year_to=153,
        )

        response = self.client.get(reverse("instability_events_all"), {"is_macro_event": "true"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [macro_event])
        self.assertEqual(response.context["selected_is_macro_event"], "true")

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
            is_macro_event=True,
            year_from=150,
            year_to=151,
        )
        manual_event.inst_type.add(inst_type)

        llm_comment = SeshatComment.objects.create(text="Approved LLM summary")
        llm_event = Instability_event.objects.create(
            polity=polity,
            name="LLM JSON Event",
            source=Instability_event.Source.LLM,
            is_macro_event=False,
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
        self.assertTrue(manual_entry["coded_values"]["is_macro_event"])
        self.assertEqual(manual_entry["coded_values"]["inst_types"], "Urban Riot")
        self.assertEqual(manual_entry["coded_values"]["checking_status"], "")
        self.assertIsNone(manual_entry["coded_values"]["batch_number"])
        self.assertIsNone(manual_entry["coded_values"]["llm_description"])

        llm_entry = entries_by_source["llm"]
        self.assertEqual(llm_entry["coded_values"]["name"], "LLM JSON Event")
        self.assertEqual(llm_entry["coded_values"]["macro_event"], "LLM JSON Macro")
        self.assertFalse(llm_entry["coded_values"]["is_macro_event"])
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
