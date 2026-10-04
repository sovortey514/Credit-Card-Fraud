import pandas as pd


def clean_transactions(frame: pd.DataFrame) -> pd.DataFrame:
    cleaned = frame.drop_duplicates().copy()
    cleaned.columns = [column.strip().lower().replace(" ", "_") for column in cleaned.columns]
    return cleaned
