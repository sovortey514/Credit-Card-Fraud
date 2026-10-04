from app.schemas.dashboard import DashboardMetrics


def empty_dashboard_metrics() -> DashboardMetrics:
    return DashboardMetrics(total_transactions=0, fraud_transactions=0, fraud_rate=0.0)
