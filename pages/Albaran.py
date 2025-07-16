
import streamlit as st

st.title("Pantalla Albarán")

st.text("Instrucción:")
archivo = st.file_uploader("Adjuntar Archivo")
if archivo:
    st.success("Archivo adjuntado correctamente.")

st.text("Datos/Info de los Adjuntos:")
st.text_area("Información adicional")
