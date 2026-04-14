class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        l = r = 0
        l_sub = 0
        freq = {}
        max_f = 0
        while r < len(s):
            freq[s[r]] = freq.get(s[r],0) + 1
            max_f = max(max_f, freq[s[r]])
            if (r - l + 1) - max_f > k:
                freq[s[l]] -= 1
                l += 1
            l_sub = max(l_sub, (r - l + 1))
            r += 1
        return l_sub