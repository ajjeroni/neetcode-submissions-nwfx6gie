class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        buckets = [[] for _ in range(len(nums)+1)]
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        for num in freq:
            buckets[freq[num]].append(num)
        most_freq = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                most_freq.append(num)
            if len(most_freq) == k:
                return most_freq
            
