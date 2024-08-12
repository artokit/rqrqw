import os
from io import BytesIO
import random

from src.config import ADMIN_ID
from src.data import db
from src.data.db import *
from PIL import Image, ImageDraw, ImageFont


async def ensure_user(user_id):
    user_info = get_user_info(user_id)
    if not user_info:
        add_user(user_id)


def check_admin(user_id):
    return user_id in ADMIN_ID


def check_staff(user_id: int):
    return not not db.check_admin(user_id)


async def create_image(time, name, money, service):
    tink = Image.open("src/Image source/hungary.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 37)
    font_name = ImageFont.truetype(font_path + 'arial.ttf', 24)
    font_money = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 26)
    font_service = ImageFont.truetype(font_path + 'arial.ttf', 25)
    d = ImageDraw.Draw(tink)
    d.text((52, 103), time, font=font_time, fill=(255, 255, 255))
    d.text((159, 675), name, font=font_name, fill=(0, 0, 0))
    d.text((161, 709), '- ' + money + ' HUF', font=font_money, fill=(0, 0, 0))
    d.text((46, 23), service, font=font_service, fill=(255, 255, 255))

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_zealand(time, service, name, name2, money):
    tink = Image.open("src/Image source/Zealand.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 23)
    font_service = ImageFont.truetype(font_path + 'Roboto-Light.ttf', 21)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 21)
    font_name2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 21)
    font_money = ImageFont.truetype(font_path + 'arial.ttf', 24)
    d = ImageDraw.Draw(tink)

    d.text((45, 18), time, font=font_time, fill=(0, 0, 0))
    d.text((27, 695), service, font=font_service, fill=(57, 57, 57))
    d.text((182, 175), name, font=font_name, fill=(0, 0, 0))
    d.text((42, 335), name2, font=font_name2, fill=(0, 0, 0))

    d.text((558, 715), '-$' + money, font=font_money, fill=(0, 0, 0), anchor="rs")

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_switzerland(time, name, date, date2, date3, service, money):
    tink = Image.open("src/Image source/Switzerland.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 26)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 26)
    font_date = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_date2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_date3 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_service = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 26)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 26)
    d = ImageDraw.Draw(tink)

    d.text((73, 28), time, font=font_time, fill=(255, 255, 255))
    d.text((38, 163), name, font=font_name, fill=(255, 255, 255))
    d.text((25, 467), date, font=font_date, fill=(166, 166, 166))
    d.text((25, 619), date2, font=font_date2, fill=(166, 166, 166))
    d.text((25, 1015), date3, font=font_date3, fill=(166, 166, 166))
    d.text((96, 520), service, font=font_service, fill=(255, 255, 255))
    d.text((563, 545), '-' + money, font=font_money, fill=(255, 255, 255), anchor="rs")

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_estonia(time, name, date, date2, date3, service, money):
    tink = Image.open("src/Image source/Estonia.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 25)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 31)
    font_date = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 23)
    font_date2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 23)
    font_date3 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 23)
    font_service = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 26)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 24)
    d = ImageDraw.Draw(tink)

    d.text((35, 29), time, font=font_time, fill=(255, 255, 255))
    d.text((77, 337), name, font=font_name, fill=(123, 123, 123))
    d.text((48, 883), date, font=font_date, fill=(84, 84, 84))
    d.text((48, 1005), date2, font=font_date2, fill=(84, 84, 84))
    d.text((48, 1125), date3, font=font_date3, fill=(84, 84, 84))
    d.text((47, 840), service, font=font_service, fill=(39, 39, 39))
    d.text((545, 867), '-' + money + ' EUR', font=font_money, fill=(39, 39, 39), anchor="rs")

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_france(time, name, date, service, money):
    tink = Image.open("src/Image source/France.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 25)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_date = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 23)
    font_service = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 24)
    d = ImageDraw.Draw(tink)

    d.text((45, 17), time, font=font_time, fill=(255, 255, 255))
    d.text((297, 268), name, font=font_name, fill=(72, 72, 72), anchor='ma')
    d.text((50, 992), date, font=font_date, fill=(28, 28, 28))
    d.text((50, 1026), service, font=font_service, fill=(19, 19, 53))
    d.text((538, 1019), '-' + money + ' €', font=font_money, fill=(19, 19, 53), anchor="rs")

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_slovenia(time, date, date2, date_mt, service, money):
    tink = Image.open("src/Image source/Slovenia.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 28)
    font_date = ImageFont.truetype(font_path + 'arial.ttf', 23)
    font_date_mt = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_service = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 30)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 65)
    d = ImageDraw.Draw(tink)

    d.text((54, 21), time, font=font_time, fill=(0, 0, 0))
    d.text((52, 727), date, font=font_date, fill=(124, 124, 124))
    d.text((52, 860), date2, font=font_date, fill=(124, 124, 124))
    d.text((55, 208), date_mt, font=font_date_mt, fill=(116, 116, 116))
    d.text((53, 587), service, font=font_service, fill=(104, 104, 104))
    d.text((52, 300), '-' + money + ' EUR', font=font_money, fill=(0, 0, 0))

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_australia(time, name, date, service, money):
    tink = Image.open("src/Image source/Australia.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 25)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 21)
    font_date = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 22)
    font_service = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 21)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 24)
    d = ImageDraw.Draw(tink)

    d.text((45, 23), time, font=font_time, fill=(0, 0, 0))
    d.text((20, 305), name, font=font_name, fill=(27, 28, 32))
    d.text((31, 851), date, font=font_date, fill=(0, 0, 0))
    d.text((31, 915), service, font=font_service, fill=(36, 36, 36))
    d.text((553, 938), '-$' + money, font=font_money, fill=(29, 107, 23), anchor="rs")

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_spain(time, name, date, date2, date3, service, money):
    tink = Image.open("src/Image source/Spain.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Bold.ttf', 24)
    font_name = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 28)
    font_date = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 17)
    font_service = ImageFont.truetype(font_path + 'arial.ttf', 22)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 26)
    d = ImageDraw.Draw(tink)

    d.text((57, 19), time, font=font_time, fill=(255, 238, 238))
    d.text((375, 120), name, font=font_name, fill=(255, 255, 255), anchor="rs")
    d.text((23, 870), date, font=font_date, fill=(102, 102, 102))
    d.text((23, 965), date2, font=font_date, fill=(102, 102, 102))
    d.text((23, 1057), date3, font=font_date, fill=(102, 102, 102))
    d.text((23, 835), service, font=font_service, fill=(81, 81, 81))
    d.text((520, 865), '-€ ' + money, font=font_money, fill=(65, 65, 65), anchor="rs")

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_germany(time, name, date, service, money):
    tink = Image.open("src/Image source/Germany.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 26)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_date = ImageFont.truetype(font_path + 'Roboto-Light.ttf', 22)
    font_service = ImageFont.truetype(font_path + 'Roboto-Light.ttf', 21)
    font_money = ImageFont.truetype(font_path + 'Roboto-Light.ttf', 24)
    d = ImageDraw.Draw(tink)

    d.text((68, 21), time, font=font_time, fill=(230, 255, 255))
    d.text((495, 303), name, font=font_name, fill=(215, 243, 255), anchor='rs')
    d.text((36, 1007), date, font=font_date, fill=(13, 33, 42))
    d.text((36, 1065), service, font=font_service, fill=(13, 33, 42))
    d.text((36, 1035), money + ' EUR', font=font_money, fill=(69, 119, 126))

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_poland(time, name, date, date2, service, money):
    tink = Image.open("src/Image source/Poland.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Bold.ttf', 25)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 25)
    font_date = ImageFont.truetype(font_path + 'arial.ttf', 21)
    font_service = ImageFont.truetype(font_path + 'arial.ttf', 25)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 28)
    font_pln = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    d = ImageDraw.Draw(tink)

    d.text((62, 16), time, font=font_time, fill=(255, 242, 244))
    d.text((112, 675), name, font=font_name, fill=(18, 18, 18))
    d.text((65, 945), date, font=font_date, fill=(56, 56, 56))
    d.text((65, 1090), date2, font=font_date, fill=(56, 56, 56))
    d.text((65, 895), service, font=font_service, fill=(56, 56, 56))
    d.text((540, 920), '-' + money, font=font_money, fill=(61, 61, 61), anchor='rs')
    d.text((587, 920), 'PLN', font=font_pln, fill=(6, 6, 6), anchor='rs')

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_win(time, name, card, comm, popoln, money, money2, text):
    tink = Image.open("src/Image source/1win7.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 21)
    font_card = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 16)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 16)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 16)
    font_money2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)
    font_popoln = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 17)
    font_comm = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 15)
    font_text = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 13)
    money2 = money
    d = ImageDraw.Draw(tink)

    d.text((52, 35), time, font=font_time, fill=(255, 242, 244))
    d.text((88, 440), name, font=font_name, fill=(53, 55, 67))
    d.text((460, 148), money + '$', font=font_money, fill=(201, 204, 213), anchor='rs')
    d.text((87, 337), money2 + '$', font=font_money2, fill=(59, 59, 59))
    d.text((78, 543), card, font=font_card, fill=(145, 147, 159))
    d.text((290, 888), 'Continuar con la comision (' + comm + '$)', font=font_comm, fill=(201, 204, 213), anchor='ma')
    d.text((77, 648), popoln + ' $', font=font_popoln, fill=(59, 59, 59))
    if text.count("\n") == 0:
        d.text((290, 815), text, font=font_text, fill=(145, 147, 159), anchor='ma')
    else:
        p = 0
        for i in text.split("\n"):
            d.text((290, 815+p), i, font=font_text, fill=(145, 147, 159), anchor='ma')
            p += 15

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_win_bol(time, name, card, comm, popoln, money, money2, text):
    tink = Image.open("src/Image source/1win_bo1.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 21)
    font_card = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 16)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 16)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 16)
    font_money2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)
    font_popoln = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 17)
    font_comm = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 15)
    font_text = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 13)
    money2 = money
    d = ImageDraw.Draw(tink)

    d.text((52, 35), time, font=font_time, fill=(255, 242, 244))
    d.text((88, 440), name, font=font_name, fill=(53, 55, 67))
    d.text((460, 148), money + '$b', font=font_money, fill=(201, 204, 213), anchor='rs')
    d.text((87, 337), money2 + '$b', font=font_money2, fill=(59, 59, 59))
    d.text((78, 543), card, font=font_card, fill=(145, 147, 159))
    d.text((290, 888), 'Continuar con la comision (' + comm + '$b)', font=font_comm, fill=(201, 204, 213), anchor='ma')
    d.text((77, 648), popoln + ' $b', font=font_popoln, fill=(59, 59, 59))

    if text.count("\n") == 0:
        d.text((290, 815), text, font=font_text, fill=(145, 147, 159), anchor='ma')
    else:
        p = 0
        for i in text.split("\n"):
            d.text((290, 815+p), i, font=font_text, fill=(145, 147, 159), anchor='ma')
            p += 15

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


