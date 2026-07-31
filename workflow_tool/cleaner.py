"""Defensive JSON-record cleaning."""

import json
from pathlib import Path
from typing import Any


def clean_records(value: Any) -> tuple[list[dict[str, str]], list[str]]:
    """Normalize valid name/email records and return explicit row errors."""
    if not isinstance(value, list):
        raise ValueError("input must be a JSON array")
    cleaned: list[dict[str, str]] = []
    errors: list[str] = []
    for index, record in enumerate(value, start=1):
        if not isinstance(record, dict):
            errors.append(f"record {index}: expected object")
            continue
        name = " ".join(str(record.get("name", "")).split())
        email = str(record.get("email", "")).strip().lower()
        if not name or "@" not in email or email.startswith("@") or email.endswith("@"):
            errors.append(f"record {index}: valid name and email required")
            continue
        cleaned.append({"name": name, "email": email})
    return cleaned, errors


def clean_file(source: Path, destination: Path) -> list[str]:
    """Clean one UTF-8 JSON file and write deterministic formatted output."""
    try:
        value = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"could not read input: {error}") from error
    cleaned, errors = clean_records(value)
    destination.write_text(json.dumps(cleaned, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return errors
