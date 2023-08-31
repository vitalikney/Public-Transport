import psycopg2
from psycopg2 import Error
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import time
import os.path
from config import user, password, host, port, database
from data_bank import *

start_time = time.time()

def create_public_Transport(cursor):
    with open('/home/goidodyr2009/Документы/4_сем/Курсовая/Public Transport/0 CREATE/1_CREATE_DB.sql', 'r') as f:
        cursor.execute(f.read())

if (__name__ == '__main__'):
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(
            user=user,
            # пароль, который указали при установке PostgreSQL
            password=password,
            host=host,
            port=port,
            database=database)

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        with connection.cursor() as cursor:
            create_public_Transport(cursor)

            for i in range(len(bank_type)):
                cursor.execute('''
                    INSERT INTO types (type_name) VALUES (%s)
                ''', (bank_type[i],))

            for i in range(len(bank_transports)):
                cursor.execute('''
                    INSERT INTO transports (transport_type_id, transport_number) VALUES (%s, %s)
                ''', (bank_transports[i][0], bank_transports[i][1]))
            
            cursor.execute('''
                SELECT * FROM types
            ''')

            data = cursor.fetchall()

            for i in data:
                print(*i)

    except(Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            connection.close()
            print("-------------------------------")
            print("Соединение с PostgreSQL закрыто")

    print("--- %s seconds ---" % (time.time() - start_time))
