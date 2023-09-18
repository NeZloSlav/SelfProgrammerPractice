# Задание: Написание алгоритма последовательного поиска элемента в массиве.

def seq_search(array, element):
    """
    Последовательно ищет элемент в массиве.
    :param array: list, tuple... - массив данных
    :param element: int, str... - элемент поиска
    :return: True - элемент найден, False - элемент не найден
    """
    for i in array:
        if i == element:
            return True
    return False


my_array = []
for i in range(1, 6):
    my_array.append(i)

print(seq_search(my_array, 2))
