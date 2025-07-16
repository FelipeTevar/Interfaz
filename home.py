import streamlit as st

st.title("Pantalla Inicial")

# Botones que redirigen a la pantalla de transición con el parámetro 'destino'
col1, col2 = st.columns(2)
with col1:
    if st.button("Ir a Albarán"):
        st.query_params["destino"] = "albaran"
        st.switch_page("pages/Transicion.py")
with col2:
    if st.button("Ir a Factura"):
        st.query_params["destino"] = "factura"
        st.switch_page("pages/Transicion.py")