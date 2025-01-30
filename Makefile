# Variables
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs/source
BUILDDIR      = build
PYTHON        = python3
PYTEST        = pytest

# Documentation targets
# Put help first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

docs:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Depencency management
deps-compile:
	pip-compile --output-file=requirements.txt pyproject.toml
	pip-compile --extra-dev, test --output-file=requirements-dev.txt pyproject.toml
	
deps-sync: deps-compile
	pip-sync requirements.txt requirements-dev.txt

deps-update:
	pip-compile --upgrade --output-file=requirements.txt pyproject.toml
	pip-compile --upgrade --extra=dev, test --output-file=requirements-dev.txt pyproject.toml

# Development targets
check-setup:
	@if grep -q "PROJECT_NAME_PLACEHOLDER" pyproject.toml; then \
		echo "Error: Please run 'python setup_template.py' first"; \
		exit 1; \
	fi
install: check-setup
	$(PYTHON) -m pip install -e '.[dev,test]'

.PHONY: check-setup

test:
	$(PYTEST) --cov=src --cov-report=term-missing tests/

format:
	black src tests
	isort src tests

lint:
	flake8 src tests
	mypy src tests

# Cleanup
clean:
	rm -rf $(BUILDDIR)/*
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf src/*.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

.PHONY: help docs install test format lint clean Makefile