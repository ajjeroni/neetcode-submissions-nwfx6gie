# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class nodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return other.node.val > self.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        minHeap = []
        dummy = curr = ListNode()
        
        for node in lists:
            if not node: continue
            node = nodeWrapper(node)
            heapq.heappush(minHeap, node)

        while minHeap:
            node = heapq.heappop(minHeap).node
            
            curr.next = node
            curr = curr.next

            if node.next:
                nextNode = nodeWrapper(node.next)
                heapq.heappush(minHeap, nextNode)
        
        return dummy.next









        
        