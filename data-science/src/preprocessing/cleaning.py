import re

import numpy as np
import pandas as pd

from .features import add_time_features


def _normalize_column_name(column: str) -> str:
    name = str(column).strip()
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    return re.sub(r"[^0-9a-zA-Z]+", "_", name).strip("_").lower()


def clean_transactions(frame: pd.DataFrame) -> pd.DataFrame:
    cleaned = frame.copy()
    cleaned.columns = [_normalize_column_name(column) for column in cleaned.columns]
    if cleaned.columns.duplicated().any():
        raise ValueError("Column normalization produced duplicate column names.")
    return cleaned.drop_duplicates().reset_index(drop=True)


def clean_ieee_cis_data(
    transactions: pd.DataFrame,
    identities: pd.DataFrame,
) -> pd.DataFrame:
    """Clean and join IEEE-CIS training transactions and identity records."""
    transactions = clean_transactions(transactions)
    identities = clean_transactions(identities)

    required_columns = {"transaction_id", "transaction_dt", "transaction_amt", "is_fraud"}
    missing_columns = required_columns.difference(transactions.columns)
    if missing_columns:
        raise ValueError(f"Transaction data is missing required columns: {sorted(missing_columns)}")
    if "transaction_id" not in identities.columns:
        raise ValueError("Identity data is missing the transaction_id column.")
    if transactions["transaction_id"].isna().any():
        raise ValueError("Transaction data contains null transaction_id values.")
    if identities["transaction_id"].isna().any():
        raise ValueError("Identity data contains null transaction_id values.")
    if transactions["transaction_id"].duplicated().any():
        raise ValueError("Transaction data contains duplicate transaction_id values.")
    if transactions["is_fraud"].isna().any():
        raise ValueError("Training data contains null is_fraud labels.")
    if not transactions["is_fraud"].isin([0, 1, False, True]).all():
        raise ValueError("is_fraud must contain only binary 0/1 labels.")

    identity_ids = identities["transaction_id"]
    combined = transactions.merge(
        identities,
        on="transaction_id",
        how="left",
        validate="one_to_one",
    )
    combined["has_identity"] = combined["transaction_id"].isin(identity_ids).astype("int8")
    combined = add_time_features(combined, "transaction_dt")

    amount = pd.to_numeric(combined["transaction_amt"], errors="raise")
    if (amount.dropna() < 0).any():
        raise ValueError("transaction_amt contains negative values.")
    combined["transaction_amt"] = amount
    combined["transaction_amt_log"] = np.log1p(amount)
    return combined


def temporal_train_test_split(
    frame: pd.DataFrame,
    train_fraction: float = 0.8,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split chronologically, keeping records with the same time together."""
    if not 0 < train_fraction < 1:
        raise ValueError("train_fraction must be between 0 and 1.")
    if "transaction_dt" not in frame.columns:
        raise ValueError("Data must contain transaction_dt for a temporal split.")
    if frame["transaction_dt"].isna().any():
        raise ValueError("transaction_dt contains null values.")
    if len(frame) < 2:
        raise ValueError("At least two rows are required for a train/test split.")

    ordered = frame.sort_values("transaction_dt", kind="mergesort").reset_index(drop=True)
    split_position = min(max(int(len(ordered) * train_fraction), 1), len(ordered) - 1)
    cutoff = ordered.loc[split_position, "transaction_dt"]

    train = ordered.loc[ordered["transaction_dt"] < cutoff].copy()
    test = ordered.loc[ordered["transaction_dt"] >= cutoff].copy()
    if train.empty or test.empty:
        raise ValueError("The temporal cutoff produced an empty train or test set.")

    return train.reset_index(drop=True), test.reset_index(drop=True)
