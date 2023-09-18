# Задание: Алгоритм, вычисляющий количество вхождений символов.

def count_characters(string):
    count_dict = {}
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict


line = "ivubriufiwbfpwpenf[woefffborubwuobeiwnfenwpwnw"
print(count_characters(line))
