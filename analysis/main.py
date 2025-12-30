


import streamlit as st
import numpy as np
import pandas as pd
from joblib import load
from pathlib import Path

if "pred" not in st.session_state:
    st.session_state["pred"] = None

MODEL_PATH = Path(__file__).resolve().parent / "model_new.joblib"

@st.cache_resource(show_spinner="Loading model...")
def load_model():
    return load(MODEL_PATH)

rf_model = load_model()


def make_prediction(rf_model):
    store_id = st.session_state["store_id"]
    year = st.session_state["year_num"]
    month = st.session_state["month_num"]
    day = st.session_state["day_num"]
    temp = st.session_state["avg_temp"]


    X_pred = pd.DataFrame({
        'store_id': [store_id],
        'year_num': [year],
        'month_num': [month],
        'day_num': [day],
        'avg_temp': [temp]
        
    })

    pred =rf_model.predict(X_pred)
    pred = round(pred[0], 2)

    st.session_state["pred"] = pred


    if __name__ == "__main__":
    st.title("Coffee Shop Sales Predictor ☕")


    rf_model = load_model()
    with st.form("form"):
        col1, col2, col3 = st.columns(3)

    with col1:
        store_id = st.number_input("Store ID", min_value=1, step=1)

    with col2:
        year = st.number_input("Year", min_value=2020, step=1)

    with col3:
        month = st.number_input("Month", min_value=1, max_value=12)

    col4, col5 = st.columns(2)

    with col4:
        day = st.number_input("Day", min_value=1, max_value=31)

    with col5:
        temp = st.number_input("Avg Temperature (°C)")

    submitted = st.form_submit_button("Predict")