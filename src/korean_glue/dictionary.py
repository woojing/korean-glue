"""Manage exception dictionary for josa selection."""

from typing import Dict, Tuple, Optional

from .rules import _SINGLE_TO_PAIR

_EXCEPTION_DICT: Dict[Tuple[str, str], str] = {}


def lookup_exception(word: str, pattern: str) -> Optional[str]:
    """Return josa from exception dictionary if present."""
    result = _EXCEPTION_DICT.get((word, pattern))
    if result is not None:
        return result
    canonical = _SINGLE_TO_PAIR.get(pattern)
    if canonical is not None:
        return _EXCEPTION_DICT.get((word, canonical))
    return None


def add_exception_rule(word: str, pattern: str, output: str) -> None:
    """Add a custom exception rule."""
    _EXCEPTION_DICT[(word, pattern)] = output


def remove_exception_rule(word: str, pattern: str) -> None:
    """Remove a custom exception rule."""
    _EXCEPTION_DICT.pop((word, pattern), None)


def load_user_dictionary(path: str) -> None:
    """Load rules from a JSON or YAML file."""
    # Placeholder for future implementation
    pass


def get_dictionary_entries() -> Dict[Tuple[str, str], str]:
    """Return a copy of current dictionary entries."""
    return dict(_EXCEPTION_DICT)
