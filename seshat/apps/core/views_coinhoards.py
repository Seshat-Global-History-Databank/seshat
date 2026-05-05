import csv
from datetime import datetime
from decimal import Decimal
from io import StringIO

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Prefetch, Q, prefetch_related_objects
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import CoinHoard, CoinHoardPolityMapping, Polity

CHRE_BASE_URL = "https://chre.ashmus.ox.ac.uk/hoard/"
RATING_MAP = {
    "1": ("poor", "rating-poor"),
    "2": ("fair", "rating-fair"),
    "3": ("good", "rating-good"),
    "4": ("excellent", "rating-excellent"),
}


def _rating_meta(value):
    return RATING_MAP.get(str(value or "").strip(), ("-", "rating-empty"))


def _chre_url(hoard):
    raw_id = str(hoard.raw_external_id or "").strip()
    if raw_id.isdigit():
        return f"{CHRE_BASE_URL}{int(raw_id)}"

    ext = str(hoard.external_dataset_id or "").strip().upper()
    if ext.startswith("CHRE") and ext[4:].isdigit():
        return f"{CHRE_BASE_URL}{int(ext[4:])}"
    return ""


COINHOARD_CSV_COLUMN_GROUPS = (
    (
        "Identification",
        (
            ("external_dataset_id", "External dataset ID"),
            ("seshat_id", "Seshat ID"),
            ("raw_external_id", "Raw external ID"),
            ("hoard_name", "Hoard name"),
            ("number_of_coins", "Number of coins"),
            ("data_source", "Data source"),
        ),
    ),
    (
        "Location",
        (
            ("mapped_polities", "Mapped polities (new_name)"),
            ("city", "City"),
            ("county", "County"),
            ("region", "Region"),
            ("country", "Country"),
            ("latitude", "Latitude"),
            ("longitude", "Longitude"),
            ("altitude", "Altitude"),
        ),
    ),
    (
        "Years",
        (
            ("year_from", "Terminal year (from)"),
            ("year_to", "Terminal year (to)"),
            ("opening_year1", "Opening year (from)"),
            ("opening_year2", "Opening year (to)"),
            ("discovery_year1", "Discovery year (from)"),
            ("discovery_year2", "Discovery year (to)"),
        ),
    ),
    (
        "Discovery context",
        (("discovery_method", "Discovery method"),),
    ),
    (
        "Ratings",
        (
            ("find_spot_rating", "Find spot rating"),
            ("contextual_rating", "Contextual rating"),
            ("numismatic_rating", "Numismatic rating"),
        ),
    ),
    (
        "Narrative & links",
        (
            ("summary", "Summary"),
            ("external_source_text", "External source text"),
            ("external_url", "External URL"),
            ("chre_url", "CHRE URL"),
        ),
    ),
    (
        "Record metadata",
        (
            ("created_at", "Created at"),
            ("updated_at", "Updated at"),
        ),
    ),
)

COINHOARD_CSV_COLUMNS = tuple(col for _title, cols in COINHOARD_CSV_COLUMN_GROUPS for col in cols)

COINHOARD_CSV_ALLOWED = frozenset(k for k, _ in COINHOARD_CSV_COLUMNS)
COINHOARD_CSV_LABEL_BY_KEY = dict(COINHOARD_CSV_COLUMNS)

COINHOARD_CSV_DELIMITERS = {
    "comma": ",",
    "semicolon": ";",
    "tab": "\t",
    "pipe": "|",
}

def _coinhoard_mapped_polity_label(polity):
    base = (polity.long_name or polity.name or "").strip() or "-"
    nn = (polity.new_name or "").strip()
    return f"{base} ({nn})" if nn else base


def _coinhoard_mapped_polity_choices():
    polities = (
        Polity.objects.filter(coinhoard_mappings__isnull=False)
        .distinct()
        .order_by("long_name", "name")
        .only("id", "long_name", "name", "new_name")
    )
    return [{"id": p.id, "label": _coinhoard_mapped_polity_label(p)} for p in polities]


def _valid_selected_polity_ids(request):
    raw_ids = request.GET.getlist("polity")
    unique_ids = []
    seen = set()
    for raw in raw_ids:
        value = (raw or "").strip()
        if not value.isdigit() or value in seen:
            continue
        seen.add(value)
        unique_ids.append(value)
    return unique_ids


