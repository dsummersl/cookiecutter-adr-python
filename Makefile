.PHONY: help setup test lint type adr new coverage

setup:
    uv sync

test:
    uv run pytest

lint:
    uv run ruff check .

fix:
    uv run ruff check . --fix

type:
    uv run mypy
