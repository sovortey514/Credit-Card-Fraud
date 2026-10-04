from pydantic import BaseModel, Field


class DashboardMetrics(BaseModel):
    total_transactions: int = Field(ge=0)
    fraud_transactions: int = Field(ge=0)
    fraud_rate: float = Field(ge=0, le=1)
