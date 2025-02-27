import streamlit as st


st.title("Mi Primera App!!")



image = Image.open('Pasta.jpg')

st.image(image, caption='Pasta')
