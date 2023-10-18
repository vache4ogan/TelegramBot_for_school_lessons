import sqlite3

connection = None
cursor = None


def init():
    global connection
    global cursor
    connection = sqlite3.connect('database1.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users
    (
    Id INTEGER PRIMARY KEY,
    UserName TEXT
    )
    ''')


def insert(user_id, userName):
    userName = str(userName)
    try:
        cursor.execute('INSERT INTO Users (Id, UserName) VALUES (?, ?)', (user_id, userName))
    except:
        print("Ошибка")


def show():
    all = f"""SELECT * from Users"""
    cursor.execute(all, )
    all1 = cursor.fetchall()
    for row in all1:
        print(row[0])
        print(row[1])


def id_for_ras():
    all = f"""SELECT * from Users"""
    cursor.execute(all)
    all1 = cursor.fetchall()
    print(all1)
    return all1


def commit():
    global connection
    connection.commit()


def close():
    global connection
    connection.close()
    print('подключение к бд закрыто')
