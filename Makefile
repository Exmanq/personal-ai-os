PYTHON := python3
VENV := .venv
PIP := $(VENV)/bin/pip
PYTHON_BIN := $(VENV)/bin/python

.DEFAULT_GOAL := help

help:
	@echo "Targets: setup, lint, test, demo, doctor, clean"

$(VENV):
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip

setup: $(VENV)
	$(PIP) install -e .
	$(PIP) install -e .[dev]
	@echo "Setup complete. Activate with 'source $(VENV)/bin/activate'"

lint: $(VENV)
	$(VENV)/bin/ruff check src tests
	$(VENV)/bin/black --check src tests

format: $(VENV)
	$(VENV)/bin/black src tests
	$(VENV)/bin/ruff check --fix src tests

precommit: $(VENV)
	$(VENV)/bin/pre-commit run --all-files

test: $(VENV)
	$(VENV)/bin/pytest

# Demo creates real outputs in examples/output

demo: $(VENV)
	$(PYTHON_BIN) -m personal_ai_os.cli add-note "Demo note: shipped CLI" --tags demo
	$(PYTHON_BIN) -m personal_ai_os.cli set-goal "Demo goal: deliver wow" --deadline 2026-02-20
	$(PYTHON_BIN) -m personal_ai_os.cli plan-week > examples/output/plan.json
	$(PYTHON_BIN) -m personal_ai_os.cli daily-reflect > examples/output/reflection.json
	@echo "Demo outputs written to examples/output"

# Doctor checks environment basics

doctor:
	$(PYTHON) -c "import sys; import json; import platform; print(json.dumps({'python': sys.version.split()[0], 'platform': platform.platform()}, indent=2))"
	@echo "Run 'paios doctor' for data-dir checks"

clean:
	rm -rf $(VENV) .pytest_cache .ruff_cache .mypy_cache .coverage htmlcov
