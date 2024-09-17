import requests

url = "https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_station/"


def get_station_filepath():
    with open('stations.txt', 'r') as file:
        file_name = file.readlines()

    file_name = [f"{name.strip()}.csv.gz" for name in file_name]
    print(file_name)
    return file_name


def construct_url(filepath):
    file_url = f"{url}{filepath}"
    return file_url


def download_file(file_url, filepath):
    response = requests.get(file_url)
    with open(filepath, 'wb') as file:
        file.write(response.content)


filepath = get_station_filepath()
for name in filepath:
    file_url = construct_url(name)
    download_file(file_url, name)
