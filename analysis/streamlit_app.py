
#streamlit run analysis/streamlit_app.py

import streamlit as st
import pandas as pd
from joblib import load
from pathlib import Path
import calendar


# ---------- Store mapping ----------
STORE_MAP = {
    "Astoria": 3,
    "Lower Manhattan": 5,
    "Hell’s Kitchen": 8,
}



defaults = {
    "store_name": "Astoria",  # ID yox, ad
    "year_num": 2026,
    "month_num": 1,
    "day_num": 1,
    "avg_temp": 10.0,
    "pred": None,
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


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
    store_id = STORE_MAP[st.session_state.store_name]

    X_pred = pd.DataFrame({
        "store_id": [store_id],
        "year_num": [st.session_state.year_num],
        "month_num": [st.session_state.month_num],
        "day_num": [st.session_state.day_num],
        "avg_temp": [st.session_state.avg_temp],
    })

    pred = rf_model.predict(X_pred)
    st.session_state["pred"] = round(pred[0], 2)


# ---------- UI ----------
st.title("☕ Coffee Shop Sales Predictor")
st.markdown(" #### Predict daily sales based on store, date, and temperature")
st.markdown("---")  # horizontal line for separation
st.image("https://tenor.com/view/coffee-coffee-shop-cafe-street-gif-17572486.gif", width=450)
st.markdown(
    """
    <style>
    .stApp {
        /* Ombre: Dark Blue -> Cornflower */
        background: linear-gradient(to bottom, #061e47, #68a4f1);
    }
    .stButton>button {
        background-color: #2b6ad0;  /* Royal Blue button */
        color: #fafafc;             /* Ivory text */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("☕ Coffee Sales AI")
st.sidebar.caption("ML-powered daily sales forecast")


# -------- Inputs --------
col1, col2, col3 = st.columns(3)

with col1:
    st.selectbox(
        "Store",
        options=list(STORE_MAP.keys()),  # adlar görünəcək
        key="store_name",
        help="Select the coffee shop location"
    )

with col2:
    st.text_input("Year", value="2026", disabled=True)

with col3:
    st.selectbox("Month", list(range(1, 13)), key="month_num")

# Dynamic day logic
max_day = calendar.monthrange(
    st.session_state.year_num,
    st.session_state.month_num
)[1]


col4, col5 = st.columns(2)

with col4:
    st.selectbox("Day", list(range(1, max_day + 1)), key="day_num")

with col5:
    st.number_input(
        "Avg Temperature (°C)",
        min_value=-30.0,
        max_value=40.0,
        step=1.0,
        key="avg_temp",
        help="Average temperature in °C for the selected day"
    )




# -------- Predict button --------
st.markdown(
    """
    <style>
    .stButton>button {
        background:#2d1674; color:#fafafc; font-size:16px; border-radius:8px;
    }
    .stButton>button:hover { background:#1f0f5a; }
    </style>
    """,
    unsafe_allow_html=True
)
if st.button("Get Sales Forecast"):
    make_prediction()
    



# -------- Result --------
if st.session_state["pred"] is not None:
    st.metric("Predicted Sales", value=f"${st.session_state['pred']}",
        delta=None)
    
    
else:
     st.markdown(
        """
        <div style='background-color:#93a387; color:#fafafc; padding:10px; border-radius:5px'>
        Enter the inputs and click <b>Get Sales Forecast</b>
        </div>
        """,
        unsafe_allow_html=True
    )
     



#streamlit run analysis/streamlit_app.py