<!-- README.ko.md -->
[English](README.md)

# korean_glue (한국어)

[![CI](https://github.com/woojing/korean-glue/actions/workflows/ci.yml/badge.svg)](https://github.com/woojing/korean-glue/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%20|%203.11%20|%203.12%20|%203.13-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/woojing/korean-glue)](LICENSE)

규칙 기반과 예외 사전을 결합한 현대적인 한국어 조사 처리 파이썬 라이브러리입니다. Django 템플릿 태그와 Jinja2 필터를 제공하여 웹 프레임워크에서도 간편하게 사용할 수 있습니다. `은/는`처럼 두 조사를 함께 주거나 `은`처럼 하나만 줘도 자동으로 올바른 형태를 선택합니다.

## 설치

```bash
pip install korean_glue
```

프로젝트에서 Django나 Jinja2를 함께 사용한다면 추가 패키지가 필요합니다.

## 사용 방법

### 기본 API

```python
from korean_glue import attach, get_josa

print(get_josa("사과", "은/는"))  # "는"
print(get_josa("철수", "은"))    # "는"
print(attach("사과", "은/는"))    # "사과는"
print(attach("철수", "은"))      # "철수는"
```

### 사용자 정의 예외 규칙

```python
from korean_glue import add_exception_rule, remove_exception_rule, attach

add_exception_rule("사과", "은/는", "당")
print(attach("사과", "은/는"))  # "사과당"
remove_exception_rule("사과", "은/는")
```

### CLI 사용 예

패키지를 설치한 뒤 `kglue` 명령어로 간단히 확인할 수 있습니다.

```bash
kglue '철수(은)'
kglue 'K(이/가)'
kglue '3(을/를)'
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

개발 환경을 준비한 뒤 다음 명령어로 테스트를 실행합니다(자세한 내용은 `CONTRIBUTING.md` 참고).

```bash
pytest
```
