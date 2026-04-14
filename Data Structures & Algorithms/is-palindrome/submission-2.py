class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum()).lower();
        return self.rec(clean)

    def rec(self, text):
        if len(text) == 1 or text == '':
            return True
        elif text[0] != text[-1]:
            return False

        return self.rec(text[1:len(text) - 1])