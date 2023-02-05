import random
from aiogram.dispatcher.filters import Text
from create import dp
from aiogram import types
from keyboard import keyboard_menu
import emoji
from random import randint

from aiogram.dispatcher.filters import Text


total = 100
candy = 17
level = 1

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'привет тебе {message.from_user.first_name} мы будем играть в конфеты, по умолчанию на столе 100 конфет, можно взять не болье 17 за раз напиши /help', reply_markup=keyboard_menu)

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer(f'/rules - правила игры\n/set - выбарть общее количество конфет\n/candy - сколько можно брать конфет\n/level - выбрать уровень\n если ничего не хочешт менять - выбери сколько конфет возьмешь\n после внесенных изменений тоже выбери сколько конфет возьмешь')


@dp.message_handler(commands=['rules'])
async def mes_rules(message: types.Message):
    global total
    global candy
    await message.answer(f'На столе лежат {total} конфет ты можешь взять {candy} конфет, выиграет тот кто заберет последние конфеты')


# @dp.message_handler(commands=['level'])
# async def mes_level(message: types.Message):
#     global level
#     count = int(message.text.split()[1])
#     level = count
#     await message.answer(emoji.emojize(f'Теперь уровень сложнее :OK_hand:',language='alias'))

@dp.message_handler(commands=['level'])
async def mes_level(message: types.Message):
    global total
    global candy
    global level
    count = int(message.text.split()[1])
    level = count
    if level == 2:
        bot_step = total//(candy+1)
        total -= bot_step
    await message.answer(emoji.emojize(f'Теперь уровень сложнее :OK_hand:, я беру {bot_step}:candy:, в игре осталось {total} :candy:', language='alias'))
    # else:
    # await message.answer(emoji.emojize(f'Теперь уровень сложнее :OK_hand:', language='alias'))



@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(emoji.emojize(f'Теперь в игре :candy: {total}', language='alias'))

@dp.message_handler(commands=['candy'])
async def mes_fig(message: types.Message):
    global candy
    # await message.answer('по сколько конфет будем брать?')
    count = int(message.text.split()[1])
    candy = count
    await message.answer(emoji.emojize(f'будем брать по {candy} :candy:', language='alias'))


@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    global candy
    global level
    text = message.text
    if level == 1:
        text = int(text)
        # if text.isdigit():
        # if level == 1:
        if 0 < text <= candy:
            # total -= int(text)
            total -= text
            if total == 0:
                await message.answer(emoji.emojize(f':candy: не осталось, ты выиграл :1st_place_medal:', language='alias'))
                total = 100
                candy = 17
                level = 1
            elif total > candy:
                # total -= text
                await message.answer(emoji.emojize(f'{message.from_user.first_name} ты взял {text} :candy: осталось {total} :candy:', language='alias'))
                bot_step = random.randint(1, candy)
                total -= bot_step
                await message.answer(emoji.emojize(f'{message.from_user.first_name} я взял {bot_step} :candy: в игре осталось {total} :candy:', language='alias'))
            elif total < candy and total > 0:
                bot_step = total
                await message.answer(emoji.emojize(f'Я беру {bot_step} :candy: Ура я выиграл :1rst_place_medal:', language='alias'))
                total = 100
                candy = 17
                level = 1
        else:
            await message.answer(f'сам же выбрал максимально {candy}')
    elif level == 2:
        total -= int(text)
        # bot_step = total//(candy+1)
        # total -= bot_step
        # await message.answer(emoji.emojize(f'Я беру {bot_step} :candy: в игре осталось {total} :candy:', language='alias'))
        if total == 0:
            await message.answer(emoji.emojize(f'Я беру {bot_step} :candy: Ура я выиграл :1rst_place_medal:', language='alias'))
            total = 100
            candy = 17
            level = 1
        if total > candy:
            if 0 < int(text) <= candy:
                # total -= int(text)
                await message.answer(emoji.emojize(f'Ты взял {text} :candy: в игре осталось {total} :candy:', language='alias'))
                bot_step = (candy+1)-int(text)
                total -= bot_step
                await message.answer(emoji.emojize(f'Я беру {bot_step} :candy: в игре осталось {total} :candy:', language='alias'))
        elif total < candy and total > 0:
            await message.answer(emoji.emojize(f'Ты взял {text} :candy: в игре осталось {total} :candy:', language='alias'))

            bot_step = total
            await message.answer(emoji.emojize(f'Я беру {bot_step} :candy: Ура я выиграл :1rst_place_medal:', language='alias'))
            total = 100
            candy = 17
            level = 1