import random
import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from src.data.db import update_screenshots_count
from src.handlers.default import get_short_name, fake
from src.keyboards.markup import check6_inline
from src.loader import dp, bot
from src.states.form import Notification3
from src.utils.misc import create_notification3
from src.utils.timess import mexico_time2, mexico_date2


@dp.callback_query_handler(lambda c: c.data == 'check6')
async def screen_rendering_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(last_country='check6')
    await bot.edit_message_caption(chat_id=callback_query.message.chat.id,
                                   message_id=callback_query.message.message_id,
                                   caption='*㊙️ Выберите действие:*',
                                   reply_markup=check6_inline())


@dp.callback_query_handler(lambda c: c.data == 'check6_go')
async def screen_rendering_check1_go(callback_query: CallbackQuery, state: FSMContext):
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_time_mexica1"))
    await callback_query.message.answer(f"*🔘 Введите время в формате H:M:S [{mexico_time2}]*", reply_markup=keyboard)
    await Notification3.waiting_for_time.set()


@dp.callback_query_handler(text="use_current_time_mexica1", state=Notification3.waiting_for_time)
async def use_current_time_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(time=mexico_time2)
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_date_mexica1"))
    await callback_query.message.answer(f"*🔘 Укажите дату в формате D/M/Y [{mexico_date2}]:*", reply_markup=keyboard)
    await Notification3.waiting_for_date.set()


@dp.message_handler(state=Notification3.waiting_for_time)
async def process_time_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Автоматический", callback_data="use_current_date_mexica1"))
    await message.answer(f"*🔘 Введите дату в формате D/M/Y [{mexico_date2}]*", reply_markup=keyboard)
    await Notification3.waiting_for_date.set()


@dp.callback_query_handler(text="use_current_date_mexica1", state=Notification3.waiting_for_date)
async def use_current_date_check1(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(date=mexico_date2)
    await callback_query.message.answer("*🔘 Введите сумму пополнения в формате:* `25.000,00`:", parse_mode='MARKDOWN')
    await Notification3.waiting_for_money.set()


@dp.message_handler(state=Notification3.waiting_for_date)
async def process_date_check1(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    await message.answer("*🔘 Введите сумму пополнения:*")
    await Notification3.waiting_for_money.set()


@dp.message_handler(state=Notification3.waiting_for_money)
async def process_money_check1(message: Message, state: FSMContext):
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

        img = await create_notification3(data['money'], data['time'], data['date'], data['money2'], random_digits, random_name)
        await message.answer_photo(img)
        update_screenshots_count(user_id, 1)
        await state.finish()
