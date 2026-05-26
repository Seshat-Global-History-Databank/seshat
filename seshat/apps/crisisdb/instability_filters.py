import datetime
from collections import Counter, defaultdict

from django.db.models import Count, F, IntegerField, Q
from django.db.models.functions import Cast, Coalesce
from django.utils.dateparse import parse_date
from django.utils import timezone

from ..core.models import Polity
from .models import (
    Check_choice,
    INST_EXTENT_CHOICES,
    INST_INTENSITY_CHOICES,
    Instability_event,
    Instability_type,
)


BATCH_1_END = datetime.date(2025, 3, 29)
BATCH_2_END = datetime.date(2025, 4, 11)
BATCH_3_END = datetime.date(2026, 3, 1)
BATCH_1_END_DATETIME = timezone.make_aware(datetime.datetime.combine(BATCH_1_END, datetime.time()))
BATCH_2_END_DATETIME = timezone.make_aware(datetime.datetime.combine(BATCH_2_END, datetime.time()))
BATCH_3_END_DATETIME = timezone.make_aware(datetime.datetime.combine(BATCH_3_END, datetime.time()))
GOOD_ROW_FILTER = "good"
GOOD_ROW_EXCLUDED_CHECK_NAMES = frozenset(
    {
        "Bad Row",
        "Duplicate",
        "Not Instability Event",
        "External Event",
    }
)


def get_batch_tag(created_date):
    if created_date is None:
        return "Unknown"

    if isinstance(created_date, datetime.datetime):
        if timezone.is_naive(created_date):
            created_date = timezone.make_aware(created_date)
        created_date = created_date.date()

    if created_date < BATCH_1_END:
        return "Batch 1"
    if created_date < BATCH_2_END:
        return "Batch 2"
    if created_date < BATCH_3_END:
        return "Batch 3"
    return "Batch 4"


def get_batch_tooltip(created_date):
    if created_date is None:
        return "Unknown creation date"

    if isinstance(created_date, datetime.datetime):
        if timezone.is_naive(created_date):
            created_date = timezone.make_aware(created_date)
        created_date = created_date.date()

    if created_date < BATCH_1_END:
        return "Generated in March 2025."
    if created_date < BATCH_2_END:
        return "Generated from March 28th, to April 28th, 2025."
    if created_date < BATCH_3_END:
        return "Generated after April 28th, 2025."
    return "Generated on or after March 1st, 2026."


def apply_instability_batch_filter(queryset, selected_batch):
    if not selected_batch:
        return queryset

    if selected_batch == "Batch 1":
        return queryset.filter(created_date__lt=BATCH_1_END_DATETIME)
    if selected_batch == "Batch 2":
        return queryset.filter(
            created_date__gte=BATCH_1_END_DATETIME,
            created_date__lt=BATCH_2_END_DATETIME,
        )
    if selected_batch == "Batch 3":
        return queryset.filter(
            created_date__gte=BATCH_2_END_DATETIME,
            created_date__lt=BATCH_3_END_DATETIME,
        )
    if selected_batch == "Batch 4":
        return queryset.filter(created_date__gte=BATCH_3_END_DATETIME)
    return queryset


def get_request_list(request, key):
    return [value.strip() for value in request.GET.getlist(key) if value and value.strip()]


def get_selected_row_quality(request):
    selected_row_quality = request.GET.get("row_quality")
    if selected_row_quality == GOOD_ROW_FILTER:
        return selected_row_quality
    return None


def build_macro_event_filter_query(selected_macro_events):
    macro_event_query = Q()
    for macro_event in selected_macro_events:
        desired_str = "(macro event: " + macro_event.lower()
        macro_event_query |= Q(llm_name__icontains=desired_str) | Q(
            name__icontains=desired_str
        )
    return macro_event_query


def apply_instability_row_quality_filter(queryset, selected_row_quality):
    if selected_row_quality == GOOD_ROW_FILTER:
        return queryset.exclude(
            ra_check__name__in=GOOD_ROW_EXCLUDED_CHECK_NAMES
        ).distinct()
    return queryset


def get_polity_instability_queryset(polity_id, selected_source=None, selected_batch=None):
    queryset = Instability_event.objects.filter(
        polity__id=polity_id,
        polity__unreliable_instability_events=False,
    ).order_by("year_from")

    if selected_source in {Instability_event.Source.LLM, Instability_event.Source.MANUAL}:
        queryset = queryset.filter(source=selected_source)

    if selected_batch and selected_source != Instability_event.Source.MANUAL:
        queryset = queryset.filter(source=Instability_event.Source.LLM)
        queryset = apply_instability_batch_filter(queryset, selected_batch)

    return queryset


