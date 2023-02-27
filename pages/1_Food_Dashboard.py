import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "food.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Food_Preference.csv")

st.title("Dashboard - Food Preference Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
df = df.dropna()
st.dataframe(df)

food = st.selectbox("Select the Food Type:", df['Food'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Food'] == food], x="Gender")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Food'] == food], y="Nationality")
col2.plotly_chart(fig_2, use_container_width=True)

st.bar_chart(df['Nationality'])
st.bar_chart(df['Gender'])
st.bar_chart(df['Food'])

chart_data = pd.DataFrame(df, columns=['Food','Nationality'])
st.line_chart(chart_data)

a = pd.DataFrame(df, columns=['Food','Nationality'])
st.area_chart(a)