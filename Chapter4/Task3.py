# Задание: Напишите функцию, которая принимает три обязательных и два необязательных параметра.

def three_to_five_perimetr(a, b, c, d=0, e=0):
    """
    Returns a perimetr of the triangle or the quadrilateral or the pentagon
    :param a: int or float
    :param b: int or float
    :param c: int or float
    :param d: (optional) int or float
    :param e: (optional) int or float
    :return: Sum of all sides
    """
    return a + b + c + d + e


print(three_to_five_perimetr(1, 2, 3))
print(three_to_five_perimetr(1, 2, 3, 4))
print(three_to_five_perimetr(1, 2, 3, 4, 5))
