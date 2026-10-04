from dataclasses import dataclass


@dataclass
class Prediction:
    transaction_id: str
    risk_score: float
    is_fraud: bool
