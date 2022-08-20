import argparse
import requests

from image_manipulation import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('count', help='Количество изображений', nargs='?')
    received_args = parser.parse_args()

    count = received_args.count
    if not count:
        count = 1
    params = {
        'api_key': 'K87Qp0hdauZRImQp8U4phTGq2MZu52YLBLGSc5bb',
        'count': count
    }
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=params)
    response.raise_for_status()

    decoded_response = response.json()
    for link_number, link in enumerate(decoded_response):
        print(link['url'])
        extention = get_extention(link['url'])
        filename = f'nasa_apod_{link_number}.{extention}'
        save_image(link['url'], filename)
