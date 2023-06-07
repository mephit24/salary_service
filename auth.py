import configparser
import jwt
import time
from hashlib import sha256

from controller import users_in_db

conf = configparser.ConfigParser()
conf.read('config.ini')

LIFETIME_TOKEN_SEC = int(conf['AUTH']['LIFETIME_TOKEN_SEC'])
SECRET = conf['AUTH']['SECRET']
ALGO = conf['AUTH']['JWT_ALGO']


def hash(string: str) -> str:
    '''Create a SHA256-hash from string-argument and return it.'''
    hash = sha256()
    hash.update(str(string).encode())
    return hash.hexdigest()


def create_token(login: str) -> str:
    payload = {
        'login': login,
        'expires': time.time() + LIFETIME_TOKEN_SEC
    }
    return jwt.encode(payload, SECRET, ALGO)


def check(token: str):
    '''
    Check that token is valid.
    Valid token -> token: str
    Invalid token -> False
    '''
    decoded_token = jwt.decode(token, SECRET, ALGO)
    if decoded_token['login'] not in users_in_db():
        return False
    return decoded_token


def check_user(login, password) -> bool:
    users = users_in_db()
    if login not in users or users[login] != hash(password):
        return False
    return True
