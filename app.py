import streamlit as st
import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('vehicles_us.csv')

# Encabezado de la app
st.header("Análisis Exploratorio de Datos de Vehículos")

# Botón para el histograma
if st.button("Construir histograma"):
    st.write("Creando histograma de odómetro")
    fig = go.Figure(data=[go.Histogram(
        x=df['odometer'],
        marker_color='orange'  # opcional, para distinguirlo
    )])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)


# Botón para el gráfico de dispersión (scatter)
if st.button("Construir scatter"):
    st.write("Creando scatter de odómetro vs precio")
    fig2 = go.Figure(data=[go.Scatter(
        x=df['odometer'],
        y=df['price'],
        mode='markers',
        marker=dict(color='blue', size=6, opacity=0.6)
    )])
    fig2.update_layout(
        title_text='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )
    st.plotly_chart(fig2, use_container_width=True)
