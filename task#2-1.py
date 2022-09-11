# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# ************************************************************************************************

def get_number(input_string):
    while True:
        try:
            num=float(input(input_string))
            return num
        except ValueError:
            print("Попробуйте еще раз")
            
number=get_number("Введите число: ")
str_number=str(number)
sum_digit=0

for i in range(len(str_number)):
    if str_number[i].isdigit():
        sum_digit=sum_digit+int(str_number[i])

print(f"Сумма всех цифр числа {number}={sum_digit}")
    
