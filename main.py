import telebot
import random
from telebot import types
TOKEN = '6974611164:AAEGSjbK3AWnlnrX6g8QppsaKMhO4Ba8uz4'
bot = telebot.TeleBot(TOKEN)

users = {}

enemy_list = ["Гоблин", "Призрак", "Троль", "Слайм", "Вампир", "Зомби"]


@bot.message_handler(commands=['start'])
def start(message):
    global users, player_hp, player_pr, enemy, enemy_hp, event_count, fvic
    player_hp = 100
    player_at = 0
    player_pr = 0
    enemy_hp = 0
    enemy_at = 0
    enemy_defense = 0
    event_count = 0
    fvic = False
    enemy = ''
    user_id = message.from_user.id
    sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
    users.update({user_id: sp})
    print(users)
    event_count = 0
    bot.send_message(message.chat.id, "Добро пожаловать в мини RPG игру! Готовы начать?")
    bot.send_message(message.chat.id, "Введите /battle, чтобы начать сражение!")

@bot.message_handler(commands=['battle'])
def battle(message):
    global player_hp, enemy_hp, event_count, enemy_defense, enemy,users, users
    user_id = message.chat.id
    sp = users.get(user_id)
    print(message.from_user.username)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    event_count += 1
    enemy = random.choice(enemy_list)
    enemy_hp = random.randint(50, 100)
    enemy_defense = random.randint(3, 6)
    print(users,sp)
    sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
    print(sp)
    print(user_id)
    users[user_id] = sp
    print(users)
    print(user_id)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Обычная атака', callback_data='attack'))
    keyboard.add(types.InlineKeyboardButton(text='Сильная атака', callback_data='strong_attack'))
    keyboard.add(types.InlineKeyboardButton(text='Защита', callback_data='defend'))
    bot.send_message(message.chat.id, f"Ваш враг: {enemy} (ХП: {enemy_hp})")
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)


@bot.message_handler(commands=['attack'])
def attack(message):
    global player_hp, enemy_hp, player_at, fvic, enemy_defense, enemy
    user_id = message.chat.id
    sp = users.get(user_id)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    damage = random.randint(10, 20) + player_at - enemy_defense
    damage = int(damage)
    enemy_hp -= damage
    fvic = 0
    if enemy_hp > 0:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        bot.send_message(message.chat.id, f"Вы нанесли {damage} урона! (Враг: {enemy_hp} ХП)")
        enemy_attack(message,1)
    elif enemy_hp <= 0 and enemy == "Князь Тьмы":
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        fullvictory(message)
    elif player_hp <= 0:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        defeat(message)
    else:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        victory(message)

@bot.message_handler(commands=['strong_attack'])
def strong_attack(message):
    global player_hp, enemy_hp, player_at, fvic, enemy_defense,users
    user_id = message.chat.id
    print(user_id)
    print(message.from_user.username)
    print(message.chat.first_name)
    print(message.chat)
    sp = users.get(user_id)
    print(users,sp)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    damage = random.randint(20, 30) + player_at - enemy_defense
    damage *= 1.2
    damage = int(damage)
    enemy_hp -= damage
    if enemy_hp > 0:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        bot.send_message(message.chat.id, f"Вы нанесли {damage} урона! (Враг: {enemy_hp} ХП)")
        enemy_attack(message,1.2)
    elif enemy_hp <= 0 and enemy == "Князь Тьмы":
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        fullvictory(message)
    elif player_hp <= 0:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        defeat(message)
    else:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        victory(message)

@bot.message_handler(commands=['defend'])
def defend(message):
    global player_hp, enemy_hp, player_at, enemy
    user_id = message.chat.id
    sp = users.get(user_id)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    damage = random.randint(20, 30) + player_at - enemy_defense
    damage *= 0.2
    damage = int(damage)
    enemy_hp -= damage
    if enemy_hp > 0:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        bot.send_message(message.chat.id, f"Вы нанесли {damage} урона! (Враг: {enemy_hp} ХП)")
        enemy_attack(message,0.2)
    elif enemy_hp <= 0 and enemy == "Князь Тьмы":
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        fullvictory(message)
    elif player_hp <= 0:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        defeat(message)
    else:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        victory(message)

