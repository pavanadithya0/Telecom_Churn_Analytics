from predict_utils import predict_churn

sample_customer = {

    "Gender": "Male",
    "Senior Citizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "Tenure Months": 24,
    "Phone Service": "Yes",
    "Internet Service": "Fiber optic",
    "Contract": "Month-to-month",
    "Payment Method": "Electronic check",
    "Monthly Charges": 85.5,
    "Total Charges": 2100,
    "CLTV": 4500

}

prediction, probability = predict_churn(sample_customer)

print("Prediction :", prediction)
print("Probability:", probability)