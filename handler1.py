
from aiogram import types
from keyboard import keyboard_menu
import emoji
from create import dp
import datetime
import csv
import sys
from aiogram.dispatcher.filters import Text
result = 0

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger1.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f'привет тебе {message.from_user.first_name} поработаем с калькулятором\nнапиши /sumary', reply_markup=keyboard_menu)

# @dp.message_handler(commands=['help'])
# async def mes_help(message: types.Message):
#     dtn = datetime.datetime.now()
#     botlogfile = open('Botlogger1.log', 'a', encoding='UTF-8')
#     print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
#     botlogfile.close()
#     await message.answer(f'/sumary - для вычисления выражения', reply_markup=keyboard_menu)


@dp.message_handler(commands=['sumary'])
async def mes_sumary(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger1.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f'ввеите /sum и выражение для вычисления через пробел')


@dp.message_handler(commands=['sum'])
async def mes_calc(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger1.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global result
    res1 = 1
    text = message.text.split()
    text = list(text)
    while '*' in text or '/' in text:
        for i in range(0, len(text) - 1):
            if text[i] == '*':
                res1 = float(text.pop(i + 1)) * float(text.pop(i - 1))
                text[i - 1] = res1
            elif text[i] == '/':
                res1 = float(text.pop(i - 1)) / float(text.pop(i))
                text[i - 1] = res1

    while '+' in text or '-' in text:
        for i in range(0, len(text) - 1):
            if text[i] == '-':
                res1 = float(text.pop(i - 1)) - float(text.pop(i))
                text[i - 1] = res1

            elif text[i] == '+':
                res1 = float(text.pop(i + 1)) + float(text.pop(i - 1))
                text[i - 1] = res1

    await message.answer(f'Результат равен {res1}')











