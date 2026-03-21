"""
FastAPI Application (Production Version)

Loads pre-trained model instead of training at runtime
"""

from fastapi import FastAPI
import pandas as pd
import joblib

from core.model import predict_proba
from core.rule_engine import RuleEngine
from core.decision_engine import DecisionEngine

MODEL_PATH = "models/churn_model.pkl"

app = FastAPI(title="Decision Intelligence API")

print("🔄 Loading model...")

# Load trained model
model = joblib.load(MODEL_PATH)

# Load rule engine
rule_engine = RuleEngine("use_cases/customer_retention/rules.json")

# Initialize decision engine
decision_engine = DecisionEngine(model, rule_engine)

DDA_MODEL_PATH = "models/dda_model.pkl"

dda_model = joblib.load(DDA_MODEL_PATH)
dda_rule_engine = RuleEngine("use_cases/dda_game/rules.json")
dda_decision_engine = DecisionEngine(dda_model, dda_rule_engine)

print("✅ System ready!")

@app.get("/")
def root():
    return {"message": "Decision Intelligence API is running"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict")
def predict(input_data: dict):
    input_df = pd.DataFrame([input_data])
    prob = predict_proba(model, input_df)[0]

    return {"churn_probability": float(prob)}

@app.post("/decision")
def decision(input_data: dict):
    input_df = pd.DataFrame([input_data])
    return decision_engine.make_decision(input_df)

@app.post("/decision/dda")
def dda_decision(input_data: dict):
    input_df = pd.DataFrame([input_data])
    return dda_decision_engine.make_decision(input_df)