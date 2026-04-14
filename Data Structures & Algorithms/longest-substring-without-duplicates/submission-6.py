class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_l = l = r = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_l = max(max_l,r-l+1)
            r += 1
        return max_l