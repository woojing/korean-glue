# Guidance for Codex Agents

This document provides guidelines for making changes to this open source Python package. Please follow them carefully.

## Prerequisites

- Python 3.10 or newer
- [`uv`](https://github.com/astral-sh/uv)
- [`pre-commit`](https://pre-commit.com/)

## Development Setup

1. **Create and activate the virtual environment:**
   ```bash
   uv sync
   source .venv/bin/activate    # On Windows use: .venv\Scripts\activate
   ```
2. **Set up pre-commit hooks:**
   ```bash
   uv run pre-commit install
   ```

## Quality Checks & Workflow

You can invoke pre-commit manually:
```bash
pre-commit run --all-files
```

### Troubleshooting

If `bash scripts/check.sh` fails because tools are missing, ensure the
development dependencies are installed:

```bash
uv sync
```

Reinstall them whenever you recreate the virtual environment or change the
Python version.

## Pull Requests

- Summarize user-facing changes.
- CI/CD 자동화 검사가 통과해야 합니다. 로컬에서는 `bash scripts/check.sh`로 확인할 수 있습니다.
- Ensure all checks pass before submitting.
- If you update `README.md`, also update `README.ko.md` with the same content in Korean.
