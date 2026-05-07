# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        tail = None
        curr = head
        while head:
            head = head.next
            curr.next = tail
            tail = curr
            curr = head
        return tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        dummy = curr = ListNode(next=head)
        

        while curr.next:
            # start by getting the bounds 
            first = curr.next
            last = curr
            for _ in range(k):
                last = last.next
                if not last:
                    return dummy.next
                
            print(first.val, last.val)

            # send the bounds to get cut and reversed
            nextStart = last.next

            curr.next = None
            last.next = None
            
            newFirst = self.reverseList(first)
            curr.next = newFirst
            first.next = nextStart

            curr = first 
        
        return dummy.next











