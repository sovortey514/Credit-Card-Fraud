from app.models.alert import FraudAlert


class AlertRepository:
    def list_alerts(self) -> list[FraudAlert]:
        return []
