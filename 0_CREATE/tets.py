stops = [1, 2, 3, 4, 5, 6, 7]
shortest_length = [13, 11, 63, 8, 3, 9, 5, 100]            # Массив кратчайших длин
passed_indexes = [1, 2, 3, 5, 6, 7]

rees = {j: shortest_length[i] for i in range(len(shortest_length)) for j in passed_indexes if j == i}
print(rees)
print(min(rees.values()))
print([key for key in passed_indexes if rees[key] == min(rees.values())][0])
# passed = [[1, 2, 4, 5], 
#           [4, 0, 6, 0],
#           [1, 3, 6, 9]]
# res = [[0] * len(passed)] * len(passed[0])
# # print(passed)

# # print(passed.index(4))

# # if not ((5 + 1) in stops):
# #     print(123)
# # else: 
# #     print(-1)


# def transposed_matrix(matrix):
#     result = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
#     for i in range(len(result)):
#         for j in range(len(result[0])): 
#             result[i][j] = matrix[j][i]
#     return result

# result = transposed_matrix(passed)
# for j in result:
#     print(j)
