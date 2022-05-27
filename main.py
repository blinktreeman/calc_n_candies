# make settings.py file with string:
# BOT_TOKEN = 'your bot token'

import settings
import math_part
import candies
import telebot

bot = telebot.TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['help'])
def help(message):
    mess = 'Для работы с калькулятором введите <b>/calc "выражение"</b>\n'
    mess += 'Для игры в конфеты <b>/candy</b>\n'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['calc'])
def calc(message):
    bot.send_message(message.chat.id, math_part.calc(message), parse_mode='html')


@bot.message_handler(commands=['candy'])
def init_candy(message):
    bot.send_message(message.chat.id, candies.init_candy(), parse_mode='html')


@bot.message_handler()
def input_candy(message):
    bot.send_message(message.chat.id, candies.input_candies(message), parse_mode='html')


bot.polling(none_stop=True)
