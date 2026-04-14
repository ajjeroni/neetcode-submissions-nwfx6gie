class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        id_s1 = [0] * 26
        id_s2 = [0] * 26
        for c in s1:
            id_s1[ord(c) - ord('a')] += 1
        l = r = 0
        while r < len(s2):
            id_s2[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) == len(s1):
                if id_s2 == id_s1:
                    return True
                id_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            r += 1
        return False