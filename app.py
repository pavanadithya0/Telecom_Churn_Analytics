import streamlit as st
import pandas as pd

from dashboard import dashboard_page
from prediction import prediction_page
from analytics import analytics_page
from about import about_page

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.markdown("""
<style>

.main{
    background-color:#f4f7fc;
}

/* Hide Streamlit Menu & Footer */
#MainMenu{
    visibility:hidden;
}
footer{
    visibility:hidden;
}
header{
    visibility:hidden;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0E4C92;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Buttons */
.stButton>button{
    background:#0E4C92;
    color:white;
    border-radius:10px;
    border:none;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1976D2;
    color:white;
}

/* Metric Cards */
[data-testid="metric-container"]{
    background:white;
    border-radius:15px;
    padding:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.12);
}

/* Charts */
.js-plotly-plot{
    border-radius:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.12);
    padding:10px;
    background:white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = pd.read_csv("data/cleaned_data.csv")

# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.title("📊 Telecom Dashboard")

    st.markdown("---")

    page = st.radio(

        "Navigation",

        [

            "🏠 Dashboard",

            "🤖 Prediction",

            "📈 Analytics",

            "ℹ About"

        ]

    )

    st.markdown("---")

    st.success("Model : Random Forest")

# -----------------------------------
# ROUTING
# -----------------------------------

if page == "🏠 Dashboard":

    dashboard_page(df)

elif page == "🤖 Prediction":

    prediction_page(df)

elif page == "📈 Analytics":

    analytics_page(df)

else:

    about_page()
st.success(
    "✅ Machine Learning Model Loaded Successfully"
)


st.markdown("---")

st.markdown(
"""
<center>

Developed by ** Buridi Pavan Adithya**

Machine Learning | Data Science | Streamlit

© 2026

</center>
""",
unsafe_allow_html=True
)
