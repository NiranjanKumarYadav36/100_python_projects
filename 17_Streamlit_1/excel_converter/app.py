import streamlit as st
from views import convert_to_json, convert_to_csv

option = st.selectbox(label='Select the format of file.', options=['Json', 'CSV'])

file = st.file_uploader(label="Choose an excel fle", type=['xlsx', 'xls'])

if option is not None:
    if file is not None:
        if option == 'Json':
            json_data = convert_to_json(file)
            # st.json(json_data)
            st.download_button(label="Download", data=json_data, file_name="Europe.json", mime='text/json')

        if option == 'CSV':
            csv_data = convert_to_csv(file)
            st.download_button(label='Download', data=csv_data, file_name="Europe.csv", mime='text/csv')
