# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# ************************************************************************

a = int(input('Введите число: '))
list =[]
for i in range(1,a+1):
    if(a%i==0):
      list.append(i)
print('Простые множители для числа', f'{a} = {list}')