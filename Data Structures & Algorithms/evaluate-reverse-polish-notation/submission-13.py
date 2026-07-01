class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token == '+':
                n1 = nums.pop()
                n2 = nums.pop()
                nums.append(n1 + n2)
            elif token == '-':
                n1 = nums.pop()
                n2 = nums.pop()
                nums.append(n2 - n1)
            elif token == '*':
                n1 = nums.pop()
                n2 = nums.pop()
                nums.append(n1 * n2)
            elif token == '/':
                n1 = nums.pop()
                n2 = nums.pop()
                nums.append(int(n2 / n1))
            else:
                nums.append(int(token))
        return nums[-1]