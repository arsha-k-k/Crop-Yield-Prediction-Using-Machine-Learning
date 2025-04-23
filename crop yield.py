import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the model and transformed data (replace with the correct file paths if necessary)
model = joblib.load('D:\\arsha\\python\\Crop Yield Project\\crop yield.joblib')
data = joblib.load('D:\\arsha\\python\\Crop Yield Project\\transformed_data.joblib')

# Set up the Streamlit interface
st.title("Crop Yield Prediction App")

# Input fields for user to input values
region = st.selectbox("Region", ['North', 'West', 'South', 'East'])
soil_type = st.selectbox("Soil Type", ['Sandy', 'Loam', 'Chalky', 'Silt', 'Clay', 'Peaty'])
crop = st.selectbox("Crop", ['Maize', 'Rice', 'Barley', 'Wheat', 'Cotton', 'Soybean'])
rainfall = st.number_input("Rainfall (mm)", min_value=0)
temperature = st.number_input("Temperature (°C)", min_value=-10, max_value=50)
fertilizer_used = st.selectbox("Fertilizer Used", [False, True])
irrigation_used = st.selectbox("Irrigation Used", [False, True])
weather_condition = st.selectbox("Weather Condition", ['Sunny', 'Rainy', 'Cloudy'])
days_to_harvest = st.number_input("Days to Harvest", min_value=0)

# Button to predict crop yield
if st.button('Predict Yield'):
    try:
        # Encode the input data based on how the model was trained
        input_data = np.array([[
            {'North': 0, 'West': 1, 'South': 2, 'East': 3}[region],
            {'Sandy': 0, 'Loam': 1, 'Chalky': 2, 'Silt': 3, 'Clay': 4, 'Peaty': 5}[soil_type],
            {'Maize': 0, 'Rice': 1, 'Barley': 2, 'Wheat': 3, 'Cotton': 4, 'Soybean': 5}[crop],
            rainfall,
            temperature,
            int(fertilizer_used),  # Convert boolean to integer (0 or 1)
            int(irrigation_used),  # Convert boolean to integer (0 or 1)
            {'Sunny': 0, 'Rainy': 1, 'Cloudy': 2}[weather_condition],
            days_to_harvest
        ]])

        # Make the prediction using the trained model
        predicted_yield = model.predict(input_data)
        st.write(f"Predicted Yield: {predicted_yield[0]:.2f} tons per hectare")
    except Exception as e:
        st.error(f"Error during prediction: {e}")