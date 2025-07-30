import streamlit as st

st.title("🧪 Pollutants & Their Health Effects")

st.markdown("""
### 🌫️ PM2.5
Fine particulate matter (diameter < 2.5 µm) that penetrates deep into the lungs.
- 🔸 Causes respiratory diseases, lung cancer, heart attacks.

### 🌫️ PM10
Coarse dust particles (diameter < 10 µm).
- 🔸 Causes coughing, sneezing, and asthma aggravation.

### 💨 NO₂ (Nitrogen Dioxide)
Produced from fuel combustion (vehicles, power plants).
- 🔸 Irritates airways, reduces lung function, and increases asthma.

### ☁️ SO₂ (Sulfur Dioxide)
Emitted from burning fossil fuels and industrial activity.
- 🔸 Causes bronchitis, eye irritation, and worsens heart conditions.

---

### 🧮 Why Use Sub-Indices & Breakpoints?

- Each pollutant affects health differently.
- **Sub-indices** allow conversion of concentrations to **comparable risk scores**.
- **Breakpoints** (CPCB or EPA) define the range → AQI bucket (Good, Moderate, etc.).

---
""")
