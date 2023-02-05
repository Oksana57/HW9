from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

book_but = KeyboardButton('/book')
del_but = KeyboardButton('/del')
find_but = KeyboardButton('/find')
new_but = KeyboardButton('/new')


keyboard_menu.add(book_but, del_but, find_but, new_but)