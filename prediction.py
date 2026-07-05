import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from predict_utils import predict_churn


def prediction_page(df):

    # ==========================================
    # PAGE TITLE
    # ==========================================

    st.title("🤖 Customer Churn Prediction")

    st.write(
        "Enter the customer details below to predict whether the customer is likely to churn."
    )

    st.markdown("---")

    # ==========================================
    # CUSTOMER INPUT
    # ==========================================

    left, right = st.columns(2)

    with left:

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        senior = st.selectbox(
            "Senior Citizen",
            [0, 1]
        )

        partner = st.selectbox(
            "Partner",
            ["Yes", "No"]
        )

        tenure = st.slider(
            "Tenure Months",
            0,
            72,
            24
        )

    with right:

        internet = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )

        monthly = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            value=70.0
        )

        cltv = st.number_input(
            "CLTV",
            min_value=0,
            value=4500
        )

    st.markdown("---")

    # ==========================================
    # PREDICT BUTTON
    # ==========================================

    if st.button("🚀 Predict Customer"):

        customer = {

            "Gender": gender,
            "Senior Citizen": senior,
            "Partner": partner,
            "Tenure Months": tenure,
            "Internet Service": internet,
            "Contract": contract,
            "Monthly Charges": monthly,
            "Total Charges": tenure * monthly,
            "CLTV": cltv

        }

        # ==========================================
        # MODEL PREDICTION
        # ==========================================

        prediction, probability = predict_churn(customer)

        st.markdown("---")

        # ==========================================
        # RESULT
        # ==========================================

        st.subheader("Prediction Result")

        if prediction == 1:

            st.error("⚠️ Customer is likely to Churn")

        else:

            st.success("✅ Customer is likely to Stay")

        st.metric(

            label="Churn Probability",

            value=f"{probability:.2%}"

        )

        # ==========================================
        # GAUGE CHART
        # ==========================================

        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=probability * 100,

                title={"text": "Customer Churn Risk (%)"},

                gauge={

                    "axis": {"range": [0, 100]},

                    "bar": {"color": "red"},

                    "steps": [

                        {"range": [0, 30], "color": "lightgreen"},

                        {"range": [30, 70], "color": "gold"},

                        {"range": [70, 100], "color": "tomato"}

                    ]

                }

            )

        )

        st.plotly_chart(fig, use_container_width=True)

        # ==========================================
        # RISK LEVEL
        # ==========================================

        st.subheader("Risk Level")

        if probability < 0.30:

            st.success("🟢 LOW RISK")

        elif probability < 0.70:

            st.warning("🟡 MEDIUM RISK")

        else:

            st.error("🔴 HIGH RISK")

        # ==========================================
        # CUSTOMER SUMMARY
        # ==========================================

        st.markdown("---")

        st.subheader("📋 Customer Summary")

        summary = pd.DataFrame({

            "Feature": [

                "Gender",

                "Senior Citizen",

                "Partner",

                "Internet Service",

                "Contract",

                "Tenure Months",

                "Monthly Charges",

                "Total Charges",

                "CLTV"

            ],

            "Value": [

                gender,

                senior,

                partner,

                internet,

                contract,

                tenure,

                monthly,

                tenure * monthly,

                cltv

            ]

        })

        st.dataframe(summary, use_container_width=True)

        # ==========================================
        # BUSINESS RECOMMENDATION
        # ==========================================

        st.markdown("---")

        st.subheader("💡 Recommendation")

        if prediction == 1:

            st.warning("""

### Suggested Retention Strategies

- Offer promotional discounts
- Encourage the customer to switch to a yearly contract
- Contact the customer before renewal
- Assign the customer to the retention team
- Provide loyalty rewards

""")

        else:

            st.success("""

### Customer Status

- Customer is likely to remain with the company.
- Continue providing quality service.
- Offer premium plans for upselling.
- Maintain regular engagement.

""")

        # ==========================================
        # DOWNLOAD REPORT
        # ==========================================

        st.markdown("---")

        st.subheader("📥 Download Prediction Report")

        report = pd.DataFrame({

            "Field": [

                "Gender",

                "Senior Citizen",

                "Partner",

                "Internet Service",

                "Contract",

                "Tenure Months",

                "Monthly Charges",

                "Total Charges",

                "CLTV",

                "Prediction",

                "Churn Probability"

            ],

            "Value": [

                gender,

                senior,

                partner,

                internet,

                contract,

                tenure,

                monthly,

                tenure * monthly,

                cltv,

                "Churn" if prediction == 1 else "No Churn",

                f"{probability:.2%}"

            ]

        })

        csv = report.to_csv(index=False).encode("utf-8")

        st.download_button(

            label="📥 Download CSV Report",

            data=csv,

            file_name="customer_prediction_report.csv",

            mime="text/csv"

        )