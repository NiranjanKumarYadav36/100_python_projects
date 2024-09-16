import requests

API_KEY = "2c156ae82747d4e6768ac7329f33087c"


def get_temperature(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    temp = data['main']['temp']
    return temp


city = input("Enter city: ")
temperature = get_temperature(city)

temp_type = input("Choose temperature unit (C for Celsius, F for Fahrenheit): ").strip().upper()

if temp_type == 'C':
    print(f"Current temperature in {city}: {temperature}C")
if temp_type == 'F':
    temperature = (temperature * (9/5)) + 32
    print(f"Current temperature in {city}: {temperature}F")
