from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from src.data.db import update_screenshots_count
from src.keyboards.markup import new_check_bol, null_message
from src.loader import dp, bot
from src.states.form import NewCheckBol
from src.utils.misc import new_check_for_boli


@dp.callback_query_handler(lambda c: c.data == 'new_check_bol')
async def screen_rendering_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(last_country='new_check_bol')
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=new_check_bol())


@dp.callback_query_handler(lambda c: c.data == 'new_check_bol_go')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"*🔘 Введите дату в формате* `14 jul 2024 - 6:14 p. m.`")
    await NewCheckBol.date.set()


@dp.message_handler(state=NewCheckBol.date)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer(f"*🔘 Введите сумму в формате* `1400.00`")
    await NewCheckBol.money.set()



@dp.message_handler(state=NewCheckBol.money)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['money'] = message.text
    await message.answer("*🔘 Имя получателя:*")
    await NewCheckBol.name_getter.set()


@dp.message_handler(state=NewCheckBol.name_getter)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["name_getter"] = message.text

        await message.answer(f"*🔘 Введите карту получателя*")
        await NewCheckBol.card_getter.set()


@dp.message_handler(state=NewCheckBol.card_getter)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["card_getter"] = message.text

        await message.answer(f"*🔘 Введите имя отправителя*")
        await NewCheckBol.name_sender.set()


@dp.message_handler(state=NewCheckBol.name_sender)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["name_sender"] = message.text

        await message.answer(f"*🔘 Введите сообщение*", reply_markup=null_message())
        await NewCheckBol.message.set()


@dp.callback_query_handler(lambda call: call.data == "message_is_null", state=NewCheckBol.message)
async def proccess_message(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data["message"] = " "
        img = await new_check_for_boli(data["date"], data["money"], data["name_getter"], data["card_getter"], data["name_sender"], data["message"])
        await call.message.answer_photo(img)
        update_screenshots_count(call.message.chat.id, 1)
        await state.finish()

@dp.message_handler(state=NewCheckBol.message)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["message"] = message.text
        img = await new_check_for_boli(data["date"], data["money"], data["name_getter"], data["card_getter"], data["name_sender"], data["message"])
        await message.answer_photo(img)
        update_screenshots_count(message.from_user.id, 1)
        await state.finish()
