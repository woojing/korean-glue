"""Basic phonological rules for selecting josa.

This module contains helper functions used by the engine to decide which
josa (Korean particle) should be attached to a word.  The logic goes beyond
simply checking Hangul syllable endings so that digits and latin letters can
also be processed in a reasonable way.  Only a subset of rules is implemented
for demonstration purposes.
"""

# Map single josa to their canonical pairs so that patterns like "은" will
# behave the same as "은/는".
_SINGLE_TO_PAIR = {
    "은": "은/는",
    "는": "은/는",
    "이": "이/가",
    "가": "이/가",
    "을": "을/를",
    "를": "을/를",
    "으로": "으로/로",
    "로": "으로/로",
    "아": "아/야",
    "야": "아/야",
}


def _hangul_has_final(word: str) -> bool:
    """Return True if ``word`` ends with a Hangul syllable that has 받침."""
    code = ord(word[-1]) - 0xAC00
    if 0 <= code <= 11171:
        return (code % 28) != 0
    return False


_FINAL_DIGITS = set("136780")
_NON_FINAL_DIGITS = set("2459")
_FINAL_ALPHABET = set("FHLMNRS")


def has_final_consonant(word: str) -> bool:
    """Return True if ``word`` ends with a final consonant."""
    if not word:
        return False
    last = word[-1]
    if "가" <= last <= "힣":
        return _hangul_has_final(word)
    if last.isdigit():
        if last in _FINAL_DIGITS:
            return True
        if last in _NON_FINAL_DIGITS:
            return False
        # Fallback for other digits: treat as no final consonant
        return False
    if last.isalpha():
        return last.upper() in _FINAL_ALPHABET
    return False


def _has_final_l(word: str) -> bool:
    """Return True if ``word`` ends with the final consonant 'ㄹ'."""
    if not word:
        return False
    last = word[-1]
    if "가" <= last <= "힣":
        code = ord(last) - 0xAC00
        if 0 <= code <= 11171:
            return (code % 28) == 8
        return False
    return last.upper() == "L"


def select_josa(word: str, pattern: str) -> str:
    """Select josa according to phonological rules."""
    # Expand patterns like "은" to "은/는" if possible
    if "/" not in pattern:
        canonical = _SINGLE_TO_PAIR.get(pattern)
        if canonical is None:
            return pattern
        pattern = canonical
    parts = pattern.split("/")
    if len(parts) != 2:
        return pattern
    first, second = parts
    # '(으)로' has a special rule when the word ends with 'ㄹ'
    if pattern == "으로/로" and _has_final_l(word):
        return second
    return first if has_final_consonant(word) else second
