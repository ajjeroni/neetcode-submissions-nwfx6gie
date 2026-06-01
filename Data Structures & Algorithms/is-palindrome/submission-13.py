class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
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