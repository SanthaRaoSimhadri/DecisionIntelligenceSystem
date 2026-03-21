"""
Data Pipeline for Customer Retention Use Case

Generates synthetic data representing user behavior and churn patterns.
"""

import numpy as np
import pandas as pd


def generate_synthetic_data(n_samples=5000, seed=42):
    np.random.seed(seed)

    data = pd.DataFrame({
        "engagement_score": np.random.beta(2, 5, n_samples),
        "days_since_last_login": np.random.randint(0, 60, n_samples),
        "avg_session_time": np.random.exponential(scale=10, size=n_samples),
        "num_transactions": np.random.poisson(3, n_samples),
        "support_tickets": np.random.poisson(1, n_samples)
    })

    # Hidden logic to simulate churn behavior
    churn_prob = (
        0.4 * (1 - data["engagement_score"]) +
        0.3 * (data["days_since_last_login"] / 60) +
        0.2 * (data["support_tickets"] / 5) -
        0.2 * (data["num_transactions"] / 10)
    )

    churn_prob = np.clip(churn_prob, 0, 1)

    data["churn"] = np.random.binomial(1, churn_prob)

    return data