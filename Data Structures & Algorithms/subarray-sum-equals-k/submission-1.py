class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        summ = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            summ += num
            diff = summ - k

            if diff in prefixSums:
                res += prefixSums[diff]
            
            prefixSums[summ] = prefixSums.get(summ, 0) + 1
        return res