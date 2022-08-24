import argparse
import requests

from image_manipulation import save_image, get_extension


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('launch_id', help='ID запуска', nargs='?')
    received_args = parser.parse_args()

    launch_id = received_args.launch_id
    if not launch_id:
        url = 'https://api.spacexdata.com/v5/launches'
        response = requests.get(url)
        response.raise_for_status()
        decoded_response = response.json()
        for launch in decoded_response:
            links = launch['links']['flickr']['original']
            if links:
                break
    else:
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
        response = requests.get(url)
        response.raise_for_status()
        decoded_response = response.json()
        links = decoded_response['links']['flickr']['original']

    for link_number, link in enumerate(links):
        extension = get_extension(link)
        filename = f'spacex_{link_number}{extension}'
        save_image(link, filename)
