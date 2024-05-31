import streamlit as st
import pandas as pd
import plost
import mysql.connector

def dashboard():
    st.empty()
    importarDatos()
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
    cursor.execute("SELECT * FROM ClimaCDMX")
    clima_CDMX_db = cursor.fetchall()  # Obtener todos los registros de la tabla

    # Convertir los datos recuperados a un DataFrame de pandas
    clima_CDMX_df = pd.DataFrame(clima_CDMX_db, columns=['date', 'precipitation', 'temp_min', 'temp_max', 'wind'])

    st.markdown('### Heatmap')
    plost.time_hist(
        data=clima_CDMX_df,
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
    st.line_chart(clima_CDMX_df, x='date', y=plot_data, height=plot_height)


connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="streamlit"
)
cursor = connection.cursor()

def authUsuario(usuario, password):
    query = "SELECT * FROM Users WHERE UserId = %s AND Password = %s"
    cursor.execute(query, (usuario, password))
    user = cursor.fetchone()
    return user is not None

def regUsuario(usuario, password):
    query = "INSERT INTO Users (UserId, Password) VALUES (%s, %s)"
    cursor.execute(query, (usuario, password))
    connection.commit()

def importarDatos():
    clima_CDMX = pd.read_csv('ClimaCDMX.csv', parse_dates=['date'])

    for index, row in clima_CDMX.iterrows():
        query = "INSERT INTO ClimaCDMX (date, precipitation, temp_min, temp_max, wind) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (row['date'], row['precipitation'], row['temp_min'], row['temp_max'], row['wind']))
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
    usuario = usuarioPlaceholder.text_input("Nombre de Usuario")
    password = contraPlaceholder.text_input("Contraseña", type="password")

    if checkboxPlaceholder.checkbox("Registrarse"):
        usuarioNuevo = regUsuarioPlaceholder.text_input("Nuevo Nombre de Usuario")
        contraNueva = regContraPlaceholder.text_input("Nueva Contraseña", type="password")
        if registroPlaceholder.button("Registrar"):
            if regUsuario(usuarioNuevo, contraNueva):
                st.success("Registro exitoso. Por favor inicie sesión con sus nuevas credenciales.")

    if inicioPlaceholder.button("Iniciar Sesión"):
        if authUsuario(usuario, password):
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
