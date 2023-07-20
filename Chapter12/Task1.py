# Задание: Определите класс Apple с четырьмя переменными экземпляра, представляющими четыре свойства яблока.

class Apple:
    def __init__(self, w, c, t, p):
        """
        Инициализирует экземпляр класса Apple (Яблоко)
        :param w: int, float - (weight) вес
        :param c: str - (color) цвет
        :param t: str - (taste) вкус
        :param p: int, float - (price) цена
        """
        self.weight = w
        self.color = c
        self.taste = t
        self.price = p


apple1 = Apple(12, "красное", "сладкое", 20.00)
print(apple1.weight)
print(apple1.color)
print(apple1.taste)
print(apple1.price)
