# Задание: Напишите программу с бесконечным циклом (с возможностью ввести букву Х, чтобы выйти) и списком чисел.
# При каждом переборе цикла предлагайте пользователю отгадать число из списка и сообщайте, правильно ли он отгадал.

num_array = [0, 2, 3, 6, 7, 8]

print("Enter the x if you want to quit.")
while True:
    answer = input("Guess a number in the list: ")
    answer_int = 0
    try:
        answer_int = int(answer)
    except:

        if answer == 'x' or answer == 'X':
            print('Okay. Goodbye!')
            break
        else:
            print("You entered the wrong data.")
            continue

    isGuessed = False
    for i in range(0, len(num_array)):
        if answer_int == num_array[i]:
            print("Yes, you did it!!!")
            isGuessed = True
            break

    if not isGuessed:
        print("No, you didn't guess")
