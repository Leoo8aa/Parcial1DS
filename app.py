import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

# Define the prediction function
def predict(input_data):
    prediction = model.predict(pd.DataFrame([input_data]))
    return prediction[0]

# Create the Streamlit app
st.title("California Housing Price Prediction")

# Input form
longitude = st.number_input("Longitude", value=-122.23)
latitude = st.number_input("Latitude", value=37.88)
housing_median_age = st.number_input("Housing Median Age", value=41.0)
total_rooms = st.number_input("Total Rooms", value=880.0)
total_bedrooms = st.number_input("Total Bedrooms", value=129.0)
population = st.number_input("Population", value=322.0)
households = st.number_input("Households", value=126.0)
median_income = st.number_input("Median Income", value=8.3252)
ocean_proximity = st.selectbox("Ocean Proximity", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"])

# Create input data dictionary
input_data = {
    "longitude": longitude,
    "latitude": latitude,
    "housing_median_age": housing_median_age,
    "total_rooms": total_rooms,
    "total_bedrooms": total_bedrooms,
    "population": population,
    "households": households,
    "median_income": median_income,
    "ocean_proximity": ocean_proximity,
}

# Make prediction when button is clicked
if st.button("Predict"):
    prediction = predict(input_data)
    st.success(f"Predicted Median House Value: ${prediction:,.2f}")