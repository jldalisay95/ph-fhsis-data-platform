"""Provenance/checksum helper stubs."""
import hashlib
from pathlib import Path


def file_sha256(path: str | Path) -> str:
    """Compute SHA256 for a file path."""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
