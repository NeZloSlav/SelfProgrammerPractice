# Задание: Создайте класс Shape. Определите в нём метод what_i_am, который при вызове выводит строку "Я - фигура.".
# Измените ваши классы Rectangle и Square из предыдущих заданий для наследования Shape, создайте объекты Square и
# Rectangle и вызовите в них новый метод.

class Shape:
    def __init__(self, w, l):
        """
        Инициализирует экземпляр класса Shape (Фигура).
        :param w: int, float - (width) ширина.
        :param l: int, float - (length) длина.
        """
        self.width = w
        self.length = l

    def what_i_am(self):
        """
        Выводит название объекта.
        """
        print("Я - фигура.")


class Rectangle(Shape):
    def calculate_perimeter(self):
        """
        Подсчитывает и возвращает периметр прямоугольника.
        :return: (int, float) Периметр по формуле (a+b)*2
        """
        return (self.length + self.width) * 2

    def what_i_am(self):
        print("Я - прямоугольник.")


class Square(Shape):
    def calculate_perimeter(self):
        """
        Подсчитывает и возвращает периметр квадрата.
        :return: (int, float) Периметр по формуле a*4.
        """
        return self.width * 4

    def change_size(self, n):
        """
        Изменяет стороны квадрата на число n.
        :param n: int, float - (number) число.
        """
        self.width = self.width + n
        self.length = self.length + n

    def what_i_am(self):
        print("Я - квадрат.")


rect = Rectangle(1, 2)
sqr = Square(2, 2)
rect.what_i_am()
sqr.what_i_am()

