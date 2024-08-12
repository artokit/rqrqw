import sqlite3
from sqlite3 import IntegrityError
from datetime import datetime

conn = sqlite3.connect('otrisoval.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    registration_date TIMESTAMP,
    screenshots_count INTEGER DEFAULT 0
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS admins (
    user_id INTEGER PRIMARY KEY
)
''')


def add_user(user_id):
    registration_date = datetime.now()
    cursor.execute('INSERT INTO users (user_id, registration_date) VALUES (?, ?)', (user_id, registration_date))
    conn.commit()


def check_admin(user_id: int):
    return cursor.execute("SELECT * FROM ADMINS WHERE user_id = ?", (user_id,)).fetchone()


def get_admins():
    return [i[0] for i in cursor.execute("SELECT USER_ID FROM ADMINS").fetchall()]


def add_admin(user_id: int):
    try:
        cursor.execute("INSERT INTO ADMINS(USER_ID) VALUES(?)", (user_id,))
        conn.commit()
    except IntegrityError:
        pass


def del_admin(user_id: int):
    cursor.execute("DELETE FROM ADMINS WHERE user_id = ?", (user_id,))
    conn.commit()

def update_screenshots_count(user_id, count):
    cursor.execute('UPDATE users SET screenshots_count = screenshots_count + ? WHERE user_id = ?', (count, user_id))
    conn.commit()


def get_user_info(user_id):
    cursor.execute('SELECT user_id, registration_date, screenshots_count FROM users WHERE user_id = ?', (user_id,))
    return cursor.fetchone()


def get_total_users_count():
    cursor.execute('SELECT COUNT(*) FROM users')
    return cursor.fetchone()[0]


def get_total_drawings_count():
    cursor.execute('SELECT SUM(screenshots_count) FROM users')
    result = cursor.fetchone()[0]
    return result if result is not None else 0
