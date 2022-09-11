# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#***************************************************************************************************

def get_number(input_string):
    while True:
        try:
            num=int(input(input_string))
            return num
        except ValueError:
            print("Попробуйте еще раз")
            
number=get_number("Введите целое число N: ")

for i in range(number):
    if i==0:
        fact=[1]
    else:
        fact.append(fact[i-1]*(i+1))
print(f"набор произведений чисел от 1 до {number} ={fact}")