# Guidance for Codex Agents

This document provides guidelines for making changes to this open source Python package. Please follow them carefully.

## Prerequisites

- Python 3.10 or newer
- [`uv`](https://github.com/astral-sh/uv)
- [`pre-commit`](https://pre-commit.com/)

## Development Setup

1. **Create and activate the virtual environment:**
   ```bash
   uv venv
   source .venv/bin/activate    # On Windows use: .venv\Scripts\activate
   ```
2. **Install dependencies:**
   ```bash
   uv pip install -e ".[dev]"
   ```
3. **Set up pre-commit hooks:**
   ```bash
   pre-commit install
   ```

## Quality Checks & Workflow

Run all checks with the helper script:

```bash
bash scripts/check.sh
```

The script runs formatting and linting via `pre-commit`, then type checks with `mypy` and runs the test suite with `pytest`.

You can also invoke pre-commit manually:
```bash
pre-commit run --all-files
```

### Troubleshooting

If `bash scripts/check.sh` fails because tools are missing, ensure the
development dependencies are installed:

```bash
uv pip install -e ".[dev]"
```

Reinstall them whenever you recreate the virtual environment or change the
Python version.

## Pull Requests

- Summarize user-facing changes.
- CI/CD 자동화 검사가 통과해야 합니다. 로컬에서는 `bash scripts/check.sh`로 확인할 수 있습니다.
- Ensure all checks pass before submitting.
