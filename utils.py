from emoji import emojize 
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton
import Settings

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(Settings.USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']

def play_random_numbers(user_number):
    bot_number = randint(user_number -10, user_number +10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, моё число {bot_number}, вы выйграли!'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, моё число {bot_number}, ничья!'
    else:
        message = f'Ваше число {user_number}, моё число {bot_number}, вы проиграли!'
    return message  






def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать котика', KeyboardButton('Мои координаты', request_location=True)]])
