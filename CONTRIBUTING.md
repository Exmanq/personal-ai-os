# Contributing

## Getting started
- Clone the repo and run `make setup` (creates `.venv`, installs dev deps, editable install).
- Activate the env: `source .venv/bin/activate` (or `.venv\Scripts\activate` on Windows).

## Commands
- Lint: `make lint` (ruff + black check)
- Tests: `make test`
- Format: `make format`
- Demo: `make demo` (writes outputs to `examples/output`)
- Doctor: `make doctor`

## Commit style
- Use concise, descriptive messages (e.g., `add reflection tests`, `improve demo data`).

## Adding features
- Add tests for new behaviors.
- Update docs (README, docs/CONFIG.md, docs/ARCHITECTURE.md) if you change flows.
- Keep `examples/output` in sync when demo behavior changes.

## Pull requests
- Follow templates in `.github/`.
- Ensure CI is green (lint + tests).