async def create_check1(money, time, date, money2, random_digits, random_name):
    tink = Image.open("src/Image source/Check1_3.jpg") #1_3
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Barlow-Regular.otf', 21)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 25)
    font_money2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 52)
    font_symbol = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 30)
    font_random = ImageFont.truetype(font_path + 'arial.ttf', 21)
    font_random2 = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 22)

    d = ImageDraw.Draw(tink)

    d.text((236, 965), time, font=font_time, fill=(118, 121, 126), anchor='rs')
    d.text((158, 965), date + ' - ', font=font_time, fill=(118, 121, 126), anchor='rs')
    d.text((123, 82), 'ferencia por $' + money + ' desde...', font=font_money, fill=(237, 237, 237))


    money_bbox = d.textbbox((0, 0), money2, font=font_money2)
    money_width = money_bbox[2] - money_bbox[0]
    money_height = money_bbox[3] - money_bbox[1]

    dollar_bbox = d.textbbox((0, 0), "$", font=font_symbol)
    dollar_width = dollar_bbox[2] - dollar_bbox[0]
    dollar_height = dollar_bbox[3] - dollar_bbox[1]

    mn_bbox = d.textbbox((0, 0), "MN", font=font_symbol)
    mn_width = mn_bbox[2] - mn_bbox[0]
    mn_height = mn_bbox[3] - mn_bbox[1]

    total_width = dollar_width + money_width + mn_width + 10

    center_x = 315
    center_y = 510

    dollar_x = center_x - total_width / 2
    dollar_y = center_y - dollar_height / 2 + 13

    money_x = dollar_x + dollar_width + 5
    money_y = center_y - money_height / 2

    mn_x = money_x + money_width + 14
    mn_y = center_y - mn_height / 2 + 9

    d.text((dollar_x, dollar_y), "$", font=font_symbol, fill=(51, 54, 59))
    d.text((money_x, money_y), money2, font=font_money2, fill=(47, 54, 62))
    d.text((mn_x, mn_y), "MN", font=font_symbol, fill=(51, 54, 59))

    d.text((477, 775), random_digits, font=font_random, fill=(124, 124, 124))

    d.text((448, 715), random_name, font=font_random2, fill=(57, 58, 60), anchor='ma')

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_check2(time, date, money2, random_digits, random_name):
    tink = Image.open("src/Image source/Check2.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Barlow-Regular.otf', 21)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 25)
    font_money2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 52)
    font_symbol = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 30)
    font_random = ImageFont.truetype(font_path + 'arial.ttf', 21)
    font_random2 = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 22)

    d = ImageDraw.Draw(tink)

    d.text((236, 945), time, font=font_time, fill=(118, 121, 126), anchor='rs')
    d.text((158, 945), date + ' - ', font=font_time, fill=(118, 121, 126), anchor='rs')

    money_bbox = d.textbbox((0, 0), money2, font=font_money2)
    money_width = money_bbox[2] - money_bbox[0]
    money_height = money_bbox[3] - money_bbox[1]

    dollar_bbox = d.textbbox((0, 0), "$", font=font_symbol)
    dollar_width = dollar_bbox[2] - dollar_bbox[0]
    dollar_height = dollar_bbox[3] - dollar_bbox[1]

    mn_bbox = d.textbbox((0, 0), "MN", font=font_symbol)
    mn_width = mn_bbox[2] - mn_bbox[0]
    mn_height = mn_bbox[3] - mn_bbox[1]

    total_width = dollar_width + money_width + mn_width + 10

    center_x = 315
    center_y = 510

    dollar_x = center_x - total_width / 2
    dollar_y = center_y - dollar_height / 2 - 37

    money_x = dollar_x + dollar_width + 15
    money_y = center_y - money_height / 2 - 48

    mn_x = money_x + money_width + 14
    mn_y = center_y - mn_height / 2 - 37

    d.text((dollar_x, dollar_y), "$", font=font_symbol, fill=(51, 54, 59))
    d.text((money_x, money_y), money2, font=font_money2, fill=(47, 54, 62))
    d.text((mn_x, mn_y), "MN", font=font_symbol, fill=(51, 54, 59))

    d.text((508, 742), random_digits, font=font_random, fill=(124, 124, 124))

    d.text((478, 685), random_name, font=font_random2, fill=(57, 58, 60), anchor='ma')

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


