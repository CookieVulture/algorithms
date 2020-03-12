class node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SortLL:
    def __init__(self):
        self.head = None

    def sort_insert(self, data):
        data = node(data)
        if self.head is None:
            data.next = self.head
            self.head = data
            return
        elif self.head.value >= data.value:
            data.next = self.head
            self.head = data
            return
        start = self.head
        while (start.next is not None) and (data.value > start.next.value):
            start = start.next
        data.next = start.next
        start.next = data

    def push(self, data):
        data = node(data)
        data.next = self.head
        self.head = data

    def printf(self):
        start = self.head
        while start:
            print(start.value, end=" ")
            start = start.next


test1 = SortLL()
test1.push(2)
test1.sort_insert(4)
test1.sort_insert(1)
test1.printf()
