class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        balance = [0] * 26

        for i in range(len(s)):
            balance[ord(s[i]) - ord('a')] += 1
            balance[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
            if balance[i] != 0:
                return False
        
        return True

