class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            
            L, R = i + 1, len(nums) - 1
            a = 0 - num
            while L < R:
                if nums[L] + nums[R] < a:
                    L += 1
                elif nums[L] + nums[R] > a:
                    R -= 1
                else:
                    results.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        return results