COINHOARD_CSV_DEFAULT_COLS = (
    "external_dataset_id",
    "hoard_name",
    "mapped_polities",
    "number_of_coins",
    "year_from",
    "year_to",
    "latitude",
    "longitude",
    "region",
    "country",
    "chre_url",
    "external_url",
)


def _filtered_coinhoard_queryset(request):
    q = request.GET.get("q", "").strip()
    start = request.GET.get("start_year", "").strip()
    end = request.GET.get("end_year", "").strip()

    queryset = CoinHoard.objects.all()

    if q:
        queryset = queryset.filter(
            Q(external_dataset_id__icontains=q)
            | Q(hoard_name__icontains=q)
            | Q(country__icontains=q)
        )

    try:
        if start:
            start_int = int(start)
            queryset = queryset.filter(Q(year_to__isnull=True) | Q(year_to__gte=start_int))
        if end:
            end_int = int(end)
            queryset = queryset.filter(Q(year_from__isnull=True) | Q(year_from__lte=end_int))
    except ValueError:
        pass

    selected_polity_ids = _valid_selected_polity_ids(request)
    if selected_polity_ids:
        queryset = queryset.filter(polity_mappings__polity_id__in=selected_polity_ids).distinct()

    return queryset, q, start, end, selected_polity_ids


def _mapped_polities_export_text(hoard):
    seen = set()
    parts = []
    for mapping in hoard.polity_mappings.all():
        polity = mapping.polity
        if polity.id in seen:
            continue
        seen.add(polity.id)
        new_name = (polity.new_name or "").strip()
        if new_name:
            parts.append(new_name)
    return " & ".join(parts)


def _coinhoard_csv_cell_value(hoard, key):
    if key == "chre_url":
        return _chre_url(hoard)
    if key == "mapped_polities":
        return _mapped_polities_export_text(hoard)
    value = getattr(hoard, key)
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Decimal):
        return format(value, "f").rstrip("0").rstrip(".") or "0"
    return str(value)


@login_required
def hoard_list(request):
    queryset, q, start, end, selected_polity_ids = _filtered_coinhoard_queryset(request)
    polity_options = _coinhoard_mapped_polity_choices()
    polity_label_by_id = {str(item["id"]): item["label"] for item in polity_options}
    selected_polity_items = [
        {"id": pid, "label": polity_label_by_id[pid]}
        for pid in selected_polity_ids
        if pid in polity_label_by_id
    ]
    selected_polity_labels = [item["label"] for item in selected_polity_items]

    paginator = Paginator(queryset, 50)
    page_obj = paginator.get_page(request.GET.get("page", 1))
    prefetch_related_objects(
        page_obj.object_list,
        Prefetch(
            "polity_mappings",
            queryset=CoinHoardPolityMapping.objects.select_related("polity").order_by(
                "polity__long_name", "polity__name"
            ),
        ),
    )

    for hoard in page_obj.object_list:
        hoard.findspot_label, hoard.findspot_class = _rating_meta(hoard.find_spot_rating)
        hoard.context_label, hoard.context_class = _rating_meta(hoard.contextual_rating)
        hoard.numismatic_label, hoard.numismatic_class = _rating_meta(hoard.numismatic_rating)
        hoard.chre_url = _chre_url(hoard)
        seen_polity_ids = set()
        hoard.mapped_polities = []
        for mapping in hoard.polity_mappings.all():
            polity = mapping.polity
            if polity.id in seen_polity_ids:
                continue
            seen_polity_ids.add(polity.id)
            display = (polity.long_name or polity.name or "").strip() or "-"
            new_name = (polity.new_name or "").strip()
            hoard.mapped_polities.append(
                {"display": display, "new_name": new_name, "polity_id": polity.id}
            )

    return render(
        request,
        "core/coinhoards/hoard_list.html",
        {
            "page_obj": page_obj,
            "q": q,
            "start_year": start,
            "end_year": end,
            "selected_polity_ids": selected_polity_ids,
            "selected_polity_items": selected_polity_items,
            "selected_polity_labels": selected_polity_labels,
            "coinhoard_polity_options": polity_options,
            "coinhoard_csv_column_groups": COINHOARD_CSV_COLUMN_GROUPS,
            "coinhoard_csv_default_cols": COINHOARD_CSV_DEFAULT_COLS,
        },
    )


