class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLList:
    def __init__(self):
        self.head = None

    def push(self, value):
        value = Node(value)
        start = self.head

        value.next = self.head

        if self.head is not None:
            while start.next != self.head:
                start = start.next
            start.next = value
        else:
            value.next = value

        self.head = value

    def printf(self):
        size = 0
        start = self.head
        if self.head is not None:
            while True:
                print(start.data, end=" ")
                start = start.next
                size += 1
                if start == self.head:
                    break
        print()
        print(size)

    def insert(self, value):
        value = Node(value)
        current = self.head

        if current is None:
            self.head = value
            value.next = value
            return

        start = current
        while current.next != start:
            current = current.next

        current.next = value
        value.next = start


test1 = CLList()
test1.push(1)
test1.push(2)
test1.push(3)
test1.push(4)
test1.insert(5)
print(test1.head.next.next.next.next.next.data)
test1.printf()
