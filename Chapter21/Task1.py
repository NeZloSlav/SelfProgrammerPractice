# Задание: Измените порядок символов строки "позавчера" при помощи стека.

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
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


stack = Stack()

for char in "позавчера":
    stack.push(char)

for item in range(len(stack.items)):
    print(stack.pop(), end="")
