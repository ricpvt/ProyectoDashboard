# Dashboard Clima CDMX (2020-2024)

Este Dashboard fue creado con streamlit para mostrar el clima de la Ciudad de México desde el 01/01/2020 hasta el 20/04/2024.

## Requisitos

Este programa esta hecho en Python con las librerías streamlit, pandas, plost y  mysql-connector.

Para instalar estas librerías se tiene que ejecutar los siguientes comandos en la terminal de Python:

```python
pip install streamlit
```

```python
pip install pandas
```

```python
pip install plost
```

```python
pip install mysql-connector
```

Para ejecutar el programa se tiene que ejecutar el siguiente comando en cualquier terminal:

```
streamlit run streamlit_app.py
```

También es necesario MySQL (este programa se realizo con la versión 8.0.37). El archivo MySQL.sql contiene un script el cual genera una tabla para los usuarios registrados.

## Caracteristicas
En este programa se puede iniciar sesion para acceder una dashboard que muestra datos del clima de la Ciudad de Mexico desde 01-01-2020 hasta 20-04-2024.

Pantalla de login:
![imagen](https://github.com/ricpvt/ProyectoDashboard/assets/158591406/9566376a-cd48-43a1-a44b-d515c35250ef)
Dashboard:
![imagen](https://github.com/ricpvt/ProyectoDashboard/assets/158591406/610ebad7-11af-4174-9016-9af10a4d41b1)

En la parte de la izquierda se muestran opciones para mostrar los datos en el dashboard.
En esta parte puedes elegir entre la temperatura maxima y la minima. Esto se refleja en la intensidad del color de las casillas en el heatmap.

![imagen](https://github.com/ricpvt/ProyectoDashboard/assets/158591406/fb64397b-d9a8-470e-89f0-4df86fe24f19)

Abajo se pueden elegir los datos a mostrar en la grafica de linea.

![imagen](https://github.com/ricpvt/ProyectoDashboard/assets/158591406/d5cac97d-2ee9-4d97-be1f-8019de1d22db)


