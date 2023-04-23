from mysql.connector import connect, Error
import os

# TODO: add hashing passwords!

config = {
    "host": os.getenv('MYSQL_HOST'),
    "database": os.getenv('MYSQL_DATABASE'),
    "user": os.getenv('MYSQL_USER'),
    "password": os.getenv('MYSQL_PASSWORD'),
    "port": 3306,
    "charset": "utf8",
    "use_unicode": True,
    "get_warnings": True,
}


def add_user(email, password):
    try:
        with connect(**config) as connection:
            add_query = f'INSERT INTO users (email, password) VALUES("{email}", "{password}");'
            with connection.cursor() as cursor:
                cursor.execute('USE accountsdb;')
                cursor.execute(add_query)
            
            connection.commit()

    except Error as e:
        print(e)


def check_user(email, password):

    is_user = False

    try:
        with connect(**config) as connection:
            select_query = f'SELECT * FROM users WHERE email="{email}"'

            with connection.cursor() as cursor:
                cursor.execute('USE accountsdb;')
                cursor.execute(select_query)

                for user in cursor.fetchall():
                    print(user, flush=True)
                    if user[2] == password:
                        is_user = True
            connection.commit()

    except Error as e:
        print(e)

    return is_user

