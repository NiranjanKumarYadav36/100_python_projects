import streamlit as st
import glob

filepaths = sorted(glob.glob("files/*.txt"))

data = {}

for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()

    letters, numbers = content.split(":")
    data[letters] = float(numbers)

chart_data = {
    'Letters': list(data.keys()),
    'Numbers': list(data.values())
}


st.title("Numbers from text file")
st.line_chart(data=chart_data, x='Letters', y='Numbers')

st.write("Letters and their values")
for l, v in data.items():
    st.write(f"{l}:{v}")

