# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next: return 

        def reverseList(head):
            prev = None
            while head:
                ahead = head.next
                head.next = prev
                prev = head 
                head = ahead
            return prev

        def findMid(head):
            # odd - mid
            # even - right mid
            slow = fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow 

        l, r = head, reverseList(findMid(head))
        le = l
        ri = r
        left = []
        right = []
        while le:
            left.append(le.val)
            le = le.next
        while ri:
            right.append(ri.val)
            ri = ri.next
        print("left:",left)
        print("right:",right)
        while l.next and r.next:
            l_nxt = l.next
            l.next = r
            l = l_nxt

            r_nxt = r.next
            r.next = l
            r = r_nxt
        

    