@login_required
def hoard_export_csv(request):
    selected = {c for c in request.GET.getlist("col") if c in COINHOARD_CSV_ALLOWED}
    if not selected:
        return HttpResponseBadRequest("Select at least one column.")

    ordered_keys = [k for k, _ in COINHOARD_CSV_COLUMNS if k in selected]
    labels = [COINHOARD_CSV_LABEL_BY_KEY[k] for k in ordered_keys]

    delim_key = request.GET.get("delimiter", "pipe").strip().lower()
    delimiter = COINHOARD_CSV_DELIMITERS.get(delim_key)
    if delimiter is None:
        return HttpResponseBadRequest("Invalid delimiter.")

    queryset, *_ = _filtered_coinhoard_queryset(request)
    if "mapped_polities" in ordered_keys:
        queryset = queryset.prefetch_related(
            Prefetch(
                "polity_mappings",
                queryset=CoinHoardPolityMapping.objects.select_related("polity").order_by(
                    "polity__long_name", "polity__name"
                ),
            )
        )

    buf = StringIO()
    buf.write("\ufeff")
    writer = csv.writer(buf, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(labels)

    for hoard in queryset.order_by("external_dataset_id"):
        writer.writerow([_coinhoard_csv_cell_value(hoard, k) for k in ordered_keys])

    ts = timezone.now().strftime("%Y%m%d_%H%M%S")
    filename = f"coinhoards_export_{ts}.csv"
    response = HttpResponse(buf.getvalue(), content_type="text/csv; charset=utf-8")
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


@login_required
def hoard_detail(request, external_dataset_id):
    hoard = get_object_or_404(
        CoinHoard.objects.prefetch_related(
            Prefetch(
                "polity_mappings",
                queryset=CoinHoardPolityMapping.objects.select_related("polity", "cliopatria_shape").order_by(
                    "polity__long_name", "polity__name", "id"
                ),
            )
        ),
        external_dataset_id=external_dataset_id,
    )
    hoard.chre_url = _chre_url(hoard)
    hoard.findspot_label, hoard.findspot_class = _rating_meta(hoard.find_spot_rating)
    hoard.context_label, hoard.context_class = _rating_meta(hoard.contextual_rating)
    hoard.numismatic_label, hoard.numismatic_class = _rating_meta(hoard.numismatic_rating)
    hoard.polity_mapping_rows = []
    for mapping in hoard.polity_mappings.all():
        polity_name = (mapping.polity.long_name or mapping.polity.name or "").strip() or "-"
        shape_name = ""
        if mapping.cliopatria_shape_id and mapping.cliopatria_shape:
            shape_name = (mapping.cliopatria_shape.name or "").strip()
        hoard.polity_mapping_rows.append(
            {
                "polity_name": polity_name,
                "polity_new_name": (mapping.polity.new_name or "").strip(),
                "polity_id": mapping.polity_id,
                "polity_year_from": mapping.polity.start_year,
                "polity_year_to": mapping.polity.end_year,
                "overlap_year_from": mapping.overlap_year_from,
                "overlap_year_to": mapping.overlap_year_to,
                "shape_name": shape_name,
            }
        )
    return render(request, "core/coinhoards/hoard_detail.html", {"hoard": hoard})


@login_required
def hoard_list_json(request):
    rows = list(
        CoinHoard.objects.values(
            "external_dataset_id",
            "raw_external_id",
            "hoard_name",
            "number_of_coins",
            "opening_year1",
            "opening_year2",
            "year_from",
            "year_to",
            "latitude",
            "longitude",
            "region",
            "country",
            "external_source_text",
            "external_url",
        )[:500]
    )
    for row in rows:
        raw_id = str(row.get("raw_external_id") or "").strip()
        if raw_id.isdigit():
            row["chre_url"] = f"{CHRE_BASE_URL}{int(raw_id)}"
        else:
            ext = str(row.get("external_dataset_id") or "").strip().upper()
            row["chre_url"] = f"{CHRE_BASE_URL}{int(ext[4:])}" if ext.startswith("CHRE") and ext[4:].isdigit() else ""
    return JsonResponse({"count": len(rows), "results": rows})
