from datetime import datetime

from pydantic import BaseModel, Field


class TransactionRead(BaseModel):
    id: str
    amount: float = Field(ge=0)
    currency: str
    timestamp: datetime
