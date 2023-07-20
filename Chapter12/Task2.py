# Задание: Создайте класс Circle с методом area, подсчитывающим и возвращающим площадь круга. Затем создайте объект
# Circle, вызовите в нём метод area и выведите результат. Воспользуйтесь функцией pi из встроенного в Python модуля
# math.

import math


class Circle:
    def __init__(self, r):
        """
        Инициализирует экземпляр класса Circle (Круг)
        :param r: int, float - (radius) радиус
        """
        self.radius = r

    def area(self):
        """
        Подсчитывает и возвращает площадь круга.
        :return: (float) Площадь круга по формуле pi*r^2
        """
        return math.pi * (self.radius * self.radius)


circle1 = Circle(5)
print(circle1.area())

