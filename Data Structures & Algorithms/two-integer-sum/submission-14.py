class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_i = {}

        for i,num in enumerate(nums):
            num_to_i[num] = i
        
        for i,num in enumerate(nums):
            if (target - num) in num_to_i and i != num_to_i[target - num]:
                return [i, num_to_i[target - num]]

