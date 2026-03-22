"""
SHAP Explainability Module
"""

import shap
import pandas as pd


class ExplainabilityEngine:
    def __init__(self, model, background_data):
        """
        background_data: sample dataset used for SHAP baseline
        """
        self.model = model
        self.explainer = shap.Explainer(model, background_data)

    def explain(self, input_df):
        shap_values = self.explainer(input_df)

        values = shap_values.values

        # Handle multi-class case
        if len(values.shape) == 3:
            # (samples, features, classes)
            predicted_class = self.model.predict(input_df)[0]

            feature_contributions = {}

            for i, col in enumerate(input_df.columns):
                feature_contributions[col] = float(values[0][i][predicted_class])

        else:
            # Binary case
            feature_contributions = {}

            for i, col in enumerate(input_df.columns):
                feature_contributions[col] = float(values[0][i])

        return feature_contributions