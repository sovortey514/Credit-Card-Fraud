from dataclasses import dataclass


@dataclass
class FraudAlert:
    transaction_id: str
    risk_score: float
    status: str = "open"
