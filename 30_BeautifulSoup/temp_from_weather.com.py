import requests
from bs4 import BeautifulSoup


def get_weather(lat, lon):

    url = f"https://weather.com/weather/today/l/{lat},{lon}"
    print(url)
    # Step 1:
    content = requests.get(url).text
    # print(content)

    # Step 2:
    soup = BeautifulSoup(content, 'html.parser')
    # print(soup)

    temp = soup.find(class_="CurrentConditions--tempValue--MHmYY").get_text()
    print(temp)


lat = input("Enter the latitude: ")
lon = input("Enter the longitude: ")

get_weather(lat, lon)
