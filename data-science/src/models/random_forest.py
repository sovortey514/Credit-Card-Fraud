from sklearn.ensemble import RandomForestClassifier


def build_model() -> RandomForestClassifier:
    return RandomForestClassifier(
        class_weight="balanced_subsample", n_estimators=300, random_state=42, n_jobs=-1
    )
