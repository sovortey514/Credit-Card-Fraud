from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    id: str
    amount: float
    currency: str
    timestamp: datetime
