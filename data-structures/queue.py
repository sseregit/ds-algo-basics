class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.rear = -1
        self.front = -1

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == self.capacity - 1

    def enqueue(self, value):
        if not self.isFull():
            self.rear += 1
            self.array[self.rear] = value
        else:
            print("Overflow")

    def dequeue(self):
        if not self.isEmpty():
            self.front += 1
            return self.array[self.front]
        else:
            print("Underflow")

    def size(self):
        return self.rear - self.front

    def display(self):
        for i in range(self.front + 1, self.rear + 1):
            print(self.array[i], " ", end="")

q1 = Queue(10)

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)
q1.enqueue(90)
q1.enqueue(100)

q1.display()

q1.enqueue(110)

q1.dequeue()
q1.dequeue()

q1.display()

q1.enqueue(110)