class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                string = []
                while stack and stack[-1] != '[':
                    string.append(stack.pop())
                stack.pop()
                string = ''.join(string[::-1])

                k = []
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                k = int(''.join(k[::-1]))

                for i in range(k):
                    stack.append(string)
        return ''.join(stack)