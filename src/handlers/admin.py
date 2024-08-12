from src.data.db import get_admins, del_admin, add_admin
from src.keyboards.markup import admin_keyboard, back_to_admin_panel
from src.loader import dp, bot
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from src.states.form import AdminStates
from src.utils.misc import check_admin
from aiogram.utils.exceptions import BadRequest


main_photo_url = 'https://imgur.com/a/t49MRL7'


@dp.callback_query_handler(lambda call: call.data == "admin_panel", state="*")
async def get_admin_buttons(call: CallbackQuery, state: FSMContext):
    await state.finish()
    if not check_admin(call.message.chat.id):
        return await call.message.answer("Ты слишком маленький для таких функций 😡")
    try:
        await call.message.edit_caption("Выберите действие", reply_markup=admin_keyboard())
    except BadRequest:
        await call.message.answer_photo(photo=main_photo_url, caption="Выберите действие", reply_markup=admin_keyboard())


@dp.callback_query_handler(lambda call: call.data == "add_admin")
async def send_add_admin(call: CallbackQuery, state: FSMContext):
    await AdminStates.add_admin.set()
    await call.message.answer("Введите айди", reply_markup=back_to_admin_panel())


@dp.message_handler(state=AdminStates.add_admin)
async def get_add_admin_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
            return await message.answer("Введите верный айди!", reply_markup=back_to_admin_panel())
        
    add_admin(int(message.text))
    await state.finish()
    await message.answer_photo(photo=main_photo_url, caption="Админ был успешно добавлен!", reply_markup=admin_keyboard())


@dp.callback_query_handler(lambda call: call.data == "del_admin")
async def send_del_admin(call: CallbackQuery, state: FSMContext):
    await AdminStates.del_admin.set()
    await call.message.answer("Введите айди", reply_markup=back_to_admin_panel())


@dp.message_handler(state=AdminStates.del_admin)
async def get_del_admin_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Введите верный айди!", reply_markup=back_to_admin_panel())
    
    del_admin(int(message.text))
    await state.finish()
    await message.answer_photo(photo=main_photo_url, caption="Админ был успешно удалён!", reply_markup=admin_keyboard())


@dp.callback_query_handler(lambda call: call.data == "get_admins")
async def send_admins(call: CallbackQuery):
    admins_id = get_admins()
    await call.message.edit_caption(
        "Список админов: \n\n" + "\n".join([f"`{i}`" for i in admins_id]),
        reply_markup=admin_keyboard()
    )
