def explain_model(model, features):
    import shap

    explainer = shap.Explainer(model)
    return explainer(features)
