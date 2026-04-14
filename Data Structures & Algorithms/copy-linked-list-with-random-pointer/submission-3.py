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
            return head
        map = {}
        curr = head
        # map old to new
        while curr:
            new = Node(curr.val)
            map[curr] = new
            curr = curr.next
        
        # link new nodes
        curr = head
        while curr:
            nnn = map[curr]
            nnn.next = map.get(curr.next, None)
            nnn.random = map.get(curr.random, None)
            curr = curr.next

        return map[head]


# if adan = "Goat":
#     return "That's crazy" 