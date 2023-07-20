# Задание: Создайте классы Rectangle и Square с методом calculate_perimeter, вычисляющим периметр фигур, которые эти
# классы представляют. Создайте объекты Rectangle и Square, вызовите в них метод.

class Rectangle:
    def __init__(self, w, l):
        """
        Инициализирует экземпляр класса Rectangle (Прямоугольник).
        :param w: int, float - (width) ширина.
        :param l: int, float - (length) длина.
        """
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        """
        Подсчитывает и возвращает периметр прямоугольника.
        :return: (int, float) Периметр по формуле (a+b)*2
        """
        return (self.length + self.width) * 2


class Square:
    def __init__(self, a):
        """
        Инициализирует экземпляр класса Square (Квадрат).
        :param a: int, float - (side) сторона.
        """
        self.side = a

    def calculate_perimeter(self):
        """
        Подсчитывает и возвращает периметр квадрата.
        :return: (int, float) Периметр по формуле a*4.
        """
        return self.side * 4


rect = Rectangle(2, 4)
sqr = Square(2)
print(rect.calculate_perimeter())
print(sqr.calculate_perimeter())

