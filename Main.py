import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from Amplitude.send_events import send_event
from database.database_connection import Session
from database.characters_operation import add_new_character_to_user
from database.user_operation import add_new_user
from database.greetings_operation import get_greeting_by_character_name
from database.user_api_operations import save_request_response
from database.characters_operation import character_exists


MENU = 'Если не понравился прошлый персонаж, выбери нового!)'

TOKEN = os.environ["TOKEN"]
URL = os.environ["URL"]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_web_app = types.KeyboardButton('Выбор персонажа', web_app=WebAppInfo(url=URL))
    keyboard.add(button_web_app)

    response = add_new_user(message, Session())

    await message.answer(response, reply_markup=keyboard)


@dp.message_handler(commands=['menu'])
async def on_menu(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_web_app = types.KeyboardButton('Выбор персонажа', web_app=WebAppInfo(url=URL))
    keyboard.add(button_web_app)

    await message.answer(MENU, reply_markup=keyboard)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    character_name = message.web_app_data.data
    character_name = character_name.replace('\n', '')
    character_name = character_name.split('Вы выбрали персонажа:')
    character_name = character_name[1].strip()

    await message.answer(f"Вы выбрали персонажа: {character_name}")

    add_new_character_to_user(message, character_name, Session())

    character_greeting = get_greeting_by_character_name(character_name, Session())

    await message.answer(character_greeting)


@dp.message_handler(content_types=['text'])
async def on_text_message(message: types.Message):

    user_id = message.from_user.id

    user_input_request = message.text
    if not character_exists(user_id, Session()):
        await message.answer('Сначал выберите персонажа!')
    else:
        response = save_request_response(user_input_request, Session(), user_id)

        await message.answer(response)

        data = [{
                "event_type": "response delivered",
                "user_id": user_id,
                "delivered": 'Yes!'
                }]
        send_event(data)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)
