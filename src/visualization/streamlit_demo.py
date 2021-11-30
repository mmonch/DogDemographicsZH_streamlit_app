## this is a livecoding demo for streamliut
# run this in the terminal
# streamlit run src/visualization/streamlit_demo.py

import pandas as pd 
import streamlit as st
#import 
mpg_df=pd.read_csv("./data/raw/mpg.csv")

st.title("introduction to Streamlit")
st.header("MPG Data Exploration")

st.table(data=mpg_df.head())

#streamlit mas
st.subheader("Streamlit Map")
ds_geo = px.data.carshare()

ds_geo["lat"]=ds_geo["centroid_lat"]
ds_geo["lon"]=ds_geo["centroid_lon"]

st.map(ds_geo)