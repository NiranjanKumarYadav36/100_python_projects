import pandas as pd
import plotly.express as px

df = pd.read_csv('houses.csv')
print(df)

fig = px.scatter(df,
                 x='Size',
                 y='Price',
                 color='Location',
                 hover_data={'Bedrooms': True,
                             'Bathrooms': True},
                 title="House Price vs House Size")
fig.show()
