from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from src.data.db import update_screenshots_count
from src.handlers.default import get_short_name, fake
from src.keyboards.markup import check6_inline, checks_inline
from src.loader import dp, bot
from src.states.form import DrawBol2
from src.utils.misc import oxxo_pay_screen, draw_bol1, draw_bol1_notify, draw_bol2


@dp.callback_query_handler(lambda c: c.data == 'draw_bol3')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"🔘 Введите сумму в формате `1.800,00`")
    await DrawBol2.amount.set()


@dp.message_handler(state=DrawBol2.amount)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = message.text
    await message.answer(f"🔘 Введите имя получателя в формате  `ADRIANA CAROLINA RENGIFO TORREALBA`")
    await DrawBol2.getter.set()


@dp.message_handler(state=DrawBol2.getter)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['getter'] = message.text
    await message.answer("🔘 Введите cuenta в формате `0108 1896`")
    await DrawBol2.pin.set()


@dp.message_handler(state=DrawBol2.pin)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['pin'] = message.text
    await message.answer("🔘 Введите дату в формате `31/07/2024`")
    await DrawBol2.date.set()


@dp.message_handler(state=DrawBol2.date)
async def process_money_check1(message: Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['date'] = message.text
        img = draw_bol2(data["amount"], data["getter"], data["pin"], data["date"])

        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()
