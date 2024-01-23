import telebot
import random

TOKEN = '6974611164:AAEGSjbK3AWnlnrX6g8QppsaKMhO4Ba8uz4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет! Я бот-визитка.\n"
                                      f"Мой разработчик Потёмкин Михаил Дмитриевич.\n"
                                      f"Что бы узнать про все команды напишите /help")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Я могу отвечать на некоторые сообщения так же у меня есть команды /start, /help, /achievements, /me, /meme.")

@bot.message_handler(commands=['achievements'])
def send_image(message):
    chat_id = message.chat.id
    photo_path = '../info/dost.jpg'
    photo = open(photo_path, 'rb')
    bot.send_message(message.chat.id, f"Достижения Потёмкина Михаила Дмитревича\n"
                                      f"Я и мои кенты где-то в горах на Байкале")
    bot.send_photo(chat_id, photo)

@bot.message_handler(commands=['me'])
def send_image(message):
    bot.send_message(message.chat.id, f"ФИО: Потёмкина Михаила Дмитревича \n"
                                      f"Возраст: 14\n"
                                      f"Хобби: Програмирование, Спортивный nуризм\n"
                                      f"Любимые онлайн игры: Fortinate, WarThunder\n"
                                      f"Любимые офлайн игры: Subnatica, Xcom, Cyberpank, и другие\n")

@bot.message_handler(commands=['meme'])
def send_image(message):
    a = random.randint(1,8)
    if a == 1:
        chat_id = message.chat.id
        photo_path = '../info/meme1.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(chat_id, photo)
    elif a == 2:
        chat_id = message.chat.id
        photo_path = '../info/meme2.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(chat_id, photo)
    elif a == 3:
        chat_id = message.chat.id
        photo_path = '../info/meme3.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(chat_id, photo)
    elif a == 4:
        chat_id = message.chat.id
        photo_path = '../info/meme4.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(chat_id, photo)
    elif a == 5:
        chat_id = message.chat.id
        photo_path = '../info/meme5.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(chat_id, photo)
    elif a == 6:
        chat_id = message.chat.id
        photo_path = '../info/meme6.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(chat_id, photo)
    elif a == 7:
        chat_id = message.chat.id
        photo_path = '../info/meme7.jpg'
        photo = open(photo_path, 'rb')
        bot.send_photo(chat_id, photo)
    else:
        bot.send_message(message.chat.id, "Програмисты не шутят")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if 'ку ' in message.text.lower() or message.text.lower() == "ку":
        bot.reply_to(message, 'ку')
    elif 'привет ' in message.text.lower() or message.text.lower() == "привет":
        bot.reply_to(message, 'привет')
    elif 'hello ' in message.text.lower() or message.text.lower() == "hello":
        bot.reply_to(message, 'Ай спиек енглишь веру вел')
    elif 'c++' in message.text.lower() or 'python' in message.text.lower() or 'питон' in message.text.lower():
        bot.send_message(message.chat.id, "Я этот язык знаю")
    else:
        bot.send_message(message.chat.id, f"не пон")


@bot.message_handler(content_types=['photo','audio','video','animation','document'])
def handle_photo(message):
    bot.send_message(message.chat.id, "Нормально общайся пж")

bot.polling()