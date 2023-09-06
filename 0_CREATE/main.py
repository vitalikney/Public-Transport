import psycopg2
from psycopg2 import Error
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import time
import os.path
from config import user, password, host, port, database
from data_bank import *
from generate_routes import *

start_time = time.time()

# Функция создания Базы данных
def create_public_Transport(cursor):
    with open('/home/goidodyr2009/Документы/4_сем/Курсовая/Public_Transport/0_CREATE/1_CREATE_DB.sql', 'r') as f:
        cursor.execute(f.read())

# Заполнение таблицы типов (type)
def incert_type(cursor, bank_type):
    for i in range(len(bank_type)):
                cursor.execute('''
                    INSERT INTO types (type_name) VALUES (%s)
                ''', (bank_type[i],))

# Заполнение таблицы транспортов (transports)
def incert_transports(cursor, bank_transports):
    for i in range(len(bank_transports)):
        if i <= 7:
            transport_type_id = 2
        else:
            transport_type_id = 1
        cursor.execute('''
            INSERT INTO transports (transport_type_id, transport_number) VALUES (%s, %s)
        ''', (transport_type_id, bank_transports[i]))

# Заполнение таблицы остановок (stops)
def incert_stops(cursor, bank_stops):
    for i in range(0, len(bank_stops), 2):
        if bank_transports.index(bank_stops[i + 1]) <= 7:
            stop_type_id = 2
        else:
            stop_type_id = 1
        cursor.execute('''
                INSERT INTO stops (stop_type_id, stop_name) VALUES (%s, %s)
            ''', (stop_type_id, bank_stops[i]))

# Заполнение таблицы остановок и транспортов (stop_transports)
def incert_stop_transports(cursor, bank_stop_transports, bank_transports):
    keys = list(bank_stop_transports.keys())
    for i in range(len(keys)):
        for value in bank_stop_transports[keys[i]]:
            cursor.execute('''
                    INSERT INTO stop_transports (stop_id, transport_id) VALUES (%s, %s)
                ''', (i + 1, bank_transports.index(value) + 1))

# Заполнение таблицы графика автобусов (timetables)
def incert_timetables(cursor, bank_timetables):
    for i in range(195):
        cursor.execute('''
                INSERT INTO timetables (stop_transport_id, times) VALUES (%s, %s)
            ''', (i + 1, bank_timetables))

# Заполнение таблицы связей остановок (communications)
def incert_communications(cursor, bank_communications, bank_stops):
    for i in range(len(bank_communications)):
        cursor.execute('''
                INSERT INTO communications (first_stop_id, second_stop_id, tyme_interval) VALUES (%s, %s, %s)
            ''', (bank_stops.index(bank_communications[i][0]) // 2 + 1, bank_stops.index(bank_communications[i][1]) // 2 + 1, bank_communications[i][2]))

# Заполнение таблицы маршруты (routes)
def incert_routes(cursor, bank_routes, bank_communications, bank_stops):
    for i in range(len(bank_routes)):
        if len(bank_routes[i]) == 2:
            for k in range(len(bank_communications)):
                if ((bank_stops.index(bank_communications[k][0]) // 2 == bank_routes[i][0]) and (bank_stops.index(bank_communications[k][1]) // 2 == bank_routes[i][1])):
                    communication_id = k
                    break
            # print(communication_id + 1, 1, bank_stops[bank_routes[i][0] * 2], bank_stops[bank_routes[i][1] * 2], bank_stops[bank_routes[i][1] * 2])
            cursor.execute('''
                INSERT INTO routes (communication_id, route_part, start_stop, next_stop, finish_stop) VALUES (%s, %s, %s, %s, %s)
            ''', (communication_id + 1, 1, str(bank_stops[bank_routes[i][0] * 2]), str(bank_stops[bank_routes[i][1] * 2]), str(bank_stops[bank_routes[i][1] * 2])))
            continue
        for j in range(len(bank_routes[i]) - 1):
            for k in range(len(bank_communications)):
                if ((bank_stops.index(bank_communications[k][0]) // 2 == bank_routes[i][j]) and (bank_stops.index(bank_communications[k][1]) // 2 == bank_routes[i][j + 1])):
                    communication_id = k
                    break
            # print(communication_id, j + 1, bank_stops[bank_routes[i][0] * 2], bank_stops[bank_routes[i][j + 1] * 2], bank_stops[bank_routes[i][-1] * 2])
            cursor.execute('''
                INSERT INTO routes (communication_id, route_part, start_stop, next_stop, finish_stop) VALUES (%s, %s, %s, %s, %s)
            ''', (communication_id + 1, j + 1, str(bank_stops[bank_routes[i][0] * 2]), str(bank_stops[bank_routes[i][j + 1] * 2]), str(bank_stops[bank_routes[i][-1] * 2])))

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
            #routes = all_routes() 
            #s = 0
            #for i in range(len(routes)):
            #    for j in range(len(routes[i])):
            #        s += 1
            #        cursor.execute('''
            #            INSERT INTO routes (communication_id, route_num, route_part, start_stop, finish_stop) VALUES (%s, %s, %s, %s, %s)
            #        ''', (int(routes[i][j]), int(routes[i][j]), int(routes[i][j]), str(routes[i][j]), str(routes[i][j])))
            #        print(s)

            #for i in range(len(bank_type)):
            #    cursor.execute('''
            #        INSERT INTO types (type_name) VALUES (%s)
            #    ''', (bank_type[i],))

            # for i in range(len(bank_transports)):
            #    cursor.execute('''
            #        INSERT INTO transports (transport_type_id, transport_number) VALUES (%s, %s)
            #    ''', (bank_transports[i][0], bank_transports[i][1]))
            
            # Создание базы данных
            create_public_Transport(cursor)

            # Заполнение
            incert_type(cursor,bank_type)
            incert_transports(cursor, bank_transports)
            incert_stops(cursor, bank_stops)
            incert_stop_transports(cursor, bank_stop_transports, bank_transports)
            incert_timetables(cursor, bank_timetables)
            incert_communications(cursor, bank_communications, bank_stops)
            incert_routes(cursor, bank_routes, bank_communications, bank_stops)
            cursor.execute('''
                SELECT * FROM routes
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
