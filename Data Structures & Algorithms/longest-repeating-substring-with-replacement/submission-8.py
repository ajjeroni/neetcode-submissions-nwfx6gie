class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = max_len = high_freq = 0
        freq = {}
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            high_freq = max(high_freq, freq[s[r]])
            if ((r-l+1) - high_freq) > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, (r-l+1))
            r += 1
        return max_len