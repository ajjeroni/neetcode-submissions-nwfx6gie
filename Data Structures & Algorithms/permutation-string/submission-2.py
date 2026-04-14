class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_id = [0] * 26
        s2_id = [0] * 26
        for c in s1:
            s1_id[ord(c)-ord('a')] += 1
        l = r = 0
        while r < len(s2):
            s2_id[ord(s2[r])-ord('a')] += 1
            if r-l+1 == len(s1):
                if s1_id == s2_id:
                    return True
                s2_id[ord(s2[l])-ord('a')] -= 1
                l += 1
            r += 1
        return False