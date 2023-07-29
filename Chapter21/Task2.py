# Задание: Используйте стек, чтобы создать новый список с элементами списка [1, 2, 3, 4, 5] в обратном порядке.

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
for i in range(1, 6):
    print(i)
    stack.push(i)

list1 = []

for i in range(len(stack.items)):
    list1.append(stack.pop())

print(list1)
