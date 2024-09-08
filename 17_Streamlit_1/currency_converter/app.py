import streamlit as st
import requests

api_key = ""
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"


def convert(conversion, currency_value):
    response = requests.get(url)
    data = response.json()
    conversion_rate = data['conversion_rates']['EUR']
    result = currency_value * conversion_rate
    return result


st.title("Currency Converter")
conversion = st.radio(label="Choose the conversion", options=["USD to EUR", "EUR to USD"])
input_value = st.number_input("Enter the input amount:")
button = st.button(label="Button")

if conversion == 'USD to EURO':
    if button:
        euros = convert(conversion[:3], input_value)
        st.success(f"{input_value} {conversion} is equal to {euros:.2f} {conversion[-3:]}")
else:
    if button:
        dollars = convert(conversion[:3], input_value)
        st.success(f"{input_value} {conversion} is equal to {dollars:.2f} {conversion[-3:]}")
