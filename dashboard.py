import streamlit as st
import plotly.express as px

def dashboard_page(df):

    st.title("📊 Telecom Customer Churn Dashboard")
    st.markdown("### Business Overview")
    st.markdown("---")

    # ==========================
    # KPI CARDS
    # ==========================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "👥 Customers",
        f"{len(df):,}"
    )

    c2.metric(
        "📉 Churn Rate",
        f"{(df['Churn Label']=='Yes').mean()*100:.2f}%"
    )

    c3.metric(
        "💰 Avg Monthly Charges",
        f"${df['Monthly Charges'].mean():.2f}"
    )

    c4.metric(
        "📅 Avg Tenure",
        f"{df['Tenure Months'].mean():.1f} Months"
    )

    st.markdown("---")

    # ==========================
    # ROW 1
    # ==========================

    left, right = st.columns(2)

    with left:

        churn = df["Churn Label"].value_counts().reset_index()
        churn.columns = ["Churn", "Customers"]

        fig = px.pie(
            churn,
            names="Churn",
            values="Customers",
            hole=0.55,
            title="Customer Churn Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        contract = df["Contract"].value_counts().reset_index()
        contract.columns = ["Contract", "Customers"]

        fig = px.bar(
            contract,
            x="Contract",
            y="Customers",
            color="Customers",
            title="Customers by Contract Type"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================
    # ROW 2
    # ==========================

    left, right = st.columns(2)

    with left:

        fig = px.histogram(
            df,
            x="Monthly Charges",
            nbins=40,
            title="Monthly Charges Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        fig = px.histogram(
            df,
            x="Tenure Months",
            nbins=40,
            title="Customer Tenure Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================
    # CONTRACT VS CHURN
    # ==========================

    contract_churn = (
        df.groupby(["Contract", "Churn Label"])
          .size()
          .reset_index(name="Customers")
    )

    fig = px.bar(
        contract_churn,
        x="Contract",
        y="Customers",
        color="Churn Label",
        barmode="group",
        title="Contract Type vs Churn"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ==========================
    # BUSINESS INSIGHTS
    # ==========================

    st.subheader("📌 Business Insights")

    churn_rate = (df["Churn Label"] == "Yes").mean() * 100

    st.info(f"""
- 📊 Total Customers: **{len(df):,}**
- 📉 Current Churn Rate: **{churn_rate:.2f}%**
- 💰 Average Monthly Charges: **${df['Monthly Charges'].mean():.2f}**
- 📅 Average Customer Tenure: **{df['Tenure Months'].mean():.1f} Months**

**Recommendation:** Focus customer retention efforts on customers with month-to-month contracts and higher monthly charges.
""")