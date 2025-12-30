# streamlit run analysis/main.py

import streamlit as st
import pandas as pd
from joblib import load
from pathlib import Path

# ---------- Session state ----------
if "pred" not in st.session_state:
    st.session_state["pred"] = None

# ---------- Load model ----------
MODEL_PATH = Path(__file__).resolve().parent / "model_new.joblib"

@st.cache_resource(show_spinner="Loading model...")
def load_model():
    return load(MODEL_PATH)

rf_model = load_model()

# ---------- Prediction function ----------
def make_prediction():
    X_pred = pd.DataFrame({
        "store_id": [st.session_state.store_id],
        "year_num": [st.session_state.year_num],
        "month_num": [st.session_state.month_num],
        "day_num": [st.session_state.day_num],
        "avg_temp": [st.session_state.avg_temp],
    })

    pred = rf_model.predict(X_pred)
    st.session_state["pred"] = round(pred[0], 2)

# ---------- UI ----------
st.title("☕ Coffee Shop Sales Predictor")
st.caption("Predict daily sales based on store, date, and temperature")

with st.form("sales_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
         st.selectbox(
        "Store ID",
        options=[3, 5, 8],
        key="store_id")

    with col2:
        st.selectbox("Year", [2023, 2024], key="year_num")

    with col3:
        st.selectbox(
        "Month",
        options=list(range(1, 13)),
        key="month_num")

    col4, col5 = st.columns(2)

    import calendar

    max_day = calendar.monthrange(
        st.session_state.year_num,
        st.session_state.month_num
        )[1]

    with col4:
        st.selectbox(
        "Day",
        options=list(range(1, max_day + 1)),
        key="day_num"
    )

    with col5:
        st.number_input("Avg Temperature (°C)", key="avg_temp")

    submitted = st.form_submit_button("Get Sales Forecast")

    if submitted:
        make_prediction()

# ---------- Result ----------
if st.session_state["pred"] is not None:
    st.metric("Predicted Sales", st.session_state["pred"])
else:
    st.info("Enter the inputs and click **Get Sales Forecast**")
