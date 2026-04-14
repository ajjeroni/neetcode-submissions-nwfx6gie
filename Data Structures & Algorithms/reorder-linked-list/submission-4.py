# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def find_mid(head):
            behind = ahead = head
            while ahead and ahead.next:
                ahead = ahead.next.next
                behind = behind.next
            return behind 

        def reverse_list(head):
            prev = None
            curr = head
            while curr:
                ahead = curr.next
                curr.next = prev
                prev = curr
                curr = ahead
            return prev

        if not head:
            return None
        elif not head.next:
            return None

        l,r = head.next, reverse_list(find_mid(head))
        head.next = r
        while l.next:
            r_p = r.next
            r.next = l 
            r = r_p
            l_p = l.next
            l.next = r
            l = l_p








