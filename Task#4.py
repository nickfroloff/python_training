# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *********************************************************************

def get_quarter():
    while True:
        try:
            num = int(input("Введите номер четверти плоскости координат от 1 до 4): "))
            while ((num < 1) or (num>4)):
                print("Введите число от 1 до 4")
                num = get_quarter()            
            return num
        except ValueError:
            print("Попробуйте ввести число еще раз.")
            
def quarter(num):
    if (num==1): print("диапазон возможных координат точек в этой четверти: Х от 0 до ∞ и Y от 0 до ∞")
    elif (num==2): print("диапазон возможных координат точек в этой четверти: X от -∞ до 0 и Y от 0 до ∞")
    elif (num==3): print("диапазон возможных координат точек в этой четверти: X от -∞ до 0 и Y от -∞ до 0")
    elif (num==4): print("диапазон возможных координат точек в этой четверти: Х от 0 до ∞ и Y от -∞ до 0")

num = get_quarter()

quarter(num)