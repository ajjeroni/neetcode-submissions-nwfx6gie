class Solution:
    
    def isPalindrome(self, s: str) -> bool:

        def my_isalnum(s):
            if not s:
                return False
            for c in s:
                ascii_val = ord(c)
                if 97 <= ascii_val <= 122:
                    continue
                if 65 <= ascii_val <= 90:
                    continue
                if 48 <= ascii_val <= 57:
                    continue
                return False
            return True

            


        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not my_isalnum(s[l]):
                l += 1
            while l < r and not my_isalnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True 

