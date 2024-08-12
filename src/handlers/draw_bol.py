import random

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from src.data.db import update_screenshots_count
from src.handlers.default import get_short_name, fake
from src.keyboards.markup import check6_inline, checks_inline, random_keyboard
from src.loader import dp, bot
from src.states.form import DrawBol
from src.utils.misc import oxxo_pay_screen, draw_bol1, draw_bol1_notify


@dp.callback_query_handler(lambda c: c.data == 'draw_bol1')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["image"] = "bol1"
    await callback_query.message.answer(f"🔘 Введите сумму в формате `2.535,00`")
    await DrawBol.amount.set()


@dp.callback_query_handler(lambda c: c.data == 'draw_bol2')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["image"] = "bol2"
    await callback_query.message.answer(f"🔘 Введите сумму в формате `2.535,00`")
    await DrawBol.amount.set()


@dp.message_handler(state=DrawBol.amount)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = message.text
    await message.answer(f"🔘 Введите дату в формате `31/07/2024`")
    await DrawBol.date.set()


@dp.message_handler(state=DrawBol.date)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer("🔘 Введите id операции:", reply_markup=random_keyboard())
    await DrawBol.operation.set()


@dp.callback_query_handler(lambda c: c.data == "random_data", state=DrawBol.operation)
async def process_operation_check1(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['operation'] = str(random.randint(3700_0000_0000_0, 4900_0000_0000_0))
    await call.message.answer("🔘 Введите имя получателя")
    await DrawBol.getter.set()


@dp.message_handler(state=DrawBol.operation)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['operation'] = message.text
    await message.answer("🔘 Введите имя получателя")
    await DrawBol.getter.set()


@dp.message_handler(state=DrawBol.getter)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['getter'] = message.text
    await message.answer("🔘 Введите origen в формате `0102****9313`:", reply_markup=random_keyboard())
    await DrawBol.origen.set()


@dp.callback_query_handler(lambda c: c.data == "random_data", state=DrawBol.origen)
async def random_origen(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['origen'] = f"{random.randint(1000, 9999)}****{random.randint(1000, 9999)}"
    await callback_query.message.answer("🔘 Введите destino в формате `0108****1896`:", reply_markup=random_keyboard())
    await DrawBol.destino.set()


@dp.message_handler(state=DrawBol.origen)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['origen'] = message.text
    await message.answer("🔘 Введите destino в формате `0108****1896`:", reply_markup=random_keyboard())
    await DrawBol.destino.set()


@dp.callback_query_handler(lambda c: c.data == "random_data", state=DrawBol.destino)
async def random_origen(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['destino'] = f"{random.randint(1000, 9999)}****{random.randint(1000, 9999)}"
    await callback_query.message.answer("🔘 Введите банк")
    await DrawBol.bank.set()


@dp.message_handler(state=DrawBol.destino)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['destino'] = message.text
    await message.answer("🔘 Введите банк")
    await DrawBol.bank.set()


@dp.message_handler(state=DrawBol.bank)
async def process_date_check1(message: Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['bank'] = message.text
        if data["image"] == "bol1":
            img = draw_bol1(data['amount'], data['date'], data['operation'], data["getter"], data["origen"], data["destino"], data["bank"])
        else:
            img = draw_bol1_notify(data['amount'], data['date'], data['operation'], data["getter"], data["origen"], data["destino"], data["bank"])
        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()
