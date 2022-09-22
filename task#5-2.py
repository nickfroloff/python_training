# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# **************************************************************************************************

from random import *
import os

welcome_text = ('Хочешь сиграть в игру?')
print(welcome_text)

message = ['сколько берешь конфет?', 'в этот раз возьмешь', 'твой выбор', 'ставка',]

def player_vs_player():
    candies_total = 2021
    max_take = 28
    count = 0
    player_1 = input('\n Игрок №1: ')
    player_2 = input('\n Игрок №2: ')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f' {lucky} ходит первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\n взять можно не более {max_take} конфет {lucky}!: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\n осталось {candies_total}')
            count = 1
        else:
            print('Конфет больше нет')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\n взять можно не более {max_take} конфет {loser},!: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\n осталось {candies_total}')
            count = 0
        else:
            print('Конфет больше нет')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')


player_vs_player()


def player_vs_bot():
    candies_total = 2021
    max_take = 28
    player_1 = input('\nКак твоё имя, человек?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print(f'\n {player_1} и {player_2} начинаем игру\n')
    
    lucky = randint(-1, 0)

    print(f'Первым ходит {players[lucky+1]}')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \n осталось {candies_total} конфет. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\n Ходит {players[lucky%2]} \n осталось {candies_total} {choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nможно взять не больше {max_take} конфет!: '))
        candies_total = candies_total - step

    print(f'осталось {candies_total} конфет \n Победил {players[lucky%2]}')

player_vs_bot()