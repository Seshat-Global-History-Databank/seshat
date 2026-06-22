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
        polity = Polity.objects.create(
            name="filter_default_polity",
            new_name="filter_default_polity",
            long_name="Filter Default Polity",
            start_year=100,
            end_year=200,
        )
        Instability_event.objects.create(
            polity=polity,
            name="Filter Default Event",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
        )

        response = self.client.get(reverse("instability_events_all"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, reverse("instability_event-create"))
        self.assertContains(response, "Apply filters")
        self.assertContains(response, 'id="year_from_min"')
        self.assertContains(response, 'id="year_to_max"')
        self.assertNotContains(response, 'id="instability-time-section"')
        self.assertContains(response, 'data-bs-target="#instability-scope-section"')
        self.assertContains(response, 'aria-expanded="false"')
        self.assertNotContains(response, 'id="instability-scope-section" class="collapse show"')

    def test_invalid_year_filters_are_ignored_without_error(self):
        response = self.client.get(
            reverse("instability_events_all"),
            {"year_from_min": "not-a-year", "year_to_max": "1.5"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context["selected_year_from_min"])
        self.assertIsNone(response.context["selected_year_to_max"])
        self.assertEqual(response.context["active_filter_count"], 0)

    def test_year_zero_is_a_valid_filter_value(self):
        polity = Polity.objects.create(
            name="year_zero_filter_polity",
            new_name="year_zero_filter_polity",
            long_name="Year Zero Filter Polity",
            start_year=-100,
            end_year=100,
        )
        included_event = Instability_event.objects.create(
            polity=polity,
            name="Year Zero Included Event",
            source=Instability_event.Source.MANUAL,
            year_from=0,
            year_to=0,
        )
        Instability_event.objects.create(
            polity=polity,
            name="Before Year Zero Event",
            source=Instability_event.Source.MANUAL,
            year_from=-10,
            year_to=-10,
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {"year_from_min": "0", "year_to_max": "0"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [included_event])
        self.assertEqual(response.context["selected_year_from_min"], 0)
        self.assertEqual(response.context["selected_year_to_max"], 0)
        self.assertEqual(response.context["active_filter_count"], 2)

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

    def test_instability_list_can_filter_multiple_sources(self):
        polity = Polity.objects.create(
            name="multi_source_filter_polity",
            new_name="multi_source_filter_polity",
            long_name="Multi Source Filter Polity",
            start_year=100,
            end_year=200,
        )
        manual_event = Instability_event.objects.create(
            polity=polity,
            name="Manual Multi Source Event",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
        )
        llm_event = Instability_event.objects.create(
            polity=polity,
            name="LLM Multi Source Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {"source": [Instability_event.Source.MANUAL, Instability_event.Source.LLM]},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [manual_event, llm_event])
        self.assertEqual(
            response.context["selected_source_values"],
            [Instability_event.Source.MANUAL, Instability_event.Source.LLM],
        )
        self.assertIsNone(response.context["selected_source"])
        self.assertEqual(response.context["active_filter_count"], 2)

    def test_zero_result_filters_keep_selected_active_filter_labels(self):
        polity = Polity.objects.create(
            name="zero_result_filter_polity",
            new_name="zero_result_filter_polity",
            long_name="Zero Result Filter Polity",
            start_year=100,
            end_year=200,
        )
        check = Check_choice.objects.create(
            name="Zero Result Check",
            check_description="Used to verify selected filter labels.",
            color="Red",
        )
        event = Instability_event.objects.create(
            polity=polity,
            name="Zero Result LLM Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        event.ra_check.add(check)

        response = self.client.get(
            reverse("instability_events_all"),
            {
                "polity": str(polity.id),
                "ra_check": str(check.id),
                "source": Instability_event.Source.MANUAL,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [])
        self.assertEqual(response.context["selected_polity_filters"], [polity])
        self.assertEqual(response.context["selected_ra_check_filters"], [check])
        self.assertEqual(
            [option.id for option in response.context["polities"] if option.event_count == 0],
            [polity.id],
        )
        self.assertEqual(
            [option.id for option in response.context["check_choices"] if option.event_count == 0],
            [check.id],
        )
        self.assertContains(response, '<small class="fw-light">Polity:</small>')
        self.assertContains(response, '<small class="fw-light">RA Check:</small>')

    def test_batch_filter_forces_llm_rows_even_with_manual_source(self):
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
        llm_event = Instability_event.objects.create(
            polity=polity,
            name="LLM Batch Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        Instability_event.objects.filter(pk=llm_event.pk).update(
            created_date=timezone.make_aware(datetime.datetime(2025, 3, 1))
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {"source": "manual", "selected_batch": "Batch 1"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [llm_event])
        self.assertEqual(response.context["selected_source_values"], [Instability_event.Source.LLM])
        self.assertEqual(response.context["explicit_selected_source"], Instability_event.Source.MANUAL)
        self.assertEqual(response.context["selected_batch_values"], ["Batch 1"])
        self.assertTrue(response.context["batch_filter_forces_llm"])
        self.assertContains(response, "LLM only")
        self.assertContains(response, 'data-instability-source-conflict="batch"')
        self.assertNotContains(response, 'data-instability-clear-sources="true"')
        self.assertNotContains(response, manual_event.name)

    def test_instability_list_can_filter_multiple_batches(self):
        polity = Polity.objects.create(
            name="multi_batch_polity",
            new_name="multi_batch_polity",
            long_name="Multi Batch Polity",
            start_year=100,
            end_year=200,
        )
        batch_one_event = Instability_event.objects.create(
            polity=polity,
            name="Batch One List Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        batch_four_event = Instability_event.objects.create(
            polity=polity,
            name="Batch Four List Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        batch_two_event = Instability_event.objects.create(
            polity=polity,
            name="Batch Two List Event",
            source=Instability_event.Source.LLM,
            year_from=154,
            year_to=155,
        )
        Instability_event.objects.filter(pk=batch_one_event.pk).update(
            created_date=timezone.make_aware(datetime.datetime(2025, 3, 1))
        )
        Instability_event.objects.filter(pk=batch_four_event.pk).update(
            created_date=timezone.make_aware(datetime.datetime(2026, 3, 2))
        )
        Instability_event.objects.filter(pk=batch_two_event.pk).update(
            created_date=timezone.make_aware(datetime.datetime(2025, 4, 1))
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {"selected_batch": ["Batch 1", "Batch 4"]},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [batch_one_event, batch_four_event])
        self.assertEqual(response.context["selected_batch_values"], ["Batch 1", "Batch 4"])
        self.assertEqual(response.context["active_filter_count"], 3)
        self.assertContains(response, "3 filters active")
        self.assertContains(response, "Search & add filters")
        self.assertContains(response, "selected_batch:Batch 1")
        self.assertContains(response, "selected_batch:Batch 4")
        self.assertContains(response, 'name="selected_batch"')
        self.assertContains(response, 'value="Batch 1" selected')
        self.assertContains(response, 'value="Batch 4" selected')
        self.assertContains(response, "Select one or more import batches")
        self.assertContains(response, 'data-instability-source-conflict="batch"')
        self.assertNotContains(response, 'data-instability-clear-sources="true"')
        self.assertNotContains(response, batch_two_event.name)

    def test_instability_list_can_filter_by_exact_event_id(self):
        polity = Polity.objects.create(
            name="event_token_polity",
            new_name="event_token_polity",
            long_name="Event Token Polity",
            start_year=100,
            end_year=200,
        )
        selected_event = Instability_event.objects.create(
            polity=polity,
            name="Selected Exact Event",
            source=Instability_event.Source.MANUAL,
            year_from=150,
            year_to=151,
        )
        other_event = Instability_event.objects.create(
            polity=polity,
            name="Other Exact Event",
            source=Instability_event.Source.MANUAL,
            year_from=152,
            year_to=153,
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {"event": str(selected_event.id)},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [selected_event])
        self.assertEqual(response.context["selected_event_ids"], [str(selected_event.id)])
        self.assertContains(response, f"event:{selected_event.id}")
        self.assertContains(response, "Event:")
        self.assertNotContains(response, other_event.name)

    def test_instability_list_global_text_filter_searches_across_fields(self):
        polity = Polity.objects.create(
            name="global_text_polity",
            new_name="global_text_polity",
            long_name="Global Search Polity",
            start_year=100,
            end_year=200,
        )
        event_type = Instability_type.objects.create(name="Global Search Type")
        matching_event = Instability_event.objects.create(
            polity=polity,
            name="Plain Event Name",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        matching_event.inst_type.add(event_type)
        other_event = Instability_event.objects.create(
            polity=polity,
            name="Other Plain Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {"q": "Global Search Type"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [matching_event])
        self.assertEqual(response.context["selected_text_queries"], ["Global Search Type"])
        self.assertContains(response, 'text:Global Search Type')
        self.assertContains(response, "Search:")
        self.assertNotContains(response, other_event.name)

        reordered_response = self.client.get(
            reverse("instability_events_all"),
            {"q": "TYPE global"},
        )

        self.assertEqual(reordered_response.status_code, 200)
        self.assertEqual(list(reordered_response.context["object_list"]), [matching_event])

        punctuation_response = self.client.get(
            reverse("instability_events_all"),
            {"q": "!!!"},
        )

        self.assertEqual(punctuation_response.status_code, 200)
        self.assertEqual(list(punctuation_response.context["object_list"]), [])

    def test_instability_filter_token_endpoint_returns_grouped_limited_results(self):
        polity = Polity.objects.create(
            name="token_polity",
            new_name="token_polity",
            long_name="Token Polity",
            start_year=100,
            end_year=200,
        )
        event_type = Instability_type.objects.create(name="Token Rebellion")
        check = Check_choice.objects.create(
            name="Token Check",
            check_description="Tokenized review label.",
            color="Blue",
        )
        macro_event = Instability_event.objects.create(
            polity=polity,
            name="A Token Macro Event",
            llm_name="A Token Macro Event (Macro Event: Token Umbrella)",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        macro_event.inst_type.add(event_type)
        macro_event.ra_check.add(check)

        for index in range(10):
            Instability_event.objects.create(
                polity=polity,
                name=f"Token Event {index}",
                source=Instability_event.Source.LLM,
                year_from=152 + index,
                year_to=153 + index,
            )

        response = self.client.get(
            reverse("instability_event-filter-tokens"),
            {"q": "Token"},
        )

        self.assertEqual(response.status_code, 200)
        group_names = [group["text"] for group in response.json()["results"]]
        groups = {
            group["text"]: group["children"]
            for group in response.json()["results"]
        }
        self.assertEqual(
            group_names,
            [
                "Polities",
                "Event Types",
                "Researcher Checks",
                "Text Search",
                "Events",
                "Umbrella Events",
            ],
        )
        self.assertIn("Text Search", groups)
        self.assertIn("Polities", groups)
        self.assertIn("Events", groups)
        self.assertIn("Umbrella Events", groups)
        self.assertIn("Event Types", groups)
        self.assertIn("Researcher Checks", groups)
        self.assertLessEqual(len(groups["Events"]), 8)
        self.assertTrue(
            any(option["id"] == f"polity:{polity.id}" for option in groups["Polities"])
        )
        self.assertTrue(
            any(option["id"] == f"event:{macro_event.id}" for option in groups["Events"])
        )
        self.assertTrue(
            any(option["id"] == "macro_event:Token Umbrella" for option in groups["Umbrella Events"])
        )
        self.assertTrue(
            any(option["id"] == f"inst_type:{event_type.id}" for option in groups["Event Types"])
        )
        self.assertTrue(
            any(option["id"] == f"ra_check:{check.id}" for option in groups["Researcher Checks"])
        )

        reordered_response = self.client.get(
            reverse("instability_event-filter-tokens"),
            {"q": "REBELLION token"},
        )
        reordered_groups = {
            group["text"]: group["children"]
            for group in reordered_response.json()["results"]
        }

        self.assertEqual(reordered_response.status_code, 200)
        reordered_group_names = [
            group["text"]
            for group in reordered_response.json()["results"]
        ]
        self.assertLess(
            reordered_group_names.index("Event Types"),
            reordered_group_names.index("Text Search"),
        )
        self.assertTrue(
            any(
                option["id"] == f"inst_type:{event_type.id}"
                for option in reordered_groups["Event Types"]
            )
        )

    def test_instability_filter_token_endpoint_returns_source_and_batch_tokens(self):
        polity = Polity.objects.create(
            name="batch_token_polity",
            new_name="batch_token_polity",
            long_name="Batch Token Polity",
            start_year=100,
            end_year=200,
        )
        batch_one_event = Instability_event.objects.create(
            polity=polity,
            name="Batch Token Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        Instability_event.objects.filter(pk=batch_one_event.pk).update(
            created_date=timezone.make_aware(datetime.datetime(2025, 3, 1))
        )

        batch_response = self.client.get(
            reverse("instability_event-filter-tokens"),
            {"q": "batch"},
        )
        source_response = self.client.get(
            reverse("instability_event-filter-tokens"),
            {"q": "llm"},
        )

        batch_groups = {
            group["text"]: group["children"]
            for group in batch_response.json()["results"]
        }
        source_groups = {
            group["text"]: group["children"]
            for group in source_response.json()["results"]
        }
        self.assertEqual(batch_response.status_code, 200)
        self.assertIn("LLM Batches", batch_groups)
        self.assertTrue(
            any(option["id"] == "selected_batch:Batch 1" for option in batch_groups["LLM Batches"])
        )
        self.assertEqual(source_response.status_code, 200)
        self.assertIn("Sources", source_groups)
        self.assertTrue(
            any(option["id"] == "source:llm" for option in source_groups["Sources"])
        )

    def test_instability_list_can_require_researcher_checks(self):
        polity = Polity.objects.create(
            name="require_check_polity",
            new_name="require_check_polity",
            long_name="Require Check Polity",
            start_year=100,
            end_year=200,
        )
        required_check = Check_choice.objects.create(
            name="Require Check",
            check_description="A check used for positive filtering.",
            color="Blue",
        )
        other_check = Check_choice.objects.create(
            name="Other Check",
            check_description="A different review label.",
            color="Red",
        )
        matching_event = Instability_event.objects.create(
            polity=polity,
            name="Matching Checked Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        matching_event.ra_check.add(required_check)
        non_matching_event = Instability_event.objects.create(
            polity=polity,
            name="Other Checked Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        non_matching_event.ra_check.add(other_check)
        unchecked_event = Instability_event.objects.create(
            polity=polity,
            name="Unchecked Event",
            source=Instability_event.Source.LLM,
            year_from=154,
            year_to=155,
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {"ra_check": str(required_check.id)},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [matching_event])
        self.assertEqual(response.context["selected_ra_check_ids"], [str(required_check.id)])
        self.assertContains(response, matching_event.name)
        self.assertNotContains(response, non_matching_event.name)
        self.assertNotContains(response, unchecked_event.name)

    def test_required_researcher_checks_are_not_also_excluded(self):
        polity = Polity.objects.create(
            name="require_exclude_conflict_polity",
            new_name="require_exclude_conflict_polity",
            long_name="Require Exclude Conflict Polity",
            start_year=100,
            end_year=200,
        )
        required_check = Check_choice.objects.create(
            name="Required Conflict Check",
            check_description="The check that should stay required.",
            color="Blue",
        )
        other_excluded_check = Check_choice.objects.create(
            name="Other Excluded Check",
            check_description="A separate excluded label.",
            color="Red",
        )
        matching_event = Instability_event.objects.create(
            polity=polity,
            name="Required Conflict Matching Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        matching_event.ra_check.add(required_check)
        Instability_event.objects.create(
            polity=polity,
            name="Required Conflict Unchecked Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )

        response = self.client.get(
            reverse("instability_events_all"),
            {
                "ra_check": str(required_check.id),
                "row_quality": GOOD_ROW_FILTER,
                "excluded_ra_check_mode": "custom",
                "excluded_ra_check": [
                    str(required_check.id),
                    str(other_excluded_check.id),
                ],
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [matching_event])
        self.assertEqual(response.context["selected_ra_check_ids"], [str(required_check.id)])
        self.assertEqual(
            response.context["selected_excluded_ra_check_ids"],
            [str(other_excluded_check.id)],
        )

    def test_required_default_invalid_check_is_not_excluded(self):
        polity = Polity.objects.create(
            name="require_default_invalid_polity",
            new_name="require_default_invalid_polity",
            long_name="Require Default Invalid Polity",
            start_year=100,
            end_year=200,
        )
        bad_row_check = Check_choice.objects.create(
            name="Bad Row",
            check_description="Default invalid label that is explicitly required.",
            color="Red",
        )
        external_event_check = Check_choice.objects.create(
            name="External Event",
            check_description="Another default invalid label.",
            color="Blue",
        )
        bad_row_event = Instability_event.objects.create(
            polity=polity,
            name="Required Bad Row Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        bad_row_event.ra_check.add(bad_row_check)
        external_event = Instability_event.objects.create(
            polity=polity,
            name="Default External Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        external_event.ra_check.add(external_event_check)

        response = self.client.get(
            reverse("instability_events_all"),
            {
                "ra_check": str(bad_row_check.id),
                "row_quality": GOOD_ROW_FILTER,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [bad_row_event])
        self.assertEqual(response.context["selected_ra_check_ids"], [str(bad_row_check.id)])
        self.assertEqual(
            response.context["selected_excluded_ra_check_ids"],
            [str(external_event_check.id)],
        )
        self.assertNotContains(response, external_event.name)

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
        self.assertEqual(response.context["active_filter_count"], 2)
        self.assertContains(response, "2 filters active")

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
        self.assertEqual(
            response.context["selected_excluded_ra_check_ids"],
            [str(bad_row_check.id), str(external_event_check.id)],
        )
        self.assertEqual(
            response.context["selected_excluded_ra_check_labels"],
            ["Bad Row", "External Event"],
        )
        self.assertEqual(response.context["active_filter_count"], 1)
        self.assertTrue(response.context["default_invalid_filter_active"])
        self.assertContains(response, "1 filter active")
        self.assertContains(response, "Exclude invalid rows")
        self.assertContains(response, "Include by Researcher Check")
        self.assertContains(response, "Exclude by Researcher Check")
        self.assertNotContains(response, "Exclude all labels")
        self.assertContains(response, "Researcher checks excluded:")
        self.assertContains(response, "Bad Row, External Event")
        self.assertNotContains(response, "Good rows only")

    def test_good_row_filter_can_customize_excluded_researcher_checks(self):
        polity = Polity.objects.create(
            name="custom_good_row_polity",
            new_name="custom_good_row_polity",
            long_name="Custom Good Row Polity",
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
            check_description="External event should be excluded by default.",
            color="Blue",
        )
        intensity_check = Check_choice.objects.create(
            name="Intensity",
            check_description="Intensity was corrected.",
            color="Red",
        )

        clean_event = Instability_event.objects.create(
            polity=polity,
            name="Custom Clean Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        bad_row_event = Instability_event.objects.create(
            polity=polity,
            name="Custom Bad Row Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        bad_row_event.ra_check.add(bad_row_check)
        external_event = Instability_event.objects.create(
            polity=polity,
            name="Custom External Event",
            source=Instability_event.Source.LLM,
            year_from=154,
            year_to=155,
        )
        external_event.ra_check.add(external_event_check)
        intensity_event = Instability_event.objects.create(
            polity=polity,
            name="Custom Intensity Event",
            source=Instability_event.Source.LLM,
            year_from=156,
            year_to=157,
        )
        intensity_event.ra_check.add(intensity_check)

        response = self.client.get(
            reverse("instability_events_all"),
            {
                "row_quality": GOOD_ROW_FILTER,
                "excluded_ra_check_mode": "custom",
                "excluded_ra_check": [str(bad_row_check.id), str(intensity_check.id)],
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["object_list"]),
            [clean_event, external_event],
        )
        self.assertEqual(
            response.context["selected_excluded_ra_check_ids"],
            [str(bad_row_check.id), str(intensity_check.id)],
        )
        self.assertEqual(
            response.context["selected_excluded_ra_check_labels"],
            ["Bad Row", "Intensity"],
        )
        self.assertFalse(response.context["default_invalid_filter_active"])
        self.assertContains(response, "Bad Row, Intensity")
        self.assertContains(response, external_event.name)
        self.assertNotContains(response, bad_row_event.name)
        self.assertNotContains(response, intensity_event.name)

        implied_row_quality_response = self.client.get(
            reverse("instability_events_all"),
            {
                "excluded_ra_check": [str(bad_row_check.id), str(intensity_check.id)],
            },
        )

        self.assertEqual(implied_row_quality_response.status_code, 200)
        self.assertEqual(
            list(implied_row_quality_response.context["object_list"]),
            [clean_event, external_event],
        )
        self.assertEqual(
            implied_row_quality_response.context["selected_row_quality"],
            GOOD_ROW_FILTER,
        )

    def test_good_row_filter_custom_empty_excludes_no_researcher_checks(self):
        polity = Polity.objects.create(
            name="empty_custom_good_row_polity",
            new_name="empty_custom_good_row_polity",
            long_name="Empty Custom Good Row Polity",
            start_year=100,
            end_year=200,
        )
        bad_row_check = Check_choice.objects.create(
            name="Bad Row",
            check_description="Entire row is invalid.",
            color="Red",
        )
        clean_event = Instability_event.objects.create(
            polity=polity,
            name="Empty Custom Clean Event",
            source=Instability_event.Source.LLM,
            year_from=150,
            year_to=151,
        )
        bad_row_event = Instability_event.objects.create(
            polity=polity,
            name="Empty Custom Bad Row Event",
            source=Instability_event.Source.LLM,
            year_from=152,
            year_to=153,
        )
        bad_row_event.ra_check.add(bad_row_check)

        response = self.client.get(
            reverse("instability_events_all"),
            {
                "row_quality": GOOD_ROW_FILTER,
                "excluded_ra_check_mode": "custom",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["object_list"]), [clean_event, bad_row_event])
        self.assertEqual(response.context["selected_excluded_ra_check_ids"], [])
        self.assertContains(response, "Researcher checks excluded:")
        self.assertContains(response, "None")

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
        self.assertContains(response, "is_macro_event:true")
        self.assertContains(response, "Macroevent")
        self.assertContains(response, "Macro events")
        self.assertContains(response, "Normal events")

        token_response = self.client.get(
            reverse("instability_event-filter-tokens"),
            {"q": "macro"},
        )
        token_groups = {
            group["text"]: group["children"]
            for group in token_response.json()["results"]
        }

        self.assertEqual(token_response.status_code, 200)
        self.assertIn("Macroevent", token_groups)
        self.assertTrue(
            any(
                option["id"] == "is_macro_event:true"
                for option in token_groups["Macroevent"]
            )
        )

        true_token_response = self.client.get(
            reverse("instability_event-filter-tokens"),
            {"q": "true"},
        )
        true_group_names = [
            group["text"]
            for group in true_token_response.json()["results"]
        ]
        true_token_groups = {
            group["text"]: group["children"]
            for group in true_token_response.json()["results"]
        }

        self.assertEqual(true_token_response.status_code, 200)
        self.assertEqual(true_group_names[0], "Macroevent")
        self.assertTrue(
            any(
                option["id"] == "is_macro_event:true"
                for option in true_token_groups["Macroevent"]
            )
        )

        false_token_response = self.client.get(
            reverse("instability_event-filter-tokens"),
            {"q": "false"},
        )
        false_token_groups = {
            group["text"]: group["children"]
            for group in false_token_response.json()["results"]
        }

        self.assertEqual(false_token_response.status_code, 200)
        self.assertTrue(
            any(
                option["id"] == "is_macro_event:false"
                for option in false_token_groups["Macroevent"]
            )
        )

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
