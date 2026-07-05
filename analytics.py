import streamlit as st
import pandas as pd
import plotly.express as px
import joblib


# Load trained Random Forest model
model = joblib.load("models/churn_model.pkl")

# Load feature names
feature_names = joblib.load("models/feature_names.pkl")

def analytics_page(df):

    st.title("📊 Telecom Customer Analytics")

    st.markdown("---")

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Customers", len(df))
    col2.metric(
        "Churn Rate",
        f"{(df['Churn Label']=='Yes').mean()*100:.2f}%"
    )
    col3.metric(
        "Avg Monthly Charges",
        f"${df['Monthly Charges'].mean():.2f}"
    )
    col4.metric(
        "Avg Tenure",
        f"{df['Tenure Months'].mean():.1f}"
    )

    st.markdown("---")

    # Churn Pie Chart
    churn = df["Churn Label"].value_counts().reset_index()
    churn.columns = ["Churn", "Count"]

    fig = px.pie(
        churn,
        names="Churn",
        values="Count",
        hole=0.5,
        title="Customer Churn Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
 # =====================================
 #         FEATURE IMPORTANCE
 # =====================================

st.markdown("---")

st.subheader("⭐ Top 20 Important Features")

importance = pd.DataFrame({

    "Feature": feature_names,

    "Importance": model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

fig = px.bar(

    importance.head(20),

    x="Importance",

    y="Feature",

    orientation="h",

    title="Top 20 Features Influencing Customer Churn"

)

fig.update_layout(

    yaxis=dict(categoryorder="total ascending"),

    height=700

)

st.plotly_chart(fig, use_container_width=True)