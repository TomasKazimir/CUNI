class CircularQueue:
    def __init__(self, size: int):
        self.size = size
        self.stored = 0
        self.sum = 0
        self.array = [None] * size
        self.head = (size // 2)
        self.tail = (size // 2)


    def enqueue(self, value):
        self.array[self.tail % self.size] = value
        self.tail += 1
        self.tail %= self.size

        self.stored += 1
        self.sum += value
        if self.stored == self.size:
            self.resize()
        # print(value, ">", *[str(n).ljust(4) for n in self.array])

    def dequeue(self):
        value = self.array[self.head]
        self.array[self.head] = None
        self.head += 1
        self.head %= self.size

        self.stored -= 1
        self.sum -= value
        return value

    def count(self):
        return self.stored

    def resize(self):
        new_array = [None] * self.size * 2
        for i in range(self.size):
            new_array[i] = self.array[(self.head + i) % self.size]

        self.array = new_array
        self.head = 0
        self.tail = self.size
        self.size *= 2

        print("Resized to " + str(self.size) + " elements")

    def avg(self):
        return self.sum / self.stored

# cqueue = CircularQueue(2)
# for i in range(0, 63):
#     cqueue.enqueue(i)
#     # print(*cqueue.array, end=", avg = ")
#     # print(cqueue.avg())
