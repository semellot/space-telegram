import argparse
from dotenv import load_dotenv
import os
import random
import time

import telegram


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['BOT_TOKEN']
    bot = telegram.Bot(token=token)

    for files in os.walk('images'):
        images = files[2]
    random.shuffle(images)

    parser = argparse.ArgumentParser()
    parser.add_argument('period', help='Период публикации (в секундах)', nargs='?')
    received_args = parser.parse_args()

    if received_args.period:
        period = int(received_args.period)
        print(period)
    else:
        period = int(os.environ['PERIOD'])
        print(period)

    while True:
        for image in images:
            bot.send_photo(chat_id="@epic_space", photo=open(f'images/{image}', 'rb'))
            time.sleep(period)
