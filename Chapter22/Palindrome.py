# Задание: Алгоритм, выясняющий, является ли слово палиндромом или нет.

def palindrome(word):
    word = word.lower()
    return word[::-1] == word


print(palindrome("Шалаш"))
