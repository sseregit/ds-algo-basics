class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = value
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            print("Stack Underflow")

    def size(self):
        return self.top + 1

    def display(self):
        for i in range(self.top + 1):
            print(self.array[i], "", end="")


def check_brackets(str, length):
    s1 = Stack(length)
    for ch in str:
        if ch == '(':
            s1.push(ch)
        elif ch == ')':
            if s1.isEmpty():
                return False
            else:
                s1.pop()
        else:
            pass
    return s1.isEmpty()


str = input("수식 입력:")
print("괄호 짝맞추기 결과: ", check_brackets(str, len(str)))
