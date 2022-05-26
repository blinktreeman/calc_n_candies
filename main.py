import settings
import telebot
import random

bot = telebot.TeleBot(settings.BOT_TOKEN)

@bot.message_handler(commands=['help'])
def help(message):
    mess = '<u>Для работы с калькулятором введите /calc "выражение"</u>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['calc'])
def calc(message):
    args = message.text.split()
    arg = ''
    if len(args) > 1:
        arg = ''.join(args[1:])
    result = eval(arg)
    mess = result
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['candy'])
def candy(message):
    candies = random.randint(20, 30)
    #print(candies)
    while candies > 0:
        mess = f'Конфет на столе {candies}\n'
        mess += 'Можно взять до 4 шт\n'
        bot.send_message(message.chat.id, mess, parse_mode='html')

        @bot.message_handler()
        def input_candy(message):
            input()
            get_candies = int(message.text)
            print(get_candies)
    #candies

bot.polling(none_stop=True)
