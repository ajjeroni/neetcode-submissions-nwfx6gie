# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def find_mid(head):
            slow = fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow 
        def reverse_list(head):
            prev, curr = None, head
            while curr:
                ahead = curr.next
                curr.next = prev
                prev = curr
                curr = ahead
            return prev

        if not head or not head.next:
            return None
        
        l,r = head.next,reverse_list(find_mid(head))
        head.next = r
        while l.next:
            r_ahead = r.next
            r.next = l
            r = r_ahead

            l_ahead = l.next
            l.next = r
            l = l_ahead
            