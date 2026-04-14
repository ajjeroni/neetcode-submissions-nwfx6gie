import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and self.minHeap[0] < num:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > len(self.maxHeap):
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        else:
            heapq.heappush(self.maxHeap, -num)
            if len(self.maxHeap) - len(self.minHeap) > 1:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            print("min heap: ", self.minHeap[0])
            print("max heap: ", self.maxHeap[0])
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            # print("min heap: ", self.minHeap[0])
            # print("max heap: ", self.maxHeap[0])
            return float(-self.maxHeap[0])
        
        