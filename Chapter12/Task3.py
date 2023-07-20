# Задание: Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь треугольника. Затем создайте
# объект Triangle, вызовите в нём area и выведите результат.

import math


class Triangle:
    def __init__(self, a, b, c):
        """
        Инициализирует экземпляр класса Triangle (Треугольник)
        :param a: int, float - 1-ая сторона
        :param b: int, float - 2-ая сторона
        :param c: int, float - 3-ья сторона
        """
        self.side1 = a
        self.side2 = b
        self.side3 = c

    def area(self):
        """
        Подсчитывает и возвращает площадь треугольника по 3-м сторонам.
        :return: (int, float) Площадь треугольника по формуле Герона
        """
        p = (self.side1 + self.side2 + self.side3) / 2  # полупериметр

        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))


triangle1 = Triangle(3, 4, 5)
print(triangle1.area())
