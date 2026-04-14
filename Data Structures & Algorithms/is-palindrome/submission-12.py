class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        def isAlNumChar(c):
            if 97 <= ord(c) <= 122:
                return True
            elif 65 <= ord(c) <= 90:
                return True
            elif 48 <= ord(c) <= 57:
                return True
            else:
                return False
        
        l, r = 0, len(s) - 1
        while l < r:
            while not isAlNumChar(s[l]) and l < r:
                l += 1
            while not isAlNumChar(s[r]) and l < r:
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True




