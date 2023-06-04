import re
import pytest

from auth import hash, create_token, check, check_user


@pytest.mark.parametrize('hashing_obj, result', [('0', '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'),
                                                (0, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'),
                                                ([], '4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'),
                                                ])
def test_hash(hashing_obj, result):
    assert hash(hashing_obj) == result


def test_create_token():
    pattern = r'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\..*\..*'
    assert re.fullmatch(pattern, create_token('somename')) is not None


def test_check():
    token = create_token('test')
    assert check(token)['login'] == 'test'
    token = create_token('jhgrcykvulkiyunlikybfkjykutui')
    assert check(token) is False


@pytest.mark.parametrize('login, password, result', [('test', '12345', True),
                                                     ('gcnjc7tvkv', '12345', False),
                                                     ('test', 'qwerty', False),
                                                     (123, 123, False),
                                                     ])
def test_check_user(login, password, result):
    assert check_user(login, password) is result
