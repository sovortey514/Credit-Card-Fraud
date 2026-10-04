from xgboost import XGBClassifier


def build_model() -> XGBClassifier:
    return XGBClassifier(
        eval_metric="aucpr", learning_rate=0.05, n_estimators=300, random_state=42
    )
