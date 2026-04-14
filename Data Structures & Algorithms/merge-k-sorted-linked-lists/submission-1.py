# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class heapNode:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 

        dummy = curr = ListNode()
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                node = heapNode(lists[i])
                heapq.heappush(heap, node)
        # print(heap)
        while heap:
            
            top = heapq.heappop(heap)
            if top.node.next:
                new = heapNode(top.node.next)
                heapq.heappush(heap, new)
            curr.next = top.node
            
            curr = curr.next
        return dummy.next













