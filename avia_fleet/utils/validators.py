import re


def validate_tail_number(pattern: str) -> bool:
    """Validate an aircraft tail number."""
    regex = r"^[A-Z]{2}-\d{4,5}$"
    return bool(re.fullmatch(regex, pattern))
