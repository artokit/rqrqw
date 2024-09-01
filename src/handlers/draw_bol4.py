from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from src.data.db import update_screenshots_count
from src.loader import dp
from src.states.form import DrawBol4, DrawBol5, DrawBol6, FinalChecks, NewCheck
from src.utils.misc import draw_bol4, draw_bol5, draw_bol6, draw_check1, draw_check2, draw_new_check


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


@dp.callback_query_handler(lambda c: c.data == 'draw_bol7')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"🔘 Введите счёт клиента в формате  `4405 4253 4053 3563`")
    await FinalChecks.card.set()


@dp.message_handler(state=FinalChecks.card)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['card'] = message.text
    await message.answer(f"🔘 Введите банк клиента")
    await FinalChecks.bank.set()


@dp.message_handler(state=FinalChecks.bank)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['bank'] = message.text
    await message.answer("🔘 Введите сумму платежа в формате `24000`")
    await FinalChecks.amount.set()


@dp.message_handler(state=FinalChecks.amount)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = message.text
        user_id = message.from_user.id
        img = draw_check1(data["card"], data["bank"], data["amount"])
        await message.answer_photo(img)
        img = draw_check2(data["card"], data["bank"], data["amount"])
        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'draw_bol8')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"🔘 Введите сумму в формате `4757.00`")
    await NewCheck.amount.set()


@dp.message_handler(state=NewCheck.amount)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = message.text
    await message.answer(f"🔘 Введите дату в формате `10 may.2024`")
    await NewCheck.date.set()


@dp.message_handler(state=NewCheck.date)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer("🔘 Введите имя в формате `Pablo Iglesias`")
    await NewCheck.name.set()


@dp.message_handler(state=NewCheck.name)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("🔘 Введите карту в формате `5686`")
    await NewCheck.card.set()


@dp.message_handler(state=NewCheck.card)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['card'] = message.text
        img = draw_new_check(data["amount"], data["date"], data["name"], data["card"])
        await message.answer_photo(img)
        await state.finish()
