import streamlit as st
from PIL import Image

st.title("Mi Primera App!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Pasta2.png')

st.image(image, caption='Pasta2')


text = st.text_input('Escribe algo','Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora useamos 2 Columnas")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')
    
with col2:
  modo = st.radio("Que Modadlidad es la principal en tu interfaz", ('Visual','auditiva', 'Tactil'))    
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'auditiva':
    st.write('La audicion es fundamental para tu interfaz')
  if modo == 'Tactil':
    st.write('El tacto es fundamental para tu interfaz')

st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('Graciaspor presionar')
else:
  st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
  "Selecciona la modalidad",
  ("Audio", "Visual", "Haptico"),
)
if in_mod == "Audio":
