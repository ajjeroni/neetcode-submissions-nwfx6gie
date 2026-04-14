class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+' or c == '*':
                a = stack.pop()
                b = stack.pop()
                if c == '+':
                    stack.append(a+b)
                else:
                    stack.append(a*b)
            elif c == '-' or c == '/':
                a = stack.pop()
                b = stack.pop()
                if c == '-':
                    stack.append(b-a)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]