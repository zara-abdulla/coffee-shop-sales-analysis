# streamlit run analysis/streamlit_app.py

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


# ---------- Defaults ----------
defaults = {
    "store_name": "Astoria",
    "year_num": 2026,
    "month_num": 1,
    "day_num": 1,
    "avg_temp": 10.0,
    "pred": None,
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ---------- Prediction history ----------
if "history" not in st.session_state:
    st.session_state["history"] = pd.DataFrame(
        columns=["date", "store", "avg_temp", "predicted_sales"]
    )


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

    pred = rf_model.predict(X_pred)[0]
    pred = round(pred, 2)
    st.session_state["pred"] = pred

    date_str = f"{st.session_state.year_num}-" \
               f"{st.session_state.month_num:02d}-" \
               f"{st.session_state.day_num:02d}"

    new_row = {
        "date": date_str,
        "store": st.session_state.store_name,
        "avg_temp": st.session_state.avg_temp,
        "predicted_sales": pred
    }

    st.session_state["history"] = pd.concat(
        [st.session_state["history"], pd.DataFrame([new_row])],
        ignore_index=True
    )


# ---------- UI ----------
st.markdown(
    """
    <h1 style='text-align: center; color: #fafafc;'>
        Coffee Shop Sales Predictor  &nbsp;☕
    </h1>
    """,
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("images/str2.png", width=400)

st.markdown("---")

st.markdown(
    """
    <h4 style='text-align: center; color: #fafafc;'>
        Predict daily sales based on date, store and temperature:
    </h4>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #061e47, #68a4f1);
    }
    .stButton>button {
        background-color: #2b6ad0;
        color: #fafafc;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -------- Sidebar --------
st.sidebar.image("images/side_img.png", width=300)
st.sidebar.title("ℹ️ Information")

with st.sidebar.expander("📌 Project Info"):
    st.markdown(
        """
        Coffee Shop Sales Predictor is a machine learning application that estimates
        daily coffee shop sales using store location, date, and average temperature.

        It helps optimize inventory planning, staff scheduling, and data-driven decisions.

        **Built with:** 
        - Python  
        - Streamlit  
        - Machine Learning
        """
    )

with st.sidebar.expander("📬 Contact Us"):
    st.markdown(
        """
        
        **Feel free to connect with us 👇**

        **Zahra Abdullayeva**  
        🔗 [GitHub](https://github.com/zara-abdulla)  
        🔗 [LinkedIn](https://linkedin.com/in/zahra-abdullayeva-23143a169)  

        **Ziyafat Rzayeva**  
        🔗 [GitHub](https://github.com/Ziyafat98)  
        🔗 [LinkedIn](https://linkedin.com/in/ziyafət-rzayeva-a45675321)  

        🚀 Let’s collaborate and build something impactful
        """
    )


# -------- Inputs --------
col1, col2, col3 = st.columns(3)

max_day = calendar.monthrange(
    st.session_state.year_num,
    st.session_state.month_num
)[1]

with col1:
    st.selectbox("Day", list(range(1, max_day + 1)), key="day_num")

with col2:
    st.selectbox("Month", list(range(1, 13)), key="month_num")

with col3:
    st.text_input("Year", value="2026", disabled=True)

col4, col5 = st.columns(2)

with col4:
    st.selectbox(
        "Store",
        options=list(STORE_MAP.keys()),
        key="store_name"
    )

with col5:
    temp = st.slider("🌡️ Avg Temperature (°C)", -30, 40, step=1, key="avg_temp")

    if temp <= 0:
        st.caption("❄️ Cold day")
    elif temp <= 20:
        st.caption("🌤️ Mild weather")
    else:
        st.caption("🔥 Hot day")


# -------- Predict button --------
st.markdown(
    """
    <style>
    .stButton>button {
        background:#2d1674; color:#fafafc; font-size:16px; border-radius:8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if st.button("Get Sales Forecast"):
    make_prediction()


# -------- Result --------
if st.session_state["pred"] is not None:
    st.markdown(
        f"""
        <div style="
            backdrop-filter: blur(8px);
            background: rgba(255,255,255,0.12);
            border-radius:16px;
            padding:24px;
            text-align:center;
            color:#fafafc;
        ">
            <div style="font-size:14px;">Predicted Sales</div>
            <div style="font-size:34px; font-weight:600;">
                ${st.session_state['pred']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div style='background-color:#93a387; color:#fafafc; padding:10px; border-radius:5px'>
        Enter the inputs and click <b>Get Sales Forecast</b>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")


# -------- Prediction History Chart --------
if not st.session_state["history"].empty:
    st.markdown("### Prediction History")

    df_chart = st.session_state["history"].copy()
    df_chart["date"] = pd.to_datetime(df_chart["date"])
    df_chart = df_chart.sort_values("date")

    st.line_chart(
        df_chart.set_index("date")["predicted_sales"]
    )
