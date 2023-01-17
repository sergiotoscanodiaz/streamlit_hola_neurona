import streamlit as st
from PIL import Image

image = Image.open('neurona.jpg')

st.image(image)

st.header("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.subheader("Una neurona con una entrada y un peso")

    w = st.slider("Peso", 0.0, 5.0, key="w")

    x = st.number_input("Introduzca el valor de la entrada:", key="x")

    y = x * w

    if st.button("Calcular la salida", key="b1"):
        st.text(f"La salida de la neurona es: {y}")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        w0 = st.slider("Peso w0", 0.0, 5.0, key="w0")
        x0 = st.number_input("Entrada x0:", key="x0")
    with col2:
        w1 = st.slider("Peso w1", 0.0, 5.0, key="w1")
        x1 = st.number_input("Entrada x1:", key="x1")
    y = x0 * w0 + x1 * w1
    if st.button("Calcular la salida", key="b2"):
        st.text(f"La salida de la neurona es: {y}")

with tab3:
    col1, col2, col3 = st.columns(3)
    with col1:
        w0 = st.slider("Peso w0", 0.0, 5.0, key="w01")
        x0 = st.number_input("Entrada x0:", key="x01")
    with col2:
        w1 = st.slider("Peso w1", 0.0, 5.0, key="w11")
        x1 = st.number_input("Entrada x1:", key="x11")
    with col3:
        w2 = st.slider("Peso w2", 0.0, 5.0, key="w2")
        x2 = st.number_input("Entrada x1:", key="x2")
    b = st.number_input("Introduzca el valor del sesgo:")
    y = x0 * w0 + x1 * w1 + x2 * w2 + b
    if st.button("Calcular la salida", key="3"):
        st.text(f"La salida de la neurona es: {y}")