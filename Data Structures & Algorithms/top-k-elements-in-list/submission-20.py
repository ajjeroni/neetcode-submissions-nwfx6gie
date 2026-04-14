class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        freqs = {}
        topK = []
        for num in nums:
            freqs[num] = freqs.get(num,0) + 1
        print(freqs)
        for num,freq in freqs.items():
            buckets[freq].append(num)
        print(buckets)
        for i in range(len(buckets)-1,0,-1):
            for j in range(len(buckets[i])-1,-1,-1):
                topK.append(buckets[i][j])
                if len(topK) == k:
                    return topK
            
        