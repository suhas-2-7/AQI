import streamlit as st
from utils import predict_aqi_from_values

st.title("📈 Predict AQI from Pollutants")

st.markdown("Enter the pollutant concentrations below to calculate the **Air Quality Index (AQI)**:")

pm25 = st.number_input("🔹 PM2.5 (µg/m³)", min_value=0.0, step=0.1)
pm10 = st.number_input("🔹 PM10 (µg/m³)", min_value=0.0, step=0.1)
no2  = st.number_input("🔹 NO₂ (µg/m³)", min_value=0.0, step=0.1)
so2  = st.number_input("🔹 SO₂ (µg/m³)", min_value=0.0, step=0.1)

if st.button("🚀 Predict AQI"):
    aqi, category = predict_aqi_from_values(pm25, pm10, no2, so2)
    st.success(f"✅ AQI: {aqi}")
    st.info(f"🟢 Category: **{category}**")
