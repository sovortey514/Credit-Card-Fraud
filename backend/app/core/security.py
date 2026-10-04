def redact_sensitive_value(value: str) -> str:
    if len(value) < 5:
        return "*" * len(value)
    return f"{value[:2]}{'*' * (len(value) - 4)}{value[-2:]}"
