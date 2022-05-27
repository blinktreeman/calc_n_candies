import random

cand = 0


def init_candy():
    global cand
    cand = random.randint(20, 30)
    mess = f'Конфет на столе {cand}\n'
    mess += 'Можно взять до 4 шт\n'
    return mess


def input_candies(message):
    global cand
    if message.text in '1234' and int(message.text) <= cand:
        get_candies = int(message.text)
        cand -= get_candies
        if cand <= 0:
            return '<u>Победа!</u>'
        else:
            mess = f'Конфет на столе {cand}\n'
            mess += 'Можно взять до '
            if cand >= 4:
                mess += '4 шт\n'
            else:
                mess += f'{cand} шт.'
            return mess
    else:
        return 'Неверный ввод'

