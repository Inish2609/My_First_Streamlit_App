import streamlit as st
from PIL import Image
st.title('Hello, EveryOne! :wave:')
st.title('Welcome to My Data App! :smile:')
st.balloons()
st.header("I am Inish Raj B :sunglasses:")
st.subheader("Student @ Mepco Schlenk Engineering College | Aritificial Intelligence and Data Science | Data Science Enthusiast | Proficient Full Stack Developer")


image = Image.open('resources\images\photo.jpg')
st.image(image, use_column_width='auto')