import telebot
from telebot.types import Message
import random

TOKKEN = '714355239:AAFoyBVLNxf7rAVWDh79oP-_dXE0eDMh2Hk'
bot = telebot.TeleBot(TOKKEN)

smiles = ['👌', '😉', '😏', '😀', '😁',
        '🙃', '😎', '😉', '😇', '👌', 
        '😐', '😕', '😞', '😒', '😔',
        '😡', '😔', '☹️', '😱', '😢', '🎱']

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать! \nПотряси шар и узнай ответ на свой вопрос! /shaketheball ' + smiles[20])

@bot.message_handler(commands=['shaketheball'])
def question(message):
    answer = random.randint(1, 20)
    if answer == 1:
        bot.send_message(message.chat.id, 'Бесспорно' + smiles[0])
    if answer == 2:
        bot.send_message(message.chat.id, 'Предрешено' + smiles[1])
    if answer == 3:
        bot.send_message(message.chat.id, 'Никаких сомнений' + smiles[2])
    if answer == 4:
        bot.send_message(message.chat.id, 'Определённо да' + smiles[3])
    if answer == 5:
        bot.send_message(message.chat.id, 'Можешь быть уверен в этом' + smiles[4])
    if answer == 6:
        bot.send_message(message.chat.id, 'Мне кажется — «да»' + smiles[5])
    if answer == 7:
        bot.send_message(message.chat.id, 'Вероятнее всего' + smiles[6])
    if answer == 8:
        bot.send_message(message.chat.id, 'Хорошие перспективы' + smiles[7])
    if answer == 9:
        bot.send_message(message.chat.id, 'Знаки говорят — «да»' + smiles[8])
    if answer == 10:
        bot.send_message(message.chat.id, 'Да' + smiles[9])
    if answer == 11:
        bot.send_message(message.chat.id, 'Пока не ясно, попробуй снова' + smiles[10])
    if answer == 12:
        bot.send_message(message.chat.id, 'Спроси позже' + smiles[11])
    if answer == 13:
        bot.send_message(message.chat.id, 'Лучше не рассказывать' + smiles[12])
    if answer == 14:
        bot.send_message(message.chat.id, 'Сейчас нельзя предсказать' + smiles[13])
    if answer == 15:
        bot.send_message(message.chat.id, 'Сконцентрируйся и спроси опять' + smiles[14])
    if answer == 16:
        bot.send_message(message.chat.id, 'Даже не думай' + smiles[15])
    if answer == 17:
        bot.send_message(message.chat.id, 'Мой ответ — «нет»' + smiles[16])
    if answer == 18:
        bot.send_message(message.chat.id, 'По моим данным — «нет»' + smiles[17])
    if answer == 19:
        bot.send_message(message.chat.id, 'Перспективы не очень хорошие' + smiles[18])
    if answer == 20:
        bot.send_message(message.chat.id, 'Весьма сомнительно' + smiles[19])

@bot.message_handler(func=lambda message: True)
def somemes(message: Message):
    bot.send_message(message.chat.id, 'Чтобы получить ответ, выберите команду /shaketheball ' + smiles[20])

bot.polling()