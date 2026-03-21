"""
Main Entry Point

Runs the full pipeline:
- Data generation
- Model training
- Decision inference
"""

import pandas as pd

from use_cases.customer_retention.data_pipeline import generate_synthetic_data
from core.model import train_model
from core.rule_engine import RuleEngine
from core.decision_engine import DecisionEngine

# Step 1: Generate data
df = generate_synthetic_data()

# Step 2: Train model
model = train_model(df)

# Step 3: Initialize rule engine
rule_engine = RuleEngine("use_cases/customer_retention/rules.json")

# Step 4: Initialize decision engine
decision_engine = DecisionEngine(model, rule_engine)

# Step 5: Test with a sample input
sample_input = df.drop("churn", axis=1).iloc[[0]]

decision = decision_engine.make_decision(sample_input)

print("\nFinal Decision Output:\n")
print(decision)