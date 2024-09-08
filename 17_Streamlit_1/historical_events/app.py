import streamlit as st
import requests

st.title("Historical Events Viewer")
st.write("Enter a date to retrieve historical events.")

month = st.number_input(label="Enter the month(e.g.,7 for July):", min_value=1, max_value=12, value=7, step=1)
day = st.number_input(label="Enter the day(e.g.,1 for the 1st):", min_value=1, max_value=31, value=1, step=1)
button = st.button(label="Show Events")

if button:
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)
    data = response.json()

    events = data['data']["Events"]

    for event in events:
        year = event["year"]
        description = event["text"]
        links = event["links"][0]["link"]
        st.write(f"Year:{year}")
        st.write(f"Description:{description}")
        st.write(f"Link:{links}")
        st.markdown("-"*100)
