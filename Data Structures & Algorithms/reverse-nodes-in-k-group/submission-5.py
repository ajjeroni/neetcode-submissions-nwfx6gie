# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 1:
            return head

        def reverseList(node):
            prev = None
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            

        dummy = curr = ListNode()
        dummy.next = head

        before = dummy
        curr = curr.next

        while curr:

            kCheck = curr
            kValue = k
            while kValue > 1 and kCheck:
                kCheck = kCheck.next
                kValue -= 1
            
            if not kCheck:
                break
            

            after = kCheck.next
            kCheck.next = None
            reverseList(curr)

            before.next = kCheck

            curr.next = after

            before = curr
            curr = after
            
        return dummy.next























