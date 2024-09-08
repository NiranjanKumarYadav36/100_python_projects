import streamlit as st
from faker import Faker

fake = Faker()


def generate_names(number):
    names = [fake.name() for i in range(number)]
    return names


st.title("Random Name Generator")


num_input = st.number_input(label="Enter the number of name to generate", min_value=1, max_value=100, step=1, value=5)
button = st.button(label="Generate")

if button:
    names = generate_names(num_input)
    st.subheader("Generated Names")
    for i in names:
        st.write(i)
