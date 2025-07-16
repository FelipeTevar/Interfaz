import streamlit as st
import time

with st.spinner("Leyendo Documentos..."):
    for i in range(100):
        time.sleep(0.005)
        st.progress(i + 1)
st.success("¡Comparando Documentos!")

# Luego el contenido de la pantalla
st.title("Pantalla Albarán")
st.text("Instrucción:")
archivo = st.file_uploader("Adjuntar Archivo")
if archivo:
    st.success("Archivo adjuntado correctamente.")
st.text("Datos/Info de los Adjuntos:")
st.text_area("Información adicional")

