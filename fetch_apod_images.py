import argparse
from dotenv import load_dotenv
import requests

from image_manipulation import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('count', help='Количество изображений', nargs='?')
    received_args = parser.parse_args()

    count = received_args.count
    if not count:
        count = 1

    load_dotenv()
    params = {
        "api_key": os.environ['NASA_KEY'],
        'count': count
    }

    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()

    decoded_response = response.json()
    for link_number, link in enumerate(decoded_response):
        extention = get_extention(link['url'])
        filename = f'nasa_apod_{link_number}.{extention}'
        save_image(link['url'], filename)
