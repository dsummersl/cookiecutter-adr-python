.PHONY: setup test lint type adr new coverage vulture fix radon treepeat ci

setup:
	uv venv
	uv sync --python .venv/bin/python

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run ast-grep scan {{ cookiecutter.package_name }} tests

vulture:
	uv run vulture --min-confidence 55 {{ cookiecutter.package_name }}

fix:
	uv run ast-grep scan --update-all {{ cookiecutter.package_name }} tests
	uv run ruff check . --fix
	uv run ruff format .

type:
	uv run mypy

radon:
	uv run .github/scripts/check_radon.sh

treepeat:
	uv run treepeat detect .

ci: test lint type radon vulture
