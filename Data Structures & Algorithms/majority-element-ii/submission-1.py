class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []

        for num in nums:
            if num in seen:
                continue
            count = sum(1 for i in nums if i == num)

            if count > len(nums) // 3:
                res.append(num)
            seen.add(num)
        return res