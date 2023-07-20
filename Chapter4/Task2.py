# Задание: Создайте функцию, которая принимает строку в качестве параметра и возвращает её.

def re_string(line):
    """
    Returns the same string as in the parameter
    :param line: str
    :return: line converted to a string type
    """
    return str(line)


line1 = input('Enter any line: ')
print(re_string(line1))
