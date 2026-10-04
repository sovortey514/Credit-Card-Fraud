from pathlib import Path


def get_model_path() -> Path:
    return Path(__file__).resolve().parents[3] / "data-science" / "models" / "fraud_model.pkl"
