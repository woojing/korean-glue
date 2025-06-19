#!/usr/bin/env bash
set -euo pipefail

# Run formatting and linting via pre-commit
pre-commit run --all-files

# Validate GitHub Actions workflows
if ! command -v actionlint >/dev/null; then
  bash <(curl -fsSL https://raw.githubusercontent.com/rhysd/actionlint/main/scripts/download-actionlint.bash)
  ACTIONLINT=./actionlint
else
  ACTIONLINT=$(command -v actionlint)
fi
$ACTIONLINT
if [ "$ACTIONLINT" = "./actionlint" ]; then
  rm ./actionlint
fi

# Type checking
uv run mypy --ignore-missing-imports src

# Run tests
uv run pytest
