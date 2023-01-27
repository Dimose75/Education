from random import randint
from time import sleep
from colorama import *


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить вне границ игрового поля, пожалуйста проверьте правильность введенных координат"


class BoardUsedException(BoardException):
    def __str__(self):
        return "В эту клетку уже был произведен выстрел, пожалуйста выберите другую"


class BoardWrongShipException(BoardException):  # исключение для случая, когда корабли расставить не удалось
    pass


class Color:  # устанавливаем жирный шрифт
    BOLD = '\033[1m'


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    # dot1 = Dot(1, 2)
    # dot2 = Dot(1, 1)
    # print(dot1 == dot2)
    # False

    def __repr__(self):
        return f'{self.x, self.y}'
    # dot1 = Dot(1, 2)
    # print(dot1)
    # (1, 2)


class Ship:
    def __init__(self, bow, life, o):  # bow - длина корабля; life - кол-во жизней(точек); o - ориентация корабля
        self.bow = bow
        self.life = life
        self.o = o
        self.lives = life

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.life):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:  # горизонтальная ориентация
                cur_x += i

            elif self.o == 1:  # вертикальная ориентация
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots
    # s = Ship(Dot(1, 2), 4, 1)
    # print(s.dots)
    # [(5, 2), (5, 3), (5, 4), (5, 5)]

    def check_shoot(self, shot):  # метод проверки на попадание в корабль
        return shot in self.dots
    # s = Ship(Dot(1, 2), 4, 1)
    # print(s.check_shoot(Dot(3, 2)))
    # False


class Board:
    def __init__(self, hid=False, size=6):
        self.size = size  # размер игрового поля
        self.hid = hid  # атрибут для сокрытия кораблей

        self.count = 0  # количество пораженных кораблей

        self.field = [["O"] * size for _ in range(size)]  # сетка игрового поля, храним состояние

        self.busy = []  # список занятых точек
        self.ships = []  # список кораблей доски

    def add_ship(self, ship):
        for d in ship.dots:  # проверка не занята ли точка или находится ли точка в пределах поля
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()  # b.add_ship(Ship(Dot(1, 2), 4, 0)) b.add_ship(Ship(Dot(1, 1), 3, 0))
                # проверка работы исключения
        for d in ship.dots:  # расставляем квадратики во всех точках корабля и записываем точки в список занятых
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    # b = Board()
    # b.add_ship(Ship(Dot(1, 2), 4, 0))
    # print(b)
    # print(b.busy)
    # [(1, 2), (2, 2), (3, 2), (4, 2), (0, 1), (0, 2), (0, 3), (1, 1),
    #  (1, 3), (2, 1), (2, 3), (3, 1), (3, 3), (4, 1), (4, 3), (5, 1), (5, 2), (5, 3)]  также список точек котрые
    #  окружают корабль

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not (self.out(cur)) and cur not in self.busy:  # если точка не занята и не выходит за границы доски
                    if verb:  # параметр, определяющий нужно ли ставить точки
                        self.field[cur.x][cur.y] = "."  # ставим точку если точка занята
                    self.busy.append(cur)  # добавляем в список занятых точек

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"  # обозначение номера поля
        for i, row in enumerate(self.field):  # берем номер и клетку строки
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res
    # b = Board()
    # print(b)

    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))  # проверка находится ли точка за пределами доски

    def shot(self, d):  # метод выстрела по кораблю
        if self.out(d):  # если точка вне поля - выбрасываем исключение
            raise BoardOutException()

        if d in self.busy:  # если точка занята выбрасываем исключение
            raise BoardUsedException()

        self.busy.append(d)  # добавляем точку в список занятых точек

        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1  # уменьшаем жизнь корабля
                self.field[d.x][d.y] = "X"  # ставим Х - кораблю или его часть поражена
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "."  # если корабль не ранен и не уничтожен - ставим точку
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))  # генерируем точки
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input("  Ваш ход: ").split()  # запрос координат

            if len(cords) != 2:  # проверка, что введены 2 координаты
                print("   Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):  # проверка, что введены числа
                print("   Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)  # вычитаем 1, так как пользователю отображена индексация с единицы


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True  # спрячем корабли компьютера

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def two_board(self):  # метод для оптимизации игровых досок
        a = str(self.us.board)
        b = str(self.ai.board)
        for x, y in zip(a.split('\n'), b.split("\n")):
            print(x, '  ', y)
        return ""  # чтобы ничего не возвращать

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):  # бесконечный цикл для установки кораблей на доску
        lens = [3, 2, 2, 1, 1, 1, 1]  # список с длинами всех кораблей
        board = Board(size=self.size)  # создаем доску
        attempts = 0
        for life in lens:
            while True:
                attempts += 1  # прибавляем попытки
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), life, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print(Fore.BLACK + Back.WHITE + "----------------------------------------------------------")
        print(Color.BOLD + "                   Добро пожаловать в игру  ")
        print("                        МОРСКОЙ БОЙ    ")
        print("----------------------------------------------------------")
        print("                   Формат ввода: x y ")
        print("                   x - номер строки  ")
        print("                   y - номер столбца ")

    def loop(self):
        num = 0
        while True:
            print("-" * 58)
            print("  Доска пользователя:", "     ""     Доска компьютера:")
            print(Game.two_board(self))
            if num % 2 == 0:
                print("-" * 58)
                print("   Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-" * 20)
                print("   Ходит компьютер!")
                sleep(3)
                repeat = self.ai.move()
            if repeat:
                num -= 1  # сохраняем значение, чтобы ход остался у игрока

            if self.ai.board.count == 7:
                print("-" * 20)
                print("   Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("-" * 20)
                print("   Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
