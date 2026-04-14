class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # len of sub string - max freq <= k
        lg = l = 0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0 ) + 1
            if (r - l + 1) - max(freq.values()) <= k:
                lg = max(lg, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1
        return lg