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
        if not head:
            return None
        
        curr = head
        while curr:
            tmp = curr.next
            curr.next = Node(curr.val, tmp)
            curr = tmp
        curr = head
        newHead = head.next
        while curr:
            tmp = curr.next.next
            copy = curr.next
            copy.random = curr.random.next if curr.random else None
            curr = tmp
        curr = head
        while curr:
            tmp = curr.next.next
            copy = curr.next
            copy.next = tmp.next if tmp else None
            curr.next = tmp
            curr = tmp
        return newHead










