from app.models.prediction import Prediction
from app.services.fraud_service import is_high_risk


def test_high_risk_threshold() -> None:
    assert is_high_risk(Prediction("tx-1", 0.9, True))
