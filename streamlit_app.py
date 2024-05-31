import streamlit as st
import pandas as pd
import plost
import mysql.connector

def dashboard():
    st.empty()
        
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


connection = mysql.connector.connect(
    host="127.0.0.7",
    user="root",
    password="password",
    database="streamlit"
)
cursor = connection.cursor()

def authenticate_user(username, password):
    query = "SELECT * FROM Users WHERE UserId = %s AND Password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    return user is not None

def register_user(username, password):
    query = "INSERT INTO Users (UserId, Password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    connection.commit()

def main():
    st.set_page_config(layout='wide', initial_sidebar_state='expanded')

    tituloPlaceholder = st.empty()
    usuarioPlaceholder = st.empty()
    contraPlaceholder = st.empty()
    inicioPlaceholder = st.empty()
    registroPlaceholder = st.empty()
    regUsuarioPlaceholder = st.empty()
    regContraPlaceholder = st.empty()
    checkboxPlaceholder = st.empty()
    
    tituloPlaceholder.markdown('### Inicio de Sesión')
    username = usuarioPlaceholder.text_input("Nombre de Usuario")
    password = contraPlaceholder.text_input("Contraseña", type="password")

    if checkboxPlaceholder.checkbox("Registrarse"):
        usuarioNuevo = regUsuarioPlaceholder.text_input("Nuevo Nombre de Usuario")
        contraNueva = regContraPlaceholder.text_input("Nueva Contraseña", type="password")
        if registroPlaceholder.button("Registrar"):
            if register_user(usuarioNuevo, contraNueva):
                st.success("Registro exitoso. Por favor inicie sesión con sus nuevas credenciales.")
            else:
                st.error("Error al registrar. Inténtelo de nuevo.")

    if inicioPlaceholder.button("Iniciar Sesión"):
        if authenticate_user(username, password):
            st.success("Inicio de sesión exitoso. ¡Bienvenido!")

            tituloPlaceholder.empty()
            usuarioPlaceholder.empty()
            contraPlaceholder.empty()
            inicioPlaceholder.empty()
            registroPlaceholder.empty()
            regUsuarioPlaceholder.empty()
            regContraPlaceholder.empty()
            checkboxPlaceholder.empty()

            dashboard()
        else:
            st.error("Nombre de usuario o contraseña incorrectos")

if __name__ == "__main__":
    main()
