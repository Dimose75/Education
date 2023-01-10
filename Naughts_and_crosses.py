from colorama import *
init()


def greet():
    print(Fore.CYAN + ' ' * 50, '|' + "Х" * 10, "Игра крестики - нолики v1.0", "0" * 9 + '|')
    print('Добро пожаловать, игра расчитана на двух игроков. Ввод осуществляется по очереди. '
          'Координаты ввода лежат в диапазоне от 0 до 2, в соответствии с игровым полем. Удачи! ')
    print()

greet()
board = [[" "] * 3 for i in range(3) ]
def board_():
    print('Игровое поле:')
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {board[i][0]} {board[i][1]} {board[i][2]}')



def ask_user():
    while True:
        move = input("Сделайте ваш ход: ").split()
        if len(move) != 2:
            print('Введите координаты в формате x y, повторите ваш ход')
            continue
        x, y = move
        if x.isdigit() != True or y.isdigit() != True:
            print('Введите числа, а не буквы! Повторите ваш ход')
            continue
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Введите координаты в диапазоне от 0 до 2, повторите ваш ход')
            continue
        if board[x][y] != " ":
            print('Введите другой вариант хода, клетка уже используется!, Повторите ваш ход')
            continue
        return x, y


def check_():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for comb in win_comb:
        list_ = []
        for c in comb:
            list_.append(board[c[0]][c[1]])
        if list_ == ["Х", "Х", "Х"]:
            print("Победа крестика!")
            return True
        if list_ == ["0", "0", "0"]:
            print("Победа нолика!")
            return True
    return False


counter = 0
while True:
    counter += 1
    board_()
    print()
    if counter % 2 != 0:
        print('Ход игрока "крестик"')
    else:
        print('Ход игрока "нолик"')
    x, y = ask_user()
    if counter % 2 != 0:
        board[x][y] = 'Х'
    else:
        board[x][y] = '0'
    if check_():
        break
    if counter == 9:
        print(" Ничья!")
        break



