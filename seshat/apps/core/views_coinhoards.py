from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import CoinHoard


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
    return render(request, "core/coinhoards/hoard_detail.html", {"hoard": hoard})


def hoard_list_json(request):
    rows = list(
        CoinHoard.objects.values(
            "external_dataset_id",
            "hoard_name",
            "number_of_coins",
            "year_from",
            "year_to",
            "latitude",
            "longitude",
            "region",
            "country",
            "external_url",
        )[:500]
    )
    return JsonResponse({"count": len(rows), "results": rows})
