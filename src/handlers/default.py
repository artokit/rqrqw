import random
from faker import Faker
from datetime import datetime

import pytz
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from src.states import *

from src.utils.misc import *
from src.data.db import *
from src.loader import dp, bot
from src.keyboards.markup import *
from src.states.form import *
from src.utils.timess import *

main_photo_url = 'https://imgur.com/a/t49MRL7'


@dp.message_handler(commands='start', state="*")
async def start_comm(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await ensure_user(user_id)
    await bot.send_message(message.from_user.id, '*✅ Бот готов к использованию.*', reply_markup=main_keyboard())
    await bot.send_photo(
        message.from_user.id,
        main_photo_url,
        '*Добро пожаловать в бота отрисовки!*\n\n*㊙️ Выберите действие:*', reply_markup=main_inline())
    await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'home')
async def start_comm(callback_query: types.CallbackQuery):
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*Добро пожаловать в бота отрисовки!*\n\n'
                                           '*㊙️ Выберите действие:*',
                                   reply_markup=main_inline())

    await bot.answer_callback_query(callback_query.id)


@dp.message_handler(text='㊙️ Отрисовать')
async def show_rendering(message: types.Message):
    await bot.send_photo(message.from_user.id, main_photo_url, caption='*㊙️ Выберите действие:*', reply_markup=checks())


@dp.message_handler(text='🀄️ Информация')
async def show_info(message: types.Message):
    total_drawings = get_total_drawings_count()
    text = f'*🔫 Сделано отрисовок - {total_drawings}*'
    await bot.send_message(message.from_user.id, text)


@dp.callback_query_handler(lambda c: c.data == 'rendering')
async def show_rendering(callback_query: types.CallbackQuery):
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=checks())

    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'rd')
async def show_rendering(callback_query: types.CallbackQuery):
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=rd_keyboard())

    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'all_checks')
async def show_rendering(callback_query: types.CallbackQuery):
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=all_checks_keyboard())

    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'all_in')
async def show_rendering(callback_query: types.CallbackQuery):
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=all_in_keyboard())

    await bot.answer_callback_query(callback_query.id)


@dp.callback_query_handler(lambda c: c.data == 'screen')
async def screen_rendering(callback_query: types.CallbackQuery):
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите чек:*',
                                   reply_markup=screen_inline())


@dp.callback_query_handler(lambda c: c.data == '1win')
async def screen_rendering(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(last_country='1win')
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=onewin_inline())


@dp.callback_query_handler(lambda c: c.data == 'reqs')
async def screen_rendering(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(last_country='reqs')
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=reqs_inline())


