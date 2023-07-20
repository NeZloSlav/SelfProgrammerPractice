# Задание: Создайте классы Horse и Rider. Используйте композицию, чтобы смоделировать лошадь с всадником на ней.

class Horse:
    def __init__(self, age, breed, rider):
        """
        Инициализирует экземпляр класса Horse (Лошадь).
        :param age: int - возраст
        :param breed: str - порода
        :param rider: Rider() - наездник
        """
        self.age = age
        self.breed = breed
        self.rider = rider


class Rider:
    def __init__(self, name):
        """
        Инициализирует экземпляр класса Rider (Наездник).
        :param name: str - имя
        """
        self.name = name


rider = Rider("Вова")
horse = Horse(15, "Мустанг", rider)

print(horse.rider.name)