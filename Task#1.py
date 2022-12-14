# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
# ***********************************************************************************

def week_day ():
    while True:
        try:
            num = int(input("Введите цифру, обозначающую день недели (1-7): "))
            return num
        except ValueError:
            print("Попробуйте еще раз!")

week_day = week_day()
if (0 < week_day < 8):
    if (week_day == 6 or week_day == 7):
        print("-> да (выходной) ")
    else:
        print("-> нет (рабочий день) ")