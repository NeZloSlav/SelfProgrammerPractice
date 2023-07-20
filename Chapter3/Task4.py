# Задание: Напишите программу, которая выполняет деление двух чисел и выводит остаток.

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

if number2 == 0:
    print("You can't divide on zero.")
else:
    print(f"Result ({number1 // number2}), remains ({number1 % number2})")

