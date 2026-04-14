class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'}':'{', ')':'(', ']':'['}
        stack = []
        for char in s:
            if char not in hmap:
                stack.append(char)
            elif stack and stack[-1] == hmap[char]:
                stack.pop()
            else:
                return False
        return True if not stack else False