import streamlit as st
import time

st.set_page_config(page_title="Transición", layout="centered")

# Obtener el parámetro de destino desde la URL
destino = st.query_params.get("destino", "").lower()

if destino not in ["albaran", "factura"]:
    st.error("Destino no válido. No se puede redirigir.")
    st.stop()

st.title("Cargando...")

# Spinner y barra de progreso
with st.spinner("Leyendo Documentos..."):
    barra = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        barra.progress(i + 1)

st.success("¡Comparando Documentos!")
time.sleep(0.5)

# Redirigir a la página correspondiente
if destino == "albaran":
    st.switch_page("pages/Albaran.py")
elif destino == "factura":
    st.switch_page("pages/Factura.py")
