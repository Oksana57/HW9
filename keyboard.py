from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


start_but = KeyboardButton('/start')

sumary_but = KeyboardButton('/sumary')



keyboard_menu.add(sumary_but, start_but)