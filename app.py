import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón (o casilla de verificación) para construir un gráfico de dispersión
scatter_button = st.checkbox('Construir un gráfico de dispersión')

if scatter_button:
    st.write('Construyendo un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="year", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)