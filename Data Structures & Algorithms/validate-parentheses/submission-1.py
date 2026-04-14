class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False
        stack = []
        #insert into the stack if its an opening bracket
        #traverse through the stack popping 
        #if the bracket is a closing bracket
        #if it is check if the stack has that opening bracket
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')': 
                if len(stack) == 0:
                    return False
                elif '(' != stack.pop():
                    return False
            elif s[i] == '}':
                if len(stack) == 0:
                    return False
                elif '{' != stack.pop():
                    return False
            elif s[i] == ']':
                if len(stack) == 0:
                    return False
                elif '[' != stack.pop():
                    return False
        if len(stack) > 0:
            return False
             
        return True