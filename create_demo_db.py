import sqlite3

from auth import hash


conn = sqlite3.connect('db.sqlite3')
with conn:
    cur = conn.cursor()

    cur.execute('''
                DROP TABLE IF EXISTS "users";
                ''')

    cur.execute('''
                CREATE TABLE IF NOT EXISTS "users" (
                "id"	INTEGER NOT NULL UNIQUE,
                "name"	TEXT,
                "login"	TEXT NOT NULL UNIQUE,
                "passwd"	TEXT NOT NULL,
                "current_salary"	REAL NOT NULL,
                "date_up"	DATE NOT NULL,
                PRIMARY KEY("id" AUTOINCREMENT)
                );
                ''')

    adding_users = [
        ('Иванов Иван Иванович', 'ivanov',  hash('qwerty'), 45468.50, '25.11.2024'),
        ('Каценеленбоген Густав Карлович', 'kgk', hash('Sec67'), 45000.00, '24.11.2024'),
        ('', 'anonymous', hash('correcthorsebatterystaple'), 78300.08, '01.01.2024'),
        ('test', 'test', hash('12345'), 500.0000, '01.01.2000'),
    ]

    cur.executemany('INSERT INTO users VALUES (null, ?, ?, ?, ?, ?);', adding_users)
    conn.commit()
