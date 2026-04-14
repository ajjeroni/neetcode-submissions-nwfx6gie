class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_1 = [0] * 26
        count_2 = [0] * 26
        for char in s1:
            count_1[ord(char) - ord('a')] += 1
        l = r = 0
        while r < len(s2):
            count_2[ord(s2[r]) - ord('a')] += 1
            if (r-l+1) == len(s1):
                if count_1 == count_2:
                    return True
                count_2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            r += 1
        return False