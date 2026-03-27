# 🧠 Decision Intelligence System

## 🚀 Overview

This project implements a **domain-agnostic Decision Intelligence Platform** that combines:

* Machine Learning (probabilistic inference)
* Rule-based systems (policy logic)
* SHAP-based explainability (model transparency)
* API + UI layers for real-world usage

---

## 🎯 Key Idea

Most ML systems stop at prediction.

This system goes further:

**Prediction → Decision → Action → Explanation**

---

## 🏗️ Architecture

```
User Input
   ↓
Streamlit UI
   ↓
FastAPI Layer
   ↓
Decision Engine
 ├── ML Model (Prediction)
 ├── Rule Engine (Policy Logic)
 ├── SHAP Explainer
   ↓
Decision Output + Explanation
```

---

## 🔌 Use Cases

### 📊 Customer Retention

* Predict churn probability
* Trigger actions:

  * Offer Discount
  * Send Notification
  * No Action

---

### 🎮 Game AI (Dynamic Difficulty Adjustment)

* Analyze player performance
* Adjust difficulty dynamically:

  * Increase Difficulty
  * Decrease Difficulty
  * Maintain Balance

---

## ⚙️ Tech Stack

* Python
* scikit-learn
* FastAPI
* Streamlit
* SHAP
* JSON-based rule engine

---

## 🧠 System Design Highlights

* Separation of training vs inference pipelines
* Config-driven rule engine (no hardcoding)
* Safe rule evaluation (no eval)
* Multi-domain extensibility
* Explainable AI (SHAP + rule trace)
* API-first architecture

---

## ▶️ How to Run

### 1. Install dependencies

pip install -r requirements.txt

### 2. Train models

python train.py

### 3. Run API

uvicorn api.app:app --reload

### 4. Run UI

streamlit run ui/dashboard.py

---

## 🌐 API Endpoints

| Endpoint      | Description                 |
| ------------- | --------------------------- |
| /predict      | ML prediction only          |
| /decision     | Customer retention decision |
| /decision/dda | Game AI decision            |

---

## 📊 Example Output

```
{
  "score": 0.54,
  "decision": "Send Notification",
  "rule_triggered": "Inactive User",
  "reason": ["days_since_last_login > 30"],
  "model_explanation": {
    "engagement_score": -0.12,
    "days_since_last_login": 0.25
  }
}
```

---

## 🔥 Key Learning

AI systems should not just predict—they should help make decisions.

---

## 🚀 Future Enhancements

* Model versioning
* Feature validation (Pydantic)
* Cloud deployment
* Additional domains (fraud, finance)
