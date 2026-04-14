class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_sub = 0
        l = r = 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            l_sub = max(l_sub, r - l + 1)
            r += 1
        return l_sub