class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i, num in enumerate(nums):
            if 0 < num:
                break
            elif 0 < i and num == nums[i - 1]:
                continue
            else:
                L, R = i + 1, len(nums) - 1
                comp = 0 - num
                while L < R:
                    if nums[L] + nums[R] < comp:
                        L += 1 
                    elif nums[L] + nums[R] > comp:
                        R -= 1
                    else:
                        ret.append([num, nums[L], nums[R]])
                        L += 1
                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
                        R -= 1
        return ret
