class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lgLen = 0
        l = r = 0
        seen = {}
        maxChar = 0

        while r < len(s):
            seen[s[r]] = seen.get(s[r], 0) + 1
            maxChar = max(maxChar, seen[s[r]])
            # currLen = r - l + 1

            while ((r - l + 1) - maxChar) > k:
                seen[s[l]] -= 1
                l += 1

            lgLen = max(lgLen, r - l + 1)
            r += 1
        return lgLen