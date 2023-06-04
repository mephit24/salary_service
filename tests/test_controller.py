import pytest

from controller import users_in_db, get_salary, get_date_up


valid_login = 'test'
invalid_login = 'sTpQVQxGRSeL9QAswCQM6bwA'

@pytest.mark.parametrize('login, result', [(valid_login, True),
                                          (invalid_login, False),
                                          (123, False),
                                          ])
def test_users_in_db(login, result):
    assert isinstance(users_in_db(), dict)
    assert isinstance(users_in_db().get(login), type(None)) is not result


def test_get_salary():
    assert get_salary(valid_login) == 500
    assert get_salary(invalid_login) is None


def test_get_date_up():
    assert get_date_up(valid_login) == '01.01.2000'
    assert get_salary(invalid_login) is None
