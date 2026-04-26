# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMid(self, head):
        slow = fast = head
        dummy = ListNode(-1,head)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            dummy = dummy.next
        return [slow, dummy]
    def reverseList(self, head):
        tail = None
        tmp = head
        while head:
            head = head.next
            tmp.next = tail
            tail = tmp
            tmp = head
        return tail
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid - first mid
        #split
        #reverse second half
        #weave them together
        if not head.next:
            return 

        firstMid = self.findMid(head)[0]
        beforeFirstMid = self.findMid(head)[1]
        print(firstMid.val)
        print(beforeFirstMid.val)
        beforeFirstMid.next = None
        print('/-----------------/')
        nextHalf = self.reverseList(firstMid)
        tmp = head
        while tmp:
            print(tmp.val)
            tmp = tmp.next
            
        print('/-----------------/')
        tmp = nextHalf
        while tmp:
            print(tmp.val)
            tmp = tmp.next
        while head:
            hTmp = head.next
            nTmp = nextHalf.next
            head.next = nextHalf
            if hTmp:
                nextHalf.next = hTmp
            head = hTmp
            nextHalf = nTmp
        
        




