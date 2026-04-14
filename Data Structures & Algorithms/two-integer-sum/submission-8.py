class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            seen[nums[i]] = i
        print(seen)
        for i,num in enumerate(nums):
            comp = target - nums[i]
            if comp in seen and i != seen[comp]:
                return [i, seen[comp]]
                