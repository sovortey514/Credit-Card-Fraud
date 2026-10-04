from fastapi import FastAPI

from app.api.routes import analytics, dashboard, fraud, models, transactions

app = FastAPI(title="Credit Card Fraud Detection API", version="0.1.0")
app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["dashboard"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["transactions"])
app.include_router(fraud.router, prefix="/api/v1/fraud", tags=["fraud"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])
app.include_router(models.router, prefix="/api/v1/models", tags=["models"])


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
