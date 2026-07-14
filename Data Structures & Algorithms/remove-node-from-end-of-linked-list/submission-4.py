# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        dummy = tail = ListNode(0, head)

        for i in range(n):
            tail = tail.next
        
        curr = dummy
        while tail.next:
            curr = curr.next
            tail = tail.next
        
        curr.next = curr.next.next
        return dummy.next