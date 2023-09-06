# Этап 1: Длины кратчайших путей
def stage1(matrix, start=0):
    n = len(matrix)                         # Количество вершин
    inf = 10e+9                             # Переменная бесконечности
    shortest_length = [inf] * n             # Массив кратчайших длин
    passed_indexes = [i for i in range(n)]  # Масссив вершин, которые ещё не минимальны

    current = start     # Текущая вершина

    passed_indexes.remove(current)   # начальной вершине ставим звёздочку
    shortest_length[current] = 0     # начальной вершине ставим значение ноль 

    while len(passed_indexes) != 0:
        # Обновление массива кратчайших длин
        for i in range(len(matrix[current])):
            if ((i) in passed_indexes and (matrix[current][i] != 0)):
                shortest_length[i] = min(shortest_length[i], shortest_length[current] + matrix[current][i])
        
        # Нахождение новой текущей вершины
        rees = {j: shortest_length[i] for i in range(len(shortest_length)) for j in passed_indexes if j == i}
        current = [key for key in passed_indexes if rees[key] == min(rees.values())][0]

        passed_indexes.remove(current)
    
    return shortest_length    

# Этап 2: Построение кратчайшего пути
def stage2(shortest_length, matrix, stop, start):

    # Транспонирование матрицы
    def transposed_matrix(matrix):
        result = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(len(result)):
            for j in range(len(result[0])): 
                result[i][j] = matrix[j][i]
        return result

    transposed_stops = transposed_matrix(matrix)

    def route(matrix, start, stop):
        for i in range(len(matrix[start])):
            if ((matrix[start][i] != 0) and (shortest_length[start] == (shortest_length[i] + matrix[start][i]))):
                if i == stop:
                    return [i]
                else:
                    return [i] + route(matrix, i, stop)

    return ([start + 1] + [i + 1 for i in route(transposed_stops, start, stop)])[::-1]

# Чтение файла, заполнения матрица весов графа
def lines(filename):
    result = []
    stops = [] # порядок вхождения станций
    n = 169
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
            print(stops.index(line[0]), line[0])
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

# filename = "1_INSERT/test.txt"
# filename = "1_INSERT/test2.txt"
# filename = "1_INSERT/stations.txt"
# lines = lines(filename)
# print(lines)

# 1_INSERT/test.txt
# 1_INSERT/stations.txt