# Задание: Создайте класс Hexagon с методом calculate_perimeter, подсчитывающим и возвращающим периметр шестиугольника.
# Затем создайте объект Hexagon, вызовите в нём calculate_perimeter и выведите результат.

class Hexagon:
    def __init__(self, a, b, c, d, e, f):
        """
        Инициализирует экземпляр класса Hexagon (Шестиугольник)
        :param a: int, float - 1-ая сторона
        :param b: int, float - 2-ая сторона
        :param c: int, float - 3-ья сторона
        :param d: int, float - 4-ая сторона
        :param e: int, float - 5-ая сторона
        :param f: int, float - 6-ая сторона
        """
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d
        self.side5 = e
        self.side6 = f

    def calculate_perimeter(self):
        """
        Подсчитывает и возвращает периметр шестиугольника.
        :return: (int, float) Периметр шестиугольника.
        """
        return self.side1 + self.side2 + self.side3 + self.side4 + self.side5 + self.side6


hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())
