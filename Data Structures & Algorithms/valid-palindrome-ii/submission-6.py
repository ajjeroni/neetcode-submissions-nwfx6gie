class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(l, r):
            if len(s) == 1:
                return True

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True


        l, r = 0, len(s) - 1
        left = True
        right = True

        while l < r:
            if s[l] != s[r]:
                left = checkPalindrome(l, r - 1)
                right = checkPalindrome(l + 1, r)
                if left or right:
                    return True
                else:
                    return False
            l += 1
            r -= 1

        return True

    