import streamlit as st
import pandas as pd

# Título de la aplicación
st.title('Visualización de Datos CSV con Streamlit')

# Cargar el archivo CSV
archivo_csv = st.file_uploader("Cargar archivo CSV", type=['csv'])

if archivo_csv is not None:
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv)

    # Mostrar el DataFrame en Streamlit
    st.write("Datos del CSV:")
    st.write(df)
