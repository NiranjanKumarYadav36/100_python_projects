import requests

country = input("Enter country: ")

url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url)
data = response.json()
country_data = data[0]

country_capital = country_data['capital'][0]
country_region = country_data['region']
country_population = country_data['population']
country_languages = ', '.join(country_data['languages'].values())

print(f"Capital: {country_capital}")
print(f"Region: {country_region}")
print(f"Population: {country_population}")
print(f"Languages: {country_languages}")

