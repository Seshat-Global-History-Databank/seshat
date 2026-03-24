import csv
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from seshat.apps.core.models import Polity, SeshatPrivateComment
from seshat.apps.crisisdb.models import Instability_event, Instability_ref, Instability_type


TYPE_MAP = {
    "Execution (contextually framed as a consequence of rebellion)": "Execution",
    "Execution (linked to military failure/revolt)": "Execution",
    "Political disturbance (non-violent)": "Political Disturbance",
    "Coup d’état (de facto political takeover)": "Coup d’état",
    "Coup d'etat": "Coup d’état",
}

REQUIRED_COLUMNS = {
    "Name",
    "Year",
    "Year_To",
    "Macro_Event",
    "Type",
    "Extent",
    "Intensity",
    "Reasoning",
    "Sources",
    "Evidence_Quote",
    "Evidence_File",
    "Evidence_Page",
    "Extent_Evidence_Quote",
    "Extent_Evidence_File",
    "Extent_Evidence_Page",
    "Intensity_Evidence_Quote",
    "Intensity_Evidence_File",
    "Intensity_Evidence_Page",
}


def normalize_type_name(type_name):
    cleaned = (type_name or "").strip()
    return TYPE_MAP.get(cleaned, cleaned)


def source_label(file_name, page):
    file_name = (file_name or "").strip()
    page = (page or "").strip()
    if file_name and page:
        return f"{file_name}:p{page}"
    if file_name:
        return file_name
    return None


def build_evidence_block(quote_label, source_label_text, quote, file_name, page):
    quote = (quote or "").strip()
    source_text = source_label(file_name, page)
    if not quote and not source_text:
        return None

    parts = []
    if quote:
        parts.append(f"{quote_label}:\n{quote}")
    if source_text:
        parts.append(f"{source_label_text}:\n{source_text}")
    return "\n\n".join(parts)


def parse_types(raw_value):
    return [
        normalize_type_name(part)
        for part in (raw_value or "").split(";")
        if part.strip()
    ]


def gather_refs(row):
    ref_names = []

    for raw_ref in (row.get("Sources") or "").split(";"):
        cleaned = raw_ref.strip()
        if cleaned:
            ref_names.append(cleaned)

    for extra_ref in [
        source_label(row.get("Evidence_File"), row.get("Evidence_Page")),
        source_label(row.get("Extent_Evidence_File"), row.get("Extent_Evidence_Page")),
        source_label(row.get("Intensity_Evidence_File"), row.get("Intensity_Evidence_Page")),
    ]:
        if extra_ref:
            ref_names.append(extra_ref)

    # Preserve order while deduplicating.
    return list(dict.fromkeys(ref_names))


class Command(BaseCommand):
    help = "Import instability events from a CSV file into the existing instability-event model."

    def add_arguments(self, parser):
        parser.add_argument("--csv", required=True, help="Absolute or relative path to the CSV file.")
        parser.add_argument("--polity", required=True, help="Polity.new_name to attach to every imported event.")
        parser.add_argument(
            "--limit",
            type=int,
            default=None,
            help="Only import the first N rows from the CSV.",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Parse and validate rows but do not write anything to the database.",
        )

    def handle(self, *args, **options):
        csv_path = Path(options["csv"]).expanduser()
        if not csv_path.exists():
            raise CommandError(f"CSV file not found: {csv_path}")

        polity_name = options["polity"]
        limit = options["limit"]
        dry_run = options["dry_run"]

        try:
            polity = Polity.objects.get(new_name=polity_name)
        except Polity.DoesNotExist as exc:
            raise CommandError(f"Polity not found for new_name='{polity_name}'") from exc

        with csv_path.open(newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            fieldnames = set(reader.fieldnames or [])
            missing_columns = sorted(REQUIRED_COLUMNS - fieldnames)
            if missing_columns:
                raise CommandError(
                    "CSV is missing required columns: " + ", ".join(missing_columns)
                )

            created_count = 0
            processed_count = 0

            for row_index, row in enumerate(reader, start=1):
                if limit is not None and processed_count >= limit:
                    break

                name = (row.get("Name") or "").strip()
                year_from_raw = (row.get("Year") or "").strip()
                year_to_raw = (row.get("Year_To") or "").strip()
                macro_event = (row.get("Macro_Event") or "").strip()
                reasoning = (row.get("Reasoning") or "").strip() or None

                if not name or not year_from_raw:
                    raise CommandError(
                        f"Row {row_index}: missing required Name or Year value."
                    )

                try:
                    year_from = int(year_from_raw)
                    year_to = int(year_to_raw) if year_to_raw else None
                except ValueError as exc:
                    raise CommandError(
                        f"Row {row_index}: bad year value(s) '{year_from_raw}' / '{year_to_raw}'."
                    ) from exc

                inst_type_names = parse_types(row.get("Type"))
                llm_name = f"{name} (Macro Event: {macro_event})" if macro_event else name
                llm_inst_type = "; ".join(inst_type_names) if inst_type_names else None

                general_evidence = build_evidence_block(
                    "Evidence Quote",
                    "Evidence Source",
                    row.get("Evidence_Quote"),
                    row.get("Evidence_File"),
                    row.get("Evidence_Page"),
                )
                classification_cot = build_evidence_block(
                    "Extent Evidence Quote",
                    "Extent Evidence Source",
                    row.get("Extent_Evidence_Quote"),
                    row.get("Extent_Evidence_File"),
                    row.get("Extent_Evidence_Page"),
                )
                intensity_evidence = build_evidence_block(
                    "Intensity Evidence Quote",
                    "Intensity Evidence Source",
                    row.get("Intensity_Evidence_Quote"),
                    row.get("Intensity_Evidence_File"),
                    row.get("Intensity_Evidence_Page"),
                )
                ref_names = gather_refs(row)

                if dry_run:
                    created_count += 1
                    processed_count += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Dry run ok for row {row_index}: {name} ({year_from}-{year_to})"
                        )
                    )
                    continue

                with transaction.atomic():
                    private_comment = SeshatPrivateComment.objects.create()
                    event = Instability_event.objects.create(
                        name=name,
                        llm_name=llm_name,
                        polity=polity,
                        year_from=year_from,
                        year_to=year_to,
                        llm_year_from=year_from,
                        llm_year_to=year_to,
                        llm_description=reasoning,
                        inst_extent=row.get("Extent") or None,
                        inst_intensity=row.get("Intensity") or None,
                        llm_inst_extent=row.get("Extent") or None,
                        llm_inst_intensity=row.get("Intensity") or None,
                        general_cot=intensity_evidence,
                        classification_cot=classification_cot,
                        sorokin_rationale=general_evidence,
                        real_event_check=None,
                        llm_real_event_check=None,
                        llm_inst_type=llm_inst_type,
                        private_comment=private_comment,
                    )

                    instability_types = [
                        Instability_type.objects.get_or_create(name=type_name)[0]
                        for type_name in inst_type_names
                    ]
                    instability_refs = [
                        Instability_ref.objects.get_or_create(name=ref_name, is_real=False)[0]
                        for ref_name in ref_names
                    ]

                    event.inst_type.set(instability_types)
                    event.inst_llm_ref.set(instability_refs)

                created_count += 1
                processed_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Imported row {row_index}: {name} ({year_from}-{year_to})"
                    )
                )

        summary = (
            f"Finished CSV import for polity '{polity_name}'. "
            f"Created: {created_count}."
        )
        self.stdout.write(self.style.SUCCESS(summary))
