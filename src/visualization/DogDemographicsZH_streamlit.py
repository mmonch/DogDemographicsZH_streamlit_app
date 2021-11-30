## this is a livecoding demo for streamliut
# run this in the terminal
# streamlit run src/visualization/streamlit_demo.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly import subplots
from urllib.request import urlopen
import json
import requests

#import 
# import dataframe for dogs
df = pd.read_csv(
    "./data/raw/20200306_hundehalter.csv",
    dtype={"Stadtkreis": str},
)

#import stadtquartiere ZH json
url = "https://www.ogd.stadt-zuerich.ch/wfs/geoportal/Statistische_Quartiere?service=WFS&version=1.1.0&request=GetFeature&outputFormat=GeoJSON&typename=adm_statistische_quartiere_map"
zh_quar_json = requests.get(url).json()

# Data Cleaning
# drop empty column
df.drop("RASSE2_MISCHLING", axis=1,inplace=True)

# drop duplicates (not necessary for this df)
df.drop_duplicates(subset=None, keep="first", inplace=True, ignore_index=False)

# force float datatype to connect json and df files
df.astype({"STADTQUARTIER": float}, copy=True, errors="raise")

# rename column Stadtkreis --> Kreis
#df["Kreis"] = df["STADTKREIS"]
#del df["STADTKREIS"]

# rename and drop old column to connect hson and df files
df["qnr"] = df["STADTQUARTIER"]
del df["STADTQUARTIER"]


# choropleth_mapbox of total dogs per stadtquartier
fig1 = px.choropleth_mapbox(
    df,
    geojson=zh_quar_json,
    locations="qnr",
    color="HALTER_ID",
    range_color=(151150, 152450),
    # add path as a string
    featureidkey="properties.qnr",
    mapbox_style="carto-positron",
    zoom=10,
    center={"lat": 47.3659836300, "lon": 8.5490662944},
    opacity=0.5,
    # I want to show the city district name
    # income in the city district
    labels={"HALTER_ID": "Number of Dogs", "qnr": "City District"},
    # hovertemplate =
    #'<i>Price</i>: $%{y:.2f}'+
    #'<br><b>X</b>: %{x}<br>'+
    #'<b>%{text}</b>',
    # text = ['Custom text {}'.format(i + 1) for i in range(5)],
    # showlegend = False))
    # hovertemplate = 'Price: %{y:$.2f}<extra></extra>',
)
# map bodies of water, maybe forests or greenspace # access tokens
fig1.update_geos(
    visible=False,
    resolution=50,
    showlakes=True,
    lakecolor="Blue",
    showrivers=True,
    rivercolor="Blue",
)



st.title("Dog Demographics of Zürich")
st.header("Data Exploration")

if st.sidebar.checkbox("Show Dataframe"):
    st.subheader("Dataset used for Analysis")
    st.table(data=df.head())

#streamlit mas
st.subheader("Plotly Map")
#ds_geo = px.data.carshare()

#ds_geo["lat"]=ds_geo["centroid_lat"]
#ds_geo["lon"]=ds_geo["centroid_lon"]
#with 
st.plotly_chart(fig1)