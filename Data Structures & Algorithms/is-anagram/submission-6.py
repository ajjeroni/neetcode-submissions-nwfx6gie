class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        balance = [0] * 26

        for char in s:
            balance[ord(char) - ord('a')] += 1
        for char in t:
            balance[ord(char) - ord('a')] -= 1
        
        for i in balance:
            if i != 0: return False
        
        return True