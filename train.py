"""
Offline Training Script

- Generates data
- Trains model
- Saves model to disk
"""

import joblib

from use_cases.customer_retention.data_pipeline import generate_synthetic_data
from core.model import train_model
from use_cases.dda_game.data_pipeline import generate_dda_data

MODEL_PATH = "models/churn_model.pkl"
DDA_MODEL_PATH = "models/dda_model.pkl"

if __name__ == "__main__":
    print("🔄 Generating data...")
    df = generate_synthetic_data()

    print("🧠 Training model...")
    model = train_model(df)

    print("💾 Saving model...")
    joblib.dump(model, MODEL_PATH)

    print(f"✅ Model saved at {MODEL_PATH}")

    # ---- DDA Training ---- #
    print("🎮 Generating DDA data...")
    dda_df = generate_dda_data()

    print("🧠 Training DDA model...")
    dda_model = train_model(dda_df.rename(columns={"difficulty": "churn"}))

    print("💾 Saving DDA model...")
    joblib.dump(dda_model, DDA_MODEL_PATH)
