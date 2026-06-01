class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alnum(s[l]):
                l += 1
            while l < r and not self.alnum(s[r]):
                r -= 1
            
            if self.lowercase(s[l]) != self.lowercase(s[r]):
                return False
            
            l += 1
            r -= 1
        
        return True


    def alnum(self, c):
        if not c:
            return False
        
        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
            return True
        
        return False

    def lowercase(self, c):
        if 65 <= ord(c) <= 90:
            return chr(ord(c) + 32)
        
        return c

