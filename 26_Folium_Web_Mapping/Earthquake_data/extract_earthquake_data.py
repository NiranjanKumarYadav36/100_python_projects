import requests
import pandas as pd
from datetime import datetime, timedelta, timezone


def get_data(startdate, enddate):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        'format': 'geojson',
        'starttime': startdate,
        'endtime': enddate
    }
    response = requests.get(url, params=params)
    print(response)
    data = response.json()
    return data


def extract_data(raw_data):
    clean_data = []
    features = raw_data['features']
    for feature in features:
        earthquake = {
            'Magnitude': feature['properties']['mag'],
            'Location': feature['properties']['place'],
            'Latitude': feature['geometry']['coordinates'][1],
            'Longitude': feature['geometry']['coordinates'][0]
        }
        clean_data.append(earthquake)
    return clean_data


def save_to_csv(data, path):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)


# Calculate yesterday's date
yesterday = datetime.now(timezone.utc) - timedelta(days=1)
startdate = yesterday.strftime('%Y-%m-%d')
enddate = (yesterday + timedelta(days=1)).strftime('%Y-%m-%d')

# Fetch, process, and save earthquake data for yesterday
raw_data = get_data(startdate, enddate)
clean_data = extract_data(raw_data)
save_to_csv(clean_data, 'earthquakes_yesterday.csv')

print(clean_data)
