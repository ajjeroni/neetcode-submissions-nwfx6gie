class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num,count in freq.items():
            buckets[count].append(num)
        
        res = []
        for i in range(len(buckets)-1,0,-1):
            if not buckets[i]:
                continue
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res



