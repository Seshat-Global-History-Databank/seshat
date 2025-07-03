from django.core.management.base import BaseCommand
from django.test import Client
from seshat.apps.core.models import Variablehierarchy, Section

from django.utils.text import slugify

import inflect
import requests

p = inflect.engine()

class Command(BaseCommand):
    help = "Check if all VariableHierarchy names correspond to valid API endpoints using Django test client."

    def handle(self, *args, **options):
        client = Client()
        base_url = "/api/"
        failed = []
        failed_dic = {}
        passed_dic = {}

        for vh in Variablehierarchy.objects.all():
            section = vh.section
            if not section or not section.db_table_name:
                continue

            slug_name = slugify(vh.name)
            plural_slug = p.plural(slug_name)

            endpoint = f"/api/{section.db_table_name}/{plural_slug}/"
            full_url = f"{base_url}{endpoint}"


            response = client.get(full_url)
            if response.status_code == 200:
                self.stdout.write(self.style.SUCCESS(f"[OK] {full_url}"))
                passed_dic[vh.name] = endpoint
            else:
                failed.append((full_url, response.status_code))
                self.stdout.write(self.style.WARNING(f"[FAIL] {full_url} (Status: {response.status_code})"))
                failed_dic[vh.name] = endpoint

        if failed:
            self.stdout.write(self.style.ERROR(f"\n❌ {len(failed)} endpoint(s) failed:"))
            for url, status in failed:
                self.stdout.write(f"  - {url} (Status: {status})")
        else:
            self.stdout.write(self.style.SUCCESS("\n✅ All endpoints are valid."))

        # print('####### PASSED ####')
        # print(passed_dic)
        # print('###################')
        # print('####### Failed ####')
        # print(failed_dic)
        # print('###################')
