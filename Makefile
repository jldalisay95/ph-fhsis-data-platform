.PHONY: setup check test fmt

setup:
	python -m pip install -e .[dev]

check:
	ruff check .
	python -m json.tool fhsis-reusable-database/schemas/fhsis_schema_bundle.json > /dev/null

test:
	pytest -q

fmt:
	ruff format .
