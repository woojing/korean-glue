#!/usr/bin/env bash
set -euo pipefail

# Run formatting and linting via pre-commit
pre-commit run --all-files

# Type checking
uv run mypy --ignore-missing-imports src

# Run tests
uv run pytest
