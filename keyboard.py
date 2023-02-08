from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# plus_but = KeyboardButton('/sumary')
# minus_but = KeyboardButton('/difference')
# multi_but = KeyboardButton('/multiply')
# div_but = KeyboardButton('/quotient')
#
#
# keyboard_menu.add(plus_but, minus_but, multi_but, div_but)

start_but = KeyboardButton('/start')
# help_but = KeyboardButton('/help')
sumary_but = KeyboardButton('/sumary')



keyboard_menu.add(sumary_but, start_but)