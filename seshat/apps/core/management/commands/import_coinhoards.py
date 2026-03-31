import csv
import re
from decimal import Decimal, InvalidOperation

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Max

from seshat.apps.core.models import CoinHoard


NULL_LIKE = {"", "not available", "n/a", "none", "null", "unknown"}
DEFAULT_SOURCE = "Coin Hoards of the Roman Empire"


def normalize_str(value):
    if value is None:
        return ""
    value = value.strip()
    if value.lower() in NULL_LIKE:
        return ""
    return value


def parse_int(value):
    value = normalize_str(value)
    if not value:
        return None
    try:
        return int(float(value))
    except ValueError:
        return None


def parse_decimal(value):
    value = normalize_str(value)
    if not value:
        return None
    try:
        return Decimal(value)
    except (InvalidOperation, ValueError):
        return None


def normalize_external_url(value):
    raw = normalize_str(value)
    if not raw:
        return ""
    first = raw.split(";")[0].strip()
    if first.startswith("http://") or first.startswith("https://"):
        return first
    return ""


def make_external_dataset_id(raw_id):
    parsed = parse_int(raw_id)
    if parsed is None:
        return None
    return f"CHRE{parsed:05d}"


def choose_region(row):
    return normalize_str(row.get("county")) or normalize_str(row.get("region")) or normalize_str(row.get("province"))


def next_seshat_id(existing_max):
    if not existing_max:
        return 1
    match = re.match(r"^(\d{1,6})$", existing_max)
    if not match:
        return 1
    return int(match.group(1)) + 1


class Command(BaseCommand):
    help = "Import CHRE CSV into core.CoinHoard"

    def add_arguments(self, parser):
        parser.add_argument("--csv", required=True, help="Path to CHRE CSV file")
        parser.add_argument("--chunk-size", type=int, default=2000, help="Bulk operation chunk size")

    def handle(self, *args, **options):
        csv_path = options["csv"]
        chunk_size = options["chunk_size"]

        try:
            with open(csv_path, newline="", encoding="utf-8-sig") as handle:
                rows = list(csv.DictReader(handle))
        except FileNotFoundError as exc:
            raise CommandError(f"CSV not found: {csv_path}") from exc

        normalized = []
        for row in rows:
            ext_id = make_external_dataset_id(row.get("id"))
            if ext_id:
                normalized.append((row, ext_id))

        existing = {
            obj.external_dataset_id: obj
            for obj in CoinHoard.objects.filter(external_dataset_id__in=[ext for _, ext in normalized])
        }
        seshat_counter = next_seshat_id(CoinHoard.objects.aggregate(mx=Max("seshat_id")).get("mx"))

        to_create = []
        to_update = []

        for row, ext_id in normalized:
            payload = {
                "external_dataset_id": ext_id,
                "raw_external_id": normalize_str(row.get("id")),
                "data_source": DEFAULT_SOURCE,
                "hoard_name": normalize_str(row.get("hoardName")),
                "number_of_coins": parse_int(row.get("coinCount")),
                "year_from": parse_int(row.get("terminalYear1")),
                "year_to": parse_int(row.get("terminalYear2")),
                "latitude": parse_decimal(row.get("latitude")),
                "longitude": parse_decimal(row.get("longitude")),
                "region": choose_region(row),
                "country": normalize_str(row.get("country")),
                "external_url": normalize_external_url(row.get("permalinkOnlineDatabases")),
            }

            obj = existing.get(ext_id)
            if obj is None:
                payload["seshat_id"] = f"{seshat_counter:06d}"
                seshat_counter += 1
                to_create.append(CoinHoard(**payload))
                continue

            changed = False
            for field, value in payload.items():
                if getattr(obj, field) != value:
                    setattr(obj, field, value)
                    changed = True
            if changed:
                to_update.append(obj)

        update_fields = [
            "raw_external_id",
            "data_source",
            "hoard_name",
            "number_of_coins",
            "year_from",
            "year_to",
            "latitude",
            "longitude",
            "region",
            "country",
            "external_url",
            "updated_at",
        ]

        with transaction.atomic():
            if to_create:
                CoinHoard.objects.bulk_create(to_create, batch_size=chunk_size)
            if to_update:
                CoinHoard.objects.bulk_update(to_update, update_fields, batch_size=chunk_size)

        self.stdout.write(self.style.SUCCESS("Coinhoard import completed"))
        self.stdout.write(f"Total rows: {len(rows)}")
        self.stdout.write(f"Parsed rows: {len(normalized)}")
        self.stdout.write(f"Created: {len(to_create)}")
        self.stdout.write(f"Updated: {len(to_update)}")
