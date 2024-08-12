from datetime import datetime

import pytz


def format_duration(from_date):
    duration = datetime.now() - from_date
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{days} дней {hours} часов {minutes} минут"


tz_mexico = pytz.timezone('America/Mexico_City')
mexico_time = datetime.now(tz_mexico).strftime('%H:%M')
mexico_date = datetime.now(tz_mexico).strftime('%B %d, %Y')


tz_mexico2 = pytz.timezone('America/Mexico_City')
mexico_time2 = datetime.now(tz_mexico2).strftime('%H:%M:%S')
mexico_date2 = datetime.now(tz_mexico2).strftime('%d/%m/%Y')

