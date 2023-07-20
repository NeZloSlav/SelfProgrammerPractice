# Задание: Напишите функцию, которая принимает число в качестве ввода, возводит его в квадрат и возвращает.

def square(x):
    """
    Returns square of number x
    :param x: int or float
    :return: int or float type square of the number x
    """
    return x * x


num = float(input('Enter the number for squaring: '))
print(square(num))
