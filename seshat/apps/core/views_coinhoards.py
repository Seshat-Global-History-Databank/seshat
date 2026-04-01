from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import CoinHoard

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


def hoard_list(request):
    q = request.GET.get("q", "").strip()
    region = request.GET.get("region", "").strip()
    start = request.GET.get("start_year", "").strip()
    end = request.GET.get("end_year", "").strip()

    queryset = CoinHoard.objects.all()

    if q:
        queryset = queryset.filter(
            Q(external_dataset_id__icontains=q)
            | Q(hoard_name__icontains=q)
            | Q(country__icontains=q)
        )

    if region:
        queryset = queryset.filter(region__iexact=region)

    try:
        if start:
            start_int = int(start)
            queryset = queryset.filter(Q(year_to__isnull=True) | Q(year_to__gte=start_int))
        if end:
            end_int = int(end)
            queryset = queryset.filter(Q(year_from__isnull=True) | Q(year_from__lte=end_int))
    except ValueError:
        pass

    paginator = Paginator(queryset, 50)
    page_obj = paginator.get_page(request.GET.get("page", 1))
    for hoard in page_obj.object_list:
        hoard.findspot_label, hoard.findspot_class = _rating_meta(hoard.find_spot_rating)
        hoard.context_label, hoard.context_class = _rating_meta(hoard.contextual_rating)
        hoard.numismatic_label, hoard.numismatic_class = _rating_meta(hoard.numismatic_rating)
        hoard.chre_url = _chre_url(hoard)

    return render(
        request,
        "core/coinhoards/hoard_list.html",
        {
            "page_obj": page_obj,
            "q": q,
            "region": region,
            "start_year": start,
            "end_year": end,
        },
    )


def hoard_detail(request, external_dataset_id):
    hoard = get_object_or_404(CoinHoard, external_dataset_id=external_dataset_id)
    hoard.chre_url = _chre_url(hoard)
    hoard.findspot_label, hoard.findspot_class = _rating_meta(hoard.find_spot_rating)
    hoard.context_label, hoard.context_class = _rating_meta(hoard.contextual_rating)
    hoard.numismatic_label, hoard.numismatic_class = _rating_meta(hoard.numismatic_rating)
    return render(request, "core/coinhoards/hoard_detail.html", {"hoard": hoard})


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
