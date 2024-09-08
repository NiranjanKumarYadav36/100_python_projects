import requests

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
content = response.json()

country_name = input("Enter country name: ").title()

for c in content:
    if country_name == c["name"]["common"]:
        country_capital = c["capital"][0]
        print(country_capital)

