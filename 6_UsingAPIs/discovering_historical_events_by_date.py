import requests

month = int(input("Enter month no. (e.g., 7 for July): "))
day = int(input("Enter day (e.g., 2): "))

print("Fetching historical events... Please wait.")

url = f"https://history.muffinlabs.com/date/{month}/{day}"
response = requests.get(url)
data = response.json()

events = data['data']['Events']

for event in events:
    print(f"Year: {event['year']}")
    print(f"Description: {event['text']}")
    print(f"Links: {event['links'][0]['link']}")
    print("\n")
