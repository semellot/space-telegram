# Публикация фотографий в Telegram-канал #
Публикация загруженных фотографий в Telegram-канал с помощью бота.

## Требования
- requests
- python-dotenv
- python-telegram-bot version 13

## Как установить
Должен быть установлен Python3.
Затем используя pip установите зависимости:

```
pip install -r requirements.txt
```

Необходимо создать telegram-бот перед использованием.
Напишите Отцу ботов https://t.me/BotFather

Отец ботов попросит дать вашему боту два имени.
Первое — для отображения в списке контактов, может быть на русском.
Второе — служебное, по нему бота можно будет найти в поиске.
Должно быть на английском и заканчиваться на bot (например, notification_bot)

Создайте в каталоге проекта файл с названием `.env` и поместите в него токен, который дал Отец ботов для доступа к HTTP API. Например:
```
BOT_TOKEN=***
```
Создайте Telegram-канал и добавьте бота, как администратора этого канала.
Добавьте ID чата в файл `.env`:
```
CHAT_ID=@name
```

Добавьте в файл `.env` период публикации по умолчанию (в секундах). Например:
```
PERIOD=14400
```
Добавьте каталог `images` с фотографиями или используйте скрипты проекта для загрузки изображений из интернета.

Перед запуском скриптов `fetch_apod_images.py` и `fetch_epic_images.py` необходимо получить API-токен NASA на сайте [тут](https://api.nasa.gov/).
Добавьте полученный токен в файл `.env`:
```
NASA_KEY=***
```

## Примеры запуска скриптов
Для публикации фотографий в Telegram-канал с периодом заданным по умолчанию запускайте скрипт без параметров:
```
% python publish_to_bot.py
```

Если нужно указать период публикации:
```
% python publish_to_bot.py 30
```

Чтобы загрузить фотографии из интернета используйте скрипты:
- fetch_apod_images.py
- fetch_epic_images.py
- fetch_spacex_images.py

### fetch_apod_images
По умолчанию скрипт скачивает одну фотографию космоса с сайта NASA и помещает в папке `images` текущего каталога:
```
% python fetch_apod_images.py
```
Но вы можете указать количество, которое скрипт должен скачать:
```
% python fetch_apod_images.py 10
```

### fetch_epic_images
Скрипт скачивает эпичные фотографии планеты Земля из космоса с сайта NASA за последнюю дату и помещает в папке `images` текущего каталога:
```
% python fetch_epic_images.py
```

### fetch_spacex_images
Скрипт скачивает фотографии последнего запуска ракет компании SpaceX и помещает в папке `images` текущего каталога:
```
% python fetch_spacex_images.py
```
Если вы знаете `id` последнего запуска, то можете скачать фотографии с этого запуска указав его в параметрах:
```
% python fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```

## Вспомогательные функции
В файле `image_manipulation.py` помещены вспомогательные функции для работы с изображениями.

### save_image
Функция сохраняет изображение.
Принимает два аргумента: ссылку на изображение и название файла при сохранении.
Проверяет существует ли директория `images` в каталоге проекта. Если нет, то создает ее.
И сохраняет изображение в эту папку.

### get_extension
Принимает ссылку на изображение и возвращает строку с названием расширения этого изображения.
