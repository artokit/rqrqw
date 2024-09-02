from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from src.loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("㊙️ Отрисовать"),
                KeyboardButton("🌹 Профиль"),
            ],
            [
                KeyboardButton("🀄️ Информация"),
            ],
        ],
    )


def main_inline():
    markup = InlineKeyboardMarkup(row_width=2)
    kb = [InlineKeyboardButton('㊙️ Отрисовать', callback_data='rendering'),
          InlineKeyboardButton('🌹 Профиль', callback_data='profile')]
    markup.add(*kb)
    markup.add(InlineKeyboardButton('👨 Админы', callback_data='admin_panel'))
    markup.add(InlineKeyboardButton('⏮ Последний выбор', callback_data='last_choice'))
    return markup


def admin_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton(text="👨 Добавить админа", callback_data="add_admin"))
    markup.row(InlineKeyboardButton(text="📋 Посмотреть всех админов", callback_data="get_admins"))
    markup.row(InlineKeyboardButton(text="❌ Удалить админа", callback_data="del_admin"))
    markup.row(InlineKeyboardButton('🏠 Домой', callback_data='home'))
    return markup


def back_to_admin_panel():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 Назад", callback_data="admin_panel"))
    return markup

def profile_inline():
    markup = InlineKeyboardMarkup(row_width=2)
    kb = [InlineKeyboardButton('🏠 Домой', callback_data='home')]
    markup.add(*kb)
    return markup


def rendering_inline():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🔘 MEXC", callback_data="draw_bol6"))
    markup.row(InlineKeyboardButton('🏠 Домой', callback_data='home'))
    return markup


def checks():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton('РД', callback_data='rd'))
    markup.row(InlineKeyboardButton('Чеки', callback_data='geo'))
    markup.row(InlineKeyboardButton('Ставки', callback_data='all_in'))
    markup.row(InlineKeyboardButton('🏠 Домой', callback_data='home'))
    return markup


def rd_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🔘 Комс 1", callback_data="draw_bol7"))
    markup.row(InlineKeyboardButton("🔘 PayPal", callback_data="draw_bol4"))
    markup.row(InlineKeyboardButton("🔘 BID", callback_data="draw_bol5"))
    markup.row(InlineKeyboardButton('🏠 Домой', callback_data='home'))
    return markup


def all_checks_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🔘 Чек 1", callback_data="draw_bol1"))
    markup.row(InlineKeyboardButton("🔘 Чек с уведомлением", callback_data="draw_bol2"))
    markup.row(InlineKeyboardButton("🔘 Чек 2", callback_data="draw_bol3"))
    markup.row(InlineKeyboardButton("🔘 Чек Эквадор", callback_data="draw_bol8"))
    markup.row(InlineKeyboardButton('🏠 Домой', callback_data='home'))
    return markup


def get_random_name1_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton(text="Сгенерировать рандомное имя", callback_data='random_name1'))
    return markup


def get_ven_checks_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🔘 Чек 1", callback_data="draw_bol1"))
    markup.row(InlineKeyboardButton("🔘 Чек с уведомлением", callback_data="draw_bol2"))
    markup.row(InlineKeyboardButton("🔘 Чек 2", callback_data="draw_bol3"))
    markup.row(InlineKeyboardButton('🏠 Домой', callback_data='home'))
    return markup


def get_eq_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🔘 Чек 1", callback_data="draw_bol8"))
    markup.row(InlineKeyboardButton('🏠 Домой', callback_data='home'))
    return markup


def get_geo_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton(text="Венесуэла", callback_data='ven'))
    markup.row(InlineKeyboardButton(text="Эквадор", callback_data='eqv'))
    return markup


def all_in_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🔘 MEXC", callback_data="draw_bol6"))
    markup.row(InlineKeyboardButton('🏠 Домой', callback_data='home'))
    return markup


def random_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton(text="Рандом", callback_data="random_data"))
    return markup


