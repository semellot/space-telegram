import os
import requests
from pathlib import Path
from urllib.parse import urlparse


def save_image(url, filename):
    headers = {
        'User-Agent': 'curl',
    }
    rurl = 'https://api.nasa.gov/EPIC/api/natural/all'
    response = requests.get(url, params=params)
    response.raise_for_status()

    Path('images').mkdir(parents=True, exist_ok=True)
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def save_epic_image(url, filename):
    params = {
        "api_key": "K87Qp0hdauZRImQp8U4phTGq2MZu52YLBLGSc5bb"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    Path('images').mkdir(parents=True, exist_ok=True)
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def get_extention(url):
    parsed_url = urlparse(url)
    splited_path = os.path.splitext(parsed_url.path)
    extention = splited_path[-1][1:]
    return extention


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url)
    response.raise_for_status()
    decoded_response = response.json()
    links = decoded_response[12]["links"]["flickr_images"]
    for link_number, link in enumerate(links):
        extention = get_extention(link)
        filename = f'spacex_{link_number}.{extention}'
        save_image(link, filename)


def fetch_apod_images(count):
    params = {
        "api_key": "K87Qp0hdauZRImQp8U4phTGq2MZu52YLBLGSc5bb",
        "count": count
    }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    for link_number, link in enumerate(decoded_response):
        extention = get_extention(link["url"])
        filename = f'nasa_apod_{link_number}.{extention}'
        save_image(link["url"], filename)


def fetch_epic_images():
    params = {
        "api_key": "K87Qp0hdauZRImQp8U4phTGq2MZu52YLBLGSc5bb"
    }
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    response = requests.get(url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    last_date = decoded_response[0]["date"]

    url = f'https://api.nasa.gov/EPIC/api/natural/date/{last_date}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    decoded_response = response.json()
    split_date = last_date.split('-')
    for link_number, link in enumerate(decoded_response):
        filename = f'nasa_epic_{link_number}.png'
        last_name_image = link["image"]
        url_image = f'https://api.nasa.gov/EPIC/archive/natural/{split_date[0]}/{split_date[1]}/{split_date[2]}/png/{last_name_image}.png'
        save_epic_image(url_image, filename)

fetch_epic_images()
