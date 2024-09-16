import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
import pandas as pd

st.set_page_config(layout="wide")
st.title("Accidents")

df = pd.read_csv('accidents.csv', sep=';')

m = folium.Map(location=[34, -86], zoom_start=4)
map_cluster = MarkerCluster().add_to(m)

for _, rows in df.iterrows():
    lat = rows['LATITUDE']
    lon = rows['LONGITUD']

    folium.Marker(location=[lat, lon],
                  tooltip=rows['MAN_COLLNAME']
    ).add_to(map_cluster)

m.save("accidents_map.html")

# Render the map in the Streamlit app
st_folium(m, width=1400, height=400)