def format_name(name):
    words = name.split()
    if len(words) == 1:
        return words[0][:2].upper()
    else:
        return ''.join(word[0].upper() for word in words[:2])


async def create_check3(time, money, money_fraction, name, random_digits, sender_name, sender_card_last_numbers):
    tink = Image.open("src/Image source/Check3_1.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)
    font_money = ImageFont.truetype(font_path + 'BwNistaGrotesk-Regular.ttf', 48)
    font_moneyf = ImageFont.truetype(font_path + 'BwNistaGrotesk-Regular.ttf', 30)
    font_name = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 21)
    font_name2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 29)
    font_random = ImageFont.truetype(font_path + 'Roboto-Italic.ttf', 18)
    d = ImageDraw.Draw(tink)

    d.text((283, 58), time + ' h', font=font_time, fill=(202, 254, 209), anchor='ma')

    money_bbox = d.textbbox((0, 0), '$' + money, font=font_money)
    money_width = money_bbox[2] - money_bbox[0]

    d.text((270, 125), '$' + money, font=font_money, fill=(233, 253, 232), anchor='ma')
    d.text((273 + money_width / 2 + 3, 125), money_fraction, font=font_moneyf, fill=(233, 253, 232), anchor='la')

    d.text((285, 342), name, font=font_name, fill=(0, 0, 0))

    sender_name_bbox = d.textbbox((0, 0), sender_name, font=font_name)
    sender_width = sender_name_bbox[2] - sender_name_bbox[0]
    print(sender_width, sender_name_bbox)
    w_x = 205
    if sender_width > 60:
        w_x -= sender_name_bbox[2] - 60

    d.text((w_x, 342), sender_name, font=font_name, fill=(0, 0, 0))
    formatted_name = format_name(name)
    d.text((335, 261), formatted_name, font=font_name2, fill=(233, 253, 232), anchor='ma')

    d.text((305, 388), random_digits, font=font_random, fill=(45, 45, 45))
    d.text((227, 369), sender_card_last_numbers, font=font_random, fill=(45, 45, 45))

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_bnb_screen(sender_name, date, time, recipient_name, bank_name, money):
    tink = Image.open("src/Image source/bnb.png")
    font_path = "src/Fonts/"
    font = ImageFont.truetype(os.path.join(font_path, "dizhitl-extralight.ttf"), 32)
    d = ImageDraw.Draw(tink)

    d.text((404, 320), sender_name, font=font, fill=(82, 82, 82))
    d.text((404, 390), date, font=font, fill=(82, 82, 82))
    d.text((404, 460), time, font=font, fill=(82, 82, 82))
    d.text((404, 546), sender_name.upper(), font=font, fill=(82, 82, 82))
    d.text((404, 752), recipient_name, font=font, fill=(82, 82, 82))
    d.text((404, 839), bank_name, font=font, fill=(82, 82, 82))
    d.text((404, 977), money, font=font, fill=(82, 82, 82))

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_check4(money, time, date, money2, random_digits, random_name):
    tink = Image.open("src/Image source/Check4.jpg")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Barlow-Regular.otf', 21)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 25)
    font_money2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 45)
    font_symbol = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 30)
    font_random = ImageFont.truetype(font_path + 'arial.ttf', 20)
    font_random2 = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 22)

    d = ImageDraw.Draw(tink)

    d.text((236, 923), time, font=font_time, fill=(118, 121, 126), anchor='rs')
    d.text((158, 923), date + ' - ', font=font_time, fill=(118, 121, 126), anchor='rs')
    d.text((123, 125), 'por $' + money + ' desde...', font=font_money, fill=(237, 237, 237))


    money_bbox = d.textbbox((0, 0), money2, font=font_money2)
    money_width = money_bbox[2] - money_bbox[0]
    money_height = money_bbox[3] - money_bbox[1]

    dollar_bbox = d.textbbox((0, 0), "$", font=font_symbol)
    dollar_width = dollar_bbox[2] - dollar_bbox[0]
    dollar_height = dollar_bbox[3] - dollar_bbox[1]

    mn_bbox = d.textbbox((0, 0), "MXN", font=font_symbol)
    mn_width = mn_bbox[2] - mn_bbox[0]
    mn_height = mn_bbox[3] - mn_bbox[1]

    total_width = dollar_width + money_width + mn_width + 10

    center_x = 315 # 315
    center_y = 475 # 510

    dollar_x = center_x - total_width / 2
    dollar_y = center_y - dollar_height / 2 + 8

    money_x = dollar_x + dollar_width + 5
    money_y = center_y - money_height / 2

    mn_x = money_x + money_width + 14
    mn_y = center_y - mn_height / 2 + 6

    d.text((dollar_x, dollar_y), "$", font=font_symbol, fill=(51, 54, 59))
    d.text((money_x, money_y), money2, font=font_money2, fill=(47, 54, 62))
    d.text((mn_x, mn_y), "MXN", font=font_symbol, fill=(51, 54, 59))

    d.text((455, 735), random_digits, font=font_random, fill=(124, 124, 124))

    d.text((440, 675), random_name, font=font_random2, fill=(57, 58, 60), anchor='ma')

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def create_notification3(money, time, date, money2, random_digits, random_name):
    tink = Image.open("src/Image source/Check7.png")
    font_path = "src/Fonts/"
    font_time = ImageFont.truetype(font_path + 'Barlow-Regular.otf', 21)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)
    font_money2 = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 45)
    font_symbol = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 30)
    font_random = ImageFont.truetype(font_path + 'arial.ttf', 20)
    font_random2 = ImageFont.truetype(font_path + 'Roboto-Medium.ttf', 22)
    date_s = datetime.strptime(date, "%d/%m/%Y").strftime("%b-%d")
    time_s = datetime.strptime(time, "%H:%M:%S").strftime("%H:%M")
    d = ImageDraw.Draw(tink)

    d.text((236, 923), time, font=font_time, fill=(118, 121, 126), anchor='rs')
    d.text((158, 923), date + ' - ', font=font_time, fill=(118, 121, 126), anchor='rs')
    d.text((123, 103), f'{date_s} {time_s} CTA DEB Spei enviado {money} BBVA', font=font_money, fill=(237, 237, 237))
    d.text((123, 129), '800-2262663', font=font_money, fill=(237, 237, 237))


    money_bbox = d.textbbox((0, 0), money2, font=font_money2)
    money_width = money_bbox[2] - money_bbox[0]
    money_height = money_bbox[3] - money_bbox[1]

    dollar_bbox = d.textbbox((0, 0), "$", font=font_symbol)
    dollar_width = dollar_bbox[2] - dollar_bbox[0]
    dollar_height = dollar_bbox[3] - dollar_bbox[1]

    mn_bbox = d.textbbox((0, 0), "MXN", font=font_symbol)
    mn_width = mn_bbox[2] - mn_bbox[0]
    mn_height = mn_bbox[3] - mn_bbox[1]

    total_width = dollar_width + money_width + mn_width + 10

    center_x = 315 # 315
    center_y = 475 # 510

    dollar_x = center_x - total_width / 2
    dollar_y = center_y - dollar_height / 2 + 8

    money_x = dollar_x + dollar_width + 5
    money_y = center_y - money_height / 2

    mn_x = money_x + money_width + 14
    mn_y = center_y - mn_height / 2 + 6

    d.text((dollar_x, dollar_y - 3), "$", font=font_symbol, fill=(51, 54, 59))
    d.text((money_x, money_y - 3), money2, font=font_money2, fill=(47, 54, 62))
    d.text((mn_x, mn_y), "MXN", font=font_symbol, fill=(51, 54, 59))

    d.text((455, 735), random_digits, font=font_random, fill=(124, 124, 124))

    d.text((440, 675), random_name, font=font_random2, fill=(57, 58, 60), anchor='ma')

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def oxxo_pay_screen(card, name, money, image_name):
    tink = Image.open(f"src/Image source/{image_name}_pay.png")
    font_path = "src/Fonts/"
    font_card = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 16)
    font_name = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 16)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 16)

    d = ImageDraw.Draw(tink)
    d.text((661, 258), card, font=font_card, fill=(38, 41, 48))
    d.text((661, 333), name, font=font_name, fill=(38, 41, 48))
    d.text((780, 409), money + " $", font=font_money, fill=(38, 41, 48))

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def new_check_for_boli(date, money, name_getter, card_getter, name_sender, message):
    tink = Image.open(f"src/Image source/new_check_bol.png")
    font_path = "src/Fonts/"
    font_date = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 24)
    font_money = ImageFont.truetype(font_path + 'Roboto-Bold.ttf', 38)
    font_name_getter = ImageFont.truetype(font_path + 'Roboto-Bold.ttf', 22)
    font_card_getter = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)
    font_name_sender = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)
    font_message = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)
    font_trans = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)

    d = ImageDraw.Draw(tink)
    d.text((365, 380), date, font=font_date, fill=(119, 117, 120), anchor='ma')
    d.text((365, 513), "Bs. " + money, font=font_money, fill=(42, 29, 59), anchor='ma')
    d.text((160, 632), name_getter, font=font_name_getter, fill=(111, 53, 103))
    d.text((160, 660), card_getter, font=font_card_getter, fill=(89, 89, 91))
    d.text((160, 890), name_sender, font=font_name_sender, fill=(111, 53, 103))
    d.text((160, 1005), message, font=font_message, fill=(111, 53, 103))
    d.text((160, 1120), str(random.randint(60_000_000, 90_000_000)), font=font_trans, fill=(111, 53, 103))

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def comprobante_check(date, money, name_getter):
    tink = Image.open(f"src/Image source/comprobante.png")
    font_path = "src/Fonts/"
    font_date = ImageFont.truetype(font_path + 'Roboto-Bold.ttf', 26)
    font_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 26)
    font_name_getter = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 26)

    d = ImageDraw.Draw(tink)
    d.text((41, 175), date, font=font_date, fill=(0, 0, 0))
    d.text((110, 271), "Bs. " + money, font=font_money, fill=(0, 0, 0))
    d.text((70, 301), name_getter.upper(), font=font_name_getter, fill=(0, 0, 0))

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


