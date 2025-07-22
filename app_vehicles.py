# Importación de librerias

import pandas as pd 
import plotly.express as px
import streamlit as stm 

# Colocación de cabecera

stm.header('Análisis de venta de vehiculos usados')

# Carga o lectura de la información

car_data = pd.read_csv('vehicles_us.csv') 

# Creación de botón

hist_button = stm.button('Construir histograma') # crear un botón

# Asignación de acción al botón

if hist_button:
    # escribir un mensaje
    stm.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # creación de histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    stm.plotly_chart(fig, use_container_width=True)

build_scatter = stm.checkbox('Construye un gráfico de dispersión')

if build_scatter:
    # escribir un mensaje
    stm.write('Creación de dispersión para el conjunto de datos')
         
    # creación de histograma
    fig = px.scatter(car_data, x="model_year", y = 'price')
     
    # mostrar un gráfico Plotly interactivo
    stm.plotly_chart(fig, use_container_width=True)  