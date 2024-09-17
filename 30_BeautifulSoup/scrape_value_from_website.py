from bs4 import BeautifulSoup
import requests

url = "https://forecast.weather.gov/MapClick.php?lat=40.4176&lon=-75.4552"


# Step 1: Get the page content
content = requests.get(url).text
# print(content)


# Step 2: Extract the temperature value
soup = BeautifulSoup(content, 'html.parser')
# print(soup)

temp = soup.find(class_='myforecast-current-lrg').get_text()
print(temp)

