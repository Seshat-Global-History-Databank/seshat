import datetime
from collections import Counter, defaultdict

from django.db.models import Count, F, IntegerField, Q
from django.db.models.functions import Cast, Coalesce
from django.utils.dateparse import parse_date
from django.utils import timezone

from ..core.filter_tokens import (
    FilterTokenOption,
    build_grouped_token_response,
    build_term_search_query,
    get_search_terms,
    normalize_search_text,
)
from ..core.models import Polity
from .models import (
    Check_choice,
    INST_EXTENT_CHOICES,
    INST_INTENSITY_CHOICES,
    Instability_event,
    Instability_type,
    extract_macro_event_from_llm_name,
)


BATCH_1_END = datetime.date(2025, 3, 29)
BATCH_2_END = datetime.date(2025, 4, 11)
BATCH_3_END = datetime.date(2026, 3, 1)
BATCH_1_END_DATETIME = timezone.make_aware(datetime.datetime.combine(BATCH_1_END, datetime.time()))
BATCH_2_END_DATETIME = timezone.make_aware(datetime.datetime.combine(BATCH_2_END, datetime.time()))
BATCH_3_END_DATETIME = timezone.make_aware(datetime.datetime.combine(BATCH_3_END, datetime.time()))
GOOD_ROW_FILTER = "good"
GOOD_ROW_EXCLUDED_CHECK_NAMES = (
    "Bad Row",
    "Duplicate",
    "Not Instability Event",
    "External Event",
)
EXCLUDED_RA_CHECK_PARAM = "excluded_ra_check"
EXCLUDED_RA_CHECK_MODE_PARAM = "excluded_ra_check_mode"
CUSTOM_EXCLUDED_RA_CHECK_MODE = "custom"
VALID_INSTABILITY_SOURCES = (
    Instability_event.Source.LLM,
    Instability_event.Source.MANUAL,
)
VALID_INSTABILITY_BATCHES = (
    "Batch 1",
    "Batch 2",
    "Batch 3",
    "Batch 4",
)
INSTABILITY_FILTER_TOKEN_LIMIT = 8
INSTABILITY_FILTER_TOKEN_GROUP_ORDER = (
    "Sources",
    "LLM Batches",
    "Macroevent",
    "Polities",
    "Event Types",
    "Researcher Checks",
    "Text Search",
    "Events",
    "Umbrella Events",
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


def normalize_instability_batches(selected_batches):
    if not selected_batches:
        return []

    if isinstance(selected_batches, str):
        selected_batches = [selected_batches]

    normalized_batches = []
    for batch in selected_batches:
        if batch in VALID_INSTABILITY_BATCHES and batch not in normalized_batches:
            normalized_batches.append(batch)
    return normalized_batches


def apply_instability_batch_filter(queryset, selected_batches):
    selected_batches = normalize_instability_batches(selected_batches)
    if not selected_batches:
        return queryset

    return queryset.filter(build_instability_batch_query(selected_batches))


def build_instability_batch_query(selected_batches):
    selected_batches = normalize_instability_batches(selected_batches)
    batch_query = Q()
    if "Batch 1" in selected_batches:
        batch_query |= Q(created_date__lt=BATCH_1_END_DATETIME)
    if "Batch 2" in selected_batches:
        batch_query |= Q(
            created_date__gte=BATCH_1_END_DATETIME,
            created_date__lt=BATCH_2_END_DATETIME,
        )
    if "Batch 3" in selected_batches:
        batch_query |= Q(
            created_date__gte=BATCH_2_END_DATETIME,
            created_date__lt=BATCH_3_END_DATETIME,
        )
    if "Batch 4" in selected_batches:
        batch_query |= Q(created_date__gte=BATCH_3_END_DATETIME)
    return batch_query


def get_request_list(request, key):
    values = []
    for value in request.GET.getlist(key):
        cleaned_value = value.strip() if value else ""
        if cleaned_value and cleaned_value not in values:
            values.append(cleaned_value)
    return values


def get_selected_ra_check_ids(request):
    return [
        value
        for value in get_request_list(request, "ra_check")
        if value.isdigit()
    ]


def exclude_required_ra_check_ids(request, check_ids):
    required_check_ids = set(get_selected_ra_check_ids(request))
    return [
        check_id
        for check_id in check_ids
        if check_id not in required_check_ids
    ]


def get_selected_row_quality(request):
    selected_row_quality = request.GET.get("row_quality")
    if selected_row_quality == GOOD_ROW_FILTER:
        return selected_row_quality
    if get_custom_excluded_ra_check_ids(request):
        return GOOD_ROW_FILTER
    return None


def get_default_excluded_ra_check_ids():
    return [
        str(check_id)
        for check_id in Check_choice.objects.filter(
            name__in=GOOD_ROW_EXCLUDED_CHECK_NAMES
        )
        .order_by("name")
        .values_list("id", flat=True)
    ]


def uses_custom_excluded_ra_checks(request):
    return (
        request.GET.get(EXCLUDED_RA_CHECK_MODE_PARAM) == CUSTOM_EXCLUDED_RA_CHECK_MODE
        or bool(get_raw_custom_excluded_ra_check_ids(request))
    )


def get_raw_custom_excluded_ra_check_ids(request):
    return [
        value
        for value in get_request_list(request, EXCLUDED_RA_CHECK_PARAM)
        if value.isdigit()
    ]


def get_custom_excluded_ra_check_ids(request):
    custom_check_ids = get_raw_custom_excluded_ra_check_ids(request)
    return exclude_required_ra_check_ids(request, custom_check_ids)


def get_selected_excluded_ra_check_ids(request):
    if get_selected_row_quality(request) != GOOD_ROW_FILTER:
        return []

    if uses_custom_excluded_ra_checks(request):
        return get_custom_excluded_ra_check_ids(request)

    return exclude_required_ra_check_ids(request, get_default_excluded_ra_check_ids())


def build_macro_event_filter_query(selected_macro_events):
    macro_event_query = Q()
    for macro_event in selected_macro_events:
        desired_str = "(macro event: " + macro_event.lower()
        macro_event_query |= Q(llm_name__icontains=desired_str) | Q(
            name__icontains=desired_str
        )
    return macro_event_query


def apply_instability_row_quality_filter(
    queryset,
    selected_row_quality,
    excluded_ra_check_ids=None,
):
    if selected_row_quality == GOOD_ROW_FILTER:
        if excluded_ra_check_ids is not None:
            if not excluded_ra_check_ids:
                return queryset
            return queryset.exclude(ra_check__id__in=excluded_ra_check_ids).distinct()

        return queryset.exclude(ra_check__name__in=GOOD_ROW_EXCLUDED_CHECK_NAMES).distinct()
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
    selected_sources = get_selected_instability_sources(request)
    if len(selected_sources) == 1:
        return selected_sources[0]
    return None


def get_selected_instability_sources(request):
    selected_sources = []
    for source in get_request_list(request, "source"):
        if source in VALID_INSTABILITY_SOURCES and source not in selected_sources:
            selected_sources.append(source)
    return selected_sources


def get_selected_instability_batches(request):
    return normalize_instability_batches(get_request_list(request, "selected_batch"))


def get_selected_instability_event_ids(request):
    return [
        value
        for value in get_request_list(request, "event")
        if value.isdigit()
    ]


def get_selected_instability_text_queries(request):
    return get_request_list(request, "q")


def get_active_instability_filter_count(request):
    multi_value_filters = (
        "polity",
        "macro_event",
        "inst_type",
        "ra_check",
        "inst_extent",
        "inst_intensity",
        "event",
        "q",
    )
    active_count = sum(
        len(get_request_list(request, filter_name))
        for filter_name in multi_value_filters
    )

    selected_batches = get_selected_instability_batches(request)
    selected_sources = get_selected_instability_sources(request)
    if selected_batches:
        # Batch filters imply LLM-only results and each selected batch is shown as a chip.
        active_count += 1 + len(selected_batches)
    else:
        active_count += len(selected_sources)
    if get_selected_row_quality(request):
        active_count += 1
    if request.GET.get("is_macro_event") in {"true", "false"}:
        active_count += 1
    if request.GET.get("searched_name", "").strip():
        active_count += 1
    if request.GET.get("year_from_min"):
        active_count += 1
    if request.GET.get("year_to_max"):
        active_count += 1

    return active_count


def apply_instability_event_source_filter(queryset, request):
    selected_sources = get_selected_instability_sources(request)
    if selected_sources:
        return queryset.filter(source__in=selected_sources)
    return queryset


def build_instability_global_text_query(text_values):
    global_query = Q()
    searchable_fields = (
        "name",
        "llm_name",
        "polity__name",
        "polity__long_name",
        "polity__new_name",
        "inst_type__name",
        "ra_check__name",
    )
    for text_value in text_values:
        if not get_search_terms(text_value):
            continue
        item_query = build_term_search_query(text_value, searchable_fields)

        matching_sources = [
            source
            for source, label in (
                (Instability_event.Source.LLM, "LLM"),
                (Instability_event.Source.MANUAL, "Manual"),
            )
            if _token_query_matches(text_value, source, label)
        ]
        if matching_sources:
            item_query |= Q(source__in=matching_sources)

        matching_batches = [
            batch
            for batch in VALID_INSTABILITY_BATCHES
            if _token_query_matches(text_value, batch, batch.replace(" ", ""))
        ]
        if matching_batches:
            item_query |= (
                Q(source=Instability_event.Source.LLM)
                & build_instability_batch_query(matching_batches)
            )

        for value, label in INST_INTENSITY_CHOICES:
            if _token_query_matches(text_value, value, label):
                item_query |= Q(inst_intensity=value)

        for value, label in INST_EXTENT_CHOICES:
            if _token_query_matches(text_value, value, label):
                item_query |= Q(inst_extent=value)

        global_query |= item_query
    return global_query


def apply_instability_global_text_filter(queryset, text_values):
    if not text_values:
        return queryset
    searchable_text_values = [
        text_value
        for text_value in text_values
        if get_search_terms(text_value)
    ]
    if not searchable_text_values:
        return queryset.none()
    return queryset.filter(
        build_instability_global_text_query(searchable_text_values)
    ).distinct()


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
    selected_batches = (
        []
        if "selected_batch" in ignored_filters
        else get_selected_instability_batches(request)
    )
    selected_sources = (
        [] if "source" in ignored_filters else get_selected_instability_sources(request)
    )
    selected_event_ids = (
        [] if "event" in ignored_filters else get_selected_instability_event_ids(request)
    )
    selected_text_queries = (
        [] if "q" in ignored_filters else get_selected_instability_text_queries(request)
    )
    polity_ids = [] if "polity" in ignored_filters else get_request_list(request, "polity")
    inst_type_ids = (
        [] if "inst_type" in ignored_filters else get_request_list(request, "inst_type")
    )
    ra_check_ids = (
        [] if "ra_check" in ignored_filters else get_selected_ra_check_ids(request)
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
    excluded_ra_check_ids = (
        []
        if EXCLUDED_RA_CHECK_PARAM in ignored_filters or "row_quality" in ignored_filters
        else get_selected_excluded_ra_check_ids(request)
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

    if selected_event_ids:
        queryset = queryset.filter(id__in=selected_event_ids)

    if selected_batches:
        queryset = queryset.filter(source=Instability_event.Source.LLM)
    elif selected_sources:
        queryset = queryset.filter(source__in=selected_sources)

    if selected_macro_events:
        queryset = queryset.filter(build_macro_event_filter_query(selected_macro_events))

    if selected_is_macro_event in {"true", "false"}:
        queryset = queryset.filter(is_macro_event=(selected_is_macro_event == "true"))

    if name_query:
        queryset = queryset.filter(name__icontains=name_query)

    queryset = apply_instability_global_text_filter(queryset, selected_text_queries)

    queryset = apply_instability_row_quality_filter(
        queryset,
        selected_row_quality,
        excluded_ra_check_ids=excluded_ra_check_ids,
    )

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

    if selected_batches:
        queryset = apply_instability_batch_filter(queryset, selected_batches)

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


def _token_query_matches(search_query, *values):
    terms = get_search_terms(search_query)
    if not terms:
        return False

    normalized_values = [
        normalize_search_text(value)
        for value in values
        if str(value or "").strip()
    ]
    return all(
        any(term in normalized_value for normalized_value in normalized_values)
        for term in terms
    )


def _build_instability_text_token(search_query):
    if len(search_query) < 2:
        return []

    return [
        FilterTokenOption(
            kind="text",
            value=search_query,
            label=f'Search all fields for "{search_query}"',
            group="Text Search",
            meta="Event names, polities, labels, source, and batch",
        )
    ]


def _build_instability_polity_tokens(base_queryset, search_query, limit):
    polity_rows = (
        base_queryset.filter(
            build_term_search_query(
                search_query,
                (
                    "polity__name",
                    "polity__long_name",
                    "polity__new_name",
                ),
            )
        )
        .values(
            "polity_id",
            "polity__long_name",
            "polity__new_name",
            "polity__start_year",
            "polity__end_year",
        )
        .annotate(event_count=Count("id", distinct=True))
        .order_by("-event_count", "polity__long_name")[:limit]
    )

    return [
        FilterTokenOption(
            kind="polity",
            value=str(row["polity_id"]),
            label=f"{row['polity__long_name']} ({row['polity__new_name']})",
            group="Polities",
            meta=(
                f"{row['event_count']} events"
                f" | {row['polity__start_year']} to {row['polity__end_year']}"
            ),
        )
        for row in polity_rows
        if row["polity_id"]
    ]


def _build_instability_event_tokens(base_queryset, search_query, limit):
    events = (
        base_queryset.filter(
            build_term_search_query(
                search_query,
                (
                    "name",
                    "llm_name",
                    "polity__long_name",
                    "polity__new_name",
                ),
            )
        )
        .select_related("polity")
        .only("id", "name", "llm_name", "year_from", "year_to", "polity__long_name")
        .order_by("name", "id")[:limit]
    )

    return [
        FilterTokenOption(
            kind="event",
            value=str(event.id),
            label=event.name or event.llm_name or f"Event {event.id}",
            group="Events",
            meta=(
                f"{event.polity.long_name if event.polity_id else 'No polity'}"
                f" | {event.year_from or '?'} to {event.year_to or '?'}"
            ),
        )
        for event in events
    ]


def _build_instability_type_tokens(base_queryset, search_query, limit):
    event_types = (
        Instability_type.objects.filter(
            build_term_search_query(search_query, ("name",)),
            crisisdb_instability_events__in=base_queryset,
        )
        .annotate(event_count=Count("crisisdb_instability_events", distinct=True))
        .distinct()
        .order_by("name")[:limit]
    )

    return [
        FilterTokenOption(
            kind="inst_type",
            value=str(event_type.id),
            label=event_type.name,
            group="Event Types",
            meta=f"{event_type.event_count} events",
        )
        for event_type in event_types
    ]


def _build_instability_check_tokens(base_queryset, search_query, limit):
    check_choices = (
        Check_choice.objects.filter(
            build_term_search_query(search_query, ("name",)),
            crisisdb_instability_events__in=base_queryset,
        )
        .annotate(event_count=Count("crisisdb_instability_events", distinct=True))
        .distinct()
        .order_by("name")[:limit]
    )

    return [
        FilterTokenOption(
            kind="ra_check",
            value=str(check.id),
            label=check.name,
            group="Researcher Checks",
            meta=f"{check.event_count} events",
        )
        for check in check_choices
    ]


def _build_instability_source_tokens(base_queryset, search_query):
    source_labels = {
        Instability_event.Source.LLM: "LLM",
        Instability_event.Source.MANUAL: "Manual",
    }

    tokens = []
    for source, label in source_labels.items():
        if _token_query_matches(search_query, source, label, "source"):
            tokens.append(
                FilterTokenOption(
                    kind="source",
                    value=source,
                    label=label,
                    group="Sources",
                    meta=f"{base_queryset.filter(source=source).count()} events",
                )
            )
    return tokens


def _build_instability_batch_tokens(base_queryset, search_query):
    tokens = []
    llm_queryset = base_queryset.filter(source=Instability_event.Source.LLM)
    for batch in VALID_INSTABILITY_BATCHES:
        if _token_query_matches(search_query, batch, batch.replace(" ", "")):
            tokens.append(
                FilterTokenOption(
                    kind="selected_batch",
                    value=batch,
                    label=batch,
                    group="LLM Batches",
                    meta=f"{apply_instability_batch_filter(llm_queryset, batch).count()} events",
                )
            )
    return tokens


def _build_instability_macro_event_record_tokens(base_queryset, search_query):
    choices = (
        (
            "true",
            "Macro events only",
            (
                "macro",
                "macroevent",
                "macro event",
                "macroevent true",
                "record",
                "record type",
                "true",
            ),
        ),
        (
            "false",
            "Normal events only",
            (
                "macro",
                "macroevent",
                "macro event",
                "macroevent false",
                "non macro",
                "non-macroevent",
                "record",
                "record type",
                "normal",
                "normal event",
                "normal events",
                "single event",
                "single-event",
                "false",
            ),
        ),
    )

    tokens = []
    for value, label, aliases in choices:
        if _token_query_matches(search_query, label, *aliases):
            tokens.append(
                FilterTokenOption(
                    kind="is_macro_event",
                    value=value,
                    label=label,
                    group="Macroevent",
                    meta=f"{base_queryset.filter(is_macro_event=(value == 'true')).count()} events",
                )
            )
    return tokens


def _build_instability_macro_event_tokens(base_queryset, search_query, limit):
    candidates = base_queryset.filter(
        Q(name__icontains="Macro Event") | Q(llm_name__icontains="Macro Event"),
        build_term_search_query(search_query, ("name", "llm_name")),
    ).values_list("name", "llm_name")[:200]

    macro_counts = Counter()
    for name, llm_name in candidates:
        macro_event = extract_macro_event_from_llm_name(llm_name or name)
        if macro_event and _token_query_matches(search_query, macro_event):
            macro_counts[macro_event] += 1

    return [
        FilterTokenOption(
            kind="macro_event",
            value=macro_event,
            label=macro_event,
            group="Umbrella Events",
            meta=f"{count} events",
        )
        for macro_event, count in macro_counts.most_common(limit)
    ]


def build_instability_filter_token_options(search_query, limit=INSTABILITY_FILTER_TOKEN_LIMIT):
    search_query = (search_query or "").strip()
    if not search_query or not get_search_terms(search_query):
        return []

    base_queryset = get_instability_list_queryset(Instability_event)
    return (
        _build_instability_source_tokens(base_queryset, search_query)
        + _build_instability_batch_tokens(base_queryset, search_query)
        + _build_instability_macro_event_record_tokens(base_queryset, search_query)
        + _build_instability_polity_tokens(base_queryset, search_query, limit)
        + _build_instability_type_tokens(base_queryset, search_query, limit)
        + _build_instability_check_tokens(base_queryset, search_query, limit)
        + _build_instability_text_token(search_query)
        + _build_instability_event_tokens(base_queryset, search_query, limit)
        + _build_instability_macro_event_tokens(base_queryset, search_query, limit)
    )


def build_instability_filter_token_response(search_query):
    return build_grouped_token_response(
        build_instability_filter_token_options(search_query),
        group_order=INSTABILITY_FILTER_TOKEN_GROUP_ORDER,
    )


def build_selected_instability_filter_token_options(request):
    options = []

    for text_query in get_selected_instability_text_queries(request):
        options.append(
            FilterTokenOption(
                kind="text",
                value=text_query,
                label=f'Search all fields for "{text_query}"',
                group="Text Search",
            )
        )

    for polity in Polity.objects.filter(
        id__in=get_request_list(request, "polity")
    ).order_by("long_name"):
        options.append(
            FilterTokenOption(
                kind="polity",
                value=str(polity.id),
                label=f"{polity.long_name} ({polity.new_name})",
                group="Polities",
            )
        )

    for event in get_instability_list_queryset(Instability_event).filter(
        id__in=get_selected_instability_event_ids(request)
    ).select_related("polity"):
        options.append(
            FilterTokenOption(
                kind="event",
                value=str(event.id),
                label=event.name or event.llm_name or f"Event {event.id}",
                group="Events",
            )
        )

    for macro_event in get_request_list(request, "macro_event"):
        options.append(
            FilterTokenOption(
                kind="macro_event",
                value=macro_event,
                label=macro_event,
                group="Umbrella Events",
            )
        )

    selected_is_macro_event = request.GET.get("is_macro_event")
    if selected_is_macro_event in {"true", "false"}:
        options.append(
            FilterTokenOption(
                kind="is_macro_event",
                value=selected_is_macro_event,
                label=(
                    "Macro events only"
                    if selected_is_macro_event == "true"
                    else "Normal events only"
                ),
                group="Macroevent",
            )
        )

    for event_type in Instability_type.objects.filter(
        id__in=get_request_list(request, "inst_type")
    ).order_by("name"):
        options.append(
            FilterTokenOption(
                kind="inst_type",
                value=str(event_type.id),
                label=event_type.name,
                group="Event Types",
            )
        )

    for check in Check_choice.objects.filter(
        id__in=get_selected_ra_check_ids(request)
    ).order_by("name"):
        options.append(
            FilterTokenOption(
                kind="ra_check",
                value=str(check.id),
                label=check.name,
                group="Researcher Checks",
            )
        )

    source_labels = {
        Instability_event.Source.LLM: "LLM",
        Instability_event.Source.MANUAL: "Manual",
    }
    for source in get_selected_instability_sources(request):
        options.append(
            FilterTokenOption(
                kind="source",
                value=source,
                label=source_labels.get(source, source.title()),
                group="Sources",
            )
        )

    for batch in get_selected_instability_batches(request):
        options.append(
            FilterTokenOption(
                kind="selected_batch",
                value=batch,
                label=batch,
                group="LLM Batches",
            )
        )

    return options


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
    selected_batch_values = get_selected_instability_batches(request)
    batch_filter_forces_llm = bool(selected_batch_values)
    explicit_selected_source_values = get_selected_instability_sources(request)
    explicit_selected_source = (
        explicit_selected_source_values[0]
        if len(explicit_selected_source_values) == 1
        else None
    )
    selected_sources = (
        [Instability_event.Source.LLM]
        if batch_filter_forces_llm
        else explicit_selected_source_values
    )
    selected_source = selected_sources[0] if len(selected_sources) == 1 else None
    selected_row_quality = get_selected_row_quality(request)
    selected_polity_ids = get_request_list(request, "polity")
    selected_macro_events = get_request_list(request, "macro_event")
    selected_event_ids = get_selected_instability_event_ids(request)
    selected_text_queries = get_selected_instability_text_queries(request)
    selected_inst_type_ids = get_request_list(request, "inst_type")
    selected_ra_check_ids = get_selected_ra_check_ids(request)
    selected_excluded_ra_check_ids = get_selected_excluded_ra_check_ids(request)
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
    excluded_ra_check_option_queryset = get_instability_filter_option_queryset(
        model_class,
        request,
        ignored_filters={
            EXCLUDED_RA_CHECK_PARAM,
            EXCLUDED_RA_CHECK_MODE_PARAM,
            "row_quality",
        },
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
    batch_option_queryset = get_instability_filter_option_queryset(
        model_class,
        request,
        ignored_filters={"selected_batch", "source"},
    )
    source_option_queryset = get_instability_filter_option_queryset(
        model_class,
        request,
        ignored_filters={"source"},
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
    source_counts = {
        row["source"]: row["event_count"]
        for row in source_option_queryset.values("source").annotate(
            event_count=Count("id", distinct=True)
        )
    }
    source_filter_choices = [
        (Instability_event.Source.LLM, "LLM", source_counts.get(Instability_event.Source.LLM, 0)),
        (
            Instability_event.Source.MANUAL,
            "Manual",
            source_counts.get(Instability_event.Source.MANUAL, 0),
        ),
    ]
    batch_counts = Counter(
        get_batch_tag(created_date)
        for source, created_date in batch_option_queryset.values_list(
            "source",
            "created_date",
        )
        if source == Instability_event.Source.LLM and created_date is not None
    )
    batch_filter_choices = [
        (batch, batch_counts.get(batch, 0))
        for batch in VALID_INSTABILITY_BATCHES
        if batch_counts.get(batch, 0) or batch in selected_batch_values
    ]
    selected_event_filters = list(
        get_instability_list_queryset(model_class)
        .filter(id__in=selected_event_ids)
        .select_related("polity")
        .order_by("name", "id")
    )
    excluded_ra_check_choices = list(
        Check_choice.objects.filter(
            Q(crisisdb_instability_events__in=excluded_ra_check_option_queryset)
            | Q(id__in=selected_excluded_ra_check_ids)
            | Q(name__in=GOOD_ROW_EXCLUDED_CHECK_NAMES)
        )
        .annotate(event_count=Count("crisisdb_instability_events", distinct=True))
        .distinct()
        .order_by("name")
    )
    selected_excluded_ra_check_labels = [
        check.name
        for check in excluded_ra_check_choices
        if str(check.id) in selected_excluded_ra_check_ids
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
        "selected_event_ids": selected_event_ids,
        "selected_event_filters": selected_event_filters,
        "selected_text_queries": selected_text_queries,
        "selected_is_macro_event": request.GET.get("is_macro_event"),
        "name_query": request.GET.get("searched_name", "").strip(),
        "selected_source": selected_source,
        "selected_source_values": selected_sources,
        "explicit_selected_source": explicit_selected_source,
        "explicit_selected_source_values": explicit_selected_source_values,
        "selected_batch": selected_batch_values[0] if len(selected_batch_values) == 1 else None,
        "selected_batch_values": selected_batch_values,
        "batch_filter_forces_llm": batch_filter_forces_llm,
        "selected_row_quality": selected_row_quality,
        "default_excluded_ra_check_ids": get_default_excluded_ra_check_ids(),
        "excluded_ra_check_choices": excluded_ra_check_choices,
        "selected_excluded_ra_check_ids": selected_excluded_ra_check_ids,
        "selected_excluded_ra_check_labels": selected_excluded_ra_check_labels,
        "show_llm_batch_filter": True,
        "selected_polity_ids": selected_polity_ids,
        "selected_inst_type_ids": selected_inst_type_ids,
        "selected_ra_check_ids": selected_ra_check_ids,
        "selected_inst_extent_values": selected_inst_extent_values,
        "selected_inst_intensity_values": selected_inst_intensity_values,
        "active_filter_count": get_active_instability_filter_count(request),
        "selected_global_filter_tokens": build_selected_instability_filter_token_options(request),
        "source_filter_choices": source_filter_choices,
        "batch_filter_choices": batch_filter_choices,
        "inst_extent_filter_choices": inst_extent_filter_choices,
        "inst_intensity_filter_choices": inst_intensity_filter_choices,
        "INST_EXTENT_CHOICES": INST_EXTENT_CHOICES,
        "INST_INTENSITY_CHOICES": INST_INTENSITY_CHOICES,
    }


def is_llm_instability_event(instance):
    return bool(
        instance and getattr(instance, "source", None) == Instability_event.Source.LLM
    )
