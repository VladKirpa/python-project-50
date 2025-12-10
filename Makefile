install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

lint:
	uv run ruff check --fix

test:
	uv run pytest

check: test lint

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml



