import streamlit as st

st.set_page_config(page_title="Pantalla Inicial", layout="centered")
st.title("Pantalla Inicial")

# Navegación con pantalla de transición
col1, col2 = st.columns(2)
with col1:
    if st.button("Ir a Albarán"):
        st.query_params["destino"] = "albaran"
        st.switch_page("pages/Transicion.py")
with col2:
    if st.button("Ir a Factura"):
        st.query_params["destino"] = "factura"
        st.switch_page("pages/Transicion.py")
