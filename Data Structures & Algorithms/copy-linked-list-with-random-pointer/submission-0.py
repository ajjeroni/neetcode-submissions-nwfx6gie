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

        OldToCopy = { None : None }

        curr = head

        while curr:
            new = Node(curr.val)
            OldToCopy[curr] = new
            curr = curr.next

        curr = head

        while curr:
            new = OldToCopy[curr]
            new.next = OldToCopy[curr.next]
            new.random = OldToCopy[curr.random]
            curr = curr.next
        
        return OldToCopy[head]

















