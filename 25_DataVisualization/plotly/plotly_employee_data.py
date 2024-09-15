import pandas as pd
import plotly.express as px

df = pd.read_csv('employees (1).csv')

fig = px.scatter(df,
                 title="Salary vs Performance Score by Department",
                 x='PerformanceScore',
                 y='Salary',
                 color='Department',
                 hover_data={
                     'Name': True,
                     'Position': True,
                     'Gender': True
                 })
fig.show()
