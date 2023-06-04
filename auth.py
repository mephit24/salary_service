import jwt
import time
from hashlib import sha256

from controller import users_in_db


LIFETIME_TOKEN_SEC = 3200
SECRET = '$2a$12$QiMiyseFBMWE.lhYOFajFOPU6hSr3RdyAUpmmvpmHKvdxL2/P0/M2'
ALGO = 'HS256'


def hash(string: str) -> str:
    ''' Create a SHA256-hash from string-argument and return it.'''
    hash = sha256()
    hash.update(str(string).encode())
    return hash.hexdigest()


def create_token(login: str) -> str:
    payload = {
        'login': login,
        'expires': time.time() + LIFETIME_TOKEN_SEC
    }
    return jwt.encode(payload, SECRET, ALGO)


def check(token):
    decoded_token = jwt.decode(token, SECRET, ALGO)
    if decoded_token['login'] not in users_in_db():
        return False
    return decoded_token


def check_user(login, password) -> bool:
    users = users_in_db()
    if login not in users or users[login] != hash(password):
        return False
    return True
