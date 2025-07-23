# Examen_TT_bueno
Proyecto del sprint 7 de triple ten


Examen_TT_bueno

Análisis Exploratorio de Datos de Vehículos con Streamlit y Plotly

Este proyecto es una aplicación web interactiva desarrollada con Streamlit que permite realizar un análisis exploratorio básico sobre un conjunto de datos de anuncios de venta de vehículos en Estados Unidos (vehicles_us.csv).

Funcionalidad

Histograma de odómetro: Genera un histograma interactivo que muestra la distribución de los valores del odómetro de los vehículos.

Gráfico de dispersión (Scatter): Construye un diagrama de dispersión que visualiza la relación entre el kilometraje (odómetro) y el precio de los vehículos.

Cada gráfico se construye al hacer clic en botones específicos, facilitando la exploración dinámica de los datos.

Estructura del proyecto

app.py: Archivo principal de la aplicación Streamlit.

vehicles_us.csv: Conjunto de datos en formato CSV de anuncios de vehículos.

notebooks/EDA.ipynb: Notebook de Jupyter con ejemplos de análisis exploratorio usando Pandas y Plotly.

requirements.txt: Lista de dependencias (pandas, plotly, streamlit).

vehicles_env/: Entorno virtual (excluido por .gitignore).

Instrucciones de uso

Clona el repositorio y sitúate en la carpeta raíz:

git clone https://github.com/<tu-usuario>/Examen_TT_bueno.git
cd Examen_TT_bueno

Crea y activa el entorno virtual:

python -m venv vehicles_env
# Windows (PowerShell)
.\\vehicles_env\\Scripts\\Activate.ps1
# macOS/Linux
source vehicles_env/bin/activate

Instala las dependencias:

pip install pandas plotly streamlit

Ejecuta la aplicación:

streamlit run app.py

Abre el navegador en la dirección que mostrará Streamlit (por defecto http://localhost:8501).

Desarrollado como parte del proyecto Examen_TT de Triple Ten.


##Enlace al despliegue

La aplicación está disponible en (Render):

https://examen-tt-bueno.onrender.com*


