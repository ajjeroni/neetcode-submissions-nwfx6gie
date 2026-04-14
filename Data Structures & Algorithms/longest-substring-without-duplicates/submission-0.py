class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        length = 0
        L = 0
        for R in range(len(s)):
            while s[R] in c:
                c.remove(s[L])
                L += 1
            c.add(s[R])
            length = max(length, R - L + 1)
        return length