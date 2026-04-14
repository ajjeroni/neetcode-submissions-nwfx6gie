class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count_freq = Counter(nums)
        print(count_freq)
        
        for num,freq in count_freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if heap[0][0] < freq:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, num))
            print(num, ':', freq)
            print(heap)
        print(heap)
        res = []
        for item in heap:
            res.append(item[1])

        return res