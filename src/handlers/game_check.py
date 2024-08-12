from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from src.data.db import update_screenshots_count
from src.keyboards.markup import empty_data_game_check, game_check_go, one_more_check_bol, null_message
from src.loader import dp, bot
from src.states.form import GameCheckStates
from src.utils.misc import comprobante_check, new_check_for_boli, win_game_check


@dp.callback_query_handler(lambda c: c.data.startswith('check_game'))
async def screen_rendering_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(lang=callback_query.data.split(":")[1])
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=game_check_go())


@dp.callback_query_handler(lambda c: c.data == 'game_check_go')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"*🔘 Введите дату в формате* `13 de juilo 10:24`", reply_markup=empty_data_game_check())
    await GameCheckStates.date.set()


@dp.callback_query_handler(lambda c: c.data == "empty_date", state=GameCheckStates.date)
async def proccess_empty_date(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["date"] = ""
    await call.message.answer(f"*🔘 Введите сумму в формате* `1,500.00`")
    await GameCheckStates.win_money.set()


@dp.message_handler(state=GameCheckStates.date)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer(f"*🔘 Введите сумму в формате* `1,500.00`")
    await GameCheckStates.win_money.set()



@dp.message_handler(state=GameCheckStates.win_money)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['win_money'] = message.text
    await message.answer("*🔘 Введите деньги на аккаунте в формате:* `30.000`")
    await GameCheckStates.account_money.set()


@dp.message_handler(state=GameCheckStates.account_money)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["account_money"] = message.text
    await message.answer("*🔘 Введите cuota в формате:* `30`")
    await GameCheckStates.cuota.set()


@dp.message_handler(state=GameCheckStates.cuota)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["cuota"] = message.text
    await message.answer("*🔘 Введите apuesta в формате:* `1.500`")
    await GameCheckStates.apuesta.set()


@dp.message_handler(state=GameCheckStates.apuesta)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["apuesta"] = message.text
        img = await win_game_check(data["date"], data["win_money"], data["account_money"], data["cuota"], data["apuesta"], data["lang"])
        await message.answer_photo(img)
        update_screenshots_count(message.from_user.id, 1)
        await state.finish()