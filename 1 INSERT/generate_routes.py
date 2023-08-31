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


# stops = [
#     [0, 7, 2, 0, 13, 0],
#     [0, 0, 0, 0, 4, 0],
#     [0, 2, 0, 8, 0, 11],
#     [0, 0, 0, 0, 0, 5],
#     [0, 0, 0, 3, 0, 1],
#     [2, 0, 0, 0, 0, 0]
# ]

stops = [
    [0, 4, 5, 0, 0],
    [4, 0, 3, 5, 0],
    [5, 3, 0, 7, 8],
    [0, 5, 7, 0, 4],
    [0, 0, 8, 4, 0]
]

all_routes = []
for i in range(len(stops)):
    shortest_length = stage1(stops, i)
    for j in range(len(stops)):
        if (i != j):
            routes = stage2(shortest_length, stops, i, j)
            all_routes.append(routes)
print(len(all_routes))
print(all_routes)
# print(shortest_length, "\n")
# shortest_length = stage1(stops, 5)
# print(shortest_length)

