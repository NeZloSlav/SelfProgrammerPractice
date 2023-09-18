# Задание: Написание весёлой песни с помощью рекурсии.

def bottles_of_beer(bob):
    """
    Печатает текст песенки по 99 бутылок пива.
    :param bob: int
    :return:
    """

    if bob < 1:
        print("Нет бутылок пива на стене. Нет бутылок пива.")
        return

    tmp = bob
    bob -= 1
    print(f"{tmp} бутылок пива на стене. {tmp} бутылок пива.\n"
          f"Возьми одну,пусти по кругу, {bob} бутылок пива на стене.")
    return bottles_of_beer(bob)


bottles_of_beer(29)
