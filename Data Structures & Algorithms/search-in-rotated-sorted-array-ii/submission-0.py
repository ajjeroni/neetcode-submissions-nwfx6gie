class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1: return nums[0] == target

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target or nums[l] == target:
                return True
            elif nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1

        return False