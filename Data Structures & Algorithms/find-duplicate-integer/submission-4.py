class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n + 1
        # n = 5
        # 6
        # [1 - 5]
        if len(nums) == 2:
            return 1

        slow = fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        trail = 0
        while True:
            slow = nums[slow]
            trail = nums[trail]
            if slow == trail:
                return slow
