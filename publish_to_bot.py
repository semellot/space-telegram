import argparse
import os
import random
import time

from dotenv import load_dotenv
from requests.exceptions import ConnectionError
import telegram


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']

    bot = telegram.Bot(token=token)

    for files in os.walk('images'):
        images = files[2]
    random.shuffle(images)

    period = int(os.environ['PERIOD'])
    parser = argparse.ArgumentParser()
    parser.add_argument('period', help='Период публикации (в секундах)', nargs='?', default=period)
    received_args = parser.parse_args()

    period = received_args.period

    while True:
        for image in images:
            with open(os.path.join('images', image), 'rb') as file:
                try:
                    bot.send_photo(chat_id=chat_id, photo=file)
                    time.sleep(period)
                except telegram.error.TelegramError:
                    time.sleep(360)
