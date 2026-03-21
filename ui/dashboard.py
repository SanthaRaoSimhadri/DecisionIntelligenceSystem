"""
Streamlit Dashboard

- Takes user input
- Calls Decision Intelligence API
- Displays results
"""

import streamlit as st
import requests

st.set_page_config(page_title="Decision Intelligence System", layout="centered")

st.title("🧠 Decision Intelligence System")

use_case = st.selectbox(
    "Select Use Case",
    ["Customer Retention", "DDA Game AI"]
)

st.markdown("---")

# Input Form
st.header("📥 Input Features")

if use_case == "Customer Retention":
    API_URL = "http://127.0.0.1:8000/decision"

    engagement_score = st.slider("Engagement Score", 0.0, 1.0, 0.5)
    days_since_last_login = st.number_input("Days Since Last Login", 0, 100, 10)
    avg_session_time = st.number_input("Avg Session Time", 0.0, 100.0, 10.0)
    num_transactions = st.number_input("Number of Transactions", 0, 20, 3)
    support_tickets = st.number_input("Support Tickets", 0, 10, 1)

    payload = {
        "engagement_score": engagement_score,
        "days_since_last_login": days_since_last_login,
        "avg_session_time": avg_session_time,
        "num_transactions": num_transactions,
        "support_tickets": support_tickets
    }

else:
    API_URL = "http://127.0.0.1:8000/decision/dda"

    player_health = st.slider("Player Health", 0.0, 100.0, 50.0)
    enemy_kill_rate = st.slider("Enemy Kill Rate", 0.0, 10.0, 5.0)
    damage_taken = st.slider("Damage Taken", 0.0, 50.0, 10.0)
    level_time = st.slider("Level Time", 1.0, 30.0, 10.0)
    win_streak = st.slider("Win Streak", 0, 10, 2)

    payload = {
        "player_health": player_health,
        "enemy_kill_rate": enemy_kill_rate,
        "damage_taken": damage_taken,
        "level_time": level_time,
        "win_streak": win_streak
    }

# Button
if st.button("🔍 Get Decision"):

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.markdown("---")
            st.header("📊 Results")

            # Probability
            if use_case == "Customer Retention":
                st.metric("Churn Probability", f"{result['score']:.2f}")
            else:
                st.metric("Difficulty Score", f"{result['score']:.2f}")
                
            # Decision
            st.success(f"Decision: {result['decision']}")

            # Rule
            st.info(f"Rule Triggered: {result.get('rule_triggered', 'N/A')}")

            # Reasons
            st.write("### 🧾 Reason")
            for r in result["reason"]:
                st.write(f"- {r}")

        else:
            st.error("API Error")

    except Exception as e:
        st.error(f"Error: {e}")