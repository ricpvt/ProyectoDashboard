import streamlit as st
import pandas as pd
import plost

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard Clima CDMX (2020-2024)')

st.sidebar.subheader('Parametros del Heatmap')
time_hist_color = st.sidebar.selectbox('Colorear por', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Parametros del grafico de linea')
plot_data = st.sidebar.multiselect('Seleccionar datos', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = 500

st.sidebar.markdown('''
---
Creado por [Ricardo Ortega](https://github.com/ricpvt/).
''')


# Fila A
st.markdown('### Medidas')
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "32 °C", "1 °C")
col2.metric("Viento", "16 km/h", "-10%")
col3.metric("Humedad", "33%", "2%")

# Fila B
clima_CDMX = pd.read_csv('ClimaCDMX.csv', parse_dates=['date'])

st.markdown('### Heatmap')
plost.time_hist(
data=clima_CDMX,
date='date',
x_unit='week',
y_unit='day',
color=time_hist_color,
aggregate='median',
legend=None,
height=345,
use_container_width=True)

# Fila C
st.markdown('### Grafico de linea')
st.line_chart(clima_CDMX, x = 'date', y = plot_data, height = plot_height)
