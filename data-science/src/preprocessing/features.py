import pandas as pd


def add_time_features(frame: pd.DataFrame, timestamp_column: str) -> pd.DataFrame:
    result = frame.copy()
    timestamp = pd.to_datetime(result[timestamp_column], utc=True)
    result["transaction_hour"] = timestamp.dt.hour
    result["transaction_day"] = timestamp.dt.dayofweek
    return result