def get_selected_instability_source(request):
    selected_source = request.GET.get("source")
    if selected_source in {Instability_event.Source.LLM, Instability_event.Source.MANUAL}:
        return selected_source
    return None


def apply_instability_event_source_filter(queryset, request):
    selected_source = get_selected_instability_source(request)
    if selected_source:
        return queryset.filter(source=selected_source)
    return queryset


def apply_instability_event_filters(queryset, request, ignored_filters=None):
    ignored_filters = set(ignored_filters or [])
    year_from_min = (
        None if "year_from_min" in ignored_filters else request.GET.get("year_from_min")
    )
    year_to_max = (
        None if "year_to_max" in ignored_filters else request.GET.get("year_to_max")
    )
    created_before = (
        None if "created_before" in ignored_filters else request.GET.get("created_before")
    )
    selected_batch = (
        None if "selected_batch" in ignored_filters else request.GET.get("selected_batch")
    )
    selected_source = (
        None if "source" in ignored_filters else get_selected_instability_source(request)
    )
    polity_ids = [] if "polity" in ignored_filters else get_request_list(request, "polity")
    inst_type_ids = (
        [] if "inst_type" in ignored_filters else get_request_list(request, "inst_type")
    )
    ra_check_ids = (
        [] if "ra_check" in ignored_filters else get_request_list(request, "ra_check")
    )
    inst_extent_values = (
        [] if "inst_extent" in ignored_filters else get_request_list(request, "inst_extent")
    )
    inst_intensity_values = (
        []
        if "inst_intensity" in ignored_filters
        else get_request_list(request, "inst_intensity")
    )
    selected_macro_events = (
        []
        if "macro_event" in ignored_filters
        else get_request_list(request, "macro_event")
    )
    selected_is_macro_event = (
        None
        if "is_macro_event" in ignored_filters
        else request.GET.get("is_macro_event")
    )
    name_query = (
        ""
        if "searched_name" in ignored_filters
        else request.GET.get("searched_name", "").strip()
    )
    selected_row_quality = (
        None if "row_quality" in ignored_filters else get_selected_row_quality(request)
    )

    if inst_type_ids:
        queryset = queryset.filter(inst_type__in=inst_type_ids).distinct()

    if ra_check_ids:
        queryset = queryset.filter(ra_check__in=ra_check_ids).distinct()

    if inst_extent_values:
        queryset = queryset.filter(inst_extent__in=inst_extent_values)

    if inst_intensity_values:
        queryset = queryset.filter(inst_intensity__in=inst_intensity_values)

    if polity_ids:
        queryset = queryset.filter(polity__id__in=polity_ids)

    if selected_source:
        queryset = queryset.filter(source=selected_source)

    if selected_macro_events:
        queryset = queryset.filter(build_macro_event_filter_query(selected_macro_events))

    if selected_is_macro_event in {"true", "false"}:
        queryset = queryset.filter(is_macro_event=(selected_is_macro_event == "true"))

    if name_query:
        queryset = queryset.filter(name__icontains=name_query)

    queryset = apply_instability_row_quality_filter(queryset, selected_row_quality)

    queryset = queryset.annotate(
        start_year_effective=Coalesce("year_from", F("polity__start_year")),
        end_year_effective=Coalesce("year_to", F("polity__end_year")),
    )

    if year_from_min:
        queryset = queryset.filter(start_year_effective__gte=int(year_from_min))

    if year_to_max:
        queryset = queryset.filter(end_year_effective__lte=int(year_to_max))

    if created_before:
        parsed_date = parse_date(created_before)
        if parsed_date:
            queryset = queryset.filter(created_date__lt=parsed_date)

    if selected_batch and selected_source != Instability_event.Source.MANUAL:
        queryset = queryset.filter(source=Instability_event.Source.LLM)
        queryset = apply_instability_batch_filter(queryset, selected_batch)

    return queryset


