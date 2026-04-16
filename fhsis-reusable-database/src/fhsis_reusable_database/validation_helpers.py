"""Validation utility stubs for schema and quality checks."""


def require_keys(record: dict, keys: list[str]) -> list[str]:
    """Return missing required keys.

    TODO: replace with JSON schema-backed validation in implementation phase.
    """
    return [key for key in keys if key not in record]
