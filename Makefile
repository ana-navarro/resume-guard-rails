VENV := .venv
ifeq ($(OS),Windows_NT)
	PYTHON := $(VENV)/Scripts/python.exe
else
	PYTHON := $(VENV)/bin/python
endif

.PHONY: install lint test validate-pipeline

install:
	python -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements-dev.txt

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) scripts/gen_coveragerc.py
	$(PYTHON) -m pytest --cov --cov-config=.coveragerc --cov-report=term-missing

validate-pipeline: install lint test
	@echo "validate-pipeline passed: lint + tests + coverage >= 80% (see output above)"
