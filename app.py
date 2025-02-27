import streamlit as st


st.title("Mi Primera App!!")



image = Image.open('Pasta.png')

st.image(image, caption='Pasta')
