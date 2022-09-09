import os
import requests

from pathlib import Path
from urllib.parse import urlparse


def save_image(url, filename, api_key=''):
    params = {
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    Path('images').mkdir(parents=True, exist_ok=True)
    with open(os.path.join('images', filename), 'wb') as file:
        file.write(response.content)


def get_extension(url):
    parsed_url = urlparse(url)
    splitted_path = os.path.splitext(parsed_url.path)
    extension = splitted_path[-1]
    return extension
