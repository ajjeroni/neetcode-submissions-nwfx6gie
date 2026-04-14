class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''
        for string in strs:
            ret += str(len(string)) + '#' + string
        print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        ret = []
        L = 0
        while L < len(s):
            R = L 
            while s[R] != '#':
                R += 1
            length = int(s[L: R])
            ret.append(s[R + 1: R + length + 1])
            L = R + length + 1
        return ret