def apply_instability_event_ordering(queryset, orderby):
    queryset = queryset.annotate(
        inst_intensity_num=Cast(F("inst_intensity"), output_field=IntegerField()),
        inst_extent_num=Cast(F("inst_extent"), output_field=IntegerField()),
    )

    if not orderby:
        return queryset

    ordering_map = {
        "year_from": "start_year_effective",
        "year_to": "end_year_effective",
        "inst_intensity": "inst_intensity_num",
        "inst_extent": "inst_extent_num",
    }

    field = ordering_map.get(orderby.lstrip("-"), orderby.lstrip("-"))

    if orderby.startswith("-"):
        return queryset.order_by(F(field).desc(nulls_last=True))
    return queryset.order_by(F(field).asc(nulls_last=True))


def get_instability_list_queryset(model_class):
    return (
        model_class.objects.filter(polity__unreliable_instability_events=False)
        .defer("general_cot", "classification_cot", "sorokin_rationale", "llm_description")
        .order_by("polity_id", "year_from", "id")
    )


def get_filtered_instability_queryset(model_class, request):
    queryset = get_instability_list_queryset(model_class)
    queryset = apply_instability_event_filters(queryset, request)
    return apply_instability_event_ordering(queryset, request.GET.get("orderby"))


def get_instability_filter_option_queryset(model_class, request, ignored_filters=None):
    queryset = get_instability_list_queryset(model_class)
    return apply_instability_event_filters(
        queryset,
        request,
        ignored_filters=ignored_filters,
    )


def get_instability_checking_status(event):
    if event.source != Instability_event.Source.LLM:
        return ""

    if event.researchers_list() and event.seshat_experts_list():
        return "Expert Checked"
    if event.researchers_list() or event.get_llm_instability_checks_str():
        return "RA Checked"
    return "Unchecked"


def get_instability_approved_description(event):
    if not event.comment:
        return None

    comment_parts = event.comment.inner_comments_related.all().order_by("comment_order")
    if comment_parts.exists():
        description = str(event.comment)
    elif event.comment.text:
        description = event.comment.text
    else:
        return None

    return (
        description
        .replace("\n", " ")
        .replace("<br>", " ")
        .replace("\r", " ")
    )


def build_instability_json_coded_values(event):
    return {
        "name": event.name,
        "macro_event": event.made_up_macro_event,
        "is_macro_event": event.is_macro_event,
        "inst_intensity": event.inst_intensity,
        "inst_extent": event.inst_extent,
        "real_event_check": event.real_event_check,
        "inst_types": event.get_instability_types_str(),
        "ra_checks": event.get_llm_instability_checks_str(),
        "checking_status": get_instability_checking_status(event),
        "sorokin_rationale": event.sorokin_rationale,
        "llm_description": event.llm_description,
        "llm_references": event.get_llm_instability_refs_str(),
        "ra_approved_description": get_instability_approved_description(event),
        "source": event.source,
        "batch_number": event.batch_number,
        "llm_name": event.llm_name,
        "llm_year_from": event.llm_year_from,
        "llm_year_to": event.llm_year_to,
        "llm_inst_type": event.llm_inst_type,
        "llm_inst_extent": event.llm_inst_extent,
        "llm_inst_intensity": event.llm_inst_intensity,
        "llm_real_event_check": event.llm_real_event_check,
    }


