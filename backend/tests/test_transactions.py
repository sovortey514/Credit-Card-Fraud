from app.services.transaction_service import normalize_currency


def test_normalize_currency() -> None:
    assert normalize_currency(" usd ") == "USD"
