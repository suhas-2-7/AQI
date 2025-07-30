import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="AQI Prediction App", layout="centered")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Overview", "Pollutants Info", "Predict AQI", "Libraries Used"],
        icons=["house", "info-circle", "activity", "tools"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Overview":
    st.switch_page("pages/1_Overview.py")
elif selected == "Pollutants Info":
    st.switch_page("pages/2_Pollutants_Info.py")
elif selected == "Predict AQI":
    st.switch_page("pages/3_Predict_AQI.py")
elif selected == "Libraries Used":
    st.switch_page("pages/4_Libraries_Used.py")
