import random
import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from src.data.db import update_screenshots_count
from src.handlers.default import get_short_name, fake
from src.keyboards.markup import check6_inline, checks_inline
from src.loader import dp, bot
from src.states.form import Notification3, Checks
from src.utils.misc import create_notification3, oxxo_pay_screen
from src.utils.timess import mexico_time2, mexico_date2


@dp.callback_query_handler(lambda c: c.data.startswith("checks"))
async def screen_rendering_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(image_name=callback_query.data.split(":")[1])
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=checks_inline())


@dp.callback_query_handler(lambda c: c.data == 'c_go')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"🔘 Введите номер карты")
    await Checks.card.set()


@dp.message_handler(state=Checks.card)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['card'] = message.text
    await message.answer(f"🔘 Введите ФИО")
    await Checks.fio.set()


@dp.message_handler(state=Checks.fio)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['fio'] = message.text
    await message.answer("🔘 Введите сумму пополнения:")
    await Checks.money.set()


@dp.message_handler(state=Checks.money)
async def process_money_check1(message: Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['money'] = message.text

        img = await oxxo_pay_screen(data['card'], data['fio'], data['money'], data["image_name"])
        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()
