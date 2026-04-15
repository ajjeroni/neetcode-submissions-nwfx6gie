# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, curr, tail):
        head = curr
        tmp = tail
        while curr:
            curr = curr.next
            head.next = tmp
            tmp = head
            head = curr
        return tmp
    def getKth(self, curr, k):
        count = k
        while curr and count > 0:
            curr = curr.next
            count -= 1
        return curr
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        dummy = ListNode(-1,head)
        prevGroup = dummy

        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                break


            nextGroup = kth.next
            # node that should be next prevGroup
            tmp = prevGroup.next
            kth.next = None

            prevGroup.next = self.reverseList(prevGroup.next, nextGroup)

            prevGroup = tmp
        
        return dummy.next
            
