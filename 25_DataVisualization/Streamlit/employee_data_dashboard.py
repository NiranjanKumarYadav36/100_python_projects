import streamlit as st
import pandas as pd

st.title("Employee Data Dashboard")

uploaded_file = st.file_uploader("Choose a csv file", type='csv')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data:")
    st.table(df)

    column = st.selectbox("Select a column to plot", df.columns.to_list())

    st.write(f"Plotting column:{column}")

    # st.line_chart(df.set_index('EmployeeID')[column])
    st.line_chart(df[column])
