class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.rear = 0
        self.front = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, value):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = value
        else:
            print("Overflow")

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print("Underflow")

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def display(self):
        for i in range(self.front + 1, self.front+1+self.size()):
            print(self.array[i % self.capacity], " ", end="")

def josephus(n, k):

    q1 = CircularQueue(n + 1)

    for i in range(1, n+1):
        q1.enqueue(i)

    print("초기 값 입력: ", end=" ")
    print(q1.display())

    while q1.size() > 1:
        for i in range(k-1):
            j = q1.dequeue()
            q1.enqueue(j)
        print(f'\n 제외 : {q1.dequeue()} \n')
        q1.display()

    return q1.dequeue()

n = int(input("게임 사람 수 입력 : "))
k = int(input("제외될 번호 입력 : "))

print("남은 사람의 번호는 ", josephus(n, k))