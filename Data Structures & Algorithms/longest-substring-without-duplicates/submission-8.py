class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = r = 0
        maxLen = 0
        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            maxLen = max(maxLen,(r-l+1))
            r += 1
        return maxLen