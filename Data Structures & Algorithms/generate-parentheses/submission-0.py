class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ret = []

        def rec(op, cl):
            if op == cl == n:
                ret.append("".join(stack))       
                return
            if op < n:
                stack.append('(')
                rec(op + 1, cl)
                stack.pop()
            if cl < op:
                stack.append(')')
                rec(op, cl + 1)
                stack.pop()
        rec(0,0)
        return ret

