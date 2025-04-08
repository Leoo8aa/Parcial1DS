# app.py (Streamlit)
import streamlit as st
import joblib
import pandas as pd

# Cargar el modelo entrenado
model = joblib.load("best_model.pkl")

# Título de la aplicación
st.title("Clasificador de Arroz (Cammeo vs Osmancik)")

# Descripción del dataset
st.write("""
Este clasificador predice si un grano de arroz pertenece a la clase **Cammeo** u **Osmancik** 
basándose en sus características físicas.
""")

# Entrada de datos
st.subheader("Ingrese las características del grano de arroz:")
# Cambiar los nombres de las características en app.py
feature_names = [
    "Area", "Perimeter", "Major_Axis_Length", "Minor_Axis_Length",
    "Aspect_Ratio", "Eccentricity", "Convex_Area", "Extent", "Compactness"
]

# Crear campos de entrada para cada característica
input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(f"{feature}", value=0.0)

# Botón de predicción
if st.button("Predecir"):
    # Convertir los datos ingresados en un DataFrame
    input_df = pd.DataFrame([input_data])

    # Realizar la predicción
    prediction = model.predict(input_df)

    # Mostrar el resultado
    st.subheader("Resultado de la Predicción:")
    st.write(f"La clase predicha es: **{prediction[0]}**")