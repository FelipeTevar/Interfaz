# Código para el archivo home.py con navegación a través de una pantalla de transición

import streamlit as st

# Título de la pantalla inicial
st.title("Pantalla Inicial")

# Botón para ir a Albarán con pantalla de transición
if st.button("Ir a Albarán"):
    st.experimental_set_query_params(destino="albaran")
    st.switch_page("pages/Transicion.py")

# Botón para ir a Factura con pantalla de transición
if st.button("Ir a Factura"):
    st.experimental_set_query_params(destino="factura")
    st.switch_page("pages/Transicion.py")

