# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val


class NodeHeap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, node)

    def pop(self):
        return heapq.heappop(self.heap)
    
    def peek(self):
        return self.heap[0] if self.heap else None

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None
        
        dummy = curr = ListNode()
        heap = NodeHeap()

        for l in lists:
            if l:
                heap.push(l)
        
        while heap.heap:
            node = heap.pop()
            
            if node.next:
                heap.push(node.next)
                node.next = None
            
            curr.next = node
            curr = curr.next
        
        return dummy.next
            

            



