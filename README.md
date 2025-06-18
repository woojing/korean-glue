<!-- README.md -->
[한국어](README.ko.md)

# korean_glue

[![CI](https://github.com/woojing/korean-glue/actions/workflows/ci.yml/badge.svg)](https://github.com/woojing/korean-glue/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12%20|%203.13-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/woojing/korean-glue)](LICENSE)

A modern Python library for Korean josa processing combining rule-based and dictionary-based approaches. Django template tags and Jinja2 filters are included for easy web framework integration.

## Installation

```bash
pip install korean_glue
```

Framework integrations rely on Django and Jinja2.

## Usage

### Basic API

```python
from korean_glue import attach, get_josa

print(get_josa("사과", "은/는"))  # "는"
print(attach("사과", "은/는"))    # "사과는"
```

### Custom Exception Rules

```python
from korean_glue import add_exception_rule, remove_exception_rule, attach

add_exception_rule("사과", "은/는", "당")
print(attach("사과", "은/는"))  # "사과당"
remove_exception_rule("사과", "은/는")
```

### Command Line

Install the package and run the `kglue` command:

```bash
kglue '철수(은/는)'
kglue 'K(이/가)'
kglue '3(을/를)'
```

### Framework Integrations

**Django**

```django
{{ variable|josa:"을/를" }}
```

**Jinja2**

```python
from korean_glue.integrations import jinja_filters
from jinja2 import Environment

env = Environment()
jinja_filters.register(env)
result = env.from_string("{{ word|josa('으로/로') }}").render(word="서울")
```

## Running Tests

After setting up a development environment (see `CONTRIBUTING.md`), run:

```bash
pytest
```

