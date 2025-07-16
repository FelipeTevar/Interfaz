# Crear el archivo 'pages/Transicion.py' con la lógica de pantalla de carga y redirección

transicion_code = '''
import streamlit as st
import time

# Obtener el destino desde los parámetros de la URL
query_params = st.experimental_get_query_params()
destino = query_params.get("destino", [""])[0].lower()

st.title("Cargando...")

# Spinner y barra de progreso en tiempo real
with st.spinner("Leyendo Documentos..."):
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)

st.success("¡Comparando Documentos!")

# Redirigir a la página de destino
if destino == "albaran":
    st.switch_page("pages/Albaran.py")
elif destino == "factura":
    st.switch_page("pages/Factura.py")
else:
    st.error("Destino no válido. No se puede redirigir.")
'''

# Guardar el archivo en la carpeta 'pages'
import os

os.makedirs("pages", exist_ok=True)
with open("pages/Transicion.py", "w", encoding="utf-8") as f:
    f.write(transicion_code)

print("Archivo 'pages/Transicion.py' creado correctamente.")

