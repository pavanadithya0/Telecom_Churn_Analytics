import joblib

model = joblib.load("models/churn_model.pkl")

print(model)