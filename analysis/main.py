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