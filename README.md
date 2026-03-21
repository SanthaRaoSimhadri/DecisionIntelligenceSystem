🧠 Decision Intelligence System
🚀 Overview

This project implements a domain-agnostic Decision Intelligence Platform that combines:

Machine Learning (probabilistic inference)

Rule-based systems (policy logic)

Explainability (transparent decisions)

API + UI layers for real-world usage

🎯 Key Idea

Traditional ML systems stop at predictions.

This system goes further:

Prediction → Decision → Action → Explanation

🏗️ Architecture
User Input
   ↓
FastAPI Layer
   ↓
Decision Engine
 ├── ML Model (Prediction)
 ├── Rule Engine (Policy Logic)
   ↓
Decision Output + Explanation
🔌 Use Cases
📊 1. Customer Retention

Predict churn probability

Actions:

Offer Discount

Send Notification

No Action

🎮 2. Game AI (Dynamic Difficulty Adjustment)

Analyze player performance

Actions:

Increase Difficulty

Decrease Difficulty

Maintain Balance

⚙️ Tech Stack

Python

scikit-learn

FastAPI

Streamlit

JSON-based rule engine

🧠 System Design Highlights

✅ Separation of training vs inference

✅ Config-driven rule engine (no hardcoding)

✅ Safe rule evaluation (no eval)

✅ Multi-domain extensibility

✅ Explainable decisions

✅ API-first architecture

▶️ How to Run
1. Install dependencies
pip install -r requirements.txt
2. Train models
python train.py
3. Run API
uvicorn api.app:app --reload
4. Run UI
streamlit run ui/dashboard.py
🌐 API Endpoints
Endpoint	Description
/predict	ML prediction only
/decision	Full decision system
/decision/dda	DDA game decision
📊 Example Output
{
  "score": 0.54,
  "decision": "Send Notification",
  "rule_triggered": "Inactive User",
  "reason": ["days_since_last_login > 30"]
}
🔥 Key Learning

“AI systems should not just predict—they should help make decisions.”

🚀 Future Enhancements

SHAP-based explainability

Model versioning

Feature validation (Pydantic)

Cloud deployment
