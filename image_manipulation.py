from dotenv import load_dotenv
import os
import requests

from pathlib import Path
from urllib.parse import urlparse


def save_image(url, filename):
    load_dotenv()
    params = {
        "api_key": os.environ['NASA_KEY']
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
