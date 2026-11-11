class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0':
            return b
        if b == '0':
            return a

        bi = 1
        a_sum = 0
        for i in range(len(a) - 1, -1, -1):
            a_sum += bi * int(a[i])
            bi *= 2
        
        bi = 1
        b_sum = 0
        for j in range(len(b) - 1, -1, -1):
            b_sum += bi * int(b[j])
            bi *= 2
        
        summ = a_sum + b_sum
        
        res = []
        while summ > 0:
            res.append(str(summ % 2))
            summ = summ // 2

        return ''.join(reversed(res))

