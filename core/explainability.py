"""
Explainability Module

Provides basic explanation using feature contribution (placeholder for SHAP).
"""


def explain_decision(features, prediction):
    explanation = {
        "prediction": prediction,
        "top_factors": sorted(features.items(), key=lambda x: abs(x[1]), reverse=True)
    }

    return explanation