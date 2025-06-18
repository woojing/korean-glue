# Contributing

Thank you for considering contributing to **korean_glue**. The steps below set up a local development environment.

```bash
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
uv pip install -e ".[dev]"
pre-commit install
```

Run the full test suite with:

```bash
bash scripts/check.sh
```

