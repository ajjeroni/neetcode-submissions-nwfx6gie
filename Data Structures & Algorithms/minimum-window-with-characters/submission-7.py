# from collections import defaultdict 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT = {}
        window = {}
        
        l = r = 0
        res, resLen = [-1, -1], float('inf')

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        

        have, need = 0, len(countT)

        while r < len(s):
            if s[r] in countT:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == countT[s[r]]:
                    have += 1
            
            while have == need and l <= r:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                if s[l] in countT:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
                
            r += 1

        l, r = res
        return s[l: r + 1]
        





