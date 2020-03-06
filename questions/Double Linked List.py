import gc

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def printf(self):
        size = 0
        tempe = self.head
        while tempe is not None:
            print(tempe.data, end=" ")
            tempe = tempe.next
            size += 1
        print()
        print(size)

    def push(self, value):
        value = node(value)
        value.next = self.head
        if self.head is not None:
            self.head.previous = value
        self.head = value

    def insert(self, value, position):
        start = self.head
        if position <= 1:
            self.push(value)
            return
        while start is not None:
            if position == 1:
                value = node(value)
                value.next = start.next
                value.previous = start
                start.next = value
                value.next.previous = value
                break
            position -= 1
            start = start.next

    def remove(self, value):
        if self.head is None or value is None:
            return
        if self.head == value:
            self.head = self.next
        if value.next is not None:
            value.next.previous = value.previous
        if value.previous is not None:
            value.previous.next = value.next
        gc.collect()

test1 = DoubleLinkedList()
test1.head = node(100)
test1.head.next = node(200)
test1.head.next.next = node(300)
test1.push(40)
print(test1.head.next.previous.data == 40)
test1.insert(250,3)
test1.remove(test1.head.next)
test1.printf()
