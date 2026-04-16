"""Source manifest loading helpers.

TODO: enforce full schema validation against source manifest spec.
"""
from pathlib import Path
import yaml


def load_source_manifest(path: str | Path) -> dict:
    """Load a YAML source manifest file.

    Returns parsed dictionary without domain-level assertions.
    """
    with Path(path).open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}