def enemy_attack(message,a):
    global player_hp, enemy_hp, player_pr, enemy, enemy_at
    user_id = message.chat.id
    sp = users.get(user_id)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    damage = random.randint(5, 15) - player_pr
    damage *= a
    damage = int(damage)
    enemy_at = damage
    player_hp -= enemy_at
    if player_hp > 0:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Обычная атака', callback_data='attack'))
        keyboard.add(types.InlineKeyboardButton(text='Сильная атака', callback_data='strong_attack'))
        keyboard.add(types.InlineKeyboardButton(text='Защита', callback_data='defend'))
        bot.send_message(message.chat.id, f"Ваш враг: {enemy} (ХП: {enemy_hp})")
        bot.send_message(message.chat.id, f"Враг нанес вам {damage} урона! (Ваше ХП: {player_hp})")
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)
    else:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        defeat(message)
def defeat(message):
    bot.send_message(message.chat.id, "Вы погибли.")
    fullvictory(message)
def victory(message):
    bot.send_message(message.chat.id, f"Победа! Враг повержен!")
    if fvic:
        fullvictory(message)
    else:
        check_event_count(message)

def fullvictory(message):
    bot.send_message(message.chat.id, f"Игра окончена!")

def check_event_count(message):
    global event_count
    user_id = message.chat.id
    sp = users.get(user_id)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    event_count += 1
    if event_count == 8:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        boss_battle(message)
    else:
        sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
        users[user_id] = sp
        bot.send_message(message.chat.id, "Вы прошли этот уровень! Для следующего события /start_next_event")


@bot.message_handler(commands=['start_next_event'])
def start_next_event(message):
    nextevent = random.randint(1,8)
    if nextevent >= 5:
        tavern(message)
    else:
        battle(message)
@bot.message_handler(commands=['tavern'])
def tavern(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Зелье здоровья', callback_data='zelhealth'))
    keyboard.add(types.InlineKeyboardButton(text='Зелье силы', callback_data='zelyron'))
    keyboard.add(types.InlineKeyboardButton(text='Зелье защиты', callback_data='zelprotect'))
    bot.send_message(message.chat.id, "Вы заходите в таверну и продавец предлагает выбрать зелье на выбор", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'attack':
        attack(call.message)
    elif call.data == 'strong_attack':
        strong_attack(call.message)
    elif call.data == 'defend':
        defend(call.message)
    elif call.data == 'zelhealth':
        zelhealth(call.message)
    elif call.data == 'zelyron':
        zelyron(call.message)
    elif call.data == 'zelprotect':
        zelprotect(call.message)
@bot.message_handler(commands=['zelhealth'])
def zelhealth(message):
    global player_hp
    user_id = message.chat.id
    sp = users.get(user_id)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    player_hp += 80
    bot.send_message(message.chat.id, "Вы выпеваете это зелье и чуствуете себя как никогда лучше")
    sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
    users[user_id] = sp
    start_next_event(message)

@bot.message_handler(commands=['zelyron'])
def zelyron(message):
    global player_at
    user_id = message.chat.id
    sp = users.get(user_id)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    player_at += 5
    bot.send_message(message.chat.id, "Вы выпеваете это зелье и чуствуете себя как никогда лучше")
    sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
    users[user_id] = sp
    start_next_event(message)

@bot.message_handler(commands=['zelprotect'])
def zelprotect(message):
    global player_pr
    user_id = message.chat.id
    sp = users.get(user_id)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    player_pr += 2
    bot.send_message(message.chat.id, "Вы выпеваете это зелье и чуствуете себя как никогда лучше")
    sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
    users[user_id] = sp
    start_next_event(message)
def boss_battle(message):
    global player_hp, enemy_hp, enemy
    user_id = message.chat.id
    sp = users.get(user_id)
    player_hp = sp[0]
    player_pr = sp[1]
    enemy = sp[2]
    enemy_hp = sp[3]
    event_count = sp[4]
    fvic = sp[5]
    player_at = sp[6]
    enemy = "Князь Тьмы"
    enemy_hp = 150
    sp = [player_hp, player_pr, enemy, enemy_hp, event_count, fvic, player_at]
    users[user_id] = sp
    bot.send_message(message.chat.id, "После 8 событий наступает битва с Князем Тьмы!")
    bot.send_message(message.chat.id, "Готовы ли вы сразиться с боссом?")
    bot.send_message(message.chat.id, "Введите /attack, чтобы атаковать!")

@bot.message_handler(func=lambda message: True)
def handle_all_other_messages(message):
    bot.send_message(message.chat.id, "Извините, я не понимаю вашу команду.")
bot.polling()