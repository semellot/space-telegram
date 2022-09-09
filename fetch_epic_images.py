from dotenv import load_dotenv
from datetime import datetime
import os
import requests

from image_manipulation import save_image


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    params = {
        "api_key": api_key
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

    date = datetime.fromisoformat(last_date)
    full_date = date.strftime("%Y/%m/%d")
    for link_number, link in enumerate(decoded_response):
        filename = f'nasa_epic_{link_number}.png'
        last_name_image = link["image"]
        url_image = f'https://api.nasa.gov/EPIC/archive/natural/{full_date}/png/{last_name_image}.png'
        save_image(url_image, filename, api_key)
