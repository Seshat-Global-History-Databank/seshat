from django.db import migrations


AGREEMENT_SLUG = "seshat-user-agreement-2026-07-14-cc-by-sa-4-0"
AGREEMENT_TITLE = "Seshat Databank — User Agreement"
AGREEMENT_BODY_HTML = """
<div style="font-size:12px">
  <h4>Seshat Databank — User Agreement</h4>

  <h5>1) Introduction</h5>
  <p>By using the Seshat Databank (“<strong>Seshat</strong>,” “<strong>we</strong>,” “<strong>us</strong>”), you (“<strong>User</strong>”) agree to this User Agreement. If you do not agree, do not create an account, download data, or use the API.</p>

  <h5>2) Scope &amp; Definitions</h5>
  <ul>
    <li><strong>Public Data:</strong> Datasets released in connection with Seshat publications or curated public releases.</li>
    <li><strong>Private Data:</strong> Work-in-progress datasets under review/cleaning or otherwise not publicly released.</li>
    <li><strong>Download Formats:</strong> CSV and JSON files available from the website or programmatic endpoints.</li>
    <li><strong>Current Terms:</strong> The active Terms &amp; Conditions version shown on the site.</li>
  </ul>

  <h5>3) Access &amp; Accounts</h5>
  <ul>
    <li><strong>Browse without an account:</strong> You may browse public pages without signing in.</li>
    <li><strong>Account required to download:</strong> To download Public Data (CSV/JSON), you must create a free account and consent to the Current Terms.</li>
    <li><strong>Google sign-in:</strong> If you sign in with Google (or any SSO), you must accept the Current Terms on your first logged-in visit before continuing.</li>
    <li><strong>Existing users:</strong> If you have an account but have not accepted the Current Terms, you will be prompted to accept them before continuing (excluding the landing page and API).</li>
  </ul>

  <h5>4) Consent, Logging, and Re-consent</h5>
  <ul>
    <li><strong>Consent record:</strong> When you accept the Terms, we log the terms version, timestamp, IP address, and user agent for audit.</li>
    <li><strong>One-time per version:</strong> You won’t be prompted again for the same version.</li>
    <li><strong>When terms change:</strong> If we publish new terms, you’ll be prompted to accept the new version on your next visit before continuing (and before any download).</li>
  </ul>

  <h5>5) Data Categories &amp; Restrictions</h5>
  <ul>
    <li><strong>Public Data:</strong> Can be viewed by anyone and downloaded by registered users who have accepted the Terms. Licensed under the <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license">Creative Commons Attribution–ShareAlike 4.0 International License (CC BY-SA 4.0)</a>.</li>
    <li><strong>Private Data:</strong> May be visible in parts of the interface for transparency to collaborators but is <strong>not downloadable</strong> and must <strong>not</strong> be shared or published. You may submit feedback and sources via private comments where available.</li>
  </ul>

  <h5>6) License (Public Data)</h5>
  <p>Public Data is provided under <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license"><strong>CC BY-SA 4.0</strong></a>: you may share and adapt the Public Data, including for commercial purposes, provided that you give appropriate attribution, include a link to the license, and indicate whether changes were made. If you remix, transform, or build upon the Public Data, you must distribute your contributions under the same license or a license that Creative Commons has declared compatible.</p>
  <p><strong>Required citation text in publications (example):</strong></p>
  <blockquote>
    This research used data from the Seshat Databank (https://seshat-db.com) under the Creative Commons Attribution–ShareAlike 4.0 International License (CC BY-SA 4.0): https://creativecommons.org/licenses/by-sa/4.0/.
  </blockquote>

  <p><strong>Reference (example):</strong></p>
  <ul>
    <li>
      Benam, M. et al. (2022). <em>Seshat Data: Equinox Packaged Data (1.0)</em> [Data set]. Zenodo.
      <a href="https://doi.org/10.5281/zenodo.6642229">https://doi.org/10.5281/zenodo.6642229</a><br>
      (For replication datasets tied to articles, see <a href="https://seshat-db.com/downloads_page/">https://seshat-db.com/downloads_page/</a>.)
    </li>
  </ul>

  <h5>7) API Access</h5>
  <ul>
    <li><strong>Agreement applies:</strong> Use of any programmatic endpoints constitutes acceptance of the Current Terms.</li>
    <li><strong>Authentication:</strong> We may require API tokens and verified accounts; only users who have accepted the Current Terms will receive/retain access.</li>
    <li><strong>Rate limits &amp; suspension:</strong> We may limit, suspend, or revoke API access to protect the service or enforce this Agreement.</li>
  </ul>

  <h5>8) Prohibited Uses</h5>
  <ul>
    <li>Share, publish, or redistribute <strong>Private Data</strong>.</li>
    <li>Use Public Data without complying with the <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license">CC BY-SA 4.0 license terms</a>.</li>
    <li>Remove or obscure attribution/license notices.</li>
    <li>Misrepresent Seshat data, or attempt to re-identify sensitive information contrary to ethical guidelines.</li>
  </ul>

  <h5>9) Accuracy &amp; Feedback</h5>
  <p>Seshat strives for accuracy but provides data “as is.” We welcome corrections and sources via the private comment features where available.</p>

  <h5>10) Attribution</h5>
  <p>Whenever you use or refer to Seshat Public Data, you must provide clear attribution as outlined in Section 6.</p>

  <h5>11) Changes to this Agreement</h5>
  <p>We may update these terms. <strong>Material changes</strong> will require <strong>re-consent</strong> on your next visit before you can continue or download.</p>
</div>
""".strip()


def publish_cc_by_sa_agreement(apps, schema_editor):
    TermsVersion = apps.get_model("accounts", "TermsVersion")

    TermsVersion.objects.filter(is_active=True).exclude(slug=AGREEMENT_SLUG).update(
        is_active=False
    )
    TermsVersion.objects.update_or_create(
        slug=AGREEMENT_SLUG,
        defaults={
            "title": AGREEMENT_TITLE,
            "body_html": AGREEMENT_BODY_HTML,
            "is_active": True,
        },
    )


def restore_previous_agreement(apps, schema_editor):
    TermsVersion = apps.get_model("accounts", "TermsVersion")

    TermsVersion.objects.filter(slug=AGREEMENT_SLUG).update(is_active=False)
    previous = (
        TermsVersion.objects.exclude(slug=AGREEMENT_SLUG)
        .order_by("-published_at")
        .first()
    )
    if previous:
        previous.is_active = True
        previous.save(update_fields=["is_active"])


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0016_termsversion_termsacceptance"),
    ]

    operations = [
        migrations.RunPython(
            publish_cc_by_sa_agreement,
            reverse_code=restore_previous_agreement,
        ),
    ]
