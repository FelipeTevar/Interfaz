import streamlit as st

st.set_page_config(page_title="Pantalla Factura", layout="centered")
st.title("Pantalla Factura")

st.text("Contenido:")
st.text("Info datos documentos")

st.write("¿Quiere modificar línea de pedido?")
col1, col2 = st.columns(2)
with col1:
    if st.button("Sí"):
        st.info("Modificando línea de pedido...")
with col2:
    if st.button("No"):
        st.warning("No se modificará la línea.")
