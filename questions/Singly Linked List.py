class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printf(self):
        size = 0
        tempe = self.head
        while tempe:
            print(tempe.data, end=" ")
            tempe = tempe.next
            size += 1
        print()
        print(size)

    def push(self, value):
        value = node(value)
        value.next = self.head
        self.head = value

    def inserting(self, value, position):
        start = self.head
        if position<=1:
            self.push(value)
            return
        while start is not None:
            if position == 1:
                value = node(value)
                value.next = start.next
                start.next = value
                break
            position -= 1
            start = start.next


test1 = LinkedList()
test1.head = node(10)
test1.head.next = node(20)
test1.head.next.next = node(30)
test1.push(5)
test1.inserting(39, 3)
test1.printf()
