import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/sales_model.pkl")

st.title("🎮 Video Game Global Sales Predictor")

# Inputs
platform = st.text_input("Platform (e.g., Wii, PS2, NES)")
year = st.number_input("Year", min_value=1980, max_value=2025, step=1)
genre = st.text_input("Genre (e.g., Sports, Action)")
publisher = st.text_input("Publisher (e.g., Nintendo, EA)")
na_sales = st.number_input("NA Sales (millions)", step=0.1)
eu_sales = st.number_input("EU Sales (millions)", step=0.1)
jp_sales = st.number_input("JP Sales (millions)", step=0.1)
other_sales = st.number_input("Other Sales (millions)", step=0.1)

# Encode inputs (dummy simple encoding for demo)
input_data = pd.DataFrame([[0, year, 0, 0, na_sales, eu_sales, jp_sales, other_sales]],
                          columns=["Platform", "Year", "Genre", "Publisher", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"])

if st.button("Predict Global Sales"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Global Sales: {prediction:.2f} million units")
