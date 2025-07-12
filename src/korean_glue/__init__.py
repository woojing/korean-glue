"""Public API for korean_glue."""

from .engine import attach, get_josa, auto_attach
from .dictionary import (
    add_exception_rule,
    remove_exception_rule,
    load_user_dictionary,
    get_dictionary_entries,
)
from .exceptions import JosaError, DictionaryError

__all__ = [
    "attach",
    "get_josa",
    "auto_attach",
    "add_exception_rule",
    "remove_exception_rule",
    "load_user_dictionary",
    "get_dictionary_entries",
    "JosaError",
    "DictionaryError",
]
