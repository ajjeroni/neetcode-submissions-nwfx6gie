# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        count1 = 0
        num2 = 0
        count2 = 0
        carry = 1

        curr = l1
        while curr:
            num1 += carry * curr.val
            carry *= 10
            count1 += 1
            curr = curr.next
        
        carry = 1
        curr = l2
        while curr:
            num2 += carry * curr.val
            carry *= 10
            count2 += 1
            curr = curr.next
        
        summ = num1 + num2

        if summ == 0:
            return l1

        head = curr = l1 if count1 >= count2 else l2
        dummy = ListNode()
        dummy.next = head
        num = summ % 10
        summ = summ // 10

        while curr:
            curr.val = num
            num = summ % 10
            summ = summ // 10
            curr = curr.next
            dummy = dummy.next
        
        curr = dummy 
        while num > 0:
            curr.next = ListNode(num)
            num = summ % 10
            summ = summ // 10
            curr = curr.next
        
        return head



