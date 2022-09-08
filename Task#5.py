# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# **********************************************************************

import math

def get_coordinate():
    while True:
        try:
            num = int(input("Введите координату точки: "))
            return num
        except ValueError:
            print("Вы ввели не число. Повторите ввод")
            
x1 = get_coordinate()
y1 = get_coordinate()
x2 = get_coordinate()
y2 = get_coordinate()

print(f"Расстояние между точками A({x1},{y1}) и B({x2},{y2}) \
равно {round(math.sqrt((x2-x1)**2 + (y2-y1)**2),2)}")