import streamlit as st

# Título de la aplicación
st.title("Hola desde Render.com")
st.subtitle("esto es de la rama main")

# Botón para mostrar el mensaje
if st.button("Mostrar mensaje"):
    st.write("Hola mundo")
