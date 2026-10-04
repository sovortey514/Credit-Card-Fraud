from app.models.transaction import Transaction


def normalize_currency(value: str) -> str:
    return value.strip().upper()
