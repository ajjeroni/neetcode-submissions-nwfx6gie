class Solution:
    def simplifyPath(self, path: str) -> str:
        cPath = []
        p = 0
        while p < len(path):
            if path[p] == '/':
                r = p
                while r < len(path) and path[r] == '/':
                    r += 1
                if cPath and cPath[-1] == '/':
                    cPath.pop()
                cPath.append('/')
                p = r
            else:
                r = p
                while r < len(path) and path[r] != '/':
                    r += 1
                if path[p:r] == '..':
                    count = 2
                    while cPath and count > 0:
                        cPath.pop()
                        count -= 1
                elif path[p:r] == '.':
                    p = r
                else:
                    cPath.append(path[p:r])    
                p = r
        print(cPath)
        if len(cPath) > 1 and cPath[-1] == '/':
            cPath.pop()
        
        return ''.join(cPath)