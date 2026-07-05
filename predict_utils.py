import joblib
import pandas as pd

# Load model artifacts
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")


def predict_churn(user_input):

    # Convert input dictionary to DataFrame
    df = pd.DataFrame([user_input])

    # One Hot Encoding
    df = pd.get_dummies(df)

    # Add missing columns
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    # Keep correct order
    df = df[feature_names]

    # Scale numerical columns
    numeric_columns = [
        col for col in [
            "Tenure Months",
            "Monthly Charges",
            "Total Charges",
            "CLTV"
        ] if col in df.columns
    ]

    df[numeric_columns] = scaler.transform(df[numeric_columns])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    return prediction, probability
