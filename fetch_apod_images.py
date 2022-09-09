import argparse
from dotenv import load_dotenv
import os
import requests

from image_manipulation import save_image, get_extension


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument('count', help='Количество изображений', nargs='?', default=1)
    received_args = parser.parse_args()

    count = received_args.count

    params = {
        "api_key": api_key,
        'count': count
    }

    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()

    decoded_response = response.json()
    for link_number, link in enumerate(decoded_response):
        if 'url' not in link:
            continue
        extensions = ('.jpg', '.png', '.gif')
        if link['url'].endswith(extensions):
            extension = get_extension(link['url'])
            filename = f'nasa_apod_{link_number}{extension}'
            save_image(link['url'], filename)
