import argparse
import requests

from image_manipulation import *


if __name__ == '__main__':
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
        save_image(url_image, filename)
