class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minn = 0
        seen = set()
        for num in nums:
            if num < 0 or num in seen:
                continue
            seen.add(num)
            minn = min(minn, num)
        # print(seen)

        nextNum = minn + 1
        while nextNum in seen:
            nextNum += 1

        
        return nextNum