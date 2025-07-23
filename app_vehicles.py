# Importación de librerias

import pandas as pd 
import plotly.express as px
import streamlit as stm
import numpy as np

# Colocación de cabecera

stm.header('Análisis de venta de vehiculos usados')

# Carga o lectura de la información

car_data = pd.read_csv('vehicles_us.csv') 

# Creación de botón

hist_button = stm.button('Construir histograma') # crear un botón

stm.divider()

# Asignación de acción al botón

if hist_button:
    # escribir un mensaje
    stm.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # creación de histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    stm.plotly_chart(fig, use_container_width=True)

build_scatter = stm.checkbox('Construye un gráfico de dispersión')

stm.divider()

if build_scatter:
    # escribir un mensaje
    stm.write('Creación de dispersión para el conjunto de datos')
         
    # creación de histograma
    fig = px.scatter(car_data, x="model_year", y = 'price')
     
    # mostrar un gráfico Plotly interactivo
    stm.plotly_chart(fig, use_container_width=True)

stm.divider()

build_lineplot = stm.checkbox('Gráfica de ventas por tipo de transmisión')

if build_lineplot:
    # escribir un mensaje
    stm.write('Comportamiento de precio respecto a la transmisión')
         
    # creación de filtro
    df_analytics = car_data.groupby(['date_posted', 'transmission'])['price'].mean().reset_index()
         
    # mostrar un gráfico Plotly interactivo
    fig = px.line(df_analytics, x = 'date_posted', y = 'price', color='transmission')
    stm.plotly_chart(fig, use_container_width=True) 

stm.divider()

opciones = list(car_data.columns)[0:5]

variable = stm.multiselect(
            label = "Seleccione dos tipos de vehiculos",
            options = opciones,
            max_selections = 2

)

analis_01 = stm.button(
            label= 'Analizar'
)

if analis_01:

    hist_plot = px.histogram(car_data, x = variable[0], y = variable[1])
    stm.plotly_chart(hist_plot, use_container_width=True )

stm.divider()