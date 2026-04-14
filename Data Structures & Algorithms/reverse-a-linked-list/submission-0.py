# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None 
        curr = head
        post = head.next

        while post:
            head.next = prev
            prev = head
            head = post
            post = head.next

        head.next = prev    

        return head