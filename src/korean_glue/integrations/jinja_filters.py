"""Jinja2 filters for korean_glue."""

from jinja2 import Environment

from ..engine import attach, auto_attach


def josa_filter(word, pattern):
    if not isinstance(word, str):
        return word
    return attach(word, pattern)


def josa_text_filter(text):
    if not isinstance(text, str):
        return text
    return auto_attach(text)


def register(env: Environment) -> None:
    env.filters["josa"] = josa_filter
    env.filters["josa_text"] = josa_text_filter
