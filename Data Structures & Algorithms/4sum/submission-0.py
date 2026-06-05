class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # brute force
        res = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        summ = nums[i] + nums[j] + nums[k] + nums[l]
                        if summ == target:
                            arr = [nums[i],nums[j],nums[k],nums[l]]
                            arr.sort()
                            tup = tuple(arr)
                            res.add(tup)
        
        return [list(x) for x in res]
