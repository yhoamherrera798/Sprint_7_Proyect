import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
df = pd.read_csv('vehicles_us.csv') 

# Título de la aplicación
st.title('Análisis de Datos de Vehículos')

# Mostrar información básica del dataset
st.header('Información del Dataset')
st.write(f'Este dataset contiene {df.shape[0]} filas y {df.shape[1]} columnas')

# Mostrar las primeras filas del dataset
st.subheader('Muestra de los datos')
st.dataframe(df.head())

# Crear un botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(df, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un gráfico de dispersión
    fig = px.scatter(df, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
