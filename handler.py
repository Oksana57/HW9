
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
    botlogfile = open('Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f'привет тебе {message.from_user.first_name} поработаем с калькулятором\nнапиши /help', reply_markup=keyboard_menu)

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f'/sumary - сумма \n/difference - разность\n/multiply - произведения\n/quotient - частное', reply_markup=keyboard_menu)


@dp.message_handler(commands=['sumary'])
async def mes_sumary(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f'введите /sum и два числа через пробел')

@dp.message_handler(commands=['sum'])
async def mes_sum(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global result
    text = message.text.split()

    first_count = float(text[1])
    second_count = float(text[2])
    result = round((first_count + second_count), 2)
    await message.answer(f'Сумма равна {result}')

@dp.message_handler(commands=['difference'])
async def mes_difference(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f'введите /diff и два числа через пробел')

@dp.message_handler(commands=['diff'])
async def mes_diff(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global result
    text = message.text.split()
    first_count = float(text[1])
    second_count = float(text[2])
    result = round((first_count - second_count), 2)
    await message.answer(f'Разность равна {result}')

@dp.message_handler(commands=['multiply'])
async def mes_multiply(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f'введите /mult и два числа через пробел')

@dp.message_handler(commands=['mult'])
async def mes_mult(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Candies\Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global result
    text = message.text.split()
    first_count = float(text[1])
    second_count = float(text[2])
    result = round((first_count * second_count),2)
    await message.answer(f'Произедение равно {result}')

@dp.message_handler(commands=['quotient'])
async def mes_quotient(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    await message.answer(f'введите /quot и два числа через пробел')

@dp.message_handler(commands=['quot'])
async def mes_phone(message: types.Message):
    dtn = datetime.datetime.now()
    botlogfile = open('Candies\Botlogger.log', 'a', encoding='UTF-8')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id,'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global result
    text = message.text.split()
    first_count = float(text[1])
    second_count = float(text[2])
    result = round((first_count / second_count),2)
    await message.answer(f'Частное равнао {result}')




