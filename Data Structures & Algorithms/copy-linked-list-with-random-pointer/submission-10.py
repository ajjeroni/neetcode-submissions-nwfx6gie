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
            copy = Node(curr.val)
            curr.next = copy
            copy.next = tmp
            curr = tmp
        
        old = head
        while old:
            new = old.next
            oldRandom = old.random
            new.random = oldRandom.next if oldRandom else None
            old = new.next

        old = head
        newHead = old.next
        while old:
            new = old.next
            oldNext = new.next
            new.next = oldNext.next if oldNext else None
            old.next = oldNext
            old = oldNext

        return newHead
        
        