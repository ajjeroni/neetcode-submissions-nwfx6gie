class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedString = []
        for string in strs:
            encodedString.append(str(len(string)))
            encodedString.append('#')
            encodedString.append(string)
        return ''.join(encodedString)
    def decode(self, s: str) -> List[str]:
        print(s)
        l = 0
        strs = []
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            strs.append(s[r + 1: r + length + 1])
            l = r + length + 1
        return strs



