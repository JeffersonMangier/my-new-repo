#######################
# Import libraries
import pandas as pd
import plotly.express as px
import streamlit as st

#######################
# Page configuration
st.set_page_config(
    page_title="Car Sales Dashboard",
    page_icon=":red_car:",
    layout="wide",
    initial_sidebar_state="expanded")

st.header('Análisis de Anuncios de Coches')

#######################
# Load data
car_data = pd.read_csv('vehicles_us.csv')

#Extract the elements to use it in the sidebar
model_year = sorted(car_data["model_year"].unique().tolist(), reverse=True)
models = sorted(car_data["model_year"].unique().tolist())
type_car = sorted(car_data["model_year"].unique().tolist())
fuel = sorted(car_data["model_year"].unique().tolist())
cylinders = sorted(car_data["model_year"].unique().tolist())


#######################
# Sidebar
with st.sidebar:
    selected_year = st.multiselect("Select the model year(s)", model_year) or model_year
    selected_model = st.multiselect("Select the model", sorted(car_data.query("@selected_year in model_year")["model"].unique())) or models
    selected_type = st.multiselect("Select the type of car", sorted(car_data.query("@selected_year in model_year and @selected_model in model")["type"].unique())) or type_car
    selected_fuel = st.multiselect("Select the type off fuel", sorted(car_data.query("@selected_year in model_year and @selected_model in model and @selected_type in type")["fuel"].unique())) or fuel
    selected_cylinders = st.multiselect("Select the cylinders", sorted(car_data.query("@selected_year in model_year and @selected_model in model and @selected_type in type and @selected_fuel in fuel")["cylinders"].unique())) or cylinders
    
############################   
# df_filtered = car_data.query("@selected_year in model_year and @selected_model in model and @selected_type in type and @selected_fuel in fuel and @selected_cylinders in cylinders")
df_filtered = car_data.query("@selected_year in model_year and @selected_model in model and @selected_type in type and @selected_fuel in fuel and @selected_cylinders in cylinders")
# Mostrar el DataFrame filtrado
st.write("Filtered DataFrame:")
st.write(df_filtered)

# Botón para construir histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir gráfico de dispersión
scatter_button = st.checkbox('Construir gráfico de dispersión')

if scatter_button:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


    