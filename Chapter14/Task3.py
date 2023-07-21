# Задание: Напишите функцию, которая принимает два объекта в качестве параметров и возращает True, если они являются
# одним и тем же объектом, и False в противном случае.

def is_equal(o1, o2):
    """
    Проверяет, являются ли две переменные одним и тем же объектом.
    :param o1: (object) 1-ый объект.
    :param o2: (object) 2-ой объект.
    :return: True, если являются, False, если нет.
    """
    return a is b


a = None
b = 0
print(is_equal(a, b))  # False

c = None
d = c
print(is_equal(c, d))  # True
