id="g8m81h"
import pandas as pd
import streamlit as st
import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Cars24 Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

h1 {
    color: #FF4B4B;
}

.stButton>button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

.stSelectbox, .stSlider {
    padding-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("""
# 🚗 Cars24 Used Car Price Prediction
### Predict resale prices of used cars intelligently
""")

# ---------------- LOAD DATA ----------------
cars_df = pd.read_csv("Data/cars24-car-price-cleaned-new.csv")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Car Configuration")

fuel_type = st.sidebar.selectbox(
    "Select Fuel Type",
    ["Diesel", "Petrol", "CNG", "LPG", "Electric"]
)

engine = st.sidebar.slider(
    "Engine Power (CC)",
    800,
    5000,
    1200
)

year = st.sidebar.slider(
    "Manufacturing Year",
    2000,
    datetime.datetime.now().year,
    2018
)

kms_driven = st.sidebar.slider(
    "Kilometers Driven",
    0,
    300000,
    50000
)

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Selected Fuel", fuel_type)

with col2:
    st.metric("Engine Power", f"{engine} CC")

with col3:
    st.metric("Manufacturing Year", year)

st.divider()

# ---------------- DATA PREVIEW ----------------
st.subheader("📊 Dataset Preview")

st.dataframe(cars_df.head())

# ---------------- SIMPLE DATA ANALYSIS ----------------
st.subheader("📈 Dataset Insights")

st.write("Total Cars in Dataset:", len(cars_df))

st.write("Fuel Type Counts:")

if "fuel_type" in cars_df.columns:
    st.bar_chart(cars_df["fuel_type"].value_counts())

# ---------------- PREDICTION SECTION ----------------
st.subheader("💰 Price Prediction")

# Dummy prediction logic
predicted_price = (
    800000
    - (2025 - year) * 25000
    - (kms_driven * 0.5)
    + (engine * 20)
)

predicted_price = max(predicted_price, 50000)

if st.button("Predict Car Price"):
    st.success(f"Estimated Car Price: ₹ {int(predicted_price):,}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")