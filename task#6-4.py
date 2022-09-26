# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
#*********************************

import math
def get_number(input_string, start=None, stop=None) -> int:
            num = int(input(input_string))
            return num
num = get_number("Введите количество членов последовательности: ",1)
array = [int(math.pow((-1), i)*3**i) for i in range(num)]
print(f'\nСписок из {num} членов последовательности: {array}\n')