"""Django template filters for korean_glue."""

from django import template  # type: ignore

from ..engine import attach, auto_attach

register = template.Library()


@register.filter(name="josa")
def josa_filter(word, pattern):
    if not isinstance(word, str):
        return word
    return attach(word, pattern)


@register.filter(name="josa_text")
def josa_text_filter(text):
    if not isinstance(text, str):
        return text
    return auto_attach(text)