async def win_game_check(date, win_money, account_money, cuota, apuesta, lang):
    if lang == "mx":
        tink = Image.open(f"src/Image source/game_check.png")
    else:
        tink = Image.open(f"src/Image source/game_check_bol.png")

    font_path = "src/Fonts/"
    ticket_id = random.randint(110_000_000, 310_000_000)
    font_date = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 14)
    font_win_money = ImageFont.truetype(font_path + 'Roboto-Bold.ttf', 21)
    font_account_money = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)
    font_cuota = ImageFont.truetype(font_path + 'Roboto-Bold.ttf', 20)
    font_apuesta = ImageFont.truetype(font_path + 'Roboto-Bold.ttf', 20)
    font_ticket = ImageFont.truetype(font_path + "Roboto-Regular.ttf", 17)
    font_cuota_big = ImageFont.truetype(font_path + "Roboto-Bold.ttf", 17)
    font_min_date = ImageFont.truetype(font_path + "Roboto-Regular.ttf", 13)
    d = ImageDraw.Draw(tink)
    d.text((38, 252), date, font=font_date, fill=(255, 255, 255))
    d.text((500, 475), f"+ {win_money} {'$' if lang == 'mx' else 'Bs'}", font=font_win_money, fill=(32, 129, 22), anchor="rm")
    d.text((274, 48), f"{account_money} {'$' if lang == 'mx' else '$S'}", font=font_account_money, fill=(255, 255, 255), anchor="rm")
    d.text((156, 465), cuota, font=font_cuota, fill=(0, 0, 0), anchor="ma")
    d.text((64, 297), cuota, font=font_cuota_big, fill=(255, 255, 255), anchor="ma")
    d.text((65, 465), f"{apuesta}{'$' if lang == 'mx' else '$S'}", font=font_apuesta, fill=(0, 0, 0), anchor="ma")
    d.text((497, 258), f"ID {ticket_id}", font=font_ticket, fill=(255, 255, 255), anchor="rm")
    d.text((500, 418), date, font=font_min_date, fill=(134, 134, 134), anchor="rm")

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


