# Задание: игра "Пьяница".

from random import shuffle


class Card:
    suits = ["Пики", "Черви", "Бубны", "Крести"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]

    def __init__(self, v: int, s: int):
        self.value = v
        self.suit = s

    def __lt__(self, other_card):
        if self.value < other_card.value:
            return True
        elif self.value == other_card.value:
            if self.suit < other_card.suit:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other_card):
        if self.value > other_card.value:
            return True
        elif self.value == other_card.value:
            if self.suit > other_card.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return f"{self.values[self.value]} {self.suits[self.suit]}"


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))

        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        self.deck = Deck()
        self.plr1 = Player(input("Введите имя 1-го игрока: "))
        self.plr2 = Player(input("Введите имя 2-го игрока: "))

    def wins(self, winner):
        print(f"{winner} забирает карты.")

    def draw(self, p1n, p1c, p2n, p2c):
        print(f"{p1n} кладёт {p1c}, а {p2n} кладёт {p2c}.")

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return f"Выиграл {p1.name}!"
        elif p1.wins < p2.wins:
            return f"Выиграл {p2.name}!"
        else:
            return "Ничья!"

    def play_game(self):
        cards = self.deck.cards
        print("Поехали!")

        while len(cards) >= 2:
            m = "\nНажмите клавишу Х для выхода. Нажмите любую другую клавишу дя начала игры."
            response = input(m)
            if response == "Х" or response == "х":
                break

            self.plr1.card = self.deck.remove_card()
            self.plr2.card = self.deck.remove_card()

            self.draw(self.plr1.card, self.plr1.name, self.plr2.card, self.plr2.name)
            if self.plr1.card > self.plr2.card:
                self.plr1.wins += 1
                self.wins(self.plr1.name)
            else:
                self.plr2.wins += 1
                self.wins(self.plr2.name)

        print("Игра окончена. {}".format(self.winner(self.plr1, self.plr2)))


game = Game()
game.play_game()




