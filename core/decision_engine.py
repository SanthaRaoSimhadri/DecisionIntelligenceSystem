"""
Decision Engine (Enhanced)

- Selects highest priority rule
- Returns explainable output
"""

from core.model import predict_proba


class DecisionEngine:
    def __init__(self, model, rule_engine, explainability_engine=None):
        self.model = model
        self.rule_engine = rule_engine
        self.explainability_engine = explainability_engine

    def make_decision(self, input_df):
        prob = predict_proba(self.model, input_df)[0]
        features = input_df.iloc[0].to_dict()

        rule_results = self.rule_engine.evaluate(features, prob)
        if self.explainability_engine:
            shap_values = self.explainability_engine.explain(input_df)
        else:
            shap_values = {}

        if rule_results:
            # Sort by priority (lower = higher priority)
            best_rule = sorted(rule_results, key=lambda x: x["priority"])[0]

            decision = {
                "score": prob,  # generic name
                "decision": best_rule["action"],
                "rule_triggered": best_rule["rule"],
                "reason": best_rule["reasons"],
                "model_explanation": shap_values
            }
        else:
             decision = {
                "score": prob,  # generic name
                "decision": "No Action",
                "rule_triggered": None,
                "reason": ["No rules matched"],
                "model_explanation": shap_values
            }

        

        return decision