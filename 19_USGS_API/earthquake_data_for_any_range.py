import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

def get_data(start_date, end_date):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": start_date,
        "endtime": end_date
    }

    response = requests.get(url, params)
    data = response.json()
    return data


def extract_data(raw_data):
    features = raw_data['features']
    earthquake_data = []
    for feature in features:
        earthquake = {
            "magnitude": feature['properties']['mag'],
            'location': feature['properties']['place'],
            "langitude": feature['geometry']['coordinates'][1],
            "longtiude": feature['geometry']['coordinates'][2]
        }
        earthquake_data.append(earthquake)

    return earthquake_data


def get_csv(data, file_fath):
    df = pd.DataFrame(data)
    df.to_csv(file_fath, index=False)


yesterday = datetime.now(timezone.utc) - timedelta(days=1)
startdate = yesterday.strftime('%Y-%m-%d')
enddate = (yesterday + timedelta(days=1)).strftime('%Y-%m-%d')

raw_data = get_data(startdate, enddate)
data = extract_data(raw_data)
get_csv(data, 'earthquake_data.csv')
