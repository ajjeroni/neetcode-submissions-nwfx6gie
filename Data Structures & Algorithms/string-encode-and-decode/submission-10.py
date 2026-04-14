class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += str(len(string)) + '#' + string
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            string = s[r+1:r+1+length]
            decoded.append(string)
            l = r+1+length
        return decoded
