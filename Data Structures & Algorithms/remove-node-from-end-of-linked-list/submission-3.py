# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # spacer
        dummy = back = front = ListNode(-1,head)
        
        for _ in range(n):
            front = front.next
        
        while front.next:
            front = front.next
            back = back.next
        
        tmp = back.next
        back.next = back.next.next
        tmp.next = None
        
        return dummy.next

            