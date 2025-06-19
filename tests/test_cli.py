import subprocess
import sys


def run_cli(arg: str) -> str:
    result = subprocess.run(
        [sys.executable, "-m", "korean_glue", arg],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def test_cli_basic():
    assert run_cli("철수(은/는)") == "철수는"
    assert run_cli("철수(은)") == "철수는"
    assert run_cli("K(이/가)") == "K가"
    assert run_cli("3(을/를)") == "3을"
