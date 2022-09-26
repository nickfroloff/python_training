# Найти расстояние между двумя точками пространства(числа вводятся через пробел)
#************************************************************************************

import math
numbers_str = input("Введите координаты точек (x, y) и (x1, y1) через пробел: ").split(" ")
numbers = list(map(float, numbers_str))
path = round(math.sqrt((numbers[2]-numbers[0])**2 + (numbers[3]-numbers[1])**2),2)
print(f"\nРасстояние между точками с координатами: ({numbers[0]}, {numbers[1]}) и ({numbers[2]}, {numbers[3]}) = {path}\n")