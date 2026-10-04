from app.models.prediction import Prediction


def predict(transaction_id: str, risk_score: float) -> Prediction:
    return Prediction(
        transaction_id=transaction_id,
        risk_score=risk_score,
        is_fraud=risk_score >= 0.5,
    )
