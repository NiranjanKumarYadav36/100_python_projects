import requests

url = "https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/"


def construct_filepath(year):
    filepath = f"{year}.csv.gz"
    return filepath


def construct_file_ulr(filepath):
    fileurl = f"{url}{filepath}"
    return fileurl


def download_file(file_url, file_path):
    response = requests.get(file_url)
    with open(file_path, 'wb') as file:
        file.write(response.content)


for year in range(1800, 1805):
    file_path = construct_filepath(year)
    file_ulr = construct_file_ulr(file_path)
    download_file(file_ulr, file_path)
