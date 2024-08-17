from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from src.data.db import update_screenshots_count
from src.loader import dp
from src.states.form import DrawBol4, DrawBol5, DrawBol6
from src.utils.misc import draw_bol4, draw_bol5, draw_bol6


@dp.callback_query_handler(lambda c: c.data == 'draw_bol4')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"🔘 Введите имя клиента")
    await DrawBol4.client_name.set()


@dp.message_handler(state=DrawBol4.client_name)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer(f"🔘 Введите сумму к оплате в формате `16 400`")
    await DrawBol4.amount1.set()


@dp.message_handler(state=DrawBol4.amount1)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount1'] = message.text
    await message.answer("🔘 Введите введите сумму прибыли в формате `4 958`")
    await DrawBol4.amount2.set()


@dp.message_handler(state=DrawBol4.amount2)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount2'] = message.text
    await message.answer("🔘 Введите счёт клиента")
    await DrawBol4.card.set()


@dp.message_handler(state=DrawBol4.card)
async def process_money_check1(message: Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['card'] = message.text
        img = draw_bol4(data["name"], data["amount1"], data["amount2"], data["card"])

        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'draw_bol5')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"🔘 Введите счёт клиента")
    await DrawBol5.card.set()


@dp.message_handler(state=DrawBol5.card)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['card'] = message.text
    await message.answer(f"🔘 Введите банк клиента")
    await DrawBol5.bank.set()


@dp.message_handler(state=DrawBol5.bank)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['bank'] = message.text
    await message.answer("🔘 Введите сумму платежа в формате `24 000`")
    await DrawBol5.amount1.set()


@dp.message_handler(state=DrawBol5.amount1)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount1'] = message.text
    await message.answer("🔘 Введите сумму прибыли в формате `5 362`")
    await DrawBol5.amount2.set()


@dp.message_handler(state=DrawBol5.amount2)
async def process_money_check1(message: Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['amount2'] = message.text
        img = draw_bol5(data["card"], data["bank"], data["amount1"], data["amount2"])

        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'draw_bol6')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"🔘 Введите пару в формате `ESC_USDT`")
    await DrawBol6.pair.set()


@dp.message_handler(state=DrawBol6.pair)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['pair'] = message.text
    await message.answer(f"🔘 Введите сумму в формате `45643.10`")
    await DrawBol6.amount.set()


@dp.message_handler(state=DrawBol6.amount)
async def process_time_check1(message: Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        data['amount'] = message.text
        img = draw_bol6(data["pair"], data["amount"])

        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()
