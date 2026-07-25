# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            num = guess(m)
            if num == 0:
                return m
            elif num == -1:
                # num > pick
                r = m - 1
            else:
                # num < pick
                l = m + 1