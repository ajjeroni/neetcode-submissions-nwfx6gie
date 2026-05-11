class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        key = [0] * 26
        for char in s1:
            key[ord(char) - ord('a')] += 1
        
        l = r = 0
        seen = [0] * 26
        while r < len(s2):
            seen[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) == len(s1):
                if seen == key:
                    return True
                seen[ord(s2[l]) - ord('a')] -= 1
                l += 1
            r += 1

        return False