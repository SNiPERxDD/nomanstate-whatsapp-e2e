def normalize_name(value: str) -> str:
    """Normalize whitespace and title-case a candidate name."""
    return " ".join(value.split()).title()
