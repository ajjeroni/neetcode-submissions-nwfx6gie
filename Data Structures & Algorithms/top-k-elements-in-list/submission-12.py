class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1) ]
        numFreq = {}
        for num in nums:
            numFreq[num] = numFreq.get(num, 0) + 1
        for num in numFreq:
            buckets[numFreq[num]].append(num)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
            if len(result) == k:
                return result
