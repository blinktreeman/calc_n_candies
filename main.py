import settings
import math_part
import telebot
import random

candies = 0

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
def candy(message):
    global candies
    candies = random.randint(20, 30)
    mess = f'Конфет на столе {candies}\n'
    mess += 'Можно взять до 4 шт\n'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler()
def input_candy(message):
    global candies
    if message.text in '1234' and candies != 0:
        get_candies = int(message.text)
        candies -= get_candies
        if candies <= 0:
            mess = '<u>Победа!</u>'
            bot.send_message(message.chat.id, mess, parse_mode='html')
        else:
            mess = f'Конфет на столе {candies}\n'
            mess += 'Можно взять до '
            if candies >= 4:
                mess += '4 шт\n'
            else:
                mess += f'{candies} шт.'
            bot.send_message(message.chat.id, mess, parse_mode='html')

    #print(get_candies)
    #print(candies)


bot.polling(none_stop=True)
