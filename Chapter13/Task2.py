# Задание: В классе Square определите метод change_size, позволяющий передавать ему число, которое увеличивает
# или уменьшает (если оно отрицательное) каждую сторону объекта Square на соответствующее значение.

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

    def change_size(self, n):
        """
        Изменяет сторону квадрата на число n.
        :param n: int, float - (number) число.
        """
        self.side = self.side + n
