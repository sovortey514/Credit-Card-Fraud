from app.schemas.analytics import FraudBucket


def empty_bucket(label: str) -> FraudBucket:
    return FraudBucket(label=label, transaction_count=0, fraud_count=0)