def mx_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🔘 1WIN', callback_data='onewin_go'),
        InlineKeyboardButton("🔘 Чеки", callback_data="checks:mx"),
        InlineKeyboardButton('🔘 Ставки', callback_data="check_game:mx"),
        InlineKeyboardButton('🔘 Реквизиты', callback_data='reqs'),
        InlineKeyboardButton('🈳 В меню', callback_data='rendering')
    ]
    markup.add(*buttons)
    return markup


def checks_mx():
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🔘 С уведомлением', callback_data='check1'),
        InlineKeyboardButton('🔘 С уведомлением №2', callback_data='check4'),
        InlineKeyboardButton('🔘 С уведомлением №3', callback_data='check6'),
        InlineKeyboardButton('🔘 Без уведомления', callback_data='check2'),
        InlineKeyboardButton('🔘 Третий чек', callback_data='check3'),
        InlineKeyboardButton('🈳 В меню', callback_data='rendering')
    ]
    markup.add(*buttons)
    return markup


def bol_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🔘 1WIN', callback_data='onewinbo_go'),
        InlineKeyboardButton("🔘 Чеки", callback_data="checks:bol"),
        InlineKeyboardButton('🔘 Ставки', callback_data="check_game:bol"),
        InlineKeyboardButton('🈳 В меню', callback_data='rendering')
    ]
    markup.add(*buttons)
    return markup


def checks_bol():
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton('🔘 BNB', callback_data="check5"),
        InlineKeyboardButton('🔘 Чек №1', callback_data="new_check_bol"),
        InlineKeyboardButton('🔘 Чек №2', callback_data="one_more_check_bol"),
        InlineKeyboardButton('🈳 В меню', callback_data='rendering')
    ]
    markup.add(*buttons)
    return markup


def screen_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    buttons = [
        [InlineKeyboardButton('🔘 С уведомлением', callback_data='check1')],
        [InlineKeyboardButton('🔘 С уведомлением №2', callback_data='check4')],
        [InlineKeyboardButton('🔘 С уведомлением №3', callback_data='check6')],
        [InlineKeyboardButton('🔘 Без уведомления', callback_data='check2')],
        [InlineKeyboardButton('🔘 Третий чек', callback_data='check3')],
        [InlineKeyboardButton('🔘 BNB Боливия', callback_data="check5")],
        [InlineKeyboardButton('🔘 Чек для Боливии №1', callback_data="new_check_bol")],
        [InlineKeyboardButton('🔘 Чек для Боливии №2', callback_data="one_more_check_bol")],
        [InlineKeyboardButton('🔘 Ставка Мексика', callback_data="check_game:mx")],
        [InlineKeyboardButton('🔘 Ставка Боливия', callback_data="check_game:bol")],
        [InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    ]
    markup.add(*[button for sublist in buttons for button in sublist])
    return markup


def reqs_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Oxxo', callback_data='checks:oxxo'),
          InlineKeyboardButton('🔘 Clabe', callback_data='checks:clabe'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def onewin_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать Мексику', callback_data='onewin_go'),
          InlineKeyboardButton('🔘 Отрисовать Боливию', callback_data='onewinbo_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def check1_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать', callback_data='check1_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def check2_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать', callback_data='check2_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def check3_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать', callback_data='check3_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def check4_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать', callback_data='check4_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def check6_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать', callback_data='check6_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def empty_data_game_check():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("Без даты", callback_data="empty_date"))
    return markup


def new_check_bol():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать', callback_data='new_check_bol_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def one_more_check_bol():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать', callback_data='one_more_check_bol_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def game_check_go():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать', callback_data='game_check_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def checks_inline():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('🔘 Отрисовать', callback_data='c_go'),
          InlineKeyboardButton('🈳 В меню', callback_data='rendering')]
    markup.add(*kb)
    return markup


def null_message():
    markup = InlineKeyboardMarkup(row_width=1)
    kb = [InlineKeyboardButton('Оставить пустым', callback_data='message_is_null')]
    markup.add(*kb)
    return markup
