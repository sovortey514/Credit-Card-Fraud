def explain_prediction(feature_contributions: dict[str, float]) -> list[tuple[str, float]]:
    return sorted(feature_contributions.items(), key=lambda item: abs(item[1]), reverse=True)
