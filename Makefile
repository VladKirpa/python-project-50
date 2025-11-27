install:
	uv sync

gendiff:
	uv run gendiff


build:
	uv build

lint:
	uv run ruff check --fix

	
	