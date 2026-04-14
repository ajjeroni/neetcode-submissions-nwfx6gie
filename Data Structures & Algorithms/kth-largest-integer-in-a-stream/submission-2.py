import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        print(self.heap)
        

    def add(self, val: int) -> int:
        pass
        # if self.heap and self.heap[0] < val:
        #     heapq.heappop(self.heap)
        #     heapq.heappush(self.heap, val)
        # return self.heap[0] if self.heap 
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]



    # 2, [1]
    # add - [0] -> [1, 0]
    # add - [2] -> [2, 1]
