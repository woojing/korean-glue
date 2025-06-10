import pytest

from korean_glue import (
    attach,
    get_josa,
    add_exception_rule,
    remove_exception_rule,
)


def test_basic_josa():
    assert get_josa("사과", "은/는") == "는"
    assert attach("사과", "은/는") == "사과는"


@pytest.mark.parametrize(
    "word,pattern,expected",
    [
        ("학생", "이/가", "학생이"),
        ("교실", "은/는", "교실은"),
        ("책", "을/를", "책을"),
        ("서울", "으로/로", "서울로"),
        ("이메일", "으로/로", "이메일로"),
        ("나무", "으로/로", "나무로"),
        ("철수", "아/야", "철수야"),
        ("3", "이/가", "3이"),
        ("5", "은/는", "5는"),
        ("10", "을/를", "10을"),
        ("M", "은/는", "M은"),
        ("K", "이/가", "K가"),
        ("L", "으로/로", "L로"),
        ("프로젝트", "은/는", "프로젝트는"),
        ("나에게", "만", "나에게만"),
    ],
)
def test_various_cases(word, pattern, expected):
    assert attach(word, pattern) == expected


def test_exception_rule():
    add_exception_rule("사과", "은/는", "딱")
    try:
        assert attach("사과", "은/는") == "사과딱"
    finally:
        remove_exception_rule("사과", "은/는")
