"""
Model Module

Handles training and inference for churn prediction.
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


def train_model(df):
    X = df.drop("churn", axis=1)
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("\nModel Performance:\n")
    print(classification_report(y_test, preds))

    return model


def predict_proba(model, input_df):
    """
    Returns churn probability for given input
    """
    return model.predict_proba(input_df)[:, 1]