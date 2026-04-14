# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        place = 1
        while l1 and l2:
            count += (l1.val + l2.val) * place 
            place *= 10
            l1 = l1.next
            l2 = l2.next
        # print(count)
        while l1:
            count += l1.val * place
            place *= 10
            l1 = l1.next
        while l2:
            count += l2.val * place
            place *= 10
            l2 = l2.next
        if count == 0:
            return ListNode(0)
        # print(count)
        # print(count % 10)
        # print(count // 10)
        dummy = tail = ListNode()
        while count > 0:
            digit = count % 10
            count = count // 10
            node = ListNode(digit)
            tail.next = node 
            tail = tail.next

        return dummy.next
        