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
        if position <= 1:
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

    def delkey(self, value):
        start = self.head
        if start is not None:
            if start.data == value:
                self.head = start.next
                start = None
                return
        while start is not None:
            if start.data == value:
                break
            const = start
            start = start.next
        if start is None:
            print("Key invalid")
            return
        const.next = start.next
        start = None

    def delposition(self, position):
        if self.head is None:
            return
        start = self.head
        if position == 0:
            self.head = start.next
            start = None
            return
        for i in range(position-1):
            start = start.next
            if start is None:
                break
        if start is None:
            return
        if start.next is None:
            return
        temp = start.next.next
        start.next = None
        start.next = temp

    def dellist(self):
        start = self.head
        while start:
            temp = start.next
            del start.data
            start = temp

    def search(self, start, value):
        if not start:
            return False
        if start.data == value:
            return True
        return self.search(start.next, value)

test1 = LinkedList()
test1.head = node(10)
test1.head.next = node(20)
test1.head.next.next = node(30)
test1.push(5)
test1.push(1)
test1.inserting(39, 3)
test1.delkey(39)
test1.delposition(3)
print(test1.search(test1.head, 10))
print(test1.search(test1.head, 110))
test1.printf()
