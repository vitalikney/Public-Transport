def lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return lines

""" lines = lines("1_INSERT/test.txt")
print(lines) """

line = 'Краснопресненская, 5, Баррикадная, 7, 3'
line = line.split(', ')
if line[-1].find("\n") != -1:
    line[-1] = line[-1][:line[-1].find("\n")]
print(line)
# print(line[-1][:line[-1].find("\n")])
