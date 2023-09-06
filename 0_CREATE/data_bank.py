from read_file import *
from generate_routes import *

bank_type = ['Назменый тип', 'Подземный тип']

# 0 1 2 3 4 5 6  7 - 2 type
bank_transports = ['1', '2', '3', '5', '6', '7', '9', '10', 'Трамвай А', 'Трамвай 7', 'Автобус Б', 'Автобус М1', 'Автобус М5', 'Автобус М7', 'Автобус М9', 'Автобус М90']
filename = "0_CREATE/stations.txt"

""" result = read_file(filename)
for i in range(len(result)):
    print(i, bank_transports.index(result[i][1]), bank_transports.index(result[i][3])) """

bank_stops = read_stops(filename)
# for i in range(0, len(bank_stops), 2):
    # print(stops[i], bank_transports.index(stops[i + 1]))
    # print(i, i // 2,  bank_stops[i], bank_stops[i + 1])
    # print((i // 2) + 1, bank_transports.index(bank_stops[i + 1]) + 1)

bank_stop_transports = read_stop_transports(filename)

bank_timetables = "с 5:30 до 1 часу каждые 3 - 10 минут"

bank_communications = read_communications(filename)

# print(bank_communications)

bank_routes = all_routes()
print()

""" print(bank_routes)
for i in range(len(bank_routes)):
    if len(bank_routes[i]) == 2:
        for k in range(len(bank_communications)):
            if ((bank_stops.index(bank_communications[k][0]) // 2 == bank_routes[i][0]) and (bank_stops.index(bank_communications[k][1]) // 2 == bank_routes[i][1])):
                communication_id = k
                break
        print(communication_id + 1, 1, bank_stops[bank_routes[i][0] * 2], bank_stops[bank_routes[i][1] * 2], bank_stops[bank_routes[i][1] * 2])
        continue
    for j in range(len(bank_routes[i]) - 1):
        for k in range(len(bank_communications)):
            if ((bank_stops.index(bank_communications[k][0]) // 2 == bank_routes[i][j]) and (bank_stops.index(bank_communications[k][1]) // 2 == bank_routes[i][j + 1])):
                communication_id = k
                break
        print(communication_id, j + 1, bank_stops[bank_routes[i][0] * 2], bank_stops[bank_routes[i][j + 1] * 2], bank_stops[bank_routes[i][-1] * 2]) """



""" keys = list(bank_stop_transports.keys())
print(keys)
print(len(keys))
for i in range(len(keys)):
    for value in bank_stop_transports[keys[i]]:
        print(keys[i], i + 1, value, bank_transports.index(value) + 1) """