def draw_bol1(amount, date, operation_id, getter, origen, destino, bank):
    tink = Image.open(f"src/Image source/bol1.png")
    font_path = "src/Fonts/"
    font_amount = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 32)
    font_date = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_operation = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_getter = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_origen = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_destino = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)
    font_bank = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 22)

    d = ImageDraw.Draw(tink)
    d.text((290, 343), amount + " Bs", font=font_amount, fill=(0, 0, 0), anchor="ma")
    d.text((525, 433), date, font=font_date, fill=(0, 0, 0), anchor="rm")
    d.text((490, 480), operation_id, font=font_operation, fill=(0, 0, 0), anchor="rm")
    d.text((525, 530), getter, font=font_getter, fill=(0, 0, 0), anchor="rm")
    d.text((525, 630), origen, font=font_origen, fill=(0, 0, 0), anchor="rm")
    d.text((525, 680), destino, font=font_destino, fill=(0, 0, 0), anchor="rm")
    d.text((525, 730), bank, font=font_bank, fill=(0, 0, 0), anchor="rm")

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


def draw_bol1_notify(amount, date, operation_id, getter, origen, destino, bank):
    tink = Image.open(f"src/Image source/bol1_notify.png")
    font_path = "src/Fonts/"
    font_amount = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 24)
    font_date = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 18)
    font_operation = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 20)
    font_getter = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 19)
    font_origen = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 20)
    font_destino = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 20)
    font_bank = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 20)
    font_notify = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 19)

    d = ImageDraw.Draw(tink)
    d.text((130, 125), f"Bs.{amount.replace('.', '')} se realizó con éxito bajo el", font=font_notify, fill=(112, 112, 112))
    d.text((282, 390), amount + " Bs", font=font_amount, fill=(0, 0, 0), anchor="ma")
    d.text((511, 474), date, font=font_date, fill=(0, 0, 0), anchor="rm")
    d.text((480, 518), operation_id, font=font_operation, fill=(0, 0, 0), anchor="rm")
    d.text((510, 560), getter, font=font_getter, fill=(0, 0, 0), anchor="rm")
    d.text((512, 648), origen, font=font_origen, fill=(0, 0, 0), anchor="rm")
    d.text((512, 691), destino, font=font_destino, fill=(0, 0, 0), anchor="rm")
    d.text((512, 735), bank, font=font_bank, fill=(0, 0, 0), anchor="rm")

    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio


