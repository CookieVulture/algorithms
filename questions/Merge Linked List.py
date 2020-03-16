# Merge two sorted linked list
# Recursion
# Time Complexity: O(n+m),where n and m are lengths of two lists

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

def merge_list(headA, headB):
    if headA is None:
        return headB
    if headB is None:
        return headA

    if headA.data < headB.data:
        headA.next = merge_list(headA.next, headB)
        return headA

    else:
        headB.next = merge_list(headB.next, headA)
        return headB



