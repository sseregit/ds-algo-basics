class SList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.link = None

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def getNode(self, p):
        if p < 0 or p > self.size:
            return None

        curr = self.head
        for i in range(p):
            curr = curr.link
        return curr

    def getEntry(self, p):
        node = self.getNode(p)
        if node == None:
            return node
        else:
            return node.data

    def insert(self, data, p):
        new_node = self.Node(data)

        before = self.getNode(p - 1)
        if before == None:
            new_node.link = self.head
            self.head = new_node
        else:
            new_node.link = before.link
            before.link = new_node
        self.size += 1

    def delete(self, p):
        if self.isEmpty():
            print('Underflow')
            return
        elif self.size < p:
            print('No Data')
            return
        elif p == 0:
            self.head = self.head.link
        else:
            before = self.getNode(p-1)
            curr = self.getNode(p)
            before.link = curr.link
        self.size -= 1

    def search(self, data):
        curr = self.head
        for i in range(self.size):
            if data == curr.data:
                return i
            curr = curr.link
        return False

    def display(self):
        curr = self.head
        for i in range(self.size):
            print(curr.data, end = ' -> ')
            curr = curr.link
        print("None")

a = SList()
a.display()
a.insert(10, 0)
a.display()
a.insert(20, 0)
a.display()
a.insert(30, 1)
a.display()
a.insert(40, 2)
a.display()

print(f"연결리스트의 노드 갯수 : {a.size}")

a.delete(0)
a.display()
a.delete(2)
a.display()
a.delete(3)
a.display()

print(f"30이 들어있는 노드의 위치 : {a.search(30)}")
print(f"40이 들어있는 노드의 위치 : {a.search(40)}")
print(f"10이 들어있는 노드의 위치 : {a.search(10)}")