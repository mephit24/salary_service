from model import User


def get_salary(login: str):
    try:
        row = User.get(User.login == login)
        return row.current_salary
    except:
        return None


def get_date_up(login: str):
    try:
        row = User.get(User.login == login)
        return row.date_up
    except:
        return None


def users_in_db():
    try:
        return {user.login: user.passwd for user in User.select()}
    except:
        return None
