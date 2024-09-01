from aiogram.dispatcher.filters.state import State, StatesGroup


class Win(StatesGroup):
    waiting_for_time = State()
    waiting_for_money = State()
    waiting_for_name = State()
    waiting_for_card = State()
    waiting_for_service = State()
    waiting_for_money2 = State()
    waiting_for_comm = State()
    waiting_for_text = State()


class Check1(StatesGroup):
    waiting_for_time = State()
    waiting_for_date = State()
    waiting_for_money = State()
    waiting_for_name = State()
    waiting_for_card = State()
    waiting_for_service = State()
    waiting_for_money2 = State()
    waiting_for_comm = State()
    waiting_for_text = State()


class Check2(StatesGroup):
    waiting_for_time = State()
    waiting_for_date = State()
    waiting_for_money = State()
    waiting_for_name = State()
    waiting_for_card = State()
    waiting_for_service = State()
    waiting_for_money2 = State()
    waiting_for_comm = State()
    waiting_for_text = State()


class Check3(StatesGroup):
    waiting_for_time = State()
    waiting_for_money = State()
    waiting_for_name = State()
    waiting_for_sender_name = State()
    waiting_for_sender_last_numbers = State()
    waiting_for_random_digits = State()


class Check4(StatesGroup):
    waiting_for_time = State()
    waiting_for_date = State()
    waiting_for_money = State()
    waiting_for_name = State()
    waiting_for_card = State()
    waiting_for_service = State()
    waiting_for_money2 = State()
    waiting_for_comm = State()
    waiting_for_text = State()


class Check5(StatesGroup):
    waiting_sender_name = State()
    waiting_date = State()
    waiting_time = State()
    waiting_recipient_name = State()
    waiting_bank_name = State()
    waiting_money = State()


class WinBo(StatesGroup):
    waiting_for_time = State()
    waiting_for_money = State()
    waiting_for_name = State()
    waiting_for_card = State()
    waiting_for_service = State()
    waiting_for_money2 = State()
    waiting_for_comm = State()
    waiting_for_text = State()


class Notification3(StatesGroup):
    waiting_for_time = State()
    waiting_for_date = State()
    waiting_for_money = State()
    waiting_for_name = State()
    waiting_for_card = State()
    waiting_for_service = State()
    waiting_for_money2 = State()
    waiting_for_comm = State()
    waiting_for_text = State()


class Checks(StatesGroup):
    card = State()
    fio = State()
    money = State()


class NewCheckBol(StatesGroup):
    date = State()
    money = State()
    name_getter = State()
    card_getter = State()
    name_sender = State()
    message = State()


class AdminStates(StatesGroup):
    del_admin = State()
    add_admin = State()


class ComproStates(StatesGroup):
    date = State()
    money = State()
    name_getter = State()


class GameCheckStates(StatesGroup):
    date = State()
    win_money = State()
    account_money = State()
    cuota = State()
    apuesta = State()


class DrawBol(StatesGroup):
    amount = State()
    date = State()
    operation = State()
    getter = State()
    origen = State()
    destino = State()
    bank = State()


class DrawBol2(StatesGroup):
    amount = State()
    getter = State()
    pin = State()
    date = State()


class DrawBol4(StatesGroup):
    client_name = State()
    amount1 = State()
    amount2 = State()
    card = State()


class DrawBol5(StatesGroup):
    card = State()
    bank = State()
    amount1 = State()
    amount2 = State()


class DrawBol6(StatesGroup):
    pair = State()
    amount = State()


class FinalChecks(StatesGroup):
    card = State()
    bank = State()
    amount = State()


class NewCheck(StatesGroup):
    amount = State()
    date = State()
    name = State()
    card = State()
