class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''
        for c in s:
            if c.isalnum():
                string += c.lower()
        print(string)
        L, R = 0, len(string) - 1

        while L < R:
            if string[L] == string[R]:
                L += 1
                R -= 1
            else:
                return False
        return True