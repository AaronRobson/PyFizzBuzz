.DEFAULT_GOAL := all

.PHONY: all
all: check test run

.PHONY: check
check: lint typecheck

.PHONY: lint
lint:
	flake8 .

.PHONY: typecheck
typecheck:
	mypy .

.PHONY: test
test:
	python3 -m unittest

.PHONY: run
run:
	python3 fizzbuzz.py
