class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in p_map:
                stack.append(c)
            else:
                if stack and p_map[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return not stack