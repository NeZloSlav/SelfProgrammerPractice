# Задание: Добавьте переменную square_list в класс Square так, чтобы всякий раз, когда вы создаёте новый объект
# Square, он добавлялся в список.

class Square:
    square_list = []

    def __init__(self, a):
        """
        Инициализирует экземпляр класса Square (Квадрат) и добавляет его в список.
        :param a: int, float - (side) сторона
        """
        self.side = a
        self.square_list.append(self.side)


square1 = Square(1)
square2 = Square(2)
print(Square.square_list)

