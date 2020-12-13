#helper.py

from functools import wraps
from flask import session, redirect
import sqlite3
import os

#login required decorated function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect('/login')
        return f(*args, *kwargs)
    return decorated_function

#function to create users table
def create_users_table(dbFile: str):
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    c.execute(f'''CREATE TABLE IF NOT EXISTS users(id INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(20) NOT NULL, 
    hash BINARY(255) NOT NULL)''')
    conn.commit()
    conn.close()

#function to add user to database
def add_user(Username, Hash):
    DB = 'databases/users.db'
    try:
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('''INSERT INTO users(username, hash) VALUES(?, ?)''', (Username, Hash))
        conn.commit()
        conn.close()
        return redirect('/login')
    except sqlite3.OperationalError as e:
        print(e)

#function to create databases
def initialise():
    if not os.path.exists('databases'):
        print(os.getcwd())
        os.mkdir('databases')
        sqlite3.connect('databases/users.db').close()
        create_users_table(dbFile='databases/users.db')
    else:
        print('Already initialised')


#function to returmn username password hash
def check_username_password_hash(Username):
    DB = 'databases/user.db'
    try:
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('''SELECT hash from users WHERE username = :username''', (Username, ))
        found_hash = list(c.fetchall())
        return found_hash
    except sqlite3.OperationalError as e:
        print (e)
    except Exception as e:
        print(e)
