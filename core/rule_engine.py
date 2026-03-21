"""
Safe Rule Engine (No eval)

Evaluates structured rules using operators.
"""

import json


class RuleEngine:
    def __init__(self, rule_file_path):
        with open(rule_file_path, "r") as f:
            self.rules = json.load(f)["rules"]

    def _evaluate_condition(self, feature_value, operator, target_value):
        if operator == ">":
            return feature_value > target_value
        elif operator == "<":
            return feature_value < target_value
        elif operator == ">=":
            return feature_value >= target_value
        elif operator == "<=":
            return feature_value <= target_value
        elif operator == "==":
            return feature_value == target_value
        else:
            raise ValueError(f"Unsupported operator: {operator}")

    def evaluate(self, features, prediction):
        results = []

        # Inject prediction into feature space
        features = features.copy()
        features["churn_prob"] = prediction

        for rule in self.rules:
            conditions_met = True
            reasons = []

            for cond in rule["conditions"]:
                feature = cond["feature"]
                operator = cond["operator"]
                value = cond["value"]

                feature_value = features.get(feature)

                if feature_value is None:
                    conditions_met = False
                    break

                if self._evaluate_condition(feature_value, operator, value):
                    reasons.append(f"{feature} {operator} {value}")
                else:
                    conditions_met = False
                    break

            if conditions_met:
                results.append({
                    "rule": rule["name"],
                    "action": rule["action"],
                    "priority": rule.get("priority", 999),
                    "reasons": reasons
                })

        return results