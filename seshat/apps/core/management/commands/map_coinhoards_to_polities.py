from collections import defaultdict

from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from django.db import transaction

from seshat.apps.core.models import (
    Cliopatria,
    CoinHoard,
    CoinHoardPolityMapping,
    Polity,
)


def normalize_range(start, end):
    if start is None and end is None:
        return None, None
    if start is None:
        start = end
    if end is None:
        end = start
    return (start, end) if start <= end else (end, start)


def coin_hoard_temporal_anchor(coin_hoard):
    if coin_hoard.deposit_year_from is not None:
        return coin_hoard.deposit_year_from, "deposit"
    if coin_hoard.deposit_year_to is not None:
        return coin_hoard.deposit_year_to, "deposit"
    if coin_hoard.year_from is not None:
        return coin_hoard.year_from, "terminal_fallback"
    if coin_hoard.year_to is not None:
        return coin_hoard.year_to, "terminal_fallback"
    return None, ""


def map_coinhoard_to_polities(coin_hoard, polities_by_seshat_id):
    """
    Return CoinHoardPolityMapping rows for one CoinHoard.
    Mapping criteria:
    1) hoard has a point (lon/lat),
    2) deposit anchor year exists, falling back to terminal chronology when
       deposit chronology is unavailable,
    3) Cliopatria polygon contains the point,
    4) anchor year falls within Cliopatria shape year range and Polity year range.
    """
    if coin_hoard.latitude is None or coin_hoard.longitude is None:
        return []

    anchor_year, match_basis = coin_hoard_temporal_anchor(coin_hoard)
    if anchor_year is None:
        return []

    point = Point(float(coin_hoard.longitude), float(coin_hoard.latitude), srid=4326)
    candidate_shapes = Cliopatria.objects.filter(
        geom__contains=point,
        start_year__lte=anchor_year,
        end_year__gte=anchor_year,
    ).only("id", "seshat_id", "start_year", "end_year").order_by("id")

    mappings = []
    matched_polity_ids = set()
    for shape in candidate_shapes:
        candidate_polities = polities_by_seshat_id.get(shape.seshat_id, [])
        for polity in candidate_polities:
            if polity.id in matched_polity_ids:
                continue

            polity_start, polity_end = normalize_range(polity.start_year, polity.end_year)
            if polity_start is None:
                continue
            if not (polity_start <= anchor_year <= polity_end):
                continue

            if not (shape.start_year <= anchor_year <= shape.end_year):
                continue

            mappings.append(
                CoinHoardPolityMapping(
                    coin_hoard=coin_hoard,
                    polity=polity,
                    cliopatria_shape=shape,
                    overlap_year_from=anchor_year,
                    overlap_year_to=anchor_year,
                    temporal_match_basis=match_basis,
                )
            )
            matched_polity_ids.add(polity.id)

    return mappings


class Command(BaseCommand):
    help = "Map CoinHoard records to Polities using Cliopatria geometry + year overlap."

    def add_arguments(self, parser):
        parser.add_argument(
            "--hoard-id",
            help="Optional external_dataset_id of one hoard to map (e.g. CHRE04630).",
        )
        parser.add_argument("--limit", type=int, help="Optional max number of hoards to process.")
        parser.add_argument(
            "--keep-existing",
            action="store_true",
            help="Keep previous mappings instead of replacing mappings for processed hoards.",
        )

    def handle(self, *args, **options):
        hoard_id = options.get("hoard_id")
        limit = options.get("limit")
        keep_existing = options.get("keep_existing", False)

        polities_by_seshat_id = defaultdict(list)
        for polity in Polity.objects.exclude(new_name__isnull=True).exclude(new_name__exact=""):
            polities_by_seshat_id[polity.new_name].append(polity)

        hoards = CoinHoard.objects.all().order_by("external_dataset_id")
        if hoard_id:
            hoards = hoards.filter(external_dataset_id=hoard_id)
        if limit:
            hoards = hoards[:limit]

        hoards = list(hoards)
        processed_ids = [h.id for h in hoards]
        if not hoards:
            self.stdout.write(self.style.WARNING("No matching hoards found to process."))
            return

        all_mappings = []
        mapped_hoards = 0
        for hoard in hoards:
            mappings = map_coinhoard_to_polities(hoard, polities_by_seshat_id)
            if mappings:
                mapped_hoards += 1
                all_mappings.extend(mappings)

        with transaction.atomic():
            if not keep_existing:
                CoinHoardPolityMapping.objects.filter(coin_hoard_id__in=processed_ids).delete()
            if all_mappings:
                CoinHoardPolityMapping.objects.bulk_create(all_mappings, ignore_conflicts=True)

        self.stdout.write(self.style.SUCCESS("Coinhoard-to-polity mapping completed."))
        self.stdout.write(f"Hoard records processed: {len(hoards)}")
        self.stdout.write(f"Hoard records mapped: {mapped_hoards}")
        self.stdout.write(f"Mapping rows created: {len(all_mappings)}")
