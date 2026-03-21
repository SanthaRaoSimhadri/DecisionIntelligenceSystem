"""
Synthetic Data for DDA Game Use Case
"""

import numpy as np
import pandas as pd

# Convert to discrete classes
def categorize_difficulty(score):
    if score < 0.3:
        return 0
    elif score < 0.7:
        return 1
    else:
        return 2


def generate_dda_data(n_samples=5000, seed=42):
    np.random.seed(seed)

    data = pd.DataFrame({
        "player_health": np.random.uniform(0, 100, n_samples),
        "enemy_kill_rate": np.random.uniform(0, 10, n_samples),
        "damage_taken": np.random.uniform(0, 50, n_samples),
        "level_time": np.random.uniform(1, 30, n_samples),
        "win_streak": np.random.randint(0, 10, n_samples)
    })

    # Simulate difficulty score (target)
    difficulty_score = (
        0.4 * (data["enemy_kill_rate"] / 10) +
        0.3 * (data["win_streak"] / 10) +
        0.2 * (data["player_health"] / 100) -
        0.3 * (data["damage_taken"] / 50)
    )

    difficulty_score = np.clip(difficulty_score, 0, 1)

    data["difficulty"] = difficulty_score.apply(categorize_difficulty)

    return data