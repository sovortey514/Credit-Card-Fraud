from pydantic import BaseModel


class FraudBucket(BaseModel):
    label: str
    transaction_count: int
    fraud_count: int
