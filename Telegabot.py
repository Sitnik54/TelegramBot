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
    answer = random.randint(0, 19)
    messages = [
        'Бесспорно' + smiles[0],
        'Предрешено' + smiles[1],
        'Никаких сомнений' + smiles[2],
        'Определённо да' + smiles[3],
        'Можешь быть уверен в этом' + smiles[4],
        'Мне кажется — «да»' + smiles[5],
        'Вероятнее всего' + smiles[6], 
        'Хорошие перспективы' + smiles[7],
        'Знаки говорят — «да»' + smiles[8], 
        'Да' + smiles[9],
        'Пока не ясно, попробуй снова' + smiles[10],
        'Спроси позже' + smiles[11],
        'Лучше не рассказывать' + smiles[12],
        'Сейчас нельзя предсказать' + smiles[13],
        'Сконцентрируйся и спроси опять' + smiles[14],
        'Даже не думай' + smiles[15],
        'Мой ответ — «нет»' + smiles[16],
        'По моим данным — «нет»' + smiles[17],
        'Перспективы не очень хорошие' + smiles[18],
        'Весьма сомнительно' + smiles[19]   
    ]
    bot.send_message(message.chat.id, messages[answer])

@bot.message_handler(func=lambda message: True)
def somemes(message: Message):
    bot.send_message(message.chat.id, 'Чтобы получить ответ, выберите команду /shaketheball ' + smiles[20])

bot.polling()
