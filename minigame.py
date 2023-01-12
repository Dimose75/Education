#  minigame_
from random import *
from math import ceil
d = randint(1, 100)

def greet():
    print(" " * 66, 'Игра "Угадай число"')
    print("Добро пожаловать!\nПравила простые: вам будет предложено угадать загаданное число в диапазоне от 1 до 100. ")
    return greet
greet()


def is_valid(txt):
    if txt.isdigit and 1<= int(txt) <=100:
        return True
    else:
        return False


def restart():
    print("Сыграем еще раз? Введите 'да' или 'нет'")
    return input()


def game():
    counter = 0
    while True:
        print("Введите целое число:   ")
        num = input()
        counter += 1
        if is_valid(num):
            num = int(num)
        else:
            print("Попробуйте еще раз, введите целое число от 1 до 100")
        if num < d:
            print('Ваше число меньше загаданного, попробуйте еще раз')
        elif num > d:
            print('Ваше число больше загаданного, попробуйте еще раз')
        else:
            print(f'Вы угадали число с {counter} попытки!\nСпасибо за игру!')
            if restart() == "да":
                game()
            else:
                break

game()














# def check_user(number, left, right):
#     left = int(input(("Введите левую границу диапазона, например 1:  ")))
#     right = int(input(("Введите правую границу диапазона, например 100:  ")))
#     number = randint(left, right)
#     print(f"Отлично! Вам нужно будет угадать число в диапазоне {number}")
#
#
#
#
#
#
#
#     left = int(input(("Введите левую границу диапазона, например 1:  ")))
#     right = int(input(("Введите правую границу диапазона, например 100:  ")))
#     number = randint(left, right)
#     print(f"Отлично! Вам нужно будет угадать число в диапазоне {number}")



