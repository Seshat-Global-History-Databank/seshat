from django.core.management.base import BaseCommand
from django.urls import reverse, resolve
from django.conf import settings
from seshat.apps.core.models import Variablehierarchy, Section
from django.utils.text import slugify
import inflect
import requests

p = inflect.engine()


class Command(BaseCommand):
    help = "Check if all Variablehierarchy names can be used to generate valid API endpoints."

    def handle(self, *args, **kwargs):
        base_url = getattr(settings, 'BASE_URL', 'http://127.0.0.1:8000')
        failed = []
        failed_dic = {}
        passed_dic = {}

        for vh in Variablehierarchy.objects.all():
            section: Section = vh.section
            if not section or not section.db_table_name:
                self.stdout.write(self.style.WARNING(f"Skipping variable '{vh.name}' (no section)."))
                continue

            slug_name = slugify(vh.name)
            majid_name = vh.name.lower().replace(' ', '-')
            plural_slug = p.plural(slug_name)
            majid_plural = majid_name + "s"

            endpoint = f"/api/{section.db_table_name}/{plural_slug}/"
            full_url = f"{base_url}{endpoint}"

            endpoint2 = f"/api/{section.db_table_name}/{majid_plural}/"
            full_url2 = f"{base_url}{endpoint2}"
            #print(full_url2)

            endpoint3 = f"/api/{section.db_table_name}/{majid_name}/"
            full_url3 = f"{base_url}{endpoint3}"
            #print(full_url2)

            mapped_names = {
                'Leather Cloth': '/api/wf/leathers/',
                'Small Vessels Canoes Etc': '/api/wf/small-vessel-canoe-etc/',
                'Merchant Ships Pressed Into Service': '/api/wf/merchant-ship-pressed-into-service/',
                'Settlements In A Defensive Position': '/api/wf/settlement-in-defensive-positions/',
                'Drinking Water Supply System': '/api/sc/drinking-water-supplies/',
                'Government Restrictions On Property Ownership For Adherents Of Any Religious Group': '/api/rt/government-restrictions-on-property-ownership-for-adherents-of-any-religious-groups/',
                'Polity Utm Zone': '/api/general/polity-utm-timezones/',
                'Fine Ceramic Wares': '/api/ec/lux-fine-ceramic-wares/',
                'Polity Suprapolity Relations': '/api/general/polity-suprapolities/',
                #'Polity Relationship To Preceding Entity': '/api/general/polity relationships-to-preceding entity/',
                'Precious Metal': '/api/ec/lux-precious-metal/',
                'Luxury Drink/Alcohol': '/api/ec/luxury-drink-alcohol/',
                'Precious Stone': '/api/ec/lux-precious-stone/',
                'Statuary': '/api/ec/lux-statuary/',
                'Human Sacrifice': '/api/rt/human-sacrifices/',
            }

            if vh.name in mapped_names:
                endpoint = f"{mapped_names[vh.name]}"
                full_url = f"{base_url}{endpoint}"


            try:
                response = requests.get(full_url)
                response2 = requests.get(full_url2)
                response3 = requests.get(full_url3)
                if response.status_code == 200:
                    self.stdout.write(self.style.SUCCESS(f"✓ {full_url} exists"))
                    passed_dic[vh.name] = endpoint
                elif response2.status_code == 200:
                    self.stdout.write(self.style.SUCCESS(f"✓✓ {full_url2} exists"))
                    passed_dic[vh.name] = endpoint2
                elif response3.status_code == 200:
                    self.stdout.write(self.style.SUCCESS(f"✓✓✓ {full_url3} exists"))
                    passed_dic[vh.name] = endpoint3
                else:
                    self.stdout.write(self.style.ERROR(f"✗ {full_url} returned {response.status_code}"))
                    failed.append((vh.id, vh.name, full_url))
                    failed_dic[vh.name] = endpoint
            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"✗ Failed to access {full_url}: {e}"))
                failed.append((vh.id, vh.name, full_url))

        self.stdout.write("\nSummary:")
        if failed:
            self.stdout.write(self.style.ERROR(f"{len(failed)} endpoints failed:"))
            for fid, fname, furl in failed:
                self.stdout.write(f"  [{fid}] {fname} → {furl}")
        else:
            self.stdout.write(self.style.SUCCESS("All endpoints are valid."))

        print('####### PASSED ####')
        print(passed_dic)
        print('###################')
        print('####### Failed ####')
        print(failed_dic)
        print('###################')