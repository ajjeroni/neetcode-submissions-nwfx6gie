# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        last = head
        dummy = None
        tail = head
        while head:
            head = head.next
            tail.next = dummy
            dummy = tail
            tail = head
        return [dummy,last]
            
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # use a list
        # check multiple of k 
        # store the heads 
        

        if k == 1:
            return head

        holder = []
        tail = head
        lead = head
        count = 1
        dummy = ListNode(-1,head)
        # how do we iterate k times through a linked list?
        while tail and tail.next:
            tail = tail.next
            count += 1
            if count == k:
                holder.append(lead)
                lead = tail.next
                tail.next = None
                tail = lead
                count = 1
        
        for i in range(len(holder)):
            holder[i] = self.reverseList(holder[i])
        
        holder.append([None])
        for i in range(0, len(holder)-1):
            holder[i][1].next = holder[i+1][0]
        
        holder[-2][1].next = lead

        return holder[0][0]
            
        
        
        

        

        
            



            
        
