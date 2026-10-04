from app.models.prediction import Prediction


def is_high_risk(prediction: Prediction, threshold: float = 0.8) -> bool:
    return prediction.risk_score >= threshold
