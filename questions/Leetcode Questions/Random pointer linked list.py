# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.
# Space Complexity: O(n)


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        value = Node(value)
        value.next = self.head
        self.head = value


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        d = {}
        p = head
        while p:
            d[p] = Node(p.val)
            p = p.next
        p = head
        while p:
            d[p].next = d[p.next] if p.next in d else None
            d[p].random = d[p.random] if p.random in d else None
            p = p.next
