from korean_glue.integrations import jinja_filters
from jinja2 import Environment
from django.template import Engine, Context
from django.conf import settings
import django

if not settings.configured:
    settings.configure(
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
            }
        ]
    )
django.setup()


def test_jinja_filter_basic():
    env = Environment()
    jinja_filters.register(env)
    template = env.from_string("{{ word|josa('으로/로') }}")
    result = template.render(word="서울")
    assert result == "서울로"


def test_jinja_filter_single():
    env = Environment()
    jinja_filters.register(env)
    template = env.from_string("{{ word|josa('은') }}")
    result = template.render(word="철수")
    assert result == "철수는"


def test_jinja_filter_non_string():
    env = Environment()
    jinja_filters.register(env)
    template = env.from_string("{{ value|josa('을/를') }}")
    result = template.render(value=10)
    assert result == "10"


def test_django_filter_basic():
    engine = Engine(builtins=["korean_glue.integrations.django_tags"])
    template = engine.from_string("{{ word|josa:'이/가' }}")
    result = template.render(Context({"word": "사과"}))
    assert result == "사과가"


def test_django_filter_single():
    engine = Engine(builtins=["korean_glue.integrations.django_tags"])
    template = engine.from_string("{{ word|josa:'은' }}")
    result = template.render(Context({"word": "철수"}))
    assert result == "철수는"


def test_django_filter_non_string():
    engine = Engine(builtins=["korean_glue.integrations.django_tags"])
    template = engine.from_string("{{ value|josa:'을/를' }}")
    result = template.render(Context({"value": 10}))
    assert result == "10"
