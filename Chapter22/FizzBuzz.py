# Задание: Решение задания с собеседования FizzBuzz. Когда число кратно 3-ём, выводится Fizz, когда 5-ти, выводится Buzz, когда кратно
# и трём, и пяти, тогда FizzBuzz, и если не кратно ни одному из чисел, то выводится данное число.


def fizz_buzz(array):
    for number in array:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


my_array = []
for i in range(0, 20):
    my_array.append(i)

fizz_buzz(my_array)
