import pandas as pd


def add_time_features(frame: pd.DataFrame, timestamp_column: str) -> pd.DataFrame:
    result = frame.copy()
    elapsed_seconds = pd.to_numeric(result[timestamp_column], errors="raise")
    if elapsed_seconds.isna().any():
        raise ValueError(f"{timestamp_column} contains null values.")
    result["transaction_hour"] = ((elapsed_seconds // 3600) % 24).astype("int8")
    result["transaction_day"] = (elapsed_seconds // 86400).astype("int16")
    return result
