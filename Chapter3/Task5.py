# Задание: Напишите программу, которая принимает две переменные, делит одну на другую и выводит частное.

num1 = float(input('Enter the 1st number: '))
num2 = float(input('Enter the 2nd number: '))

if num2 == 0:
    print("You can't divide on zero.")
else:
    print("Result is " + str(num1 / num2))
