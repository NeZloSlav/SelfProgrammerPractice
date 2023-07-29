# Задание: Создание структуры данных "стек" своими руками.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())
stack.push(1)
print(stack.is_empty())
stack.push(2)
stack.push(3)
print(stack.size())
stack.pop()
print(stack.size())
print(stack.items)
stack.pop()
stack.pop()
# Переворачиваем сс помощью стека слово ПРИВЕТ

reverse = ""
for char in "Привет":
    stack.push(char)

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)