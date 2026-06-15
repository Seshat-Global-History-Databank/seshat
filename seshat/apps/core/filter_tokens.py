import re
import unicodedata
from dataclasses import dataclass
from typing import Iterable

from django.db.models import Q


TOKEN_SEPARATOR = ":"
SEARCH_TERM_PATTERN = re.compile(r"[\w]+")


@dataclass(frozen=True)
class FilterTokenOption:
    """Reusable grouped option shape for AJAX-backed filter pickers."""

    kind: str
    value: str
    label: str
    group: str
    meta: str = ""

    @property
    def token_id(self):
        return make_filter_token(self.kind, self.value)

    def as_select2_result(self):
        result = {
            "id": self.token_id,
            "text": self.label,
            "kind": self.kind,
            "value": self.value,
        }
        if self.meta:
            result["meta"] = self.meta
        return result


def make_filter_token(kind, value):
    return f"{kind}{TOKEN_SEPARATOR}{value}"


def parse_filter_token(token_id):
    kind, separator, value = str(token_id).partition(TOKEN_SEPARATOR)
    if not separator or not kind or not value:
        return None, None
    return kind, value


def normalize_search_text(value):
    """Normalize user-entered filter text for case/diacritic-insensitive matching."""
    normalized = unicodedata.normalize("NFKD", str(value or ""))
    ascii_text = "".join(
        character
        for character in normalized
        if not unicodedata.combining(character)
    )
    return " ".join(SEARCH_TERM_PATTERN.findall(ascii_text.lower()))


def get_search_terms(search_query):
    return normalize_search_text(search_query).split()


def build_term_search_query(search_query, fields):
    """Build a Q object requiring every search term to match at least one field."""
    terms = get_search_terms(search_query)
    if not terms:
        return Q()

    combined_query = Q()
    for term in terms:
        term_query = Q()
        for field in fields:
            term_query |= Q(**{f"{field}__icontains": term})
        combined_query &= term_query
    return combined_query


def build_grouped_token_response(options: Iterable[FilterTokenOption], group_order=None):
    """Return Select2 grouped results, optionally honoring an explicit group order."""
    grouped_results = {}
    inserted_groups = []
    for option in options:
        if option.group not in grouped_results:
            grouped_results[option.group] = []
            inserted_groups.append(option.group)
        grouped_results[option.group].append(option.as_select2_result())

    ordered_groups = []
    seen_groups = set()
    for group in group_order or ():
        if (
            group not in seen_groups
            and group in grouped_results
            and grouped_results[group]
        ):
            ordered_groups.append(group)
            seen_groups.add(group)
    for group in inserted_groups:
        if group not in seen_groups and grouped_results[group]:
            ordered_groups.append(group)

    return {
        "results": [
            {"text": group, "children": children}
            for group in ordered_groups
            for children in (grouped_results[group],)
        ]
    }
