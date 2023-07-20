# Задание: Напишите функцию, которая преобразовывает строку в тип данных float и возвращает результат.
# Используйте обработку исключений, чтобы перехватить возможные исключения.

def str_to_float(line):
    """
    Returns str line converted to a float
    :param line: str
    :return: line converted to a float
    """
    try:
        return float(line)
    except:
        return f"You can't convert to float this ('{line}')"


print(str_to_float('Hello'))
print(str_to_float('12.3'))
