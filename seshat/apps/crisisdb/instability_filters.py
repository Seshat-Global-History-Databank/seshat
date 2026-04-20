import datetime
from collections import Counter

from django.db.models import F, IntegerField, Q
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


def apply_instability_event_filters(queryset, request):
    year_from_min = request.GET.get("year_from_min")
    year_to_max = request.GET.get("year_to_max")
    created_before = request.GET.get("created_before")
    selected_batch = request.GET.get("selected_batch")
    selected_source = get_selected_instability_source(request)
    polity_id = request.GET.get("polity")
    inst_type_ids = request.GET.getlist("inst_type")
    ra_check_ids = request.GET.getlist("ra_check")
    inst_extent = request.GET.get("inst_extent")
    inst_intensity = request.GET.get("inst_intensity")
    selected_macro = request.GET.get("macro_event")
    selected_is_macro_event = request.GET.get("is_macro_event")
    name_query = request.GET.get("searched_name", "").strip()

    if inst_type_ids:
        queryset = queryset.filter(inst_type__in=inst_type_ids).distinct()

    if ra_check_ids:
        queryset = queryset.filter(ra_check__in=ra_check_ids).distinct()

    if inst_extent:
        queryset = queryset.filter(inst_extent=inst_extent)

    if inst_intensity:
        queryset = queryset.filter(inst_intensity=inst_intensity)

    if polity_id:
        queryset = queryset.filter(polity__id=polity_id)

    queryset = apply_instability_event_source_filter(queryset, request)

    if selected_macro:
        desired_str = "(macro event: " + selected_macro.lower()
        queryset = queryset.filter(
            Q(llm_name__icontains=desired_str) | Q(name__icontains=desired_str)
        )

    if selected_is_macro_event in {"true", "false"}:
        queryset = queryset.filter(is_macro_event=(selected_is_macro_event == "true"))

    if name_query:
        queryset = queryset.filter(name__icontains=name_query)

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
    filter_option_queryset = apply_instability_event_source_filter(
        get_instability_list_queryset(model_class),
        request,
    )
    polity_ids = filter_option_queryset.values_list("polity_id", flat=True).distinct()
    polities = Polity.objects.filter(id__in=polity_ids).order_by("new_name")

    macro_event_list = [
        obj.made_up_macro_event
        for obj in filter_option_queryset
        if obj.made_up_macro_event
    ]
    macro_event_counts = Counter(macro_event_list)
    macro_events_with_counts = sorted(
        macro_event_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )

    batch_order = ["Batch 1", "Batch 2", "Batch 3", "Batch 4", "Unknown"]
    enriched_polities = []
    for polity in polities:
        llm_created_dates = filter_option_queryset.filter(
            polity=polity,
            source=Instability_event.Source.LLM,
        ).values_list("created_date", flat=True).distinct()

        batch_list = sorted(
            {
                get_batch_tag(created.date())
                for created in llm_created_dates
                if created is not None
            },
            key=lambda value: (
                batch_order.index(value) if value in batch_order else len(batch_order)
            ),
        )
        setattr(polity, "batch_list", batch_list)
        enriched_polities.append(polity)

    return {
        "polities": enriched_polities,
        "unreliable_polities": Polity.objects.filter(
            unreliable_instability_events=True
        ).order_by("new_name"),
        "instability_types": Instability_type.objects.all(),
        "check_choices": Check_choice.objects.all(),
        "macro_events_with_counts": macro_events_with_counts,
        "macro_events": [event for event, _count in macro_events_with_counts],
        "selected_macro": request.GET.get("macro_event"),
        "selected_is_macro_event": request.GET.get("is_macro_event"),
        "name_query": request.GET.get("searched_name", "").strip(),
        "selected_source": selected_source,
        "selected_batch": selected_batch,
        "show_llm_batch_filter": selected_source != Instability_event.Source.MANUAL,
        "selected_inst_type_ids": request.GET.getlist("inst_type"),
        "selected_ra_check_ids": request.GET.getlist("ra_check"),
        "INST_EXTENT_CHOICES": INST_EXTENT_CHOICES,
        "INST_INTENSITY_CHOICES": INST_INTENSITY_CHOICES,
    }


def is_llm_instability_event(instance):
    return bool(
        instance and getattr(instance, "source", None) == Instability_event.Source.LLM
    )