def draw_bol2(amount, getter, pin, date):
    tink = Image.open(f"src/Image source/bol2.png")
    font_path = "src/Fonts/"
    font_amount = ImageFont.truetype(font_path + 'Roboto-Light.ttf', 80)
    font_amount1 = ImageFont.truetype(font_path + 'Roboto-Light.ttf', 60)
    font_date = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 37)
    font_getter = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 36)
    font_pin = ImageFont.truetype(font_path + 'Roboto-Regular.ttf', 40)

    left_pin, right_pin = pin.split(" ")
    d = ImageDraw.Draw(tink)
    d.text((540, 185), f"  {amount}", font=font_amount, fill=(252, 255, 243), anchor="ma")
    mn_bbox = d.textbbox((0, 0), f"  {amount}", font=font_amount)
    mn_width = mn_bbox[2] - mn_bbox[0]
    d.text((540 - (mn_width/2), 185), f"Bs.", font=font_amount1, fill=(252, 255, 243), anchor="ma")
    d.text((285, 538), getter, font=font_getter, fill=(0, 0, 0))
    d.text((285, 633), f"{left_pin}-****-**-******-{right_pin}", font=font_pin, fill=(0, 0, 0))
    d.text((285, 824), date, font=font_date, fill=(0, 0, 0))
    bio = BytesIO()
    bio.name = 'output.png'
    tink.save(bio, 'PNG')
    bio.seek(0)
    return bio
