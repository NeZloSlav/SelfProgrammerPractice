# Задание: Измените класс Square так, чтобы когда вы выводите объект Square, выводилось сообщение с длинами всех
# четырёх сторон фигуры. Например, если вы создадите квадрат при помощи Square(29) и осуществите вывод, Python должен
# вывести строку 29 на 29 на 29 на 29.

class Square:
    square_list = []

    def __init__(self, a):
        """
        Инициализирует экземпляр класса Square (Квадрат) и добавляет его в список.
        :param a: int, float - (side) сторона
        """
        self.side = a
        self.square_list.append(self.side)

    def __repr__(self):
        print("Размер {0} на {0} на {0} на {0}".format(self.side))


square1 = Square(3)
print(square1)
