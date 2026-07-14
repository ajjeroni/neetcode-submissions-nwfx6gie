# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def findMid(curr):
            slow = fast = curr

            while fast and fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            
            return slow

        def reverseList(curr):
            
            prv = None

            while curr:
                nxt = curr.next
                curr.next = prv
                prv = curr
                curr = nxt

            return prv
        
        def printList(curr):
            toPrint = []
            while curr:
                toPrint.append(curr.val)
                curr = curr.next
            return toPrint
        
        mid = findMid(head)
        end = mid.next
        mid.next = None
        head2 = reverseList(end)

                                    # [2, 4]
                                    # [8, 6]
        # 2 -> 4 -> 6 <- 8          ==> 2 -> 8 -> 4 -> 6

                                    # [2, 4, 6]
                                    # [10, 8]
        # 2 -> 4 -> 6 <- 8 <- 10    ==> 2 -> 10 -> 4 -> 8 -> 6
        while head2:
            nxt = head.next
            nxt2 = head2.next

            head.next = head2
            head2.next = nxt

            head = nxt
            head2 = nxt2

        

        





            