import random

cand = 0
bot_action = True


def bot_logic(num):
    if num % 5 == 0:
        return 1
    else:
        return num % 5


def init_candy(message):
    global cand, bot_action
    cand = random.randint(20, 30)
    bot_action = random.choice([True, False])
    mess = f'Конфет на столе <b>{cand}</b>\n'
    mess += 'Можно взять до <b>4</b> шт\n'
    mess += 'Первый ход '
    if bot_action:
        mess += 'Бота\n'
        get_candies = bot_logic(cand)
        cand -= get_candies
        mess += f'Бот взял <b>{get_candies}</b> конфет\n'
        mess += f'Конфет на столе <b>{cand}</b>\n'
        mess += 'Можно взять до <b>4</b> шт\n'
        mess += f'Ваш ход {message.from_user.first_name}'
    else:
        mess += str(message.from_user.first_name)
    return mess


def input_candies(message):
    global cand
    if message.text in '1234' and int(message.text) <= cand:
        get_candies = int(message.text)
        cand -= get_candies
        mess = f'{message.from_user.first_name} взял <b>{get_candies}</b> конфет\n'
        if cand <= 0:
            mess += f'{message.from_user.first_name}, <u>Победа!</u>'
            return mess
        else:
            get_candies = bot_logic(cand)
            cand -= get_candies
            mess += f'Бот взял <b>{get_candies}</b> конфет\n'
            if cand == 0:
                mess += '<u>Бот победил</u>'
            else:
                mess += f'Конфет на столе <b>{cand}</b>\n'
                mess += 'Можно взять до '
                if cand >= 4:
                    mess += '<b>4</b> шт\n'
                else:
                    mess += f'<b>{cand}</b> шт.'
            return mess
    else:
        return 'Неверный ввод'
