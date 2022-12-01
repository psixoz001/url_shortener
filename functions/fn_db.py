from database.CreateDB import *
from werkzeug.security import generate_password_hash, check_password_hash


def findUser(email):
    return connect.cursor().execute('SELECT * FROM users WHERE email=?', (email,)).fetchone()


def registration(email, password):
    if findUser(email) is None:
        password = generate_password_hash(password)
        connect.cursor().execute('INSERT INTO users (email,password) VALUES(?,?)', (email, password,))
        connect.commit()
        return True
    return False


def auth(email, password):
    user = findUser(email)
    if user:
        if check_password_hash(user['password'], password):
            return True
        return False
    return False
