PWD ?= $(error PWD is not set)
VENV_DIR = $(PWD)/.venv
SRC_FILES = $(shell find tests excel_reader -name '*.py') pyproject.toml

.PHONY: test
test: install
	@$(VENV_DIR)/bin/poetry run pytest

.PHONY: build
build: .make.build

.make.build: pyproject.toml
	@python3 -m venv $(VENV_DIR)
	@$(VENV_DIR)/bin/pip3 install poetry
	@touch $@

.PHONY: install
install: build
	@$(VENV_DIR)/bin/poetry install

.PHONY: clean
clean:
	@find . -type d -name __pycache__ -exec rm -r {} \+
	@rm -rf .make.* poetry.lock $(VENV_DIR) .pytest_cache
