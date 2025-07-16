import streamlit as st
import time

with st.spinner("Leyendo Documentos..."):
    for i in range(100):
        time.sleep(0.005)
        st.progress(i + 1)
st.success("¡Comparando Documentos!")

# Contenido de la pantalla
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
