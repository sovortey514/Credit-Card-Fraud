from app.services.dashboard_service import empty_dashboard_metrics


def test_empty_dashboard_metrics() -> None:
    metrics = empty_dashboard_metrics()
    assert metrics.total_transactions == 0
    assert metrics.fraud_rate == 0
