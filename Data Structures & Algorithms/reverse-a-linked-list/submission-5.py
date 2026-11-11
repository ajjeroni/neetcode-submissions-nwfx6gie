# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        dummy = None
        tmp = head

        while head:
            head = head.next
            tmp.next = dummy
            dummy = tmp
            tmp = head

        return dummy
