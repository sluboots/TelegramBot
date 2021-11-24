import telebot
import requests
import random

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

bot = telebot.TeleBot('2006001446:AAHb8J2UHV7Vek-Ag7Yhv3o44iVvS51anKA')
print(telebot)

@bot.message_handler(commands=['photo'])
def photo(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Собачки', callback_data='get_dog'),
    telebot.types.InlineKeyboardButton('Котики', callback_data='get_cat'))
    keyboard.row(telebot.types.InlineKeyboardButton('Лисички', callback_data='get_fox'),
    telebot.types.InlineKeyboardButton('HTTP-коты', callback_data='get_http_cat'))
    bot.send_message(message.from_user.id, 'Выберите какую картинку вы хотите', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.from_user.id, 'Данный бот выдает картинки животных по выбору. \n'
    'Напишите /photo для выбора')
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.answer_callback_query(call.id)
    send_photo(call.message, call.data)



def send_photo(message, data):
    if data == 'get_dog':
        dog = requests.get('https://random.dog/woof.json')
    #print(dog.text[-5:-2])
    #print(dog.text[dog.text.find('h'):-2])
        if dog.text[-5:-2] == 'jpg' or dog.text[-5:-2] == 'JPG' or dog.text[-5:-2] == 'png' or dog.text[-5:-2] == 'PNG':
            bot.send_photo(message.chat.id, dog.text[dog.text.find('h'):-2])
        else:
            bot.send_video(message.chat.id, dog.text[dog.text.find('h'):-2])
    elif data == 'get_fox':
        fox = requests.get('https://randomfox.ca/floof/')
        fox_url = fox.text[10:]
    #print(fox_url[:fox_url.find('"')])
    #print(fox_url[:fox_url.find('"')].replace('\\', ''))
        bot.send_photo(message.chat.id, fox_url[:fox_url.find('"')].replace('\\', ''))
    elif data == 'get_cat':
        number_cat = random.randint(1, 200)
        source_cat = requests.get(f'https://aws.random.cat/view/{number_cat}').text
        if "id=\"cat" in source_cat:
            bot.send_photo(message.chat.id, source_cat.split("src=\"")[1].split("\"")[0])
    elif data == 'get_http_cat':
        id_http_cat = [100, 101, 102, 200, 201, 202, 203, 204, 206, 207, 300 ,301, 302, 303, 304, 305, 307, 308, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409,
                           410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 421, 422, 423, 424, 425, 426, 429, 431, 444, 450, 451, 497, 498, 500, 501, 502, 503, 504,
                           506, 507, 508, 509, 510, 511, 521, 523, 525, 599]
        bot.send_photo(message.chat.id, f'https://http.cat/{id_http_cat[random.randint(0, len(id_http_cat)-1)]}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, 'Введите /photo для выбора картинки');
    elif message.text == '/help':
        bot.send_message(message.from_user.id, "Напишите /photo или 'Хочу картинку'")
    elif message.text == 'Хочу картинку':
        bot.send_message(message.from_user.id, 'Введите /photo для выбора картинки');
    else:
        bot.send_message(message.from_user.id, "Напишите /help")



bot.polling(none_stop=True, interval=0)

# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/