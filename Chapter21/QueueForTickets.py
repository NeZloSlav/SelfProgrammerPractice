# Задание: Моделирование ситуации, когда люди стоят в очереди за билетами на фильм.

import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tickets_sold = []

        for i in range(10):
            pq.enqueue("кинофанат " + str(i))

        t_end = time.time() + till_show
        now = time.time()

        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tickets_sold.append(person)

        return tickets_sold


queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)
