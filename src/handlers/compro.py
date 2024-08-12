from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from src.data.db import update_screenshots_count
from src.keyboards.markup import one_more_check_bol, null_message
from src.loader import dp, bot
from src.states.form import ComproStates
from src.utils.misc import comprobante_check, new_check_for_boli


@dp.callback_query_handler(lambda c: c.data == 'one_more_check_bol')
async def screen_rendering_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(last_country='new_check_bol')
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=one_more_check_bol())


@dp.callback_query_handler(lambda c: c.data == 'one_more_check_bol_go')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(f"*🔘 Введите дату в формате* `15/07/2024 13:05`")
    await ComproStates.date.set()


@dp.message_handler(state=ComproStates.date)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer(f"*🔘 Введите сумму в формате* `1400.00`")
    await ComproStates.money.set()



@dp.message_handler(state=ComproStates.money)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['money'] = message.text
    await message.answer("*🔘 Введите Имя получателя:*")
    await ComproStates.name_getter.set()


@dp.message_handler(state=ComproStates.name_getter)
async def process_money_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["name_getter"] = message.text
        img = await comprobante_check(data["date"], data["money"], data["name_getter"])
        await message.answer_photo(img)
        update_screenshots_count(message.from_user.id, 1)
        await state.finish()