@dp.callback_query_handler(lambda c: c.data == 'onewin_go')
async def screen_rendering(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("*🔘 Укажите название банка:*")
    await Win.waiting_for_name.set()


@dp.message_handler(state=Win.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_time_mexica"))
    await message.answer(f"*🔘 Введите время в формате H:M [{mexico_time}]*", reply_markup=keyboard)
    await Win.waiting_for_time.set()


@dp.callback_query_handler(text="use_current_time_mexica", state=Win.waiting_for_time)
async def use_current_time_poland(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(time=mexico_time, date=mexico_date)
    await callback_query.message.answer("*🔘 Укажите карту:*")
    await Win.waiting_for_card.set()


@dp.message_handler(state=Win.waiting_for_time)
async def process_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    await message.answer("*🔘 Укажите карту:*")
    await Win.waiting_for_card.set()


@dp.message_handler(state=Win.waiting_for_card)
async def process_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['card'] = message.text
    await message.answer("*🔘 Укажите комиссию:*")
    await Win.waiting_for_comm.set()


@dp.message_handler(state=Win.waiting_for_comm)
async def process_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comm'] = message.text
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Оставить стандартным", callback_data="use_text"))
    await message.answer("*🔘 Укажите текст над синей плашкой:*", reply_markup=keyboard)
    await Win.waiting_for_text.set()


@dp.callback_query_handler(text="use_text", state=Win.waiting_for_text)
async def use_current_time_poland(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = 'La cuenta especificada se encuentra en el extranjero\nDebe pagar una tarifa de transferencia internacional del 5% del monto del retiro'
    await callback_query.message.answer("*🔘 Укажите сумму пополнения::*")
    await Win.waiting_for_money2.set()


@dp.message_handler(state=Win.waiting_for_text)
async def process_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await message.answer("*🔘 Укажите сумму пополнения:*")
    await Win.waiting_for_money2.set()


@dp.message_handler(state=Win.waiting_for_money2)
async def process_money(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if ',' in message.text or '.' in message.text:
            data['popoln'] = message.text
        else:
            data['popoln'] = message.text
        await message.answer("*🔘 Укажите баланс (Salto и Cuenta):*")
        await Win.waiting_for_money.set()


@dp.message_handler(state=Win.waiting_for_money)
async def process_money(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        if ',' in message.text or '.' in message.text:
            data['money'] = message.text
            data['money2'] = data['money']
        else:
            data['money'] = message.text
            data['money2'] = data['money']

        img = await create_win(data['time'], data['name'], data['card'], data['comm'], data['popoln'], data['money'], data['money2'], data['text'])
        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'check1')
async def screen_rendering_check1(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(last_country='check1')
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=check1_inline())


@dp.callback_query_handler(lambda c: c.data == 'check1_go')
async def screen_rendering_check1_go(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_time_mexica"))
    await callback_query.message.answer(f"*🔘 Введите время в формате H:M:S [{mexico_time2}]*", reply_markup=keyboard)
    await Check1.waiting_for_time.set()


@dp.callback_query_handler(text="use_current_time_mexica", state=Check1.waiting_for_time)
async def use_current_time_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(time=mexico_time2)
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_date_mexica"))
    await callback_query.message.answer(f"*🔘 Укажите дату в формате D/M/Y [{mexico_date2}]:*", reply_markup=keyboard)
    await Check1.waiting_for_date.set()


@dp.message_handler(state=Check1.waiting_for_time)
async def process_time_check1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_date_mexica"))
    await message.answer(f"*🔘 Введите дату в формате D/M/Y [{mexico_date2}]*", reply_markup=keyboard)
    await Check1.waiting_for_date.set()


@dp.callback_query_handler(text="use_current_date_mexica", state=Check1.waiting_for_date)
async def use_current_date_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(date=mexico_date2)
    await callback_query.message.answer("*🔘 Введите сумму пополнения в формате:* `25.000,00`:", parse_mode='MARKDOWN')
    await Check1.waiting_for_money.set()


@dp.message_handler(state=Check1.waiting_for_date)
async def process_date_check1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer("*🔘 Введите сумму пополнения:*")
    await Check1.waiting_for_money.set()

fake = Faker('es_MX')


def get_short_name(fake):
    while True:
        name = fake.name()
        if len(name.split()) == 2 and all(len(word) <= 12 for word in name.split()):
            return name


@dp.message_handler(state=Check1.waiting_for_money)
async def process_money_check1(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        if ',' in message.text or '.' in message.text:
            data['money'] = message.text
        else:
            data['money'] = message.text + ',00'

        money = data['money']
        last_comma_index = money.rfind(',')
        last_dot_index = money.rfind('.')

        if last_comma_index != -1:
            money = money[:last_comma_index] + '.' + money[last_comma_index + 1:]
        if last_dot_index != -1:
            parts = money.rsplit('.', 1)
            money2 = parts[0].replace('.', ',') + '.' + parts[1]
        else:
            money2 = money

        data['money2'] = money2
        random_digits = '{:04d}'.format(random.randint(0, 9999))
        random_name = get_short_name(fake)

        img = await create_check1(data['money'], data['time'], data['date'], data['money2'], random_digits, random_name)
        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == "check5")
async def start_process_check5(call: types.CallbackQuery, state: FSMContext):
    await Check5.waiting_sender_name.set()
    await call.message.answer("*🔘 Введите имя отправителя: *")


@dp.message_handler(state=Check5.waiting_sender_name)
async def get_sender_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["sender_name"] = message.text

    await Check5.waiting_date.set()
    await message.answer("*🔘 Введите дату в формате* `01/06/2024`: ")


@dp.message_handler(state=Check5.waiting_date)
async def get_sender_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["date"] = message.text

    await Check5.waiting_time.set()
    await message.answer("*🔘 Введите время: *")


@dp.message_handler(state=Check5.waiting_time)
async def get_sender_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["time"] = message.text

    await Check5.waiting_recipient_name.set()
    await message.answer("*🔘 Введите имя получателя: *")


@dp.message_handler(state=Check5.waiting_recipient_name)
async def get_sender_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["recipient_name"] = message.text

    await Check5.waiting_bank_name.set()
    await message.answer("*🔘 Введите имя банка: *")


@dp.message_handler(state=Check5.waiting_bank_name)
async def get_sender_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["bank_name"] = message.text

    await Check5.waiting_money.set()
    await message.answer("*🔘 Введите сумму  в формате* `14000`:")


@dp.message_handler(state=Check5.waiting_money)
async def final_check5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["money"] = message.text
    img = await create_bnb_screen(data['sender_name'], data['date'], data['time'], data['recipient_name'], data["bank_name"], data["money"])
    await message.answer_photo(img)
    update_screenshots_count(message.chat.id, 1)
    await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'check2')
async def screen_rendering_check1(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(last_country='check2')
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=check2_inline())


@dp.callback_query_handler(lambda c: c.data == 'check2_go')
async def screen_rendering_check1_go(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_time_mexica"))
    await callback_query.message.answer(f"*🔘 Введите время в формате H:M:S [{mexico_time2}]*", reply_markup=keyboard)
    await Check2.waiting_for_time.set()


@dp.callback_query_handler(text="use_current_time_mexica", state=Check2.waiting_for_time)
async def use_current_time_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(time=mexico_time2)
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_date_mexica"))
    await callback_query.message.answer(f"*🔘 Укажите дату в формате D/M/Y [{mexico_date2}]:*", reply_markup=keyboard)
    await Check2.waiting_for_date.set()


@dp.message_handler(state=Check2.waiting_for_time)
async def process_time_check1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_date_mexica"))
    await message.answer(f"*🔘 Введите дату в формате D/M/Y [{mexico_date2}]*", reply_markup=keyboard)
    await Check2.waiting_for_date.set()


@dp.callback_query_handler(text="use_current_date_mexica", state=Check2.waiting_for_date)
async def use_current_date_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(date=mexico_date2)
    await callback_query.message.answer("*🔘 Введите сумму пополнения:*")
    await Check2.waiting_for_money.set()


@dp.message_handler(state=Check2.waiting_for_date)
async def process_date_check1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer("*🔘 Введите сумму пополнения:*")
    await Check2.waiting_for_money.set()


@dp.message_handler(state=Check2.waiting_for_money)
async def process_money_check1(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        if ',' in message.text or '.' in message.text:
            data['money2'] = message.text
        else:
            data['money2'] = message.text + ',00'

        money = data['money2']
        last_comma_index = money.rfind(',')
        last_dot_index = money.rfind('.')

        if last_comma_index != -1:
            money = money[:last_comma_index] + '.' + money[last_comma_index + 1:]
        if last_dot_index != -1:
            parts = money.rsplit('.', 1)
            money2 = parts[0].replace('.', ',') + '.' + parts[1]
        else:
            money2 = money

        data['money2'] = money2
        random_digits = '{:04d}'.format(random.randint(0, 9999))
        random_name = get_short_name(fake)

        img = await create_check2(data['time'], data['date'], data['money2'], random_digits, random_name)
        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'check3')
async def screen_rendering_check1(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(last_country='check3')
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=check3_inline())


@dp.callback_query_handler(lambda c: c.data == 'check3_go')
async def screen_rendering_check1_go(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("*🔘 Введите время как в примере - * `4 junio 2024, 10:47:08`:", parse_mode='MARKDOWN')
    await Check3.waiting_for_time.set()


@dp.message_handler(state=Check3.waiting_for_time)
async def process_date_check1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    await message.answer("*🔘 Введите сумму пополнения:*")
    await Check3.waiting_for_money.set()


@dp.message_handler(state=Check3.waiting_for_money)
async def process_money_check3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['money'] = message.text
        data['money_fraction'] = '00'
        await message.answer('*🔘 Введите имя получателя:*')
        await Check3.waiting_for_name.set()


@dp.message_handler(state=Check3.waiting_for_name)
async def process_name_check3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await message.answer("*🔘 Введите имя отправителя:*")
    await Check3.waiting_for_sender_name.set()


@dp.message_handler(state=Check3.waiting_for_sender_name)
async def process_name_check3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["sender_name"] = message.text
    await message.answer("*🔘 Введите последнии 4 цифры карты отправителя:*")
    await Check3.waiting_for_sender_last_numbers.set()


@dp.message_handler(state=Check3.waiting_for_sender_last_numbers)
async def process_date_check1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_numbers'] = message.text
    await message.answer("*🔘 Введите последнии 4 цифры карты получателя:*")
    await Check3.waiting_for_random_digits.set()


@dp.message_handler(state=Check3.waiting_for_random_digits)
async def process_random_digits(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["random_digits"] = message.text
        img = await create_check3(data['time'], data['money'], data['money_fraction'], data['name'], data["random_digits"], data["sender_name"], data["last_numbers"])
        await message.answer_photo(img)
        update_screenshots_count(message.chat.id, 1)
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'check4')
async def screen_rendering_check1(callback_query: types.CallbackQuery, state: FSMContext):
    await state.update_data(last_country='check4')
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=check4_inline())


@dp.callback_query_handler(lambda c: c.data == 'check4_go')
async def screen_rendering_check1_go(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_time_mexica"))
    await callback_query.message.answer(f"*🔘 Введите время в формате H:M:S [{mexico_time2}]*", reply_markup=keyboard)
    await Check4.waiting_for_time.set()


@dp.callback_query_handler(text="use_current_time_mexica", state=Check4.waiting_for_time)
async def use_current_time_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(time=mexico_time2)
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_date_mexica"))
    await callback_query.message.answer(f"*🔘 Укажите дату в формате D/M/Y [{mexico_date2}]:*", reply_markup=keyboard)
    await Check4.waiting_for_date.set()


@dp.message_handler(state=Check4.waiting_for_time)
async def process_time_check1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_date_mexica"))
    await message.answer(f"*🔘 Введите дату в формате D/M/Y [{mexico_date2}]*", reply_markup=keyboard)
    await Check4.waiting_for_date.set()


@dp.callback_query_handler(text="use_current_date_mexica", state=Check4.waiting_for_date)
async def use_current_date_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(date=mexico_date2)
    await callback_query.message.answer("*🔘 Введите сумму пополнения в формате:* `25.000,00`:", parse_mode='MARKDOWN')
    await Check4.waiting_for_money.set()


@dp.message_handler(state=Check4.waiting_for_date)
async def process_date_check1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer("*🔘 Введите сумму пополнения:*")
    await Check4.waiting_for_money.set()


@dp.message_handler(state=Check4.waiting_for_money)
async def process_money_check1(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        if ',' in message.text or '.' in message.text:
            data['money'] = message.text
        else:
            data['money'] = message.text + ',00'

        money = data['money']
        last_comma_index = money.rfind(',')
        last_dot_index = money.rfind('.')

        if last_comma_index != -1:
            money = money[:last_comma_index] + '.' + money[last_comma_index + 1:]
        if last_dot_index != -1:
            parts = money.rsplit('.', 1)
            money2 = parts[0].replace('.', ',') + '.' + parts[1]
        else:
            money2 = money

        data['money2'] = money2
        random_digits = '{:04d}'.format(random.randint(0, 9999))
        random_name = get_short_name(fake)

        img = await create_check4(data['money'], data['time'], data['date'], data['money2'], random_digits, random_name)
        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()


@dp.callback_query_handler(text='last_choice')
async def last_choice(callback_query: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    last_country = user_data.get('last_country')

    if not last_country:
        await callback_query.answer("Вы еще не сделали выбора.", show_alert=True)
        return

    if last_country == '1win':
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption="*Вы вновь выбрали 1WIN. Выберите действие:*",
            reply_markup=onewin_inline()
        )
    elif last_country == 'check1':
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption="*Вы вновь выбрали чек с уведомлением. Выберите действие:*",
            reply_markup=check1_inline()
        )
    elif last_country == 'check2':
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption="*Вы вновь выбрали чек без уведомления. Выберите действие:*",
            reply_markup=check2_inline()
        )
    elif last_country == 'check3':
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption="*Вы вновь выбрали третий чек. Выберите действие:*",
            reply_markup=check3_inline()
        )

    elif last_country == 'check4':
        await bot.edit_message_caption(
            chat_id=callback_query.message.chat.id,
            message_id=callback_query.message.message_id,
            caption="*Вы вновь выбрали чек с уведомлением №2. Выберите действие:*",
            reply_markup=check4_inline()
        )


@dp.callback_query_handler(lambda c: c.data == 'onewinbo_go')
async def screen_rendering(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("*🔘 Укажите название банка:*")
    await WinBo.waiting_for_name.set()


@dp.message_handler(state=WinBo.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_time_mexica"))
    await message.answer(f"*🔘 Введите время в формате H:M [{mexico_time}]*", reply_markup=keyboard)
    await WinBo.waiting_for_time.set()


@dp.callback_query_handler(text="use_current_time_mexica", state=WinBo.waiting_for_time)
async def use_current_time_poland(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(time=mexico_time, date=mexico_date)
    await callback_query.message.answer("*🔘 Укажите карту:*")
    await WinBo.waiting_for_card.set()


@dp.message_handler(state=WinBo.waiting_for_time)
async def process_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    await message.answer("*🔘 Укажите карту:*")
    await WinBo.waiting_for_card.set()


@dp.message_handler(state=WinBo.waiting_for_card)
async def process_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['card'] = message.text
    await message.answer("*🔘 Укажите комиссию:*")
    await WinBo.waiting_for_comm.set()


@dp.message_handler(state=WinBo.waiting_for_comm)
async def process_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comm'] = message.text
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Оставить стандартным", callback_data="use_text"))
    await message.answer("*🔘 Укажите текст над синей плашкой:*", reply_markup=keyboard)
    await WinBo.waiting_for_text.set()


@dp.callback_query_handler(text="use_text", state=WinBo.waiting_for_text)
async def use_current_time_poland(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = 'La cuenta especificada se encuentra en el extranjero\nDebe pagar una tarifa de transferencia internacional del 5% del monto del retiro'
    await callback_query.message.answer("*🔘 Укажите сумму пополнения::*")
    await WinBo.waiting_for_money2.set()


@dp.message_handler(state=WinBo.waiting_for_text)
async def process_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await message.answer("*🔘 Укажите сумму пополнения:*")
    await WinBo.waiting_for_money2.set()


@dp.message_handler(state=WinBo.waiting_for_money2)
async def process_money(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if ',' in message.text or '.' in message.text:
            data['popoln'] = message.text
        else:
            data['popoln'] = message.text
        await message.answer("*🔘 Укажите баланс (Salto и Cuenta):*")
        await WinBo.waiting_for_money.set()


@dp.message_handler(state=WinBo.waiting_for_money)
async def process_money(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        if ',' in message.text or '.' in message.text:
            data['money'] = message.text
            data['money2'] = data['money']
        else:
            data['money'] = message.text
            data['money2'] = data['money']

        img = await create_win_bol(data['time'], data['name'], data['card'], data['comm'], data['popoln'], data['money'], data['money2'], data['text'])
        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()


@dp.callback_query_handler(lambda c: c.data == "mx_keyboard")
async def get_mx_keyboard(call: CallbackQuery):
    await call.message.edit_caption(caption="㊙️ Выберите действие:", reply_markup=mx_keyboard())


@dp.callback_query_handler(lambda c: c.data == "bol_keyboard")
async def get_mx_keyboard(call: CallbackQuery):
    await call.message.edit_caption(caption="㊙️ Выберите действие:", reply_markup=bol_keyboard())


@dp.callback_query_handler(lambda c: c.data == "checks:mx")
async def get_checks_mx(call: CallbackQuery):
    await call.message.edit_caption("㊙️ Выберите действие:", reply_markup=checks_mx())


@dp.callback_query_handler(lambda c: c.data == "checks:bol")
async def get_check_bol(call: CallbackQuery):
    await call.message.edit_caption("㊙️ Выберите действие:", reply_markup=checks_bol())
