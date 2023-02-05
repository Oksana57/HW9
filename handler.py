
from aiogram import types
from keyboard import keyboard_menu
import emoji
from create import dp
import csv
import sys
from aiogram.dispatcher.filters import Text
contact = []

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'привет тебе {message.from_user.first_name} заполним телефонный справочник\nнапиши /help', reply_markup=keyboard_menu)

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer(f'/new - заполнить\n/book - посмотреть\n/del - удалить\n/find - найти')



@dp.message_handler(commands=['new'])
async def mes_phone(message: types.Message):
    await message.answer(emoji.emojize(f'Введи /cont Введи через пробел Фамилию Имя :telephone: Коментарий к контакту', language='alias'))

@dp.message_handler(commands=['book'])
async def mes_one(message: types.Message):
    global contact
    with open('data.csv', 'r', encoding='UTF-8') as n_file:
        reader_object = csv.reader(n_file, delimiter="*")
        count = 0
        n = csv.field_size_limit(sys.maxsize)
        for row in reader_object:
            if count == 0:
                # alist = ' '.join(row).split()
                count += 1
                continue
            elif 0 < count < n:
                contact.append(row)
            count += 1
    # alist = ['name', 'surname', 'phone', 'info']
    # # print('|   ', ' | '.join(alist), '  |')
    # await message.answer('|   ', ' | '.join(alist), '  |')
    for i in range(0, len(contact)):
        for j in range(len(contact[i])):
            view1 = '--'.join(contact[i])
        # print('|', '|'.join(alist), '|')
        # print('|', view1, '|')
        await message.answer(f'| {view1} |')


@dp.message_handler(commands='del')
async def mes_del(message: types.Message):
    await message.answer(emoji.emojize(f'Введи /2 и номер :telephone: для удаления', language='alias'))

@dp.message_handler(commands=['2'])
async def mes_one(message: types.Message):
    global contact
    # number = await message.answer('Введите номер для удаления')
    text = message.text.split()
    number = text[1]
    #contact1 = []
    with open('data.csv', 'r', encoding='UTF-8') as file1:
        cont2 = csv.reader(file1, delimiter="*")
        count = 0
        n = csv.field_size_limit(sys.maxsize)
        for row in cont2:
            if count == 0:
                #     alist = ' '.join(row).split()
                count += 1
                continue
            if 0 < count < n:
                contact.append(row)
            count += 1
        n = len(contact)
        # print(contact)
        # contact2=[]
        for i in range(len(contact)):
            for j in range(len(contact[i])):
                if number == contact[i][j]:
                    break
        del contact[i]
    key1 = ['surname', 'name', 'phone', 'info']
    dict2 = {}
    book = []
    for i in range(len(contact)):
        dict2 = {key1[j]: contact[i][j] for j in range(len(key1))}
        book.append(dict2)
    names = ['surname', 'name', 'phone', 'info']
    # dict = book
    csv_file = 'data.csv'
    with open(csv_file, 'w', encoding='UTF-8') as file_c:
        writer = csv.DictWriter(file_c, fieldnames=names, delimiter="*")
        writer.writeheader()
        for item in book:
            writer.writerow(item)

@dp.message_handler(commands='find')
async def mes_find(message: types.Message):
    await message.answer(emoji.emojize(f'Введи /2 и номер :telephone: для поиска', language='alias'))


@dp.message_handler(commands=['3'])
async def mes_find(message: types.Message):
    global contact
    text = message.text.split()
    number = text[1]
    with open('data.csv', 'r', encoding='UTF-8') as file1:
        cont2 = csv.reader(file1, delimiter="*")
        count = 0
        n = csv.field_size_limit(sys.maxsize)
        for row in cont2:
            if count == 0:
                count += 1
                continue
            if 0 < count < n:
                contact.append(row)
            count += 1
        for i in range(len(contact)):
            for j in range(len(contact[i])):
                if number == contact[i][j]:
                    print(contact[i])
                    await message.answer(f'Это {contact[i]}')
                    break


@dp.message_handler(commands=['cont'])
async def mes_input(message: types.Message):
    # await message.answer(f'Введи через пробел Фамилию Имя Телефон Коментарий к контакту')
    text = []
    book = []
    global contact
    text = message.text.split()
    c_surname = text[1]
    c_name = text[2]
    c_phone = text[3]
    c_info = text[4]
    key1 = ['surname', 'name', 'phone', 'info']
    contact = [c_surname, c_name, c_phone, c_info]
    dict1 = {key1[j]: contact[j] for j in range(len(key1))}
    book.append(dict1)
    with open('data.csv', 'r', encoding='UTF-8') as file1:
        cont2 = csv.reader(file1, delimiter="*")
        count = 0
        text = []
        n = csv.field_size_limit(sys.maxsize)
        for row in cont2:
            if count == 0:
                count += 1
                continue
            if 0 < count < n:
                text.append(row)
            count += 1
        # print(text)
    for i in range(len(text)):
        dict2 = {key1[j]: text[i][j] for j in range(len(key1))}
        book.append(dict2)
    names = ['surname', 'name', 'phone', 'info']
    csv_file = 'data.csv'
    with open(csv_file, 'w', encoding='UTF-8') as file_c:
        writer = csv.DictWriter(file_c, fieldnames=names, delimiter="*")
        writer.writeheader()
        for item in book:
            writer.writerow(item)




