# Задание: Алгоритм, выясняющий, являются ли два слова анаграммами друг друга.

def anagram(word_1, word_2):
    word_1 = word_1.lower()
    word_2 = word_2.lower()
    return sorted(word_1) == sorted(word_2)


print(anagram("тАпок", "Капот"))
