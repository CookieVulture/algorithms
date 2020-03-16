# Reverse the linked list in pairs
# Ex. Input - 1->2->3->4->X     Output - 2->1->4->3->X


class node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Iterative
# Time Complexity: O(n)
# Space Complexity: O(1)

class LinkedList:
    def __init__(self):
        self.head = None

    def pairiter(self):
        start = self.head
        if start is None:
            return
        while start is not None and start.next is not None:
            start.data, start.next.data = start.next.data, start.data
            start = start.next.next

