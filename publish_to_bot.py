import telegram


bot = telegram.Bot(token='5757191574:AAFWlVI8zFimFbwb-hr07TKEm0ZW7kKaizg')
bot.send_message(text='Hello World!', chat_id="@epic_space")
bot.send_photo(chat_id="@epic_space", photo=open('images/nasa_apod_0.jpg', 'rb'))
