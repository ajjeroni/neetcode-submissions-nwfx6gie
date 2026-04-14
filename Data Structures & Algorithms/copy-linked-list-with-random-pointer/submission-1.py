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
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new 
            curr = new.next 

        curr, deep = head, head.next

        while curr:
            new = curr.next
            if curr.random:
                new.random = curr.random.next
            curr = new.next
        
        curr = head

        while curr:
            new = curr.next
            curr.next = new.next
            if new.next:
                new.next = new.next.next
            curr = curr.next



        return deep



























