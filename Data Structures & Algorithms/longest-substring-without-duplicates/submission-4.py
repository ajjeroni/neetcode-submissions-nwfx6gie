class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = r = max_len = 0
        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            max_len = max(max_len, (r-l+1))
            seen[s[r]] = r
            r += 1
        return max_len