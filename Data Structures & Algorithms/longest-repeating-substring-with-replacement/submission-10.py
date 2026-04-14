class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # substring length - most frequency <= K
        # expand window 
        # else slide window

        most_freq = l = r = max_l = 0
        freq = {}

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            most_freq = max(most_freq, freq[s[r]])

            if ((r-l+1) - most_freq) > k:
                freq[s[l]] -= 1
                l += 1
            max_l = max(max_l, r-l+1)
            r += 1
        return max_l