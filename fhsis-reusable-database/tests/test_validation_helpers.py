from fhsis_reusable_database.validation_helpers import require_keys


def test_require_keys_reports_missing_keys() -> None:
    missing = require_keys({"a": 1}, ["a", "b"])
    assert missing == ["b"]
