"""
textutils - ett litet bibliotek for textbearbetning.

Moduler:
    slugify  - omvandlar text till URL-sakra strangar
    password - betygsatter och analyserar losenordsstyrka
    stats    - analyserar textstatistik
"""

from textutils.slugify import slugify, truncate_slug
from textutils.password import check_strength, has_common_pattern, WEAK, MEDIUM, STRONG, VERY_STRONG
from textutils.stats import word_count, sentence_count, average_word_length, summarize

__all__ = [
    "slugify",
    "truncate_slug",
    "check_strength",
    "has_common_pattern",
    "WEAK",
    "MEDIUM",
    "STRONG",
    "VERY_STRONG",
    "word_count",
    "sentence_count",
    "average_word_length",
    "summarize",
]
