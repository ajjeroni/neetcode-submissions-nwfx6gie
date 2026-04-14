import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while heap:
            if len(heap) == 1:
                return -heapq.heappop(heap)
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            # if a - b == 0:
            #     continue
            heapq.heappush(heap, -(a - b))
