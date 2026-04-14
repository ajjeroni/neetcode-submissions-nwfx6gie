class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f_map = {}
        maxLen = 0
        l = r = 0
        maxFreq = 0
        while r < len(s):
            f_map[s[r]] = f_map.get(s[r],0) + 1
            maxFreq = max(maxFreq,f_map[s[r]])

            if r-l+1 - maxFreq > k:
                f_map[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, (r-l+1))
            r += 1
        return maxLen