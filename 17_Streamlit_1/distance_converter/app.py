import streamlit as st


def convert(conversion_type, distance):
    if conversion_type == 'Kilometers':
        miles = distance * 0.62137119
        return miles
    if conversion_type == 'Miles':
        km = distance * 1.609344
        return km


st.title("Distance Converter")
conversion = st.radio(label="Choose the conversion direction", options=["Kilometers to Miles", "Miles to Kilometers"])
input_value = st.number_input("Enter the distance:")
button = st.button(label="Convert")
print(conversion)

if button:
    if conversion == 'Kilometers to Miles':
        result = convert(conversion[:10], input_value)
        st.success(f"{input_value} Kilometers is equal to{result:.2f} miles")
    if conversion == 'Miles to Kilometers':
        result = convert(conversion[:5], input_value)
        st.success(f"{input_value} Miles is equal to{result:.2f} Kilometers")
