# Задание: Умножьте все числа в списке [8, 19, 148, 4] на все числа в списке [9, 1, 33, 83] и поместите результаты в
# третий список.

array1 = [8, 19, 148, 4]
array2 = [9, 1, 33, 83]
array3 = []

for i in array1:
    for j in array2:
        array3.append(i * j)

for i in array3:
    print(i, end=" ")
