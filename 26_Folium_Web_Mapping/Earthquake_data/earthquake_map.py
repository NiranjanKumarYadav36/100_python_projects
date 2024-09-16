import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.set_page_config(layout='wide')
st.title('Earthquake Global Map')
df = pd.read_csv('earthquakes_yesterday.csv')

mean_lat = df['Latitude'].mean()
mean_long = df['Longitude'].mean()
m = folium.Map(location=[mean_lat, mean_long], zoom_start=2)

for i, rows in df.iterrows():
    # print(i, rows)
    latitude = rows['Latitude']
    longitude = rows['Longitude']
    magnitude = rows['Magnitude']
    location = rows['Location']
    folium.CircleMarker(
        location=[latitude, longitude],
        radius=magnitude * 2,
        color='crimson',
        fill=True,
        fiil_color='crimson',
        tooltip=f"Loc:{location}, Mag:{magnitude}"
    ).add_to(m)
m.save('earthquake_map.html')

st_folium(m, width=1400)
