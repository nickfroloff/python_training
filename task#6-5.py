# 5- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*****************************************************************************


from random import randint
def get_number(input_string, start=None, stop=None) -> int:
            num = int(input(input_string))
            return num

num = get_number("Введите количество символов в массиве: ",1)
min_n = 0
max_n = 20

list_numbers = [randint (min_n,max_n) for _ in range(num)]
new_list = [list_numbers[i]*list_numbers[num-1-i] for i in range(num//2)] 
if num%2 != 0: 
    new_list.append(list_numbers[num-1-int(num/2)]**2)
print(f'\nИз списка: {list_numbers} получается список: {new_list}\n')