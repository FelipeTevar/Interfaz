import streamlit as st

st.set_page_config(page_title="Pantalla Inicial", layout="centered")
st.title("Pantalla Inicial")

# Navegación con pantalla de transición usando URL con parámetro
col1, col2 = st.columns(2)
with col1:
    if st.button("Ir a Albarán"):
        st.switch_page("pages/Transicion.py?destino=albaran")
with col2:
    if st.button("Ir a Factura"):
        st.switch_page("pages/Transicion.py?destino=factura")
