from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from seshat.apps.accounts.models import TermsAcceptance, TermsVersion


class TermsAcceptanceFlowTests(TestCase):
    def setUp(self):
        TermsVersion.objects.update(is_active=False)
        self.old_terms = TermsVersion.objects.create(
            slug="old-terms",
            title="Old terms",
            body_html="<p>Old terms</p>",
            is_active=False,
        )
        self.current_terms = TermsVersion.objects.create(
            slug="current-terms",
            title="Current terms",
            body_html="<p>Current terms</p>",
            is_active=True,
        )
        self.user = get_user_model().objects.create_user(
            username="terms-user",
            password="test-password",
        )
        self.client.force_login(self.user)

    def test_old_acceptance_does_not_satisfy_current_terms(self):
        TermsAcceptance.objects.create(user=self.user, terms=self.old_terms)

        response = self.client.get(reverse("seshat-index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="termsModal"')
        self.assertContains(response, "Current terms")
        self.assertContains(response, "I Agree")

    def test_user_accepts_current_terms_only_once(self):
        agreement_page = self.client.get(reverse("terms_current"))
        self.assertContains(agreement_page, "Current terms")
        self.assertContains(agreement_page, "I Agree")

        response = self.client.post(
            reverse("terms_accept"),
            {"next": reverse("seshat-methods")},
        )

        self.assertRedirects(
            response,
            reverse("seshat-methods"),
            fetch_redirect_response=False,
        )
        self.assertEqual(
            TermsAcceptance.objects.filter(
                user=self.user,
                terms=self.current_terms,
            ).count(),
            1,
        )

        self.client.post(reverse("terms_accept"), {"next": "/"})
        self.assertEqual(
            TermsAcceptance.objects.filter(
                user=self.user,
                terms=self.current_terms,
            ).count(),
            1,
        )

    def test_current_acceptance_allows_site_access(self):
        TermsAcceptance.objects.create(user=self.user, terms=self.current_terms)

        response = self.client.get(reverse("seshat-methods"))

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'id="termsModal"')

    def test_public_api_access_remains_unchanged(self):
        response = self.client.get("/api/")

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'id="termsModal"')

    def test_download_redirects_to_homepage_modal_until_terms_are_accepted(self):
        response = self.client.get(reverse("seshat-olddownloads"))

        self.assertRedirects(
            response,
            reverse("seshat-index"),
            fetch_redirect_response=False,
        )
        homepage = self.client.get(reverse("seshat-index"))
        self.assertContains(homepage, 'id="termsModal"')

    def test_external_next_url_is_rejected(self):
        response = self.client.post(
            reverse("terms_accept"),
            {"next": "https://example.com/phishing"},
        )

        self.assertRedirects(response, "/", fetch_redirect_response=False)
