#!/usr/bin/env bash
set -euo pipefail

# Validate GitHub Actions workflows
if ! command -v actionlint >/dev/null; then
  bash <(curl -fsSL https://raw.githubusercontent.com/rhysd/actionlint/main/scripts/download-actionlint.bash)
  ACTIONLINT=./actionlint
else
  ACTIONLINT=$(command -v actionlint)
fi
$ACTIONLINT