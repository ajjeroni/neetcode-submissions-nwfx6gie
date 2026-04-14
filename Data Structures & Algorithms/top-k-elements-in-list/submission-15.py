class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            bucket[freq[num]].append(num)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) == k:
                    return result
            