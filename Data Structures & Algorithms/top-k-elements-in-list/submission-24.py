class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count_freq = Counter(nums)
        print(count_freq)
        
        for num,freq in count_freq.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for item in heap:
            res.append(item[1])

        return res