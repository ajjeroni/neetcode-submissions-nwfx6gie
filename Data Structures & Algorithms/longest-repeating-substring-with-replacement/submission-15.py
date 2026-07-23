class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxChar = 0
        length = 0
        charMap = {}

        l = r = 0

        while r < len(s):
            char = s[r]
            charMap[char] = charMap.get(char, 0) + 1
            maxChar = max(maxChar, charMap[char])

            if (r - l + 1) - maxChar > k:
                charMap[s[l]] -= 1
                l += 1

            length = max(length, r - l + 1)
            r += 1

        return length