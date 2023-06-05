from peewee import *


db = SqliteDatabase('db.sqlite3')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = TextField(column_name='name')
    login = TextField(column_name='login')
    passwd = TextField(column_name='passwd')
    current_salary = FloatField(column_name='current_salary')
    date_up = DateField(column_name='date_up')

    class Meta:
        table_name = 'users'
