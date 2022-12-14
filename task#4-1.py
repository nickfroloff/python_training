# Вычислить число π (?) c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#**************************************************************************

import math

pi = math.pi
print('число π = ', pi)
d = 0.001
print(f'точность вычиления = {d}')
count = 0
while d < 1:
    count += 1
    d = d*10
print('Результат:', round(pi, count))