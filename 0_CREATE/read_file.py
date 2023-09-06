# Чтение всех файла
def read_file(filename):
    result = [] # массив всех данных из файла
    stops = [] # порядок вхождения станций
    # n = 169
    # lens = [[0 for j in range(n)] for i in range(n)] # матрица длин
    # lens = [[0] * 169] * 169
    # print(lens)
    with open(filename, "r") as file:
        line = file.readline()
        while line:
            line = line.split(', ')
            if line[-1].find("\n") != -1:
                line[-1] = line[-1][:line[-1].find("\n")]
            if not (line[0] in stops):
                stops.append(line[0])
            if not (line[2] in stops):
                stops.append(line[2])
            # print(stops.index(line[0]), line[0])
            # lens[stops.index(line[0])][stops.index(line[2])] = int(line[-1])
            result.append(line)
            line = file.readline()
    # for i in result:
    #   print(*i)
    # print(result)
    # print(stops)
    # print(len(stops))
    # print(len(stops))
    # for i in lens:
    #    print(*i)
    # print(lens)
    # return stops, lens
    return result

# Чтение остановок для таблицы Stops
def read_stops(filename):
    stops = [] # порядок вхождения станций
    with open(filename, "r") as file:
        line = file.readline()
        while line:
            line = line.split(', ')
            if line[-1].find("\n") != -1:
                line[-1] = line[-1][:line[-1].find("\n")]
            if not (line[0] in stops):
                stops.append(line[0])
                stops.append(line[1])
            if not (line[2] in stops):
                stops.append(line[2])
                stops.append(line[3])
            line = file.readline()
    return stops

# Чтение остановок для таблицы Stops_transports
def read_stop_transports(filename):
    stops = {} # порядок вхождения станций
    with open(filename, "r") as file:
        line = file.readline()
        while line:
            line = line.split(', ')
            if not (line[0] in stops.keys()):
                stops[line[0]] = [line[1]]
            elif not (line[1] in stops[line[0]]):
                stops[line[0]] += [line[1]]
            if not (line[2] in stops.keys()):
                stops[line[2]] = [line[3]]
            elif not (line[3] in stops[line[2]]):
                stops[line[2]] += [line[3]]
            line = file.readline()
    return stops

# Чтение остановок для таблицы communications
def read_communications(filename):
    result = [] # массив всех данных из файла
    with open(filename, "r") as file:
        line = file.readline()
        while line:
            line = line.split(', ')
            if line[-1].find("\n") != -1:
                line[-1] = line[-1][:line[-1].find("\n")]
            result.append([line[0], line[2], int(line[4])])
            line = file.readline()
    return result

# Чтение файла, заполнения матрица весов графа
def lines(filename, n):
    result = [] # массив всех данных из файла
    stops = [] # порядок вхождения станций
    # n = 169
    lens = [[0 for j in range(n)] for i in range(n)] # матрица длин
    # lens = [[0] * 169] * 169
    # print(lens)
    with open(filename, "r") as file:
        line = file.readline()
        while line:
            line = line.split(', ')
            if line[-1].find("\n") != -1:
                line[-1] = line[-1][:line[-1].find("\n")]
            if not (line[0] in stops):
                stops.append(line[0])
            if not (line[2] in stops):
                stops.append(line[2])
            # print(stops.index(line[0]), line[0])
            lens[stops.index(line[0])][stops.index(line[2])] = int(line[-1])
            result.append(line)
            line = file.readline()
    # for i in result:
    #   print(*i)
    # print(result)
    # print(stops)
    # print(len(stops))
    # print(len(stops))
    # for i in lens:
    #    print(*i)
    # print(lens)
    return stops, lens
    # return result

# filename = "0_CREATE/test.txt"
# filename = "0_CREATE/test2.txt"
# filename = "0_CREATE/stations.txt"
# lines = lines(filename)
# print(lines)

# 0_CREATE/test.txt
# 0_CREATE/stations.txt