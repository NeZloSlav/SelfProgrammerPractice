# Задание: Напишите программу с двумя функциями.
# Первая функция должна принимать в качестве параметра целое число и возвращать результат деления этого числа на 2.
# Вторая функция должна принимать в качестве параметра целое число и возвращать результат умножения этого числа на 4.
# Вызовите первую функцию, сохраните результат в переменной и передайте её в качестве параметра во вторую функцию.

def division_on_two(num: int):
    """
    Returns num divided on 2
    :param num: int
    :return: float or int division a num by 2
    """
    return num // 2


def multiply_on_four(num: int):
    """
    Returns num multiplied in 4
    :param num: int
    :return: int multiplication a num by 4
    """
    return num * 4


number = int(input('Enter the number: '))
result1 = division_on_two(number)
result2 = multiply_on_four(result1)
print(result1)
print(result2)
