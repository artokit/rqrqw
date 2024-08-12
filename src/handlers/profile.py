from datetime import datetime

from src.utils.timess import *
from aiogram import types
from src.loader import dp, bot
from src.data.db import get_user_info
from src.keyboards.markup import *


main_photo_url = 'https://imgur.com/a/t49MRL7'


@dp.message_handler(text='🌹 Профиль')
async def show_profile(message: types.Message):
    user_id = message.from_user.id
    user_info = get_user_info(user_id)
    if user_info:
        registration_date = datetime.strptime(user_info[1], '%Y-%m-%d %H:%M:%S.%f')
        duration = format_duration(registration_date)
        profile_info = (
            "*☘️ Ваш профиль:*\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
            f"*🍏 ID:* `{user_id}`\n"
            f"*🕰 Регистрация:* `{duration}`\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
            f"*🌴 Создано скриншотов:* `{user_info[2]}` шт."
        )
        await bot.send_photo(message.from_user.id, main_photo_url, profile_info, reply_markup=profile_inline())
    else:
        await bot.send_message(message.from_user.id, "Произошла ошибка при получении данных профиля.")


@dp.callback_query_handler(lambda c: c.data == 'profile')
async def show_profile(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user_info = get_user_info(user_id)
    if user_info:
        registration_date = datetime.strptime(user_info[1], '%Y-%m-%d %H:%M:%S.%f')
        duration = format_duration(registration_date)
        profile_info = (
            "*☘️ Ваш профиль:*\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
            f"*🍏 ID:* `{user_id}`\n"
            f"*🕰 Регистрация:* `{duration}`\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
            f"*🌴 Создано скриншотов:* `{user_info[2]}` шт."
        )
        await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                       message_id=callback_query.message.message_id,
                                       caption=profile_info,
                                       reply_markup=profile_inline())
    else:
        await bot.answer_callback_query(callback_query.id, "Произошла ошибка при получении данных профиля.", show_alert=True)

    await bot.answer_callback_query(callback_query.id)