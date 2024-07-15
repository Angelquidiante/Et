# Encabezado de la aplicación
st.title('Análisis de Datos con Streamlit')

# Mostrar los datos del archivo CSV
st.write("### Datos del archivo CSV")
st.write(df)  # Mostrar el DataFrame en Streamlit

# Ejemplo de análisis interactivo (puedes personalizar esto según tus necesidades)
st.write("### Resumen Estadístico")
st.write(df.describe())  # Mostrar estadísticas descriptivas básicas

# Gráfico interactivo (ejemplo de gráfico de barras)
st.write("### Gráfico de Barras de una Columna")
column = st.selectbox('Selecciona una columna para graficar:', df.columns)
st.bar_chart(df[column])

# Otros tipos de gráficos y análisis según sea necesario
