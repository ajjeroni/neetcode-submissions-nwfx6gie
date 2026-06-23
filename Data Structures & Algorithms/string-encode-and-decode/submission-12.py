class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        # delimiter
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append('#')
            res.append(string)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        # two-pointer approach 
        res = []
        l = 0
        while l < len(s):
            r = l 
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            # print(length)
            string = s[r+1:r+1+length]
            # print(string)
            res.append(string)
            l = r + 1 + length
        return res


