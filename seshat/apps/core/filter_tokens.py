from dataclasses import dataclass
from typing import Iterable


TOKEN_SEPARATOR = ":"


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


def build_grouped_token_response(options: Iterable[FilterTokenOption]):
    grouped_results = {}
    for option in options:
        grouped_results.setdefault(option.group, []).append(option.as_select2_result())

    return {
        "results": [
            {"text": group, "children": children}
            for group, children in grouped_results.items()
            if children
        ]
    }
