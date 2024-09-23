__all__ = [
    "PATTERNS",
]

import re

from .types import DotDict


PATTERNS = DotDict(
    {
        "YEAR": re.compile(r"[12]\d{3}"),
        "HTML_TAGS": re.compile("<.*?>"),
    }
)
