# Задание: Напишите программу, которая запрашивает у пользователя его вес, любимый цвет или актёра,
# и возвращает результат из словаря, созданного в предыдущем задании.

dictionary = {
    'Age': 18,
    'Height': 185,
    'Favourite actor': 'Tom Cruise'
}

answer = input("""What you want to know?
1) Age
2) Height
3) Favourite actor
Enter the number: """)

match answer:
    case '1':
        print(dictionary['Age'])
    case '2':
        print(dictionary['Height'])
    case '3':
        print(dictionary['Favourite actor'])
    case _:
        print('You enter the wrong data!')
