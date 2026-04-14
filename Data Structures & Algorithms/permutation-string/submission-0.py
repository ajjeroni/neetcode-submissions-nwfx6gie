class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        len_s1, len_s2 = len(s1), len(s2)
        count_s1, count_s2 = [0] * 26, [0] * 26

        for char in s1:
            count_s1[ord(char) - ord('a')] += 1
        
        l = r = 0

        while r < len_s2:
            count_s2[ord(s2[r]) - ord('a')] += 1

            if (r-l+1) == len_s1:
                if count_s1 == count_s2:
                    return True
                count_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            r += 1
        return False