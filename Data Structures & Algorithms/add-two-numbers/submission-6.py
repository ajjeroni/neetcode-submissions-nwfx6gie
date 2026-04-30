# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fNum = 0
        sNum = 0

        t1 = l1
        t2 = l2
        place = 0
        while t1 or t2:
            if t1:
                fNum += t1.val * (10 ** place)
            
            if t2:
                sNum += t2.val * (10 ** place)
            
            t1 = t1.next if t1 else None
            t2 = t2.next if t2 else None
            place += 1
        
        sumNum = fNum + sNum 
        if sumNum == 0:
            return l1
        head = trail = ListNode(-1)
        while sumNum > 0:
            digit = sumNum % 10
            newNode = ListNode(digit)
            trail.next = newNode
            trail = trail.next
            sumNum -= digit
            sumNum //= 10
        return head.next

        

            
            