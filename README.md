# korean_glue

A modern Python library for Korean josa processing combining rule-based and dictionary-based approaches. Django template tags and Jinja2 filters are included for easy web framework integration.

## Installation

```bash
pip install korean_glue
```

Optional extras are provided for Django and Jinja2 integration:

```bash
pip install korean_glue[django]
pip install korean_glue[jinja]
```

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

add_exception_rule("사과", "은/는", "딱")
print(attach("사과", "은/는"))  # "사과딱"
remove_exception_rule("사과", "은/는")
```

### Framework Integrations

**Django**

```python
# in a Django template
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

Install development dependencies and run:

```bash
pip install -e .[dev]
pytest
```

---

# korean_glue (한국어)

규칙 기반과 예외 사전을 결합한 현대적인 한국어 조사 처리 파이썬 라이브러리입니다. Django 템플릿 태그와 Jinja2 필터를 제공하여 웹 프레임워크에서도 간편하게 사용할 수 있습니다.

## 설치

```bash
pip install korean_glue
```

Django와 Jinja2 연동을 위한 추가 기능은 다음과 같이 설치합니다.

```bash
pip install korean_glue[django]
pip install korean_glue[jinja]
```

## 사용 방법

### 기본 API

```python
from korean_glue import attach, get_josa

print(get_josa("사과", "은/는"))  # "는"
print(attach("사과", "은/는"))    # "사과는"
```

### 사용자 정의 예외 규칙

```python
from korean_glue import add_exception_rule, remove_exception_rule, attach

add_exception_rule("사과", "은/는", "딱")
print(attach("사과", "은/는"))  # "사과딱"
remove_exception_rule("사과", "은/는")
```

### 프레임워크 연동

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

## 테스트 실행

개발용 의존성을 설치한 후 다음 명령어를 실행합니다.

```bash
pip install -e .[dev]
pytest
```
