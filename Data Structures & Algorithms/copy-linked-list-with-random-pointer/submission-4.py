"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        curr = head
        while curr:
            new = Node(curr.val, curr.next)
            curr.next = new
            curr = new.next

        curr = head
        while curr:
            new = curr.next
            if curr.random:
                new.random = curr.random.next
            curr = new.next

        # A -> A' -> B -> B' -> C -> C'

        # A -> B -> C
        # A' -> B' -> C'
        curr = head
        deep = head.next
        while curr:
            new = curr.next
            curr.next = new.next

            if new.next:
                new.next = curr.next.next

            curr = curr.next

        return deep 