def build_instability_list_context(model_class, request):
    selected_source = get_selected_instability_source(request)
    selected_batch = request.GET.get("selected_batch")
    selected_row_quality = get_selected_row_quality(request)
    selected_polity_ids = get_request_list(request, "polity")
    selected_macro_events = get_request_list(request, "macro_event")
    selected_inst_type_ids = get_request_list(request, "inst_type")
    selected_ra_check_ids = get_request_list(request, "ra_check")
    selected_inst_extent_values = get_request_list(request, "inst_extent")
    selected_inst_intensity_values = get_request_list(request, "inst_intensity")

    polity_option_queryset = get_instability_filter_option_queryset(
        model_class,
        request,
        ignored_filters={"polity"},
    )
    macro_option_queryset = get_instability_filter_option_queryset(
        model_class,
        request,
        ignored_filters={"macro_event"},
    )
    inst_type_option_queryset = get_instability_filter_option_queryset(
        model_class,
        request,
        ignored_filters={"inst_type"},
    )
    ra_check_option_queryset = get_instability_filter_option_queryset(
        model_class,
        request,
        ignored_filters={"ra_check"},
    )
    inst_extent_option_queryset = get_instability_filter_option_queryset(
        model_class,
        request,
        ignored_filters={"inst_extent"},
    )
    inst_intensity_option_queryset = get_instability_filter_option_queryset(
        model_class,
        request,
        ignored_filters={"inst_intensity"},
    )

    polity_counts = {
        row["polity_id"]: row["event_count"]
        for row in polity_option_queryset.values("polity_id").annotate(
            event_count=Count("id", distinct=True)
        )
        if row["polity_id"] is not None
    }
    polities = list(Polity.objects.filter(id__in=polity_counts).order_by("new_name"))

    macro_event_list = [
        obj.made_up_macro_event
        for obj in macro_option_queryset
        if obj.made_up_macro_event
    ]
    macro_event_counts = Counter(macro_event_list)
    macro_events_with_counts = sorted(
        macro_event_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )

    batch_order = ["Batch 1", "Batch 2", "Batch 3", "Batch 4", "Unknown"]
    polity_batch_tags = defaultdict(set)
    for polity_id, source, created_date in polity_option_queryset.values_list(
        "polity_id",
        "source",
        "created_date",
    ):
        if (
            polity_id is not None
            and source == Instability_event.Source.LLM
            and created_date is not None
        ):
            polity_batch_tags[polity_id].add(get_batch_tag(created_date))

    enriched_polities = []
    for polity in polities:
        batch_list = sorted(
            polity_batch_tags.get(polity.id, set()),
            key=lambda value: (
                batch_order.index(value) if value in batch_order else len(batch_order)
            ),
        )
        setattr(polity, "event_count", polity_counts.get(polity.id, 0))
        setattr(polity, "batch_list", batch_list)
        enriched_polities.append(polity)

    inst_extent_counts = {
        row["inst_extent"]: row["event_count"]
        for row in inst_extent_option_queryset.exclude(inst_extent__isnull=True)
        .values("inst_extent")
        .annotate(event_count=Count("id", distinct=True))
    }
    inst_intensity_counts = {
        row["inst_intensity"]: row["event_count"]
        for row in inst_intensity_option_queryset.exclude(inst_intensity__isnull=True)
        .values("inst_intensity")
        .annotate(event_count=Count("id", distinct=True))
    }
    inst_extent_filter_choices = [
        (value, label, inst_extent_counts.get(value, 0))
        for value, label in INST_EXTENT_CHOICES
        if inst_extent_counts.get(value, 0) or value in selected_inst_extent_values
    ]
    inst_intensity_filter_choices = [
        (value, label, inst_intensity_counts.get(value, 0))
        for value, label in INST_INTENSITY_CHOICES
        if inst_intensity_counts.get(value, 0) or value in selected_inst_intensity_values
    ]

    return {
        "polities": enriched_polities,
        "unreliable_polities": Polity.objects.filter(
            unreliable_instability_events=True
        ).order_by("new_name"),
        "instability_types": Instability_type.objects.filter(
            crisisdb_instability_events__in=inst_type_option_queryset
        )
        .annotate(event_count=Count("crisisdb_instability_events", distinct=True))
        .distinct()
        .order_by("name"),
        "check_choices": Check_choice.objects.filter(
            crisisdb_instability_events__in=ra_check_option_queryset
        )
        .annotate(event_count=Count("crisisdb_instability_events", distinct=True))
        .distinct()
        .order_by("name"),
        "macro_events_with_counts": macro_events_with_counts,
        "macro_events": [event for event, _count in macro_events_with_counts],
        "selected_macro": selected_macro_events[0] if len(selected_macro_events) == 1 else None,
        "selected_macro_events": selected_macro_events,
        "selected_is_macro_event": request.GET.get("is_macro_event"),
        "name_query": request.GET.get("searched_name", "").strip(),
        "selected_source": selected_source,
        "selected_batch": selected_batch,
        "selected_row_quality": selected_row_quality,
        "show_llm_batch_filter": selected_source != Instability_event.Source.MANUAL,
        "selected_polity_ids": selected_polity_ids,
        "selected_inst_type_ids": selected_inst_type_ids,
        "selected_ra_check_ids": selected_ra_check_ids,
        "selected_inst_extent_values": selected_inst_extent_values,
        "selected_inst_intensity_values": selected_inst_intensity_values,
        "inst_extent_filter_choices": inst_extent_filter_choices,
        "inst_intensity_filter_choices": inst_intensity_filter_choices,
        "INST_EXTENT_CHOICES": INST_EXTENT_CHOICES,
        "INST_INTENSITY_CHOICES": INST_INTENSITY_CHOICES,
    }


def is_llm_instability_event(instance):
    return bool(
        instance and getattr(instance, "source", None) == Instability_event.Source.LLM
    )
