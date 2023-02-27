import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import os

st.title("Dashboard - Placement Data")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "placement.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Placement_Data_Full_Class.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
df = df.dropna()
st.dataframe(df)

type = st.selectbox("Select the Group of Study:", df['hsc_s'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['hsc_s'] == type], x="status")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['hsc_s'] == type], y="gender")
col2.plotly_chart(fig_2, use_container_width=True)

st.bar_chart(df['status'])
st.bar_chart(df['hsc_s'])
st.bar_chart(df['hsc_b'])
st.bar_chart(df['gender'])

chart_data = pd.DataFrame(df, columns=['hsc_s','status'])
st.line_chart(chart_data)