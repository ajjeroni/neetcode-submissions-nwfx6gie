class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        l = longest = 0
        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l += 1
            c.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        return longest
