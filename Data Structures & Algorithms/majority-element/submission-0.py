class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        seen = {}
        maxx = nums[0]
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if count < seen[num]:
                maxx = num
                count = seen[num]
        
        return maxx

        
        
