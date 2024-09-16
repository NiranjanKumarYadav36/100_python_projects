import streamlit as st
import folium
from streamlit_folium import folium_static, st_folium
import pandas as pd

st.set_page_config(layout="wide")

# Create a Streamlit app
st.title("European Countries Map")

df = pd.read_csv("europe.csv")
print(df)

# Calculate the mean latitude and longitude for centering the map
mean_latitude = df['Latitude'].mean()
mean_longitude = df['Longitude'].mean()

# Create a Folium map centered around Europe
m = folium.Map(location=[mean_latitude, mean_longitude], zoom_start=4)

# Add country names as labels to the map
for i, rows in df.iterrows():
    latitude = rows['Latitude']
    longitude = rows['Longitude']
    country_name = rows['Country']
    folium.Marker(location=[latitude, longitude],
                  tooltip=f"{country_name}",
    ).add_to(m)

m.save("europe_map.html")

# Render the Folium map using Streamlit
st_folium(m, width=1400, height=800)
