# Задание: Напишите программу, которая будет выводить одно сообщение, если значение переменной меньше или равно 10,
# или другое, если переменная больше 10, но меньше или равна 25, и третье сообщение, если переменная больше 25.

number = int(input('Enter the number: '))

if number <= 10:
    print('Number equal to 10 or smaller.')
elif number > 10 <= 25:
    print('Number is bigger than 10 and equal to 25 or smaller.')
else:
    print('Number is bigger than 25.')
