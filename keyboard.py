from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

help_but = KeyboardButton('/help')
ruls_but = KeyboardButton('/rules')
start_but = KeyboardButton('start')

keyboard_menu.add(help_but, ruls_but, start_but)