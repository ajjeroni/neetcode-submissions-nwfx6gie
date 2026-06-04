class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        left = True
        right = True

        while l < r:
            if s[l] != s[r]:
                print(s[l:r])
                print(s[l+1:r+1])
                left = self.checkPalindrome(s[l:r])
                right = self.checkPalindrome(s[l+1:r+1])
                if left or right:
                    return True
                else:
                    return False
            l += 1
            r -= 1

        return True

        
    def checkPalindrome(self, s):
        if len(s) == 1:
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True