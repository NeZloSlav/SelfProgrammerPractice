# Задание: Напишите программу, которая будет выводить разные строки в зависимости от того, какое целое число было вами
# присвоено переменной age, содержащейся в этой программе.

age = int(input('Enter the age: '))

if age <= 18:
    print("Oou, you very small)")
elif age > 18 <= 35:
    print("Oou, you very sad(")
else:
    print("Hello, dinosaur!")
    