from sklearn.linear_model import LogisticRegression


def build_model() -> LogisticRegression:
    return LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42)
