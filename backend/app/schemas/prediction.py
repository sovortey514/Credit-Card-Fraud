from pydantic import BaseModel, Field


class PredictionRead(BaseModel):
    transaction_id: str
    risk_score: float = Field(ge=0, le=1)
    is_fraud: bool
