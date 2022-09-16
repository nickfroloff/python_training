# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
#**********************************************************************

with open('file_1.txt', 'w') as file:
    file.write('2*x^2 + 5*x^5')
with open('file_2.txt', 'w') as file:
    file.write('23*x^4 + 9*x^6')

with open('file_1.txt','r') as file:
    file_1 = file.readline()
    poly_1 = file_1.split()


with open('file_2.txt','r') as file:
    file_2 = file.readline()
    poly_2 = file_2.split()

print(f'{poly_1}+{poly_2}')

with open('file with sum.txt', 'w') as file:
    file.write(f'{poly_1}+{poly_2}')