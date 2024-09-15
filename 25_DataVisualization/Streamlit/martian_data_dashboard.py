import streamlit as st
import pandas as pd

st.title("Mars Atmospheric Conditions Dashboard")

uploaded_file = st.file_uploader("Choose a Csv file", type='csv')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data:")
    st.table(df)

    column = st.selectbox('Select a column to visualize', df.columns[1:])
    minimum_value = df[column].min()
    maximum_value = df[column].max()
    min, max = st.slider(label="Select range to filter", min_value=minimum_value, max_value=maximum_value,
                         value=(minimum_value, maximum_value))

    df_filtered_data = df[df[column].between(min, max)]

    st.line_chart(df_filtered_data.set_index('Date')[column])
