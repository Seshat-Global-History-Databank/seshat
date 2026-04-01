"""
Import CHRE coin hoard CSV rows into ``core.CoinHoard``.

Django management command name (from this filename): ``import_coinhoards``.

Integration steps (run from the directory that contains ``manage.py``, e.g.
``.../seshat``):

1. **Apply database migrations** so ``CoinHoard`` and related fields exist::

       python manage.py migrate

   To see pending migrations without applying::

       python manage.py showmigrations core

2. **Import the CHRE export CSV** (UTF-8 with BOM is fine; the importer uses
   ``utf-8-sig``). Example::

       python manage.py import_coinhoards \\
           --csv "/path/to/CHRE_hoard_export_YYYY_MM_DD.csv" \\
          

   Optional: adjust batch size (default 2000)::

       python manage.py import_coinhoards \\
           --csv "/path/to/your.csv" \\
           --chunk-size 2000 \\
          

3. **Re-runs are safe**: rows are keyed by ``external_dataset_id`` (e.g.
   ``CHRE04630`` from CSV ``id``). Existing rows are updated; new rows are
   created and ``seshat_id`` is assigned for new records only.

4. **Quick sanity check** (optional)::

       python manage.py shell -c \\
           "from seshat.apps.core.models import CoinHoard; print(CoinHoard.objects.count())"

**CSV expectations**: columns such as ``id``, ``hoardName``, ``coinCount``,
``terminalYear1``/``terminalYear2``, ``openingYear1``/``openingYear2``,
``discoveryYear1``/``discoveryYear2``, ``permalinkOnlineDatabases`` (mixed text
and URLs), coordinates, etc., as produced by the CHRE export.

**UI**: list at ``/core/coinhoards/`` (name ``coinhoards``); canonical CHRE
permalink for a hoard is built in views as
``https://chre.ashmus.ox.ac.uk/hoard/<raw id>`` (see CHRE site structure, e.g.
https://chre.ashmus.ox.ac.uk/hoard/4630).

**Troubleshooting**: If Postgres raises ``value too long for type character
varying(N)``, some CSV cell exceeds a column limit. Run ``migrate`` after pulling
``CoinHoard`` field changes (e.g. ``external_source_text`` as ``TextField``).
The importer also clips bounded string fields to their model limits.
"""
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


def clip_str(value, max_len):
    """Keep values within CharField / URLField limits (CSV rows can exceed them)."""
    s = normalize_str(value)
    if max_len <= 0:
        return ""
    return s[:max_len]


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


def parse_external_source(value):
    raw = normalize_str(value)
    if not raw:
        return "", ""

    url_match = re.search(r"https?://\S+", raw)
    if not url_match:
        return raw, ""

    url = url_match.group(0).rstrip(").,;")
    left = raw[: url_match.start()].strip()
    right = raw[url_match.end() :].strip()
    source_text = left or right
    if source_text.endswith(":"):
        source_text = source_text[:-1].strip()
    return source_text, url


def make_external_dataset_id(raw_id):
    parsed = parse_int(raw_id)
    if parsed is None:
        return None
    return f"CHRE{parsed:05d}"


def choose_region(row):
    return normalize_str(row.get("county")) or normalize_str(row.get("region")) or normalize_str(row.get("province"))


def normalize_choice(value, allowed_values):
    value = normalize_str(value)
    return value if value in allowed_values else ""


def next_seshat_id(existing_max):
    if not existing_max:
        return 1
    match = re.match(r"^(\d{1,6})$", existing_max)
    if not match:
        return 1
    return int(match.group(1)) + 1


class Command(BaseCommand):
    help = "Import CHRE CSV into core.CoinHoard. See module docstring for migrate + import commands."

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
            external_source_text, external_url = parse_external_source(
                row.get("permalinkOnlineDatabases")
            )
            payload = {
                "external_dataset_id": ext_id,
                "raw_external_id": normalize_str(row.get("id")),
                "data_source": DEFAULT_SOURCE,
                "hoard_name": normalize_str(row.get("hoardName")),
                "number_of_coins": parse_int(row.get("coinCount")),
                "discovery_method": normalize_choice(
                    row.get("discoveryMethod"),
                    {choice[0] for choice in CoinHoard.DISCOVERY_METHOD_CHOICES},
                ),
                "discovery_year1": parse_int(row.get("discoveryYear1")),
                "discovery_year2": parse_int(row.get("discoveryYear2")),
                "opening_year1": parse_int(row.get("openingYear1")),
                "opening_year2": parse_int(row.get("openingYear2")),
                "year_from": parse_int(row.get("terminalYear1")),
                "year_to": parse_int(row.get("terminalYear2")),
                "find_spot_rating": normalize_choice(
                    row.get("findSpotRating"), {choice[0] for choice in CoinHoard.RATING_CHOICES}
                ),
                "contextual_rating": normalize_choice(
                    row.get("contextualRating"), {choice[0] for choice in CoinHoard.RATING_CHOICES}
                ),
                "numismatic_rating": normalize_choice(
                    row.get("numismaticRating"), {choice[0] for choice in CoinHoard.RATING_CHOICES}
                ),
                "latitude": parse_decimal(row.get("latitude")),
                "longitude": parse_decimal(row.get("longitude")),
                "altitude": parse_decimal(row.get("altitude")),
                "city": clip_str(row.get("city"), 255),
                "county": clip_str(row.get("county"), 255),
                "region": clip_str(choose_region(row), 255),
                "country": clip_str(row.get("country"), 255),
                "summary": normalize_str(row.get("summary")),
                "external_source_text": external_source_text,
                "external_url": clip_str(external_url, 500),
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
            "discovery_method",
            "discovery_year1",
            "discovery_year2",
            "opening_year1",
            "opening_year2",
            "year_from",
            "year_to",
            "find_spot_rating",
            "contextual_rating",
            "numismatic_rating",
            "latitude",
            "longitude",
            "altitude",
            "city",
            "county",
            "region",
            "country",
            "summary",
            "external_source_text",
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
