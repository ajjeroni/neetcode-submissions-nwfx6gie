# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # get the start and the end
        # reverse
        # connect start to new head
        # connect new end to end
        if left == right:
            return head

        dummy = leftNode = rightNode = ListNode()
        dummy.next = head

        while right > 0:
            rightNode = rightNode.next
            right -= 1
        
        while left > 1:
            leftNode = leftNode.next
            left -= 1
        
        end = rightNode.next
        rightNode.next = None

        start = leftNode
        leftNode = leftNode.next
        start.next = None
        

        while leftNode:
            tmp = leftNode.next
            leftNode.next = end
            end = leftNode
            leftNode = tmp

        start.next = end

        return dummy.next


    


        
        

        





        